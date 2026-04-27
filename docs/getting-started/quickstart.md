
# Quickstart

```python
from aryeo import AryeoClient

with AryeoClient.from_env() as client:
    appointments = client.appointments.list(params={"page": 1})
    orders = client.orders.list(params={"page": 1, "per_page": 5})
```

The generated resource methods currently return decoded JSON values. Typed
request and response models are tracked as later work in the planning tree.

Runnable examples in `examples/` load a local `.env` file automatically and
avoid placeholder IDs by default. Set fixture IDs such as `ARYEO_LIVE_ORDER_ID`
when you want to exercise ID-specific reads.
