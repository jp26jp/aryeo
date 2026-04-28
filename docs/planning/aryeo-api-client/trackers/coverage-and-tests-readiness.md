# Coverage And Tests Readiness

| Area | Status | Notes |
| --- | --- | --- |
| Core transport tests | Present | `tests/test_base_client.py` |
| Client wiring tests | Present | `tests/test_client.py` |
| Exception tests | Present | `tests/test_exceptions.py` |
| Model/export tests | Present | `tests/test_models.py` |
| Per-resource tests | Present | 16 generated `tests/test_<resource>.py` files |
| Live integration tests | Opt-in | Safe checks remain outside default CI |
