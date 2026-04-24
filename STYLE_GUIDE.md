
# Style Guide

## Python

- Use Google-style docstrings on public modules, classes, and functions.
- Prefer explicit, thorough type hints over `Any`.
- Keep the shared HTTP behavior in `aryeo/base_client.py`.
- Treat generated resource modules as low-level transport surfaces until typed
  request and response models land.

## Sync Rules

- Update tests, docs, examples, and planning docs whenever the client surface
  changes.
- Treat `docs/api/` and `docs/planning/aryeo-api-client/` as the contract
  sources before changing endpoint behavior.
- Regenerate the client scaffold with `python tools/bootstrap_client_repo.py`
  after meaningful OpenAPI changes.
