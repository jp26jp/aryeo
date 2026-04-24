
# Source Of Truth Matrix

| Topic | Canonical source | Secondary source | Confidence | Follow-up |
| --- | --- | --- | --- | --- |
| Authentication | `docs/api/guides/authentication.md` | `docs/api/aryeo.json` | High | None |
| Base URL and versioning | `docs/api/README.md` | `docs/api/aryeo.json` | High | None |
| Resource grouping | `docs/api/reference/README.md` | `docs/api/README.md` | High | None |
| Error contract | `docs/api/guides/errors.md` | `docs/api/aryeo.json` | High | None |
| Pagination | `docs/api/guides/pagination.md` | `docs/api/reference/*.md` | High | None |
| Request/response schemas | `docs/api/aryeo.json` | `docs/api/reference/*.md` | High | Typed models still needed |
| Enums and shared types | `docs/api/aryeo.json` | `docs/api/reference/*.md` | Medium | 138 inline enum paths need modeling strategy |
| Uploads and downloads | `docs/api/aryeo.json` | `docs/api/reference/*.md` | High | Only JSON content types are present today |
| Rate limits | `docs/api/aryeo.json` | None | Low | No limit guidance is documented |
| Webhooks | `docs/api/aryeo.json` | None | Low | No webhook section is present |
