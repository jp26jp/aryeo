
# Aryeo Python Client

This project turns the checked-in Aryeo OpenAPI wrapper into a usable Python
client baseline.

## What Exists

- 90 low-level resource methods generated from
  `docs/api/aryeo.json`
- shared auth, timeout, and error handling in `aryeo/base_client.py`
- package reference pages backed by `mkdocstrings`
- planning docs under `docs/planning/aryeo-api-client/`

## Where To Start

- Read `docs/api/README.md` for the API contract summary.
- Read `docs/reference/client.md` for the Python client surface.
- Read `docs/planning/aryeo-api-client/execution/api-client-bootstrap-plan.md`
  for the active implementation roadmap.
