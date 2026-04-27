"""Example workflow for loading orders from Aryeo."""

from __future__ import annotations

import os

from _env import load_example_environment

from aryeo import AryeoClient


def main() -> None:
    """List orders and optionally fetch payment info for a configured order."""

    load_example_environment()
    with AryeoClient.from_env() as client:
        client.orders.list(params={"page": 1, "per_page": 10})
        order_id = os.getenv("ARYEO_LIVE_ORDER_ID")
        if order_id:
            client.orders.get_payment_information(order_id)


if __name__ == "__main__":
    main()
