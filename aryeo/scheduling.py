"""Generated resource client for the Scheduling API tag."""

from __future__ import annotations

from aryeo._resource import ResourceClient
from aryeo.types import JSONMapping, JSONResponse, QueryParams, RequestTimeout


class SchedulingResource(ResourceClient):
    """Access scheduling API operations."""

    def create_block(
        self, *, payload: JSONMapping | None = None, timeout: RequestTimeout = None
    ) -> JSONResponse:
        """Create block.

        Args:
            payload: JSON payload matching BlockPostPayload.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request(
            "POST", "/blocks", payload=payload, timeout=timeout, auth_required=True
        )

    def get_block(
        self, block_id: str, *, timeout: RequestTimeout = None
    ) -> JSONResponse:
        """Get block.

        Args:
            block_id: The `block_id` path value.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request(
            "GET", f"/blocks/{block_id}", timeout=timeout, auth_required=True
        )

    def update_block(
        self, block_id: str, *, timeout: RequestTimeout = None
    ) -> JSONResponse:
        """Update block.

        Args:
            block_id: The `block_id` path value.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request(
            "PUT", f"/blocks/{block_id}", timeout=timeout, auth_required=True
        )

    def delete_block(
        self, block_id: str, *, timeout: RequestTimeout = None
    ) -> JSONResponse:
        """Delete block.

        Args:
            block_id: The `block_id` path value.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request(
            "DELETE", f"/blocks/{block_id}", timeout=timeout, auth_required=True
        )

    def list_regions(
        self, *, params: QueryParams | None = None, timeout: RequestTimeout = None
    ) -> JSONResponse:
        """List regions.

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
            "GET", "/regions", params=params, timeout=timeout, auth_required=True
        )

    def get_assignment(
        self, *, params: QueryParams | None = None, timeout: RequestTimeout = None
    ) -> JSONResponse:
        """Get scheduling assignment.

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
            "/scheduling/assignment",
            params=params,
            timeout=timeout,
            auth_required=True,
        )

    def list_available_dates(
        self, *, params: QueryParams | None = None, timeout: RequestTimeout = None
    ) -> JSONResponse:
        """List available dates.

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
            "/scheduling/available-dates",
            params=params,
            timeout=timeout,
            auth_required=True,
        )

    def list_available_timeslots(
        self, *, params: QueryParams | None = None, timeout: RequestTimeout = None
    ) -> JSONResponse:
        """List available timeslots.

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
            "/scheduling/available-timeslots",
            params=params,
            timeout=timeout,
            auth_required=True,
        )

    def list_schedule_item_groupings(
        self, *, params: QueryParams | None = None, timeout: RequestTimeout = None
    ) -> JSONResponse:
        """List schedule item groupings.

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
            "/scheduling/item-groupings",
            params=params,
            timeout=timeout,
            auth_required=True,
        )


__all__ = ["SchedulingResource"]
