
"""Top-level package exports for the Aryeo client."""

from aryeo.client import AryeoClient
from aryeo.exceptions import (
    AryeoAPIError,
    AryeoConfigurationError,
    AryeoError,
    AryeoRequestError,
)

__all__ = [
    "AryeoAPIError",
    "AryeoClient",
    "AryeoConfigurationError",
    "AryeoError",
    "AryeoRequestError",
]

__version__ = "0.1.0"
