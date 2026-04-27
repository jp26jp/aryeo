
"""Shared HTTP transport helpers for the Aryeo Python client."""

from __future__ import annotations

from typing import cast

import httpx

from aryeo.exceptions import AryeoAPIError, AryeoConfigurationError, AryeoRequestError
from aryeo.types import JSONMapping, JSONResponse, QueryParams, RequestTimeout

DEFAULT_BASE_URL = "https://api.aryeo.com/v1"
DEFAULT_TIMEOUT: float = 30.0
DEFAULT_USER_AGENT = "aryeo-python-client"


class BaseClient:
    """Manage auth, transport, and JSON request behavior for Aryeo calls."""

    def __init__(
        self,
        token: str | None = None,
        *,
        base_url: str = DEFAULT_BASE_URL,
        timeout: RequestTimeout = DEFAULT_TIMEOUT,
        user_agent: str = DEFAULT_USER_AGENT,
        http_client: httpx.Client | None = None,
    ) -> None:
        """Initialize the shared client transport.

        Args:
            token: Optional bearer token used for protected operations.
            base_url: Base URL for API requests.
            timeout: Default request timeout.
            user_agent: User-Agent header sent with every request.
            http_client: Optional injected `httpx.Client`.
        """

        self._token = token
        self._base_url = base_url.rstrip("/")
        self._default_timeout = timeout
        self._user_agent = user_agent
        self._owns_http_client = http_client is None
        self._http_client = http_client or httpx.Client()

    @property
    def base_url(self) -> str:
        """Return the configured base URL."""

        return self._base_url

    def close(self) -> None:
        """Close the owned HTTP client when this instance created it."""

        if self._owns_http_client:
            self._http_client.close()

    def __enter__(self) -> "BaseClient":
        """Enter the client context manager."""

        return self

    def __exit__(self, *args: object) -> None:
        """Close the client when leaving a context manager."""

        self.close()

    def _build_headers(self, *, auth_required: bool) -> dict[str, str]:
        """Build per-request headers for the outgoing request.

        Args:
            auth_required: Whether the request requires a bearer token.

        Returns:
            A header mapping for the request.

        Raises:
            AryeoConfigurationError: If auth is required and no token is configured.
        """

        headers = {
            "Accept": "application/json",
            "User-Agent": self._user_agent,
        }
        if self._token:
            headers["Authorization"] = f"Bearer {self._token}"
        elif auth_required:
            raise AryeoConfigurationError(
                "A bearer token is required for this Aryeo API operation."
            )
        return headers

    def _build_url(self, path: str) -> str:
        """Construct a request URL from the base URL and relative API path."""

        return f"{self._base_url}{path}"

    def request_json(
        self,
        method: str,
        path: str,
        *,
        params: QueryParams | None = None,
        payload: JSONMapping | None = None,
        timeout: RequestTimeout = None,
        auth_required: bool = True,
    ) -> JSONResponse:
        """Execute a JSON API request and decode the response body.

        Args:
            method: HTTP method to use.
            path: API path that will be joined to the configured base URL.
            params: Optional query string parameters.
            payload: Optional JSON request body.
            timeout: Optional timeout override for this request.
            auth_required: Whether the request must include the bearer token.

        Returns:
            The decoded JSON response body, or `None` for empty responses.

        Raises:
            AryeoAPIError: If the API returns a non-success status code.
            AryeoRequestError: If the transport fails or the body is not JSON.
            AryeoConfigurationError: If auth is required and no token exists.
        """

        try:
            response = self._http_client.request(
                method=method,
                url=self._build_url(path),
                headers=self._build_headers(auth_required=auth_required),
                params=params,
                json=payload,
                timeout=timeout if timeout is not None else self._default_timeout,
            )
        except httpx.HTTPError as exc:
            raise AryeoRequestError("The Aryeo request did not complete.", exc) from exc

        if response.is_error:
            raise AryeoAPIError.from_response(response)

        if response.status_code == 204 or not response.content:
            return None

        try:
            body = cast(JSONResponse, response.json())
        except ValueError as exc:
            raise AryeoRequestError(
                "The Aryeo response body was not valid JSON.",
                exc,
            ) from exc

        return body
