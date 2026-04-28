# Live Integration Readiness

The live integration check is intentionally opt-in and read-only by default. It
loads local `.env` values, accepts either `ARYEO_API_TOKEN` or `ARYEO_API_KEY`,
and avoids printing credentials.

## Command

```bash
python tools/verify_live_integrations.py
```

Use `--strict` when skipped fixture checks should fail the run.

## Latest Local Run

Date: 2026-04-27

Result: 10 passed, 0 failed, 6 skipped.

Endpoint-level production verification is tracked in
`live-endpoint-verification-checklist.md`.

| Resource | Live Check | Status | Notes |
| --- | --- | --- | --- |
| Addresses | `GET /addresses/{address}` | Skipped | Requires `ARYEO_LIVE_ADDRESS_ID` |
| Appointments | `GET /appointments` | Passed | Read-only paginated smoke |
| Company Users | `GET /company-team-members` | Passed | Read-only paginated smoke |
| Customer Users | `GET /customer-users` | Passed | Read-only paginated smoke |
| Discounts | `GET /coupons` | Passed | Read-only paginated smoke |
| Listings | `GET /listings` | Passed | Read-only paginated smoke |
| Notes | `PUT /orders/{order_id}/notes` | Skipped | No read-only notes endpoint in current client |
| Order Forms | `GET /order-forms` | Passed | Read-only smoke |
| Order Items | `GET /order-items/{order_item_id}` | Skipped | Requires `ARYEO_LIVE_ORDER_ITEM_ID` |
| Orders | `GET /orders` | Passed | Read-only paginated smoke |
| Payroll | `GET /order-items/{order_item_id}/pay-run-item-defaults` | Skipped | Requires `ARYEO_LIVE_ORDER_ITEM_ID` |
| Products | `GET /products` | Passed | Read-only paginated smoke |
| Scheduling | `GET /regions` | Passed | Uses `filter[type]=COUNTRY` |
| Tags | `POST /tags` | Skipped | No read-only tags endpoint in current client |
| Tasks | `GET /tasks` | Passed | Read-only smoke |
| Videos | `GET /videos/{video_id}` | Skipped | Requires `ARYEO_LIVE_VIDEO_ID` |

## Fixture Variables

- `ARYEO_LIVE_ADDRESS_ID`: enables the address read check.
- `ARYEO_LIVE_ORDER_ITEM_ID`: enables order item and payroll read checks.
- `ARYEO_LIVE_VIDEO_ID`: enables the video read check.
- `ARYEO_LIVE_ORDER_ID`: enables the optional payment-info branch in
  `examples/list_orders.py`.
