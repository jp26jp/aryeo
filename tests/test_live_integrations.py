"""Tests for the opt-in live integration verification command."""

from __future__ import annotations

import os
from pathlib import Path

import pytest

from aryeo.client import RESOURCE_NAMES
from tools.verify_live_integrations import (
    LIVE_CHECKS,
    LiveResult,
    exit_code,
    load_env_file,
)


def test_live_checks_cover_each_resource_group() -> None:
    """The live matrix should account for every generated resource group."""

    assert {check.resource_name for check in LIVE_CHECKS} == set(RESOURCE_NAMES)


def test_live_checks_do_not_run_mutations_by_default() -> None:
    """Mutation endpoints should be represented as skipped checks."""

    mutating_methods = ("POST", "PUT", "PATCH", "DELETE")

    for check in LIVE_CHECKS:
        method = check.endpoint.split(" ", 1)[0]
        if method in mutating_methods:
            assert check.skip_reason


def test_load_env_file_preserves_exported_values(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Dotenv loading should not overwrite values already in the environment."""

    env_file = tmp_path / ".env"
    env_file.write_text(
        "ARYEO_API_KEY=file-token\nARYEO_TIMEOUT=3\n",
        encoding="utf-8",
    )
    monkeypatch.setenv("ARYEO_API_KEY", "exported-token")
    monkeypatch.delenv("ARYEO_TIMEOUT", raising=False)

    values = load_env_file(env_file)

    assert values == {"ARYEO_API_KEY": "file-token", "ARYEO_TIMEOUT": "3"}
    assert os.environ["ARYEO_API_KEY"] == "exported-token"
    assert os.environ["ARYEO_TIMEOUT"] == "3"


def test_exit_code_respects_failures_and_strict_skips() -> None:
    """The command should fail on errors and optionally fail on skips."""

    passed = LiveResult("orders", "list", "GET /orders", "passed", "ok")
    skipped = LiveResult("videos", "get", "GET /videos/{video_id}", "skipped", "id")
    failed = LiveResult("orders", "list", "GET /orders", "failed", "boom")

    assert exit_code([passed], strict=False) == 0
    assert exit_code([passed, skipped], strict=False) == 0
    assert exit_code([passed, skipped], strict=True) == 1
    assert exit_code([failed], strict=False) == 1
