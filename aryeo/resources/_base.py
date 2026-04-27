
"""Shared helpers for generated Aryeo resource clients."""

from __future__ import annotations

from aryeo.base_client import BaseClient
from aryeo.types import JSONMapping, JSONResponse, QueryParams, RequestTimeout


class ResourceClient:
    """Wrap the shared `BaseClient` for a specific resource group."""

    def __init__(self, client: BaseClient) -> None:
        """Store the shared base client.

        Args:
            client: The root Aryeo client transport.
        """

        self._client = client

    def _request(
        self,
        method: str,
        path: str,
        *,
        params: QueryParams | None = None,
        payload: JSONMapping | None = None,
        timeout: RequestTimeout = None,
        auth_required: bool = True,
    ) -> JSONResponse:
        """Delegate a JSON request to the shared base client."""

        return self._client.request_json(
            method,
            path,
            params=params,
            payload=payload,
            timeout=timeout,
            auth_required=auth_required,
        )
