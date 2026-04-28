
# Aryeo Python Client

Aryeo is a typed Python client for the Aryeo API. The client is generated from
the checked-in OpenAPI wrapper at `docs/api/aryeo.json` and uses a
client-library repository shape: flat resource modules, explicit exports,
MkDocs documentation, per-resource tests, and release-quality checks.

## Current Scope

- Sync `httpx` transport in `aryeo/base_client.py`
- Flat resource modules for 16 API tags and 90
  operations
- Generated `aryeo/models.py` and `aryeo/enums.py` from the checked-in spec
- Compatibility exports under `aryeo/resources/`
- Python `>=3.11` by design

Resource methods intentionally return decoded JSON until each endpoint can be
confidently mapped to stable request and response models.

## Install

```bash
python -m pip install -e ".[dev]"
python -m pip install -r docs/requirements.txt
```

## Quickstart

```python
from aryeo import AryeoClient

with AryeoClient.from_env() as client:
    orders = client.orders.list(params={"page": 1, "per_page": 25})
    listings = client.listings.list(params={"page": 1, "per_page": 25})
```

Set `ARYEO_API_TOKEN` before using protected operations. `ARYEO_API_KEY` is
also accepted as a fallback for local `.env` files. Public operations can be
called without a token.

## Live Integration Checks

Live checks are opt-in and avoid mutating API data by default:

```bash
python tools/verify_live_integrations.py
```

Some resource groups require stable fixture IDs before they can be checked live.
Set `ARYEO_LIVE_ADDRESS_ID`, `ARYEO_LIVE_ORDER_ITEM_ID`,
`ARYEO_LIVE_ORDER_ID`, or `ARYEO_LIVE_VIDEO_ID` for fixture-based reads.

## Regenerate

```bash
python tools/bootstrap_client_repo.py --force-curated
python docs/api/generate_reference.py
```

## Validation

```bash
black --check --diff --line-length=88 .
isort --check-only --diff --profile=black --line-length=88 .
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
flake8 . --count --exit-zero --max-complexity=10 --max-line-length=88 --statistics
mypy aryeo/ --strict --ignore-missing-imports
pytest --cov=aryeo --cov-report=term-missing
mkdocs build --strict
python -m build
python -m twine check dist/*
```

## Resource Groups

| Tag | Module | Operations |
| --- | --- | --- |
| Addresses | `aryeo/addresses.py` | 3 |
| Appointments | `aryeo/appointments.py` | 12 |
| Company Users | `aryeo/company_users.py` | 3 |
| Customer Users | `aryeo/customer_users.py` | 8 |
| Discounts | `aryeo/discounts.py` | 6 |
| Listings | `aryeo/listings.py` | 7 |
| Notes | `aryeo/notes.py` | 1 |
| Order Forms | `aryeo/order_forms.py` | 2 |
| Order Items | `aryeo/order_items.py` | 4 |
| Orders | `aryeo/orders.py` | 6 |
| Payroll | `aryeo/payroll.py` | 2 |
| Products | `aryeo/products.py` | 5 |
| Scheduling | `aryeo/scheduling.py` | 9 |
| Tags | `aryeo/tags.py` | 12 |
| Tasks | `aryeo/tasks.py` | 7 |
| Videos | `aryeo/videos.py` | 3 |
