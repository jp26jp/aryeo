
# API Source Of Truth

## Source Priority

1. checked-in `docs/api/`
2. checked-in OpenAPI wrapper in `docs/api/aryeo.json`

## Inputs Used

| Source | Path | Status | Why it matters |
| --- | --- | --- | --- |
| Generated API overview | `docs/api/README.md` | Used | Summarizes the wrapper, counts, and server. |
| OpenAPI wrapper | `docs/api/aryeo.json` | Used | Canonical machine-readable contract. |
| Auth guide | `docs/api/guides/authentication.md` | Used | Confirms bearer-token behavior and public ops. |
| Errors guide | `docs/api/guides/errors.md` | Used | Captures shared 4xx and 5xx shapes. |
| Pagination guide | `docs/api/guides/pagination.md` | Used | Confirms shared page/per_page semantics. |
| Reference index | `docs/api/reference/README.md` | Used | Confirms tag groupings and counts. |

## Base Contract

| Area | Current answer | Canonical source |
| --- | --- | --- |
| Base URL | `https://api.aryeo.com/v1` | `docs/api/aryeo.json` |
| Authentication | Bearer token on 85 operations; 5 are public | `docs/api/guides/authentication.md` |
| Versioning | Spec version `1.0.0` | `docs/api/README.md` |
| Pagination | `page` and `per_page` plus common sort/include support | `docs/api/guides/pagination.md` |
| Errors | Shared 403/404/409/422/500 schema family | `docs/api/guides/errors.md` |
| Rate limits | Not documented in checked-in sources | `docs/api/aryeo.json` |

## Resource Inventory

| Resource group | Coverage status | Notes |
| --- | --- | --- |
| Addresses | Low-level surface scaffolded | 3 operations in `aryeo/resources/addresses.py` |
| Appointments | Low-level surface scaffolded | 12 operations in `aryeo/resources/appointments.py` |
| Company Users | Low-level surface scaffolded | 3 operations in `aryeo/resources/company_users.py` |
| Customer Users | Low-level surface scaffolded | 8 operations in `aryeo/resources/customer_users.py` |
| Discounts | Low-level surface scaffolded | 6 operations in `aryeo/resources/discounts.py` |
| Listings | Low-level surface scaffolded | 7 operations in `aryeo/resources/listings.py` |
| Notes | Low-level surface scaffolded | 1 operations in `aryeo/resources/notes.py` |
| Order Forms | Low-level surface scaffolded | 2 operations in `aryeo/resources/order_forms.py` |
| Order Items | Low-level surface scaffolded | 4 operations in `aryeo/resources/order_items.py` |
| Orders | Low-level surface scaffolded | 6 operations in `aryeo/resources/orders.py` |
| Payroll | Low-level surface scaffolded | 2 operations in `aryeo/resources/payroll.py` |
| Products | Low-level surface scaffolded | 5 operations in `aryeo/resources/products.py` |
| Scheduling | Low-level surface scaffolded | 9 operations in `aryeo/resources/scheduling.py` |
| Tags | Low-level surface scaffolded | 12 operations in `aryeo/resources/tags.py` |
| Tasks | Low-level surface scaffolded | 7 operations in `aryeo/resources/tasks.py` |
| Videos | Low-level surface scaffolded | 3 operations in `aryeo/resources/videos.py` |

## Contradictions And Gaps

- The checked-in docs do not describe rate limits or retry budgets.
- The spec applies auth per operation instead of globally, so the client must preserve public exceptions.
- Path parameter naming is inconsistent across endpoints, for example `order_id` versus `order`.
- Two request bodies are inline objects instead of named component schemas.
- Enums are mostly inline within properties and parameters rather than shared component enum schemas.
- No webhook or async callback contract is present in the checked-in sources.

## Follow-Up Before Implementation

- Decide how to model inline request bodies in a typed way during the next phase.
- Confirm whether publication should use the distribution name `aryeo` or a namespaced variant.
- Add live contract tests once valid credentials and a non-production environment are available.
