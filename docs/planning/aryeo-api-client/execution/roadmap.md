
# Roadmap

| Phase | Why it exists | Files or directories | Acceptance | Risk if skipped |
| --- | --- | --- | --- | --- |
| Phase 0 - Source Audit | Establish one honest API source of truth. | docs/api/, docs/planning/.../foundation/ | Base contract, inventory, and contradictions are documented. | Implementation can drift from the checked-in docs. |
| Phase 1 - Foundation And Packaging | Create the package identity and shared runtime primitives. | pyproject.toml, aryeo/, README.md | Package metadata, core transport, and exceptions exist. | Later endpoint work has no stable runtime contract. |
| Phase 2 - Endpoint Inventory And Models | Map all endpoints into flat resources and generated models. | aryeo/*.py, aryeo/models.py, aryeo/enums.py | Generated resources, models, and enums cover the spec. | Resource and model coverage becomes ad hoc. |
| Phase 3 - Tests And Coverage | Exercise core behavior and per-resource request construction. | tests/ | Core, model/export, and per-resource tests pass. | Transport regressions slip in unnoticed. |
| Phase 4 - Docs And Examples | Publish client-library docs and safe examples. | docs/, mkdocs.yml, examples/ | Docs use client-library navigation and strict builds pass. | Users cannot discover the client shape. |
| Phase 5 - Workflows And Release | Keep CI, release, docs, and security gates aligned. | .github/workflows/, .github/dependabot.yml | Release paths run the same core validation as CI. | Tags can publish lower-quality artifacts than PRs. |
| Phase 6 - Parity Audit | Compare implementation claims against code, tests, and docs. | docs/planning/.../trackers/, execution/ | Remaining gaps are explicit and prioritized. | The repo may look more complete than it is. |
