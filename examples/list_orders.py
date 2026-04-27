
"""Example workflow for loading orders from Aryeo."""

from __future__ import annotations

from aryeo import AryeoClient


def main() -> None:
    """List the first page of orders and fetch a single payment-info record."""

    with AryeoClient.from_env() as client:
        client.orders.list(params={"page": 1, "per_page": 10})
        client.orders.get_payment_information("00000000-0000-4000-8000-000000000000")


if __name__ == "__main__":
    main()
