"""Generated resource client for the Order Forms API tag."""

from __future__ import annotations

from aryeo.resources._base import ResourceClient
from aryeo.types import JSONMapping, JSONResponse, RequestTimeout


class OrderFormsResource(ResourceClient):
    """Access order forms API operations."""

    def create_session(
        self, *, payload: JSONMapping | None = None, timeout: RequestTimeout = None
    ) -> JSONResponse:
        """Create order form session.

        Args:
            payload: JSON payload matching OrderFormSessionPostPayload.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request(
            "POST",
            "/order-form-sessions",
            payload=payload,
            timeout=timeout,
            auth_required=True,
        )

    def list(self, *, timeout: RequestTimeout = None) -> JSONResponse:
        """List order forms.

        Args:
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request("GET", "/order-forms", timeout=timeout, auth_required=True)


__all__ = ["OrderFormsResource"]
