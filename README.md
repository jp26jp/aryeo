
# Aryeo Python Client

This repository bootstraps a typed Python client around the checked-in Aryeo
OpenAPI wrapper in `docs/api/aryeo.json`.

The current baseline includes:

- a sync `httpx` transport layer with auth, timeout, and error handling
- generated resource clients for 16 API tags and
  90 operations
- planning docs under `docs/planning/aryeo-api-client/`
- repo-local Cursor rules under `.cursor/rules/`
- MkDocs configuration, examples, tests, and GitHub workflow scaffolding

## Current Scope

This scaffold intentionally exposes low-level JSON request and response shapes.
Schema-perfect models, richer pagination helpers, and live parity checks are
deferred to later phases in the planning tree.

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
    listing = client.listings.get("00000000-0000-4000-8000-000000000000")
```

Set `ARYEO_API_TOKEN` before using protected operations. Public operations can
be called without a token.

## Regenerate

The generated resource surface can be refreshed from the checked-in spec with:

```bash
python tools/bootstrap_client_repo.py
```

## Docs

- API contract docs: `docs/api/`
- Planning root: `docs/planning/aryeo-api-client/`
- Package reference: `docs/reference/`

## Validation

```bash
black --check --diff --line-length=88 .
isort --check-only --diff --profile=black --line-length=88 .
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
flake8 . --count --exit-zero --max-complexity=10 --max-line-length=88 --statistics
mypy aryeo/ --strict --ignore-missing-imports
pytest --cov=aryeo --cov-report=xml --cov-report=term-missing
mkdocs build --strict
python -m build
python -m twine check dist/*
```

## Resource Groups

| Tag | Module | Operations |
| --- | --- | --- |
| Addresses | `aryeo/resources/addresses.py` | 3 |
| Appointments | `aryeo/resources/appointments.py` | 12 |
| Company Users | `aryeo/resources/company_users.py` | 3 |
| Customer Users | `aryeo/resources/customer_users.py` | 8 |
| Discounts | `aryeo/resources/discounts.py` | 6 |
| Listings | `aryeo/resources/listings.py` | 7 |
| Notes | `aryeo/resources/notes.py` | 1 |
| Order Forms | `aryeo/resources/order_forms.py` | 2 |
| Order Items | `aryeo/resources/order_items.py` | 4 |
| Orders | `aryeo/resources/orders.py` | 6 |
| Payroll | `aryeo/resources/payroll.py` | 2 |
| Products | `aryeo/resources/products.py` | 5 |
| Scheduling | `aryeo/resources/scheduling.py` | 9 |
| Tags | `aryeo/resources/tags.py` | 12 |
| Tasks | `aryeo/resources/tasks.py` | 7 |
| Videos | `aryeo/resources/videos.py` | 3 |
