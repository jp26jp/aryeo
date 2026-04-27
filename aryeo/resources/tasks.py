
"""Generated resource client for the Tasks API tag."""

from __future__ import annotations

from aryeo.resources._base import ResourceClient
from aryeo.types import JSONMapping, JSONResponse, RequestTimeout


class TasksResource(ResourceClient):
    """Access tasks API operations."""

    def list(self, *, timeout: RequestTimeout = None) -> JSONResponse:
        """List tasks.

        Args:
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request("GET", "/tasks", timeout=timeout, auth_required=True)

    def create(self, *, payload: JSONMapping | None = None, timeout: RequestTimeout = None) -> JSONResponse:
        """Create task.

        Args:
            payload: JSON payload matching TaskPostPayload.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request("POST", "/tasks", payload=payload, timeout=timeout, auth_required=True)

    def delete(self, task_id: str, *, timeout: RequestTimeout = None) -> JSONResponse:
        """Delete task.

        Args:
            task_id: The `task_id` path value.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request("DELETE", f"/tasks/{task_id}", timeout=timeout, auth_required=True)

    def get(self, task_id: str, *, timeout: RequestTimeout = None) -> JSONResponse:
        """Get task.

        Args:
            task_id: The `task_id` path value.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request("GET", f"/tasks/{task_id}", timeout=timeout, auth_required=True)

    def update(self, task_id: str, *, payload: JSONMapping | None = None, timeout: RequestTimeout = None) -> JSONResponse:
        """Update task.

        Args:
            task_id: The `task_id` path value.
            payload: JSON payload matching TaskPutPayload.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request("PUT", f"/tasks/{task_id}", payload=payload, timeout=timeout, auth_required=True)

    def complete(self, task_id: str, *, payload: JSONMapping | None = None, timeout: RequestTimeout = None) -> JSONResponse:
        """Complete task.

        Args:
            task_id: The `task_id` path value.
            payload: JSON payload matching TaskCompletePutPayload.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request("PUT", f"/tasks/{task_id}/complete", payload=payload, timeout=timeout, auth_required=True)

    def reinstate(self, task_id: str, *, payload: JSONMapping | None = None, timeout: RequestTimeout = None) -> JSONResponse:
        """Reinstate task.

        Args:
            task_id: The `task_id` path value.
            payload: JSON payload matching TaskReinstatePutPayload.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request("PUT", f"/tasks/{task_id}/reinstate", payload=payload, timeout=timeout, auth_required=True)


__all__ = ["TasksResource"]
