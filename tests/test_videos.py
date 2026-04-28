"""Request-construction tests for `aryeo.videos`."""

from __future__ import annotations

import pytest

from tests.helpers import ClientFactory, assert_resource_method_request

CASES = [
    (
        "get",
        {"video_id": "00000000-0000-4000-8000-000000000000"},
        {},
        "GET",
        "/videos/{video_id}",
        True,
    ),
    (
        "update",
        {"video_id": "00000000-0000-4000-8000-000000000000"},
        {"payload": {"example": "value"}},
        "PUT",
        "/videos/{video_id}",
        True,
    ),
    (
        "delete",
        {"video_id": "00000000-0000-4000-8000-000000000000"},
        {},
        "DELETE",
        "/videos/{video_id}",
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
def test_videos_resource_methods(
    client_factory: ClientFactory,
    method_name: str,
    path_arguments: dict[str, str],
    call_kwargs: dict[str, object],
    expected_method: str,
    expected_path: str,
    auth_required: bool,
) -> None:
    """Each Videos method should issue the documented HTTP request."""

    assert_resource_method_request(
        client_factory,
        resource_name="videos",
        method_name=method_name,
        path_arguments=path_arguments,
        call_kwargs=call_kwargs,
        expected_method=expected_method,
        expected_path=expected_path,
        auth_required=auth_required,
    )
