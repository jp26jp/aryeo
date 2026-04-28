"""Compatibility entrypoint for the Aryeo client generator.

Historically this module contained the generator implementation. The canonical
implementation now lives in :mod:`tools.aryeo_codegen`; keep this wrapper so
existing docs and scripts can continue to run ``python tools/bootstrap_client_repo.py``.
"""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    """Generate the Aryeo client scaffold from the checked-in API docs."""

    if str(REPO_ROOT) not in sys.path:
        sys.path.insert(0, str(REPO_ROOT))

    from tools.aryeo_codegen import run_from_cli

    run_from_cli()


if __name__ == "__main__":
    main()
