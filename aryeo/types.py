"""Shared transport-level type aliases used by the Aryeo client runtime."""

from __future__ import annotations

from typing import TypeAlias

import httpx

JSONScalar: TypeAlias = str | int | float | bool | None
JSONValue: TypeAlias = JSONScalar | dict[str, "JSONValue"] | list["JSONValue"]
JSONMapping: TypeAlias = dict[str, JSONValue]
JSONResponse: TypeAlias = JSONValue

QueryScalar: TypeAlias = str | int | float | bool | None
QueryValue: TypeAlias = QueryScalar | list[QueryScalar] | tuple[QueryScalar, ...]
QueryParams: TypeAlias = dict[str, QueryValue]

RequestTimeoutTuple: TypeAlias = tuple[
    float | None,
    float | None,
    float | None,
    float | None,
]
RequestTimeout: TypeAlias = float | httpx.Timeout | RequestTimeoutTuple | None

__all__ = [
    "JSONMapping",
    "JSONResponse",
    "JSONScalar",
    "JSONValue",
    "QueryParams",
    "QueryScalar",
    "QueryValue",
    "RequestTimeout",
    "RequestTimeoutTuple",
]
