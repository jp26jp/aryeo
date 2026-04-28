
# API Client Bootstrap Plan

## Goal

- Maintain a typed Python client baseline from the checked-in Aryeo API docs.

## Current Focus

- ReZEN-style package structure, generated models/enums, per-resource tests, and
  release hygiene.

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
- Inputs: aryeo/*.py, aryeo/models.py, aryeo/enums.py
- Deliverables: Generated resources, models, and enums cover the spec.
- Exit criteria: In Progress
### Phase 3 - Tests And Coverage
- Inputs: tests/
- Deliverables: Core, model/export, and per-resource tests pass.
- Exit criteria: In Progress
### Phase 4 - Docs And Examples
- Inputs: docs/, mkdocs.yml, examples/
- Deliverables: Docs use ReZEN-style navigation and strict builds pass.
- Exit criteria: In Progress
### Phase 5 - Workflows And Release
- Inputs: .github/workflows/, .github/dependabot.yml
- Deliverables: Release paths run the same core validation as CI.
- Exit criteria: In Progress
### Phase 6 - Parity Audit
- Inputs: docs/planning/.../trackers/, execution/
- Deliverables: Remaining gaps are explicit and prioritized.
- Exit criteria: Pending
