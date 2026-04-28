
# Package And Versioning ADR

## Decision

- Distribution name: `aryeo`
- Import package: `aryeo`
- Initial version: `0.1.0`
- Version sources of truth: `pyproject.toml` and `aryeo/__init__.py`
- Python support: `>=3.11`

## Intentional Project Decisions

- Aryeo keeps Python `>=3.11` to avoid broad syntax and CI refactors in this
  pass.
- Aryeo keeps `httpx` as its sync transport.

## Follow-Up

- Confirm PyPI name availability before publication.
- Decide when typed endpoint coercion justifies a `1.0.0` stability target.
