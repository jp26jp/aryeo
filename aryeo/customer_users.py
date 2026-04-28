"""Generated resource client for the Customer Users API tag."""

from __future__ import annotations

from aryeo._resource import ResourceClient
from aryeo.types import JSONMapping, JSONResponse, QueryParams, RequestTimeout


class CustomerUsersResource(ResourceClient):
    """Access customer users API operations."""

    def get_team_member(
        self,
        customer_team_member_id: str,
        *,
        params: QueryParams | None = None,
        timeout: RequestTimeout = None,
    ) -> JSONResponse:
        """Get customer team member.

        Args:
            customer_team_member_id: The `customer_team_member_id` path value.
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
            f"/customer-team-members/{customer_team_member_id}",
            params=params,
            timeout=timeout,
            auth_required=True,
        )

    def create_team_affiliate_membership(
        self, *, payload: JSONMapping | None = None, timeout: RequestTimeout = None
    ) -> JSONResponse:
        """Create customer team affiliate membership.

        Args:
            payload: JSON payload matching CustomerTeamAffiliateMembershipPostPayload.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request(
            "POST",
            "/customer-teams/affiliate-memberships",
            payload=payload,
            timeout=timeout,
            auth_required=True,
        )

    def list_team_memberships(
        self,
        customer_team_id: str,
        *,
        params: QueryParams | None = None,
        timeout: RequestTimeout = None,
    ) -> JSONResponse:
        """List customer team memberships.

        Args:
            customer_team_id: The `customer_team_id` path value.
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
            f"/customer-teams/{customer_team_id}/memberships",
            params=params,
            timeout=timeout,
            auth_required=True,
        )

    def list(
        self, *, params: QueryParams | None = None, timeout: RequestTimeout = None
    ) -> JSONResponse:
        """List customer users.

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
            "GET", "/customer-users", params=params, timeout=timeout, auth_required=True
        )

    def create(
        self, *, payload: JSONMapping | None = None, timeout: RequestTimeout = None
    ) -> JSONResponse:
        """Create customer user.

        Args:
            payload: JSON payload matching CustomerUserPostPayload.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request(
            "POST",
            "/customer-users",
            payload=payload,
            timeout=timeout,
            auth_required=True,
        )

    def store_credit_transaction(
        self, user: str, *, payload: JSONMapping, timeout: RequestTimeout = None
    ) -> JSONResponse:
        """Store customer user credit transaction.

        Args:
            user: The `user` path value.
            payload: JSON payload matching the documented inline object payload.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request(
            "POST",
            f"/customer-users/{user}/credit-transactions",
            payload=payload,
            timeout=timeout,
            auth_required=True,
        )

    def list_customers(
        self, *, params: QueryParams | None = None, timeout: RequestTimeout = None
    ) -> JSONResponse:
        """List customers.

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
            "GET", "/customers", params=params, timeout=timeout, auth_required=True
        )

    def create_customers(
        self, *, payload: JSONMapping | None = None, timeout: RequestTimeout = None
    ) -> JSONResponse:
        """Create a customer.

        Args:
            payload: JSON payload matching CustomerPostPayload.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request(
            "POST", "/customers", payload=payload, timeout=timeout, auth_required=True
        )


__all__ = ["CustomerUsersResource"]
