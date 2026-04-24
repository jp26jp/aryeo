
# Contributing

## Bootstrap

```bash
python tools/bootstrap_client_repo.py
```

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

## Planning

Treat `docs/planning/aryeo-api-client/` as the checked-in implementation
ledger for the scaffold and its follow-on phases.
