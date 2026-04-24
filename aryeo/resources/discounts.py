"""Generated resource client for the Discounts API tag."""

from __future__ import annotations

from aryeo.resources._base import ResourceClient
from aryeo.types import JSONMapping, JSONResponse, QueryParams, RequestTimeout


class DiscountsResource(ResourceClient):
    """Access discounts API operations."""

    def list_coupons(
        self, *, params: QueryParams | None = None, timeout: RequestTimeout = None
    ) -> JSONResponse:
        """List coupons.

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
            "GET", "/coupons", params=params, timeout=timeout, auth_required=True
        )

    def create(
        self, *, payload: JSONMapping | None = None, timeout: RequestTimeout = None
    ) -> JSONResponse:
        """Create discount.

        Args:
            payload: JSON payload matching DiscountPostPayload.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request(
            "POST", "/discounts", payload=payload, timeout=timeout, auth_required=True
        )

    def delete(
        self, discount_id: str, *, timeout: RequestTimeout = None
    ) -> JSONResponse:
        """Delete discount.

        Args:
            discount_id: The `discount_id` path value.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request(
            "DELETE", f"/discounts/{discount_id}", timeout=timeout, auth_required=True
        )

    def delete_order(
        self, order: str, discount: str, *, timeout: RequestTimeout = None
    ) -> JSONResponse:
        """Delete order discount.

        Args:
            order: The `order` path value.
            discount: The `discount` path value.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request(
            "DELETE",
            f"/orders/{order}/discounts/{discount}",
            timeout=timeout,
            auth_required=True,
        )

    def redeem_promotion_code(
        self,
        discounted_type: str,
        discounted: str,
        *,
        payload: JSONMapping | None = None,
        timeout: RequestTimeout = None,
    ) -> JSONResponse:
        """Redeem promotion code.

        Args:
            discounted_type: The `discounted_type` path value.
            discounted: The `discounted` path value.
            payload: JSON payload matching PromotionCodeRedeemPostPayload.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request(
            "POST",
            f"/promotion-codes/redeem/{discounted_type}/{discounted}",
            payload=payload,
            timeout=timeout,
            auth_required=False,
        )

    def refund_order_payment(
        self,
        order_payment: str,
        *,
        payload: JSONMapping | None = None,
        timeout: RequestTimeout = None,
    ) -> JSONResponse:
        """Refund order payment.

        Args:
            order_payment: The `order_payment` path value.
            payload: JSON payload matching OrderRefundPostPayload.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request(
            "POST",
            f"/refunds/{order_payment}",
            payload=payload,
            timeout=timeout,
            auth_required=True,
        )


__all__ = ["DiscountsResource"]
