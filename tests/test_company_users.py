"""Request-construction tests for `aryeo.company_users`."""

from __future__ import annotations

import pytest

from tests.helpers import ClientFactory, assert_resource_method_request

CASES = [
    (
        "list_team_members",
        {},
        {"params": {"page": 1}},
        "GET",
        "/company-team-members",
        True,
    ),
    (
        "get_team_member",
        {"company_team_member_id": "00000000-0000-4000-8000-000000000000"},
        {"params": {"page": 1}},
        "GET",
        "/company-team-members/{company_team_member_id}",
        True,
    ),
    (
        "list_team_member_events",
        {"company_team_member_id": "00000000-0000-4000-8000-000000000000"},
        {"params": {"page": 1}},
        "GET",
        "/company-team-members/{company_team_member_id}/events",
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
def test_company_users_resource_methods(
    client_factory: ClientFactory,
    method_name: str,
    path_arguments: dict[str, str],
    call_kwargs: dict[str, object],
    expected_method: str,
    expected_path: str,
    auth_required: bool,
) -> None:
    """Each Company Users method should issue the documented HTTP request."""

    assert_resource_method_request(
        client_factory,
        resource_name="company_users",
        method_name=method_name,
        path_arguments=path_arguments,
        call_kwargs=call_kwargs,
        expected_method=expected_method,
        expected_path=expected_path,
        auth_required=auth_required,
    )
