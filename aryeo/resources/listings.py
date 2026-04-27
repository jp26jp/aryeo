
"""Generated resource client for the Listings API tag."""

from __future__ import annotations

from aryeo.resources._base import ResourceClient
from aryeo.types import JSONMapping, JSONResponse, QueryParams, RequestTimeout


class ListingsResource(ResourceClient):
    """Access listings API operations."""

    def list(self, *, params: QueryParams | None = None, timeout: RequestTimeout = None) -> JSONResponse:
        """List listings.

        Args:
            params: Optional query parameters for the underlying API call.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request("GET", "/listings", params=params, timeout=timeout, auth_required=True)

    def create(self, *, payload: JSONMapping | None = None, timeout: RequestTimeout = None) -> JSONResponse:
        """Create listing.

        Args:
            payload: JSON payload matching ListingPostPayload.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request("POST", "/listings", payload=payload, timeout=timeout, auth_required=True)

    def get(self, listing_id: str, *, params: QueryParams | None = None, timeout: RequestTimeout = None) -> JSONResponse:
        """Get listing.

        Args:
            listing_id: The `listing_id` path value.
            params: Optional query parameters for the underlying API call.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request("GET", f"/listings/{listing_id}", params=params, timeout=timeout, auth_required=True)

    def update(self, listing_id: str, *, payload: JSONMapping | None = None, timeout: RequestTimeout = None) -> JSONResponse:
        """Update listing.

        Args:
            listing_id: The `listing_id` path value.
            payload: JSON payload matching ListingPutPayload.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request("PUT", f"/listings/{listing_id}", payload=payload, timeout=timeout, auth_required=True)

    def get_cubicasa_information(self, listing_id: str, *, timeout: RequestTimeout = None) -> JSONResponse:
        """Get listing Cubicasa information.

        Args:
            listing_id: The `listing_id` path value.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request("GET", f"/listings/{listing_id}/cubi-casa", timeout=timeout, auth_required=True)

    def search_details(self, listing_id: str, *, timeout: RequestTimeout = None) -> JSONResponse:
        """Search listing details.

        Args:
            listing_id: The `listing_id` path value.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request("GET", f"/listings/{listing_id}/details/search", timeout=timeout, auth_required=True)

    def get_statistics(self, listing_id: str, *, timeout: RequestTimeout = None) -> JSONResponse:
        """Get listing statistics.

        Args:
            listing_id: The `listing_id` path value.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request("GET", f"/listings/{listing_id}/stats", timeout=timeout, auth_required=True)


__all__ = ["ListingsResource"]
