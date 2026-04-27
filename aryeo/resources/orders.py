
"""Generated resource client for the Orders API tag."""

from __future__ import annotations

from aryeo.resources._base import ResourceClient
from aryeo.types import JSONMapping, JSONResponse, QueryParams, RequestTimeout


class OrdersResource(ResourceClient):
    """Access orders API operations."""

    def list(self, *, params: QueryParams | None = None, timeout: RequestTimeout = None) -> JSONResponse:
        """List orders.

        Args:
            params: Optional query parameters for the underlying API call.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request("GET", "/orders", params=params, timeout=timeout, auth_required=True)

    def create(self, *, payload: JSONMapping | None = None, timeout: RequestTimeout = None) -> JSONResponse:
        """Create order.

        Args:
            payload: JSON payload matching OrderPostPayload.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request("POST", "/orders", payload=payload, timeout=timeout, auth_required=True)

    def get(self, order_id: str, *, params: QueryParams | None = None, timeout: RequestTimeout = None) -> JSONResponse:
        """Get order.

        Args:
            order_id: The `order_id` path value.
            params: Optional query parameters for the underlying API call.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request("GET", f"/orders/{order_id}", params=params, timeout=timeout, auth_required=True)

    def create_manual_payment(self, order: str, *, payload: JSONMapping, timeout: RequestTimeout = None) -> JSONResponse:
        """Create a manual order payment.

        Args:
            order: The `order` path value.
            payload: JSON payload matching the documented inline object payload.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request("POST", f"/orders/{order}/payments", payload=payload, timeout=timeout, auth_required=True)

    def update_billing_address(self, order: str, *, payload: JSONMapping | None = None, timeout: RequestTimeout = None) -> JSONResponse:
        """Update order billing address.

        Args:
            order: The `order` path value.
            payload: JSON payload matching OrderBillingAddressPutPayload.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request("PUT", f"/orders/{order}/billing-address", payload=payload, timeout=timeout, auth_required=True)

    def get_payment_information(self, order: str, *, timeout: RequestTimeout = None) -> JSONResponse:
        """Get payment information an order.

        Args:
            order: The `order` path value.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request("GET", f"/orders/{order}/payment-info", timeout=timeout, auth_required=False)


__all__ = ["OrdersResource"]
