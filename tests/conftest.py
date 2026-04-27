
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
