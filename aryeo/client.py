"""Top-level Aryeo client composed from resource-specific subclients."""

from __future__ import annotations

import os

import httpx

from aryeo.base_client import (
    DEFAULT_BASE_URL,
    DEFAULT_TIMEOUT,
    DEFAULT_USER_AGENT,
    BaseClient,
)
from aryeo.exceptions import AryeoConfigurationError
from aryeo.resources import (
    AddressesResource,
    AppointmentsResource,
    CompanyUsersResource,
    CustomerUsersResource,
    DiscountsResource,
    ListingsResource,
    NotesResource,
    OrderFormsResource,
    OrderItemsResource,
    OrdersResource,
    PayrollResource,
    ProductsResource,
    SchedulingResource,
    TagsResource,
    TasksResource,
    VideosResource,
)
from aryeo.types import RequestTimeout

RESOURCE_NAMES = (
    "addresses",
    "appointments",
    "company_users",
    "customer_users",
    "discounts",
    "listings",
    "notes",
    "order_forms",
    "order_items",
    "orders",
    "payroll",
    "products",
    "scheduling",
    "tags",
    "tasks",
    "videos",
)


class AryeoClient(BaseClient):
    """Sync Aryeo API client grouped by API tag."""

    addresses: AddressesResource
    appointments: AppointmentsResource
    company_users: CompanyUsersResource
    customer_users: CustomerUsersResource
    discounts: DiscountsResource
    listings: ListingsResource
    notes: NotesResource
    order_forms: OrderFormsResource
    order_items: OrderItemsResource
    orders: OrdersResource
    payroll: PayrollResource
    products: ProductsResource
    scheduling: SchedulingResource
    tags: TagsResource
    tasks: TasksResource
    videos: VideosResource

    def __init__(
        self,
        token: str | None = None,
        *,
        base_url: str = DEFAULT_BASE_URL,
        timeout: RequestTimeout = DEFAULT_TIMEOUT,
        user_agent: str = DEFAULT_USER_AGENT,
        http_client: httpx.Client | None = None,
    ) -> None:
        """Initialize the Aryeo client and its resource bindings.

        Args:
            token: Optional bearer token for protected operations.
            base_url: Base URL for the Aryeo API.
            timeout: Default request timeout.
            user_agent: User-Agent header sent on each request.
            http_client: Optional injected `httpx.Client`.
        """

        super().__init__(
            token,
            base_url=base_url,
            timeout=timeout,
            user_agent=user_agent,
            http_client=http_client,
        )
        self.addresses = AddressesResource(self)
        self.appointments = AppointmentsResource(self)
        self.company_users = CompanyUsersResource(self)
        self.customer_users = CustomerUsersResource(self)
        self.discounts = DiscountsResource(self)
        self.listings = ListingsResource(self)
        self.notes = NotesResource(self)
        self.order_forms = OrderFormsResource(self)
        self.order_items = OrderItemsResource(self)
        self.orders = OrdersResource(self)
        self.payroll = PayrollResource(self)
        self.products = ProductsResource(self)
        self.scheduling = SchedulingResource(self)
        self.tags = TagsResource(self)
        self.tasks = TasksResource(self)
        self.videos = VideosResource(self)

    @classmethod
    def from_env(
        cls,
        *,
        token_env_var: str = "ARYEO_API_TOKEN",
        base_url_env_var: str = "ARYEO_BASE_URL",
        timeout_env_var: str = "ARYEO_TIMEOUT",
    ) -> "AryeoClient":
        """Build a client from conventional environment variables.

        Args:
            token_env_var: Environment variable containing the bearer token.
            base_url_env_var: Environment variable overriding the base URL.
            timeout_env_var: Environment variable overriding the timeout.

        Returns:
            A configured `AryeoClient` instance.

        Raises:
            AryeoConfigurationError: If the timeout environment variable is invalid.
        """

        timeout_value = os.getenv(timeout_env_var)
        timeout: RequestTimeout = DEFAULT_TIMEOUT
        if timeout_value:
            try:
                timeout = float(timeout_value)
            except ValueError as exc:
                raise AryeoConfigurationError(
                    f"{timeout_env_var} must be a float if provided."
                ) from exc

        return cls(
            token=os.getenv(token_env_var),
            base_url=os.getenv(base_url_env_var, DEFAULT_BASE_URL),
            timeout=timeout,
        )


__all__ = ["AryeoClient", "RESOURCE_NAMES"]
