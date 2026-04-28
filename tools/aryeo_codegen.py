"""Generate the Aryeo client scaffold.

The checked-in OpenAPI wrapper at ``docs/api/aryeo.json`` is the only source
used for endpoint, model, and enum generation. This generator intentionally
keeps runtime resource methods JSON-based while emitting typed model and enum
modules for the full component-schema surface that can be represented
confidently from the spec.
"""

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
HTTP_METHODS = ("get", "post", "put", "patch", "delete", "options", "head")
SUPPORTED_HTTP_METHODS = {method.upper() for method in HTTP_METHODS}
MODEL_FIELD_INDENT = "    "


@dataclass
class Operation:
    """Store normalized OpenAPI operation metadata.

    Attributes:
        tag: OpenAPI tag used for grouping.
        tag_description: Tag description from the OpenAPI document.
        method: Uppercase HTTP method.
        path: API path template using original OpenAPI parameter names.
        path_template: Python f-string template using sanitized parameter names.
        summary: Human-readable operation summary.
        doc_path: Generated markdown API contract path.
        path_params: Sanitized path parameter names used by the Python method.
        has_query_params: Whether the operation declares query parameters.
        has_payload: Whether the operation accepts a JSON request body.
        payload_required: Whether the request body is required.
        payload_schema: Human-readable payload schema name.
        response_schema: Human-readable response schema name.
        auth_required: Whether a bearer token is required.
        method_name: Python method name assigned within the resource client.
    """

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
    """Represent a generated resource module.

    Attributes:
        tag: Display name for the API tag.
        description: Tag description.
        module_name: Python module name.
        class_name: Resource client class name.
        doc_path: Generated API contract markdown path.
        operations: Operations assigned to this resource.
    """

    tag: str
    description: str
    module_name: str
    class_name: str
    doc_path: str
    operations: list[Operation]


@dataclass(frozen=True)
class AuditSummary:
    """Capture source-of-truth statistics used in generated docs."""

    title: str
    version: str
    primary_server: str
    operation_count: int
    path_count: int
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
    """Collect OpenAPI audit metadata while parsing operations."""

    request_content_types: Counter[str] = field(default_factory=Counter)
    response_content_types: Counter[str] = field(default_factory=Counter)
    public_operations: list[str] = field(default_factory=list)
    inline_request_bodies: list[str] = field(default_factory=list)
    protected_operation_count: int = 0


@dataclass(frozen=True)
class EnumDefinition:
    """Represent one generated enum class.

    Attributes:
        class_name: Python enum class name.
        source_path: OpenAPI path where the enum was found.
        values: Raw enum values.
        is_string_enum: Whether every value is a string.
    """

    class_name: str
    source_path: str
    values: tuple[object, ...]
    is_string_enum: bool


@dataclass(frozen=True)
class ModelSurface:
    """Represent generated model and enum metadata."""

    model_names: tuple[str, ...]
    enum_names: tuple[str, ...]
    ambiguous_schemas: tuple[str, ...]


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments for the generator.

    Returns:
        Parsed command-line arguments.
    """

    parser = argparse.ArgumentParser(
        description="Generate the Aryeo client from docs/api/aryeo.json."
    )
    parser.add_argument(
        "--force-curated",
        action="store_true",
        help="Overwrite curated files in addition to generated files.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print writes without modifying the repository.",
    )
    return parser.parse_args()


def read_spec() -> dict[str, Any]:
    """Load the checked-in OpenAPI wrapper.

    Returns:
        The unwrapped OpenAPI definition.
    """

    wrapper = json.loads(SPEC_PATH.read_text(encoding="utf-8"))
    definition = wrapper.get("definition")
    if not isinstance(definition, dict):
        raise ValueError("docs/api/aryeo.json must contain a definition object.")
    return definition


def write_text(
    path: Path,
    content: str,
    *,
    overwrite: bool,
    dry_run: bool,
) -> None:
    """Write normalized text while respecting overwrite and dry-run flags.

    Args:
        path: Destination path.
        content: File content to write.
        overwrite: Whether existing files may be replaced.
        dry_run: Whether to report the write without touching the filesystem.
    """

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
    """Render a Markdown table.

    Args:
        headers: Table column headers.
        rows: Table body rows.

    Returns:
        Markdown table text.
    """

    header_line = "| " + " | ".join(headers) + " |"
    separator_line = "| " + " | ".join("---" for _ in headers) + " |"
    row_lines = ["| " + " | ".join(row) + " |" for row in rows]
    return "\n".join([header_line, separator_line, *row_lines])


def snake_case(value: str) -> str:
    """Convert an arbitrary value into snake_case.

    Args:
        value: Source value.

    Returns:
        A lowercase snake_case string.
    """

    cleaned = re.sub(r"[^A-Za-z0-9]+", "_", value)
    cleaned = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", cleaned)
    cleaned = re.sub(r"_+", "_", cleaned)
    return cleaned.strip("_").lower()


def pascal_case(value: str) -> str:
    """Convert an arbitrary value into PascalCase.

    Args:
        value: Source value.

    Returns:
        A PascalCase identifier fragment.
    """

    return "".join(part.capitalize() for part in snake_case(value).split("_"))


def sanitize_identifier(value: str) -> str:
    """Return a valid Python identifier.

    Args:
        value: Source value.

    Returns:
        A valid non-keyword Python identifier.
    """

    identifier = snake_case(value)
    if not identifier:
        identifier = "value"
    if identifier[0].isdigit():
        identifier = f"op_{identifier}"
    if keyword.iskeyword(identifier):
        identifier = f"{identifier}_value"
    return identifier


def sanitize_class_name(value: str, *, fallback: str = "Generated") -> str:
    """Return a valid Python class name.

    Args:
        value: Source value.
        fallback: Name to use if the source has no valid characters.

    Returns:
        A PascalCase class name.
    """

    class_name = pascal_case(value) or fallback
    if class_name[0].isdigit():
        class_name = f"{fallback}{class_name}"
    if keyword.iskeyword(class_name.lower()):
        class_name = f"{class_name}Value"
    return class_name


def slugify(value: str) -> str:
    """Convert text into a stable docs slug.

    Args:
        value: Source value.

    Returns:
        Kebab-case slug.
    """

    return snake_case(value).replace("_", "-")


def singularize(word: str) -> str:
    """Apply a small singularization pass for method names.

    Args:
        word: Source word.

    Returns:
        Best-effort singular form.
    """

    if word.endswith("ies") and len(word) > 3:
        return f"{word[:-3]}y"
    if word.endswith("ses") and len(word) > 3:
        return word[:-2]
    if word.endswith("s") and not word.endswith("ss") and len(word) > 1:
        return word[:-1]
    return word


def clean_markdown_text(value: str | None) -> str:
    """Convert markdown-ish prose into a compact single-line description."""

    if not value:
        return ""
    text = re.sub(r"<[^>]+>", "", value)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def get_schemas(spec: dict[str, Any]) -> dict[str, dict[str, Any]]:
    """Return component schemas from an OpenAPI document."""

    components = spec.get("components", {})
    if not isinstance(components, dict):
        return {}
    schemas = components.get("schemas", {})
    if not isinstance(schemas, dict):
        return {}
    return {
        name: schema
        for name, schema in schemas.items()
        if isinstance(name, str) and isinstance(schema, dict)
    }


def schema_label(schema: dict[str, Any]) -> str | None:
    """Return a compact label for a schema.

    Args:
        schema: OpenAPI schema object.

    Returns:
        Human-readable schema label, if available.
    """

    if "$ref" in schema:
        return str(schema["$ref"]).rsplit("/", 1)[-1]
    if "enum" in schema:
        return "inline enum"
    schema_type = schema.get("type")
    if schema_type == "object":
        properties = schema.get("properties", {})
        if isinstance(properties, dict) and properties:
            preview = ", ".join(sorted(properties)[:5])
            suffix = "..." if len(properties) > 5 else ""
            return f"inline object ({preview}{suffix})"
        return "inline object"
    if isinstance(schema_type, str):
        return schema_type
    if isinstance(schema_type, list):
        return " | ".join(str(item) for item in schema_type)
    return None


def is_public_operation(operation: dict[str, Any], global_security: object) -> bool:
    """Return whether an operation is public."""

    if operation.get("security") == []:
        return True
    if "security" not in operation and global_security == []:
        return True
    return False


def collect_path_parameters(
    path: str,
    parameters: list[object],
) -> tuple[list[str], str]:
    """Collect sanitized path parameters and an f-string template.

    Args:
        path: OpenAPI path template.
        parameters: Operation and path-level parameters.

    Returns:
        A tuple of sanitized path parameter names and Python path template.
    """

    parameter_names: list[str] = []
    original_to_sanitized: dict[str, str] = {}
    for parameter in parameters:
        if not isinstance(parameter, dict):
            continue
        if parameter.get("in") != "path":
            continue
        name = parameter.get("name")
        if not isinstance(name, str):
            continue
        sanitized = sanitize_identifier(name)
        original_to_sanitized[name] = sanitized
        parameter_names.append(sanitized)

    for original in re.findall(r"{([^}]+)}", path):
        sanitized = original_to_sanitized.get(original, sanitize_identifier(original))
        if sanitized not in parameter_names:
            parameter_names.append(sanitized)
        original_to_sanitized[original] = sanitized

    path_template = path
    for original, sanitized in original_to_sanitized.items():
        path_template = path_template.replace(f"{{{original}}}", f"{{{sanitized}}}")
    return parameter_names, path_template


def first_json_schema(content: object) -> dict[str, Any] | None:
    """Return the first JSON-compatible content schema."""

    if not isinstance(content, dict):
        return None
    for content_type, content_record in content.items():
        if not isinstance(content_type, str) or "json" not in content_type:
            continue
        if isinstance(content_record, dict):
            schema = content_record.get("schema")
            if isinstance(schema, dict):
                return schema
    return None


def request_body_metadata(
    operation: dict[str, Any],
    audit: AuditAccumulator,
    operation_label: str,
) -> tuple[bool, bool, str | None]:
    """Extract request-body metadata for a resource operation."""

    request_body = operation.get("requestBody")
    if not isinstance(request_body, dict):
        return False, False, None
    content = request_body.get("content", {})
    if isinstance(content, dict):
        audit.request_content_types.update(str(key) for key in content)
    schema = first_json_schema(content)
    if schema is None:
        return False, bool(request_body.get("required")), None
    if "$ref" not in schema:
        audit.inline_request_bodies.append(operation_label)
    return True, bool(request_body.get("required")), schema_label(schema)


def response_schema_label(
    operation: dict[str, Any],
    audit: AuditAccumulator,
) -> str | None:
    """Extract the first documented JSON response schema label."""

    responses = operation.get("responses", {})
    if not isinstance(responses, dict):
        return None
    for response in responses.values():
        if not isinstance(response, dict):
            continue
        content = response.get("content", {})
        if isinstance(content, dict):
            audit.response_content_types.update(str(key) for key in content)
        schema = first_json_schema(content)
        if schema is not None:
            return schema_label(schema)
    return None


def derive_method_name(summary: str, tag: str, method: str, path: str) -> str:
    """Build a concise resource-local method name."""

    words = [word.lower() for word in re.findall(r"[A-Za-z0-9]+", summary)]
    if not words:
        words = [method.lower(), *re.findall(r"[A-Za-z0-9]+", path)]

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
    return sanitize_identifier("_".join(filtered_words))


def assign_method_names(operations: list[Operation]) -> None:
    """Assign unique method names in-place for one resource group."""

    used_names: set[str] = set()
    for operation in operations:
        candidate = derive_method_name(
            operation.summary,
            operation.tag,
            operation.method,
            operation.path,
        )
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


def build_resource_groups(
    spec: dict[str, Any]
) -> tuple[list[ResourceGroup], AuditSummary]:
    """Build resource groups and API audit metadata from the OpenAPI spec."""

    tag_descriptions = {
        tag["name"]: clean_markdown_text(tag.get("description"))
        for tag in spec.get("tags", [])
        if isinstance(tag, dict) and isinstance(tag.get("name"), str)
    }
    global_security = spec.get("security")
    audit = AuditAccumulator()
    operations_by_tag: dict[str, list[Operation]] = defaultdict(list)
    paths = spec.get("paths", {})
    if not isinstance(paths, dict):
        paths = {}

    for path, path_item in sorted(paths.items()):
        if not isinstance(path, str) or not isinstance(path_item, dict):
            continue
        path_parameters = path_item.get("parameters", [])
        if not isinstance(path_parameters, list):
            path_parameters = []
        for method in HTTP_METHODS:
            operation = path_item.get(method)
            if not isinstance(operation, dict):
                continue
            tag = str((operation.get("tags") or ["Default"])[0])
            summary = clean_markdown_text(operation.get("summary"))
            operation_id = clean_markdown_text(operation.get("operationId"))
            summary = summary or operation_id or f"{method.upper()} {path}"
            operation_label = f"{method.upper()} {path}"
            operation_parameters = operation.get("parameters", [])
            if not isinstance(operation_parameters, list):
                operation_parameters = []
            all_parameters = [*path_parameters, *operation_parameters]
            path_params, path_template = collect_path_parameters(path, all_parameters)
            has_query_params = any(
                isinstance(parameter, dict) and parameter.get("in") == "query"
                for parameter in all_parameters
            )
            has_payload, payload_required, payload_schema = request_body_metadata(
                operation,
                audit,
                operation_label,
            )
            response_schema = response_schema_label(operation, audit)
            public = is_public_operation(operation, global_security)
            if public:
                audit.public_operations.append(operation_label)
            else:
                audit.protected_operation_count += 1
            operations_by_tag[tag].append(
                Operation(
                    tag=tag,
                    tag_description=tag_descriptions.get(tag, ""),
                    method=method.upper(),
                    path=path,
                    path_template=path_template,
                    summary=summary.rstrip("."),
                    doc_path=f"api/reference/{slugify(tag)}.md",
                    path_params=path_params,
                    has_query_params=has_query_params,
                    has_payload=has_payload,
                    payload_required=payload_required,
                    payload_schema=payload_schema,
                    response_schema=response_schema,
                    auth_required=not public,
                )
            )

    groups: list[ResourceGroup] = []
    for tag, operations in operations_by_tag.items():
        assign_method_names(operations)
        groups.append(
            ResourceGroup(
                tag=tag,
                description=tag_descriptions.get(tag, ""),
                module_name=snake_case(tag),
                class_name=f"{sanitize_class_name(tag)}Resource",
                doc_path=f"api/reference/{slugify(tag)}.md",
                operations=operations,
            )
        )
    groups.sort(key=lambda group: group.tag.lower())

    schemas = get_schemas(spec)
    info = spec.get("info", {}) if isinstance(spec.get("info"), dict) else {}
    servers = spec.get("servers", [])
    primary_server = DEFAULT_BASE_URL
    if isinstance(servers, list) and servers and isinstance(servers[0], dict):
        primary_server = str(servers[0].get("url") or DEFAULT_BASE_URL)
    audit_summary = AuditSummary(
        title=str(info.get("title") or "Aryeo"),
        version=str(info.get("version") or "unknown"),
        primary_server=primary_server,
        operation_count=sum(len(group.operations) for group in groups),
        path_count=len(paths),
        tag_count=len(groups),
        component_schema_count=len(schemas),
        protected_operation_count=audit.protected_operation_count,
        public_operations=sorted(audit.public_operations),
        request_content_types=sorted(audit.request_content_types),
        response_content_types=sorted(audit.response_content_types),
        inline_request_bodies=sorted(audit.inline_request_bodies),
        inline_enum_paths=count_inline_enum_paths(schemas),
        webhooks_present=bool(spec.get("webhooks")),
    )
    return groups, audit_summary


def count_inline_enum_paths(schemas: dict[str, dict[str, Any]]) -> int:
    """Count enum declarations beneath component schemas."""

    return len(collect_enum_definitions(schemas)[1])


def enum_member_name(value: object, used: set[str]) -> str:
    """Create a valid enum member name for a raw enum value."""

    if isinstance(value, str):
        candidate = sanitize_identifier(value).upper()
    else:
        candidate = sanitize_identifier(str(value)).upper()
    if not candidate:
        candidate = "VALUE"
    if candidate[0].isdigit():
        candidate = f"VALUE_{candidate}"
    original = candidate
    counter = 2
    while candidate in used:
        candidate = f"{original}_{counter}"
        counter += 1
    used.add(candidate)
    return candidate


def enum_path_name(schema_name: str, path: tuple[str, ...]) -> str:
    """Build a deterministic class name for an inline enum path."""

    if not path:
        return sanitize_class_name(schema_name, fallback="Enum")
    path_bits = [bit for bit in path if bit not in {"properties", "items"}]
    return sanitize_class_name(
        "_".join([schema_name, *path_bits, "enum"]), fallback="Enum"
    )


def walk_schema_enums(
    schema: object,
    *,
    schema_name: str,
    path: tuple[str, ...],
    enum_definitions: dict[str, EnumDefinition],
    enum_path_map: dict[str, str],
    used_names: set[str],
) -> None:
    """Collect enum definitions recursively from a schema object."""

    if not isinstance(schema, dict):
        return
    values = schema.get("enum")
    if isinstance(values, list) and values:
        base_name = enum_path_name(schema_name, path)
        class_name = base_name
        counter = 2
        while class_name in used_names:
            class_name = f"{base_name}{counter}"
            counter += 1
        used_names.add(class_name)
        source_path = ".".join((schema_name, *path)) if path else schema_name
        enum_definitions[class_name] = EnumDefinition(
            class_name=class_name,
            source_path=source_path,
            values=tuple(values),
            is_string_enum=all(isinstance(value, str) for value in values),
        )
        enum_path_map[source_path] = class_name

    properties = schema.get("properties")
    if isinstance(properties, dict):
        for property_name, child in properties.items():
            if isinstance(property_name, str):
                walk_schema_enums(
                    child,
                    schema_name=schema_name,
                    path=(*path, "properties", property_name),
                    enum_definitions=enum_definitions,
                    enum_path_map=enum_path_map,
                    used_names=used_names,
                )

    items = schema.get("items")
    if isinstance(items, dict):
        walk_schema_enums(
            items,
            schema_name=schema_name,
            path=(*path, "items"),
            enum_definitions=enum_definitions,
            enum_path_map=enum_path_map,
            used_names=used_names,
        )

    for composition_key in ("allOf", "anyOf", "oneOf"):
        composition = schema.get(composition_key)
        if isinstance(composition, list):
            for index, child in enumerate(composition):
                walk_schema_enums(
                    child,
                    schema_name=schema_name,
                    path=(*path, composition_key, str(index)),
                    enum_definitions=enum_definitions,
                    enum_path_map=enum_path_map,
                    used_names=used_names,
                )


def collect_enum_definitions(
    schemas: dict[str, dict[str, Any]],
) -> tuple[dict[str, EnumDefinition], dict[str, str]]:
    """Collect all component and inline enum definitions."""

    enum_definitions: dict[str, EnumDefinition] = {}
    enum_path_map: dict[str, str] = {}
    used_names: set[str] = set()
    for schema_name, schema in sorted(schemas.items()):
        walk_schema_enums(
            schema,
            schema_name=schema_name,
            path=(),
            enum_definitions=enum_definitions,
            enum_path_map=enum_path_map,
            used_names=used_names,
        )
    return enum_definitions, enum_path_map


def nullable_schema(schema: dict[str, Any]) -> tuple[dict[str, Any], bool]:
    """Return a schema without null-only wrappers and whether null is allowed."""

    schema_type = schema.get("type")
    if schema.get("nullable") is True:
        return schema, True
    if isinstance(schema_type, list) and "null" in schema_type:
        non_null_types = [item for item in schema_type if item != "null"]
        copied = dict(schema)
        copied["type"] = (
            non_null_types[0] if len(non_null_types) == 1 else non_null_types
        )
        return copied, True
    for key in ("anyOf", "oneOf"):
        variants = schema.get(key)
        if not isinstance(variants, list):
            continue
        non_null = [
            item
            for item in variants
            if not (isinstance(item, dict) and item.get("type") == "null")
        ]
        if len(non_null) != len(variants):
            copied = dict(schema)
            copied[key] = non_null
            return copied, True
    return schema, False


def ref_to_class_name(ref: str) -> str:
    """Convert a JSON schema ref into a generated model class name."""

    return sanitize_class_name(ref.rsplit("/", 1)[-1], fallback="Model")


def schema_type_hint(
    schema: object,
    *,
    schemas: dict[str, dict[str, Any]],
    enum_path_map: dict[str, str],
    schema_name: str,
    path: tuple[str, ...],
) -> str:
    """Convert an OpenAPI schema into a Python type hint."""

    _ = schemas
    if not isinstance(schema, dict):
        return "builtins.object"
    schema, nullable = nullable_schema(schema)
    source_path = ".".join((schema_name, *path)) if path else schema_name
    if source_path in enum_path_map:
        hint = enum_path_map[source_path]
    elif "$ref" in schema and isinstance(schema["$ref"], str):
        hint = ref_to_class_name(schema["$ref"])
    elif "const" in schema:
        hint = "builtins.object"
    elif isinstance(schema.get("allOf"), list):
        variants = [
            schema_type_hint(
                variant,
                schemas=schemas,
                enum_path_map=enum_path_map,
                schema_name=schema_name,
                path=(*path, "allOf", str(index)),
            )
            for index, variant in enumerate(schema["allOf"])
        ]
        unique_variants = [variant for variant in dict.fromkeys(variants) if variant]
        hint = unique_variants[0] if len(unique_variants) == 1 else "builtins.object"
    elif isinstance(schema.get("anyOf"), list) or isinstance(schema.get("oneOf"), list):
        key = "anyOf" if isinstance(schema.get("anyOf"), list) else "oneOf"
        variants = [
            schema_type_hint(
                variant,
                schemas=schemas,
                enum_path_map=enum_path_map,
                schema_name=schema_name,
                path=(*path, key, str(index)),
            )
            for index, variant in enumerate(schema[key])
        ]
        unique_variants = [variant for variant in dict.fromkeys(variants) if variant]
        hint = " | ".join(unique_variants) if unique_variants else "builtins.object"
    else:
        schema_type = schema.get("type")
        if schema_type == "array":
            item_hint = schema_type_hint(
                schema.get("items", {}),
                schemas=schemas,
                enum_path_map=enum_path_map,
                schema_name=schema_name,
                path=(*path, "items"),
            )
            hint = f"list[{item_hint}]"
        elif schema_type == "object":
            additional = schema.get("additionalProperties")
            if isinstance(additional, dict):
                value_hint = schema_type_hint(
                    additional,
                    schemas=schemas,
                    enum_path_map=enum_path_map,
                    schema_name=schema_name,
                    path=(*path, "additionalProperties"),
                )
                hint = f"dict[str, {value_hint}]"
            else:
                hint = "dict[str, builtins.object]"
        elif schema_type == "integer":
            hint = "int"
        elif schema_type == "number":
            hint = "float"
        elif schema_type == "boolean":
            hint = "bool"
        elif schema_type == "string":
            hint = "str"
        else:
            hint = "builtins.object"

    if nullable and "None" not in hint:
        return f"{hint} | None"
    return hint


def render_enum_module(enum_definitions: dict[str, EnumDefinition]) -> str:
    """Render ``aryeo/enums.py``."""

    if not enum_definitions:
        return '''"""Generated enum values for the Aryeo API."""

from __future__ import annotations

__all__: list[str] = []
'''

    sections = [
        '"""Generated enum values for the Aryeo API.',
        "",
        "Do not edit by hand; regenerate from docs/api/aryeo.json.",
        '"""',
        "",
        "from __future__ import annotations",
        "",
        "from enum import Enum",
        "",
    ]
    exports: list[str] = []
    for enum_definition in sorted(
        enum_definitions.values(),
        key=lambda definition: definition.class_name,
    ):
        exports.append(enum_definition.class_name)
        base_class = "str, Enum" if enum_definition.is_string_enum else "Enum"
        sections.append(f"class {enum_definition.class_name}({base_class}):")
        sections.append(
            f'    """Allowed values for `{enum_definition.source_path}`."""'
        )
        used_members: set[str] = set()
        for value in enum_definition.values:
            member_name = enum_member_name(value, used_members)
            sections.append(f"    {member_name} = (")
            sections.append(f"        {value!r}")
            sections.append("    )")
        sections.append("")
        sections.append("")

    sections.append("__all__ = [")
    sections.extend(f'    "{name}",' for name in exports)
    sections.append("]")
    return "\n".join(sections)


def render_model_field(
    schema_name: str,
    field_name: str,
    field_schema: object,
    *,
    required_fields: set[str],
    schemas: dict[str, dict[str, Any]],
    enum_path_map: dict[str, str],
) -> str:
    """Render one Pydantic model field."""

    attribute_name = sanitize_identifier(field_name)
    hint = schema_type_hint(
        field_schema,
        schemas=schemas,
        enum_path_map=enum_path_map,
        schema_name=schema_name,
        path=("properties", field_name),
    )
    required = field_name in required_fields
    if not required and "None" not in hint:
        hint = f"{hint} | None"
    default_line = "..." if required else "None"
    return "\n".join(
        [
            f"{MODEL_FIELD_INDENT}{attribute_name}: {hint} = Field(",
            f"{MODEL_FIELD_INDENT}    default={default_line},",
            f'{MODEL_FIELD_INDENT}    alias="{field_name}",',
            f"{MODEL_FIELD_INDENT})",
        ]
    )


def render_model_module(
    schemas: dict[str, dict[str, Any]],
    enum_path_map: dict[str, str],
) -> tuple[str, tuple[str, ...], tuple[str, ...]]:
    """Render ``aryeo/models.py`` and return model metadata."""

    model_sections = [
        '"""Generated Pydantic models for the Aryeo API.',
        "",
        "Fields are derived from docs/api/aryeo.json. Resource methods stay",
        "JSON-based when request or response coercion cannot be inferred safely.",
        '"""',
        "",
        "from __future__ import annotations",
        "",
        "import builtins",
        "",
        "from pydantic import BaseModel, ConfigDict, Field, RootModel",
        "",
    ]
    enum_names = sorted(set(enum_path_map.values()))
    if enum_names:
        model_sections.append("from aryeo.enums import (")
        model_sections.extend(f"    {name}," for name in enum_names)
        model_sections.append(")")
    model_sections.append("")
    model_sections.append("")

    model_names: list[str] = []
    ambiguous: list[str] = []
    for schema_name, schema in sorted(schemas.items()):
        if schema_name in enum_path_map and "properties" not in schema:
            continue
        class_name = sanitize_class_name(schema_name, fallback="Model")
        model_names.append(class_name)
        properties = schema.get("properties")
        schema_type = schema.get("type")
        required_raw = schema.get("required", [])
        required_fields = (
            {item for item in required_raw if isinstance(item, str)}
            if isinstance(required_raw, list)
            else set()
        )

        if isinstance(properties, dict):
            model_sections.append(f"class {class_name}(BaseModel):")
            model_sections.append(
                f'    """Aryeo API schema for `#/components/schemas/{schema_name}`."""'
            )
            model_sections.append("")
            model_sections.append(
                '    model_config = ConfigDict(populate_by_name=True, extra="allow")'
            )
            model_sections.append("")
            for field_name, field_schema in sorted(properties.items()):
                if not isinstance(field_name, str):
                    continue
                model_sections.append(
                    render_model_field(
                        schema_name,
                        field_name,
                        field_schema,
                        required_fields=required_fields,
                        schemas=schemas,
                        enum_path_map=enum_path_map,
                    )
                )
                model_sections.append("")
            model_sections.append("")
            continue

        root_hint = schema_type_hint(
            schema,
            schemas=schemas,
            enum_path_map=enum_path_map,
            schema_name=schema_name,
            path=(),
        )
        if root_hint == class_name:
            root_hint = "builtins.object"
        known_root_type = isinstance(schema_type, str) and schema_type in {
            "array",
            "object",
            "string",
            "integer",
            "number",
            "boolean",
        }
        if not known_root_type:
            ambiguous.append(schema_name)
        model_sections.append(f"class {class_name}(RootModel[{root_hint}]):")
        model_sections.append(
            f'    """Aryeo API root schema for `#/components/schemas/{schema_name}`."""'
        )
        model_sections.append("")
        model_sections.append("")

    model_sections.append("__all__ = [")
    model_sections.extend(f'    "{name}",' for name in model_names)
    model_sections.append("]")
    return "\n".join(model_sections), tuple(model_names), tuple(sorted(ambiguous))


def render_resource_base_module() -> str:
    """Render the shared resource helper."""

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
        """Delegate a JSON request to the shared base client.

        Args:
            method: HTTP method.
            path: API path.
            params: Optional query parameters.
            payload: Optional JSON payload.
            timeout: Optional request timeout override.
            auth_required: Whether a bearer token must be present.

        Returns:
            Decoded JSON response data.
        """

        return self._client.request_json(
            method,
            path,
            params=params,
            payload=payload,
            timeout=timeout,
            auth_required=auth_required,
        )


__all__ = ["ResourceClient"]
'''


def render_resource_base_shim() -> str:
    """Render the compatibility import for the old resource base path."""

    return '''
"""Compatibility import for the generated resource base class."""

from __future__ import annotations

from aryeo._resource import ResourceClient

__all__ = ["ResourceClient"]
'''


def resource_import_list(operations: list[Operation]) -> str:
    """Return type aliases needed by a resource module."""

    import_names = ["JSONResponse", "RequestTimeout"]
    if any(operation.has_payload for operation in operations):
        import_names.append("JSONMapping")
    if any(operation.has_query_params for operation in operations):
        import_names.append("QueryParams")
    return ", ".join(sorted(import_names))


def resource_signature(operation: Operation) -> str:
    """Build a generated resource method signature."""

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
    """Return a docstring payload label."""

    payload_label = operation.payload_schema or "documented payload"
    if payload_label.startswith("inline object"):
        return "the documented inline object payload"
    return payload_label


def resource_doc_lines(operation: Operation) -> list[str]:
    """Render resource method docstring lines."""

    lines = [f'        """{operation.summary}.', "", "        Args:"]
    for path_param in operation.path_params:
        lines.append(f"            {path_param}: The `{path_param}` path value.")
    if operation.has_query_params:
        lines.append(
            "            params: Optional query parameters for the underlying API call."
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
            "            AryeoRequestError: If the request fails before completion.",
            '        """',
        ]
    )
    return lines


def resource_call_arguments(operation: Operation) -> str:
    """Render keyword arguments for the request helper."""

    call_arguments = []
    if operation.has_query_params:
        call_arguments.append("params=params")
    if operation.has_payload:
        call_arguments.append("payload=payload")
    call_arguments.append("timeout=timeout")
    call_arguments.append(f"auth_required={operation.auth_required}")
    return ", ".join(call_arguments)


def resource_path_literal(operation: Operation) -> str:
    """Render the request path literal."""

    if operation.path_params:
        return f'f"{operation.path_template}"'
    return f'"{operation.path}"'


def render_resource_method(operation: Operation) -> str:
    """Render a generated resource method."""

    return "\n".join(
        [
            f"    def {operation.method_name}({resource_signature(operation)}) -> JSONResponse:",
            *resource_doc_lines(operation),
            (
                "        return self._request("
                f'"{operation.method}", {resource_path_literal(operation)}, '
                f"{resource_call_arguments(operation)})"
            ),
        ]
    )


def render_resource_module(group: ResourceGroup) -> str:
    """Render one flat resource module."""

    method_blocks = "\n\n".join(
        render_resource_method(operation) for operation in group.operations
    )
    import_list = resource_import_list(group.operations)
    description = f"Access {group.tag.lower()} API operations."
    return f'''
"""Generated resource client for the {group.tag} API tag."""

from __future__ import annotations

from aryeo._resource import ResourceClient
from aryeo.types import {import_list}


class {group.class_name}(ResourceClient):
    """{description}"""

{method_blocks}


__all__ = ["{group.class_name}"]
'''


def render_resource_shim(group: ResourceGroup) -> str:
    """Render a compatibility module under ``aryeo.resources``."""

    return f'''
"""Compatibility exports for `aryeo.{group.module_name}`."""

from __future__ import annotations

from aryeo.{group.module_name} import {group.class_name}

__all__ = ["{group.class_name}"]
'''


def render_resources_init(resource_groups: list[ResourceGroup]) -> str:
    """Render compatibility exports for ``aryeo.resources``."""

    imports = "\n".join(
        f"from aryeo.{group.module_name} import {group.class_name}"
        for group in resource_groups
    )
    exports = ",\n".join(f'    "{group.class_name}"' for group in resource_groups)
    return f'''
"""Compatibility exports for generated Aryeo resource clients.

Flat modules under `aryeo/` are the primary public surface. This package remains
as a compatibility layer for earlier scaffold imports.
"""

from __future__ import annotations

{imports}

__all__ = [
{exports}
]
'''


def render_types_module() -> str:
    """Render transport-level aliases."""

    return '''
"""Shared transport-level type aliases used by the Aryeo client runtime."""

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

__all__ = [
    "JSONMapping",
    "JSONResponse",
    "JSONScalar",
    "JSONValue",
    "QueryParams",
    "QueryScalar",
    "QueryValue",
    "RequestTimeout",
    "RequestTimeoutTuple",
]
'''


def render_exceptions_module() -> str:
    """Render exception classes."""

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


__all__ = [
    "AryeoAPIError",
    "AryeoConfigurationError",
    "AryeoError",
    "AryeoRequestError",
]
'''


def render_base_client_module() -> str:
    """Render the shared HTTP transport."""

    return f'''
"""Shared HTTP transport helpers for the Aryeo Python client."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, cast

import httpx
from pydantic import BaseModel

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

    def _serialize_payload(
        self,
        payload: JSONMapping | BaseModel | Mapping[str, Any] | None,
    ) -> Mapping[str, Any] | None:
        """Serialize supported JSON payload inputs.

        Args:
            payload: JSON mapping or Pydantic model to send.

        Returns:
            A JSON-compatible mapping, or `None`.
        """

        if payload is None:
            return None
        if isinstance(payload, BaseModel):
            return cast(
                Mapping[str, Any],
                payload.model_dump(by_alias=True, exclude_none=True),
            )
        return payload

    def request_json(
        self,
        method: str,
        path: str,
        *,
        params: QueryParams | None = None,
        payload: JSONMapping | BaseModel | Mapping[str, Any] | None = None,
        timeout: RequestTimeout = None,
        auth_required: bool = True,
    ) -> JSONResponse:
        """Execute a JSON API request and decode the response body.

        Args:
            method: HTTP method to use.
            path: API path that will be joined to the configured base URL.
            params: Optional query string parameters.
            payload: Optional JSON request body or Pydantic model.
            timeout: Optional timeout override for this request.
            auth_required: Whether the request must include the bearer token.

        Returns:
            The decoded JSON response body, or `None` for empty responses.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
            AryeoConfigurationError: If auth is required and no token exists.
        """

        try:
            response = self._http_client.request(
                method=method,
                url=self._build_url(path),
                headers=self._build_headers(auth_required=auth_required),
                params=params,
                json=self._serialize_payload(payload),
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


__all__ = [
    "BaseClient",
    "DEFAULT_BASE_URL",
    "DEFAULT_TIMEOUT",
    "DEFAULT_USER_AGENT",
]
'''


def render_client_module(resource_groups: list[ResourceGroup]) -> str:
    """Render the top-level composed client."""

    imports = "\n".join(
        f"from aryeo.{group.module_name} import {group.class_name}"
        for group in resource_groups
    )
    annotations = "\n".join(
        f"    {group.module_name}: {group.class_name}" for group in resource_groups
    )
    assignments = "\n".join(
        f"        self.{group.module_name} = {group.class_name}(self)"
        for group in resource_groups
    )
    resource_names = "\n".join(
        f'    "{group.module_name}",' for group in resource_groups
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
    """Sync Aryeo API client grouped by documented API tag."""

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

        token = os.getenv(token_env_var)
        if token is None and token_env_var == "ARYEO_API_TOKEN":
            token = os.getenv("ARYEO_API_KEY")

        return cls(
            token=token,
            base_url=os.getenv(base_url_env_var, DEFAULT_BASE_URL),
            timeout=timeout,
        )


__all__ = ["AryeoClient", "RESOURCE_NAMES"]
'''


def parenthesized_import(module: str, names: tuple[str, ...]) -> list[str]:
    """Render a parenthesized import block."""

    if not names:
        return []
    lines = [f"from {module} import ("]
    lines.extend(f"    {name}," for name in names)
    lines.append(")")
    return lines


def render_package_init(
    resource_groups: list[ResourceGroup],
    model_surface: ModelSurface,
) -> str:
    """Render top-level package exports."""

    resource_names = tuple(group.class_name for group in resource_groups)
    lines = [
        '"""Top-level package exports for the Aryeo client."""',
        "",
        "from aryeo.client import AryeoClient",
    ]
    for group in resource_groups:
        lines.append(f"from aryeo.{group.module_name} import {group.class_name}")
    lines.extend(parenthesized_import("aryeo.enums", model_surface.enum_names))
    lines.extend(
        [
            "from aryeo.exceptions import (",
            "    AryeoAPIError,",
            "    AryeoConfigurationError,",
            "    AryeoError,",
            "    AryeoRequestError,",
            ")",
        ]
    )
    lines.extend(parenthesized_import("aryeo.models", model_surface.model_names))
    lines.extend(
        [
            "",
            f'__version__ = "{PROJECT_VERSION}"',
            "",
            "__all__ = [",
            '    "AryeoAPIError",',
            '    "AryeoClient",',
            '    "AryeoConfigurationError",',
            '    "AryeoError",',
            '    "AryeoRequestError",',
        ]
    )
    for name in (
        *resource_names,
        *model_surface.enum_names,
        *model_surface.model_names,
    ):
        lines.append(f'    "{name}",')
    lines.append("]")
    return "\n".join(lines)


def render_pyproject() -> str:
    """Render package and tooling configuration."""

    return f"""
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "{PROJECT_NAME}"
version = "{PROJECT_VERSION}"
description = "Typed Python client for the Aryeo API."
readme = "README.md"
requires-python = ">=3.11"
authors = [{{ name = "Aryeo API Client Maintainers" }}]
keywords = ["aryeo", "real-estate", "api", "python-client"]
classifiers = [
  "Development Status :: 3 - Alpha",
  "Intended Audience :: Developers",
  "Operating System :: OS Independent",
  "Programming Language :: Python :: 3",
  "Programming Language :: Python :: 3.11",
  "Programming Language :: Python :: 3.12",
  "Topic :: Software Development :: Libraries :: Python Modules",
  "Typing :: Typed",
]
dependencies = [
  "httpx>=0.27.0",
  "pydantic>=2.5.0",
]

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
where = ["."]
include = ["aryeo*"]
exclude = ["tests*", "venv*"]

[tool.setuptools.package-data]
aryeo = ["py.typed"]

[tool.black]
line-length = 88
target-version = ["py311"]
include = '\\.pyi?$'

[tool.isort]
profile = "black"
multi_line_output = 3
line_length = 88
known_first_party = ["aryeo"]

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
python_files = ["test_*.py", "*_test.py"]

[tool.coverage.run]
source = ["aryeo"]
branch = true
omit = ["*/tests/*", "*/test_*", "*/__pycache__/*"]

[tool.coverage.report]
show_missing = true
skip_covered = false
exclude_lines = [
  "pragma: no cover",
  "if TYPE_CHECKING:",
  "raise NotImplementedError",
  "if __name__ == .__main__.:",
]

[tool.mypy]
python_version = "3.11"
strict = true
warn_unused_ignores = true
show_error_codes = true

[tool.pydocstyle]
convention = "google"
add-ignore = ["D205", "D212"]
"""


def render_manifest() -> str:
    """Render package manifest."""

    return """
include README.md
include mkdocs.yml
recursive-include aryeo py.typed
recursive-include docs *.md
"""


def render_style_guide() -> str:
    """Render the root style guide."""

    return """
# Style Guide

## Python

- Use Google-style docstrings on public modules, classes, and functions.
- Prefer explicit, thorough type hints over `Any`.
- Keep shared HTTP behavior in `aryeo/base_client.py`.
- Keep flat resource modules such as `aryeo/orders.py` as the primary public
  surface.
- Keep `aryeo/resources/` as compatibility exports only.
- Keep `aryeo/types.py` limited to transport-level aliases.
- Generate models and enums from `docs/api/aryeo.json`; do not invent fields.

## Sync Rules

- Update tests, docs, examples, and planning docs whenever the client surface
  changes.
- Treat `docs/api/` and `docs/planning/aryeo-api-client/` as the contract
  sources before changing endpoint behavior.
- Regenerate the client scaffold with `python tools/bootstrap_client_repo.py`
  after meaningful OpenAPI changes.
"""


def render_readme(resource_groups: list[ResourceGroup], audit: AuditSummary) -> str:
    """Render the project README."""

    rows = [
        [group.tag, f"`aryeo/{group.module_name}.py`", str(len(group.operations))]
        for group in resource_groups
    ]
    return f"""
# Aryeo Python Client

Aryeo is a typed Python client for the Aryeo API. The client is generated from
the checked-in OpenAPI wrapper at `docs/api/aryeo.json` and uses a
client-library repository shape: flat resource modules, explicit exports,
MkDocs documentation, per-resource tests, and release-quality checks.

## Current Scope

- Sync `httpx` transport in `aryeo/base_client.py`
- Flat resource modules for {audit.tag_count} API tags and {audit.operation_count}
  operations
- Generated `aryeo/models.py` and `aryeo/enums.py` from the checked-in spec
- Compatibility exports under `aryeo/resources/`
- Python `>=3.11` by design

Resource methods intentionally return decoded JSON until each endpoint can be
confidently mapped to stable request and response models.

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
    listings = client.listings.list(params={{"page": 1, "per_page": 25}})
```

Set `ARYEO_API_TOKEN` before using protected operations. `ARYEO_API_KEY` is
also accepted as a fallback for local `.env` files. Public operations can be
called without a token.

## Live Integration Checks

Live checks are opt-in and avoid mutating API data by default:

```bash
python tools/verify_live_integrations.py
```

Some resource groups require stable fixture IDs before they can be checked live.
Set `ARYEO_LIVE_ADDRESS_ID`, `ARYEO_LIVE_ORDER_ITEM_ID`,
`ARYEO_LIVE_ORDER_ID`, or `ARYEO_LIVE_VIDEO_ID` for fixture-based reads.

## Regenerate

```bash
python tools/bootstrap_client_repo.py --force-curated
python docs/api/generate_reference.py
```

## Validation

```bash
black --check --diff --line-length=88 .
isort --check-only --diff --profile=black --line-length=88 .
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
flake8 . --count --exit-zero --max-complexity=10 --max-line-length=88 --statistics
mypy aryeo/ --strict --ignore-missing-imports
pytest --cov=aryeo --cov-report=term-missing
mkdocs build --strict
python -m build
python -m twine check dist/*
```

## Resource Groups

{markdown_table(["Tag", "Module", "Operations"], rows)}
"""


def render_docs_requirements() -> str:
    """Render docs requirements."""

    return """
mkdocs-material
mkdocstrings[python]
"""


def render_mkdocs(resource_groups: list[ResourceGroup]) -> str:
    """Render MkDocs configuration."""

    resource_nav = "\n".join(
        f"      - {group.tag}: api-reference/{group.module_name}.md"
        for group in resource_groups
    )
    contract_resource_nav = "\n".join(
        f"          - {group.tag}: {group.doc_path}" for group in resource_groups
    )
    planning_nav = """
          - Planning Overview: planning/aryeo-api-client/README.md
          - Artifact Path Index: planning/aryeo-api-client/ARTIFACT_PATH_INDEX.md
          - Foundation Overview: planning/aryeo-api-client/foundation/README.md
          - Source Of Truth: planning/aryeo-api-client/foundation/api-source-of-truth.md
          - Source Matrix: planning/aryeo-api-client/foundation/source-of-truth-matrix.md
          - Package And Versioning ADR: planning/aryeo-api-client/foundation/package-and-versioning-adr.md
          - Rules And Ownership ADR: planning/aryeo-api-client/foundation/rules-and-ownership-adr.md
          - Trackers Overview: planning/aryeo-api-client/trackers/README.md
          - Readiness Overview: planning/aryeo-api-client/trackers/readiness-overview.md
          - Endpoint Readiness: planning/aryeo-api-client/trackers/endpoint-inventory-readiness.md
          - Coverage Readiness: planning/aryeo-api-client/trackers/coverage-and-tests-readiness.md
          - Docs Readiness: planning/aryeo-api-client/trackers/docs-parity-readiness.md
          - Workflow Readiness: planning/aryeo-api-client/trackers/workflow-release-readiness.md
          - Live Integration Readiness: planning/aryeo-api-client/trackers/live-integration-readiness.md
          - Live Endpoint Checklist: planning/aryeo-api-client/trackers/live-endpoint-verification-checklist.md
          - Execution Overview: planning/aryeo-api-client/execution/README.md
          - Execution Plan: planning/aryeo-api-client/execution/execution-plan.md
          - Roadmap: planning/aryeo-api-client/execution/roadmap.md
          - Bootstrap Plan: planning/aryeo-api-client/execution/api-client-bootstrap-plan.md
          - Phase 00 Source Audit: planning/aryeo-api-client/execution/api_client_PHASE_00_source_audit.md
          - Phase 01 Foundation: planning/aryeo-api-client/execution/api_client_PHASE_01_foundation.md
          - Phase 02 Endpoint Inventory: planning/aryeo-api-client/execution/api_client_PHASE_02_endpoint_inventory.md
          - Phase 03 Tests And Coverage: planning/aryeo-api-client/execution/api_client_PHASE_03_tests_and_coverage.md
          - Phase 04 Docs And Examples: planning/aryeo-api-client/execution/api_client_PHASE_04_docs_and_examples.md
          - Phase 05 Workflows And Release: planning/aryeo-api-client/execution/api_client_PHASE_05_workflows_and_release.md
          - Phase 06 Parity Audit: planning/aryeo-api-client/execution/api_client_PHASE_06_parity_audit.md"""
    return f"""
site_name: Aryeo Python Client
site_description: Typed Python client for the Aryeo API

theme:
  name: material
  language: en
  features:
    - navigation.tabs
    - navigation.sections
    - navigation.expand
    - navigation.top
    - search.highlight
    - search.suggest
    - content.code.copy
    - toc.follow

plugins:
  - search
  - mkdocstrings:
      handlers:
        python:
          paths: [.]
          options:
            docstring_style: google
            merge_init_into_class: true
            show_source: false
            show_signature_annotations: true
            show_root_heading: true
            show_submodules: false

markdown_extensions:
  - admonition
  - attr_list
  - def_list
  - tables
  - toc:
      permalink: true

nav:
  - Home: index.md
  - Getting Started:
      - getting-started/index.md
      - Installation: getting-started/installation.md
      - Authentication: getting-started/authentication.md
      - Quickstart: getting-started/quickstart.md
  - Guides:
      - guides/index.md
      - Examples: guides/examples.md
      - Orders: guides/orders.md
      - Listings: guides/listings.md
      - Appointments: guides/appointments.md
      - Live Checks: guides/live-checks.md
  - API Reference:
      - api-reference/index.md
      - Client: api-reference/client.md
      - Base Client: api-reference/base-client.md
      - Exceptions: api-reference/exceptions.md
      - Models: api-reference/models.md
      - Enums: api-reference/enums.md
{resource_nav}
  - Reference:
      - reference/index.md
      - API Contract Overview: api/README.md
      - API Authentication: api/guides/authentication.md
      - API Errors: api/guides/errors.md
      - API Pagination: api/guides/pagination.md
      - API Reference Index: api/reference/README.md
      - API Tag Reference:
{contract_resource_nav}
      - Changelog: reference/changelog.md
  - Development:
      - development/index.md
      - Contributing: development/contributing.md
      - Planning Guide: development/planning.md
      - Style Guide: STYLE_GUIDE.md
      - Planning Artifacts:
{planning_nav}
"""


def render_docs_index(audit: AuditSummary) -> str:
    """Render docs home page."""

    return f"""
# Aryeo Python Client

This documentation is for the Python client library generated from the checked-in
Aryeo API contract.

## What Is Included

- {audit.operation_count} operations across {audit.tag_count} resource modules
- Sync `httpx` transport with bearer-token auth
- Generated models and enums from `docs/api/aryeo.json`
- Client-library docs, tests, and release hygiene

Start with [Quickstart](getting-started/quickstart.md), then browse the
[API Reference](api-reference/index.md).
"""


def render_simple_doc(title: str, body: str) -> str:
    """Render a titled Markdown page."""

    return f"# {title}\n\n{body.strip()}\n"


def render_api_reference_page(module: str, title: str) -> str:
    """Render a mkdocstrings page for a module."""

    return f"# {title}\n\n::: {module}\n"


def build_docs_files(
    resource_groups: list[ResourceGroup],
    audit: AuditSummary,
) -> list[tuple[Path, str]]:
    """Build documentation files."""

    files: list[tuple[Path, str]] = [
        (REPO_ROOT / "docs" / "requirements.txt", render_docs_requirements()),
        (REPO_ROOT / "docs" / "index.md", render_docs_index(audit)),
        (
            REPO_ROOT / "docs" / "getting-started" / "index.md",
            render_simple_doc(
                "Getting Started",
                "Install the package, configure authentication, and make the first "
                "safe read request.",
            ),
        ),
        (
            REPO_ROOT / "docs" / "getting-started" / "installation.md",
            render_simple_doc(
                "Installation",
                'Use `python -m pip install -e ".[dev]"` for local development. '
                "Aryeo intentionally supports Python `>=3.11` in this repo.",
            ),
        ),
        (
            REPO_ROOT / "docs" / "getting-started" / "authentication.md",
            render_simple_doc(
                "Authentication",
                "`AryeoClient.from_env()` reads `ARYEO_API_TOKEN`, with "
                "`ARYEO_API_KEY` as a local fallback. Public operations preserve the "
                "OpenAPI contract and do not require a token.",
            ),
        ),
        (
            REPO_ROOT / "docs" / "getting-started" / "quickstart.md",
            render_simple_doc(
                "Quickstart",
                "```python\nfrom aryeo import AryeoClient\n\n"
                "with AryeoClient.from_env() as client:\n"
                '    client.orders.list(params={"page": 1, "per_page": 25})\n'
                "```",
            ),
        ),
        (
            REPO_ROOT / "docs" / "guides" / "index.md",
            render_simple_doc(
                "Guides",
                "Workflow guides focus on safe request construction and opt-in live "
                "checks.",
            ),
        ),
        (
            REPO_ROOT / "docs" / "guides" / "examples.md",
            render_simple_doc(
                "Examples",
                "See `examples/quickstart.py`, `examples/list_orders.py`, "
                "`examples/list_listings.py`, `examples/appointments_workflow.py`, "
                "and `examples/customer_users_lookup.py`.",
            ),
        ),
        (
            REPO_ROOT / "docs" / "guides" / "orders.md",
            render_simple_doc(
                "Orders",
                "`client.orders` supports documented order listing, creation, lookup, "
                "billing-address updates, manual payments, and public payment-info "
                "retrieval.",
            ),
        ),
        (
            REPO_ROOT / "docs" / "guides" / "listings.md",
            render_simple_doc(
                "Listings",
                "`client.listings` exposes listing list, create, get, update, "
                "Cubicasa, detail search, and stats operations from the spec.",
            ),
        ),
        (
            REPO_ROOT / "docs" / "guides" / "appointments.md",
            render_simple_doc(
                "Appointments",
                "`client.appointments` preserves all documented appointment lifecycle "
                "paths. Mutating workflows should be run only against safe fixtures.",
            ),
        ),
        (
            REPO_ROOT / "docs" / "guides" / "live-checks.md",
            render_simple_doc(
                "Live Checks",
                "Run `python tools/verify_live_integrations.py` only when you have "
                "safe credentials. Default checks avoid mutating API data.",
            ),
        ),
        (
            REPO_ROOT / "docs" / "api-reference" / "index.md",
            render_simple_doc(
                "API Reference",
                "The Python API reference covers the client, resource modules, "
                "transport, exceptions, models, and enums.",
            ),
        ),
        (
            REPO_ROOT / "docs" / "api-reference" / "client.md",
            render_api_reference_page("aryeo.client", "Client"),
        ),
        (
            REPO_ROOT / "docs" / "api-reference" / "base-client.md",
            render_api_reference_page("aryeo.base_client", "Base Client"),
        ),
        (
            REPO_ROOT / "docs" / "api-reference" / "exceptions.md",
            render_api_reference_page("aryeo.exceptions", "Exceptions"),
        ),
        (
            REPO_ROOT / "docs" / "api-reference" / "models.md",
            render_api_reference_page("aryeo.models", "Models"),
        ),
        (
            REPO_ROOT / "docs" / "api-reference" / "enums.md",
            render_api_reference_page("aryeo.enums", "Enums"),
        ),
        (
            REPO_ROOT / "docs" / "reference" / "index.md",
            render_simple_doc(
                "Reference",
                "This section keeps API-contract docs and release notes separate from "
                "the Python module reference.",
            ),
        ),
        (
            REPO_ROOT / "docs" / "reference" / "changelog.md",
            render_simple_doc(
                "Changelog",
                "Release notes are not yet published for this scaffold.",
            ),
        ),
        (
            REPO_ROOT / "docs" / "development" / "index.md",
            render_simple_doc(
                "Development",
                "Development docs cover contribution commands, planning artifacts, "
                "and repository maintenance.",
            ),
        ),
        (
            REPO_ROOT / "docs" / "development" / "contributing.md",
            render_simple_doc(
                "Contributing",
                "Run the validation command set from `README.md` before proposing "
                "changes. Keep generated files synchronized with `docs/api/aryeo.json`.",
            ),
        ),
        (
            REPO_ROOT / "docs" / "development" / "planning.md",
            render_simple_doc(
                "Planning Guide",
                "Planning docs live under `docs/planning/aryeo-api-client/` and are "
                "development artifacts, not primary user-facing docs.",
            ),
        ),
        (
            REPO_ROOT / "docs" / "STYLE_GUIDE.md",
            render_simple_doc(
                "Documentation Style Guide",
                "Use concise task-oriented pages, Google-style docstrings for Python "
                "API reference, and keep API-contract claims tied to `docs/api/`.",
            ),
        ),
    ]
    for group in resource_groups:
        files.append(
            (
                REPO_ROOT / "docs" / "api-reference" / f"{group.module_name}.md",
                render_api_reference_page(
                    f"aryeo.{group.module_name}",
                    group.tag,
                ),
            )
        )
    return files


def render_example_quickstart() -> str:
    """Render quickstart example."""

    return '''
"""Quickstart example for the Aryeo client."""

from __future__ import annotations

from aryeo import AryeoClient


def main() -> None:
    """Run a small safe read example against the Aryeo API."""

    with AryeoClient.from_env() as client:
        client.orders.list(params={"page": 1, "per_page": 5})
        client.listings.list(params={"page": 1, "per_page": 5})


if __name__ == "__main__":
    main()
'''


def render_example_orders() -> str:
    """Render order example."""

    return f'''
"""Example workflow for loading orders from Aryeo."""

from __future__ import annotations

from aryeo import AryeoClient


def main() -> None:
    """List orders and fetch public payment information for a fixture order."""

    with AryeoClient.from_env() as client:
        client.orders.list(params={{"page": 1, "per_page": 10}})
        client.orders.get_payment_information("{UUID_EXAMPLE}")


if __name__ == "__main__":
    main()
'''


def render_example_listings() -> str:
    """Render listing example."""

    return f'''
"""Example workflow for listing reads."""

from __future__ import annotations

from aryeo import AryeoClient


def main() -> None:
    """List listings and fetch details for a fixture listing."""

    with AryeoClient.from_env() as client:
        client.listings.list(params={{"page": 1, "per_page": 10}})
        client.listings.get("{UUID_EXAMPLE}")


if __name__ == "__main__":
    main()
'''


def render_example_appointments() -> str:
    """Render appointment example."""

    return f'''
"""Example workflow for appointment availability reads."""

from __future__ import annotations

from aryeo import AryeoClient


def main() -> None:
    """Check appointment availability for a fixture appointment."""

    with AryeoClient.from_env() as client:
        client.appointments.check_availability("{UUID_EXAMPLE}", params={{"page": 1}})


if __name__ == "__main__":
    main()
'''


def render_example_customer_users() -> str:
    """Render customer-user example."""

    return '''
"""Example workflow for customer user lookup."""

from __future__ import annotations

from aryeo import AryeoClient


def main() -> None:
    """List customer users using documented query parameters."""

    with AryeoClient.from_env() as client:
        client.customer_users.list(params={"page": 1, "per_page": 10})


if __name__ == "__main__":
    main()
'''


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


def render_tests_helpers() -> str:
    """Render shared request assertion helpers."""

    return '''
"""Helpers shared by generated resource tests."""

from __future__ import annotations

from typing import Protocol

import httpx

from aryeo.base_client import DEFAULT_BASE_URL
from aryeo.client import AryeoClient
from aryeo.types import JSONResponse


class ClientFactory(Protocol):
    """Protocol for the test client factory fixture."""

    def __call__(
        self,
        token: str | None = "test-token",
        response_body: JSONResponse | None = None,
        status_code: int = 200,
    ) -> tuple[AryeoClient, list[httpx.Request]]:
        """Create a mocked Aryeo client."""


def assert_resource_method_request(
    client_factory: ClientFactory,
    *,
    resource_name: str,
    method_name: str,
    path_arguments: dict[str, str],
    call_kwargs: dict[str, object],
    expected_method: str,
    expected_path: str,
    auth_required: bool,
) -> None:
    """Assert that a generated resource method builds the expected request."""

    token = "test-token" if auth_required else None
    client, requests = client_factory(token)
    resource = getattr(client, resource_name)
    method = getattr(resource, method_name)

    response = method(**path_arguments, **call_kwargs)

    assert response == {"ok": True}
    assert requests[0].method == expected_method
    base_path = httpx.URL(DEFAULT_BASE_URL).path.rstrip("/")
    assert requests[0].url.path == (
        f"{base_path}{expected_path.format(**path_arguments)}"
    )
    if auth_required:
        assert requests[0].headers["Authorization"] == "Bearer test-token"
    else:
        assert "Authorization" not in requests[0].headers
'''


def render_tests_base_client() -> str:
    """Render base client tests."""

    return '''
"""Unit tests for the shared Aryeo base client."""

from __future__ import annotations

import pytest

from aryeo.exceptions import AryeoConfigurationError


def test_request_json_includes_auth_header(client_factory: object) -> None:
    """Protected requests should include the bearer token."""

    client, requests = client_factory("token-value")
    response = client.request_json("GET", "/appointments", params={"page": 1})

    assert response == {"ok": True}
    assert requests[0].headers["Authorization"] == "Bearer token-value"
    assert requests[0].url.params["page"] == "1"


def test_request_json_allows_public_requests_without_token(
    client_factory: object,
) -> None:
    """Public endpoints should work when no bearer token is configured."""

    client, requests = client_factory(None)
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

    client, _ = client_factory(None)

    with pytest.raises(AryeoConfigurationError):
        client.request_json("GET", "/appointments")
'''


def render_tests_client(resource_groups: list[ResourceGroup]) -> str:
    """Render high-level client tests."""

    first_group = resource_groups[0]
    return f'''
"""Unit tests for the high-level Aryeo client."""

from __future__ import annotations

from aryeo import AryeoClient, {first_group.class_name}
from aryeo.client import RESOURCE_NAMES


def test_client_exposes_generated_resources(client_factory: object) -> None:
    """The top-level client should expose each generated resource attribute."""

    client, _ = client_factory("token-value")

    for resource_name in RESOURCE_NAMES:
        assert hasattr(client, resource_name)


def test_top_level_exports_include_resource_client() -> None:
    """The package should export public resource client classes."""

    assert {first_group.class_name}.__name__ == "{first_group.class_name}"


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
    """Render exception tests."""

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


def render_tests_models(model_surface: ModelSurface) -> str:
    """Render tests for generated models and enums."""

    model_name = model_surface.model_names[0] if model_surface.model_names else None
    enum_name = model_surface.enum_names[0] if model_surface.enum_names else None
    imports = []
    if enum_name:
        imports.append(f"from aryeo.enums import {enum_name}")
    if model_name:
        imports.append(f"from aryeo.models import {model_name}")
    import_block = "\n".join(imports)
    model_assertion = (
        f'    assert {model_name}.__name__ == "{model_name}"'
        if model_name
        else "    assert True"
    )
    enum_assertion = (
        f'    assert {enum_name}.__name__ == "{enum_name}"'
        if enum_name
        else "    assert True"
    )
    return f'''
"""Tests for generated Aryeo models and enums."""

from __future__ import annotations

{import_block}


def test_generated_model_is_importable() -> None:
    """Generated models should be importable from `aryeo.models`."""

{model_assertion}


def test_generated_enum_is_importable() -> None:
    """Generated enums should be importable from `aryeo.enums`."""

{enum_assertion}
'''


def render_resource_test(group: ResourceGroup) -> str:
    """Render one per-resource request-construction test module."""

    cases: list[str] = []
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
            "\n".join(
                [
                    "    (",
                    f'        "{operation.method_name}",',
                    f"        {path_arguments!r},",
                    f"        {call_kwargs!r},",
                    f'        "{operation.method}",',
                    f'        "{operation.path_template}",',
                    f"        {operation.auth_required},",
                    "    ),",
                ]
            )
        )
    cases_text = "\n".join(cases)
    return f'''
"""Request-construction tests for `aryeo.{group.module_name}`."""

from __future__ import annotations

import pytest

from tests.helpers import ClientFactory, assert_resource_method_request

CASES = [
{cases_text}
]


@pytest.mark.parametrize(
    (
        "method_name",
        "path_arguments",
        "call_kwargs",
        "expected_method",
        "expected_path",
        "auth_required",
    ),
    CASES,
)
def test_{group.module_name}_resource_methods(
    client_factory: ClientFactory,
    method_name: str,
    path_arguments: dict[str, str],
    call_kwargs: dict[str, object],
    expected_method: str,
    expected_path: str,
    auth_required: bool,
) -> None:
    """Each {group.tag} method should issue the documented HTTP request."""

    assert_resource_method_request(
        client_factory,
        resource_name="{group.module_name}",
        method_name=method_name,
        path_arguments=path_arguments,
        call_kwargs=call_kwargs,
        expected_method=expected_method,
        expected_path=expected_path,
        auth_required=auth_required,
    )
'''


def render_ci_workflow() -> str:
    """Render CI workflow."""

    return """
name: CI

on:
  push:
  pull_request:

jobs:
  quality:
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
      - run: python -m build
      - run: python -m twine check dist/*
      - run: pip-audit
"""


def render_release_workflow() -> str:
    """Render release workflow."""

    gates = """
      - run: black --check --diff --line-length=88 .
      - run: isort --check-only --diff --profile=black --line-length=88 .
      - run: flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
      - run: >-
          flake8 . --count --exit-zero --max-complexity=10
          --max-line-length=88 --statistics
      - run: mypy aryeo/ --strict --ignore-missing-imports
      - run: pytest --cov=aryeo --cov-report=xml --cov-report=term-missing
      - run: mkdocs build --strict
      - run: python -m build
      - run: python -m twine check dist/*"""
    return f"""
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
{gates}
      - uses: pypa/gh-action-pypi-publish@release/v1
"""


def render_unified_deployment_workflow() -> str:
    """Render manual deployment workflow."""

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
      - run: black --check --diff --line-length=88 .
      - run: isort --check-only --diff --profile=black --line-length=88 .
      - run: flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
      - run: >-
          flake8 . --count --exit-zero --max-complexity=10
          --max-line-length=88 --statistics
      - run: mypy aryeo/ --strict --ignore-missing-imports
      - run: pytest --cov=aryeo --cov-report=xml --cov-report=term-missing
      - run: mkdocs build --strict
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


def render_docs_workflow() -> str:
    """Render docs workflow."""

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
    """Render security audit workflow."""

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
      - run: python -m pip install -r docs/requirements.txt
      - run: pip-audit
"""


def render_dependabot() -> str:
    """Render Dependabot configuration."""

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
    """Render API source-truth Cursor rule."""

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
    """Render implementation Cursor rule."""

    return f"""
---
description: Implementation rules for the Aryeo Python API client project.
globs:
alwaysApply: true
---
Implement runtime code under `./{PACKAGE_NAME}/` and group endpoints by resource
or service boundary.

Use flat modules such as `aryeo/orders.py` as the primary resource surface.
Keep `aryeo/resources/` as compatibility re-export modules only.

Use Google-style docstrings and thorough type hints for Python files.

Every endpoint or client change must update:
- tests under `./tests/`
- docs under `./docs/`
- examples under `./examples/` when user-facing usage changes
- the owning planning docs under `docs/planning/{INITIATIVE_SLUG}/`

Do not mark an endpoint or model complete until code, tests, docs, examples,
and status docs land.
"""


def render_rule_docs_tests_sync() -> str:
    """Render docs/tests Cursor rule."""

    return f"""
---
description: Keep docs, tests, and examples aligned with the Aryeo client surface.
globs:
alwaysApply: true
---
When scaffolding or changing the client surface, keep `README.md`, `docs/`,
`examples/`, and `tests/` synchronized with the same commands and supported
Python versions.

Use pytest with coverage on `{PACKAGE_NAME}` and keep one test module per public
resource module where practical.

Docs must build with `mkdocs build --strict` before the work is considered
ready.
"""


def render_rule_release_quality() -> str:
    """Render release-quality Cursor rule."""

    return f"""
---
description: Quality and release rules for the Aryeo Python client project.
globs:
alwaysApply: true
---
Before changing CI or release behavior, keep `pyproject.toml`,
`{PACKAGE_NAME}/__init__.py`, and the release workflow aligned on versioning.

CI and release validation must cover formatting, import order, lint, typing,
tests, package build, strict docs build, and dependency/security audit.

Use Dependabot as the default dependency automation tool unless the planning
docs record an intentional exception.
"""


def phase_rows() -> list[dict[str, str]]:
    """Return planning phase rows for generated trackers."""

    return [
        {
            "title": "Phase 0 - Source Audit",
            "status": "Complete",
            "goal": "Establish one honest API source of truth.",
            "paths": "docs/api/, docs/planning/.../foundation/",
            "acceptance": "Base contract, inventory, and contradictions are documented.",
            "risk": "Implementation can drift from the checked-in docs.",
        },
        {
            "title": "Phase 1 - Foundation And Packaging",
            "status": "Complete",
            "goal": "Create the package identity and shared runtime primitives.",
            "paths": "pyproject.toml, aryeo/, README.md",
            "acceptance": "Package metadata, core transport, and exceptions exist.",
            "risk": "Later endpoint work has no stable runtime contract.",
        },
        {
            "title": "Phase 2 - Endpoint Inventory And Models",
            "status": "In Progress",
            "goal": "Map all endpoints into flat resources and generated models.",
            "paths": "aryeo/*.py, aryeo/models.py, aryeo/enums.py",
            "acceptance": "Generated resources, models, and enums cover the spec.",
            "risk": "Resource and model coverage becomes ad hoc.",
        },
        {
            "title": "Phase 3 - Tests And Coverage",
            "status": "In Progress",
            "goal": "Exercise core behavior and per-resource request construction.",
            "paths": "tests/",
            "acceptance": "Core, model/export, and per-resource tests pass.",
            "risk": "Transport regressions slip in unnoticed.",
        },
        {
            "title": "Phase 4 - Docs And Examples",
            "status": "In Progress",
            "goal": "Publish client-library docs and safe examples.",
            "paths": "docs/, mkdocs.yml, examples/",
            "acceptance": "Docs use client-library navigation and strict builds pass.",
            "risk": "Users cannot discover the client shape.",
        },
        {
            "title": "Phase 5 - Workflows And Release",
            "status": "In Progress",
            "goal": "Keep CI, release, docs, and security gates aligned.",
            "paths": ".github/workflows/, .github/dependabot.yml",
            "acceptance": "Release paths run the same core validation as CI.",
            "risk": "Tags can publish lower-quality artifacts than PRs.",
        },
        {
            "title": "Phase 6 - Parity Audit",
            "status": "Pending",
            "goal": "Compare implementation claims against code, tests, and docs.",
            "paths": "docs/planning/.../trackers/, execution/",
            "acceptance": "Remaining gaps are explicit and prioritized.",
            "risk": "The repo may look more complete than it is.",
        },
    ]


def render_planning_root_readme() -> str:
    """Render planning landing page."""

    return """
# Aryeo API Client Planning

This planning tree is docs-only and owns the long-lived roadmap for the Aryeo
Python client scaffold.

## Status Snapshot

- Phase 0 and Phase 1 are complete.
- Phase 2 through Phase 5 are in progress while flat modules, generated models,
  docs, tests, and release gates are being proven.
- Phase 6 remains the honesty pass for endpoint/model parity and live checks.

## Fastest Reality Checks

- `foundation/api-source-of-truth.md`
- `foundation/source-of-truth-matrix.md`
- `trackers/readiness-overview.md`
- `execution/execution-plan.md`

## Active Plan

- `execution/api-client-bootstrap-plan.md`
"""


def render_artifact_index() -> str:
    """Render artifact path index."""

    return f"""
# Artifact Path Index

- Planning root: `docs/planning/{INITIATIVE_SLUG}/`
- Repo rules: `.cursor/rules/`
- Package directory: `{PACKAGE_NAME}/`
- Flat resources: `{PACKAGE_NAME}/<resource>.py`
- Compatibility resources: `{PACKAGE_NAME}/resources/`
- Models and enums: `{PACKAGE_NAME}/models.py`, `{PACKAGE_NAME}/enums.py`
- Tests: `tests/`
- Docs site: `docs/`
- Examples: `examples/`
- Workflows: `.github/workflows/`
- Dependency automation: `.github/dependabot.yml`
"""


def render_api_source_of_truth(
    resource_groups: list[ResourceGroup],
    audit: AuditSummary,
    model_surface: ModelSurface,
) -> str:
    """Render source-of-truth foundation doc."""

    inputs_table = markdown_table(
        ["Source", "Path", "Status", "Why it matters"],
        [
            [
                "Generated API overview",
                "`docs/api/README.md`",
                "Used",
                "Summarizes counts and generated API contract docs.",
            ],
            [
                "OpenAPI wrapper",
                "`docs/api/aryeo.json`",
                "Used",
                "Canonical machine-readable endpoint and schema contract.",
            ],
            [
                "Generated API guides",
                "`docs/api/guides/`",
                "Used",
                "Documents auth, errors, and pagination.",
            ],
        ],
    )
    base_contract = markdown_table(
        ["Area", "Current answer", "Canonical source"],
        [
            ["Base URL", f"`{audit.primary_server}`", "`docs/api/aryeo.json`"],
            [
                "Authentication",
                (
                    f"Bearer token on {audit.protected_operation_count} operations; "
                    f"{len(audit.public_operations)} are public"
                ),
                "`docs/api/guides/authentication.md`",
            ],
            ["Versioning", f"Spec version `{audit.version}`", "`docs/api/README.md`"],
            ["Pagination", "`page` and `per_page` query patterns", "`docs/api/`"],
            ["Errors", "Shared 4xx and 5xx JSON payloads", "`docs/api/`"],
            ["Rate limits", "Not documented", "`docs/api/aryeo.json`"],
        ],
    )
    resource_inventory = markdown_table(
        ["Resource group", "Coverage status", "Notes"],
        [
            [
                group.tag,
                "Flat resource generated",
                f"{len(group.operations)} operations in `aryeo/{group.module_name}.py`",
            ]
            for group in resource_groups
        ],
    )
    gaps = [
        "- Rate limits and retry budgets are not documented in checked-in sources.",
        "- No webhook or async callback contract is present.",
        (
            "- Resource methods remain JSON-based until endpoint-specific model "
            "coercion can be proven with tests and examples."
        ),
    ]
    if model_surface.ambiguous_schemas:
        gaps.append(
            "- Ambiguous schemas retained JSON-compatible fallback typing: "
            + ", ".join(f"`{name}`" for name in model_surface.ambiguous_schemas[:20])
            + ("." if len(model_surface.ambiguous_schemas) <= 20 else ", ...")
        )
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

## Model And Enum Inventory

- Generated models: {len(model_surface.model_names)}
- Generated enums: {len(model_surface.enum_names)}
- Inline enum paths found: {audit.inline_enum_paths}

## Contradictions And Gaps

{chr(10).join(gaps)}
"""


def render_source_matrix(audit: AuditSummary, model_surface: ModelSurface) -> str:
    """Render source matrix."""

    rows = [
        ["Authentication", "`docs/api/guides/authentication.md`", "High", "None"],
        ["Base URL and versioning", "`docs/api/aryeo.json`", "High", "None"],
        ["Resource grouping", "`docs/api/reference/README.md`", "High", "None"],
        [
            "Request/response schemas",
            "`docs/api/aryeo.json`",
            "Medium",
            "Models generated; resource coercion deferred",
        ],
        [
            "Enums",
            "`docs/api/aryeo.json`",
            "Medium",
            f"{len(model_surface.enum_names)} enum classes generated",
        ],
        ["Pagination", "`docs/api/guides/pagination.md`", "High", "None"],
        ["Rate limits", "`docs/api/aryeo.json`", "Low", "No limit guidance documented"],
        ["Webhooks", "`docs/api/aryeo.json`", "Low", "No webhook section present"],
    ]
    return f"""
# Source Of Truth Matrix

{markdown_table(["Topic", "Canonical source", "Confidence", "Follow-up"], rows)}
"""


def render_package_versioning_adr() -> str:
    """Render package/version ADR."""

    return f"""
# Package And Versioning ADR

## Decision

- Distribution name: `{PROJECT_NAME}`
- Import package: `{PACKAGE_NAME}`
- Initial version: `{PROJECT_VERSION}`
- Version sources of truth: `pyproject.toml` and `{PACKAGE_NAME}/__init__.py`
- Python support: `>=3.11`

## Intentional Project Decisions

- Aryeo keeps Python `>=3.11` to avoid broad syntax and CI refactors in this
  pass.
- Aryeo keeps `httpx` as its sync transport.

## Follow-Up

- Confirm PyPI name availability before publication.
- Decide when typed endpoint coercion justifies a `1.0.0` stability target.
"""


def render_rules_ownership_adr() -> str:
    """Render rules/ownership ADR."""

    return f"""
# Rules And Ownership ADR

## Planning Ownership

- `docs/planning/{INITIATIVE_SLUG}/` owns roadmap, readiness, and truthful status.
- `.cursor/rules/` owns repo-local AI guidance derived from the planning tree.

## Runtime Ownership

- `{PACKAGE_NAME}/base_client.py` owns transport, auth, and error behavior.
- `{PACKAGE_NAME}/client.py` owns resource bindings.
- `{PACKAGE_NAME}/<resource>.py` owns generated endpoint methods by tag.
- `{PACKAGE_NAME}/models.py` and `{PACKAGE_NAME}/enums.py` own generated schema
  types.
- `{PACKAGE_NAME}/resources/` owns compatibility re-exports only.

## Supporting Surfaces

- `tests/` owns regression coverage.
- `docs/` owns published documentation and examples.
- `.github/workflows/` owns automation and release quality checks.
"""


def render_readiness_overview() -> str:
    """Render readiness overview."""

    rows = [[phase["title"], phase["status"], phase["goal"]] for phase in phase_rows()]
    return (
        f"# Readiness Overview\n\n{markdown_table(['Phase', 'Status', 'Goal'], rows)}\n"
    )


def render_endpoint_inventory(resource_groups: list[ResourceGroup]) -> str:
    """Render endpoint readiness tracker."""

    rows = [
        [
            group.tag,
            str(len(group.operations)),
            f"`aryeo/{group.module_name}.py`",
            f"`{group.doc_path}`",
            "Flat low-level methods generated; typed resource coercion deferred",
        ]
        for group in resource_groups
    ]
    return f"""
# Endpoint Inventory Readiness

{markdown_table(["Resource group", "Ops", "Module", "Doc source", "Current status"], rows)}
"""


def render_coverage_readiness(resource_groups: list[ResourceGroup]) -> str:
    """Render coverage readiness tracker."""

    rows = [
        ["Core transport tests", "Present", "`tests/test_base_client.py`"],
        ["Client wiring tests", "Present", "`tests/test_client.py`"],
        ["Exception tests", "Present", "`tests/test_exceptions.py`"],
        ["Model/export tests", "Present", "`tests/test_models.py`"],
        [
            "Per-resource tests",
            "Present",
            f"{len(resource_groups)} generated `tests/test_<resource>.py` files",
        ],
        ["Live integration tests", "Opt-in", "Safe checks remain outside default CI"],
    ]
    return f"# Coverage And Tests Readiness\n\n{markdown_table(['Area', 'Status', 'Notes'], rows)}\n"


def render_docs_readiness() -> str:
    """Render docs readiness tracker."""

    rows = [
        ["README", "Present", "Explains Aryeo's client-library structure"],
        [
            "MkDocs nav",
            "Present",
            "Home, Getting Started, Guides, API Reference, Reference, Development",
        ],
        ["API reference", "Present", "Every public resource module has a page"],
        ["API contract docs", "Present", "Kept under Reference"],
        ["Planning docs", "Development only", "Moved out of primary user-facing nav"],
    ]
    return f"# Docs Parity Readiness\n\n{markdown_table(['Surface', 'Status', 'Notes'], rows)}\n"


def render_workflow_readiness() -> str:
    """Render workflow readiness tracker."""

    rows = [
        ["CI", "Present", "Format, imports, flake8, mypy, pytest, docs, build, audit"],
        ["Docs", "Present", "Strict MkDocs build"],
        ["Security", "Present", "Scheduled and manual `pip-audit`"],
        ["Release", "Present", "Runs CI-like gates before Trusted Publishing"],
        ["Unified deployment", "Present", "Manual validation mirrors release gates"],
        ["Dependabot", "Present", "Weekly pip/docs/actions updates"],
    ]
    return f"# Workflow Release Readiness\n\n{markdown_table(['Area', 'Status', 'Notes'], rows)}\n"


def render_execution_plan(model_surface: ModelSurface) -> str:
    """Render live execution ledger."""

    return f"""
# Execution Plan

## Already Scaffolded

- Core runtime modules for transport, exceptions, and flat resource bindings
- Generated resource modules for every documented API tag
- Generated `{PACKAGE_NAME}/models.py` and `{PACKAGE_NAME}/enums.py`
- Planning docs and Cursor rules
- Examples, MkDocs config, tests, and workflow scaffolding

## Only Planned

- Endpoint-specific request and response coercion using generated models
- Live integration tests against a safe non-production environment
- First live trusted release after PyPI publisher registration

## Highest-Risk Remaining Surface

- The client is resource-complete at the transport layer, but endpoint methods
  still return decoded JSON until model coercion is proven endpoint by endpoint.

## Current Blockers

- Rate limits and live retry guidance are undocumented.
- Integration validation needs safe credentials and stable fixtures.
- Ambiguous generated schema fallbacks: {len(model_surface.ambiguous_schemas)}
"""


def render_roadmap() -> str:
    """Render roadmap."""

    rows = [
        [
            phase["title"],
            phase["goal"],
            phase["paths"],
            phase["acceptance"],
            phase["risk"],
        ]
        for phase in phase_rows()
    ]
    return f"""
# Roadmap

{markdown_table(["Phase", "Why it exists", "Files or directories", "Acceptance", "Risk if skipped"], rows)}
"""


def render_bootstrap_plan() -> str:
    """Render active bootstrap plan."""

    sections = []
    for phase in phase_rows():
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

- Maintain a typed Python client baseline from the checked-in Aryeo API docs.

## Current Focus

- Client-library package structure, generated models/enums, per-resource tests, and
  release hygiene.

## Ordered Phases

{chr(10).join(sections)}
"""


def render_phase_doc(title: str, lines: list[str]) -> str:
    """Render a phase proof document."""

    return f"# {title}\n\n{chr(10).join(lines)}\n"


def build_planning_files(
    resource_groups: list[ResourceGroup],
    audit: AuditSummary,
    model_surface: ModelSurface,
) -> list[tuple[Path, str]]:
    """Build planning files."""

    planning_root = REPO_ROOT / "docs" / "planning" / INITIATIVE_SLUG
    foundation_root = planning_root / "foundation"
    tracker_root = planning_root / "trackers"
    execution_root = planning_root / "execution"
    return [
        (planning_root / "README.md", render_planning_root_readme()),
        (planning_root / "ARTIFACT_PATH_INDEX.md", render_artifact_index()),
        (
            foundation_root / "README.md",
            "# Foundation\n\nSource, package, and ownership decisions.\n",
        ),
        (
            foundation_root / "api-source-of-truth.md",
            render_api_source_of_truth(resource_groups, audit, model_surface),
        ),
        (
            foundation_root / "source-of-truth-matrix.md",
            render_source_matrix(audit, model_surface),
        ),
        (
            foundation_root / "package-and-versioning-adr.md",
            render_package_versioning_adr(),
        ),
        (foundation_root / "rules-and-ownership-adr.md", render_rules_ownership_adr()),
        (tracker_root / "README.md", "# Trackers\n\nFocused readiness trackers.\n"),
        (tracker_root / "readiness-overview.md", render_readiness_overview()),
        (
            tracker_root / "endpoint-inventory-readiness.md",
            render_endpoint_inventory(resource_groups),
        ),
        (
            tracker_root / "coverage-and-tests-readiness.md",
            render_coverage_readiness(resource_groups),
        ),
        (tracker_root / "docs-parity-readiness.md", render_docs_readiness()),
        (tracker_root / "workflow-release-readiness.md", render_workflow_readiness()),
        (execution_root / "README.md", "# Execution\n\nLive implementation ledger.\n"),
        (execution_root / "execution-plan.md", render_execution_plan(model_surface)),
        (execution_root / "roadmap.md", render_roadmap()),
        (execution_root / "api-client-bootstrap-plan.md", render_bootstrap_plan()),
        (
            execution_root / "api_client_PHASE_00_source_audit.md",
            render_phase_doc(
                "API Client Phase 00 Source Audit",
                [
                    "- Confirmed `docs/api/aryeo.json` as the canonical source.",
                    "- Preserved per-operation public/protected auth semantics.",
                    "- Rate limits and webhooks remain undocumented.",
                ],
            ),
        ),
        (
            execution_root / "api_client_PHASE_01_foundation.md",
            render_phase_doc(
                "API Client Phase 01 Foundation",
                [
                    "- Kept `httpx` transport in `aryeo/base_client.py`.",
                    "- Kept Python `>=3.11` as an intentional project decision.",
                    "- Kept version sources in `pyproject.toml` and `aryeo/__init__.py`.",
                ],
            ),
        ),
        (
            execution_root / "api_client_PHASE_02_endpoint_inventory.md",
            render_phase_doc(
                "API Client Phase 02 Endpoint Inventory",
                [
                    "- Generated flat resource modules for every documented tag.",
                    "- Generated model and enum modules from component schemas.",
                    "- Kept endpoint methods JSON-based until coercion is proven.",
                ],
            ),
        ),
        (
            execution_root / "api_client_PHASE_03_tests_and_coverage.md",
            render_phase_doc(
                "API Client Phase 03 Tests And Coverage",
                [
                    "- Added one request-construction test module per resource.",
                    "- Kept core transport, exception, client, and model/export tests.",
                    "- Kept live integration checks opt-in.",
                ],
            ),
        ),
        (
            execution_root / "api_client_PHASE_04_docs_and_examples.md",
            render_phase_doc(
                "API Client Phase 04 Docs And Examples",
                [
                    "- Reworked MkDocs into client-library navigation.",
                    "- Added API reference pages for every public module.",
                    "- Added safe workflow examples.",
                ],
            ),
        ),
        (
            execution_root / "api_client_PHASE_05_workflows_and_release.md",
            render_phase_doc(
                "API Client Phase 05 Workflows And Release",
                [
                    "- Aligned release and unified deployment gates with CI.",
                    "- Kept strict docs build, package build, and twine check.",
                    "- Kept dependency/security audit automation.",
                ],
            ),
        ),
        (
            execution_root / "api_client_PHASE_06_parity_audit.md",
            render_phase_doc(
                "API Client Phase 06 Parity Audit",
                [
                    "- Full parity still requires endpoint-level model coercion proof.",
                    "- Do not claim complete model coverage until docs, tests, and examples prove it.",
                ],
            ),
        ),
    ]


def build_root_files(
    resource_groups: list[ResourceGroup],
    audit: AuditSummary,
) -> list[tuple[Path, str]]:
    """Build root files."""

    return [
        (REPO_ROOT / "pyproject.toml", render_pyproject()),
        (REPO_ROOT / "MANIFEST.in", render_manifest()),
        (REPO_ROOT / "README.md", render_readme(resource_groups, audit)),
        (REPO_ROOT / "STYLE_GUIDE.md", render_style_guide()),
        (REPO_ROOT / "mkdocs.yml", render_mkdocs(resource_groups)),
    ]


def build_package_files(
    resource_groups: list[ResourceGroup],
    enum_content: str,
    model_content: str,
    model_surface: ModelSurface,
) -> list[tuple[Path, str]]:
    """Build runtime package files."""

    files = [
        (
            REPO_ROOT / PACKAGE_NAME / "__init__.py",
            render_package_init(resource_groups, model_surface),
        ),
        (REPO_ROOT / PACKAGE_NAME / "client.py", render_client_module(resource_groups)),
        (REPO_ROOT / PACKAGE_NAME / "types.py", render_types_module()),
        (REPO_ROOT / PACKAGE_NAME / "exceptions.py", render_exceptions_module()),
        (REPO_ROOT / PACKAGE_NAME / "base_client.py", render_base_client_module()),
        (REPO_ROOT / PACKAGE_NAME / "_resource.py", render_resource_base_module()),
        (REPO_ROOT / PACKAGE_NAME / "enums.py", enum_content),
        (REPO_ROOT / PACKAGE_NAME / "models.py", model_content),
        (REPO_ROOT / PACKAGE_NAME / "py.typed", ""),
        (
            REPO_ROOT / PACKAGE_NAME / "resources" / "_base.py",
            render_resource_base_shim(),
        ),
        (
            REPO_ROOT / PACKAGE_NAME / "resources" / "__init__.py",
            render_resources_init(resource_groups),
        ),
    ]
    for group in resource_groups:
        files.append(
            (
                REPO_ROOT / PACKAGE_NAME / f"{group.module_name}.py",
                render_resource_module(group),
            )
        )
        files.append(
            (
                REPO_ROOT / PACKAGE_NAME / "resources" / f"{group.module_name}.py",
                render_resource_shim(group),
            )
        )
    return files


def build_example_files() -> list[tuple[Path, str]]:
    """Build example files."""

    return [
        (REPO_ROOT / "examples" / "quickstart.py", render_example_quickstart()),
        (REPO_ROOT / "examples" / "list_orders.py", render_example_orders()),
        (REPO_ROOT / "examples" / "list_listings.py", render_example_listings()),
        (
            REPO_ROOT / "examples" / "appointments_workflow.py",
            render_example_appointments(),
        ),
        (
            REPO_ROOT / "examples" / "customer_users_lookup.py",
            render_example_customer_users(),
        ),
    ]


def build_test_files(
    resource_groups: list[ResourceGroup],
    model_surface: ModelSurface,
) -> list[tuple[Path, str]]:
    """Build test files."""

    files = [
        (REPO_ROOT / "tests" / "__init__.py", '"""Test suite for Aryeo."""\n'),
        (REPO_ROOT / "tests" / "conftest.py", render_tests_conftest()),
        (REPO_ROOT / "tests" / "helpers.py", render_tests_helpers()),
        (REPO_ROOT / "tests" / "test_base_client.py", render_tests_base_client()),
        (REPO_ROOT / "tests" / "test_client.py", render_tests_client(resource_groups)),
        (REPO_ROOT / "tests" / "test_exceptions.py", render_tests_exceptions()),
        (REPO_ROOT / "tests" / "test_models.py", render_tests_models(model_surface)),
    ]
    for group in resource_groups:
        files.append(
            (
                REPO_ROOT / "tests" / f"test_{group.module_name}.py",
                render_resource_test(group),
            )
        )
    return files


def build_workflow_files() -> list[tuple[Path, str]]:
    """Build workflow files."""

    return [
        (REPO_ROOT / ".github" / "workflows" / "ci.yml", render_ci_workflow()),
        (REPO_ROOT / ".github" / "workflows" / "docs.yml", render_docs_workflow()),
        (
            REPO_ROOT / ".github" / "workflows" / "security-audit.yml",
            render_security_workflow(),
        ),
        (
            REPO_ROOT / ".github" / "workflows" / "release.yml",
            render_release_workflow(),
        ),
        (
            REPO_ROOT / ".github" / "workflows" / "unified-deployment.yml",
            render_unified_deployment_workflow(),
        ),
        (REPO_ROOT / ".github" / "dependabot.yml", render_dependabot()),
    ]


def build_rule_files() -> list[tuple[Path, str]]:
    """Build Cursor rule files."""

    return [
        (
            REPO_ROOT / ".cursor" / "rules" / "api-source-truth.mdc",
            render_rule_api_source_truth(),
        ),
        (
            REPO_ROOT / ".cursor" / "rules" / "api-client-implementation.mdc",
            render_rule_implementation(),
        ),
        (
            REPO_ROOT / ".cursor" / "rules" / "docs-tests-sync.mdc",
            render_rule_docs_tests_sync(),
        ),
        (
            REPO_ROOT / ".cursor" / "rules" / "release-quality-contract.mdc",
            render_rule_release_quality(),
        ),
    ]


def build_all_files(
    spec: dict[str, Any],
) -> tuple[list[tuple[Path, str]], list[tuple[Path, str]]]:
    """Build curated and generated file registries."""

    resource_groups, audit = build_resource_groups(spec)
    schemas = get_schemas(spec)
    enum_definitions, enum_path_map = collect_enum_definitions(schemas)
    enum_content = render_enum_module(enum_definitions)
    model_content, model_names, ambiguous_schemas = render_model_module(
        schemas,
        enum_path_map,
    )
    model_surface = ModelSurface(
        model_names=model_names,
        enum_names=tuple(sorted(enum_definitions)),
        ambiguous_schemas=ambiguous_schemas,
    )

    curated_files: list[tuple[Path, str]] = []
    curated_files.extend(build_root_files(resource_groups, audit))
    curated_files.extend(build_docs_files(resource_groups, audit))
    curated_files.extend(build_example_files())
    curated_files.extend(build_test_files(resource_groups, model_surface))
    curated_files.extend(build_workflow_files())
    curated_files.extend(build_rule_files())
    curated_files.extend(build_planning_files(resource_groups, audit, model_surface))

    generated_files = build_package_files(
        resource_groups,
        enum_content,
        model_content,
        model_surface,
    )
    return curated_files, generated_files


def run_from_cli() -> None:
    """Run the generator from command-line arguments."""

    args = parse_args()
    spec = read_spec()
    curated_files, generated_files = build_all_files(spec)
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
    run_from_cli()
