
# Python Reference

The runtime surface is intentionally split into three layers:

- `aryeo.client.AryeoClient` wires resource clients together.
- `aryeo.base_client.BaseClient` owns transport, auth, and JSON behavior.
- `aryeo.resources.*` exposes low-level endpoint methods grouped by API tag.
