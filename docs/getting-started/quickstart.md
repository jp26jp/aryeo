# Quickstart

```python
from aryeo import AryeoClient

with AryeoClient.from_env() as client:
    client.orders.list(params={"page": 1, "per_page": 25})
```
