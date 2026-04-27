
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

## PyPI Trusted Publishing

GitHub Actions publishes to PyPI through Trusted Publishing with the `pypi`
environment and `id-token: write` permissions, so no long-lived PyPI API token
is required in GitHub.

Before the first live publish, add a PyPI pending publisher for this repository
under `https://pypi.org/manage/account/publishing/`.

- Register `release.yml` if you want tag-based publishing from
  `.github/workflows/release.yml`.
- Register `unified-deployment.yml` as well if you want the manual publish path
  in `.github/workflows/unified-deployment.yml` to work.
- Use the optional environment name `pypi` to match the GitHub workflow jobs.

## Planning

Treat `docs/planning/aryeo-api-client/` as the checked-in implementation
ledger for the scaffold and its follow-on phases.
