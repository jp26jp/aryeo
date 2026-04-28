"""Request-construction tests for `aryeo.addresses`."""

from __future__ import annotations

import pytest

from tests.helpers import ClientFactory, assert_resource_method_request

CASES = [
    (
        "create",
        {},
        {"payload": {"example": "value"}},
        "POST",
        "/addresses",
        False,
    ),
    (
        "get",
        {"address": "00000000-0000-4000-8000-000000000000"},
        {},
        "GET",
        "/addresses/{address}",
        False,
    ),
    (
        "update",
        {"address": "00000000-0000-4000-8000-000000000000"},
        {"payload": {"example": "value"}},
        "PATCH",
        "/addresses/{address}",
        False,
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
def test_addresses_resource_methods(
    client_factory: ClientFactory,
    method_name: str,
    path_arguments: dict[str, str],
    call_kwargs: dict[str, object],
    expected_method: str,
    expected_path: str,
    auth_required: bool,
) -> None:
    """Each Addresses method should issue the documented HTTP request."""

    assert_resource_method_request(
        client_factory,
        resource_name="addresses",
        method_name=method_name,
        path_arguments=path_arguments,
        call_kwargs=call_kwargs,
        expected_method=expected_method,
        expected_path=expected_path,
        auth_required=auth_required,
    )
