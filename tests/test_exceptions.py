
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
