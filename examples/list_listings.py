"""Example workflow for listing reads."""

from __future__ import annotations

from aryeo import AryeoClient


def main() -> None:
    """List listings and fetch details for a fixture listing."""

    with AryeoClient.from_env() as client:
        client.listings.list(params={"page": 1, "per_page": 10})
        client.listings.get("00000000-0000-4000-8000-000000000000")


if __name__ == "__main__":
    main()
