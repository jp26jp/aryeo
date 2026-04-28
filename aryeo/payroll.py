"""Generated resource client for the Payroll API tag."""

from __future__ import annotations

from aryeo._resource import ResourceClient
from aryeo.types import JSONResponse, RequestTimeout


class PayrollResource(ResourceClient):
    """Access payroll API operations."""

    def create_billing_setup_intent(
        self, *, timeout: RequestTimeout = None
    ) -> JSONResponse:
        """Create billing setup intent.

        Args:
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request(
            "POST", "/billing/setup-intents", timeout=timeout, auth_required=True
        )

    def list_order_item_pay_run_item_defaults(
        self, order_item_id: str, *, timeout: RequestTimeout = None
    ) -> JSONResponse:
        """List order item pay run item defaults.

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
            "GET",
            f"/order-items/{order_item_id}/pay-run-item-defaults",
            timeout=timeout,
            auth_required=True,
        )


__all__ = ["PayrollResource"]
