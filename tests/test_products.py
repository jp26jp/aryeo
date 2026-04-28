"""Request-construction tests for `aryeo.products`."""

from __future__ import annotations

import pytest

from tests.helpers import ClientFactory, assert_resource_method_request

CASES = [
    (
        "list_categories",
        {},
        {"params": {"page": 1}},
        "GET",
        "/product-categories",
        True,
    ),
    (
        "list",
        {},
        {"params": {"page": 1}},
        "GET",
        "/products",
        True,
    ),
    (
        "create_tax",
        {},
        {"payload": {"example": "value"}},
        "POST",
        "/taxes",
        True,
    ),
    (
        "delete_tax",
        {"tax_id": "00000000-0000-4000-8000-000000000000"},
        {},
        "DELETE",
        "/taxes/{tax_id}",
        True,
    ),
    (
        "list_territories",
        {},
        {"params": {"page": 1}},
        "GET",
        "/territories",
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
def test_products_resource_methods(
    client_factory: ClientFactory,
    method_name: str,
    path_arguments: dict[str, str],
    call_kwargs: dict[str, object],
    expected_method: str,
    expected_path: str,
    auth_required: bool,
) -> None:
    """Each Products method should issue the documented HTTP request."""

    assert_resource_method_request(
        client_factory,
        resource_name="products",
        method_name=method_name,
        path_arguments=path_arguments,
        call_kwargs=call_kwargs,
        expected_method=expected_method,
        expected_path=expected_path,
        auth_required=auth_required,
    )
