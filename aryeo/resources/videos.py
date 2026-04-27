
"""Generated resource client for the Videos API tag."""

from __future__ import annotations

from aryeo.resources._base import ResourceClient
from aryeo.types import JSONMapping, JSONResponse, RequestTimeout


class VideosResource(ResourceClient):
    """Access videos API operations."""

    def get(self, video_id: str, *, timeout: RequestTimeout = None) -> JSONResponse:
        """Get video.

        Args:
            video_id: The `video_id` path value.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request("GET", f"/videos/{video_id}", timeout=timeout, auth_required=True)

    def update(self, video_id: str, *, payload: JSONMapping | None = None, timeout: RequestTimeout = None) -> JSONResponse:
        """Update video.

        Args:
            video_id: The `video_id` path value.
            payload: JSON payload matching VideoPutPayload.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request("PUT", f"/videos/{video_id}", payload=payload, timeout=timeout, auth_required=True)

    def delete(self, video_id: str, *, timeout: RequestTimeout = None) -> JSONResponse:
        """Delete video.

        Args:
            video_id: The `video_id` path value.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request("DELETE", f"/videos/{video_id}", timeout=timeout, auth_required=True)


__all__ = ["VideosResource"]
