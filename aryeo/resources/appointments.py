
"""Generated resource client for the Appointments API tag."""

from __future__ import annotations

from aryeo.resources._base import ResourceClient
from aryeo.types import JSONMapping, JSONResponse, QueryParams, RequestTimeout


class AppointmentsResource(ResourceClient):
    """Access appointments API operations."""

    def list(self, *, params: QueryParams | None = None, timeout: RequestTimeout = None) -> JSONResponse:
        """List appointments.

        Args:
            params: Optional query parameters for the underlying API call.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request("GET", "/appointments", params=params, timeout=timeout, auth_required=True)

    def get(self, appointment_id: str, *, params: QueryParams | None = None, timeout: RequestTimeout = None) -> JSONResponse:
        """Get appointment.

        Args:
            appointment_id: The `appointment_id` path value.
            params: Optional query parameters for the underlying API call.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request("GET", f"/appointments/{appointment_id}", params=params, timeout=timeout, auth_required=True)

    def update(self, appointment_id: str, *, payload: JSONMapping | None = None, timeout: RequestTimeout = None) -> JSONResponse:
        """Update appointment.

        Args:
            appointment_id: The `appointment_id` path value.
            payload: JSON payload matching AppointmentUpdatePutPayload.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request("PUT", f"/appointments/{appointment_id}", payload=payload, timeout=timeout, auth_required=True)

    def cancel(self, appointment_id: str, *, payload: JSONMapping | None = None, timeout: RequestTimeout = None) -> JSONResponse:
        """Cancel appointment.

        Args:
            appointment_id: The `appointment_id` path value.
            payload: JSON payload matching AppointmentCancelPutPayload.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request("PUT", f"/appointments/{appointment_id}/cancel", payload=payload, timeout=timeout, auth_required=True)

    def postpone(self, appointment_id: str, *, payload: JSONMapping | None = None, timeout: RequestTimeout = None) -> JSONResponse:
        """Postpone appointment.

        Args:
            appointment_id: The `appointment_id` path value.
            payload: JSON payload matching AppointmentPostponePutPayload.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request("PUT", f"/appointments/{appointment_id}/postpone", payload=payload, timeout=timeout, auth_required=True)

    def reschedule(self, appointment_id: str, *, payload: JSONMapping | None = None, timeout: RequestTimeout = None) -> JSONResponse:
        """Reschedule appointment.

        Args:
            appointment_id: The `appointment_id` path value.
            payload: JSON payload matching AppointmentReschedulePutPayload.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request("PUT", f"/appointments/{appointment_id}/reschedule", payload=payload, timeout=timeout, auth_required=True)

    def accept(self, appointment_id: str, *, payload: JSONMapping | None = None, timeout: RequestTimeout = None) -> JSONResponse:
        """Accept appointment.

        Args:
            appointment_id: The `appointment_id` path value.
            payload: JSON payload matching AppointmentAcceptPutPayload.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request("PUT", f"/appointments/{appointment_id}/accept", payload=payload, timeout=timeout, auth_required=True)

    def decline(self, appointment_id: str, *, payload: JSONMapping | None = None, timeout: RequestTimeout = None) -> JSONResponse:
        """Decline appointment.

        Args:
            appointment_id: The `appointment_id` path value.
            payload: JSON payload matching AppointmentDeclinePutPayload.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request("PUT", f"/appointments/{appointment_id}/decline", payload=payload, timeout=timeout, auth_required=True)

    def schedule(self, appointment_id: str, *, payload: JSONMapping | None = None, timeout: RequestTimeout = None) -> JSONResponse:
        """Schedule appointment.

        Args:
            appointment_id: The `appointment_id` path value.
            payload: JSON payload matching AppointmentSchedulePutPayload.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request("PUT", f"/appointments/{appointment_id}/schedule", payload=payload, timeout=timeout, auth_required=True)

    def check_availability(self, appointment_id: str, *, params: QueryParams | None = None, timeout: RequestTimeout = None) -> JSONResponse:
        """Check appointment availability.

        Args:
            appointment_id: The `appointment_id` path value.
            params: Optional query parameters for the underlying API call.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request("GET", f"/appointments/{appointment_id}/availability", params=params, timeout=timeout, auth_required=True)

    def get_3d_home_capture_link(self, appointment_id: str, *, timeout: RequestTimeout = None) -> JSONResponse:
        """Get appointment 3D Home Capture link.

        Args:
            appointment_id: The `appointment_id` path value.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request("GET", f"/appointments/{appointment_id}/3dh-tour-link", timeout=timeout, auth_required=True)

    def create(self, *, payload: JSONMapping | None = None, timeout: RequestTimeout = None) -> JSONResponse:
        """Create appointment.

        Args:
            payload: JSON payload matching AppointmentStorePostPayload.
            timeout: Optional per-request timeout override.

        Returns:
            The decoded JSON payload returned by the API.

        Raises:
            AryeoAPIError: If the API returns a non-success response.
            AryeoRequestError: If the request fails before completion.
        """
        return self._request("POST", "/appointments/store", payload=payload, timeout=timeout, auth_required=True)


__all__ = ["AppointmentsResource"]
