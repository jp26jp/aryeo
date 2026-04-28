"""Request-construction tests for `aryeo.orders`."""

from __future__ import annotations

import pytest

from tests.helpers import ClientFactory, assert_resource_method_request

CASES = [
    (
        "list",
        {},
        {"params": {"page": 1}},
        "GET",
        "/orders",
        True,
    ),
    (
        "create",
        {},
        {"payload": {"example": "value"}},
        "POST",
        "/orders",
        True,
    ),
    (
        "get",
        {"order_id": "00000000-0000-4000-8000-000000000000"},
        {"params": {"page": 1}},
        "GET",
        "/orders/{order_id}",
        True,
    ),
    (
        "update_billing_address",
        {"order": "00000000-0000-4000-8000-000000000000"},
        {"payload": {"example": "value"}},
        "PUT",
        "/orders/{order}/billing-address",
        True,
    ),
    (
        "get_payment_information",
        {"order": "00000000-0000-4000-8000-000000000000"},
        {},
        "GET",
        "/orders/{order}/payment-info",
        False,
    ),
    (
        "create_manual_payment",
        {"order": "00000000-0000-4000-8000-000000000000"},
        {"payload": {"example": "value"}},
        "POST",
        "/orders/{order}/payments",
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
def test_orders_resource_methods(
    client_factory: ClientFactory,
    method_name: str,
    path_arguments: dict[str, str],
    call_kwargs: dict[str, object],
    expected_method: str,
    expected_path: str,
    auth_required: bool,
) -> None:
    """Each Orders method should issue the documented HTTP request."""

    assert_resource_method_request(
        client_factory,
        resource_name="orders",
        method_name=method_name,
        path_arguments=path_arguments,
        call_kwargs=call_kwargs,
        expected_method=expected_method,
        expected_path=expected_path,
        auth_required=auth_required,
    )
