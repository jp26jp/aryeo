"""Generated resource client for the Order Items API tag."""

from __future__ import annotations

from aryeo.resources._base import ResourceClient
from aryeo.types import JSONMapping, JSONResponse, QueryParams, RequestTimeout


class OrderItemsResource(ResourceClient):
    """Access order items API operations."""

    def create(
        self, *, payload: JSONMapping | None = None, timeout: RequestTimeout = None
    ) -> JSONResponse:
        """Create order item.

        Args:
            payload: JSON payload matching OrderItemPostPayload.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request(
            "POST", "/order-items", payload=payload, timeout=timeout, auth_required=True
        )

    def get(
        self,
        order_item_id: str,
        *,
        params: QueryParams | None = None,
        timeout: RequestTimeout = None,
    ) -> JSONResponse:
        """Get order item.

        Args:
            order_item_id: The `order_item_id` path value.
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
            f"/order-items/{order_item_id}",
            params=params,
            timeout=timeout,
            auth_required=True,
        )

    def update(
        self, order_item_id: str, *, timeout: RequestTimeout = None
    ) -> JSONResponse:
        """Update order item.

        Args:
            order_item_id: The `order_item_id` path value.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request(
            "PUT", f"/order-items/{order_item_id}", timeout=timeout, auth_required=True
        )

    def delete(
        self, order_item_id: str, *, timeout: RequestTimeout = None
    ) -> JSONResponse:
        """Delete order item.

        Args:
            order_item_id: The `order_item_id` path value.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request(
            "DELETE",
            f"/order-items/{order_item_id}",
            timeout=timeout,
            auth_required=True,
        )


__all__ = ["OrderItemsResource"]
