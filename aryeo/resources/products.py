"""Generated resource client for the Products API tag."""

from __future__ import annotations

from aryeo.resources._base import ResourceClient
from aryeo.types import JSONMapping, JSONResponse, QueryParams, RequestTimeout


class ProductsResource(ResourceClient):
    """Access products API operations."""

    def list(
        self, *, params: QueryParams | None = None, timeout: RequestTimeout = None
    ) -> JSONResponse:
        """List products.

        Args:
            params: Optional query parameters for the underlying API call.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request(
            "GET", "/products", params=params, timeout=timeout, auth_required=True
        )

    def list_categories(
        self, *, params: QueryParams | None = None, timeout: RequestTimeout = None
    ) -> JSONResponse:
        """List product categories.

        Args:
            params: Optional query parameters for the underlying API call.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request(
            "GET",
            "/product-categories",
            params=params,
            timeout=timeout,
            auth_required=True,
        )

    def create_tax(
        self, *, payload: JSONMapping | None = None, timeout: RequestTimeout = None
    ) -> JSONResponse:
        """Create tax.

        Args:
            payload: JSON payload matching TaxPostPayload.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request(
            "POST", "/taxes", payload=payload, timeout=timeout, auth_required=True
        )

    def delete_tax(
        self, tax_id: str, *, timeout: RequestTimeout = None
    ) -> JSONResponse:
        """Delete tax.

        Args:
            tax_id: The `tax_id` path value.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request(
            "DELETE", f"/taxes/{tax_id}", timeout=timeout, auth_required=True
        )

    def list_territories(
        self, *, params: QueryParams | None = None, timeout: RequestTimeout = None
    ) -> JSONResponse:
        """List territories.

        Args:
            params: Optional query parameters for the underlying API call.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request(
            "GET", "/territories", params=params, timeout=timeout, auth_required=True
        )


__all__ = ["ProductsResource"]
