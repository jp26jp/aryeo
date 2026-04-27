"""Generated resource client for the Company Users API tag."""

from __future__ import annotations

from aryeo.resources._base import ResourceClient
from aryeo.types import JSONResponse, QueryParams, RequestTimeout


class CompanyUsersResource(ResourceClient):
    """Access company users API operations."""

    def list_team_members(
        self, *, params: QueryParams | None = None, timeout: RequestTimeout = None
    ) -> JSONResponse:
        """List company team members.

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
            "/company-team-members",
            params=params,
            timeout=timeout,
            auth_required=True,
        )

    def get_team_member(
        self,
        company_team_member_id: str,
        *,
        params: QueryParams | None = None,
        timeout: RequestTimeout = None,
    ) -> JSONResponse:
        """Get company team member.

        Args:
            company_team_member_id: The `company_team_member_id` path value.
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
            f"/company-team-members/{company_team_member_id}",
            params=params,
            timeout=timeout,
            auth_required=True,
        )

    def list_team_member_events(
        self,
        company_team_member_id: str,
        *,
        params: QueryParams | None = None,
        timeout: RequestTimeout = None,
    ) -> JSONResponse:
        """List company team member events.

        Args:
            company_team_member_id: The `company_team_member_id` path value.
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
            f"/company-team-members/{company_team_member_id}/events",
            params=params,
            timeout=timeout,
            auth_required=True,
        )


__all__ = ["CompanyUsersResource"]
