"""Request-construction tests for `aryeo.discounts`."""

from __future__ import annotations

import pytest

from tests.helpers import ClientFactory, assert_resource_method_request

CASES = [
    (
        "list_coupons",
        {},
        {"params": {"page": 1}},
        "GET",
        "/coupons",
        True,
    ),
    (
        "create",
        {},
        {"payload": {"example": "value"}},
        "POST",
        "/discounts",
        True,
    ),
    (
        "delete",
        {"discount_id": "00000000-0000-4000-8000-000000000000"},
        {},
        "DELETE",
        "/discounts/{discount_id}",
        True,
    ),
    (
        "delete_order",
        {
            "order": "00000000-0000-4000-8000-000000000000",
            "discount": "00000000-0000-4000-8000-000000000000",
        },
        {},
        "DELETE",
        "/orders/{order}/discounts/{discount}",
        True,
    ),
    (
        "redeem_promotion_code",
        {
            "discounted_type": "00000000-0000-4000-8000-000000000000",
            "discounted": "00000000-0000-4000-8000-000000000000",
        },
        {"payload": {"example": "value"}},
        "POST",
        "/promotion-codes/redeem/{discounted_type}/{discounted}",
        False,
    ),
    (
        "refund_order_payment",
        {"order_payment": "00000000-0000-4000-8000-000000000000"},
        {"payload": {"example": "value"}},
        "POST",
        "/refunds/{order_payment}",
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
def test_discounts_resource_methods(
    client_factory: ClientFactory,
    method_name: str,
    path_arguments: dict[str, str],
    call_kwargs: dict[str, object],
    expected_method: str,
    expected_path: str,
    auth_required: bool,
) -> None:
    """Each Discounts method should issue the documented HTTP request."""

    assert_resource_method_request(
        client_factory,
        resource_name="discounts",
        method_name=method_name,
        path_arguments=path_arguments,
        call_kwargs=call_kwargs,
        expected_method=expected_method,
        expected_path=expected_path,
        auth_required=auth_required,
    )
