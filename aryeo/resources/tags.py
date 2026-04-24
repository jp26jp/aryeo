"""Generated resource client for the Tags API tag."""

from __future__ import annotations

from aryeo.resources._base import ResourceClient
from aryeo.types import JSONMapping, JSONResponse, RequestTimeout


class TagsResource(ResourceClient):
    """Access tags API operations."""

    def create_customer_team(
        self,
        customer_team_id: str,
        *,
        payload: JSONMapping | None = None,
        timeout: RequestTimeout = None,
    ) -> JSONResponse:
        """Create customer team tag.

        Args:
            customer_team_id: The `customer_team_id` path value.
            payload: JSON payload matching TagsPostPayload.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request(
            "POST",
            f"/customer-teams/{customer_team_id}/tags",
            payload=payload,
            timeout=timeout,
            auth_required=True,
        )

    def update_customer_team(
        self,
        customer_team_id: str,
        *,
        payload: JSONMapping | None = None,
        timeout: RequestTimeout = None,
    ) -> JSONResponse:
        """Update customer team tag.

        Args:
            customer_team_id: The `customer_team_id` path value.
            payload: JSON payload matching TagsPutPayload.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request(
            "PUT",
            f"/customer-teams/{customer_team_id}/tags",
            payload=payload,
            timeout=timeout,
            auth_required=True,
        )

    def delete_customer_team(
        self, customer_team_id: str, tag_id: str, *, timeout: RequestTimeout = None
    ) -> JSONResponse:
        """Delete customer team tag.

        Args:
            customer_team_id: The `customer_team_id` path value.
            tag_id: The `tag_id` path value.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request(
            "DELETE",
            f"/customer-teams/{customer_team_id}/tags/{tag_id}",
            timeout=timeout,
            auth_required=True,
        )

    def create_for_order(
        self,
        order_id: str,
        *,
        payload: JSONMapping | None = None,
        timeout: RequestTimeout = None,
    ) -> JSONResponse:
        """Create tag for order.

        Args:
            order_id: The `order_id` path value.
            payload: JSON payload matching OrderTagsPostPayload.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request(
            "POST",
            f"/orders/{order_id}/tags",
            payload=payload,
            timeout=timeout,
            auth_required=True,
        )

    def update_for_order(
        self,
        order_id: str,
        *,
        payload: JSONMapping | None = None,
        timeout: RequestTimeout = None,
    ) -> JSONResponse:
        """Update tag for order.

        Args:
            order_id: The `order_id` path value.
            payload: JSON payload matching TagsPutPayload.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request(
            "PUT",
            f"/orders/{order_id}/tags",
            payload=payload,
            timeout=timeout,
            auth_required=True,
        )

    def delete_for_order(
        self, order_id: str, tag_id: str, *, timeout: RequestTimeout = None
    ) -> JSONResponse:
        """Delete tag for order.

        Args:
            order_id: The `order_id` path value.
            tag_id: The `tag_id` path value.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request(
            "DELETE",
            f"/orders/{order_id}/tags/{tag_id}",
            timeout=timeout,
            auth_required=True,
        )

    def create(
        self,
        product_id: str,
        *,
        payload: JSONMapping | None = None,
        timeout: RequestTimeout = None,
    ) -> JSONResponse:
        """Create tag.

        Args:
            product_id: The `product_id` path value.
            payload: JSON payload matching TagsPostPayload.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request(
            "POST",
            f"/products/{product_id}/tags",
            payload=payload,
            timeout=timeout,
            auth_required=True,
        )

    def update_product(
        self,
        product_id: str,
        *,
        payload: JSONMapping | None = None,
        timeout: RequestTimeout = None,
    ) -> JSONResponse:
        """Update product tag.

        Args:
            product_id: The `product_id` path value.
            payload: JSON payload matching TagsPutPayload.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request(
            "PUT",
            f"/products/{product_id}/tags",
            payload=payload,
            timeout=timeout,
            auth_required=True,
        )

    def update(
        self,
        product_id: str,
        tag_id: str,
        *,
        payload: JSONMapping | None = None,
        timeout: RequestTimeout = None,
    ) -> JSONResponse:
        """Update tag.

        Args:
            product_id: The `product_id` path value.
            tag_id: The `tag_id` path value.
            payload: JSON payload matching TagsPutPayload.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request(
            "PUT",
            f"/products/{product_id}/tags/{tag_id}",
            payload=payload,
            timeout=timeout,
            auth_required=True,
        )

    def delete_product(
        self, product_id: str, tag_id: str, *, timeout: RequestTimeout = None
    ) -> JSONResponse:
        """Delete product tag.

        Args:
            product_id: The `product_id` path value.
            tag_id: The `tag_id` path value.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request(
            "DELETE",
            f"/products/{product_id}/tags/{tag_id}",
            timeout=timeout,
            auth_required=True,
        )

    def create_tags(
        self, *, payload: JSONMapping | None = None, timeout: RequestTimeout = None
    ) -> JSONResponse:
        """Create tag.

        Args:
            payload: JSON payload matching TagOnlyPostPayload.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request(
            "POST", "/tags", payload=payload, timeout=timeout, auth_required=True
        )

    def update_tags(
        self,
        tag_id: str,
        *,
        payload: JSONMapping | None = None,
        timeout: RequestTimeout = None,
    ) -> JSONResponse:
        """Update tag.

        Args:
            tag_id: The `tag_id` path value.
            payload: JSON payload matching TagPutPayload.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request(
            "PUT",
            f"/tags/{tag_id}",
            payload=payload,
            timeout=timeout,
            auth_required=True,
        )


__all__ = ["TagsResource"]
