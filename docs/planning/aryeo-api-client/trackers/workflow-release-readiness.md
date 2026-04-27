
# Workflow Release Readiness

| Area | Status | Notes |
| --- | --- | --- |
| CI | Scaffolded | `ci.yml` runs quality, tests, docs, and build checks |
| Docs | Scaffolded | `docs.yml` builds MkDocs strictly |
| Security | Scaffolded | `security-audit.yml` runs `pip-audit` |
| Release | Scaffolded | `release.yml` uses PyPI Trusted Publishing with the `pypi` environment |
| Unified deployment | Scaffolded | Manual workflow can publish through Trusted Publishing when its workflow file is also registered on PyPI |
| Dependabot | Scaffolded | Weekly updates for pip and GitHub Actions |
| Live publication | Deferred | Requires a PyPI pending publisher before the first trusted release |
