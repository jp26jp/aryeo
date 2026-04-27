"""Generated resource client for the Notes API tag."""

from __future__ import annotations

from aryeo.resources._base import ResourceClient
from aryeo.types import JSONMapping, JSONResponse, RequestTimeout


class NotesResource(ResourceClient):
    """Access notes API operations."""

    def update_order(
        self,
        order_id: str,
        *,
        payload: JSONMapping | None = None,
        timeout: RequestTimeout = None,
    ) -> JSONResponse:
        """Update order notes.

        Args:
            order_id: The `order_id` path value.
            payload: JSON payload matching OrderNotesPutPayload.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request(
            "PUT",
            f"/orders/{order_id}/notes",
            payload=payload,
            timeout=timeout,
            auth_required=True,
        )


__all__ = ["NotesResource"]
