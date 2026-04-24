
# Workflow Release Readiness

| Area | Status | Notes |
| --- | --- | --- |
| CI | Scaffolded | `ci.yml` runs quality, tests, docs, and build checks |
| Docs | Scaffolded | `docs.yml` builds MkDocs strictly |
| Security | Scaffolded | `security-audit.yml` runs `pip-audit` |
| Release | Scaffolded | `release.yml` expects `PYPI_API_TOKEN` secret |
| Unified deployment | Scaffolded | Manual workflow validates and can publish |
| Dependabot | Scaffolded | Weekly updates for pip and GitHub Actions |
| Live publication | Deferred | Requires GitHub repo wiring and secrets |
