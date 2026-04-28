"""Request-construction tests for `aryeo.appointments`."""

from __future__ import annotations

import pytest

from tests.helpers import ClientFactory, assert_resource_method_request

CASES = [
    (
        "list",
        {},
        {"params": {"page": 1}},
        "GET",
        "/appointments",
        True,
    ),
    (
        "create",
        {},
        {"payload": {"example": "value"}},
        "POST",
        "/appointments/store",
        True,
    ),
    (
        "get",
        {"appointment_id": "00000000-0000-4000-8000-000000000000"},
        {"params": {"page": 1}},
        "GET",
        "/appointments/{appointment_id}",
        True,
    ),
    (
        "update",
        {"appointment_id": "00000000-0000-4000-8000-000000000000"},
        {"payload": {"example": "value"}},
        "PUT",
        "/appointments/{appointment_id}",
        True,
    ),
    (
        "get_3d_home_capture_link",
        {"appointment_id": "00000000-0000-4000-8000-000000000000"},
        {},
        "GET",
        "/appointments/{appointment_id}/3dh-tour-link",
        True,
    ),
    (
        "accept",
        {"appointment_id": "00000000-0000-4000-8000-000000000000"},
        {"payload": {"example": "value"}},
        "PUT",
        "/appointments/{appointment_id}/accept",
        True,
    ),
    (
        "check_availability",
        {"appointment_id": "00000000-0000-4000-8000-000000000000"},
        {"params": {"page": 1}},
        "GET",
        "/appointments/{appointment_id}/availability",
        True,
    ),
    (
        "cancel",
        {"appointment_id": "00000000-0000-4000-8000-000000000000"},
        {"payload": {"example": "value"}},
        "PUT",
        "/appointments/{appointment_id}/cancel",
        True,
    ),
    (
        "decline",
        {"appointment_id": "00000000-0000-4000-8000-000000000000"},
        {"payload": {"example": "value"}},
        "PUT",
        "/appointments/{appointment_id}/decline",
        True,
    ),
    (
        "postpone",
        {"appointment_id": "00000000-0000-4000-8000-000000000000"},
        {"payload": {"example": "value"}},
        "PUT",
        "/appointments/{appointment_id}/postpone",
        True,
    ),
    (
        "reschedule",
        {"appointment_id": "00000000-0000-4000-8000-000000000000"},
        {"payload": {"example": "value"}},
        "PUT",
        "/appointments/{appointment_id}/reschedule",
        True,
    ),
    (
        "schedule",
        {"appointment_id": "00000000-0000-4000-8000-000000000000"},
        {"payload": {"example": "value"}},
        "PUT",
        "/appointments/{appointment_id}/schedule",
        True,
    ),
]


@pytest.mark.parametrize(
    (
        "method_name",
        "path_arguments",
        "call_kwargs",
        "expected_method",
        "expected_path",
        "auth_required",
    ),
    CASES,
)
def test_appointments_resource_methods(
    client_factory: ClientFactory,
    method_name: str,
    path_arguments: dict[str, str],
    call_kwargs: dict[str, object],
    expected_method: str,
    expected_path: str,
    auth_required: bool,
) -> None:
    """Each Appointments method should issue the documented HTTP request."""

    assert_resource_method_request(
        client_factory,
        resource_name="appointments",
        method_name=method_name,
        path_arguments=path_arguments,
        call_kwargs=call_kwargs,
        expected_method=expected_method,
        expected_path=expected_path,
        auth_required=auth_required,
    )
