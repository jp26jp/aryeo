"""Environment helpers shared by runnable Aryeo examples."""

from __future__ import annotations

import os
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ENV_FILE = REPO_ROOT / ".env"


def load_example_environment(path: Path = DEFAULT_ENV_FILE) -> dict[str, str]:
    """Load simple dotenv values for local examples.

    The helper keeps already-exported environment variables intact and exists so
    examples can be run directly from a local checkout without an extra
    dependency on `python-dotenv`.

    Args:
        path: Dotenv file to load.

    Returns:
        Parsed environment values from the file.
    """

    values: dict[str, str] = {}
    if not path.exists():
        return values

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line.removeprefix("export ").strip()
        if "=" not in line:
            continue

        name, raw_value = line.split("=", 1)
        value = raw_value.strip().strip('"').strip("'")
        env_name = name.strip()
        values[env_name] = value
        os.environ.setdefault(env_name, value)

    return values
