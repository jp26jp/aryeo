
# Style Guide

## Python

- Use Google-style docstrings on public modules, classes, and functions.
- Prefer explicit, thorough type hints over `Any`.
- Keep shared HTTP behavior in `aryeo/base_client.py`.
- Keep flat resource modules such as `aryeo/orders.py` as the primary public
  surface.
- Keep `aryeo/resources/` as compatibility exports only.
- Keep `aryeo/types.py` limited to transport-level aliases.
- Generate models and enums from `docs/api/aryeo.json`; do not invent fields.

## Sync Rules

- Update tests, docs, examples, and planning docs whenever the client surface
  changes.
- Treat `docs/api/` and `docs/planning/aryeo-api-client/` as the contract
  sources before changing endpoint behavior.
- Regenerate the client scaffold with `python tools/bootstrap_client_repo.py`
  after meaningful OpenAPI changes.
