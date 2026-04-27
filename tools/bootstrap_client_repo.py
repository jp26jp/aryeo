from __future__ import annotations

import argparse
import json
import keyword
import re
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
SPEC_PATH = REPO_ROOT / "docs" / "api" / "aryeo.json"

INITIATIVE_SLUG = "aryeo-api-client"
PACKAGE_NAME = "aryeo"
PROJECT_NAME = "aryeo"
PROJECT_VERSION = "0.1.0"
DEFAULT_BASE_URL = "https://api.aryeo.com/v1"
DEFAULT_USER_AGENT = "aryeo-python-client"
UUID_EXAMPLE = "00000000-0000-4000-8000-000000000000"
SUPPORTED_HTTP_METHODS = {"GET", "POST", "PUT", "PATCH", "DELETE"}


@dataclass
class Operation:
    """Store the subset of OpenAPI data needed for generation."""

    tag: str
    tag_description: str
    method: str
    path: str
    path_template: str
    summary: str
    doc_path: str
    path_params: list[str]
    has_query_params: bool
    has_payload: bool
    payload_required: bool
    payload_schema: str | None
    response_schema: str | None
    auth_required: bool
    method_name: str = ""


@dataclass(frozen=True)
class ResourceGroup:
    """Represent a generated resource module."""

    tag: str
    description: str
    module_name: str
    class_name: str
    doc_path: str
    operations: list[Operation]


@dataclass(frozen=True)
class AuditSummary:
    """Capture the source-of-truth audit that feeds planning docs."""

    title: str
    version: str
    primary_server: str
    operation_count: int
    tag_count: int
    component_schema_count: int
    protected_operation_count: int
    public_operations: list[str]
    request_content_types: list[str]
    response_content_types: list[str]
    inline_request_bodies: list[str]
    inline_enum_paths: int
    webhooks_present: bool


@dataclass
class AuditAccumulator:
    """Collect audit metadata while parsing the OpenAPI document."""

    request_content_types: Counter[str] = field(default_factory=Counter)
    response_content_types: Counter[str] = field(default_factory=Counter)
    public_operations: list[str] = field(default_factory=list)
    inline_request_bodies: list[str] = field(default_factory=list)
    protected_operation_count: int = 0


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments for the bootstrap command."""

    parser = argparse.ArgumentParser(
        description=(
            "Bootstrap the Aryeo Python client scaffold from " "docs/api/aryeo.json."
        )
    )
    parser.add_argument(
        "--force-curated",
        action="store_true",
        help="Overwrite curated scaffold files in addition to generated files.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the files that would be written without modifying the repo.",
    )
    return parser.parse_args()


def read_spec() -> dict[str, Any]:
    """Load the checked-in OpenAPI wrapper and return its definition payload."""

    wrapper = json.loads(SPEC_PATH.read_text(encoding="utf-8"))
    return wrapper["definition"]


def snake_case(value: str) -> str:
    """Convert arbitrary strings into snake_case identifiers."""

    cleaned = re.sub(r"[^A-Za-z0-9]+", "_", value)
    cleaned = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", cleaned)
    cleaned = re.sub(r"_+", "_", cleaned)
    return cleaned.strip("_").lower()


def pascal_case(value: str) -> str:
    """Convert arbitrary strings into PascalCase identifiers."""

    return "".join(part.capitalize() for part in snake_case(value).split("_"))


def singularize(word: str) -> str:
    """Apply a lightweight singularization pass for naming cleanup."""

    if word.endswith("ies") and len(word) > 3:
        return f"{word[:-3]}y"
    if word.endswith("ses") and len(word) > 3:
        return word[:-2]
    if word.endswith("s") and not word.endswith("ss") and len(word) > 1:
        return word[:-1]
    return word


def sanitize_identifier(value: str) -> str:
    """Make sure generated identifiers are valid Python symbols."""

    identifier = snake_case(value)
    if not identifier:
        identifier = "value"
    if identifier[0].isdigit():
        identifier = f"op_{identifier}"
    if keyword.iskeyword(identifier):
        identifier = f"{identifier}_value"
    return identifier


def schema_label(schema: dict[str, Any]) -> str | None:
    """Return a short human-readable label for a schema reference."""

    if "$ref" in schema:
        return schema["$ref"].rsplit("/", 1)[-1]
    if schema.get("type") == "object":
        properties = sorted(schema.get("properties", {}).keys())
        if not properties:
            return "inline object"
        preview = ", ".join(properties[:5])
        suffix = "..." if len(properties) > 5 else ""
        return f"inline object ({preview}{suffix})"
    if schema.get("type"):
        return str(schema["type"])
    return None


def derive_method_name(summary: str, tag: str) -> str:
    """Build a concise resource-local method name from an operation summary."""

    words = [word.lower() for word in re.findall(r"[A-Za-z0-9]+", summary)]
    if not words:
        return "call"

    removable = set(re.findall(r"[A-Za-z0-9]+", tag.lower()))
    removable.update(singularize(word) for word in list(removable))
    filtered_words: list[str] = [words[0]]
    for word in words[1:]:
        if word in {"a", "an", "the"}:
            continue
        if word in removable:
            continue
        filtered_words.append(word)

    while len(filtered_words) > 1 and filtered_words[-1] in {"a", "an", "the"}:
        filtered_words.pop()

    candidate = sanitize_identifier("_".join(filtered_words))
    return candidate or "call"


def assign_method_names(operations: list[Operation]) -> None:
    """Resolve stable, unique method names inside a resource group."""

    used_names: set[str] = set()
    for operation in operations:
        candidate = derive_method_name(operation.summary, operation.tag)
        if candidate in used_names:
            tail_parts = [
                sanitize_identifier(part)
                for part in operation.path.split("/")
                if part and not part.startswith("{")
            ]
            if tail_parts:
                candidate = f"{candidate}_{tail_parts[-1]}"

        counter = 2
        original_candidate = candidate
        while candidate in used_names:
            candidate = f"{original_candidate}_{counter}"
            counter += 1

        operation.method_name = candidate
        used_names.add(candidate)


def collect_inline_enums(schema: Any, prefix: str = "") -> set[str]:
    """Walk schemas recursively and collect paths that declare inline enums."""

    enum_paths: set[str] = set()
    if not isinstance(schema, dict):
        return enum_paths

    if "enum" in schema and isinstance(schema["enum"], list):
        enum_paths.add(prefix or "<root>")

    properties = schema.get("properties")
    if isinstance(properties, dict):
        for name, child in properties.items():
            child_prefix = f"{prefix}.{name}" if prefix else name
            enum_paths.update(collect_inline_enums(child, child_prefix))

    items = schema.get("items")
    if isinstance(items, dict):
        child_prefix = f"{prefix}[]" if prefix else "[]"
        enum_paths.update(collect_inline_enums(items, child_prefix))

    for composition_key in ("allOf", "anyOf", "oneOf"):
        composition = schema.get(composition_key)
        if isinstance(composition, list):
            for index, child in enumerate(composition):
                child_prefix = (
                    f"{prefix}.{composition_key}[{index}]"
                    if prefix
                    else f"{composition_key}[{index}]"
                )
                enum_paths.update(collect_inline_enums(child, child_prefix))

    return enum_paths


def get_tag_descriptions(spec: dict[str, Any]) -> dict[str, str]:
    """Map OpenAPI tag names to their cleaned descriptions."""

    return {
        tag_entry["name"]: str(tag_entry.get("description", "")).strip()
        for tag_entry in spec.get("tags", [])
    }


def parse_path_parameters(
    parameters: list[dict[str, Any]],
    path: str,
) -> tuple[list[str], str]:
    """Collect sanitized path parameter names and the formatted path template."""

    path_params: list[str] = []
    path_template = path
    for parameter in parameters:
        if parameter.get("in") != "path":
            continue

        raw_name = str(parameter["name"])
        sanitized_name = sanitize_identifier(raw_name)
        path_params.append(sanitized_name)
        path_template = path_template.replace(
            "{" + raw_name + "}",
            "{" + sanitized_name + "}",
        )

    return path_params, path_template


def has_query_parameters(parameters: list[dict[str, Any]]) -> bool:
    """Return whether an operation declares any query parameters."""

    return any(parameter.get("in") == "query" for parameter in parameters)


def summarize_request_body(
    method: str,
    path: str,
    request_body: dict[str, Any],
    audit: AuditAccumulator,
) -> tuple[bool, bool, str | None]:
    """Capture request body metadata and update audit counters."""

    content = request_body.get("content", {})
    if not isinstance(content, dict) or not content:
        return False, False, None

    payload_required = bool(request_body.get("required", False))
    payload_schema_name: str | None = None
    for content_type, content_schema in content.items():
        audit.request_content_types[content_type] += 1
        schema = content_schema.get("schema", {})
        payload_schema_name = payload_schema_name or schema_label(schema)
        if "$ref" not in schema:
            audit.inline_request_bodies.append(f"{method} {path}")

    return True, payload_required, payload_schema_name


def summarize_response_schema(
    responses: dict[str, Any],
    audit: AuditAccumulator,
) -> str | None:
    """Capture response content-type metadata and first success schema label."""

    response_schema_name: str | None = None
    for status_code, response in responses.items():
        content = response.get("content", {})
        if not isinstance(content, dict):
            continue

        for content_type, content_schema in content.items():
            audit.response_content_types[content_type] += 1
            if status_code.startswith("2") and response_schema_name is None:
                response_schema_name = schema_label(content_schema.get("schema", {}))

    return response_schema_name


def record_operation_visibility(
    method: str,
    path: str,
    auth_required: bool,
    audit: AuditAccumulator,
) -> None:
    """Record whether an operation is public or protected."""

    if auth_required:
        audit.protected_operation_count += 1
        return

    audit.public_operations.append(f"{method} {path}")


def build_operation_record(
    method: str,
    path: str,
    operation: dict[str, Any],
    tag_descriptions: dict[str, str],
    audit: AuditAccumulator,
) -> tuple[str, Operation]:
    """Parse one OpenAPI operation into the generator's runtime record."""

    tag = operation.get("tags", ["Untagged"])[0]
    summary = str(operation.get("summary", operation.get("operationId", path)))
    parameters = operation.get("parameters", [])
    path_params, path_template = parse_path_parameters(parameters, path)
    has_payload, payload_required, payload_schema = summarize_request_body(
        method,
        path,
        operation.get("requestBody", {}),
        audit,
    )
    response_schema = summarize_response_schema(
        operation.get("responses", {}),
        audit,
    )
    auth_required = bool(operation.get("security"))
    record_operation_visibility(method, path, auth_required, audit)

    module_name = snake_case(tag)
    return tag, Operation(
        tag=tag,
        tag_description=tag_descriptions.get(tag, ""),
        method=method,
        path=path,
        path_template=path_template,
        summary=summary.rstrip("."),
        doc_path=f"docs/api/reference/{module_name.replace('_', '-')}.md",
        path_params=path_params,
        has_query_params=has_query_parameters(parameters),
        has_payload=has_payload,
        payload_required=payload_required,
        payload_schema=payload_schema,
        response_schema=response_schema,
        auth_required=auth_required,
    )


def build_resource_group(
    tag: str,
    operations: list[Operation],
    tag_descriptions: dict[str, str],
) -> ResourceGroup:
    """Convert grouped operations into a stable resource-group record."""

    assign_method_names(operations)
    module_name = snake_case(tag)
    return ResourceGroup(
        tag=tag,
        description=tag_descriptions.get(tag, ""),
        module_name=module_name,
        class_name=f"{pascal_case(tag)}Resource",
        doc_path=f"docs/api/reference/{module_name.replace('_', '-')}.md",
        operations=operations,
    )


def count_inline_enum_paths(spec: dict[str, Any]) -> int:
    """Count inline enum paths across component schemas."""

    inline_enum_paths: set[str] = set()
    for schema_name, component_schema in (
        spec.get("components", {}).get("schemas", {}).items()
    ):
        inline_enum_paths.update(collect_inline_enums(component_schema, schema_name))

    return len(inline_enum_paths)


def build_audit_summary(
    spec: dict[str, Any],
    resource_groups: list[ResourceGroup],
    audit: AuditAccumulator,
) -> AuditSummary:
    """Assemble the final audit summary from the parsed resource groups."""

    return AuditSummary(
        title=str(spec.get("info", {}).get("title", PROJECT_NAME)),
        version=str(spec.get("info", {}).get("version", PROJECT_VERSION)),
        primary_server=str(spec.get("servers", [{}])[0].get("url", DEFAULT_BASE_URL)),
        operation_count=sum(len(group.operations) for group in resource_groups),
        tag_count=len(resource_groups),
        component_schema_count=len(spec.get("components", {}).get("schemas", {})),
        protected_operation_count=audit.protected_operation_count,
        public_operations=sorted(audit.public_operations),
        request_content_types=sorted(audit.request_content_types.keys()),
        response_content_types=sorted(audit.response_content_types.keys()),
        inline_request_bodies=sorted(set(audit.inline_request_bodies)),
        inline_enum_paths=count_inline_enum_paths(spec),
        webhooks_present=bool(spec.get("webhooks")),
    )


def build_resource_groups(
    spec: dict[str, Any]
) -> tuple[list[ResourceGroup], AuditSummary]:
    """Parse the OpenAPI document into grouped resource metadata."""

    tag_descriptions = get_tag_descriptions(spec)
    grouped_operations: dict[str, list[Operation]] = defaultdict(list)
    audit = AuditAccumulator()

    for path, path_item in spec["paths"].items():
        for method, operation in path_item.items():
            method_name = method.upper()
            if method_name not in SUPPORTED_HTTP_METHODS:
                continue

            tag, operation_record = build_operation_record(
                method_name,
                path,
                operation,
                tag_descriptions,
                audit,
            )
            grouped_operations[tag].append(operation_record)

    resource_groups: list[ResourceGroup] = []
    for tag, operations in grouped_operations.items():
        resource_groups.append(build_resource_group(tag, operations, tag_descriptions))

    resource_groups.sort(key=lambda group: group.tag.lower())
    return resource_groups, build_audit_summary(spec, resource_groups, audit)


def write_text(
    path: Path,
    content: str,
    *,
    overwrite: bool,
    dry_run: bool,
) -> None:
    """Write text content to disk while respecting overwrite and dry-run flags."""

    normalized_content = content.rstrip() + "\n"
    if path.exists() and not overwrite:
        print(f"skip  {path.relative_to(REPO_ROOT)}")
        return

    if dry_run:
        print(f"write {path.relative_to(REPO_ROOT)}")
        return

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(normalized_content, encoding="utf-8")
    print(f"write {path.relative_to(REPO_ROOT)}")


def markdown_table(headers: list[str], rows: list[list[str]]) -> str:
    """Render a simple Markdown table from headers and row values."""

    header_line = "| " + " | ".join(headers) + " |"
    separator_line = "| " + " | ".join("---" for _ in headers) + " |"
    row_lines = ["| " + " | ".join(row) + " |" for row in rows]
    return "\n".join([header_line, separator_line, *row_lines])


def render_pyproject() -> str:
    """Render the canonical pyproject configuration for the library scaffold."""

    return f"""
[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "{PROJECT_NAME}"
version = "{PROJECT_VERSION}"
description = "Typed Python client scaffold for the Aryeo API."
readme = "README.md"
requires-python = ">=3.11"
authors = [{{ name = "Aryeo API Client Maintainers" }}]
dependencies = ["httpx"]

[project.optional-dependencies]
dev = [
  "black",
  "build",
  "coverage[toml]",
  "flake8",
  "isort",
  "mkdocs-material",
  "mkdocstrings[python]",
  "mypy",
  "pip-audit",
  "pytest",
  "pytest-cov",
  "twine",
]

[tool.setuptools]
include-package-data = true

[tool.setuptools.packages.find]
include = ["aryeo", "aryeo.*"]

[tool.setuptools.package-data]
aryeo = ["py.typed"]

[tool.black]
line-length = 88
target-version = ["py311"]

[tool.isort]
profile = "black"
line_length = 88

[tool.flake8]
max-line-length = 88
max-complexity = 10
extend-ignore = ["E203", "W503"]
exclude = [
  ".git",
  "__pycache__",
  ".mypy_cache",
  ".pytest_cache",
  ".venv",
  "build",
  "dist",
  "site",
]

[tool.pytest.ini_options]
addopts = "-ra --strict-config --strict-markers"
testpaths = ["tests"]

[tool.coverage.run]
source = ["aryeo"]
branch = true

[tool.coverage.report]
show_missing = true
skip_covered = false

[tool.mypy]
python_version = "3.11"
strict = true
warn_unused_ignores = true
show_error_codes = true

[tool.pydocstyle]
convention = "google"
"""


def render_gitignore() -> str:
    """Render the default ignore file for local development artifacts."""

    return """
.DS_Store
.coverage
.mypy_cache/
.pytest_cache/
.ruff_cache/
.venv/
__pycache__/
build/
dist/
htmlcov/
site/
*.egg-info/
*.pyc
coverage.xml
"""


def render_manifest() -> str:
    """Render the package manifest."""

    return """
include README.md
include mkdocs.yml
recursive-include aryeo py.typed
recursive-include docs *.md
"""


def render_style_guide() -> str:
    """Render the repo-local style guide."""

    return """
# Style Guide

## Python

- Use Google-style docstrings on public modules, classes, and functions.
- Prefer explicit, thorough type hints over `Any`.
- Keep the shared HTTP behavior in `aryeo/base_client.py`.
- Treat generated resource modules as low-level transport surfaces until typed
  request and response models land.

## Sync Rules

- Update tests, docs, examples, and planning docs whenever the client surface
  changes.
- Treat `docs/api/` and `docs/planning/aryeo-api-client/` as the contract
  sources before changing endpoint behavior.
- Regenerate the client scaffold with `python tools/bootstrap_client_repo.py`
  after meaningful OpenAPI changes.
"""


def render_readme(resource_groups: list[ResourceGroup], audit: AuditSummary) -> str:
    """Render the top-level project README."""

    resource_group_rows = [
        [
            group.tag,
            f"`aryeo/resources/{group.module_name}.py`",
            str(len(group.operations)),
        ]
        for group in resource_groups
    ]
    return f"""
# Aryeo Python Client

This repository bootstraps a typed Python client around the checked-in Aryeo
OpenAPI wrapper in `docs/api/aryeo.json`.

The current baseline includes:

- a sync `httpx` transport layer with auth, timeout, and error handling
- generated resource clients for {audit.tag_count} API tags and
  {audit.operation_count} operations
- planning docs under `docs/planning/{INITIATIVE_SLUG}/`
- repo-local Cursor rules under `.cursor/rules/`
- MkDocs configuration, examples, tests, and GitHub workflow scaffolding

## Current Scope

This scaffold intentionally exposes low-level JSON request and response shapes.
Schema-perfect models, richer pagination helpers, and live parity checks are
deferred to later phases in the planning tree.

## Install

```bash
python -m pip install -e ".[dev]"
python -m pip install -r docs/requirements.txt
```

## Quickstart

```python
from aryeo import AryeoClient

with AryeoClient.from_env() as client:
    orders = client.orders.list(params={{"page": 1, "per_page": 25}})
    listing = client.listings.get("{UUID_EXAMPLE}")
```

Set `ARYEO_API_TOKEN` before using protected operations. Public operations can
be called without a token.

## Regenerate

The generated resource surface can be refreshed from the checked-in spec with:

```bash
python tools/bootstrap_client_repo.py
```

## Docs

- API contract docs: `docs/api/`
- Planning root: `docs/planning/{INITIATIVE_SLUG}/`
- Package reference: `docs/reference/`

## Validation

```bash
black --check --diff --line-length=88 .
isort --check-only --diff --profile=black --line-length=88 .
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
flake8 . --count --exit-zero --max-complexity=10 --max-line-length=88 --statistics
mypy aryeo/ --strict --ignore-missing-imports
pytest --cov=aryeo --cov-report=xml --cov-report=term-missing
mkdocs build --strict
python -m build
python -m twine check dist/*
```

## Resource Groups

{markdown_table(["Tag", "Module", "Operations"], resource_group_rows)}
"""


def render_mkdocs() -> str:
    """Render the MkDocs configuration."""

    return """
site_name: Aryeo Python Client
theme:
  name: material
plugins:
  - search
  - mkdocstrings:
      handlers:
        python:
          options:
            docstring_style: google
            show_root_heading: true
            show_signature_annotations: true
            show_source: false
markdown_extensions:
  - admonition
  - attr_list
  - def_list
  - tables
nav:
  - Home: index.md
  - Getting Started:
      - Installation: getting-started/installation.md
      - Authentication: getting-started/authentication.md
      - Quickstart: getting-started/quickstart.md
  - API Contract:
      - Overview: api/README.md
      - Authentication: api/guides/authentication.md
      - Errors: api/guides/errors.md
      - Pagination: api/guides/pagination.md
      - Reference Index: api/reference/README.md
      - Tag Reference:
          - Addresses: api/reference/addresses.md
          - Appointments: api/reference/appointments.md
          - Company Users: api/reference/company-users.md
          - Customer Users: api/reference/customer-users.md
          - Discounts: api/reference/discounts.md
          - Listings: api/reference/listings.md
          - Notes: api/reference/notes.md
          - Order Forms: api/reference/order-forms.md
          - Order Items: api/reference/order-items.md
          - Orders: api/reference/orders.md
          - Payroll: api/reference/payroll.md
          - Products: api/reference/products.md
          - Scheduling: api/reference/scheduling.md
          - Tags: api/reference/tags.md
          - Tasks: api/reference/tasks.md
          - Videos: api/reference/videos.md
  - Python Reference:
      - Overview: reference/index.md
      - Client: reference/client.md
      - Exceptions: reference/exceptions.md
      - Resources: reference/resources.md
  - Planning:
      - Overview: planning/aryeo-api-client/README.md
      - Artifact Path Index: planning/aryeo-api-client/ARTIFACT_PATH_INDEX.md
      - Foundation:
          - Overview: planning/aryeo-api-client/foundation/README.md
          - API Source Of Truth: planning/aryeo-api-client/foundation/api-source-of-truth.md
          - Source Of Truth Matrix: planning/aryeo-api-client/foundation/source-of-truth-matrix.md
          - Package And Versioning ADR: planning/aryeo-api-client/foundation/package-and-versioning-adr.md
          - Rules And Ownership ADR: planning/aryeo-api-client/foundation/rules-and-ownership-adr.md
      - Trackers:
          - Overview: planning/aryeo-api-client/trackers/README.md
          - Readiness Overview: planning/aryeo-api-client/trackers/readiness-overview.md
          - Endpoint Inventory Readiness: planning/aryeo-api-client/trackers/endpoint-inventory-readiness.md
          - Coverage And Tests Readiness: planning/aryeo-api-client/trackers/coverage-and-tests-readiness.md
          - Live Integration Readiness: planning/aryeo-api-client/trackers/live-integration-readiness.md
          - Docs Parity Readiness: planning/aryeo-api-client/trackers/docs-parity-readiness.md
          - Workflow Release Readiness: planning/aryeo-api-client/trackers/workflow-release-readiness.md
      - Execution:
          - Overview: planning/aryeo-api-client/execution/README.md
          - Execution Plan: planning/aryeo-api-client/execution/execution-plan.md
          - Roadmap: planning/aryeo-api-client/execution/roadmap.md
          - API Client Bootstrap Plan: planning/aryeo-api-client/execution/api-client-bootstrap-plan.md
          - Phase 00 Source Audit: planning/aryeo-api-client/execution/api_client_PHASE_00_source_audit.md
          - Phase 01 Foundation: planning/aryeo-api-client/execution/api_client_PHASE_01_foundation.md
          - Phase 02 Endpoint Inventory: planning/aryeo-api-client/execution/api_client_PHASE_02_endpoint_inventory.md
          - Phase 03 Tests And Coverage: planning/aryeo-api-client/execution/api_client_PHASE_03_tests_and_coverage.md
          - Phase 04 Docs And Examples: planning/aryeo-api-client/execution/api_client_PHASE_04_docs_and_examples.md
          - Phase 05 Workflows And Release: planning/aryeo-api-client/execution/api_client_PHASE_05_workflows_and_release.md
          - Phase 06 Parity Audit: planning/aryeo-api-client/execution/api_client_PHASE_06_parity_audit.md
  - Development:
      - Contributing: development/contributing.md
      - Planning Guide: development/planning.md
"""


def render_docs_requirements() -> str:
    """Render the docs-only requirement list."""

    return """
mkdocs-material
mkdocstrings[python]
"""


def render_docs_index(audit: AuditSummary) -> str:
    """Render the docs site landing page."""

    return f"""
# Aryeo Python Client

This project turns the checked-in Aryeo OpenAPI wrapper into a usable Python
client baseline.

## What Exists

- {audit.operation_count} low-level resource methods generated from
  `docs/api/aryeo.json`
- shared auth, timeout, and error handling in `aryeo/base_client.py`
- package reference pages backed by `mkdocstrings`
- planning docs under `docs/planning/{INITIATIVE_SLUG}/`

## Where To Start

- Read `docs/api/README.md` for the API contract summary.
- Read `docs/reference/client.md` for the Python client surface.
- Read `docs/planning/{INITIATIVE_SLUG}/execution/api-client-bootstrap-plan.md`
  for the active implementation roadmap.
"""


def render_docs_installation() -> str:
    """Render the getting-started installation guide."""

    return """
# Installation

## Runtime Install

```bash
python -m pip install .
```

## Development Install

```bash
python -m pip install -e ".[dev]"
python -m pip install -r docs/requirements.txt
```

The package targets Python 3.11 and newer.
"""


def render_docs_authentication() -> str:
    """Render the client authentication guide."""

    return f"""
# Authentication

Most Aryeo API operations require a bearer token supplied in the
`Authorization` header.

## Environment Variables

- `ARYEO_API_TOKEN`: bearer token used for protected operations
- `ARYEO_BASE_URL`: optional override for the default base URL
- `ARYEO_TIMEOUT`: optional float timeout in seconds

## Client Setup

```python
from aryeo import AryeoClient

client = AryeoClient.from_env()
```

The default base URL is `{DEFAULT_BASE_URL}`.

For the underlying API contract details, see `docs/api/guides/authentication.md`.
"""


def render_docs_quickstart() -> str:
    """Render the quickstart guide."""

    return f"""
# Quickstart

```python
from aryeo import AryeoClient

with AryeoClient.from_env() as client:
    appointments = client.appointments.list(params={{"page": 1}})
    order = client.orders.get("{UUID_EXAMPLE}")
```

The generated resource methods currently return decoded JSON values. Typed
request and response models are tracked as later work in the planning tree.
"""


def render_docs_reference_index() -> str:
    """Render the package reference landing page."""

    return """
# Python Reference

The runtime surface is intentionally split into three layers:

- `aryeo.client.AryeoClient` wires resource clients together.
- `aryeo.base_client.BaseClient` owns transport, auth, and JSON behavior.
- `aryeo.resources.*` exposes low-level endpoint methods grouped by API tag.
"""


def render_docs_reference_client() -> str:
    """Render the client reference page."""

    return """
# Client

::: aryeo.client.AryeoClient
"""


def render_docs_reference_exceptions() -> str:
    """Render the exception reference page."""

    return """
# Exceptions

::: aryeo.exceptions.AryeoError

::: aryeo.exceptions.AryeoConfigurationError

::: aryeo.exceptions.AryeoRequestError

::: aryeo.exceptions.AryeoAPIError
"""


def render_docs_reference_resources(resource_groups: list[ResourceGroup]) -> str:
    """Render the combined resource reference page."""

    sections = []
    for group in resource_groups:
        sections.append(
            "## "
            f"{group.tag}\n\n"
            f"::: aryeo.resources.{group.module_name}.{group.class_name}"
        )
    return "# Resources\n\n" + "\n\n".join(sections) + "\n"


def render_docs_contributing() -> str:
    """Render the contributor guide."""

    return f"""
# Contributing

## Bootstrap

```bash
python tools/bootstrap_client_repo.py
```

## Validation

```bash
black --check --diff --line-length=88 .
isort --check-only --diff --profile=black --line-length=88 .
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
flake8 . --count --exit-zero --max-complexity=10 --max-line-length=88 --statistics
mypy aryeo/ --strict --ignore-missing-imports
pytest --cov=aryeo --cov-report=xml --cov-report=term-missing
mkdocs build --strict
python -m build
python -m twine check dist/*
```

## PyPI Trusted Publishing

GitHub Actions publishes to PyPI through Trusted Publishing with the `pypi`
environment and `id-token: write` permissions, so no long-lived PyPI API token
is required in GitHub.

Before the first live publish, add a PyPI pending publisher for this repository
under `https://pypi.org/manage/account/publishing/`.

- Register `release.yml` if you want tag-based publishing from
  `.github/workflows/release.yml`.
- Register `unified-deployment.yml` as well if you want the manual publish path
  in `.github/workflows/unified-deployment.yml` to work.
- Use the optional environment name `pypi` to match the GitHub workflow jobs.

## Planning

Treat `docs/planning/{INITIATIVE_SLUG}/` as the checked-in implementation
ledger for the scaffold and its follow-on phases.
"""


def render_docs_planning() -> str:
    """Render the development planning guide."""

    return f"""
# Planning

The active planning root for this workstream is:

- `docs/planning/{INITIATIVE_SLUG}/`

Start with these files:

- `README.md`
- `foundation/api-source-of-truth.md`
- `execution/execution-plan.md`
- `execution/api-client-bootstrap-plan.md`
"""


def render_package_init() -> str:
    """Render the package initializer."""

    return f'''
"""Top-level package exports for the Aryeo client."""

from aryeo.client import AryeoClient
from aryeo.exceptions import (
    AryeoAPIError,
    AryeoConfigurationError,
    AryeoError,
    AryeoRequestError,
)

__all__ = [
    "AryeoAPIError",
    "AryeoClient",
    "AryeoConfigurationError",
    "AryeoError",
    "AryeoRequestError",
]

__version__ = "{PROJECT_VERSION}"
'''


def render_types_module() -> str:
    """Render shared JSON and timeout type aliases."""

    return '''
"""Shared type aliases used by the Aryeo client runtime."""

from __future__ import annotations

from typing import TypeAlias

import httpx

JSONScalar: TypeAlias = str | int | float | bool | None
JSONValue: TypeAlias = JSONScalar | dict[str, "JSONValue"] | list["JSONValue"]
JSONMapping: TypeAlias = dict[str, JSONValue]
JSONResponse: TypeAlias = JSONValue

QueryScalar: TypeAlias = str | int | float | bool | None
QueryValue: TypeAlias = QueryScalar | list[QueryScalar] | tuple[QueryScalar, ...]
QueryParams: TypeAlias = dict[str, QueryValue]

RequestTimeoutTuple: TypeAlias = tuple[
    float | None,
    float | None,
    float | None,
    float | None,
]
RequestTimeout: TypeAlias = float | httpx.Timeout | RequestTimeoutTuple | None
'''


def render_exceptions_module() -> str:
    """Render the exception hierarchy for the client."""

    return '''
"""Project-specific exception types for the Aryeo client."""

from __future__ import annotations

import httpx

from aryeo.types import JSONResponse


class AryeoError(Exception):
    """Base exception for all Aryeo client failures."""


class AryeoConfigurationError(AryeoError):
    """Raised when client configuration is insufficient for a request."""


class AryeoRequestError(AryeoError):
    """Raised when the transport fails before a valid API response arrives."""

    def __init__(
        self,
        message: str,
        original_exception: Exception | None = None,
    ) -> None:
        """Initialize a request error wrapper.

        Args:
            message: Human-readable failure summary.
            original_exception: The original lower-level exception, if available.
        """

        super().__init__(message)
        self.original_exception = original_exception


class AryeoAPIError(AryeoError):
    """Raised when the Aryeo API returns a non-success status code."""

    def __init__(
        self,
        status_code: int,
        message: str,
        *,
        api_code: str | None = None,
        api_status: int | str | None = None,
        response_body: JSONResponse | None = None,
    ) -> None:
        """Initialize an API error with parsed response details.

        Args:
            status_code: HTTP status code returned by the API.
            message: Human-readable API failure message.
            api_code: Optional Aryeo-specific error code.
            api_status: Optional status field echoed by the API.
            response_body: Parsed response body, when available.
        """

        parts = [f"HTTP {status_code}", message]
        if api_code:
            parts.append(f"code={api_code}")
        if api_status is not None:
            parts.append(f"status={api_status}")
        super().__init__(" | ".join(parts))
        self.status_code = status_code
        self.message = message
        self.api_code = api_code
        self.api_status = api_status
        self.response_body = response_body

    @classmethod
    def from_response(cls, response: httpx.Response) -> "AryeoAPIError":
        """Create an exception from an `httpx.Response`.

        Args:
            response: The failed HTTP response.

        Returns:
            A populated `AryeoAPIError` instance.
        """

        payload: JSONResponse | None
        try:
            payload = response.json()
        except ValueError:
            payload = response.text or None

        message = response.reason_phrase or "Aryeo API request failed."
        api_code: str | None = None
        api_status: int | str | None = None

        if isinstance(payload, dict):
            payload_message = payload.get("message")
            if isinstance(payload_message, str) and payload_message.strip():
                message = payload_message
            payload_code = payload.get("code")
            if isinstance(payload_code, str):
                api_code = payload_code
            payload_status = payload.get("status")
            if isinstance(payload_status, (int, str)):
                api_status = payload_status

        return cls(
            response.status_code,
            message,
            api_code=api_code,
            api_status=api_status,
            response_body=payload,
        )
'''


def render_base_client_module() -> str:
    """Render the shared HTTP client implementation."""

    return f'''
"""Shared HTTP transport helpers for the Aryeo Python client."""

from __future__ import annotations

from typing import cast

import httpx

from aryeo.exceptions import AryeoAPIError, AryeoConfigurationError, AryeoRequestError
from aryeo.types import JSONMapping, JSONResponse, QueryParams, RequestTimeout

DEFAULT_BASE_URL = "{DEFAULT_BASE_URL}"
DEFAULT_TIMEOUT: float = 30.0
DEFAULT_USER_AGENT = "{DEFAULT_USER_AGENT}"


class BaseClient:
    """Manage auth, transport, and JSON request behavior for Aryeo calls."""

    def __init__(
        self,
        token: str | None = None,
        *,
        base_url: str = DEFAULT_BASE_URL,
        timeout: RequestTimeout = DEFAULT_TIMEOUT,
        user_agent: str = DEFAULT_USER_AGENT,
        http_client: httpx.Client | None = None,
    ) -> None:
        """Initialize the shared client transport.

        Args:
            token: Optional bearer token used for protected operations.
            base_url: Base URL for API requests.
            timeout: Default request timeout.
            user_agent: User-Agent header sent with every request.
            http_client: Optional injected `httpx.Client`.
        """

        self._token = token
        self._base_url = base_url.rstrip("/")
        self._default_timeout = timeout
        self._user_agent = user_agent
        self._owns_http_client = http_client is None
        self._http_client = http_client or httpx.Client()

    @property
    def base_url(self) -> str:
        """Return the configured base URL."""

        return self._base_url

    def close(self) -> None:
        """Close the owned HTTP client when this instance created it."""

        if self._owns_http_client:
            self._http_client.close()

    def __enter__(self) -> "BaseClient":
        """Enter the client context manager."""

        return self

    def __exit__(self, *args: object) -> None:
        """Close the client when leaving a context manager."""

        self.close()

    def _build_headers(self, *, auth_required: bool) -> dict[str, str]:
        """Build per-request headers for the outgoing request.

        Args:
            auth_required: Whether the request requires a bearer token.

        Returns:
            A header mapping for the request.

        Raises:
            AryeoConfigurationError: If auth is required and no token is configured.
        """

        headers = {{
            "Accept": "application/json",
            "User-Agent": self._user_agent,
        }}
        if self._token:
            headers["Authorization"] = f"Bearer {{self._token}}"
        elif auth_required:
            raise AryeoConfigurationError(
                "A bearer token is required for this Aryeo API operation."
            )
        return headers

    def _build_url(self, path: str) -> str:
        """Construct a request URL from the base URL and relative API path."""

        return f"{{self._base_url}}{{path}}"

    def request_json(
        self,
        method: str,
        path: str,
        *,
        params: QueryParams | None = None,
        payload: JSONMapping | None = None,
        timeout: RequestTimeout = None,
        auth_required: bool = True,
    ) -> JSONResponse:
        """Execute a JSON API request and decode the response body.

        Args:
            method: HTTP method to use.
            path: API path that will be joined to the configured base URL.
            params: Optional query string parameters.
            payload: Optional JSON request body.
            timeout: Optional timeout override for this request.
            auth_required: Whether the request must include the bearer token.

        Returns:
            The decoded JSON response body, or `None` for empty responses.

        Raises:
            AryeoAPIError: If the API returns a non-success status code.
            AryeoRequestError: If the transport fails or the body is not JSON.
            AryeoConfigurationError: If auth is required and no token exists.
        """

        try:
            response = self._http_client.request(
                method=method,
                url=self._build_url(path),
                headers=self._build_headers(auth_required=auth_required),
                params=params,
                json=payload,
                timeout=timeout if timeout is not None else self._default_timeout,
            )
        except httpx.HTTPError as exc:
            raise AryeoRequestError("The Aryeo request did not complete.", exc) from exc

        if response.is_error:
            raise AryeoAPIError.from_response(response)

        if response.status_code == 204 or not response.content:
            return None

        try:
            body = cast(JSONResponse, response.json())
        except ValueError as exc:
            raise AryeoRequestError(
                "The Aryeo response body was not valid JSON.",
                exc,
            ) from exc

        return body
'''


def render_resource_base_module() -> str:
    """Render the shared resource mixin."""

    return '''
"""Shared helpers for generated Aryeo resource clients."""

from __future__ import annotations

from aryeo.base_client import BaseClient
from aryeo.types import JSONMapping, JSONResponse, QueryParams, RequestTimeout


class ResourceClient:
    """Wrap the shared `BaseClient` for a specific resource group."""

    def __init__(self, client: BaseClient) -> None:
        """Store the shared base client.

        Args:
            client: The root Aryeo client transport.
        """

        self._client = client

    def _request(
        self,
        method: str,
        path: str,
        *,
        params: QueryParams | None = None,
        payload: JSONMapping | None = None,
        timeout: RequestTimeout = None,
        auth_required: bool = True,
    ) -> JSONResponse:
        """Delegate a JSON request to the shared base client."""

        return self._client.request_json(
            method,
            path,
            params=params,
            payload=payload,
            timeout=timeout,
            auth_required=auth_required,
        )
'''


def render_client_module(resource_groups: list[ResourceGroup]) -> str:
    """Render the top-level client that wires all resource classes together."""

    imports = "\n".join(
        f"from aryeo.resources import {group.class_name}" for group in resource_groups
    )
    annotations = "\n".join(
        f"    {group.module_name}: {group.class_name}" for group in resource_groups
    )
    assignments = "\n".join(
        f"        self.{group.module_name} = {group.class_name}(self)"
        for group in resource_groups
    )
    resource_names = ",\n".join(
        f'    "{group.module_name}"' for group in resource_groups
    )

    return f'''
"""Top-level Aryeo client composed from resource-specific subclients."""

from __future__ import annotations

import os

import httpx

from aryeo.base_client import (
    DEFAULT_BASE_URL,
    DEFAULT_TIMEOUT,
    DEFAULT_USER_AGENT,
    BaseClient,
)
from aryeo.exceptions import AryeoConfigurationError
{imports}
from aryeo.types import RequestTimeout

RESOURCE_NAMES = (
{resource_names}
)


class AryeoClient(BaseClient):
    """Sync Aryeo API client grouped by API tag."""

{annotations}

    def __init__(
        self,
        token: str | None = None,
        *,
        base_url: str = DEFAULT_BASE_URL,
        timeout: RequestTimeout = DEFAULT_TIMEOUT,
        user_agent: str = DEFAULT_USER_AGENT,
        http_client: httpx.Client | None = None,
    ) -> None:
        """Initialize the Aryeo client and its resource bindings.

        Args:
            token: Optional bearer token for protected operations.
            base_url: Base URL for the Aryeo API.
            timeout: Default request timeout.
            user_agent: User-Agent header sent on each request.
            http_client: Optional injected `httpx.Client`.
        """

        super().__init__(
            token,
            base_url=base_url,
            timeout=timeout,
            user_agent=user_agent,
            http_client=http_client,
        )
{assignments}

    @classmethod
    def from_env(
        cls,
        *,
        token_env_var: str = "ARYEO_API_TOKEN",
        base_url_env_var: str = "ARYEO_BASE_URL",
        timeout_env_var: str = "ARYEO_TIMEOUT",
    ) -> "AryeoClient":
        """Build a client from conventional environment variables.

        Args:
            token_env_var: Environment variable containing the bearer token.
            base_url_env_var: Environment variable overriding the base URL.
            timeout_env_var: Environment variable overriding the timeout.

        Returns:
            A configured `AryeoClient` instance.

        Raises:
            AryeoConfigurationError: If the timeout environment variable is invalid.
        """

        timeout_value = os.getenv(timeout_env_var)
        timeout: RequestTimeout = DEFAULT_TIMEOUT
        if timeout_value:
            try:
                timeout = float(timeout_value)
            except ValueError as exc:
                raise AryeoConfigurationError(
                    f"{{timeout_env_var}} must be a float if provided."
                ) from exc

        return cls(
            token=os.getenv(token_env_var),
            base_url=os.getenv(base_url_env_var, DEFAULT_BASE_URL),
            timeout=timeout,
        )


__all__ = ["AryeoClient", "RESOURCE_NAMES"]
'''


def resource_import_list(operations: list[Operation]) -> str:
    """Render the import list needed by one generated resource module."""

    import_names = ["JSONResponse", "RequestTimeout"]
    if any(operation.has_payload for operation in operations):
        import_names.append("JSONMapping")
    if any(operation.has_query_params for operation in operations):
        import_names.append("QueryParams")
    return ", ".join(sorted(import_names))


def resource_signature(operation: Operation) -> str:
    """Build the method signature for a generated resource method."""

    positional_args = [f"{name}: str" for name in operation.path_params]
    keyword_args = []
    if operation.has_query_params:
        keyword_args.append("params: QueryParams | None = None")
    if operation.has_payload:
        payload_type = (
            "JSONMapping" if operation.payload_required else "JSONMapping | None"
        )
        payload_default = "" if operation.payload_required else " = None"
        keyword_args.append(f"payload: {payload_type}{payload_default}")
    keyword_args.append("timeout: RequestTimeout = None")
    return ", ".join(["self", *positional_args, "*", *keyword_args])


def resource_payload_label(operation: Operation) -> str:
    """Return the human-readable payload label for a generated docstring."""

    payload_label = operation.payload_schema or "documented payload"
    if payload_label.startswith("inline object"):
        return "the documented inline object payload"
    return payload_label


def resource_doc_lines(operation: Operation) -> list[str]:
    """Render the docstring lines for a generated resource method."""

    lines = [f'        """{operation.summary}.', "", "        Args:"]
    for path_param in operation.path_params:
        lines.append(f"            {path_param}: The `{path_param}` path value.")
    if operation.has_query_params:
        lines.append(
            "            params: Optional query parameters for the underlying API "
            "call."
        )
    if operation.has_payload:
        lines.append(
            "            payload: JSON payload matching "
            f"{resource_payload_label(operation)}."
        )
    lines.extend(
        [
            "            timeout: Optional per-request timeout override.",
            "",
            "        Returns:",
            "            The decoded JSON payload returned by the API.",
            "",
            "        Raises:",
            "            AryeoAPIError: If the API returns a non-success response.",
            (
                "            AryeoRequestError: If the request fails before "
                "completion."
            ),
            '        """',
        ]
    )
    return lines


def resource_call_arguments(operation: Operation) -> str:
    """Render keyword arguments for the shared resource request helper."""

    call_arguments = []
    if operation.has_query_params:
        call_arguments.append("params=params")
    if operation.has_payload:
        call_arguments.append("payload=payload")
    call_arguments.append("timeout=timeout")
    call_arguments.append(f"auth_required={operation.auth_required}")
    return ", ".join(call_arguments)


def resource_path_literal(operation: Operation) -> str:
    """Render the Python string literal for the request path."""

    if operation.path_params:
        return f'f"{operation.path_template}"'
    return f'"{operation.path}"'


def render_resource_module(group: ResourceGroup) -> str:
    """Render a resource module from grouped operation metadata."""

    method_blocks = "\n\n".join(
        render_resource_method(group, operation) for operation in group.operations
    )
    description = f"Access {group.tag.lower()} API operations."
    import_list = resource_import_list(group.operations)
    return f'''
"""Generated resource client for the {group.tag} API tag."""

from __future__ import annotations

from aryeo.resources._base import ResourceClient
from aryeo.types import {import_list}


class {group.class_name}(ResourceClient):
    """{description}"""

{method_blocks}


__all__ = ["{group.class_name}"]
'''


def render_resource_method(group: ResourceGroup, operation: Operation) -> str:
    """Render a single generated resource method."""

    _ = group
    signature = resource_signature(operation)
    doc_lines = resource_doc_lines(operation)
    path_literal = resource_path_literal(operation)
    call_arguments = resource_call_arguments(operation)
    return "\n".join(
        [
            f"    def {operation.method_name}({signature}) -> JSONResponse:",
            *doc_lines,
            (
                "        return self._request("
                f'"{operation.method}", {path_literal}, {call_arguments})'
            ),
        ]
    )


def render_resources_init(resource_groups: list[ResourceGroup]) -> str:
    """Render the generated resource package initializer."""

    imports = "\n".join(
        f"from aryeo.resources.{group.module_name} import {group.class_name}"
        for group in resource_groups
    )
    exports = ",\n".join(f'    "{group.class_name}"' for group in resource_groups)
    return f'''
"""Generated resource exports for the Aryeo client."""

{imports}

__all__ = [
{exports}
]
'''


def render_examples_quickstart() -> str:
    """Render the quickstart example script."""

    return f'''
"""Quickstart example for the Aryeo client."""

from __future__ import annotations

from aryeo import AryeoClient


def main() -> None:
    """Run a small example against the Aryeo API."""

    with AryeoClient.from_env() as client:
        client.orders.list(params={{"page": 1, "per_page": 5}})
        client.listings.get("{UUID_EXAMPLE}")


if __name__ == "__main__":
    main()
'''


def render_examples_orders() -> str:
    """Render a workflow example focused on orders."""

    return f'''
"""Example workflow for loading orders from Aryeo."""

from __future__ import annotations

from aryeo import AryeoClient


def main() -> None:
    """List the first page of orders and fetch a single payment-info record."""

    with AryeoClient.from_env() as client:
        client.orders.list(params={{"page": 1, "per_page": 10}})
        client.orders.get_payment_information("{UUID_EXAMPLE}")


if __name__ == "__main__":
    main()
'''


def render_tests_init() -> str:
    """Render the tests package initializer."""

    return '"""Test suite for the Aryeo Python client."""\n'


def render_tests_conftest() -> str:
    """Render shared pytest fixtures."""

    return '''
"""Shared fixtures for Aryeo client tests."""

from __future__ import annotations

from collections.abc import Callable, Iterator

import httpx
import pytest

from aryeo.client import AryeoClient
from aryeo.types import JSONResponse

ClientFactory = Callable[
    [str | None, JSONResponse | None, int],
    tuple[AryeoClient, list[httpx.Request]],
]


@pytest.fixture
def client_factory() -> Iterator[ClientFactory]:
    """Yield a factory that returns a mock client and captured requests."""

    clients: list[AryeoClient] = []

    def _factory(
        token: str | None = "test-token",
        response_body: JSONResponse | None = None,
        status_code: int = 200,
    ) -> tuple[AryeoClient, list[httpx.Request]]:
        captured_requests: list[httpx.Request] = []

        def handler(request: httpx.Request) -> httpx.Response:
            captured_requests.append(request)
            if response_body is None and status_code == 204:
                return httpx.Response(status_code, request=request)
            return httpx.Response(
                status_code,
                json=response_body if response_body is not None else {"ok": True},
                request=request,
            )

        client = AryeoClient(
            token=token,
            http_client=httpx.Client(transport=httpx.MockTransport(handler)),
        )
        clients.append(client)
        return client, captured_requests

    yield _factory

    for client in clients:
        client.close()
'''


def render_tests_base_client() -> str:
    """Render the base client unit tests."""

    return '''
"""Unit tests for the shared Aryeo base client."""

from __future__ import annotations

import pytest

from aryeo.exceptions import AryeoConfigurationError


def test_request_json_includes_auth_header(client_factory: object) -> None:
    """Protected requests should include the bearer token."""

    factory = client_factory
    client, requests = factory("token-value")
    response = client.request_json("GET", "/appointments", params={"page": 1})

    assert response == {"ok": True}
    assert requests[0].headers["Authorization"] == "Bearer token-value"
    assert requests[0].url.params["page"] == "1"


def test_request_json_allows_public_requests_without_token(
    client_factory: object,
) -> None:
    """Public endpoints should work when no bearer token is configured."""

    factory = client_factory
    client, requests = factory(None)
    response = client.request_json(
        "GET",
        "/orders/00000000-0000-4000-8000-000000000000/payment-info",
        auth_required=False,
    )

    assert response == {"ok": True}
    assert "Authorization" not in requests[0].headers


def test_request_json_requires_token_for_protected_endpoints(
    client_factory: object,
) -> None:
    """Protected endpoints should fail fast without a token."""

    factory = client_factory
    client, _ = factory(None)

    with pytest.raises(AryeoConfigurationError):
        client.request_json("GET", "/appointments")
'''


def render_tests_client() -> str:
    """Render the top-level client unit tests."""

    return '''
"""Unit tests for the high-level Aryeo client."""

from __future__ import annotations

from aryeo.client import AryeoClient, RESOURCE_NAMES


def test_client_exposes_generated_resources(client_factory: object) -> None:
    """The top-level client should expose each generated resource attribute."""

    factory = client_factory
    client, _ = factory("token-value")

    for resource_name in RESOURCE_NAMES:
        assert hasattr(client, resource_name)


def test_client_from_env_reads_standard_variables(monkeypatch: object) -> None:
    """The convenience constructor should honor the default env var names."""

    monkeypatch.setenv("ARYEO_API_TOKEN", "env-token")
    monkeypatch.setenv("ARYEO_BASE_URL", "https://example.test/api")
    monkeypatch.setenv("ARYEO_TIMEOUT", "12")

    client = AryeoClient.from_env()

    assert client.base_url == "https://example.test/api"
    client.close()
'''


def render_tests_exceptions() -> str:
    """Render the exception unit tests."""

    return '''
"""Unit tests for Aryeo-specific exception types."""

from __future__ import annotations

import httpx

from aryeo.exceptions import AryeoAPIError


def test_api_error_parses_response_payload() -> None:
    """API errors should preserve response metadata when present."""

    request = httpx.Request("GET", "https://example.test")
    response = httpx.Response(
        422,
        json={"status": 422, "message": "Invalid request", "code": "bad_input"},
        request=request,
    )

    error = AryeoAPIError.from_response(response)

    assert error.status_code == 422
    assert error.message == "Invalid request"
    assert error.api_code == "bad_input"
'''


def render_generated_surface_test(resource_groups: list[ResourceGroup]) -> str:
    """Render a parameterized test over all generated resource methods."""

    cases: list[str] = []
    for group in resource_groups:
        for operation in group.operations:
            path_arguments = {
                path_param: UUID_EXAMPLE for path_param in operation.path_params
            }
            call_kwargs: dict[str, object] = {}
            if operation.has_query_params:
                call_kwargs["params"] = {"page": 1}
            if operation.has_payload:
                call_kwargs["payload"] = {"example": "value"}

            cases.append(
                "    ("
                f'"{group.module_name}", '
                f'"{operation.method_name}", '
                f"{path_arguments!r}, "
                f"{call_kwargs!r}, "
                f'"{operation.method}", '
                f'"{operation.path_template}", '
                f"{operation.auth_required}"
                "),"
            )

    cases_text = "\n".join(cases)
    return f'''
"""Generated endpoint smoke tests for the Aryeo resource surface."""

from __future__ import annotations

import httpx
import pytest

from aryeo.base_client import DEFAULT_BASE_URL

GENERATED_OPERATION_CASES = [
{cases_text}
]


@pytest.mark.parametrize(
    (
        "resource_name",
        "method_name",
        "path_arguments",
        "call_kwargs",
        "expected_method",
        "expected_path",
        "auth_required",
    ),
    GENERATED_OPERATION_CASES,
)
def test_generated_resource_methods(
    client_factory: object,
    resource_name: str,
    method_name: str,
    path_arguments: dict[str, str],
    call_kwargs: dict[str, object],
    expected_method: str,
    expected_path: str,
    auth_required: bool,
) -> None:
    """Each generated method should issue the expected HTTP request."""

    factory = client_factory
    token = "test-token" if auth_required else None
    client, requests = factory(token)
    resource = getattr(client, resource_name)
    method = getattr(resource, method_name)

    response = method(**path_arguments, **call_kwargs)

    assert response == {{"ok": True}}
    assert requests[0].method == expected_method
    base_path = httpx.URL(DEFAULT_BASE_URL).path.rstrip("/")
    assert requests[0].url.path == (
        f"{{base_path}}{{expected_path.format(**path_arguments)}}"
    )
    if auth_required:
        assert requests[0].headers["Authorization"] == "Bearer test-token"
    else:
        assert "Authorization" not in requests[0].headers
'''


def render_ci_workflow() -> str:
    """Render the CI workflow."""

    return """
name: CI

on:
  push:
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.11", "3.12"]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
      - run: python -m pip install --upgrade pip
      - run: python -m pip install -e ".[dev]"
      - run: python -m pip install -r docs/requirements.txt
      - run: black --check --diff --line-length=88 .
      - run: isort --check-only --diff --profile=black --line-length=88 .
      - run: flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
      - run: >-
          flake8 . --count --exit-zero --max-complexity=10
          --max-line-length=88 --statistics
      - run: mypy aryeo/ --strict --ignore-missing-imports
      - run: pytest --cov=aryeo --cov-report=xml --cov-report=term-missing
      - run: mkdocs build --strict
      - run: python -m pip install build twine
      - run: python -m build
      - run: python -m twine check dist/*
"""


def render_docs_workflow() -> str:
    """Render the docs verification workflow."""

    return """
name: Docs

on:
  push:
  pull_request:

jobs:
  build-docs:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: python -m pip install --upgrade pip
      - run: python -m pip install -e ".[dev]"
      - run: python -m pip install -r docs/requirements.txt
      - run: mkdocs build --strict
"""


def render_security_workflow() -> str:
    """Render the scheduled dependency audit workflow."""

    return """
name: Security Audit

on:
  schedule:
    - cron: "0 8 * * 1"
  workflow_dispatch:

jobs:
  pip-audit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: python -m pip install --upgrade pip
      - run: python -m pip install -e ".[dev]"
      - run: pip-audit
"""


def render_release_workflow() -> str:
    """Render the tag-based release workflow."""

    return """
name: Release

on:
  push:
    tags:
      - "v*"

jobs:
  publish:
    runs-on: ubuntu-latest
    environment: pypi
    permissions:
      contents: read
      id-token: write
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: python -m pip install --upgrade pip
      - run: python -m pip install -e ".[dev]"
      - run: python -m pip install -r docs/requirements.txt
      - run: python -m pip install build twine
      - run: pytest --cov=aryeo --cov-report=xml --cov-report=term-missing
      - run: mkdocs build --strict
      - run: python -m build
      - run: python -m twine check dist/*
      - uses: pypa/gh-action-pypi-publish@release/v1
"""


def render_unified_deployment_workflow() -> str:
    """Render the manual deployment workflow."""

    return """
name: Unified Deployment

on:
  workflow_dispatch:
    inputs:
      publish_package:
        description: "Publish the built package to PyPI"
        required: true
        default: false
        type: boolean

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: python -m pip install --upgrade pip
      - run: python -m pip install -e ".[dev]"
      - run: python -m pip install -r docs/requirements.txt
      - run: pytest --cov=aryeo --cov-report=xml --cov-report=term-missing
      - run: mkdocs build --strict
      - run: python -m pip install build twine
      - run: python -m build
      - run: python -m twine check dist/*

  publish:
    needs: validate
    if: ${{ inputs.publish_package }}
    runs-on: ubuntu-latest
    environment: pypi
    permissions:
      contents: read
      id-token: write
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: python -m pip install --upgrade pip
      - run: python -m pip install build twine
      - run: python -m build
      - run: python -m twine check dist/*
      - uses: pypa/gh-action-pypi-publish@release/v1
"""


def render_dependabot() -> str:
    """Render the Dependabot configuration."""

    return """
version: 2
updates:
  - package-ecosystem: "pip"
    directory: "/"
    schedule:
      interval: "weekly"
  - package-ecosystem: "pip"
    directory: "/docs"
    schedule:
      interval: "weekly"
  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "weekly"
"""


def render_rule_api_source_truth() -> str:
    """Render the source-of-truth Cursor rule."""

    return f"""
---
description: Source-of-truth rules for the Aryeo API client project.
globs:
alwaysApply: true
---
Before implementing or changing API behavior, read
`docs/planning/{INITIATIVE_SLUG}/foundation/api-source-of-truth.md` and
`docs/planning/{INITIATIVE_SLUG}/foundation/source-of-truth-matrix.md`.

Prefer sources in this order:
1. explicit API docs URL from the user
2. checked-in `docs/api/`
3. checked-in OpenAPI or Swagger artifacts
4. endpoint task docs or backlog notes

If the sources disagree, record the contradiction in the planning tree before
coding.
"""


def render_rule_implementation() -> str:
    """Render the implementation Cursor rule."""

    return f"""
---
description: Implementation rules for the Aryeo Python API client project.
globs:
alwaysApply: true
---
Implement runtime code under `./{PACKAGE_NAME}/` and group endpoints by resource
or service boundary.

Use Google-style docstrings and thorough type hints for Python files.

Every endpoint or client change must update:
- tests under `./tests/`
- docs under `./docs/`
- examples under `./examples/` when user-facing usage changes
- the owning planning docs under `docs/planning/{INITIATIVE_SLUG}/`

Do not mark an endpoint complete until code, tests, docs, and status docs land.
"""


def render_rule_docs_tests_sync() -> str:
    """Render the docs/tests/examples synchronization Cursor rule."""

    return f"""
---
description: Keep docs, tests, and examples aligned with the Aryeo client surface.
globs:
alwaysApply: true
---
When scaffolding or changing the client surface, keep `README.md`, `docs/`,
`examples/`, and `tests/` synchronized with the same commands and supported
Python versions.

Use pytest with coverage on `{PACKAGE_NAME}`.

Docs must build with `mkdocs build --strict` before the work is considered
ready.
"""


def render_rule_release_quality() -> str:
    """Render the quality and release Cursor rule."""

    return f"""
---
description: Quality and release rules for the Aryeo Python client project.
globs:
alwaysApply: true
---
Before changing CI or release behavior, keep `pyproject.toml`,
`{PACKAGE_NAME}/__init__.py`, and the release workflow aligned on versioning.

CI must cover formatting, import order, lint, typing, tests, build, strict docs
build, and dependency automation.

Use Dependabot as the default dependency automation tool unless the planning
docs record an intentional exception.
"""


PHASES: list[dict[str, str]] = [
    {
        "id": "0",
        "title": "Phase 0 - Source Audit",
        "status": "Complete",
        "goal": "Establish one honest API source of truth.",
        "paths": "docs/api/, docs/planning/.../foundation/",
        "acceptance": "Base contract, inventory, and contradictions are documented.",
        "risk": "Implementation can drift from the checked-in docs.",
    },
    {
        "id": "1",
        "title": "Phase 1 - Foundation And Packaging",
        "status": "Complete",
        "goal": "Create the package identity and shared runtime primitives.",
        "paths": "pyproject.toml, aryeo/, README.md",
        "acceptance": "Package metadata, core transport, and exceptions exist.",
        "risk": "Later endpoint work has no stable runtime contract.",
    },
    {
        "id": "2",
        "title": "Phase 2 - Endpoint Inventory And Models",
        "status": "In Progress",
        "goal": (
            "Map all endpoints into resource modules and honest model follow-up "
            "work."
        ),
        "paths": "aryeo/resources/, docs/reference/resources.md",
        "acceptance": "Generated resource methods cover the documented surface.",
        "risk": "Resource coverage becomes ad hoc and hard to audit.",
    },
    {
        "id": "3",
        "title": "Phase 3 - Tests And Coverage",
        "status": "In Progress",
        "goal": "Create the baseline unit and generated route tests.",
        "paths": "tests/",
        "acceptance": "Core behavior and generated request wiring are tested.",
        "risk": "Transport regressions slip in unnoticed.",
    },
    {
        "id": "4",
        "title": "Phase 4 - Docs And Examples",
        "status": "In Progress",
        "goal": "Create a truthful docs site and working examples.",
        "paths": "docs/, mkdocs.yml, examples/",
        "acceptance": "The docs site explains install, auth, and generated surfaces.",
        "risk": "Users cannot discover the scaffolded client shape.",
    },
    {
        "id": "5",
        "title": "Phase 5 - Workflows And Release",
        "status": "In Progress",
        "goal": "Scaffold CI, docs, release, security, and dependency automation.",
        "paths": ".github/workflows/, .github/dependabot.yml",
        "acceptance": (
            "Baseline workflows are checked in and consistent with packaging."
        ),
        "risk": "The scaffold cannot be kept healthy over time.",
    },
    {
        "id": "6",
        "title": "Phase 6 - Parity Audit",
        "status": "Pending",
        "goal": "Compare the scaffold against the intended full client baseline.",
        "paths": "docs/planning/.../trackers/, execution/",
        "acceptance": "Deferred gaps are explicit and prioritized.",
        "risk": "The repo may look more complete than it really is.",
    },
]


def render_planning_root_readme() -> str:
    """Render the planning root landing README."""

    return """
# Aryeo API Client Planning

This planning tree is docs-only and owns the long-lived roadmap for the Aryeo
Python client scaffold.

## Status Snapshot

- Phase 0 and Phase 1 are complete.
- Phase 2 through Phase 5 have scaffolded outputs but still carry follow-up work.
- Phase 6 remains the honesty pass for typed parity, live checks, and release
  readiness.

## Fastest Reality Checks

- `foundation/api-source-of-truth.md`
- `trackers/endpoint-inventory-readiness.md`
- `execution/execution-plan.md`
- `execution/api-client-bootstrap-plan.md`

## Source Priority

1. explicit API docs URL from the user
2. checked-in `docs/api/`
3. checked-in OpenAPI or Swagger artifacts
4. backlog notes and task docs

## Update Order

1. `foundation/api-source-of-truth.md`
2. `foundation/source-of-truth-matrix.md`
3. focused trackers under `trackers/`
4. `execution/execution-plan.md`
5. `execution/api-client-bootstrap-plan.md`

## Active Plan

- `execution/api-client-bootstrap-plan.md`
"""


def render_artifact_index() -> str:
    """Render the artifact path index for the planning tree."""

    return f"""
# Artifact Path Index

- Planning root: `docs/planning/{INITIATIVE_SLUG}/`
- Repo rules: `.cursor/rules/`
- Package directory: `{PACKAGE_NAME}/`
- Tests: `tests/`
- Docs site: `docs/`
- Examples: `examples/`
- Workflows: `.github/workflows/`
- Dependency automation: `.github/dependabot.yml`
"""


def render_foundation_readme() -> str:
    """Render the foundation README."""

    return """
# Foundation

These docs capture the source audit, package decisions, and ownership rules that
the scaffold depends on.
"""


def render_api_source_of_truth(
    resource_groups: list[ResourceGroup], audit: AuditSummary
) -> str:
    """Render the source-of-truth foundation doc."""

    inputs_table = markdown_table(
        ["Source", "Path", "Status", "Why it matters"],
        [
            [
                "Generated API overview",
                "`docs/api/README.md`",
                "Used",
                "Summarizes the wrapper, counts, and server.",
            ],
            [
                "OpenAPI wrapper",
                "`docs/api/aryeo.json`",
                "Used",
                "Canonical machine-readable contract.",
            ],
            [
                "Auth guide",
                "`docs/api/guides/authentication.md`",
                "Used",
                "Confirms bearer-token behavior and public ops.",
            ],
            [
                "Errors guide",
                "`docs/api/guides/errors.md`",
                "Used",
                "Captures shared 4xx and 5xx shapes.",
            ],
            [
                "Pagination guide",
                "`docs/api/guides/pagination.md`",
                "Used",
                "Confirms shared page/per_page semantics.",
            ],
            [
                "Reference index",
                "`docs/api/reference/README.md`",
                "Used",
                "Confirms tag groupings and counts.",
            ],
        ],
    )

    base_contract = markdown_table(
        ["Area", "Current answer", "Canonical source"],
        [
            ["Base URL", f"`{audit.primary_server}`", "`docs/api/aryeo.json`"],
            [
                "Authentication",
                "Bearer token on 85 operations; 5 are public",
                "`docs/api/guides/authentication.md`",
            ],
            ["Versioning", f"Spec version `{audit.version}`", "`docs/api/README.md`"],
            [
                "Pagination",
                "`page` and `per_page` plus common sort/include support",
                "`docs/api/guides/pagination.md`",
            ],
            [
                "Errors",
                "Shared 403/404/409/422/500 schema family",
                "`docs/api/guides/errors.md`",
            ],
            [
                "Rate limits",
                "Not documented in checked-in sources",
                "`docs/api/aryeo.json`",
            ],
        ],
    )

    resource_inventory = markdown_table(
        ["Resource group", "Coverage status", "Notes"],
        [
            [
                group.tag,
                "Low-level surface scaffolded",
                (
                    f"{len(group.operations)} operations in "
                    f"`aryeo/resources/{group.module_name}.py`"
                ),
            ]
            for group in resource_groups
        ],
    )

    contradictions = [
        "- The checked-in docs do not describe rate limits or retry budgets.",
        (
            "- The spec applies auth per operation instead of globally, so the "
            "client must preserve public exceptions."
        ),
        (
            "- Path parameter naming is inconsistent across endpoints, for "
            "example `order_id` versus `order`."
        ),
        "- Two request bodies are inline objects instead of named component schemas.",
        (
            "- Enums are mostly inline within properties and parameters rather "
            "than shared component enum schemas."
        ),
        "- No webhook or async callback contract is present in the checked-in sources.",
    ]
    follow_ups = [
        (
            "- Decide how to model inline request bodies in a typed way during "
            "the next phase."
        ),
        (
            "- Confirm whether publication should use the distribution name "
            "`aryeo` or a namespaced variant."
        ),
        (
            "- Add live contract tests once valid credentials and a "
            "non-production environment are available."
        ),
    ]

    return f"""
# API Source Of Truth

## Source Priority

1. checked-in `docs/api/`
2. checked-in OpenAPI wrapper in `docs/api/aryeo.json`

## Inputs Used

{inputs_table}

## Base Contract

{base_contract}

## Resource Inventory

{resource_inventory}

## Contradictions And Gaps

{chr(10).join(contradictions)}

## Follow-Up Before Implementation

{chr(10).join(follow_ups)}
"""


def render_source_of_truth_matrix(audit: AuditSummary) -> str:
    """Render the source-of-truth matrix."""

    rows = [
        [
            "Authentication",
            "`docs/api/guides/authentication.md`",
            "`docs/api/aryeo.json`",
            "High",
            "None",
        ],
        [
            "Base URL and versioning",
            "`docs/api/README.md`",
            "`docs/api/aryeo.json`",
            "High",
            "None",
        ],
        [
            "Resource grouping",
            "`docs/api/reference/README.md`",
            "`docs/api/README.md`",
            "High",
            "None",
        ],
        [
            "Error contract",
            "`docs/api/guides/errors.md`",
            "`docs/api/aryeo.json`",
            "High",
            "None",
        ],
        [
            "Pagination",
            "`docs/api/guides/pagination.md`",
            "`docs/api/reference/*.md`",
            "High",
            "None",
        ],
        [
            "Request/response schemas",
            "`docs/api/aryeo.json`",
            "`docs/api/reference/*.md`",
            "High",
            "Typed models still needed",
        ],
        [
            "Enums and shared types",
            "`docs/api/aryeo.json`",
            "`docs/api/reference/*.md`",
            "Medium",
            f"{audit.inline_enum_paths} inline enum paths need modeling strategy",
        ],
        [
            "Uploads and downloads",
            "`docs/api/aryeo.json`",
            "`docs/api/reference/*.md`",
            "High",
            "Only JSON content types are present today",
        ],
        [
            "Rate limits",
            "`docs/api/aryeo.json`",
            "None",
            "Low",
            "No limit guidance is documented",
        ],
        [
            "Webhooks",
            "`docs/api/aryeo.json`",
            "None",
            "Low",
            "No webhook section is present",
        ],
    ]
    matrix = markdown_table(
        ["Topic", "Canonical source", "Secondary source", "Confidence", "Follow-up"],
        rows,
    )
    return f"""
# Source Of Truth Matrix

{matrix}
"""


def render_package_versioning_adr() -> str:
    """Render the package and versioning ADR."""

    return f"""
# Package And Versioning ADR

## Decision

- Distribution name: `{PROJECT_NAME}`
- Import package: `{PACKAGE_NAME}`
- Initial version: `{PROJECT_VERSION}`
- Version sources of truth: `pyproject.toml` and `{PACKAGE_NAME}/__init__.py`

## Rationale

- The repo name and API name already align on `aryeo`.
- Keeping the version in exactly two files matches the planning reference.
- The package currently exposes low-level JSON methods, so a `0.x` version is
  more honest than pretending the client is stable.

## Follow-Up

- Confirm PyPI name availability before publication.
- Decide when typed models justify a `1.0.0` stability target.
"""


def render_rules_ownership_adr() -> str:
    """Render the rules and ownership ADR."""

    return f"""
# Rules And Ownership ADR

## Planning Ownership

- `docs/planning/{INITIATIVE_SLUG}/` owns roadmap, readiness, and truthful status.
- `.cursor/rules/` owns repo-local AI guidance derived from the planning tree.

## Runtime Ownership

- `{PACKAGE_NAME}/base_client.py` owns transport, auth, and error behavior.
- `{PACKAGE_NAME}/client.py` owns resource bindings.
- `{PACKAGE_NAME}/resources/` owns generated endpoint methods grouped by tag.

## Supporting Surfaces

- `tests/` owns regression coverage.
- `docs/` owns published documentation and examples.
- `.github/workflows/` owns automation and release quality checks.
"""


def render_trackers_readme() -> str:
    """Render the trackers README."""

    return """
# Trackers

These focused trackers keep the planning tree honest as scaffolded work lands.
"""


def render_readiness_overview() -> str:
    """Render the readiness overview tracker."""

    rows = [[phase["title"], phase["status"], phase["goal"]] for phase in PHASES]
    return f"""
# Readiness Overview

{markdown_table(["Phase", "Status", "Goal"], rows)}
"""


def render_endpoint_inventory_readiness(resource_groups: list[ResourceGroup]) -> str:
    """Render the endpoint inventory readiness tracker."""

    rows = [
        [
            group.tag,
            str(len(group.operations)),
            f"`aryeo/resources/{group.module_name}.py`",
            f"`{group.doc_path}`",
            "Generated low-level methods; typed schemas still pending",
        ]
        for group in resource_groups
    ]
    inventory_table = markdown_table(
        ["Resource group", "Ops", "Module", "Doc source", "Current status"],
        rows,
    )
    return f"""
# Endpoint Inventory Readiness

{inventory_table}
"""


def render_coverage_tests_readiness() -> str:
    """Render the tests and coverage tracker."""

    rows = [
        ["Core transport tests", "Present", "`tests/test_base_client.py`"],
        ["Client wiring tests", "Present", "`tests/test_client.py`"],
        ["Exception tests", "Present", "`tests/test_exceptions.py`"],
        [
            "Generated endpoint smoke tests",
            "Present",
            "`tests/test_generated_surface.py`",
        ],
        [
            "Live integration tests",
            "Deferred",
            "Requires safe credentials and stable fixtures",
        ],
        [
            "Typed model validation tests",
            "Deferred",
            "Blocked on richer request/response models",
        ],
    ]
    return f"""
# Coverage And Tests Readiness

{markdown_table(["Area", "Status", "Notes"], rows)}
"""


def render_docs_parity_readiness() -> str:
    """Render the docs parity tracker."""

    rows = [
        ["README", "Present", "Explains scope, install, validation, and regeneration"],
        [
            "MkDocs config",
            "Present",
            "Builds package reference and checked-in API docs",
        ],
        [
            "Getting started guides",
            "Present",
            "Install, auth, and quickstart pages exist",
        ],
        [
            "Package reference",
            "Present",
            "Client, exceptions, and resources pages exist",
        ],
        [
            "Narrative usage guides",
            "Deferred",
            "Workflow-specific docs can grow after typed models",
        ],
    ]
    return f"""
# Docs Parity Readiness

{markdown_table(["Surface", "Status", "Notes"], rows)}
"""


def render_workflow_release_readiness() -> str:
    """Render the workflow and release readiness tracker."""

    rows = [
        ["CI", "Scaffolded", "`ci.yml` runs quality, tests, docs, and build checks"],
        ["Docs", "Scaffolded", "`docs.yml` builds MkDocs strictly"],
        ["Security", "Scaffolded", "`security-audit.yml` runs `pip-audit`"],
        [
            "Release",
            "Scaffolded",
            "`release.yml` uses PyPI Trusted Publishing with the `pypi` environment",
        ],
        [
            "Unified deployment",
            "Scaffolded",
            (
                "Manual workflow can publish through Trusted Publishing when its "
                "workflow file is also registered on PyPI"
            ),
        ],
        ["Dependabot", "Scaffolded", "Weekly updates for pip and GitHub Actions"],
        [
            "Live publication",
            "Deferred",
            "Requires a PyPI pending publisher before the first trusted release",
        ],
    ]
    return f"""
# Workflow Release Readiness

{markdown_table(["Area", "Status", "Notes"], rows)}
"""


def render_execution_readme() -> str:
    """Render the execution README."""

    return """
# Execution

These docs are the live checked-in ledger for scaffold status, next work, and
phase proof.
"""


def render_execution_plan() -> str:
    """Render the live execution ledger."""

    scaffolded = [
        "- Core runtime modules for transport, exceptions, and resource bindings",
        "- Generated resource modules for every documented API tag",
        "- Planning docs and Cursor rules",
        "- Examples, MkDocs config, tests, and workflow scaffolding",
    ]
    planned = [
        "- Typed request and response models for shared schemas",
        "- Live integration tests against a safe non-production environment",
        "- Richer pagination helpers and higher-level convenience methods",
        "- First live trusted release after the matching PyPI publisher is registered",
    ]
    work_queue = [
        "- Replace low-level JSON mappings with typed models where the docs are stable",
        "- Expand tests around inline request bodies and public endpoints",
        (
            "- Add parity reporting that compares the generated surface to the "
            "OpenAPI spec"
        ),
    ]
    return f"""
# Execution Plan

## Already Scaffolded

{chr(10).join(scaffolded)}

## Only Planned

{chr(10).join(planned)}

## Highest-Risk Remaining Surface

- The current client is resource-complete at the transport layer but not yet
  schema-complete at the model layer.

## Current Blockers

- Rate limits and live retry guidance are undocumented.
- Integration validation needs safe credentials and a non-production test target.
- Trusted Publishing still needs the matching PyPI publisher registration before
  the first live release.

## Current Work Queue

{chr(10).join(work_queue)}
"""


def render_roadmap() -> str:
    """Render the baseline roadmap."""

    rows = [
        [
            phase["title"],
            phase["goal"],
            phase["paths"],
            phase["acceptance"],
            phase["risk"],
        ]
        for phase in PHASES
    ]
    roadmap_table = markdown_table(
        [
            "Phase",
            "Why it exists",
            "Files or directories",
            "Acceptance",
            "Risk if skipped",
        ],
        rows,
    )
    return f"""
# Roadmap

{roadmap_table}
"""


def render_bootstrap_plan() -> str:
    """Render the canonical bootstrap plan."""

    sections = []
    for phase in PHASES:
        sections.append(
            "\n".join(
                [
                    f"### {phase['title']}",
                    f"- Inputs: {phase['paths']}",
                    f"- Deliverables: {phase['acceptance']}",
                    f"- Exit criteria: {phase['status']}",
                ]
            )
        )

    return f"""
# API Client Bootstrap Plan

## Goal

- Recreate a typed Python API client baseline from the available API docs.

## Current Focus

- Phase 2 follow-up work: move from low-level JSON payloads toward typed request
  and response models without losing contract coverage.

## Ordered Phases

{chr(10).join(sections)}
"""


def render_phase_doc(title: str, summary_lines: list[str]) -> str:
    """Render a short phase proof document."""

    return f"""
# {title}

{chr(10).join(summary_lines)}
"""


def file_entry(path: Path, content: str) -> tuple[Path, str]:
    """Build a file-entry tuple for scaffold registries."""

    return path, content


def build_root_files(
    resource_groups: list[ResourceGroup],
    audit: AuditSummary,
) -> list[tuple[Path, str]]:
    """Build curated files that live at the repository root."""

    return [
        file_entry(REPO_ROOT / "pyproject.toml", render_pyproject()),
        file_entry(REPO_ROOT / ".gitignore", render_gitignore()),
        file_entry(REPO_ROOT / "MANIFEST.in", render_manifest()),
        file_entry(REPO_ROOT / "README.md", render_readme(resource_groups, audit)),
        file_entry(REPO_ROOT / "STYLE_GUIDE.md", render_style_guide()),
        file_entry(REPO_ROOT / "mkdocs.yml", render_mkdocs()),
    ]


def build_docs_files(audit: AuditSummary) -> list[tuple[Path, str]]:
    """Build curated documentation files outside the planning tree."""

    return [
        file_entry(REPO_ROOT / "docs" / "requirements.txt", render_docs_requirements()),
        file_entry(REPO_ROOT / "docs" / "index.md", render_docs_index(audit)),
        file_entry(
            REPO_ROOT / "docs" / "getting-started" / "installation.md",
            render_docs_installation(),
        ),
        file_entry(
            REPO_ROOT / "docs" / "getting-started" / "authentication.md",
            render_docs_authentication(),
        ),
        file_entry(
            REPO_ROOT / "docs" / "getting-started" / "quickstart.md",
            render_docs_quickstart(),
        ),
        file_entry(
            REPO_ROOT / "docs" / "reference" / "index.md",
            render_docs_reference_index(),
        ),
        file_entry(
            REPO_ROOT / "docs" / "reference" / "client.md",
            render_docs_reference_client(),
        ),
        file_entry(
            REPO_ROOT / "docs" / "reference" / "exceptions.md",
            render_docs_reference_exceptions(),
        ),
        file_entry(
            REPO_ROOT / "docs" / "development" / "contributing.md",
            render_docs_contributing(),
        ),
        file_entry(
            REPO_ROOT / "docs" / "development" / "planning.md",
            render_docs_planning(),
        ),
    ]


def build_package_files() -> list[tuple[Path, str]]:
    """Build curated runtime package files."""

    return [
        file_entry(REPO_ROOT / PACKAGE_NAME / "__init__.py", render_package_init()),
        file_entry(REPO_ROOT / PACKAGE_NAME / "types.py", render_types_module()),
        file_entry(
            REPO_ROOT / PACKAGE_NAME / "exceptions.py",
            render_exceptions_module(),
        ),
        file_entry(
            REPO_ROOT / PACKAGE_NAME / "base_client.py",
            render_base_client_module(),
        ),
        file_entry(
            REPO_ROOT / PACKAGE_NAME / "resources" / "_base.py",
            render_resource_base_module(),
        ),
        file_entry(REPO_ROOT / PACKAGE_NAME / "py.typed", ""),
    ]


def build_example_files() -> list[tuple[Path, str]]:
    """Build curated example scripts."""

    return [
        file_entry(
            REPO_ROOT / "examples" / "quickstart.py", render_examples_quickstart()
        ),
        file_entry(REPO_ROOT / "examples" / "list_orders.py", render_examples_orders()),
    ]


def build_test_files() -> list[tuple[Path, str]]:
    """Build curated unit-test files."""

    return [
        file_entry(REPO_ROOT / "tests" / "__init__.py", render_tests_init()),
        file_entry(REPO_ROOT / "tests" / "conftest.py", render_tests_conftest()),
        file_entry(
            REPO_ROOT / "tests" / "test_base_client.py",
            render_tests_base_client(),
        ),
        file_entry(REPO_ROOT / "tests" / "test_client.py", render_tests_client()),
        file_entry(
            REPO_ROOT / "tests" / "test_exceptions.py",
            render_tests_exceptions(),
        ),
    ]


def build_workflow_files() -> list[tuple[Path, str]]:
    """Build curated workflow and dependency-automation files."""

    return [
        file_entry(
            REPO_ROOT / ".github" / "workflows" / "ci.yml", render_ci_workflow()
        ),
        file_entry(
            REPO_ROOT / ".github" / "workflows" / "docs.yml",
            render_docs_workflow(),
        ),
        file_entry(
            REPO_ROOT / ".github" / "workflows" / "security-audit.yml",
            render_security_workflow(),
        ),
        file_entry(
            REPO_ROOT / ".github" / "workflows" / "release.yml",
            render_release_workflow(),
        ),
        file_entry(
            REPO_ROOT / ".github" / "workflows" / "unified-deployment.yml",
            render_unified_deployment_workflow(),
        ),
        file_entry(REPO_ROOT / ".github" / "dependabot.yml", render_dependabot()),
    ]


def build_rule_files() -> list[tuple[Path, str]]:
    """Build curated Cursor rule files."""

    return [
        file_entry(
            REPO_ROOT / ".cursor" / "rules" / "api-source-truth.mdc",
            render_rule_api_source_truth(),
        ),
        file_entry(
            REPO_ROOT / ".cursor" / "rules" / "api-client-implementation.mdc",
            render_rule_implementation(),
        ),
        file_entry(
            REPO_ROOT / ".cursor" / "rules" / "docs-tests-sync.mdc",
            render_rule_docs_tests_sync(),
        ),
        file_entry(
            REPO_ROOT / ".cursor" / "rules" / "release-quality-contract.mdc",
            render_rule_release_quality(),
        ),
    ]


def build_phase_files(planning_root: Path) -> list[tuple[Path, str]]:
    """Build curated planning phase-proof documents."""

    execution_root = planning_root / "execution"
    return [
        file_entry(
            execution_root / "api_client_PHASE_00_source_audit.md",
            render_phase_doc(
                "API Client Phase 00 Source Audit",
                [
                    (
                        "- Confirmed `docs/api/aryeo.json` as the canonical "
                        "machine-readable source."
                    ),
                    (
                        "- Confirmed bearer-token auth on protected operations and "
                        "5 public exceptions."
                    ),
                    (
                        "- Recorded current gaps around rate limits, webhooks, and "
                        "inline request bodies."
                    ),
                ],
            ),
        ),
        file_entry(
            execution_root / "api_client_PHASE_01_foundation.md",
            render_phase_doc(
                "API Client Phase 01 Foundation",
                [
                    (
                        "- Scaffolded package metadata, base transport, exceptions, "
                        "and docs site config."
                    ),
                    (
                        "- Chose `aryeo` as both the initial distribution and import "
                        "package name."
                    ),
                    (
                        "- Kept typed response models deferred to preserve honest "
                        "status language."
                    ),
                ],
            ),
        ),
        file_entry(
            execution_root / "api_client_PHASE_02_endpoint_inventory.md",
            render_phase_doc(
                "API Client Phase 02 Endpoint Inventory",
                [
                    "- Generated resource modules for every documented tag.",
                    (
                        "- Preserved per-operation auth requirements so public "
                        "endpoints stay callable without a token."
                    ),
                    (
                        "- Deferred schema-perfect typing for the follow-on "
                        "implementation phase."
                    ),
                ],
            ),
        ),
        file_entry(
            execution_root / "api_client_PHASE_03_tests_and_coverage.md",
            render_phase_doc(
                "API Client Phase 03 Tests And Coverage",
                [
                    (
                        "- Added unit tests for the base client, client wiring, and "
                        "exception parsing."
                    ),
                    (
                        "- Added a generated route smoke test that exercises each "
                        "generated endpoint method."
                    ),
                    (
                        "- Live integration tests remain blocked on non-production "
                        "credentials."
                    ),
                ],
            ),
        ),
        file_entry(
            execution_root / "api_client_PHASE_04_docs_and_examples.md",
            render_phase_doc(
                "API Client Phase 04 Docs And Examples",
                [
                    (
                        "- Added MkDocs configuration, getting-started pages, and "
                        "package reference pages."
                    ),
                    "- Reused the checked-in API contract docs under `docs/api/`.",
                    (
                        "- Added example scripts that demonstrate the generated "
                        "client surface."
                    ),
                ],
            ),
        ),
        file_entry(
            execution_root / "api_client_PHASE_05_workflows_and_release.md",
            render_phase_doc(
                "API Client Phase 05 Workflows And Release",
                [
                    (
                        "- Added CI, docs, security, release, and manual deployment "
                        "workflow scaffolding."
                    ),
                    (
                        "- Added Dependabot configuration for root pip, docs pip, "
                        "and GitHub Actions."
                    ),
                    (
                        "- Real publication remains deferred until the repo is "
                        "connected to GitHub and PyPI."
                    ),
                ],
            ),
        ),
        file_entry(
            execution_root / "api_client_PHASE_06_parity_audit.md",
            render_phase_doc(
                "API Client Phase 06 Parity Audit",
                [
                    (
                        "- Outstanding parity gaps are currently typed models, "
                        "live contract tests, and publication wiring."
                    ),
                    (
                        "- The current scaffold should be treated as low-level "
                        "transport coverage, not complete semantic parity."
                    ),
                ],
            ),
        ),
    ]


def build_planning_files(
    planning_root: Path,
    resource_groups: list[ResourceGroup],
    audit: AuditSummary,
) -> list[tuple[Path, str]]:
    """Build curated planning and tracker documents."""

    foundation_root = planning_root / "foundation"
    tracker_root = planning_root / "trackers"
    execution_root = planning_root / "execution"
    planning_files = [
        file_entry(planning_root / "README.md", render_planning_root_readme()),
        file_entry(planning_root / "ARTIFACT_PATH_INDEX.md", render_artifact_index()),
        file_entry(foundation_root / "README.md", render_foundation_readme()),
        file_entry(
            foundation_root / "api-source-of-truth.md",
            render_api_source_of_truth(resource_groups, audit),
        ),
        file_entry(
            foundation_root / "source-of-truth-matrix.md",
            render_source_of_truth_matrix(audit),
        ),
        file_entry(
            foundation_root / "package-and-versioning-adr.md",
            render_package_versioning_adr(),
        ),
        file_entry(
            foundation_root / "rules-and-ownership-adr.md",
            render_rules_ownership_adr(),
        ),
        file_entry(tracker_root / "README.md", render_trackers_readme()),
        file_entry(
            tracker_root / "readiness-overview.md",
            render_readiness_overview(),
        ),
        file_entry(
            tracker_root / "endpoint-inventory-readiness.md",
            render_endpoint_inventory_readiness(resource_groups),
        ),
        file_entry(
            tracker_root / "coverage-and-tests-readiness.md",
            render_coverage_tests_readiness(),
        ),
        file_entry(
            tracker_root / "docs-parity-readiness.md",
            render_docs_parity_readiness(),
        ),
        file_entry(
            tracker_root / "workflow-release-readiness.md",
            render_workflow_release_readiness(),
        ),
        file_entry(execution_root / "README.md", render_execution_readme()),
        file_entry(execution_root / "execution-plan.md", render_execution_plan()),
        file_entry(execution_root / "roadmap.md", render_roadmap()),
        file_entry(
            execution_root / "api-client-bootstrap-plan.md",
            render_bootstrap_plan(),
        ),
    ]
    planning_files.extend(build_phase_files(planning_root))
    return planning_files


def build_curated_files(
    resource_groups: list[ResourceGroup], audit: AuditSummary
) -> list[tuple[Path, str]]:
    """Build the curated scaffold files that should not overwrite existing work."""

    planning_root = REPO_ROOT / "docs" / "planning" / INITIATIVE_SLUG
    curated_files: list[tuple[Path, str]] = []
    curated_files.extend(build_root_files(resource_groups, audit))
    curated_files.extend(build_docs_files(audit))
    curated_files.extend(build_package_files())
    curated_files.extend(build_example_files())
    curated_files.extend(build_test_files())
    curated_files.extend(build_workflow_files())
    curated_files.extend(build_rule_files())
    curated_files.extend(build_planning_files(planning_root, resource_groups, audit))
    return curated_files


def build_generated_files(
    resource_groups: list[ResourceGroup],
) -> list[tuple[Path, str]]:
    """Build the generated files that should be refreshed on every run."""

    generated_files: list[tuple[Path, str]] = [
        (REPO_ROOT / PACKAGE_NAME / "client.py", render_client_module(resource_groups)),
        (
            REPO_ROOT / PACKAGE_NAME / "resources" / "__init__.py",
            render_resources_init(resource_groups),
        ),
        (
            REPO_ROOT / "docs" / "reference" / "resources.md",
            render_docs_reference_resources(resource_groups),
        ),
        (
            REPO_ROOT / "tests" / "test_generated_surface.py",
            render_generated_surface_test(resource_groups),
        ),
    ]
    for group in resource_groups:
        generated_files.append(
            (
                REPO_ROOT / PACKAGE_NAME / "resources" / f"{group.module_name}.py",
                render_resource_module(group),
            )
        )
    return generated_files


def main() -> None:
    """Generate the Aryeo client scaffold from the checked-in docs."""

    args = parse_args()
    spec = read_spec()
    resource_groups, audit = build_resource_groups(spec)

    curated_files = build_curated_files(resource_groups, audit)
    generated_files = build_generated_files(resource_groups)

    for path, content in curated_files:
        write_text(
            path,
            content,
            overwrite=args.force_curated,
            dry_run=args.dry_run,
        )

    for path, content in generated_files:
        write_text(path, content, overwrite=True, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
