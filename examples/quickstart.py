"""Quickstart example for the Aryeo client."""

from __future__ import annotations

from aryeo import AryeoClient


def main() -> None:
    """Run a small example against the Aryeo API."""

    with AryeoClient.from_env() as client:
        client.orders.list(params={"page": 1, "per_page": 5})
        client.listings.get("00000000-0000-4000-8000-000000000000")


if __name__ == "__main__":
    main()
