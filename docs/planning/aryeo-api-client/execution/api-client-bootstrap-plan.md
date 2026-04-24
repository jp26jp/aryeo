
# API Client Bootstrap Plan

## Goal

- Recreate a typed Python API client baseline from the available API docs.

## Current Focus

- Phase 2 follow-up work: move from low-level JSON payloads toward typed request
  and response models without losing contract coverage.

## Ordered Phases

### Phase 0 - Source Audit
- Inputs: docs/api/, docs/planning/.../foundation/
- Deliverables: Base contract, inventory, and contradictions are documented.
- Exit criteria: Complete
### Phase 1 - Foundation And Packaging
- Inputs: pyproject.toml, aryeo/, README.md
- Deliverables: Package metadata, core transport, and exceptions exist.
- Exit criteria: Complete
### Phase 2 - Endpoint Inventory And Models
- Inputs: aryeo/resources/, docs/reference/resources.md
- Deliverables: Generated resource methods cover the documented surface.
- Exit criteria: In Progress
### Phase 3 - Tests And Coverage
- Inputs: tests/
- Deliverables: Core behavior and generated request wiring are tested.
- Exit criteria: In Progress
### Phase 4 - Docs And Examples
- Inputs: docs/, mkdocs.yml, examples/
- Deliverables: The docs site explains install, auth, and generated surfaces.
- Exit criteria: In Progress
### Phase 5 - Workflows And Release
- Inputs: .github/workflows/, .github/dependabot.yml
- Deliverables: Baseline workflows are checked in and consistent with packaging.
- Exit criteria: In Progress
### Phase 6 - Parity Audit
- Inputs: docs/planning/.../trackers/, execution/
- Deliverables: Deferred gaps are explicit and prioritized.
- Exit criteria: Pending
