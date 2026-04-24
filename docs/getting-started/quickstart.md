
# Quickstart

```python
from aryeo import AryeoClient

with AryeoClient.from_env() as client:
    appointments = client.appointments.list(params={"page": 1})
    order = client.orders.get("00000000-0000-4000-8000-000000000000")
```

The generated resource methods currently return decoded JSON values. Typed
request and response models are tracked as later work in the planning tree.
