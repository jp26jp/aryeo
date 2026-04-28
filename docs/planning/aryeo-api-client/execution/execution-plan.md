
# Execution Plan

## Already Scaffolded

- Core runtime modules for transport, exceptions, and flat resource bindings
- Generated resource modules for every documented API tag
- Generated `aryeo/models.py` and `aryeo/enums.py`
- Planning docs and Cursor rules
- Examples, MkDocs config, tests, and workflow scaffolding

## Only Planned

- Endpoint-specific request and response coercion using generated models
- Live integration tests against a safe non-production environment
- First live trusted release after PyPI publisher registration

## Highest-Risk Remaining Surface

- The client is resource-complete at the transport layer, but endpoint methods
  still return decoded JSON until model coercion is proven endpoint by endpoint.

## Current Blockers

- Rate limits and live retry guidance are undocumented.
- Integration validation needs safe credentials and stable fixtures.
- Ambiguous generated schema fallbacks: 1
