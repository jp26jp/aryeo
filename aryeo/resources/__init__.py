"""Compatibility exports for generated Aryeo resource clients.

Flat modules under `aryeo/` are the primary public surface. This package remains
as a compatibility layer for earlier scaffold imports.
"""

from __future__ import annotations

from aryeo.addresses import AddressesResource
from aryeo.appointments import AppointmentsResource
from aryeo.company_users import CompanyUsersResource
from aryeo.customer_users import CustomerUsersResource
from aryeo.discounts import DiscountsResource
from aryeo.listings import ListingsResource
from aryeo.notes import NotesResource
from aryeo.order_forms import OrderFormsResource
from aryeo.order_items import OrderItemsResource
from aryeo.orders import OrdersResource
from aryeo.payroll import PayrollResource
from aryeo.products import ProductsResource
from aryeo.scheduling import SchedulingResource
from aryeo.tags import TagsResource
from aryeo.tasks import TasksResource
from aryeo.videos import VideosResource

__all__ = [
    "AddressesResource",
    "AppointmentsResource",
    "CompanyUsersResource",
    "CustomerUsersResource",
    "DiscountsResource",
    "ListingsResource",
    "NotesResource",
    "OrderFormsResource",
    "OrderItemsResource",
    "OrdersResource",
    "PayrollResource",
    "ProductsResource",
    "SchedulingResource",
    "TagsResource",
    "TasksResource",
    "VideosResource",
]
