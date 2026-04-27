
# Execution Plan

## Already Scaffolded

- Core runtime modules for transport, exceptions, and resource bindings
- Generated resource modules for every documented API tag
- Planning docs and Cursor rules
- Examples, MkDocs config, tests, and workflow scaffolding

## Only Planned

- Typed request and response models for shared schemas
- Live integration tests against a safe non-production environment
- Richer pagination helpers and higher-level convenience methods
- First live trusted release after the matching PyPI publisher is registered

## Highest-Risk Remaining Surface

- The current client is resource-complete at the transport layer but not yet
  schema-complete at the model layer.

## Current Blockers

- Rate limits and live retry guidance are undocumented.
- Integration validation needs safe credentials and a non-production test target.
- Trusted Publishing still needs the matching PyPI publisher registration before
  the first live release.

## Current Work Queue

- Replace low-level JSON mappings with typed models where the docs are stable
- Expand tests around inline request bodies and public endpoints
- Add parity reporting that compares the generated surface to the OpenAPI spec
