"""Tests for generated Aryeo models and enums."""

from __future__ import annotations

from aryeo.enums import ActivityNameEnum
from aryeo.models import Activity


def test_generated_model_is_importable() -> None:
    """Generated models should be importable from `aryeo.models`."""

    assert Activity.__name__ == "Activity"


def test_generated_enum_is_importable() -> None:
    """Generated enums should be importable from `aryeo.enums`."""

    assert ActivityNameEnum.__name__ == "ActivityNameEnum"
