"""Request-construction tests for `aryeo.order_forms`."""

from __future__ import annotations

import pytest

from tests.helpers import ClientFactory, assert_resource_method_request

CASES = [
    (
        "create_session",
        {},
        {"payload": {"example": "value"}},
        "POST",
        "/order-form-sessions",
        True,
    ),
    (
        "list",
        {},
        {},
        "GET",
        "/order-forms",
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
def test_order_forms_resource_methods(
    client_factory: ClientFactory,
    method_name: str,
    path_arguments: dict[str, str],
    call_kwargs: dict[str, object],
    expected_method: str,
    expected_path: str,
    auth_required: bool,
) -> None:
    """Each Order Forms method should issue the documented HTTP request."""

    assert_resource_method_request(
        client_factory,
        resource_name="order_forms",
        method_name=method_name,
        path_arguments=path_arguments,
        call_kwargs=call_kwargs,
        expected_method=expected_method,
        expected_path=expected_path,
        auth_required=auth_required,
    )
