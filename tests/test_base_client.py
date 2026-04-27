
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
