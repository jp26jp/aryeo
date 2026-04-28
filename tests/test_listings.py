"""Request-construction tests for `aryeo.listings`."""

from __future__ import annotations

import pytest

from tests.helpers import ClientFactory, assert_resource_method_request

CASES = [
    (
        "list",
        {},
        {"params": {"page": 1}},
        "GET",
        "/listings",
        True,
    ),
    (
        "create",
        {},
        {"payload": {"example": "value"}},
        "POST",
        "/listings",
        True,
    ),
    (
        "get",
        {"listing_id": "00000000-0000-4000-8000-000000000000"},
        {"params": {"page": 1}},
        "GET",
        "/listings/{listing_id}",
        True,
    ),
    (
        "update",
        {"listing_id": "00000000-0000-4000-8000-000000000000"},
        {"payload": {"example": "value"}},
        "PUT",
        "/listings/{listing_id}",
        True,
    ),
    (
        "get_cubicasa_information",
        {"listing_id": "00000000-0000-4000-8000-000000000000"},
        {},
        "GET",
        "/listings/{listing_id}/cubi-casa",
        True,
    ),
    (
        "search_details",
        {"listing_id": "00000000-0000-4000-8000-000000000000"},
        {},
        "GET",
        "/listings/{listing_id}/details/search",
        True,
    ),
    (
        "get_statistics",
        {"listing_id": "00000000-0000-4000-8000-000000000000"},
        {},
        "GET",
        "/listings/{listing_id}/stats",
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
def test_listings_resource_methods(
    client_factory: ClientFactory,
    method_name: str,
    path_arguments: dict[str, str],
    call_kwargs: dict[str, object],
    expected_method: str,
    expected_path: str,
    auth_required: bool,
) -> None:
    """Each Listings method should issue the documented HTTP request."""

    assert_resource_method_request(
        client_factory,
        resource_name="listings",
        method_name=method_name,
        path_arguments=path_arguments,
        call_kwargs=call_kwargs,
        expected_method=expected_method,
        expected_path=expected_path,
        auth_required=auth_required,
    )
