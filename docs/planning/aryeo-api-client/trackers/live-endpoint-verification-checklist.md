# Live Endpoint Verification Checklist

This checklist covers every generated Aryeo client endpoint in `tests/test_generated_surface.py`.
Rows are checked only after a live production API call completed successfully with the current local `.env` credentials. Tokens and response bodies are intentionally omitted.

Date: 2026-04-27

## Summary

- Total generated endpoints: 90
- Passed live: 29
- Failed live: 6
- Blocked or fixture-dependent: 55
- Offline wiring coverage: all endpoints remain covered by `tests/test_generated_surface.py`.

## Checklist

### Addresses

| Done | Status | HTTP | Endpoint | Client method | Auth | Live evidence or blocker |
| --- | --- | --- | --- | --- | --- | --- |
| [x] | Passed | `POST` | `/addresses` | `addresses.create` | Public | Live production call created a disposable address; no delete endpoint exists for cleanup. |
| [x] | Passed | `GET` | `/addresses/{address}` | `addresses.get` | Public | Live production call fetched a disposable address created for verification. |
| [x] | Passed | `PATCH` | `/addresses/{address}` | `addresses.update` | Public | Live production call updated a disposable address using the full patch payload. |

### Appointments

| Done | Status | HTTP | Endpoint | Client method | Auth | Live evidence or blocker |
| --- | --- | --- | --- | --- | --- | --- |
| [x] | Passed | `GET` | `/appointments` | `appointments.list` | Bearer | Live production paginated read returned 200 with an empty collection. |
| [ ] | Blocked | `GET` | `/appointments/{appointment_id}` | `appointments.get` | Bearer | Requires ARYEO_LIVE_APPOINTMENT_ID or appointment data; current appointment list was empty. |
| [ ] | Blocked | `PUT` | `/appointments/{appointment_id}` | `appointments.update` | Bearer | Requires disposable appointment fixture; production appointment mutation was not safe without one. |
| [ ] | Blocked | `PUT` | `/appointments/{appointment_id}/cancel` | `appointments.cancel` | Bearer | Requires disposable appointment fixture because this changes appointment state. |
| [ ] | Blocked | `PUT` | `/appointments/{appointment_id}/postpone` | `appointments.postpone` | Bearer | Requires disposable appointment fixture because this changes appointment state. |
| [ ] | Blocked | `PUT` | `/appointments/{appointment_id}/reschedule` | `appointments.reschedule` | Bearer | Requires disposable appointment fixture because this changes appointment schedule. |
| [ ] | Blocked | `PUT` | `/appointments/{appointment_id}/accept` | `appointments.accept` | Bearer | Requires disposable appointment fixture because this changes appointment state. |
| [ ] | Blocked | `PUT` | `/appointments/{appointment_id}/decline` | `appointments.decline` | Bearer | Requires disposable appointment fixture because this changes appointment state. |
| [ ] | Blocked | `PUT` | `/appointments/{appointment_id}/schedule` | `appointments.schedule` | Bearer | Requires disposable appointment fixture because this changes appointment state. |
| [ ] | Blocked | `GET` | `/appointments/{appointment_id}/availability` | `appointments.check_availability` | Bearer | Requires appointment ID plus assignee and duration fixture values. |
| [ ] | Blocked | `GET` | `/appointments/{appointment_id}/3dh-tour-link` | `appointments.get_3d_home_capture_link` | Bearer | Requires ARYEO_LIVE_APPOINTMENT_ID; current appointment list was empty. |
| [ ] | Blocked | `POST` | `/appointments/store` | `appointments.create` | Bearer | Requires disposable order fixture; no safe order cleanup endpoint exists. |

### Company Users

| Done | Status | HTTP | Endpoint | Client method | Auth | Live evidence or blocker |
| --- | --- | --- | --- | --- | --- | --- |
| [x] | Passed | `GET` | `/company-team-members` | `company_users.list_team_members` | Bearer | Live production paginated read returned 200. |
| [x] | Passed | `GET` | `/company-team-members/{company_team_member_id}` | `company_users.get_team_member` | Bearer | Live production read used the first company team member returned by list_team_members. |
| [x] | Passed | `GET` | `/company-team-members/{company_team_member_id}/events` | `company_users.list_team_member_events` | Bearer | Live production read used the first company team member and a bounded date window. |

### Customer Users

| Done | Status | HTTP | Endpoint | Client method | Auth | Live evidence or blocker |
| --- | --- | --- | --- | --- | --- | --- |
| [ ] | Failed | `GET` | `/customer-team-members/{customer_team_member_id}` | `customer_users.get_team_member` | Bearer | Live production call with a derived customer team member fixture returned HTTP 500. |
| [ ] | Failed | `GET` | `/customer-teams/{customer_team_id}/memberships` | `customer_users.list_team_memberships` | Bearer | Live production call with a derived customer team fixture returned HTTP 404. |
| [ ] | Blocked | `POST` | `/customer-teams/affiliate-memberships` | `customer_users.create_team_affiliate_membership` | Bearer | Requires safe affiliate/customer team fixture and may create a real membership. |
| [x] | Passed | `GET` | `/customer-users` | `customer_users.list` | Bearer | Live production paginated read returned 200. |
| [ ] | Blocked | `POST` | `/customer-users` | `customer_users.create` | Bearer | Creates a real customer user; no cleanup endpoint is exposed. |
| [ ] | Blocked | `POST` | `/customer-users/{user}/credit-transactions` | `customer_users.store_credit_transaction` | Bearer | Requires disposable customer user fixture and affects credit balance. |
| [x] | Passed | `GET` | `/customers` | `customer_users.list_customers` | Bearer | Live production paginated read returned 200. |
| [ ] | Blocked | `POST` | `/customers` | `customer_users.create_customers` | Bearer | Creates a real customer; no cleanup endpoint is exposed. |

### Discounts

| Done | Status | HTTP | Endpoint | Client method | Auth | Live evidence or blocker |
| --- | --- | --- | --- | --- | --- | --- |
| [x] | Passed | `GET` | `/coupons` | `discounts.list_coupons` | Bearer | Live production paginated read returned 200 with an empty collection. |
| [ ] | Blocked | `POST` | `/discounts` | `discounts.create` | Bearer | Requires disposable order/coupon fixture and mutates order pricing. |
| [ ] | Blocked | `DELETE` | `/discounts/{discount_id}` | `discounts.delete` | Bearer | Requires discount created specifically for verification. |
| [ ] | Blocked | `DELETE` | `/orders/{order}/discounts/{discount}` | `discounts.delete_order` | Bearer | Requires disposable order discount fixture and mutates order pricing. |
| [ ] | Blocked | `POST` | `/promotion-codes/redeem/{discounted_type}/{discounted}` | `discounts.redeem_promotion_code` | Public | Requires valid promotion code and disposable discounted target. |
| [ ] | Blocked | `POST` | `/refunds/{order_payment}` | `discounts.refund_order_payment` | Bearer | Requires disposable refundable payment; may move money. |

### Listings

| Done | Status | HTTP | Endpoint | Client method | Auth | Live evidence or blocker |
| --- | --- | --- | --- | --- | --- | --- |
| [x] | Passed | `GET` | `/listings` | `listings.list` | Bearer | Live production paginated read returned 200. |
| [ ] | Blocked | `POST` | `/listings` | `listings.create` | Bearer | Creates a real listing; no delete endpoint is exposed. |
| [x] | Passed | `GET` | `/listings/{listing_id}` | `listings.get` | Bearer | Live production read used the first listing returned by listings.list. |
| [ ] | Blocked | `PUT` | `/listings/{listing_id}` | `listings.update` | Bearer | Requires disposable listing fixture because this mutates listing data. |
| [ ] | Failed | `GET` | `/listings/{listing_id}/cubi-casa` | `listings.get_cubicasa_information` | Bearer | Live production call with first listing fixture returned HTTP 500. |
| [x] | Passed | `GET` | `/listings/{listing_id}/details/search` | `listings.search_details` | Bearer | Live production read used the first listing returned by listings.list. |
| [x] | Passed | `GET` | `/listings/{listing_id}/stats` | `listings.get_statistics` | Bearer | Live production read used the first listing returned by listings.list. |

### Notes

| Done | Status | HTTP | Endpoint | Client method | Auth | Live evidence or blocker |
| --- | --- | --- | --- | --- | --- | --- |
| [ ] | Blocked | `PUT` | `/orders/{order_id}/notes` | `notes.update_order` | Bearer | Requires disposable order fixture because this mutates order notes. |

### Order Forms

| Done | Status | HTTP | Endpoint | Client method | Auth | Live evidence or blocker |
| --- | --- | --- | --- | --- | --- | --- |
| [ ] | Blocked | `POST` | `/order-form-sessions` | `order_forms.create_session` | Bearer | Requires ARYEO_LIVE_ORDER_FORM_ID; order form list was empty. |
| [x] | Passed | `GET` | `/order-forms` | `order_forms.list` | Bearer | Live production read returned 200 with an empty collection. |

### Order Items

| Done | Status | HTTP | Endpoint | Client method | Auth | Live evidence or blocker |
| --- | --- | --- | --- | --- | --- | --- |
| [ ] | Blocked | `POST` | `/order-items` | `order_items.create` | Bearer | Requires disposable order fixture and mutates order items. |
| [ ] | Blocked | `GET` | `/order-items/{order_item_id}` | `order_items.get` | Bearer | Requires ARYEO_LIVE_ORDER_ITEM_ID; no order item list endpoint exists. |
| [ ] | Blocked | `PUT` | `/order-items/{order_item_id}` | `order_items.update` | Bearer | Requires order item created specifically for verification. |
| [ ] | Blocked | `DELETE` | `/order-items/{order_item_id}` | `order_items.delete` | Bearer | Requires order item created specifically for verification. |

### Orders

| Done | Status | HTTP | Endpoint | Client method | Auth | Live evidence or blocker |
| --- | --- | --- | --- | --- | --- | --- |
| [x] | Passed | `GET` | `/orders` | `orders.list` | Bearer | Live production paginated read returned 200 with an empty collection. |
| [ ] | Blocked | `POST` | `/orders` | `orders.create` | Bearer | Creates a real order; no delete endpoint is exposed. |
| [ ] | Blocked | `GET` | `/orders/{order_id}` | `orders.get` | Bearer | Requires ARYEO_LIVE_ORDER_ID; current order list was empty. |
| [ ] | Blocked | `POST` | `/orders/{order}/payments` | `orders.create_manual_payment` | Bearer | Requires disposable order fixture and records a payment. |
| [ ] | Blocked | `PUT` | `/orders/{order}/billing-address` | `orders.update_billing_address` | Bearer | Requires disposable order fixture because this mutates billing data. |
| [ ] | Blocked | `GET` | `/orders/{order}/payment-info` | `orders.get_payment_information` | Public | Requires ARYEO_LIVE_ORDER_ID; current order list was empty. |

### Payroll

| Done | Status | HTTP | Endpoint | Client method | Auth | Live evidence or blocker |
| --- | --- | --- | --- | --- | --- | --- |
| [ ] | Failed | `POST` | `/billing/setup-intents` | `payroll.create_billing_setup_intent` | Bearer | Live production call returned HTTP 500. |
| [ ] | Blocked | `GET` | `/order-items/{order_item_id}/pay-run-item-defaults` | `payroll.list_order_item_pay_run_item_defaults` | Bearer | Requires ARYEO_LIVE_ORDER_ITEM_ID. |

### Products

| Done | Status | HTTP | Endpoint | Client method | Auth | Live evidence or blocker |
| --- | --- | --- | --- | --- | --- | --- |
| [x] | Passed | `GET` | `/products` | `products.list` | Bearer | Live production paginated read returned 200 with an empty collection. |
| [x] | Passed | `GET` | `/product-categories` | `products.list_categories` | Bearer | Live production paginated read returned 200 with an empty collection. |
| [ ] | Blocked | `POST` | `/taxes` | `products.create_tax` | Bearer | Requires disposable order fixture and mutates taxes. |
| [ ] | Blocked | `DELETE` | `/taxes/{tax_id}` | `products.delete_tax` | Bearer | Requires tax created specifically for verification. |
| [x] | Passed | `GET` | `/territories` | `products.list_territories` | Bearer | Live production paginated read returned 200 with an empty collection. |

### Scheduling

| Done | Status | HTTP | Endpoint | Client method | Auth | Live evidence or blocker |
| --- | --- | --- | --- | --- | --- | --- |
| [ ] | Failed | `POST` | `/blocks` | `scheduling.create_block` | Bearer | Live production call with schema-required disposable block payload returned HTTP 422. |
| [ ] | Blocked | `DELETE` | `/blocks/{block_id}` | `scheduling.delete_block` | Bearer | Requires disposable block ID; create_block did not produce one. |
| [ ] | Blocked | `GET` | `/blocks/{block_id}` | `scheduling.get_block` | Bearer | Requires disposable block ID; create_block did not produce one. |
| [ ] | Blocked | `PUT` | `/blocks/{block_id}` | `scheduling.update_block` | Bearer | Requires disposable block ID; create_block did not produce one. |
| [x] | Passed | `GET` | `/regions` | `scheduling.list_regions` | Bearer | Live production read returned 200 using filter[type]=COUNTRY. |
| [ ] | Failed | `GET` | `/scheduling/assignment` | `scheduling.get_assignment` | Bearer | Live production call with bounded assignment parameters returned HTTP 500. |
| [x] | Passed | `GET` | `/scheduling/available-dates` | `scheduling.list_available_dates` | Bearer | Live production read returned 200 using timezone, timeframe, duration, and interval. |
| [x] | Passed | `GET` | `/scheduling/available-timeslots` | `scheduling.list_available_timeslots` | Bearer | Live production read returned 200 using timezone, date, duration, and interval. |
| [ ] | Blocked | `GET` | `/scheduling/item-groupings` | `scheduling.list_schedule_item_groupings` | Bearer | Requires item_ids or appointment fixture values. |

### Tags

| Done | Status | HTTP | Endpoint | Client method | Auth | Live evidence or blocker |
| --- | --- | --- | --- | --- | --- | --- |
| [ ] | Blocked | `POST` | `/customer-teams/{customer_team_id}/tags` | `tags.create_customer_team` | Bearer | Requires disposable customer team fixture and mutates tags. |
| [ ] | Blocked | `PUT` | `/customer-teams/{customer_team_id}/tags` | `tags.update_customer_team` | Bearer | Requires disposable customer team tag fixture and mutates tags. |
| [ ] | Blocked | `DELETE` | `/customer-teams/{customer_team_id}/tags/{tag_id}` | `tags.delete_customer_team` | Bearer | Requires customer team tag created specifically for verification. |
| [ ] | Blocked | `POST` | `/orders/{order_id}/tags` | `tags.create_for_order` | Bearer | Requires disposable order fixture and mutates tags. |
| [ ] | Blocked | `PUT` | `/orders/{order_id}/tags` | `tags.update_for_order` | Bearer | Requires disposable order tag fixture and mutates tags. |
| [ ] | Blocked | `DELETE` | `/orders/{order_id}/tags/{tag_id}` | `tags.delete_for_order` | Bearer | Requires order tag created specifically for verification. |
| [ ] | Blocked | `POST` | `/products/{product_id}/tags` | `tags.create` | Bearer | Requires disposable product fixture and mutates tags. |
| [ ] | Blocked | `PUT` | `/products/{product_id}/tags` | `tags.update_product` | Bearer | Requires disposable product tag fixture and mutates tags. |
| [ ] | Blocked | `PUT` | `/products/{product_id}/tags/{tag_id}` | `tags.update` | Bearer | Requires disposable product/tag fixture and mutates tags. |
| [ ] | Blocked | `DELETE` | `/products/{product_id}/tags/{tag_id}` | `tags.delete_product` | Bearer | Requires product tag created specifically for verification. |
| [ ] | Blocked | `POST` | `/tags` | `tags.create_tags` | Bearer | Creates a global tag with no delete endpoint exposed by this client. |
| [ ] | Blocked | `PUT` | `/tags/{tag_id}` | `tags.update_tags` | Bearer | Requires disposable global tag fixture; create has no cleanup endpoint. |

### Tasks

| Done | Status | HTTP | Endpoint | Client method | Auth | Live evidence or blocker |
| --- | --- | --- | --- | --- | --- | --- |
| [x] | Passed | `GET` | `/tasks` | `tasks.list` | Bearer | Live production read returned 200 with an empty collection before disposable task lifecycle. |
| [x] | Passed | `POST` | `/tasks` | `tasks.create` | Bearer | Live production call created a disposable task for verification. |
| [x] | Passed | `DELETE` | `/tasks/{task_id}` | `tasks.delete` | Bearer | Live production call deleted the disposable task created for verification. |
| [x] | Passed | `GET` | `/tasks/{task_id}` | `tasks.get` | Bearer | Live production read fetched the disposable task created for verification. |
| [x] | Passed | `PUT` | `/tasks/{task_id}` | `tasks.update` | Bearer | Live production call updated the disposable task created for verification. |
| [x] | Passed | `PUT` | `/tasks/{task_id}/complete` | `tasks.complete` | Bearer | Live production call completed the disposable task created for verification. |
| [x] | Passed | `PUT` | `/tasks/{task_id}/reinstate` | `tasks.reinstate` | Bearer | Live production call reinstated the disposable task created for verification. |

### Videos

| Done | Status | HTTP | Endpoint | Client method | Auth | Live evidence or blocker |
| --- | --- | --- | --- | --- | --- | --- |
| [ ] | Blocked | `GET` | `/videos/{video_id}` | `videos.get` | Bearer | Requires ARYEO_LIVE_VIDEO_ID; no video list endpoint exists. |
| [ ] | Blocked | `PUT` | `/videos/{video_id}` | `videos.update` | Bearer | Requires disposable video fixture because this mutates video metadata. |
| [ ] | Blocked | `DELETE` | `/videos/{video_id}` | `videos.delete` | Bearer | Requires video created specifically for verification. |

## Fixture Variables For Remaining Checks

- `ARYEO_LIVE_APPOINTMENT_ID`: appointment get, availability, 3D tour link, and appointment state mutations.
- `ARYEO_LIVE_ORDER_ID`: order get, payment info, billing address, notes, discounts, taxes, payments, order items, appointment create, and order tags.
- `ARYEO_LIVE_ORDER_ITEM_ID`: order item get/update/delete, payroll defaults, and scheduling item groupings.
- `ARYEO_LIVE_ORDER_FORM_ID`: order form session creation.
- `ARYEO_LIVE_PRODUCT_ID`: product tag create/update/delete checks.
- `ARYEO_LIVE_VIDEO_ID`: video get/update/delete checks.
- `ARYEO_LIVE_CUSTOMER_TEAM_ID` and `ARYEO_LIVE_CUSTOMER_TEAM_TAG_ID`: customer team tag checks.

## Cleanup Notes

- Disposable task lifecycle cleanup completed through `tasks.delete`.
- Disposable address checks created address records, but the current client exposes no address delete endpoint for cleanup.
- No production orders, payments, refunds, customers, products, videos, or appointment state changes were created or mutated without a disposable cleanup path.

## Final Validation

- `pytest --cov=aryeo --cov-report=term-missing`: 101 passed, 96% coverage.
- `mypy aryeo/ --strict --ignore-missing-imports`: passed.
- `mkdocs build --strict`: passed.
- `python3 tools/verify_live_integrations.py`: 10 passed, 0 failed, 6 skipped.
- Checklist consistency check: 90 endpoint rows matched the generated endpoint inventory.
