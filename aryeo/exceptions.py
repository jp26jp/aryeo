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
