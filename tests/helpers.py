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
