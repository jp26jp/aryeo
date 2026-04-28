"""Example workflow for customer user lookup."""

from __future__ import annotations

from aryeo import AryeoClient


def main() -> None:
    """List customer users using documented query parameters."""

    with AryeoClient.from_env() as client:
        client.customer_users.list(params={"page": 1, "per_page": 10})


if __name__ == "__main__":
    main()
