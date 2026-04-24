
# Roadmap

| Phase | Why it exists | Files or directories | Acceptance | Risk if skipped |
| --- | --- | --- | --- | --- |
| Phase 0 - Source Audit | Establish one honest API source of truth. | docs/api/, docs/planning/.../foundation/ | Base contract, inventory, and contradictions are documented. | Implementation can drift from the checked-in docs. |
| Phase 1 - Foundation And Packaging | Create the package identity and shared runtime primitives. | pyproject.toml, aryeo/, README.md | Package metadata, core transport, and exceptions exist. | Later endpoint work has no stable runtime contract. |
| Phase 2 - Endpoint Inventory And Models | Map all endpoints into resource modules and honest model follow-up work. | aryeo/resources/, docs/reference/resources.md | Generated resource methods cover the documented surface. | Resource coverage becomes ad hoc and hard to audit. |
| Phase 3 - Tests And Coverage | Create the baseline unit and generated route tests. | tests/ | Core behavior and generated request wiring are tested. | Transport regressions slip in unnoticed. |
| Phase 4 - Docs And Examples | Create a truthful docs site and working examples. | docs/, mkdocs.yml, examples/ | The docs site explains install, auth, and generated surfaces. | Users cannot discover the scaffolded client shape. |
| Phase 5 - Workflows And Release | Scaffold CI, docs, release, security, and dependency automation. | .github/workflows/, .github/dependabot.yml | Baseline workflows are checked in and consistent with packaging. | The scaffold cannot be kept healthy over time. |
| Phase 6 - Parity Audit | Compare the scaffold against the intended full client baseline. | docs/planning/.../trackers/, execution/ | Deferred gaps are explicit and prioritized. | The repo may look more complete than it really is. |
