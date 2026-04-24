
# Package And Versioning ADR

## Decision

- Distribution name: `aryeo`
- Import package: `aryeo`
- Initial version: `0.1.0`
- Version sources of truth: `pyproject.toml` and `aryeo/__init__.py`

## Rationale

- The repo name and API name already align on `aryeo`.
- Keeping the version in exactly two files matches the planning reference.
- The package currently exposes low-level JSON methods, so a `0.x` version is
  more honest than pretending the client is stable.

## Follow-Up

- Confirm PyPI name availability before publication.
- Decide when typed models justify a `1.0.0` stability target.
