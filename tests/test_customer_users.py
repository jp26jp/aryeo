"""Request-construction tests for `aryeo.customer_users`."""

from __future__ import annotations

import pytest

from tests.helpers import ClientFactory, assert_resource_method_request

CASES = [
    (
        "get_team_member",
        {"customer_team_member_id": "00000000-0000-4000-8000-000000000000"},
        {"params": {"page": 1}},
        "GET",
        "/customer-team-members/{customer_team_member_id}",
        True,
    ),
    (
        "create_team_affiliate_membership",
        {},
        {"payload": {"example": "value"}},
        "POST",
        "/customer-teams/affiliate-memberships",
        True,
    ),
    (
        "list_team_memberships",
        {"customer_team_id": "00000000-0000-4000-8000-000000000000"},
        {"params": {"page": 1}},
        "GET",
        "/customer-teams/{customer_team_id}/memberships",
        True,
    ),
    (
        "list",
        {},
        {"params": {"page": 1}},
        "GET",
        "/customer-users",
        True,
    ),
    (
        "create",
        {},
        {"payload": {"example": "value"}},
        "POST",
        "/customer-users",
        True,
    ),
    (
        "store_credit_transaction",
        {"user": "00000000-0000-4000-8000-000000000000"},
        {"payload": {"example": "value"}},
        "POST",
        "/customer-users/{user}/credit-transactions",
        True,
    ),
    (
        "list_customers",
        {},
        {"params": {"page": 1}},
        "GET",
        "/customers",
        True,
    ),
    (
        "create_customers",
        {},
        {"payload": {"example": "value"}},
        "POST",
        "/customers",
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
def test_customer_users_resource_methods(
    client_factory: ClientFactory,
    method_name: str,
    path_arguments: dict[str, str],
    call_kwargs: dict[str, object],
    expected_method: str,
    expected_path: str,
    auth_required: bool,
) -> None:
    """Each Customer Users method should issue the documented HTTP request."""

    assert_resource_method_request(
        client_factory,
        resource_name="customer_users",
        method_name=method_name,
        path_arguments=path_arguments,
        call_kwargs=call_kwargs,
        expected_method=expected_method,
        expected_path=expected_path,
        auth_required=auth_required,
    )
