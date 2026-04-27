from __future__ import annotations

import argparse
import os
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Literal, Sequence

from aryeo import AryeoClient
from aryeo.base_client import DEFAULT_BASE_URL, DEFAULT_TIMEOUT
from aryeo.exceptions import AryeoAPIError, AryeoError
from aryeo.types import JSONResponse, QueryParams

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ENV_FILE = REPO_ROOT / ".env"
DEFAULT_TOKEN_ENV_VARS = ("ARYEO_API_TOKEN", "ARYEO_API_KEY")
DEFAULT_PAGE_PARAMS: QueryParams = {"page": 1, "per_page": 1}
DEFAULT_REGION_PARAMS: QueryParams = {
    "page": 1,
    "per_page": 1,
    "filter[type]": "COUNTRY",
}

ResultStatus = Literal["passed", "failed", "skipped"]


@dataclass(frozen=True)
class LiveCheck:
    """Describe one safe live integration check for an Aryeo resource."""

    resource_name: str
    operation_name: str
    endpoint: str
    params: QueryParams | None = None
    path_argument_name: str | None = None
    path_argument_env_var: str | None = None
    skip_reason: str | None = None


@dataclass(frozen=True)
class LiveResult:
    """Capture the outcome of one live integration check."""

    resource_name: str
    operation_name: str
    endpoint: str
    status: ResultStatus
    detail: str
    response_keys: tuple[str, ...] = ()


LIVE_CHECKS: tuple[LiveCheck, ...] = (
    LiveCheck(
        "addresses",
        "get",
        "GET /addresses/{address}",
        path_argument_name="address",
        path_argument_env_var="ARYEO_LIVE_ADDRESS_ID",
    ),
    LiveCheck("appointments", "list", "GET /appointments", DEFAULT_PAGE_PARAMS),
    LiveCheck(
        "company_users",
        "list_team_members",
        "GET /company-team-members",
        DEFAULT_PAGE_PARAMS,
    ),
    LiveCheck("customer_users", "list", "GET /customer-users", DEFAULT_PAGE_PARAMS),
    LiveCheck("discounts", "list_coupons", "GET /coupons", DEFAULT_PAGE_PARAMS),
    LiveCheck("listings", "list", "GET /listings", DEFAULT_PAGE_PARAMS),
    LiveCheck(
        "notes",
        "update_order",
        "PUT /orders/{order_id}/notes",
        skip_reason="No read-only notes endpoint is exposed by the current client.",
    ),
    LiveCheck("order_forms", "list", "GET /order-forms"),
    LiveCheck(
        "order_items",
        "get",
        "GET /order-items/{order_item_id}",
        path_argument_name="order_item_id",
        path_argument_env_var="ARYEO_LIVE_ORDER_ITEM_ID",
    ),
    LiveCheck("orders", "list", "GET /orders", DEFAULT_PAGE_PARAMS),
    LiveCheck(
        "payroll",
        "list_order_item_pay_run_item_defaults",
        "GET /order-items/{order_item_id}/pay-run-item-defaults",
        path_argument_name="order_item_id",
        path_argument_env_var="ARYEO_LIVE_ORDER_ITEM_ID",
    ),
    LiveCheck("products", "list", "GET /products", DEFAULT_PAGE_PARAMS),
    LiveCheck("scheduling", "list_regions", "GET /regions", DEFAULT_REGION_PARAMS),
    LiveCheck(
        "tags",
        "create_tags",
        "POST /tags",
        skip_reason="No read-only tags endpoint is exposed by the current client.",
    ),
    LiveCheck("tasks", "list", "GET /tasks"),
    LiveCheck(
        "videos",
        "get",
        "GET /videos/{video_id}",
        path_argument_name="video_id",
        path_argument_env_var="ARYEO_LIVE_VIDEO_ID",
    ),
)


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    """Parse command-line arguments for live Aryeo verification.

    Args:
        argv: Optional argument sequence. Defaults to `sys.argv` when omitted.

    Returns:
        Parsed CLI arguments.
    """

    parser = argparse.ArgumentParser(
        description="Run opt-in, read-only live smoke checks against the Aryeo API."
    )
    parser.add_argument(
        "--env-file",
        type=Path,
        default=DEFAULT_ENV_FILE,
        help="Optional .env file to load before resolving Aryeo configuration.",
    )
    parser.add_argument(
        "--token-env-var",
        action="append",
        default=[],
        help=(
            "Environment variable to check for the bearer token. May be provided "
            "multiple times. Defaults to ARYEO_API_TOKEN then ARYEO_API_KEY."
        ),
    )
    parser.add_argument(
        "--base-url",
        default=None,
        help="Override the Aryeo base URL. Defaults to ARYEO_BASE_URL or production.",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=None,
        help="Request timeout in seconds. Defaults to ARYEO_TIMEOUT or client default.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit non-zero when any integration is skipped.",
    )
    return parser.parse_args(argv)


def load_env_file(path: Path) -> dict[str, str]:
    """Load simple key-value pairs from a dotenv-style file.

    Existing process environment variables are preserved. The parsed values are
    returned so callers can test parsing behavior without reading `os.environ`.

    Args:
        path: Path to the dotenv file.

    Returns:
        Mapping of parsed environment names to values.
    """

    values: dict[str, str] = {}
    if not path.exists():
        return values

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line.removeprefix("export ").strip()
        if "=" not in line:
            continue

        name, raw_value = line.split("=", 1)
        value = raw_value.strip().strip('"').strip("'")
        env_name = name.strip()
        values[env_name] = value
        os.environ.setdefault(env_name, value)

    return values


def resolve_token(env_var_names: Sequence[str]) -> str:
    """Resolve the first non-empty token from the configured environment names.

    Args:
        env_var_names: Environment variable names to inspect in order.

    Returns:
        The resolved bearer token.

    Raises:
        SystemExit: If none of the configured environment variables has a value.
    """

    for env_var_name in env_var_names:
        token = os.getenv(env_var_name)
        if token:
            return token

    joined_names = ", ".join(env_var_names)
    raise SystemExit(f"Missing Aryeo token. Set one of: {joined_names}.")


def resolve_timeout(cli_timeout: float | None) -> float:
    """Resolve the request timeout from CLI, environment, or client default.

    Args:
        cli_timeout: Optional timeout supplied on the command line.

    Returns:
        Timeout in seconds.

    Raises:
        SystemExit: If `ARYEO_TIMEOUT` is present but is not a float.
    """

    if cli_timeout is not None:
        return cli_timeout

    env_timeout = os.getenv("ARYEO_TIMEOUT")
    if not env_timeout:
        return DEFAULT_TIMEOUT

    try:
        return float(env_timeout)
    except ValueError as exc:
        raise SystemExit("ARYEO_TIMEOUT must be a float if provided.") from exc


def build_client(args: argparse.Namespace) -> AryeoClient:
    """Build an Aryeo client for live verification.

    Args:
        args: Parsed CLI arguments.

    Returns:
        Configured Aryeo client.
    """

    token_env_vars = tuple(args.token_env_var) or DEFAULT_TOKEN_ENV_VARS
    token = resolve_token(token_env_vars)
    base_url = args.base_url or os.getenv("ARYEO_BASE_URL", DEFAULT_BASE_URL)
    timeout = resolve_timeout(args.timeout)
    return AryeoClient(token=token, base_url=base_url, timeout=timeout)


def summarize_response(response: JSONResponse) -> tuple[str, tuple[str, ...]]:
    """Return a short, non-sensitive summary of a JSON response.

    Args:
        response: Decoded JSON response from the Aryeo client.

    Returns:
        Pair containing a human-readable detail and sorted top-level keys.
    """

    if isinstance(response, dict):
        keys = tuple(sorted(str(key) for key in response))
        return "JSON object decoded successfully.", keys
    if isinstance(response, list):
        return f"JSON list decoded successfully with {len(response)} items.", ()
    if response is None:
        return "Empty response decoded successfully.", ()
    return f"{type(response).__name__} response decoded successfully.", ()


def run_check(client: AryeoClient, check: LiveCheck) -> LiveResult:
    """Execute one live integration check if it is safe and configured.

    Args:
        client: Aryeo client configured with live API credentials.
        check: Check definition to execute.

    Returns:
        Structured check result.
    """

    if check.skip_reason:
        return LiveResult(
            check.resource_name,
            check.operation_name,
            check.endpoint,
            "skipped",
            check.skip_reason,
        )

    path_arguments: dict[str, str] = {}
    if check.path_argument_env_var:
        fixture_value = os.getenv(check.path_argument_env_var)
        if not fixture_value:
            return LiveResult(
                check.resource_name,
                check.operation_name,
                check.endpoint,
                "skipped",
                f"Set {check.path_argument_env_var} to run this fixture-based read.",
            )
        if check.path_argument_name is None:
            return LiveResult(
                check.resource_name,
                check.operation_name,
                check.endpoint,
                "failed",
                "Check is missing a path argument name.",
            )
        path_arguments[check.path_argument_name] = fixture_value

    try:
        resource = getattr(client, check.resource_name)
        method = getattr(resource, check.operation_name)
        kwargs: dict[str, Any] = dict(path_arguments)
        if check.params is not None:
            kwargs["params"] = check.params
        response = method(**kwargs)
    except AryeoAPIError as exc:
        return LiveResult(
            check.resource_name,
            check.operation_name,
            check.endpoint,
            "failed",
            f"HTTP {exc.status_code}: {exc.message}",
        )
    except AryeoError as exc:
        return LiveResult(
            check.resource_name,
            check.operation_name,
            check.endpoint,
            "failed",
            f"{type(exc).__name__}: {exc}",
        )

    detail, response_keys = summarize_response(response)
    return LiveResult(
        check.resource_name,
        check.operation_name,
        check.endpoint,
        "passed",
        detail,
        response_keys,
    )


def run_checks(client: AryeoClient, checks: Sequence[LiveCheck]) -> list[LiveResult]:
    """Run live checks in definition order.

    Args:
        client: Aryeo client configured with live API credentials.
        checks: Check definitions to execute.

    Returns:
        Ordered result list.
    """

    return [run_check(client, check) for check in checks]


def format_results(results: Sequence[LiveResult]) -> str:
    """Format live verification results for terminal output.

    Args:
        results: Results to display.

    Returns:
        Human-readable result summary.
    """

    lines = ["Aryeo live integration results:"]
    for result in results:
        keys = ""
        if result.response_keys:
            keys = f" keys={','.join(result.response_keys)}"
        lines.append(
            f"- {result.status.upper()}: {result.resource_name}."
            f"{result.operation_name} ({result.endpoint}) - {result.detail}{keys}"
        )

    passed = sum(result.status == "passed" for result in results)
    failed = sum(result.status == "failed" for result in results)
    skipped = sum(result.status == "skipped" for result in results)
    lines.append("")
    lines.append(f"Summary: {passed} passed, {failed} failed, {skipped} skipped.")
    return "\n".join(lines)


def exit_code(results: Sequence[LiveResult], *, strict: bool) -> int:
    """Choose the process exit code for a set of results.

    Args:
        results: Live verification results.
        strict: Whether skipped checks should fail the run.

    Returns:
        POSIX process exit code.
    """

    if any(result.status == "failed" for result in results):
        return 1
    if strict and any(result.status == "skipped" for result in results):
        return 1
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    """Run the live integration verification command.

    Args:
        argv: Optional CLI argument sequence.

    Returns:
        POSIX process exit code.
    """

    args = parse_args(argv)
    load_env_file(args.env_file)

    client = build_client(args)
    try:
        results = run_checks(client, LIVE_CHECKS)
    finally:
        client.close()

    print(format_results(results))
    return exit_code(results, strict=args.strict)


if __name__ == "__main__":
    sys.exit(main())
