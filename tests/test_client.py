"""Unit tests for the high-level Aryeo client."""

from __future__ import annotations

from aryeo import AddressesResource, AryeoClient
from aryeo.client import RESOURCE_NAMES


def test_client_exposes_generated_resources(client_factory: object) -> None:
    """The top-level client should expose each generated resource attribute."""

    client, _ = client_factory("token-value")

    for resource_name in RESOURCE_NAMES:
        assert hasattr(client, resource_name)


def test_top_level_exports_include_resource_client() -> None:
    """The package should export public resource client classes."""

    assert AddressesResource.__name__ == "AddressesResource"


def test_client_from_env_reads_standard_variables(monkeypatch: object) -> None:
    """The convenience constructor should honor the default env var names."""

    monkeypatch.setenv("ARYEO_API_TOKEN", "env-token")
    monkeypatch.setenv("ARYEO_BASE_URL", "https://example.test/api")
    monkeypatch.setenv("ARYEO_TIMEOUT", "12")

    client = AryeoClient.from_env()

    assert client.base_url == "https://example.test/api"
    client.close()
