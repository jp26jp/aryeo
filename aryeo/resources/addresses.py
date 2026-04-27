"""Generated resource client for the Addresses API tag."""

from __future__ import annotations

from aryeo.resources._base import ResourceClient
from aryeo.types import JSONMapping, JSONResponse, RequestTimeout


class AddressesResource(ResourceClient):
    """Access addresses API operations."""

    def create(
        self, *, payload: JSONMapping | None = None, timeout: RequestTimeout = None
    ) -> JSONResponse:
        """Create address.

        Args:
            payload: JSON payload matching AddressPostPayload.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request(
            "POST", "/addresses", payload=payload, timeout=timeout, auth_required=False
        )

    def get(self, address: str, *, timeout: RequestTimeout = None) -> JSONResponse:
        """Get address.

        Args:
            address: The `address` path value.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request(
            "GET", f"/addresses/{address}", timeout=timeout, auth_required=False
        )

    def update(
        self,
        address: str,
        *,
        payload: JSONMapping | None = None,
        timeout: RequestTimeout = None,
    ) -> JSONResponse:
        """Update address.

        Args:
            address: The `address` path value.
            payload: JSON payload matching AddressPatchPayload.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request(
            "PATCH",
            f"/addresses/{address}",
            payload=payload,
            timeout=timeout,
            auth_required=False,
        )


__all__ = ["AddressesResource"]
