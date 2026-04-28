"""Request-construction tests for `aryeo.scheduling`."""

from __future__ import annotations

import pytest

from tests.helpers import ClientFactory, assert_resource_method_request

CASES = [
    (
        "create_block",
        {},
        {"payload": {"example": "value"}},
        "POST",
        "/blocks",
        True,
    ),
    (
        "get_block",
        {"block_id": "00000000-0000-4000-8000-000000000000"},
        {},
        "GET",
        "/blocks/{block_id}",
        True,
    ),
    (
        "update_block",
        {"block_id": "00000000-0000-4000-8000-000000000000"},
        {},
        "PUT",
        "/blocks/{block_id}",
        True,
    ),
    (
        "delete_block",
        {"block_id": "00000000-0000-4000-8000-000000000000"},
        {},
        "DELETE",
        "/blocks/{block_id}",
        True,
    ),
    (
        "list_regions",
        {},
        {"params": {"page": 1}},
        "GET",
        "/regions",
        True,
    ),
    (
        "get_assignment",
        {},
        {"params": {"page": 1}},
        "GET",
        "/scheduling/assignment",
        True,
    ),
    (
        "list_available_dates",
        {},
        {"params": {"page": 1}},
        "GET",
        "/scheduling/available-dates",
        True,
    ),
    (
        "list_available_timeslots",
        {},
        {"params": {"page": 1}},
        "GET",
        "/scheduling/available-timeslots",
        True,
    ),
    (
        "list_schedule_item_groupings",
        {},
        {"params": {"page": 1}},
        "GET",
        "/scheduling/item-groupings",
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
def test_scheduling_resource_methods(
    client_factory: ClientFactory,
    method_name: str,
    path_arguments: dict[str, str],
    call_kwargs: dict[str, object],
    expected_method: str,
    expected_path: str,
    auth_required: bool,
) -> None:
    """Each Scheduling method should issue the documented HTTP request."""

    assert_resource_method_request(
        client_factory,
        resource_name="scheduling",
        method_name=method_name,
        path_arguments=path_arguments,
        call_kwargs=call_kwargs,
        expected_method=expected_method,
        expected_path=expected_path,
        auth_required=auth_required,
    )
