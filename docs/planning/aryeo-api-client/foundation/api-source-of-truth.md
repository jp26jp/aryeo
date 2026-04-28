
# API Source Of Truth

## Source Priority

1. checked-in `docs/api/`
2. checked-in OpenAPI wrapper in `docs/api/aryeo.json`

## Inputs Used

| Source | Path | Status | Why it matters |
| --- | --- | --- | --- |
| Generated API overview | `docs/api/README.md` | Used | Summarizes counts and generated API contract docs. |
| OpenAPI wrapper | `docs/api/aryeo.json` | Used | Canonical machine-readable endpoint and schema contract. |
| Generated API guides | `docs/api/guides/` | Used | Documents auth, errors, and pagination. |

## Base Contract

| Area | Current answer | Canonical source |
| --- | --- | --- |
| Base URL | `https://api.aryeo.com/v1` | `docs/api/aryeo.json` |
| Authentication | Bearer token on 85 operations; 5 are public | `docs/api/guides/authentication.md` |
| Versioning | Spec version `1.0.0` | `docs/api/README.md` |
| Pagination | `page` and `per_page` query patterns | `docs/api/` |
| Errors | Shared 4xx and 5xx JSON payloads | `docs/api/` |
| Rate limits | Not documented | `docs/api/aryeo.json` |

## Resource Inventory

| Resource group | Coverage status | Notes |
| --- | --- | --- |
| Addresses | Flat resource generated | 3 operations in `aryeo/addresses.py` |
| Appointments | Flat resource generated | 12 operations in `aryeo/appointments.py` |
| Company Users | Flat resource generated | 3 operations in `aryeo/company_users.py` |
| Customer Users | Flat resource generated | 8 operations in `aryeo/customer_users.py` |
| Discounts | Flat resource generated | 6 operations in `aryeo/discounts.py` |
| Listings | Flat resource generated | 7 operations in `aryeo/listings.py` |
| Notes | Flat resource generated | 1 operations in `aryeo/notes.py` |
| Order Forms | Flat resource generated | 2 operations in `aryeo/order_forms.py` |
| Order Items | Flat resource generated | 4 operations in `aryeo/order_items.py` |
| Orders | Flat resource generated | 6 operations in `aryeo/orders.py` |
| Payroll | Flat resource generated | 2 operations in `aryeo/payroll.py` |
| Products | Flat resource generated | 5 operations in `aryeo/products.py` |
| Scheduling | Flat resource generated | 9 operations in `aryeo/scheduling.py` |
| Tags | Flat resource generated | 12 operations in `aryeo/tags.py` |
| Tasks | Flat resource generated | 7 operations in `aryeo/tasks.py` |
| Videos | Flat resource generated | 3 operations in `aryeo/videos.py` |

## Model And Enum Inventory

- Generated models: 248
- Generated enums: 138
- Inline enum paths found: 138

## Contradictions And Gaps

- Rate limits and retry budgets are not documented in checked-in sources.
- No webhook or async callback contract is present.
- Resource methods remain JSON-based until endpoint-specific model coercion can be proven with tests and examples.
- Ambiguous schemas retained JSON-compatible fallback typing: `FeatureFlags`.
