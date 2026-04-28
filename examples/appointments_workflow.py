"""Example workflow for appointment availability reads."""

from __future__ import annotations

from aryeo import AryeoClient


def main() -> None:
    """Check appointment availability for a fixture appointment."""

    with AryeoClient.from_env() as client:
        client.appointments.check_availability(
            "00000000-0000-4000-8000-000000000000", params={"page": 1}
        )


if __name__ == "__main__":
    main()
