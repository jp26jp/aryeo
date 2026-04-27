"""Quickstart example for the Aryeo client."""

from __future__ import annotations

from _env import load_example_environment

from aryeo import AryeoClient


def main() -> None:
    """Run small read-only examples against the Aryeo API."""

    load_example_environment()
    with AryeoClient.from_env() as client:
        client.orders.list(params={"page": 1, "per_page": 5})
        client.listings.list(params={"page": 1, "per_page": 5})


if __name__ == "__main__":
    main()
