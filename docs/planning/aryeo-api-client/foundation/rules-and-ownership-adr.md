
# Rules And Ownership ADR

## Planning Ownership

- `docs/planning/aryeo-api-client/` owns roadmap, readiness, and truthful status.
- `.cursor/rules/` owns repo-local AI guidance derived from the planning tree.

## Runtime Ownership

- `aryeo/base_client.py` owns transport, auth, and error behavior.
- `aryeo/client.py` owns resource bindings.
- `aryeo/<resource>.py` owns generated endpoint methods by tag.
- `aryeo/models.py` and `aryeo/enums.py` own generated schema
  types.
- `aryeo/resources/` owns compatibility re-exports only.

## Supporting Surfaces

- `tests/` owns regression coverage.
- `docs/` owns published documentation and examples.
- `.github/workflows/` owns automation and release quality checks.
