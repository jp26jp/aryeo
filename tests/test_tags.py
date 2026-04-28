"""Request-construction tests for `aryeo.tags`."""

from __future__ import annotations

import pytest

from tests.helpers import ClientFactory, assert_resource_method_request

CASES = [
    (
        "create_customer_team",
        {"customer_team_id": "00000000-0000-4000-8000-000000000000"},
        {"payload": {"example": "value"}},
        "POST",
        "/customer-teams/{customer_team_id}/tags",
        True,
    ),
    (
        "update_customer_team",
        {"customer_team_id": "00000000-0000-4000-8000-000000000000"},
        {"payload": {"example": "value"}},
        "PUT",
        "/customer-teams/{customer_team_id}/tags",
        True,
    ),
    (
        "delete_customer_team",
        {
            "customer_team_id": "00000000-0000-4000-8000-000000000000",
            "tag_id": "00000000-0000-4000-8000-000000000000",
        },
        {},
        "DELETE",
        "/customer-teams/{customer_team_id}/tags/{tag_id}",
        True,
    ),
    (
        "create_for_order",
        {"order_id": "00000000-0000-4000-8000-000000000000"},
        {"payload": {"example": "value"}},
        "POST",
        "/orders/{order_id}/tags",
        True,
    ),
    (
        "update_for_order",
        {"order_id": "00000000-0000-4000-8000-000000000000"},
        {"payload": {"example": "value"}},
        "PUT",
        "/orders/{order_id}/tags",
        True,
    ),
    (
        "delete_for_order",
        {
            "order_id": "00000000-0000-4000-8000-000000000000",
            "tag_id": "00000000-0000-4000-8000-000000000000",
        },
        {},
        "DELETE",
        "/orders/{order_id}/tags/{tag_id}",
        True,
    ),
    (
        "create",
        {"product_id": "00000000-0000-4000-8000-000000000000"},
        {"payload": {"example": "value"}},
        "POST",
        "/products/{product_id}/tags",
        True,
    ),
    (
        "update_product",
        {"product_id": "00000000-0000-4000-8000-000000000000"},
        {"payload": {"example": "value"}},
        "PUT",
        "/products/{product_id}/tags",
        True,
    ),
    (
        "update",
        {
            "product_id": "00000000-0000-4000-8000-000000000000",
            "tag_id": "00000000-0000-4000-8000-000000000000",
        },
        {"payload": {"example": "value"}},
        "PUT",
        "/products/{product_id}/tags/{tag_id}",
        True,
    ),
    (
        "delete_product",
        {
            "product_id": "00000000-0000-4000-8000-000000000000",
            "tag_id": "00000000-0000-4000-8000-000000000000",
        },
        {},
        "DELETE",
        "/products/{product_id}/tags/{tag_id}",
        True,
    ),
    (
        "create_tags",
        {},
        {"payload": {"example": "value"}},
        "POST",
        "/tags",
        True,
    ),
    (
        "update_tags",
        {"tag_id": "00000000-0000-4000-8000-000000000000"},
        {"payload": {"example": "value"}},
        "PUT",
        "/tags/{tag_id}",
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
def test_tags_resource_methods(
    client_factory: ClientFactory,
    method_name: str,
    path_arguments: dict[str, str],
    call_kwargs: dict[str, object],
    expected_method: str,
    expected_path: str,
    auth_required: bool,
) -> None:
    """Each Tags method should issue the documented HTTP request."""

    assert_resource_method_request(
        client_factory,
        resource_name="tags",
        method_name=method_name,
        path_arguments=path_arguments,
        call_kwargs=call_kwargs,
        expected_method=expected_method,
        expected_path=expected_path,
        auth_required=auth_required,
    )
