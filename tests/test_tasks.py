"""Request-construction tests for `aryeo.tasks`."""

from __future__ import annotations

import pytest

from tests.helpers import ClientFactory, assert_resource_method_request

CASES = [
    (
        "list",
        {},
        {},
        "GET",
        "/tasks",
        True,
    ),
    (
        "create",
        {},
        {"payload": {"example": "value"}},
        "POST",
        "/tasks",
        True,
    ),
    (
        "get",
        {"task_id": "00000000-0000-4000-8000-000000000000"},
        {},
        "GET",
        "/tasks/{task_id}",
        True,
    ),
    (
        "update",
        {"task_id": "00000000-0000-4000-8000-000000000000"},
        {"payload": {"example": "value"}},
        "PUT",
        "/tasks/{task_id}",
        True,
    ),
    (
        "delete",
        {"task_id": "00000000-0000-4000-8000-000000000000"},
        {},
        "DELETE",
        "/tasks/{task_id}",
        True,
    ),
    (
        "complete",
        {"task_id": "00000000-0000-4000-8000-000000000000"},
        {"payload": {"example": "value"}},
        "PUT",
        "/tasks/{task_id}/complete",
        True,
    ),
    (
        "reinstate",
        {"task_id": "00000000-0000-4000-8000-000000000000"},
        {"payload": {"example": "value"}},
        "PUT",
        "/tasks/{task_id}/reinstate",
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
def test_tasks_resource_methods(
    client_factory: ClientFactory,
    method_name: str,
    path_arguments: dict[str, str],
    call_kwargs: dict[str, object],
    expected_method: str,
    expected_path: str,
    auth_required: bool,
) -> None:
    """Each Tasks method should issue the documented HTTP request."""

    assert_resource_method_request(
        client_factory,
        resource_name="tasks",
        method_name=method_name,
        path_arguments=path_arguments,
        call_kwargs=call_kwargs,
        expected_method=expected_method,
        expected_path=expected_path,
        auth_required=auth_required,
    )
