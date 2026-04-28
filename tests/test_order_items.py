"""Request-construction tests for `aryeo.order_items`."""

from __future__ import annotations

import pytest

from tests.helpers import ClientFactory, assert_resource_method_request

CASES = [
    (
        "create",
        {},
        {"payload": {"example": "value"}},
        "POST",
        "/order-items",
        True,
    ),
    (
        "get",
        {"order_item_id": "00000000-0000-4000-8000-000000000000"},
        {"params": {"page": 1}},
        "GET",
        "/order-items/{order_item_id}",
        True,
    ),
    (
        "update",
        {"order_item_id": "00000000-0000-4000-8000-000000000000"},
        {},
        "PUT",
        "/order-items/{order_item_id}",
        True,
    ),
    (
        "delete",
        {"order_item_id": "00000000-0000-4000-8000-000000000000"},
        {},
        "DELETE",
        "/order-items/{order_item_id}",
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
def test_order_items_resource_methods(
    client_factory: ClientFactory,
    method_name: str,
    path_arguments: dict[str, str],
    call_kwargs: dict[str, object],
    expected_method: str,
    expected_path: str,
    auth_required: bool,
) -> None:
    """Each Order Items method should issue the documented HTTP request."""

    assert_resource_method_request(
        client_factory,
        resource_name="order_items",
        method_name=method_name,
        path_arguments=path_arguments,
        call_kwargs=call_kwargs,
        expected_method=expected_method,
        expected_path=expected_path,
        auth_required=auth_required,
    )
