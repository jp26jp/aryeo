
# Authentication

Most Aryeo API operations require a bearer token supplied in the
`Authorization` header.

## Environment Variables

- `ARYEO_API_TOKEN`: preferred bearer token used for protected operations
- `ARYEO_API_KEY`: accepted fallback for local `.env` files
- `ARYEO_BASE_URL`: optional override for the default base URL
- `ARYEO_TIMEOUT`: optional float timeout in seconds

## Client Setup

```python
from aryeo import AryeoClient

client = AryeoClient.from_env()
```

The default base URL is `https://api.aryeo.com/v1`.

For the underlying API contract details, see `docs/api/guides/authentication.md`.
