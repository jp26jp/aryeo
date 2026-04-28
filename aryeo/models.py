"""Generated Pydantic models for the Aryeo API.

Fields are derived from docs/api/aryeo.json. Resource methods stay
JSON-based when request or response coercion cannot be inferred safely.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, RootModel

from aryeo.enums import (
    ActivityNameEnum,
    ActivityPostPayloadNameEnum,
    ActivityPostPayloadResourceTypeEnum,
    ActivityPostPayloadSourceEnum,
    ActivitySourceEnum,
    AddressPatchPayloadExternalTypeEnum,
    AddressPredictionResultExternalTypeEnum,
    AddressSearchResultExternalTypeEnum,
    AppointmentAttendanceObjectEnum,
    AppointmentPreferenceTypeEnum,
    AppointmentPreferredStartAtTimeOfDayEnum,
    AppointmentStatusEnum,
    AuthActivationStageResourceStatusEnum,
    BookingLimitsAutomatedUserAssignmentStrategyEnum,
    BookingLimitsAvailabilityStyleEnum,
    BookingLimitsObjectEnum,
    CalendarBlockTypeEnum,
    CalendarEventTypeEnum,
    CompanyTeamMemberObjectEnum,
    CompanyTeamMemberPermissionNameEnum,
    CompanyTeamMemberPermissionObjectEnum,
    CompanyTeamMemberResourceStrategyTypeEnum,
    CompanyTeamMemberRoleEnum,
    CompanyTeamMemberStatusEnum,
    CreditTransactionTypeEnum,
    CustomerGroupObjectEnum,
    CustomerGroupStatusEnum,
    CustomerTeamMembershipObjectEnum,
    CustomerTeamMembershipRoleEnum,
    CustomerTeamMembershipStatusEnum,
    CustomerUserPostPayloadRoleEnum,
    CustomerUserStatusEnum,
    CustomerUserVerificationStatusEnum,
    DeleteUserPostPayloadClientEnum,
    DiscountAmountObjectEnum,
    DiscountObjectEnum,
    EsoftOrderLineObjectEnum,
    EsoftOrderLineStatusEnum,
    FeatureFlagsEnum,
    FeeObjectEnum,
    FeeTypeEnum,
    FileDisplayTypeEnum,
    FloorPlanObjectEnum,
    GroupAutomatedUserAssignmentStrategyEnum,
    GroupAvailabilityStyleEnum,
    GroupCurrencyEnum,
    GroupCustomerAutomatedUserAssignmentStrategyEnum,
    GroupCustomerAvailabilityStyleEnum,
    GroupCustomerCurrencyEnum,
    GroupCustomerTypeEnum,
    GroupCustomerVerificationStatusEnum,
    GroupObjectEnum,
    GroupTypeEnum,
    ImpersonatePostPayloadClientEnum,
    InteractiveContentContentTypeEnum,
    InteractiveContentDisplayTypeEnum,
    ListingDeliveryStatusEnum,
    ListingMarketingContentObjectEnum,
    ListingMarketingContentStatusEnum,
    ListingMarketingContentSubTypeEnum,
    ListingObjectEnum,
    ListingPutPayloadPropertyTypeEnum,
    ListingStandardStatusEnum,
    ListingStatusEnum,
    ListingSubTypeEnum,
    ListingTypeEnum,
    LoginPostPayloadClientEnum,
    LoginViaTokenPostPayloadClientEnum,
    MarketingMaterialObjectEnum,
    MarketingMaterialTemplateObjectEnum,
    MediaSearchResourceDataObjectEnum,
    NotificationPreference2NotificationTypeEnum,
    NotificationPreference2ObjectEnum,
    NotificationPreferenceChannelsEnum,
    NotificationPreferenceNotificationTypeEnum,
    NotificationPreferenceObjectEnum,
    OrderCurrencyEnum,
    OrderFormAutomatedUserAssignmentStrategyEnum,
    OrderFormAvailabilityStyleEnum,
    OrderFormObjectEnum,
    OrderFormSessionObjectEnum,
    OrderFormTypeEnum,
    OrderFulfillmentStatusEnum,
    OrderItemObjectEnum,
    OrderItemPurchasableTypeEnum,
    OrderObjectEnum,
    OrderOrderStatusEnum,
    OrderPaymentObjectEnum,
    OrderPaymentStatusEnum,
    OrderPaymentTypeEnum,
    OrderPostPayloadFulfillmentStatusEnum,
    OrderRefundObjectEnum,
    OrderRefundPostPayloadReasonEnum,
    OrderRefundReasonEnum,
    OrderSchedulingAssignmentStrategyEnum,
    OrderStatusEnum,
    PaymentCollectionSourceEnum,
    PaymentGatewayObjectEnum,
    PaymentInfoObjectEnum,
    PaymentObjectEnum,
    PaymentTypeEnum,
    PayRunItemAmountOverrideAmountTypeEnum,
    PortalAppConfigObjectEnum,
    PortalAppConfigPrimaryStatusEnum,
    PortalAppConfigPutPayloadPrimaryStatusEnum,
    PortalAppRevisionObjectEnum,
    PortalCustomerRegisterPostPayloadClientEnum,
    PortalCustomerVerifyPostPayloadClientEnum,
    ProductCategoryObjectEnum,
    ProductObjectEnum,
    ProductTypeEnum,
    ProductVariantObjectEnum,
    RegionTypeEnum,
    ReviewPostPayloadSourceTypeEnum,
    ReviewSourceTypeEnum,
    SavedViewFilterObjectEnum,
    SavedViewFilterTypeEnum,
    SavedViewObjectEnum,
    SavedViewOwnerTypeEnum,
    SavedViewPatchPayloadFiltersTypeEnum,
    SavedViewPatchPayloadOwnerTypeEnum,
    SavedViewPatchPayloadScopeEnum,
    SavedViewPostPayloadFiltersTypeEnum,
    SavedViewPostPayloadOwnerTypeEnum,
    SavedViewPostPayloadScopeEnum,
    SavedViewScopeEnum,
    SavedViewViewAccessEnum,
    TagObjectEnum,
    TagOnlyPostPayloadTypeEnum,
    TagsPostPayloadTagTypeEnum,
    TagTypeEnum,
    TaskTemplateDefaultPayRunItemAmountTypeEnum,
    TerritoryObjectEnum,
    UserStatusEnum,
    UserVerificationStatusEnum,
    VideoDisplayTypeEnum,
    VideoObjectEnum,
    VideoSourceTypeEnum,
)
from aryeo.types import JSONValue


class Activity(BaseModel):
    """Aryeo API schema for `#/components/schemas/Activity`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    acting_group: Group | None = Field(
        default=None,
        alias="acting_group",
    )

    acting_user: User | None = Field(
        default=None,
        alias="acting_user",
    )

    description: str = Field(
        default=...,
        alias="description",
    )

    group: Group | None = Field(
        default=None,
        alias="group",
    )

    html_payload: dict[str, JSONValue] | None = Field(
        default=None,
        alias="html_payload",
    )

    id: str = Field(
        default=...,
        alias="id",
    )

    name: ActivityNameEnum = Field(
        default=...,
        alias="name",
    )

    object: str | None = Field(
        default=None,
        alias="object",
    )

    occurred_at: str = Field(
        default=...,
        alias="occurred_at",
    )

    payload: dict[str, JSONValue] | None = Field(
        default=None,
        alias="payload",
    )

    resource: dict[str, JSONValue] | None = Field(
        default=None,
        alias="resource",
    )

    source: ActivitySourceEnum = Field(
        default=...,
        alias="source",
    )

    system_activity: bool | None = Field(
        default=None,
        alias="system_activity",
    )

    target_label: str | None = Field(
        default=None,
        alias="target_label",
    )

    target_url: str | None = Field(
        default=None,
        alias="target_url",
    )

    title: str | None = Field(
        default=None,
        alias="title",
    )


class ActivityCollection(BaseModel):
    """Aryeo API schema for `#/components/schemas/ActivityCollection`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: list[Activity] | None = Field(
        default=None,
        alias="data",
    )

    links: PaginationLinks | None = Field(
        default=None,
        alias="links",
    )

    meta: PaginationMeta | None = Field(
        default=None,
        alias="meta",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class ActivityPostPayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/ActivityPostPayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    description: str = Field(
        default=...,
        alias="description",
    )

    group_id: str = Field(
        default=...,
        alias="group_id",
    )

    name: ActivityPostPayloadNameEnum = Field(
        default=...,
        alias="name",
    )

    payload: dict[str, JSONValue] | None = Field(
        default=None,
        alias="payload",
    )

    resource_id: str | None = Field(
        default=None,
        alias="resource_id",
    )

    resource_type: ActivityPostPayloadResourceTypeEnum | None = Field(
        default=None,
        alias="resource_type",
    )

    source: ActivityPostPayloadSourceEnum = Field(
        default=...,
        alias="source",
    )

    user_id: str = Field(
        default=...,
        alias="user_id",
    )


class ActivityResource(BaseModel):
    """Aryeo API schema for `#/components/schemas/ActivityResource`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: Activity | None = Field(
        default=None,
        alias="data",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class Address(BaseModel):
    """Aryeo API schema for `#/components/schemas/Address`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    city: str | None = Field(
        default=None,
        alias="city",
    )

    city_region: str | None = Field(
        default=None,
        alias="city_region",
    )

    country: str | None = Field(
        default=None,
        alias="country",
    )

    country_region: str | None = Field(
        default=None,
        alias="country_region",
    )

    county_or_parish: str | None = Field(
        default=None,
        alias="county_or_parish",
    )

    id: str = Field(
        default=...,
        alias="id",
    )

    is_map_dirty: bool | None = Field(
        default=None,
        alias="is_map_dirty",
    )

    latitude: float | None = Field(
        default=None,
        alias="latitude",
    )

    longitude: float | None = Field(
        default=None,
        alias="longitude",
    )

    postal_code: str | None = Field(
        default=None,
        alias="postal_code",
    )

    state_or_province: str | None = Field(
        default=None,
        alias="state_or_province",
    )

    state_or_province_region: str | None = Field(
        default=None,
        alias="state_or_province_region",
    )

    street_name: str | None = Field(
        default=None,
        alias="street_name",
    )

    street_number: str | None = Field(
        default=None,
        alias="street_number",
    )

    timezone: str | None = Field(
        default=None,
        alias="timezone",
    )

    unit_number: str | None = Field(
        default=None,
        alias="unit_number",
    )

    unparsed_address: str | None = Field(
        default=None,
        alias="unparsed_address",
    )

    unparsed_address_part_one: str | None = Field(
        default=None,
        alias="unparsed_address_part_one",
    )

    unparsed_address_part_two: str | None = Field(
        default=None,
        alias="unparsed_address_part_two",
    )


class AddressPatchPayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/AddressPatchPayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    city: str | None = Field(
        default=None,
        alias="city",
    )

    city_region: str | None = Field(
        default=None,
        alias="city_region",
    )

    country: str | None = Field(
        default=None,
        alias="country",
    )

    country_region: str | None = Field(
        default=None,
        alias="country_region",
    )

    county_or_parish: str | None = Field(
        default=None,
        alias="county_or_parish",
    )

    external_data: list[dict[str, JSONValue]] | None = Field(
        default=None,
        alias="external_data",
    )

    external_id: str | None = Field(
        default=None,
        alias="external_id",
    )

    external_type: AddressPatchPayloadExternalTypeEnum | None = Field(
        default=None,
        alias="external_type",
    )

    external_url: str | None = Field(
        default=None,
        alias="external_url",
    )

    is_map_dirty: bool | None = Field(
        default=None,
        alias="is_map_dirty",
    )

    latitude: float | None = Field(
        default=None,
        alias="latitude",
    )

    longitude: float | None = Field(
        default=None,
        alias="longitude",
    )

    postal_code: str | None = Field(
        default=None,
        alias="postal_code",
    )

    state_or_province: str | None = Field(
        default=None,
        alias="state_or_province",
    )

    state_or_province_region: str | None = Field(
        default=None,
        alias="state_or_province_region",
    )

    street_name: str | None = Field(
        default=None,
        alias="street_name",
    )

    street_number: str | None = Field(
        default=None,
        alias="street_number",
    )

    unit_number: str | None = Field(
        default=None,
        alias="unit_number",
    )


class AddressPostPayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/AddressPostPayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    city: str | None = Field(
        default=None,
        alias="city",
    )

    city_region: str | None = Field(
        default=None,
        alias="city_region",
    )

    country: str | None = Field(
        default=None,
        alias="country",
    )

    country_region: str | None = Field(
        default=None,
        alias="country_region",
    )

    county_or_parish: str | None = Field(
        default=None,
        alias="county_or_parish",
    )

    latitude: float | None = Field(
        default=...,
        alias="latitude",
    )

    longitude: float | None = Field(
        default=...,
        alias="longitude",
    )

    postal_code: str | None = Field(
        default=None,
        alias="postal_code",
    )

    state_or_province: str | None = Field(
        default=None,
        alias="state_or_province",
    )

    state_or_province_region: str | None = Field(
        default=None,
        alias="state_or_province_region",
    )

    street_name: str | None = Field(
        default=None,
        alias="street_name",
    )

    street_number: str | None = Field(
        default=None,
        alias="street_number",
    )

    unit_number: str | None = Field(
        default=None,
        alias="unit_number",
    )


class AddressPredictionResult(BaseModel):
    """Aryeo API schema for `#/components/schemas/AddressPredictionResult`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    external_id: str | None = Field(
        default=...,
        alias="external_id",
    )

    external_type: AddressPredictionResultExternalTypeEnum | None = Field(
        default=...,
        alias="external_type",
    )

    unparsed_address: str | None = Field(
        default=...,
        alias="unparsed_address",
    )

    unparsed_address_part_one: str | None = Field(
        default=...,
        alias="unparsed_address_part_one",
    )

    unparsed_address_part_two: str | None = Field(
        default=...,
        alias="unparsed_address_part_two",
    )


class AddressPredictionResultCollection(BaseModel):
    """Aryeo API schema for `#/components/schemas/AddressPredictionResultCollection`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: list[AddressPredictionResult] | None = Field(
        default=None,
        alias="data",
    )

    links: PaginationLinks | None = Field(
        default=None,
        alias="links",
    )

    meta: PaginationMeta | None = Field(
        default=None,
        alias="meta",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class AddressResource(BaseModel):
    """Aryeo API schema for `#/components/schemas/AddressResource`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: Address | None = Field(
        default=None,
        alias="data",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class AddressSearchResult(BaseModel):
    """Aryeo API schema for `#/components/schemas/AddressSearchResult`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    city: str | None = Field(
        default=None,
        alias="city",
    )

    city_region: str | None = Field(
        default=None,
        alias="city_region",
    )

    country: str | None = Field(
        default=None,
        alias="country",
    )

    country_region: str | None = Field(
        default=None,
        alias="country_region",
    )

    county_or_parish: str | None = Field(
        default=None,
        alias="county_or_parish",
    )

    external_data: dict[str, JSONValue] | None = Field(
        default=None,
        alias="external_data",
    )

    external_id: str | None = Field(
        default=None,
        alias="external_id",
    )

    external_type: AddressSearchResultExternalTypeEnum | None = Field(
        default=None,
        alias="external_type",
    )

    external_url: str | None = Field(
        default=None,
        alias="external_url",
    )

    is_map_dirty: bool | None = Field(
        default=None,
        alias="is_map_dirty",
    )

    latitude: float | None = Field(
        default=None,
        alias="latitude",
    )

    longitude: float | None = Field(
        default=None,
        alias="longitude",
    )

    postal_code: str | None = Field(
        default=None,
        alias="postal_code",
    )

    state_or_province: str | None = Field(
        default=None,
        alias="state_or_province",
    )

    state_or_province_region: str | None = Field(
        default=None,
        alias="state_or_province_region",
    )

    street_name: str | None = Field(
        default=None,
        alias="street_name",
    )

    street_number: str | None = Field(
        default=None,
        alias="street_number",
    )

    timezone: str | None = Field(
        default=None,
        alias="timezone",
    )

    unit_number: str | None = Field(
        default=None,
        alias="unit_number",
    )

    unparsed_address: str | None = Field(
        default=None,
        alias="unparsed_address",
    )

    unparsed_address_part_one: str | None = Field(
        default=None,
        alias="unparsed_address_part_one",
    )

    unparsed_address_part_one_formatting: str | None = Field(
        default=None,
        alias="unparsed_address_part_one_formatting",
    )

    unparsed_address_part_two: str | None = Field(
        default=None,
        alias="unparsed_address_part_two",
    )

    unparsed_address_part_two_formatting: str | None = Field(
        default=None,
        alias="unparsed_address_part_two_formatting",
    )


class AddressSearchResultResource(BaseModel):
    """Aryeo API schema for `#/components/schemas/AddressSearchResultResource`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: AddressSearchResult | None = Field(
        default=None,
        alias="data",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class ApiError403(BaseModel):
    """Aryeo API schema for `#/components/schemas/ApiError403`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    code: int | None = Field(
        default=None,
        alias="code",
    )

    message: str = Field(
        default=...,
        alias="message",
    )

    status: str = Field(
        default=...,
        alias="status",
    )


class ApiError404(BaseModel):
    """Aryeo API schema for `#/components/schemas/ApiError404`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    code: int | None = Field(
        default=None,
        alias="code",
    )

    message: str = Field(
        default=...,
        alias="message",
    )

    status: str = Field(
        default=...,
        alias="status",
    )


class ApiError409(BaseModel):
    """Aryeo API schema for `#/components/schemas/ApiError409`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    code: int | None = Field(
        default=None,
        alias="code",
    )

    message: str = Field(
        default=...,
        alias="message",
    )

    status: str = Field(
        default=...,
        alias="status",
    )


class ApiError500(BaseModel):
    """Aryeo API schema for `#/components/schemas/ApiError500`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    code: int | None = Field(
        default=None,
        alias="code",
    )

    message: str = Field(
        default=...,
        alias="message",
    )

    status: str = Field(
        default=...,
        alias="status",
    )


class ApiFail422(BaseModel):
    """Aryeo API schema for `#/components/schemas/ApiFail422`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    status: str = Field(
        default=...,
        alias="status",
    )


class ApiSuccess2xx(BaseModel):
    """Aryeo API schema for `#/components/schemas/ApiSuccess2xx`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    status: str = Field(
        default=...,
        alias="status",
    )


class AppAndroidDetails(BaseModel):
    """Aryeo API schema for `#/components/schemas/AppAndroidDetails`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    package_name: str | None = Field(
        default=None,
        alias="package_name",
    )


class AppIosdetails(BaseModel):
    """Aryeo API schema for `#/components/schemas/AppIOSDetails`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    bundle_id: str | None = Field(
        default=None,
        alias="bundle_id",
    )

    itunes_app_id: str | None = Field(
        default=None,
        alias="itunes_app_id",
    )


class AppStoreDetails(BaseModel):
    """Aryeo API schema for `#/components/schemas/AppStoreDetails`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    bundle_id: str | None = Field(
        default=None,
        alias="bundle_id",
    )

    description: str | None = Field(
        default=None,
        alias="description",
    )

    itunes_app_id: str | None = Field(
        default=None,
        alias="itunes_app_id",
    )

    keywords: str | None = Field(
        default=None,
        alias="keywords",
    )

    marketing_url: str | None = Field(
        default=None,
        alias="marketing_url",
    )

    name: str | None = Field(
        default=None,
        alias="name",
    )

    package_name: str | None = Field(
        default=None,
        alias="package_name",
    )

    subtitle: str | None = Field(
        default=None,
        alias="subtitle",
    )

    support_url: str | None = Field(
        default=None,
        alias="support_url",
    )

    version_latest_android: str | None = Field(
        default=None,
        alias="version_latest_android",
    )

    version_latest_ios: str | None = Field(
        default=None,
        alias="version_latest_ios",
    )

    version_minimum: str | None = Field(
        default=None,
        alias="version_minimum",
    )


class Appointment(BaseModel):
    """Aryeo API schema for `#/components/schemas/Appointment`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    appointment_attendances: list[AppointmentAttendance] | None = Field(
        default=None,
        alias="appointment_attendances",
    )

    can_cancel: bool | None = Field(
        default=None,
        alias="can_cancel",
    )

    can_reschedule: bool | None = Field(
        default=None,
        alias="can_reschedule",
    )

    company_team_members: list[CompanyTeamMember] | None = Field(
        default=None,
        alias="company_team_members",
    )

    deleted_at: str | None = Field(
        default=None,
        alias="deleted_at",
    )

    description: str | None = Field(
        default=None,
        alias="description",
    )

    duration: int | None = Field(
        default=None,
        alias="duration",
    )

    end_at: str | None = Field(
        default=None,
        alias="end_at",
    )

    id: str = Field(
        default=...,
        alias="id",
    )

    is_within_cancellation_lock_period: bool | None = Field(
        default=None,
        alias="is_within_cancellation_lock_period",
    )

    is_within_rescheduling_lock_period: bool | None = Field(
        default=None,
        alias="is_within_rescheduling_lock_period",
    )

    items: list[OrderItem] | None = Field(
        default=None,
        alias="items",
    )

    late_cancellation_fee: list[dict[str, JSONValue]] | None = Field(
        default=None,
        alias="late_cancellation_fee",
    )

    order: Order | None = Field(
        default=None,
        alias="order",
    )

    postponed_at: str | None = Field(
        default=None,
        alias="postponed_at",
    )

    preference_type: AppointmentPreferenceTypeEnum | None = Field(
        default=None,
        alias="preference_type",
    )

    preferred_start_at: str | None = Field(
        default=None,
        alias="preferred_start_at",
    )

    preferred_start_at_day: str | None = Field(
        default=None,
        alias="preferred_start_at_day",
    )

    preferred_start_at_time_of_day: AppointmentPreferredStartAtTimeOfDayEnum | None = (
        Field(
            default=None,
            alias="preferred_start_at_time_of_day",
        )
    )

    previous_start_at: str | None = Field(
        default=None,
        alias="previous_start_at",
    )

    requires_confirmation: bool | None = Field(
        default=None,
        alias="requires_confirmation",
    )

    rescheduled_at: str | None = Field(
        default=None,
        alias="rescheduled_at",
    )

    start_at: str | None = Field(
        default=None,
        alias="start_at",
    )

    status: AppointmentStatusEnum | None = Field(
        default=None,
        alias="status",
    )

    title: str | None = Field(
        default=None,
        alias="title",
    )

    updated_at: str | None = Field(
        default=None,
        alias="updated_at",
    )

    user_has_appointments_manage_permission: bool | None = Field(
        default=None,
        alias="user_has_appointments_manage_permission",
    )

    users: list[User] | None = Field(
        default=None,
        alias="users",
    )


class Appointment3dhTourLinkResponse(BaseModel):
    """Aryeo API schema for `#/components/schemas/Appointment3dhTourLinkResponse`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    last_tour_started_at: str | None = Field(
        default=None,
        alias="last_tour_started_at",
    )

    last_tour_started_by: str | None = Field(
        default=None,
        alias="last_tour_started_by",
    )

    url: str = Field(
        default=...,
        alias="url",
    )


class AppointmentAcceptPutPayload(RootModel[dict[str, JSONValue]]):
    """Aryeo API root schema for `#/components/schemas/AppointmentAcceptPutPayload`."""


class AppointmentAttendance(BaseModel):
    """Aryeo API schema for `#/components/schemas/AppointmentAttendance`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    accepted_at: str | None = Field(
        default=None,
        alias="accepted_at",
    )

    company_team_member: CompanyTeamMember = Field(
        default=...,
        alias="company_team_member",
    )

    declined_at: str | None = Field(
        default=None,
        alias="declined_at",
    )

    id: float | None = Field(
        default=...,
        alias="id",
    )

    is_requested: bool = Field(
        default=...,
        alias="is_requested",
    )

    object: AppointmentAttendanceObjectEnum = Field(
        default=...,
        alias="object",
    )

    zillow_3d_home_deep_link_url: str | None = Field(
        default=None,
        alias="zillow_3d_home_deep_link_url",
    )


class AppointmentCancelPutPayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/AppointmentCancelPutPayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    notify: bool | None = Field(
        default=None,
        alias="notify",
    )


class AppointmentCollection(BaseModel):
    """Aryeo API schema for `#/components/schemas/AppointmentCollection`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: list[Appointment] | None = Field(
        default=None,
        alias="data",
    )

    links: PaginationLinks | None = Field(
        default=None,
        alias="links",
    )

    meta: PaginationMeta | None = Field(
        default=None,
        alias="meta",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class AppointmentDeclinePutPayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/AppointmentDeclinePutPayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    reason: str | None = Field(
        default=None,
        alias="reason",
    )


class AppointmentPostponePutPayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/AppointmentPostponePutPayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    notify: bool | None = Field(
        default=None,
        alias="notify",
    )

    waive_fee: bool | None = Field(
        default=None,
        alias="waive_fee",
    )


class AppointmentReschedulePutPayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/AppointmentReschedulePutPayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    end_at: str | None = Field(
        default=...,
        alias="end_at",
    )

    notify: bool | None = Field(
        default=None,
        alias="notify",
    )

    start_at: str | None = Field(
        default=...,
        alias="start_at",
    )


class AppointmentResource(BaseModel):
    """Aryeo API schema for `#/components/schemas/AppointmentResource`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: Appointment | None = Field(
        default=None,
        alias="data",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class AppointmentSchedulePutPayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/AppointmentSchedulePutPayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    auto_confirm: bool | None = Field(
        default=None,
        alias="auto_confirm",
    )

    company_team_member_ids: list[str] | None = Field(
        default=None,
        alias="company_team_member_ids",
    )

    end_at: str | None = Field(
        default=...,
        alias="end_at",
    )

    notify: bool | None = Field(
        default=None,
        alias="notify",
    )

    start_at: str | None = Field(
        default=...,
        alias="start_at",
    )

    user_ids: list[str] | None = Field(
        default=None,
        alias="user_ids",
    )

    waive_fee: bool | None = Field(
        default=None,
        alias="waive_fee",
    )


class AppointmentStorePostPayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/AppointmentStorePostPayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    address_id: str | None = Field(
        default=None,
        alias="address_id",
    )

    company_team_member_ids: list[str] | None = Field(
        default=None,
        alias="company_team_member_ids",
    )

    end_at: str = Field(
        default=...,
        alias="end_at",
    )

    item_ids: list[str] | None = Field(
        default=None,
        alias="item_ids",
    )

    notify: bool | None = Field(
        default=None,
        alias="notify",
    )

    notify_company: bool | None = Field(
        default=None,
        alias="notifyCompany",
    )

    notify_customer: bool | None = Field(
        default=None,
        alias="notifyCustomer",
    )

    order_id: str = Field(
        default=...,
        alias="order_id",
    )

    start_at: str = Field(
        default=...,
        alias="start_at",
    )

    user_ids: list[str] | None = Field(
        default=None,
        alias="user_ids",
    )


class AppointmentUpdatePutPayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/AppointmentUpdatePutPayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    end_at: str | None = Field(
        default=None,
        alias="end_at",
    )

    item_ids: list[str] | None = Field(
        default=None,
        alias="item_ids",
    )

    notify: bool | None = Field(
        default=None,
        alias="notify",
    )

    start_at: str | None = Field(
        default=None,
        alias="start_at",
    )

    user_ids: list[str] | None = Field(
        default=None,
        alias="user_ids",
    )


class AryeoGoConfig(BaseModel):
    """Aryeo API schema for `#/components/schemas/AryeoGoConfig`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    object: str | None = Field(
        default=None,
        alias="object",
    )

    version_latest_android: str | None = Field(
        default=None,
        alias="version_latest_android",
    )

    version_latest_ios: str | None = Field(
        default=None,
        alias="version_latest_ios",
    )

    version_minimum: str | None = Field(
        default=None,
        alias="version_minimum",
    )


class AryeoGoConfigResource(BaseModel):
    """Aryeo API schema for `#/components/schemas/AryeoGoConfigResource`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: AryeoGoConfig | None = Field(
        default=None,
        alias="data",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class AuthActivationStageResource(BaseModel):
    """Aryeo API schema for `#/components/schemas/AuthActivationStageResource`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    has_admin_account: bool | None = Field(
        default=None,
        alias="has_admin_account",
    )

    status: AuthActivationStageResourceStatusEnum | None = Field(
        default=None,
        alias="status",
    )


class AuthEmailCheckPostPayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/AuthEmailCheckPostPayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    email: str = Field(
        default=...,
        alias="email",
    )


class AvailabilityResponse(BaseModel):
    """Aryeo API schema for `#/components/schemas/AvailabilityResponse`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    has_conflicts: bool = Field(
        default=...,
        alias="has_conflicts",
    )


class BlockPostPayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/BlockPostPayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    company_team_member_ids: list[str] | None = Field(
        default=None,
        alias="company_team_member_ids",
    )

    description: str | None = Field(
        default=None,
        alias="description",
    )

    end_at: str = Field(
        default=...,
        alias="end_at",
    )

    start_at: str = Field(
        default=...,
        alias="start_at",
    )

    title: str = Field(
        default=...,
        alias="title",
    )

    user_ids: list[str] | None = Field(
        default=None,
        alias="user_ids",
    )


class BookingLimits(BaseModel):
    """Aryeo API schema for `#/components/schemas/BookingLimits`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    automated_user_assignment_strategy: (
        BookingLimitsAutomatedUserAssignmentStrategyEnum | None
    ) = Field(
        default=...,
        alias="automated_user_assignment_strategy",
    )

    availability_style: BookingLimitsAvailabilityStyleEnum | None = Field(
        default=...,
        alias="availability_style",
    )

    is_twilight_visible: bool | None = Field(
        default=...,
        alias="is_twilight_visible",
    )

    object: BookingLimitsObjectEnum = Field(
        default=...,
        alias="object",
    )

    show_user_names: bool | None = Field(
        default=...,
        alias="show_user_names",
    )

    slot_interval_minutes: int | None = Field(
        default=...,
        alias="slot_interval_minutes",
    )

    use_automated_user_assignment: bool | None = Field(
        default=...,
        alias="use_automated_user_assignment",
    )

    use_instant_appointment_scheduling: bool | None = Field(
        default=...,
        alias="use_instant_appointment_scheduling",
    )

    use_territory_awareness: bool | None = Field(
        default=...,
        alias="use_territory_awareness",
    )


class CalendarBlock(BaseModel):
    """Aryeo API schema for `#/components/schemas/CalendarBlock`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    company_team_members: list[CompanyTeamMember] | None = Field(
        default=None,
        alias="company_team_members",
    )

    description: str | None = Field(
        default=...,
        alias="description",
    )

    duration: int = Field(
        default=...,
        alias="duration",
    )

    end_at: str = Field(
        default=...,
        alias="end_at",
    )

    id: str = Field(
        default=...,
        alias="id",
    )

    is_all_day: bool = Field(
        default=...,
        alias="is_all_day",
    )

    is_busy: bool = Field(
        default=...,
        alias="is_busy",
    )

    start_at: str = Field(
        default=...,
        alias="start_at",
    )

    title: str = Field(
        default=...,
        alias="title",
    )

    type: CalendarBlockTypeEnum = Field(
        default=...,
        alias="type",
    )

    users: list[User] | None = Field(
        default=None,
        alias="users",
    )


class CalendarBlockResource(BaseModel):
    """Aryeo API schema for `#/components/schemas/CalendarBlockResource`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: CalendarBlock | None = Field(
        default=None,
        alias="data",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class CalendarDay(BaseModel):
    """Aryeo API schema for `#/components/schemas/CalendarDay`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    date: str = Field(
        default=...,
        alias="date",
    )

    is_available: bool = Field(
        default=...,
        alias="is_available",
    )


class CalendarDayCollection(BaseModel):
    """Aryeo API schema for `#/components/schemas/CalendarDayCollection`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: list[CalendarDay] | None = Field(
        default=None,
        alias="data",
    )

    links: PaginationLinks | None = Field(
        default=None,
        alias="links",
    )

    meta: CalendarDayCollectionMeta | None = Field(
        default=None,
        alias="meta",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class CalendarDayCollectionMeta(BaseModel):
    """Aryeo API schema for `#/components/schemas/CalendarDayCollectionMeta`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    appointment_id: str | None = Field(
        default=None,
        alias="appointment_id",
    )

    company_id: str | None = Field(
        default=None,
        alias="company_id",
    )

    company_team_member_ids: list[str] | None = Field(
        default=None,
        alias="company_team_member_ids",
    )

    current_page: int = Field(
        default=...,
        alias="current_page",
    )

    duration: int | None = Field(
        default=None,
        alias="duration",
    )

    end_at: str | None = Field(
        default=None,
        alias="end_at",
    )

    from_value: int | None = Field(
        default=None,
        alias="from",
    )

    group_id: str | None = Field(
        default=None,
        alias="group_id",
    )

    interval: int | None = Field(
        default=None,
        alias="interval",
    )

    is_twilight: bool | None = Field(
        default=None,
        alias="is_twilight",
    )

    last_page: int | None = Field(
        default=None,
        alias="last_page",
    )

    links: list[PaginationLink] | None = Field(
        default=None,
        alias="links",
    )

    path: str | None = Field(
        default=None,
        alias="path",
    )

    per_page: int | None = Field(
        default=None,
        alias="per_page",
    )

    start_at: str | None = Field(
        default=None,
        alias="start_at",
    )

    timeframe: str | None = Field(
        default=None,
        alias="timeframe",
    )

    timeframe_period: dict[str, JSONValue] | None = Field(
        default=None,
        alias="timeframe_period",
    )

    timezone: str | None = Field(
        default=None,
        alias="timezone",
    )

    to: int | None = Field(
        default=None,
        alias="to",
    )

    total: int | None = Field(
        default=None,
        alias="total",
    )

    user_ids: list[str] | None = Field(
        default=None,
        alias="user_ids",
    )


class CalendarEvent(BaseModel):
    """Aryeo API schema for `#/components/schemas/CalendarEvent`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    description: str | None = Field(
        default=None,
        alias="description",
    )

    duration: int | None = Field(
        default=None,
        alias="duration",
    )

    end_at: str | None = Field(
        default=None,
        alias="end_at",
    )

    id: str | None = Field(
        default=None,
        alias="id",
    )

    is_all_day: bool | None = Field(
        default=None,
        alias="is_all_day",
    )

    is_busy: bool | None = Field(
        default=None,
        alias="is_busy",
    )

    requires_confirmation: bool | None = Field(
        default=None,
        alias="requires_confirmation",
    )

    start_at: str | None = Field(
        default=None,
        alias="start_at",
    )

    title: str | None = Field(
        default=None,
        alias="title",
    )

    type: CalendarEventTypeEnum | None = Field(
        default=None,
        alias="type",
    )


class CalendarEventCollection(BaseModel):
    """Aryeo API schema for `#/components/schemas/CalendarEventCollection`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: list[CalendarEvent] | None = Field(
        default=None,
        alias="data",
    )

    links: PaginationLinks | None = Field(
        default=None,
        alias="links",
    )

    meta: PaginationMeta | None = Field(
        default=None,
        alias="meta",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class CalendarEventResource(BaseModel):
    """Aryeo API schema for `#/components/schemas/CalendarEventResource`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: CalendarEvent | None = Field(
        default=None,
        alias="data",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class CompanyTeamMember(BaseModel):
    """Aryeo API schema for `#/components/schemas/CompanyTeamMember`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    calendar_color: str | None = Field(
        default=None,
        alias="calendar_color",
    )

    company_user: User | None = Field(
        default=None,
        alias="company_user",
    )

    created_at: str | None = Field(
        default=None,
        alias="created_at",
    )

    external_id: str | None = Field(
        default=None,
        alias="external_id",
    )

    fees: list[Fee] | None = Field(
        default=None,
        alias="fees",
    )

    has_owner_role: bool | None = Field(
        default=None,
        alias="has_owner_role",
    )

    id: str = Field(
        default=...,
        alias="id",
    )

    invitation_accepted_at: str | None = Field(
        default=None,
        alias="invitation_accepted_at",
    )

    is_active: bool | None = Field(
        default=None,
        alias="is_active",
    )

    is_invited: bool | None = Field(
        default=None,
        alias="is_invited",
    )

    is_owner: bool | None = Field(
        default=None,
        alias="is_owner",
    )

    is_revoked: bool | None = Field(
        default=None,
        alias="is_revoked",
    )

    is_service_provider: bool = Field(
        default=...,
        alias="is_service_provider",
    )

    object: CompanyTeamMemberObjectEnum = Field(
        default=...,
        alias="object",
    )

    permissions: list[CompanyTeamMemberPermission] = Field(
        default=...,
        alias="permissions",
    )

    require_appointment_confirmation: bool | None = Field(
        default=None,
        alias="require_appointment_confirmation",
    )

    restricted_customers: list[Group] | None = Field(
        default=None,
        alias="restricted_customers",
    )

    restrictions: list[dict[str, JSONValue]] = Field(
        default=...,
        alias="restrictions",
    )

    role: CompanyTeamMemberRoleEnum | None = Field(
        default=None,
        alias="role",
    )

    scheduling_priority: int | None = Field(
        default=None,
        alias="scheduling_priority",
    )

    status: CompanyTeamMemberStatusEnum | None = Field(
        default=None,
        alias="status",
    )

    travel_fee_amount: int | None = Field(
        default=None,
        alias="travel_fee_amount",
    )

    travel_fee_is_estimated: bool | None = Field(
        default=None,
        alias="travel_fee_is_estimated",
    )


class CompanyTeamMemberCollection(BaseModel):
    """Aryeo API schema for `#/components/schemas/CompanyTeamMemberCollection`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: list[CompanyTeamMember] | None = Field(
        default=None,
        alias="data",
    )

    links: PaginationLinks | None = Field(
        default=None,
        alias="links",
    )

    meta: PaginationMeta | None = Field(
        default=None,
        alias="meta",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class CompanyTeamMemberPermission(BaseModel):
    """Aryeo API schema for `#/components/schemas/CompanyTeamMemberPermission`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    name: CompanyTeamMemberPermissionNameEnum = Field(
        default=...,
        alias="name",
    )

    object: CompanyTeamMemberPermissionObjectEnum | None = Field(
        default=None,
        alias="object",
    )


class CompanyTeamMemberResource(BaseModel):
    """Aryeo API schema for `#/components/schemas/CompanyTeamMemberResource`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: CompanyTeamMember | None = Field(
        default=None,
        alias="data",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    strategy_type: CompanyTeamMemberResourceStrategyTypeEnum | None = Field(
        default=None,
        alias="strategy_type",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class Coupon(BaseModel):
    """Aryeo API schema for `#/components/schemas/Coupon`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    amount_off: int | None = Field(
        default=None,
        alias="amount_off",
    )

    amount_off_formatted: str | None = Field(
        default=None,
        alias="amount_off_formatted",
    )

    created_at: str | None = Field(
        default=None,
        alias="created_at",
    )

    discountables: list[Discountable] | None = Field(
        default=None,
        alias="discountables",
    )

    id: str = Field(
        default=...,
        alias="id",
    )

    is_active: bool | None = Field(
        default=None,
        alias="is_active",
    )

    is_percent_off: bool | None = Field(
        default=None,
        alias="is_percent_off",
    )

    name: str | None = Field(
        default=None,
        alias="name",
    )

    percent_off: float | None = Field(
        default=None,
        alias="percent_off",
    )

    promotion_codes: list[PromotionCode] | None = Field(
        default=None,
        alias="promotion_codes",
    )

    times_redeemed: int | None = Field(
        default=None,
        alias="times_redeemed",
    )


class CouponCollection(BaseModel):
    """Aryeo API schema for `#/components/schemas/CouponCollection`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: list[Coupon] | None = Field(
        default=None,
        alias="data",
    )

    links: PaginationLinks | None = Field(
        default=None,
        alias="links",
    )

    meta: PaginationMeta | None = Field(
        default=None,
        alias="meta",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class CreditTransaction(BaseModel):
    """Aryeo API schema for `#/components/schemas/CreditTransaction`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    amount: int = Field(
        default=...,
        alias="amount",
    )

    created_at: str = Field(
        default=...,
        alias="created_at",
    )

    description: str | None = Field(
        default=None,
        alias="description",
    )

    posting_date: str | None = Field(
        default=None,
        alias="posting_date",
    )

    type: CreditTransactionTypeEnum = Field(
        default=...,
        alias="type",
    )

    updated_at: str = Field(
        default=...,
        alias="updated_at",
    )

    user_id: str = Field(
        default=...,
        alias="user_id",
    )


class CreditTransactionResource(BaseModel):
    """Aryeo API schema for `#/components/schemas/CreditTransactionResource`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: CreditTransaction = Field(
        default=...,
        alias="data",
    )


class CubiCasaFloorplan(BaseModel):
    """Aryeo API schema for `#/components/schemas/CubiCasaFloorplan`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    current_sync: str | None = Field(
        default=...,
        alias="current_sync",
    )

    results: list[CubiCasaFloorplanResult] = Field(
        default=...,
        alias="results",
    )

    show_all: bool = Field(
        default=...,
        alias="show_all",
    )

    suggested: dict[str, JSONValue] | None = Field(
        default=...,
        alias="suggested",
    )


class CubiCasaFloorplanResource(BaseModel):
    """Aryeo API schema for `#/components/schemas/CubiCasaFloorplanResource`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: CubiCasaFloorplan | None = Field(
        default=None,
        alias="data",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class CubiCasaFloorplanResult(BaseModel):
    """Aryeo API schema for `#/components/schemas/CubiCasaFloorplanResult`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    city: str = Field(
        default=...,
        alias="city",
    )

    county: str = Field(
        default=...,
        alias="county",
    )

    full_address: str = Field(
        default=...,
        alias="full_address",
    )

    jpg_urls: list[str] = Field(
        default=...,
        alias="jpg_urls",
    )

    latitude: float = Field(
        default=...,
        alias="latitude",
    )

    longitude: float = Field(
        default=...,
        alias="longitude",
    )

    number: str = Field(
        default=...,
        alias="number",
    )

    postal_code: str = Field(
        default=...,
        alias="postalCode",
    )

    public_id: str = Field(
        default=...,
        alias="public_id",
    )

    state: str = Field(
        default=...,
        alias="state",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    street: str = Field(
        default=...,
        alias="street",
    )

    suite: str = Field(
        default=...,
        alias="suite",
    )


class CustomerGroup(BaseModel):
    """Aryeo API schema for `#/components/schemas/CustomerGroup`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    affiliate_id: str | None = Field(
        default=None,
        alias="affiliate_id",
    )

    billing_customer: Group | None = Field(
        default=None,
        alias="billing_customer",
    )

    billing_customer_pays_externally: bool | None = Field(
        default=None,
        alias="billing_customer_pays_externally",
    )

    brokerage_name: str | None = Field(
        default=None,
        alias="brokerage_name",
    )

    brokerage_website: str | None = Field(
        default=None,
        alias="brokerage_website",
    )

    company: Group | None = Field(
        default=None,
        alias="company",
    )

    created_at: str | None = Field(
        default=None,
        alias="created_at",
    )

    description: str | None = Field(
        default=None,
        alias="description",
    )

    id: str = Field(
        default=...,
        alias="id",
    )

    internal_notes: str | None = Field(
        default=None,
        alias="internal_notes",
    )

    is_archived: bool | None = Field(
        default=None,
        alias="is_archived",
    )

    is_default: bool | None = Field(
        default=None,
        alias="is_default",
    )

    is_showingtimeplus_team: bool | None = Field(
        default=None,
        alias="is_showingtimeplus_team",
    )

    logo_url: str | None = Field(
        default=None,
        alias="logo_url",
    )

    name: str = Field(
        default=...,
        alias="name",
    )

    object: CustomerGroupObjectEnum | None = Field(
        default=None,
        alias="object",
    )

    order_form_id: str | None = Field(
        default=None,
        alias="order_form_id",
    )

    should_disable_automated_payment_reminder_email: bool | None = Field(
        default=None,
        alias="should_disable_automated_payment_reminder_email",
    )

    should_display_original_price: bool | None = Field(
        default=None,
        alias="should_display_original_price",
    )

    should_lock_downloads_before_payment: bool | None = Field(
        default=None,
        alias="should_lock_downloads_before_payment",
    )

    status: CustomerGroupStatusEnum | None = Field(
        default=None,
        alias="status",
    )

    tags: list[Tag] | None = Field(
        default=None,
        alias="tags",
    )

    website: str | None = Field(
        default=None,
        alias="website",
    )


class CustomerPostPayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/CustomerPostPayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    avatar_url: str | None = Field(
        default=None,
        alias="avatar_url",
    )

    customer_team_id: str | None = Field(
        default=None,
        alias="customer_team_id",
    )

    description: str | None = Field(
        default=None,
        alias="description",
    )

    email: str = Field(
        default=...,
        alias="email",
    )

    license_number: str | None = Field(
        default=None,
        alias="license_number",
    )

    logo_url: str | None = Field(
        default=None,
        alias="logo_url",
    )

    office_name: str | None = Field(
        default=None,
        alias="office_name",
    )

    owner_first_name: str = Field(
        default=...,
        alias="owner_first_name",
    )

    owner_last_name: str = Field(
        default=...,
        alias="owner_last_name",
    )

    phone: str | None = Field(
        default=None,
        alias="phone",
    )

    team_name: str | None = Field(
        default=None,
        alias="team_name",
    )

    timezone: str | None = Field(
        default=None,
        alias="timezone",
    )

    website_url: str | None = Field(
        default=None,
        alias="website_url",
    )


class CustomerTeamAffiliateMembershipPostPayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/CustomerTeamAffiliateMembershipPostPayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    affiliate_id: str = Field(
        default=...,
        alias="affiliate_id",
    )

    customer_user_id: str = Field(
        default=...,
        alias="customer_user_id",
    )


class CustomerTeamMembership(BaseModel):
    """Aryeo API schema for `#/components/schemas/CustomerTeamMembership`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    created_at: str | None = Field(
        default=None,
        alias="created_at",
    )

    customer_team: CustomerGroup | None = Field(
        default=None,
        alias="customer_team",
    )

    customer_user: CustomerUser | None = Field(
        default=None,
        alias="customer_user",
    )

    id: str = Field(
        default=...,
        alias="id",
    )

    invitation_accepted_at: str | None = Field(
        default=None,
        alias="invitation_accepted_at",
    )

    is_active: bool | None = Field(
        default=None,
        alias="is_active",
    )

    is_archived: bool | None = Field(
        default=None,
        alias="is_archived",
    )

    is_default: bool | None = Field(
        default=None,
        alias="is_default",
    )

    is_deleted: bool | None = Field(
        default=None,
        alias="is_deleted",
    )

    is_invited: bool | None = Field(
        default=None,
        alias="is_invited",
    )

    is_showingtimeplus_workspace_membership: bool | None = Field(
        default=None,
        alias="is_showingtimeplus_workspace_membership",
    )

    is_visible: bool | None = Field(
        default=None,
        alias="is_visible",
    )

    listing_delivery_notification_enabled: bool | None = Field(
        default=None,
        alias="listing_delivery_notification_enabled",
    )

    object: CustomerTeamMembershipObjectEnum | None = Field(
        default=None,
        alias="object",
    )

    order_index: int | None = Field(
        default=None,
        alias="order_index",
    )

    role: CustomerTeamMembershipRoleEnum = Field(
        default=...,
        alias="role",
    )

    status: CustomerTeamMembershipStatusEnum = Field(
        default=...,
        alias="status",
    )


class CustomerTeamMembershipCollection(BaseModel):
    """Aryeo API schema for `#/components/schemas/CustomerTeamMembershipCollection`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: list[CustomerTeamMembership] | None = Field(
        default=None,
        alias="data",
    )

    links: PaginationLinks | None = Field(
        default=None,
        alias="links",
    )

    meta: PaginationMeta | None = Field(
        default=None,
        alias="meta",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class CustomerTeamMembershipResource(BaseModel):
    """Aryeo API schema for `#/components/schemas/CustomerTeamMembershipResource`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: CustomerTeamMembership | None = Field(
        default=None,
        alias="data",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class CustomerTeamNotesPutPayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/CustomerTeamNotesPutPayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    internal_notes: str | None = Field(
        default=None,
        alias="internal_notes",
    )


class CustomerTeamResource(BaseModel):
    """Aryeo API schema for `#/components/schemas/CustomerTeamResource`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: CustomerGroup | None = Field(
        default=None,
        alias="data",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class CustomerUser(BaseModel):
    """Aryeo API schema for `#/components/schemas/CustomerUser`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    agent_company_name: str | None = Field(
        default=None,
        alias="agent_company_name",
    )

    agent_license_number: str | None = Field(
        default=None,
        alias="agent_license_number",
    )

    avalara_customer_code: str | None = Field(
        default=None,
        alias="avalara_customer_code",
    )

    avatar_url: str | None = Field(
        default=None,
        alias="avatar_url",
    )

    created_at: str | None = Field(
        default=None,
        alias="created_at",
    )

    credit_balance_amount: float | None = Field(
        default=None,
        alias="credit_balance_amount",
    )

    customer_team_memberships: list[CustomerTeamMembership] | None = Field(
        default=None,
        alias="customer_team_memberships",
    )

    default_allows_access_to_marketing_material: bool | None = Field(
        default=None,
        alias="default_allows_access_to_marketing_material",
    )

    default_lock_downloads_before_payment: bool | None = Field(
        default=None,
        alias="default_lock_downloads_before_payment",
    )

    email: str = Field(
        default=...,
        alias="email",
    )

    first_name: str | None = Field(
        default=None,
        alias="first_name",
    )

    full_name: str | None = Field(
        default=None,
        alias="full_name",
    )

    has_restricted_photographers: bool | None = Field(
        default=None,
        alias="has_restricted_photographers",
    )

    id: str = Field(
        default=...,
        alias="id",
    )

    internal_notes: str | None = Field(
        default=None,
        alias="internal_notes",
    )

    is_blocked_from_ordering: bool | None = Field(
        default=None,
        alias="is_blocked_from_ordering",
    )

    is_showingtimeplus_user: bool | None = Field(
        default=None,
        alias="is_showingtimeplus_user",
    )

    is_super: bool | None = Field(
        default=None,
        alias="is_super",
    )

    is_visible: bool | None = Field(
        default=None,
        alias="is_visible",
    )

    last_name: str | None = Field(
        default=None,
        alias="last_name",
    )

    license_number: str | None = Field(
        default=None,
        alias="license_number",
    )

    logo_url: str | None = Field(
        default=None,
        alias="logo_url",
    )

    name: str | None = Field(
        default=None,
        alias="name",
    )

    object: str | None = Field(
        default=None,
        alias="object",
    )

    order_index: int | None = Field(
        default=None,
        alias="order_index",
    )

    phone: str | None = Field(
        default=None,
        alias="phone",
    )

    phone_number: str | None = Field(
        default=None,
        alias="phone_number",
    )

    profile_link: str | None = Field(
        default=None,
        alias="profile_link",
    )

    quickbooks_customer_id: str | None = Field(
        default=None,
        alias="quickbooks_customer_id",
    )

    status: CustomerUserStatusEnum | None = Field(
        default=None,
        alias="status",
    )

    timezone: str | None = Field(
        default=None,
        alias="timezone",
    )

    total_balance_amount: float | None = Field(
        default=None,
        alias="total_balance_amount",
    )

    verification_status: CustomerUserVerificationStatusEnum | None = Field(
        default=None,
        alias="verification_status",
    )


class CustomerUserCollection(BaseModel):
    """Aryeo API schema for `#/components/schemas/CustomerUserCollection`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: list[CustomerUser] | None = Field(
        default=...,
        alias="data",
    )

    links: PaginationLinks | None = Field(
        default=None,
        alias="links",
    )

    meta: PaginationMeta | None = Field(
        default=None,
        alias="meta",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class CustomerUserPostPayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/CustomerUserPostPayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    add_to_customer_team: bool = Field(
        default=...,
        alias="add_to_customer_team",
    )

    avatar_url: str | None = Field(
        default=None,
        alias="avatar_url",
    )

    brokerage_name: str | None = Field(
        default=None,
        alias="brokerage_name",
    )

    customer_team_id: str | None = Field(
        default=None,
        alias="customer_team_id",
    )

    defines_new_team: bool | None = Field(
        default=None,
        alias="defines_new_team",
    )

    description: str | None = Field(
        default=None,
        alias="description",
    )

    email: str = Field(
        default=...,
        alias="email",
    )

    first_name: str = Field(
        default=...,
        alias="first_name",
    )

    last_name: str = Field(
        default=...,
        alias="last_name",
    )

    license_number: str | None = Field(
        default=None,
        alias="license_number",
    )

    name: str | None = Field(
        default=None,
        alias="name",
    )

    phone: str | None = Field(
        default=None,
        alias="phone",
    )

    role: CustomerUserPostPayloadRoleEnum | None = Field(
        default=None,
        alias="role",
    )

    timezone: str | None = Field(
        default=None,
        alias="timezone",
    )


class DeleteUserPostPayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/DeleteUserPostPayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    client: DeleteUserPostPayloadClientEnum = Field(
        default=...,
        alias="client",
    )

    company_id: str = Field(
        default=...,
        alias="company_id",
    )

    email: str = Field(
        default=...,
        alias="email",
    )

    password: str = Field(
        default=...,
        alias="password",
    )


class Discount(BaseModel):
    """Aryeo API schema for `#/components/schemas/Discount`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    coupon: Coupon | None = Field(
        default=None,
        alias="coupon",
    )

    id: str = Field(
        default=...,
        alias="id",
    )

    object: DiscountObjectEnum | None = Field(
        default=None,
        alias="object",
    )

    total_discount_amount: int | None = Field(
        default=None,
        alias="total_discount_amount",
    )


class DiscountAmount(BaseModel):
    """Aryeo API schema for `#/components/schemas/DiscountAmount`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    amount: int | None = Field(
        default=None,
        alias="amount",
    )

    applied_amount_off: int | None = Field(
        default=None,
        alias="applied_amount_off",
    )

    applied_percent_off: float | None = Field(
        default=None,
        alias="applied_percent_off",
    )

    created_at: str | None = Field(
        default=None,
        alias="created_at",
    )

    discount: Discount | None = Field(
        default=None,
        alias="discount",
    )

    id: str | None = Field(
        default=None,
        alias="id",
    )

    object: DiscountAmountObjectEnum | None = Field(
        default=None,
        alias="object",
    )


class DiscountPostPayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/DiscountPostPayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    coupon_data: dict[str, JSONValue] | None = Field(
        default=None,
        alias="coupon_data",
    )

    coupon_id: str | None = Field(
        default=None,
        alias="coupon_id",
    )

    order_id: str = Field(
        default=...,
        alias="order_id",
    )


class DiscountResource(BaseModel):
    """Aryeo API schema for `#/components/schemas/DiscountResource`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: Discount | None = Field(
        default=None,
        alias="data",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class Discountable(BaseModel):
    """Aryeo API schema for `#/components/schemas/Discountable`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    discountable: DiscountableItem | None = Field(
        default=None,
        alias="discountable",
    )

    id: str = Field(
        default=...,
        alias="id",
    )

    object: str | None = Field(
        default=None,
        alias="object",
    )


class DiscountableItem(BaseModel):
    """Aryeo API schema for `#/components/schemas/DiscountableItem`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    active: bool | None = Field(
        default=None,
        alias="active",
    )

    always_display_addons: bool | None = Field(
        default=None,
        alias="always_display_addons",
    )

    amount: float | None = Field(
        default=None,
        alias="amount",
    )

    avalara_tax_code: str | None = Field(
        default=None,
        alias="avalara_tax_code",
    )

    categories: list[ProductCategory] | None = Field(
        default=None,
        alias="categories",
    )

    description: str | None = Field(
        default=None,
        alias="description",
    )

    id: str = Field(
        default=...,
        alias="id",
    )

    image_url: str | None = Field(
        default=None,
        alias="image_url",
    )

    is_esoft_adjustment: bool | None = Field(
        default=None,
        alias="is_esoft_adjustment",
    )

    is_filterable: bool | None = Field(
        default=None,
        alias="is_filterable",
    )

    is_serviceable: bool | None = Field(
        default=None,
        alias="is_serviceable",
    )

    is_twilight: bool | None = Field(
        default=None,
        alias="is_twilight",
    )

    limit_quantity: bool | None = Field(
        default=None,
        alias="limit_quantity",
    )

    limit_quantity_amount: int | None = Field(
        default=None,
        alias="limit_quantity_amount",
    )

    name: str | None = Field(
        default=None,
        alias="name",
    )

    object: str | None = Field(
        default=None,
        alias="object",
    )

    quickbooks_item: QuickBooksItem | None = Field(
        default=None,
        alias="quickbooks_item",
    )

    quickbooks_item_id: str | None = Field(
        default=None,
        alias="quickbooks_item_id",
    )

    requires_separate_booking: bool | None = Field(
        default=None,
        alias="requires_separate_booking",
    )

    title: str | None = Field(
        default=None,
        alias="title",
    )

    type: str | None = Field(
        default=None,
        alias="type",
    )

    variant_filter_type: str | None = Field(
        default=None,
        alias="variant_filter_type",
    )

    variants: list[ProductVariant] | None = Field(
        default=None,
        alias="variants",
    )


class Dots(RootModel[dict[str, dict[str, JSONValue]]]):
    """Aryeo API root schema for `#/components/schemas/Dots`."""


class DotsResource(BaseModel):
    """Aryeo API schema for `#/components/schemas/DotsResource`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: Dots | None = Field(
        default=None,
        alias="data",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class DraftOrderCustomerUserPutPayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/DraftOrderCustomerUserPutPayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    phone_number: str | None = Field(
        default=None,
        alias="phone_number",
    )


class EsoftOrderLine(BaseModel):
    """Aryeo API schema for `#/components/schemas/EsoftOrderLine`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    client_id: str | None = Field(
        default=None,
        alias="client_id",
    )

    comments: str | None = Field(
        default=None,
        alias="comments",
    )

    esoft_order_line_id: str | None = Field(
        default=None,
        alias="esoft_order_line_id",
    )

    esoft_product_id: JSONValue | None = Field(
        default=None,
        alias="esoft_product_id",
    )

    esoft_product_name: JSONValue | None = Field(
        default=None,
        alias="esoft_product_name",
    )

    esoft_product_variant: JSONValue | None = Field(
        default=None,
        alias="esoft_product_variant",
    )

    id: float | None = Field(
        default=None,
        alias="id",
    )

    object: EsoftOrderLineObjectEnum | None = Field(
        default=None,
        alias="object",
    )

    quantity: JSONValue | None = Field(
        default=None,
        alias="quantity",
    )

    reference: JSONValue | None = Field(
        default=None,
        alias="reference",
    )

    status: EsoftOrderLineStatusEnum | None = Field(
        default=None,
        alias="status",
    )


class Export(BaseModel):
    """Aryeo API schema for `#/components/schemas/Export`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    content_type: str | None = Field(
        default=...,
        alias="content_type",
    )

    extension: str | None = Field(
        default=...,
        alias="extension",
    )

    file_path: str = Field(
        default=...,
        alias="file_path",
    )

    key: str | None = Field(
        default=...,
        alias="key",
    )

    uuid: str | None = Field(
        default=...,
        alias="uuid",
    )


class FeatureFlags(RootModel[list[FeatureFlagsEnum] | None]):
    """Aryeo API root schema for `#/components/schemas/FeatureFlags`."""


class Fee(BaseModel):
    """Aryeo API schema for `#/components/schemas/Fee`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    amount: float | None = Field(
        default=None,
        alias="amount",
    )

    avalara_tax_code: str | None = Field(
        default=None,
        alias="avalara_tax_code",
    )

    description: str | None = Field(
        default=None,
        alias="description",
    )

    id: str = Field(
        default=...,
        alias="id",
    )

    name: str | None = Field(
        default=None,
        alias="name",
    )

    object: FeeObjectEnum = Field(
        default=...,
        alias="object",
    )

    quickbooks_item_id: str | None = Field(
        default=None,
        alias="quickbooks_item_id",
    )

    title: str | None = Field(
        default=None,
        alias="title",
    )

    type: FeeTypeEnum | None = Field(
        default=None,
        alias="type",
    )


class File(BaseModel):
    """Aryeo API schema for `#/components/schemas/File`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    description: str | None = Field(
        default=None,
        alias="description",
    )

    display_type: FileDisplayTypeEnum | None = Field(
        default=None,
        alias="display_type",
    )

    file_type: str = Field(
        default=...,
        alias="file_type",
    )

    filename: str = Field(
        default=...,
        alias="filename",
    )

    id: str = Field(
        default=...,
        alias="id",
    )

    object: str | None = Field(
        default=None,
        alias="object",
    )

    url: str = Field(
        default=...,
        alias="url",
    )

    uuid: str = Field(
        default=...,
        alias="uuid",
    )


class FloorPlan(BaseModel):
    """Aryeo API schema for `#/components/schemas/FloorPlan`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id: str = Field(
        default=...,
        alias="id",
    )

    index: int | None = Field(
        default=None,
        alias="index",
    )

    large_url: str = Field(
        default=...,
        alias="large_url",
    )

    object: FloorPlanObjectEnum | None = Field(
        default=None,
        alias="object",
    )

    original_url: str = Field(
        default=...,
        alias="original_url",
    )

    thumbnail_url: str = Field(
        default=...,
        alias="thumbnail_url",
    )

    title: str | None = Field(
        default=None,
        alias="title",
    )


class ForgotPasswordPostPayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/ForgotPasswordPostPayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    company_id: str | None = Field(
        default=None,
        alias="company_id",
    )

    email: str = Field(
        default=...,
        alias="email",
    )


class Group(BaseModel):
    """Aryeo API schema for `#/components/schemas/Group`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    allow_order_cancellation: bool | None = Field(
        default=None,
        alias="allow_order_cancellation",
    )

    automated_user_assignment_strategy: (
        GroupAutomatedUserAssignmentStrategyEnum | None
    ) = Field(
        default=None,
        alias="automated_user_assignment_strategy",
    )

    availability_style: GroupAvailabilityStyleEnum | None = Field(
        default=None,
        alias="availability_style",
    )

    avatar_url: str | None = Field(
        default=None,
        alias="avatar_url",
    )

    created_at: str | None = Field(
        default=None,
        alias="created_at",
    )

    currency: GroupCurrencyEnum | None = Field(
        default=None,
        alias="currency",
    )

    custom_field_entries: list[dict[str, JSONValue]] | None = Field(
        default=None,
        alias="custom_field_entries",
    )

    customer_group: str | None = Field(
        default=None,
        alias="customer_group",
    )

    default_order_form: OrderForm | None = Field(
        default=None,
        alias="default_order_form",
    )

    email: str | None = Field(
        default=None,
        alias="email",
    )

    feature_flags: FeatureFlags | None = Field(
        default=None,
        alias="feature_flags",
    )

    has_restricted_photographers: bool | None = Field(
        default=None,
        alias="has_restricted_photographers",
    )

    id: str = Field(
        default=...,
        alias="id",
    )

    internal_notes: str | None = Field(
        default=None,
        alias="internal_notes",
    )

    is_brokerage_or_brokerage_agent: bool | None = Field(
        default=None,
        alias="is_brokerage_or_brokerage_agent",
    )

    is_payroll_enabled: bool | None = Field(
        default=None,
        alias="is_payroll_enabled",
    )

    is_visible: bool | None = Field(
        default=None,
        alias="is_visible",
    )

    license_number: str | None = Field(
        default=None,
        alias="license_number",
    )

    logo_url: str | None = Field(
        default=None,
        alias="logo_url",
    )

    name: str = Field(
        default=...,
        alias="name",
    )

    object: GroupObjectEnum | None = Field(
        default=None,
        alias="object",
    )

    office_name: str | None = Field(
        default=None,
        alias="office_name",
    )

    order_forms: list[OrderForm] | None = Field(
        default=None,
        alias="order_forms",
    )

    order_index: int | None = Field(
        default=None,
        alias="order_index",
    )

    order_page_background_color: str | None = Field(
        default=None,
        alias="order_page_background_color",
    )

    order_page_url: str | None = Field(
        default=None,
        alias="order_page_url",
    )

    owner: User | None = Field(
        default=None,
        alias="owner",
    )

    phone: str | None = Field(
        default=None,
        alias="phone",
    )

    show_user_names: bool | None = Field(
        default=None,
        alias="show_user_names",
    )

    slot_interval_minutes: int | None = Field(
        default=None,
        alias="slot_interval_minutes",
    )

    slug: str | None = Field(
        default=None,
        alias="slug",
    )

    social_profiles: SocialProfiles | None = Field(
        default=None,
        alias="social_profiles",
    )

    team_members: list[User] | None = Field(
        default=None,
        alias="team_members",
    )

    timezone: str | None = Field(
        default=None,
        alias="timezone",
    )

    type: GroupTypeEnum = Field(
        default=...,
        alias="type",
    )

    use_automated_user_assignment: bool | None = Field(
        default=None,
        alias="use_automated_user_assignment",
    )

    use_instant_appointment_scheduling: bool | None = Field(
        default=None,
        alias="use_instant_appointment_scheduling",
    )

    use_territory_awareness: bool | None = Field(
        default=None,
        alias="use_territory_awareness",
    )

    users: list[User] | None = Field(
        default=None,
        alias="users",
    )

    website_url: str | None = Field(
        default=None,
        alias="website_url",
    )


class GroupCollection(BaseModel):
    """Aryeo API schema for `#/components/schemas/GroupCollection`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: list[Group] | None = Field(
        default=None,
        alias="data",
    )

    links: PaginationLinks | None = Field(
        default=None,
        alias="links",
    )

    meta: PaginationMeta | None = Field(
        default=None,
        alias="meta",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class GroupCustomer(BaseModel):
    """Aryeo API schema for `#/components/schemas/GroupCustomer`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    agent_company_name: str | None = Field(
        default=None,
        alias="agent_company_name",
    )

    agent_license_number: str | None = Field(
        default=None,
        alias="agent_license_number",
    )

    automated_user_assignment_strategy: (
        GroupCustomerAutomatedUserAssignmentStrategyEnum | None
    ) = Field(
        default=None,
        alias="automated_user_assignment_strategy",
    )

    availability_style: GroupCustomerAvailabilityStyleEnum | None = Field(
        default=None,
        alias="availability_style",
    )

    avalara_customer_code: str | None = Field(
        default=None,
        alias="avalara_customer_code",
    )

    avatar_url: str | None = Field(
        default=None,
        alias="avatar_url",
    )

    billing_address: str | None = Field(
        default=None,
        alias="billing_address",
    )

    created_at: str | None = Field(
        default=None,
        alias="created_at",
    )

    credit_balance_amount: float | None = Field(
        default=None,
        alias="credit_balance_amount",
    )

    currency: GroupCustomerCurrencyEnum | None = Field(
        default=None,
        alias="currency",
    )

    custom_field_entries: list[dict[str, JSONValue]] | None = Field(
        default=None,
        alias="custom_field_entries",
    )

    customer_group: str | None = Field(
        default=None,
        alias="customer_group",
    )

    customer_team_memberships: list[CustomerTeamMembership] | None = Field(
        default=None,
        alias="customer_team_memberships",
    )

    default_allows_access_to_marketing_material: bool | None = Field(
        default=None,
        alias="default_allows_access_to_marketing_material",
    )

    default_lock_downloads_before_payment: bool | None = Field(
        default=None,
        alias="default_lock_downloads_before_payment",
    )

    default_order_form: OrderForm | None = Field(
        default=None,
        alias="default_order_form",
    )

    email: str | None = Field(
        default=None,
        alias="email",
    )

    feature_flags: FeatureFlags | None = Field(
        default=None,
        alias="feature_flags",
    )

    first_name: str | None = Field(
        default=None,
        alias="first_name",
    )

    full_name: str | None = Field(
        default=None,
        alias="full_name",
    )

    has_restricted_photographers: bool | None = Field(
        default=None,
        alias="has_restricted_photographers",
    )

    id: str = Field(
        default=...,
        alias="id",
    )

    internal_notes: str | None = Field(
        default=None,
        alias="internal_notes",
    )

    is_blocked_from_ordering: bool | None = Field(
        default=None,
        alias="is_blocked_from_ordering",
    )

    is_brokerage_or_brokerage_agent: bool | None = Field(
        default=None,
        alias="is_brokerage_or_brokerage_agent",
    )

    is_showingtimeplus_user: bool | None = Field(
        default=None,
        alias="is_showingtimeplus_user",
    )

    is_visible: bool | None = Field(
        default=None,
        alias="is_visible",
    )

    last_name: str | None = Field(
        default=None,
        alias="last_name",
    )

    license_number: str | None = Field(
        default=None,
        alias="license_number",
    )

    logo_url: str | None = Field(
        default=None,
        alias="logo_url",
    )

    name: str | None = Field(
        default=None,
        alias="name",
    )

    object: str | None = Field(
        default=None,
        alias="object",
    )

    office_name: str | None = Field(
        default=None,
        alias="office_name",
    )

    order_forms: list[OrderForm] | None = Field(
        default=None,
        alias="order_forms",
    )

    order_index: int | None = Field(
        default=None,
        alias="order_index",
    )

    order_page_background_color: str | None = Field(
        default=None,
        alias="order_page_background_color",
    )

    order_page_url: str | None = Field(
        default=None,
        alias="order_page_url",
    )

    owner: User | None = Field(
        default=None,
        alias="owner",
    )

    phone: str | None = Field(
        default=None,
        alias="phone",
    )

    phone_number: str | None = Field(
        default=None,
        alias="phone_number",
    )

    profile_link: str | None = Field(
        default=None,
        alias="profile_link",
    )

    quickbooks_customer_id: str | None = Field(
        default=None,
        alias="quickbooks_customer_id",
    )

    restricted_photographers: list[dict[str, JSONValue]] | None = Field(
        default=None,
        alias="restricted_photographers",
    )

    show_user_names: bool | None = Field(
        default=None,
        alias="show_user_names",
    )

    slot_interval_minutes: int | None = Field(
        default=None,
        alias="slot_interval_minutes",
    )

    slug: str | None = Field(
        default=None,
        alias="slug",
    )

    social_profiles: SocialProfiles | None = Field(
        default=None,
        alias="social_profiles",
    )

    team_members: list[User] | None = Field(
        default=None,
        alias="team_members",
    )

    timezone: str | None = Field(
        default=None,
        alias="timezone",
    )

    total_balance_amount: float | None = Field(
        default=None,
        alias="total_balance_amount",
    )

    type: GroupCustomerTypeEnum | None = Field(
        default=None,
        alias="type",
    )

    use_automated_user_assignment: bool | None = Field(
        default=None,
        alias="use_automated_user_assignment",
    )

    use_instant_appointment_scheduling: bool | None = Field(
        default=None,
        alias="use_instant_appointment_scheduling",
    )

    use_territory_awareness: bool | None = Field(
        default=None,
        alias="use_territory_awareness",
    )

    users: list[User] | None = Field(
        default=None,
        alias="users",
    )

    verification_status: GroupCustomerVerificationStatusEnum | None = Field(
        default=None,
        alias="verification_status",
    )

    website_url: str | None = Field(
        default=None,
        alias="website_url",
    )


class GroupCustomerCollection(BaseModel):
    """Aryeo API schema for `#/components/schemas/GroupCustomerCollection`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: list[GroupCustomer] | None = Field(
        default=None,
        alias="data",
    )

    links: PaginationLinks | None = Field(
        default=None,
        alias="links",
    )

    meta: PaginationMeta | None = Field(
        default=None,
        alias="meta",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class GroupCustomerResource(BaseModel):
    """Aryeo API schema for `#/components/schemas/GroupCustomerResource`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: GroupCustomer | None = Field(
        default=None,
        alias="data",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class GroupResource(BaseModel):
    """Aryeo API schema for `#/components/schemas/GroupResource`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: Group | None = Field(
        default=None,
        alias="data",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class Image(BaseModel):
    """Aryeo API schema for `#/components/schemas/Image`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    caption: str | None = Field(
        default=None,
        alias="caption",
    )

    display_in_gallery: bool = Field(
        default=...,
        alias="display_in_gallery",
    )

    filename: str = Field(
        default=...,
        alias="filename",
    )

    id: str = Field(
        default=...,
        alias="id",
    )

    index: int | None = Field(
        default=None,
        alias="index",
    )

    large_url: str = Field(
        default=...,
        alias="large_url",
    )

    object: str | None = Field(
        default=None,
        alias="object",
    )

    original_url: str = Field(
        default=...,
        alias="original_url",
    )

    thumbnail_url: str = Field(
        default=...,
        alias="thumbnail_url",
    )


class ImpersonatePostPayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/ImpersonatePostPayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    client: ImpersonatePostPayloadClientEnum = Field(
        default=...,
        alias="client",
    )

    company_team_member_id: str = Field(
        default=...,
        alias="company_team_member_id",
    )

    email: str = Field(
        default=...,
        alias="email",
    )

    password: str = Field(
        default=...,
        alias="password",
    )


class InteractiveContent(BaseModel):
    """Aryeo API schema for `#/components/schemas/InteractiveContent`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    content_type: InteractiveContentContentTypeEnum = Field(
        default=...,
        alias="content_type",
    )

    display_type: InteractiveContentDisplayTypeEnum = Field(
        default=...,
        alias="display_type",
    )

    id: str = Field(
        default=...,
        alias="id",
    )

    thumbnail_url: str | None = Field(
        default=None,
        alias="thumbnail_url",
    )

    title: str | None = Field(
        default=None,
        alias="title",
    )

    url: str = Field(
        default=...,
        alias="url",
    )


class Listing(BaseModel):
    """Aryeo API schema for `#/components/schemas/Listing`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    address: Address = Field(
        default=...,
        alias="address",
    )

    appointments: list[Appointment] | None = Field(
        default=None,
        alias="appointments",
    )

    building: ListingBuilding | None = Field(
        default=None,
        alias="building",
    )

    co_list_agent: Group | None = Field(
        default=None,
        alias="co_list_agent",
    )

    customer_team_memberships: list[CustomerTeamMembership] | None = Field(
        default=None,
        alias="customer_team_memberships",
    )

    delivery_status: ListingDeliveryStatusEnum | None = Field(
        default=None,
        alias="delivery_status",
    )

    description: str | None = Field(
        default=None,
        alias="description",
    )

    downloads_enabled: bool = Field(
        default=...,
        alias="downloads_enabled",
    )

    esoft_order_lines: list[EsoftOrderLine] | None = Field(
        default=None,
        alias="esoft_order_lines",
    )

    files: list[File] | None = Field(
        default=None,
        alias="files",
    )

    floor_plans: list[FloorPlan] | None = Field(
        default=None,
        alias="floor_plans",
    )

    has_high_resolution_images: bool | None = Field(
        default=None,
        alias="has_high_resolution_images",
    )

    has_zillow_imx_tour: bool | None = Field(
        default=None,
        alias="has_zillow_imx_tour",
    )

    id: str = Field(
        default=...,
        alias="id",
    )

    images: list[Image] | None = Field(
        default=None,
        alias="images",
    )

    interactive_content: list[InteractiveContent] | None = Field(
        default=None,
        alias="interactive_content",
    )

    is_showcasable: bool | None = Field(
        default=None,
        alias="is_showcasable",
    )

    is_showcase: bool | None = Field(
        default=None,
        alias="is_showcase",
    )

    large_thumbnail_url: str | None = Field(
        default=None,
        alias="large_thumbnail_url",
    )

    list_agent: Group | None = Field(
        default=None,
        alias="list_agent",
    )

    lot: ListingLot | None = Field(
        default=None,
        alias="lot",
    )

    marketing_materials: list[MarketingMaterial] | None = Field(
        default=None,
        alias="marketing_materials",
    )

    mls_number: str | None = Field(
        default=None,
        alias="mls_number",
    )

    object: ListingObjectEnum = Field(
        default=...,
        alias="object",
    )

    orders: list[Order] | None = Field(
        default=None,
        alias="orders",
    )

    price: ListingPrice | None = Field(
        default=None,
        alias="price",
    )

    property_website: PropertyWebsite | None = Field(
        default=None,
        alias="property_website",
    )

    standard_status: ListingStandardStatusEnum | None = Field(
        default=None,
        alias="standard_status",
    )

    status: ListingStatusEnum | None = Field(
        default=None,
        alias="status",
    )

    sub_type: ListingSubTypeEnum | None = Field(
        default=None,
        alias="sub_type",
    )

    thumbnail_url: str | None = Field(
        default=None,
        alias="thumbnail_url",
    )

    type: ListingTypeEnum | None = Field(
        default=None,
        alias="type",
    )

    unconfirmed_appointments: list[Appointment] | None = Field(
        default=None,
        alias="unconfirmed_appointments",
    )

    videos: list[Video] | None = Field(
        default=None,
        alias="videos",
    )


class ListingBuilding(BaseModel):
    """Aryeo API schema for `#/components/schemas/ListingBuilding`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    bathrooms: float | None = Field(
        default=None,
        alias="bathrooms",
    )

    bedrooms: int | None = Field(
        default=None,
        alias="bedrooms",
    )

    bedrooms_number: float | None = Field(
        default=None,
        alias="bedrooms_number",
    )

    square_feet: float | None = Field(
        default=None,
        alias="square_feet",
    )

    year_built: int | None = Field(
        default=None,
        alias="year_built",
    )


class ListingCollection(BaseModel):
    """Aryeo API schema for `#/components/schemas/ListingCollection`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: list[Listing] | None = Field(
        default=None,
        alias="data",
    )

    links: PaginationLinks | None = Field(
        default=None,
        alias="links",
    )

    meta: PaginationMeta | None = Field(
        default=None,
        alias="meta",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class ListingCountsPayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/ListingCountsPayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    include_all_listings: bool | None = Field(
        default=None,
        alias="include_all_listings",
    )

    saved_view_ids: list[str] | None = Field(
        default=None,
        alias="saved_view_ids",
    )


class ListingCountsResource(BaseModel):
    """Aryeo API schema for `#/components/schemas/ListingCountsResource`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: dict[str, JSONValue] = Field(
        default=...,
        alias="data",
    )


class ListingDetailSearch(BaseModel):
    """Aryeo API schema for `#/components/schemas/ListingDetailSearch`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    bathrooms: float | None = Field(
        default=None,
        alias="bathrooms",
    )

    bedrooms: float | None = Field(
        default=None,
        alias="bedrooms",
    )

    lot_size_acres: float | None = Field(
        default=None,
        alias="lot_size_acres",
    )

    square_feet: float | None = Field(
        default=None,
        alias="square_feet",
    )

    year_built: float | None = Field(
        default=None,
        alias="year_built",
    )


class ListingDetailSearchResource(BaseModel):
    """Aryeo API schema for `#/components/schemas/ListingDetailSearchResource`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: ListingDetailSearch | None = Field(
        default=None,
        alias="data",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class ListingLot(BaseModel):
    """Aryeo API schema for `#/components/schemas/ListingLot`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    open_parking_spaces: float | None = Field(
        default=None,
        alias="open_parking_spaces",
    )

    size_acres: float | None = Field(
        default=None,
        alias="size_acres",
    )


class ListingMarketingContent(BaseModel):
    """Aryeo API schema for `#/components/schemas/ListingMarketingContent`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    address: Address | None = Field(
        default=None,
        alias="address",
    )

    building: ListingBuilding | None = Field(
        default=None,
        alias="building",
    )

    co_list_agent: Group | None = Field(
        default=None,
        alias="co_list_agent",
    )

    company: Group | None = Field(
        default=None,
        alias="company",
    )

    customer: Group | None = Field(
        default=None,
        alias="customer",
    )

    customers: list[Group] | None = Field(
        default=None,
        alias="customers",
    )

    description: str | None = Field(
        default=None,
        alias="description",
    )

    floor_plans: list[FloorPlan] | None = Field(
        default=None,
        alias="floor_plans",
    )

    id: str | None = Field(
        default=None,
        alias="id",
    )

    images: list[Image] | None = Field(
        default=None,
        alias="images",
    )

    list_agent: Group | None = Field(
        default=None,
        alias="list_agent",
    )

    lot: ListingLot | None = Field(
        default=None,
        alias="lot",
    )

    mls_number: str | None = Field(
        default=None,
        alias="mls_number",
    )

    object: ListingMarketingContentObjectEnum | None = Field(
        default=None,
        alias="object",
    )

    price: ListingPrice | None = Field(
        default=None,
        alias="price",
    )

    status: ListingMarketingContentStatusEnum | None = Field(
        default=...,
        alias="status",
    )

    sub_type: ListingMarketingContentSubTypeEnum | None = Field(
        default=None,
        alias="sub_type",
    )

    vendor: Group | None = Field(
        default=None,
        alias="vendor",
    )


class ListingMarketingContentResource(BaseModel):
    """Aryeo API schema for `#/components/schemas/ListingMarketingContentResource`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: ListingMarketingContent | None = Field(
        default=None,
        alias="data",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class ListingPostPayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/ListingPostPayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    address_id: str = Field(
        default=...,
        alias="address_id",
    )

    co_list_agent_id: str | None = Field(
        default=None,
        alias="co_list_agent_id",
    )

    list_agent_id: str | None = Field(
        default=None,
        alias="list_agent_id",
    )

    order_ids: list[str] | None = Field(
        default=None,
        alias="order_ids",
    )

    sections: dict[str, JSONValue] | None = Field(
        default=None,
        alias="sections",
    )


class ListingPrice(BaseModel):
    """Aryeo API schema for `#/components/schemas/ListingPrice`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    list_price: int | None = Field(
        default=None,
        alias="list_price",
    )

    list_price_formatted: str | None = Field(
        default=None,
        alias="list_price_formatted",
    )


class ListingPutPayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/ListingPutPayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    address_id: str | None = Field(
        default=None,
        alias="address_id",
    )

    bathrooms: float | None = Field(
        default=None,
        alias="bathrooms",
    )

    bedrooms: float | None = Field(
        default=None,
        alias="bedrooms",
    )

    description: str | None = Field(
        default=None,
        alias="description",
    )

    home_squarefootage: float | None = Field(
        default=None,
        alias="home_squarefootage",
    )

    is_draft: bool | None = Field(
        default=None,
        alias="is_draft",
    )

    is_showcase: bool | None = Field(
        default=None,
        alias="is_showcase",
    )

    lot_acres: float | None = Field(
        default=None,
        alias="lot_acres",
    )

    mls_live_date: str | None = Field(
        default=None,
        alias="mls_live_date",
    )

    mls_number: str | None = Field(
        default=None,
        alias="mls_number",
    )

    parking_spots: float | None = Field(
        default=None,
        alias="parking_spots",
    )

    price: int | None = Field(
        default=None,
        alias="price",
    )

    property_type: ListingPutPayloadPropertyTypeEnum | None = Field(
        default=None,
        alias="property_type",
    )

    status: str | None = Field(
        default=None,
        alias="status",
    )

    title: str | None = Field(
        default=None,
        alias="title",
    )

    year_built: int | None = Field(
        default=None,
        alias="year_built",
    )


class ListingPutShowcasePayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/ListingPutShowcasePayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    is_showcase: bool | None = Field(
        default=None,
        alias="is_showcase",
    )


class ListingResource(BaseModel):
    """Aryeo API schema for `#/components/schemas/ListingResource`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: Listing | None = Field(
        default=None,
        alias="data",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class ListingStats(BaseModel):
    """Aryeo API schema for `#/components/schemas/ListingStats`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    all_referrers: list[str] | None = Field(
        default=None,
        alias="allReferrers",
    )

    avg_time_on_page: JSONValue | None = Field(
        default=None,
        alias="avgTimeOnPage",
    )

    top_referrer: str | None = Field(
        default=None,
        alias="topReferrer",
    )

    total_users: JSONValue | None = Field(
        default=None,
        alias="totalUsers",
    )

    total_views: JSONValue | None = Field(
        default=None,
        alias="totalViews",
    )


class ListingStatsResource(BaseModel):
    """Aryeo API schema for `#/components/schemas/ListingStatsResource`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    main_listing_stats: ListingStats = Field(
        default=...,
        alias="main_listing_stats",
    )


class LoginPostPayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/LoginPostPayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    client: LoginPostPayloadClientEnum = Field(
        default=...,
        alias="client",
    )

    company_id: str | None = Field(
        default=None,
        alias="company_id",
    )

    email: str = Field(
        default=...,
        alias="email",
    )

    password: str = Field(
        default=...,
        alias="password",
    )


class LoginViaTokenPostPayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/LoginViaTokenPostPayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    client: LoginViaTokenPostPayloadClientEnum = Field(
        default=...,
        alias="client",
    )


class MarketingMaterial(BaseModel):
    """Aryeo API schema for `#/components/schemas/MarketingMaterial`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    exports: list[Export] | None = Field(
        default=None,
        alias="exports",
    )

    id: str | None = Field(
        default=None,
        alias="id",
    )

    json_updated_at: float | None = Field(
        default=None,
        alias="json_updated_at",
    )

    listing_download_hash: str | None = Field(
        default=None,
        alias="listing_download_hash",
    )

    name: str | None = Field(
        default=None,
        alias="name",
    )

    object: MarketingMaterialObjectEnum | None = Field(
        default=None,
        alias="object",
    )

    polotno_json: PolotnoJson | None = Field(
        default=None,
        alias="polotno_json",
    )

    published_at: str | None = Field(
        default=None,
        alias="published_at",
    )

    thumbnail_url: str | None = Field(
        default=None,
        alias="thumbnail_url",
    )


class MarketingMaterialCategory(BaseModel):
    """Aryeo API schema for `#/components/schemas/MarketingMaterialCategory`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id: str = Field(
        default=...,
        alias="id",
    )

    name: str = Field(
        default=...,
        alias="name",
    )

    slug: str = Field(
        default=...,
        alias="slug",
    )


class MarketingMaterialPublishPayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/MarketingMaterialPublishPayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    polotno_json: str | None = Field(
        default=None,
        alias="polotno_json",
    )


class MarketingMaterialResource(BaseModel):
    """Aryeo API schema for `#/components/schemas/MarketingMaterialResource`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: MarketingMaterial | None = Field(
        default=None,
        alias="data",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class MarketingMaterialStorePayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/MarketingMaterialStorePayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    app_version: str | None = Field(
        default=None,
        alias="app_version",
    )

    listing_id: str = Field(
        default=...,
        alias="listing_id",
    )

    name: str | None = Field(
        default=None,
        alias="name",
    )

    polotno_json: str | None = Field(
        default=None,
        alias="polotno_json",
    )

    template_id: str | None = Field(
        default=None,
        alias="template_id",
    )


class MarketingMaterialTemplate(BaseModel):
    """Aryeo API schema for `#/components/schemas/MarketingMaterialTemplate`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    categories: list[MarketingMaterialCategory] | None = Field(
        default=None,
        alias="categories",
    )

    created_at: str | None = Field(
        default=None,
        alias="created_at",
    )

    customer_groups: list[Group] | None = Field(
        default=None,
        alias="customer_groups",
    )

    draft_polotno_json: PolotnoJson | None = Field(
        default=None,
        alias="draft_polotno_json",
    )

    group: Group | None = Field(
        default=None,
        alias="group",
    )

    id: str = Field(
        default=...,
        alias="id",
    )

    is_featured: bool | None = Field(
        default=None,
        alias="is_featured",
    )

    name: str = Field(
        default=...,
        alias="name",
    )

    object: MarketingMaterialTemplateObjectEnum | None = Field(
        default=None,
        alias="object",
    )

    polotno_json: PolotnoJson | None = Field(
        default=None,
        alias="polotno_json",
    )

    preview_image_url: str | None = Field(
        default=None,
        alias="preview_image_url",
    )


class MarketingMaterialTemplateCollection(BaseModel):
    """Aryeo API schema for `#/components/schemas/MarketingMaterialTemplateCollection`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: list[MarketingMaterialTemplate] | None = Field(
        default=None,
        alias="data",
    )

    links: PaginationLinks | None = Field(
        default=None,
        alias="links",
    )

    meta: PaginationMeta | None = Field(
        default=None,
        alias="meta",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class MarketingMaterialTemplatePublishPayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/MarketingMaterialTemplatePublishPayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    polotno_json: str | None = Field(
        default=None,
        alias="polotno_json",
    )


class MarketingMaterialTemplateResource(BaseModel):
    """Aryeo API schema for `#/components/schemas/MarketingMaterialTemplateResource`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: MarketingMaterialTemplate | None = Field(
        default=None,
        alias="data",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class MarketingMaterialTemplateStorePayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/MarketingMaterialTemplateStorePayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    draft_polotno_json: str | None = Field(
        default=None,
        alias="draft_polotno_json",
    )

    group_id: str | None = Field(
        default=None,
        alias="group_id",
    )

    name: str | None = Field(
        default=None,
        alias="name",
    )

    polotno_json: str | None = Field(
        default=None,
        alias="polotno_json",
    )


class MarketingMaterialTemplateUpdatePayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/MarketingMaterialTemplateUpdatePayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    app_version: str | None = Field(
        default=None,
        alias="app_version",
    )

    category_ids: list[str] | None = Field(
        default=None,
        alias="category_ids",
    )

    draft_polotno_json: str | None = Field(
        default=None,
        alias="draft_polotno_json",
    )

    name: str | None = Field(
        default=None,
        alias="name",
    )

    polotno_json: str | None = Field(
        default=None,
        alias="polotno_json",
    )


class MarketingMaterialUpdatePayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/MarketingMaterialUpdatePayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    app_version: str | None = Field(
        default=None,
        alias="app_version",
    )

    draft_polotno_json: str | None = Field(
        default=None,
        alias="draft_polotno_json",
    )

    name: str | None = Field(
        default=None,
        alias="name",
    )

    polotno_json: str | None = Field(
        default=None,
        alias="polotno_json",
    )


class MePasswordPutPayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/MePasswordPutPayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    current_password: str = Field(
        default=...,
        alias="current_password",
    )

    new_password: str = Field(
        default=...,
        alias="new_password",
    )

    new_password_confirmation: str = Field(
        default=...,
        alias="new_password_confirmation",
    )


class MediaRequestMediaSearchPayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/MediaRequestMediaSearchPayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    search: str | None = Field(
        default=None,
        alias="search",
    )

    suggested: bool | None = Field(
        default=None,
        alias="suggested",
    )


class MediaSearchResource(BaseModel):
    """Aryeo API schema for `#/components/schemas/MediaSearchResource`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: dict[str, JSONValue] | None = Field(
        default=None,
        alias="data",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class NotificationPreference(BaseModel):
    """Aryeo API schema for `#/components/schemas/NotificationPreference`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    channels: list[NotificationPreferenceChannelsEnum] = Field(
        default=...,
        alias="channels",
    )

    email: bool = Field(
        default=...,
        alias="email",
    )

    in_app: bool = Field(
        default=...,
        alias="in_app",
    )

    notification_type: NotificationPreferenceNotificationTypeEnum = Field(
        default=...,
        alias="notification_type",
    )

    object: NotificationPreferenceObjectEnum | None = Field(
        default=None,
        alias="object",
    )

    push: bool = Field(
        default=...,
        alias="push",
    )

    sms: bool = Field(
        default=...,
        alias="sms",
    )


class NotificationPreference2(BaseModel):
    """Aryeo API schema for `#/components/schemas/NotificationPreference-2`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    email: bool = Field(
        default=...,
        alias="email",
    )

    in_app: bool = Field(
        default=...,
        alias="in_app",
    )

    notification_type: NotificationPreference2NotificationTypeEnum = Field(
        default=...,
        alias="notification_type",
    )

    object: NotificationPreference2ObjectEnum | None = Field(
        default=None,
        alias="object",
    )

    push: bool = Field(
        default=...,
        alias="push",
    )

    sms: bool = Field(
        default=...,
        alias="sms",
    )


class NotificationPreferencesCollection(BaseModel):
    """Aryeo API schema for `#/components/schemas/NotificationPreferencesCollection`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: list[NotificationPreference] | None = Field(
        default=None,
        alias="data",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class NotificationPreferencesPutPayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/NotificationPreferencesPutPayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    preferences: list[NotificationPreference2] | None = Field(
        default=...,
        alias="preferences",
    )


class Order(BaseModel):
    """Aryeo API schema for `#/components/schemas/Order`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    address: Address | None = Field(
        default=None,
        alias="address",
    )

    appointments: list[Appointment] | None = Field(
        default=None,
        alias="appointments",
    )

    balance_amount: int | None = Field(
        default=None,
        alias="balance_amount",
    )

    booking_limits: BookingLimits | None = Field(
        default=None,
        alias="booking_limits",
    )

    created_at: str | None = Field(
        default=...,
        alias="created_at",
    )

    currency: OrderCurrencyEnum | None = Field(
        default=None,
        alias="currency",
    )

    custom_fields: list[dict[str, JSONValue]] | None = Field(
        default=None,
        alias="custom_fields",
    )

    custom_items: list[OrderItem] | None = Field(
        default=None,
        alias="custom_items",
    )

    customer: Group | None = Field(
        default=None,
        alias="customer",
    )

    customer_group: CustomerGroup | None = Field(
        default=None,
        alias="customer_group",
    )

    discounts: list[Discount] | None = Field(
        default=None,
        alias="discounts",
    )

    downloads_allowed: bool = Field(
        default=...,
        alias="downloads_allowed",
    )

    filter_by_list_price: bool | None = Field(
        default=None,
        alias="filter_by_list_price",
    )

    filter_by_square_feet: bool | None = Field(
        default=None,
        alias="filter_by_square_feet",
    )

    fulfilled_at: str | None = Field(
        default=None,
        alias="fulfilled_at",
    )

    fulfillment_status: OrderFulfillmentStatusEnum = Field(
        default=...,
        alias="fulfillment_status",
    )

    id: str = Field(
        default=...,
        alias="id",
    )

    identifier: str | None = Field(
        default=None,
        alias="identifier",
    )

    internal_notes: str | None = Field(
        default=None,
        alias="internal_notes",
    )

    invoice_url: str | None = Field(
        default=None,
        alias="invoice_url",
    )

    is_ghost: bool | None = Field(
        default=None,
        alias="is_ghost",
    )

    items: list[OrderItem] | None = Field(
        default=None,
        alias="items",
    )

    listing: Listing | None = Field(
        default=None,
        alias="listing",
    )

    number: int | None = Field(
        default=None,
        alias="number",
    )

    object: OrderObjectEnum | None = Field(
        default=None,
        alias="object",
    )

    order_form: OrderForm | None = Field(
        default=None,
        alias="order_form",
    )

    order_status: OrderOrderStatusEnum | None = Field(
        default=None,
        alias="order_status",
    )

    payment_status: OrderPaymentStatusEnum = Field(
        default=...,
        alias="payment_status",
    )

    payment_url: str | None = Field(
        default=None,
        alias="payment_url",
    )

    payments: list[Payment] | None = Field(
        default=None,
        alias="payments",
    )

    payments_allowed: bool = Field(
        default=...,
        alias="payments_allowed",
    )

    scheduling_assignment_strategy: OrderSchedulingAssignmentStrategyEnum | None = (
        Field(
            default=None,
            alias="scheduling_assignment_strategy",
        )
    )

    status: OrderStatusEnum | None = Field(
        default=None,
        alias="status",
    )

    status_url: str | None = Field(
        default=...,
        alias="status_url",
    )

    tags: list[Tag] | None = Field(
        default=None,
        alias="tags",
    )

    taxes: list[Tax] | None = Field(
        default=None,
        alias="taxes",
    )

    title: str = Field(
        default=...,
        alias="title",
    )

    total_amount: int | None = Field(
        default=None,
        alias="total_amount",
    )

    total_discount_amount: int | None = Field(
        default=None,
        alias="total_discount_amount",
    )

    total_tax_amount: int | None = Field(
        default=None,
        alias="total_tax_amount",
    )

    unconfirmed_appointments: list[Appointment] | None = Field(
        default=None,
        alias="unconfirmed_appointments",
    )

    updated_at: str | None = Field(
        default=...,
        alias="updated_at",
    )


class OrderBillingAddressPutPayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/OrderBillingAddressPutPayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    city: str | None = Field(
        default=None,
        alias="city",
    )

    city_region: str | None = Field(
        default=None,
        alias="city_region",
    )

    county_or_parish: str | None = Field(
        default=None,
        alias="county_or_parish",
    )

    latitude: float | None = Field(
        default=None,
        alias="latitude",
    )

    longitude: float | None = Field(
        default=None,
        alias="longitude",
    )

    postal_code: str | None = Field(
        default=None,
        alias="postal_code",
    )

    state_or_province: str | None = Field(
        default=None,
        alias="state_or_province",
    )

    state_or_province_region: str | None = Field(
        default=None,
        alias="state_or_province_region",
    )

    street_name: str | None = Field(
        default=None,
        alias="street_name",
    )

    street_number: str | None = Field(
        default=None,
        alias="street_number",
    )

    unit_number: str | None = Field(
        default=None,
        alias="unit_number",
    )


class OrderCollection(BaseModel):
    """Aryeo API schema for `#/components/schemas/OrderCollection`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: list[Order] | None = Field(
        default=None,
        alias="data",
    )

    links: PaginationLinks | None = Field(
        default=None,
        alias="links",
    )

    meta: PaginationMeta | None = Field(
        default=None,
        alias="meta",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class OrderForm(BaseModel):
    """Aryeo API schema for `#/components/schemas/OrderForm`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    automated_user_assignment_strategy: (
        OrderFormAutomatedUserAssignmentStrategyEnum | None
    ) = Field(
        default=None,
        alias="automated_user_assignment_strategy",
    )

    availability_style: OrderFormAvailabilityStyleEnum | None = Field(
        default=None,
        alias="availability_style",
    )

    company: Group | None = Field(
        default=None,
        alias="company",
    )

    form_settings: dict[str, JSONValue] | None = Field(
        default=None,
        alias="form_settings",
    )

    id: str = Field(
        default=...,
        alias="id",
    )

    is_public: bool | None = Field(
        default=None,
        alias="is_public",
    )

    object: OrderFormObjectEnum | None = Field(
        default=None,
        alias="object",
    )

    owner: Group | None = Field(
        default=None,
        alias="owner",
    )

    require_upfront_payment: bool | None = Field(
        default=None,
        alias="require_upfront_payment",
    )

    show_user_names: bool | None = Field(
        default=None,
        alias="show_user_names",
    )

    slot_interval_minutes: int | None = Field(
        default=None,
        alias="slot_interval_minutes",
    )

    thumbnail_url: str | None = Field(
        default=None,
        alias="thumbnail_url",
    )

    title: str = Field(
        default=...,
        alias="title",
    )

    type: OrderFormTypeEnum = Field(
        default=...,
        alias="type",
    )

    upfront_payment_percentage: int | None = Field(
        default=None,
        alias="upfront_payment_percentage",
    )

    url: str = Field(
        default=...,
        alias="url",
    )

    use_automated_user_assignment: bool | None = Field(
        default=None,
        alias="use_automated_user_assignment",
    )

    use_instant_appointment_scheduling: bool | None = Field(
        default=None,
        alias="use_instant_appointment_scheduling",
    )

    use_territory_awareness: bool | None = Field(
        default=None,
        alias="use_territory_awareness",
    )


class OrderFormCollection(BaseModel):
    """Aryeo API schema for `#/components/schemas/OrderFormCollection`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: list[OrderForm] | None = Field(
        default=None,
        alias="data",
    )

    links: PaginationLinks | None = Field(
        default=None,
        alias="links",
    )

    meta: PaginationMeta | None = Field(
        default=None,
        alias="meta",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class OrderFormSession(BaseModel):
    """Aryeo API schema for `#/components/schemas/OrderFormSession`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    address: Address | None = Field(
        default=None,
        alias="address",
    )

    coupons: list[Coupon] | None = Field(
        default=None,
        alias="coupons",
    )

    customer: Group | None = Field(
        default=None,
        alias="customer",
    )

    id: str = Field(
        default=...,
        alias="id",
    )

    object: OrderFormSessionObjectEnum | None = Field(
        default=None,
        alias="object",
    )

    order_form: OrderForm | None = Field(
        default=None,
        alias="order_form",
    )

    product_filters: dict[str, JSONValue] | None = Field(
        default=None,
        alias="product_filters",
    )

    show_header: bool | None = Field(
        default=None,
        alias="show_header",
    )

    step_visibility: dict[str, JSONValue] | None = Field(
        default=None,
        alias="step_visibility",
    )

    success_url: str | None = Field(
        default=None,
        alias="success_url",
    )

    url: str | None = Field(
        default=None,
        alias="url",
    )


class OrderFormSessionPostPayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/OrderFormSessionPostPayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    address_data: dict[str, JSONValue] | None = Field(
        default=None,
        alias="address_data",
    )

    address_id: str | None = Field(
        default=None,
        alias="address_id",
    )

    coupon_ids: list[str] | None = Field(
        default=None,
        alias="coupon_ids",
    )

    customer_data: dict[str, JSONValue] | None = Field(
        default=None,
        alias="customer_data",
    )

    customer_group_id: str | None = Field(
        default=None,
        alias="customer_group_id",
    )

    customer_id: str | None = Field(
        default=None,
        alias="customer_id",
    )

    order_form_id: str = Field(
        default=...,
        alias="order_form_id",
    )

    step_visibility: dict[str, JSONValue] | None = Field(
        default=None,
        alias="step_visibility",
    )

    success_url: str | None = Field(
        default=None,
        alias="success_url",
    )


class OrderFormSessionResource(BaseModel):
    """Aryeo API schema for `#/components/schemas/OrderFormSessionResource`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: OrderFormSession | None = Field(
        default=None,
        alias="data",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class OrderItem(BaseModel):
    """Aryeo API schema for `#/components/schemas/OrderItem`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    amount: int | None = Field(
        default=None,
        alias="amount",
    )

    appointment: Appointment | None = Field(
        default=None,
        alias="appointment",
    )

    description: str | None = Field(
        default=None,
        alias="description",
    )

    discounts: list[DiscountAmount] | None = Field(
        default=None,
        alias="discounts",
    )

    gross_total_amount: int | None = Field(
        default=None,
        alias="gross_total_amount",
    )

    id: str = Field(
        default=...,
        alias="id",
    )

    is_canceled: bool | None = Field(
        default=None,
        alias="is_canceled",
    )

    is_serviceable: bool | None = Field(
        default=None,
        alias="is_serviceable",
    )

    object: OrderItemObjectEnum | None = Field(
        default=None,
        alias="object",
    )

    order: Order | None = Field(
        default=None,
        alias="order",
    )

    product: Product | None = Field(
        default=None,
        alias="product",
    )

    product_variant: ProductVariant | None = Field(
        default=None,
        alias="product_variant",
    )

    purchasable_type: OrderItemPurchasableTypeEnum | None = Field(
        default=None,
        alias="purchasable_type",
    )

    quantity: int | None = Field(
        default=None,
        alias="quantity",
    )

    sub_title: str | None = Field(
        default=None,
        alias="sub_title",
    )

    subtitle: str | None = Field(
        default=None,
        alias="subtitle",
    )

    tasks: list[Task] | None = Field(
        default=None,
        alias="tasks",
    )

    taxes: list[Tax] | None = Field(
        default=None,
        alias="taxes",
    )

    title: str | None = Field(
        default=None,
        alias="title",
    )

    unit_price_amount: int | None = Field(
        default=None,
        alias="unit_price_amount",
    )


class OrderItemGrouping(BaseModel):
    """Aryeo API schema for `#/components/schemas/OrderItemGrouping`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    company_team_members: list[CompanyTeamMember] = Field(
        default=...,
        alias="company_team_members",
    )

    duration: int = Field(
        default=...,
        alias="duration",
    )

    items: list[OrderItem] = Field(
        default=...,
        alias="items",
    )

    object: str | None = Field(
        default=None,
        alias="object",
    )

    products: list[Product] = Field(
        default=...,
        alias="products",
    )

    users: list[User] = Field(
        default=...,
        alias="users",
    )


class OrderItemGroupingCollection(BaseModel):
    """Aryeo API schema for `#/components/schemas/OrderItemGroupingCollection`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: list[OrderItemGrouping] | None = Field(
        default=...,
        alias="data",
    )

    links: PaginationLinks | None = Field(
        default=None,
        alias="links",
    )

    meta: PaginationMeta | None = Field(
        default=None,
        alias="meta",
    )

    status: str | None = Field(
        default=None,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class OrderItemPayRunItemDefaults(BaseModel):
    """Aryeo API schema for `#/components/schemas/OrderItemPayRunItemDefaults`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    amount: float = Field(
        default=...,
        alias="amount",
    )

    company_team_member: CompanyTeamMember = Field(
        default=...,
        alias="company_team_member",
    )

    order_item_id: str = Field(
        default=...,
        alias="order_item_id",
    )

    title: str = Field(
        default=...,
        alias="title",
    )


class OrderItemPostPayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/OrderItemPostPayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    appointment_id: str | None = Field(
        default=None,
        alias="appointment_id",
    )

    assigned_company_team_member_id: str | None = Field(
        default=None,
        alias="assigned_company_team_member_id",
    )

    description: str | None = Field(
        default=None,
        alias="description",
    )

    order_id: str = Field(
        default=...,
        alias="order_id",
    )

    product_variant_id: str | None = Field(
        default=None,
        alias="product_variant_id",
    )

    quantity: int | None = Field(
        default=None,
        alias="quantity",
    )

    subtitle: str | None = Field(
        default=None,
        alias="subtitle",
    )

    title: str | None = Field(
        default=None,
        alias="title",
    )

    unit_price_amount: int | None = Field(
        default=None,
        alias="unit_price_amount",
    )


class OrderItemResource(BaseModel):
    """Aryeo API schema for `#/components/schemas/OrderItemResource`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: OrderItem | None = Field(
        default=None,
        alias="data",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class OrderNotesPutPayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/OrderNotesPutPayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    internal_notes: str | None = Field(
        default=None,
        alias="internal_notes",
    )


class OrderPayment(BaseModel):
    """Aryeo API schema for `#/components/schemas/OrderPayment`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    applicable_amount: int = Field(
        default=...,
        alias="applicable_amount",
    )

    collected_amount: int = Field(
        default=...,
        alias="collected_amount",
    )

    collection_source: str | None = Field(
        default=...,
        alias="collection_source",
    )

    completed_at: str = Field(
        default=...,
        alias="completed_at",
    )

    id: str = Field(
        default=...,
        alias="id",
    )

    object: OrderPaymentObjectEnum | None = Field(
        default=None,
        alias="object",
    )

    order: Order | None = Field(
        default=None,
        alias="order",
    )

    tip_amount: int = Field(
        default=...,
        alias="tip_amount",
    )

    total_amount: int = Field(
        default=...,
        alias="total_amount",
    )

    type: OrderPaymentTypeEnum = Field(
        default=...,
        alias="type",
    )


class OrderPostPayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/OrderPostPayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    address_id: str | None = Field(
        default=None,
        alias="address_id",
    )

    allow_payments_before_fulfillment: bool | None = Field(
        default=None,
        alias="allow_payments_before_fulfillment",
    )

    company_id: str | None = Field(
        default=None,
        alias="company_id",
    )

    customer_id: str | None = Field(
        default=None,
        alias="customer_id",
    )

    customer_team_membership_id: str | None = Field(
        default=None,
        alias="customer_team_membership_id",
    )

    fulfillment_status: OrderPostPayloadFulfillmentStatusEnum | None = Field(
        default=None,
        alias="fulfillment_status",
    )

    internal_notes: str | None = Field(
        default=None,
        alias="internal_notes",
    )

    listing_id: str | None = Field(
        default=None,
        alias="listing_id",
    )

    lock_download_for_payment: bool | None = Field(
        default=None,
        alias="lock_download_for_payment",
    )

    notify: bool | None = Field(
        default=None,
        alias="notify",
    )

    product_items: list[dict[str, JSONValue]] | None = Field(
        default=None,
        alias="product_items",
    )


class OrderRefund(BaseModel):
    """Aryeo API schema for `#/components/schemas/OrderRefund`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    amount: int = Field(
        default=...,
        alias="amount",
    )

    company_team_member: CompanyTeamMember | None = Field(
        default=None,
        alias="company_team_member",
    )

    completed_at: str = Field(
        default=...,
        alias="completed_at",
    )

    currency: str = Field(
        default=...,
        alias="currency",
    )

    description: str | None = Field(
        default=...,
        alias="description",
    )

    id: str = Field(
        default=...,
        alias="id",
    )

    object: OrderRefundObjectEnum | None = Field(
        default=None,
        alias="object",
    )

    order_payment: OrderPayment = Field(
        default=...,
        alias="order_payment",
    )

    payment_integration: PaymentGateway | None = Field(
        default=None,
        alias="payment_integration",
    )

    reason: OrderRefundReasonEnum = Field(
        default=...,
        alias="reason",
    )

    tip_amount: int = Field(
        default=...,
        alias="tip_amount",
    )

    total_amount: int = Field(
        default=...,
        alias="total_amount",
    )


class OrderRefundPostPayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/OrderRefundPostPayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    amount: int = Field(
        default=...,
        alias="amount",
    )

    date: str = Field(
        default=...,
        alias="date",
    )

    description: str | None = Field(
        default=None,
        alias="description",
    )

    reason: OrderRefundPostPayloadReasonEnum = Field(
        default=...,
        alias="reason",
    )

    tip_amount: int = Field(
        default=...,
        alias="tip_amount",
    )


class OrderRefundResource(BaseModel):
    """Aryeo API schema for `#/components/schemas/OrderRefundResource`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: OrderRefund | None = Field(
        default=None,
        alias="data",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class OrderResource(BaseModel):
    """Aryeo API schema for `#/components/schemas/OrderResource`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: Order | None = Field(
        default=None,
        alias="data",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class OrderTagsPostPayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/OrderTagsPostPayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    tag: dict[str, JSONValue] | None = Field(
        default=None,
        alias="tag",
    )

    tag_id: str | None = Field(
        default=None,
        alias="tag_id",
    )


class PaginationLink(BaseModel):
    """Aryeo API schema for `#/components/schemas/PaginationLink`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    active: bool = Field(
        default=...,
        alias="active",
    )

    label: str = Field(
        default=...,
        alias="label",
    )

    page: int | None = Field(
        default=None,
        alias="page",
    )

    url: str | None = Field(
        default=...,
        alias="url",
    )


class PaginationLinks(BaseModel):
    """Aryeo API schema for `#/components/schemas/PaginationLinks`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    first: str = Field(
        default=...,
        alias="first",
    )

    last: str = Field(
        default=...,
        alias="last",
    )

    next: str | None = Field(
        default=None,
        alias="next",
    )

    prev: str | None = Field(
        default=None,
        alias="prev",
    )


class PaginationMeta(BaseModel):
    """Aryeo API schema for `#/components/schemas/PaginationMeta`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    current_page: int = Field(
        default=...,
        alias="current_page",
    )

    from_value: int | None = Field(
        default=None,
        alias="from",
    )

    last_page: int = Field(
        default=...,
        alias="last_page",
    )

    links: list[PaginationLink] | None = Field(
        default=None,
        alias="links",
    )

    path: str = Field(
        default=...,
        alias="path",
    )

    per_page: int = Field(
        default=...,
        alias="per_page",
    )

    to: int | None = Field(
        default=None,
        alias="to",
    )

    total: int = Field(
        default=...,
        alias="total",
    )


class PayRunItemAmountOverride(BaseModel):
    """Aryeo API schema for `#/components/schemas/PayRunItemAmountOverride`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    amount: int = Field(
        default=...,
        alias="amount",
    )

    amount_type: PayRunItemAmountOverrideAmountTypeEnum = Field(
        default=...,
        alias="amount_type",
    )

    id: str = Field(
        default=...,
        alias="id",
    )

    task_template: TaskTemplate = Field(
        default=...,
        alias="task_template",
    )


class Payment(BaseModel):
    """Aryeo API schema for `#/components/schemas/Payment`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    applicable_amount: int = Field(
        default=...,
        alias="applicable_amount",
    )

    collected_amount: int = Field(
        default=...,
        alias="collected_amount",
    )

    collection_source: PaymentCollectionSourceEnum = Field(
        default=...,
        alias="collection_source",
    )

    completed_at: str | None = Field(
        default=...,
        alias="completed_at",
    )

    id: str = Field(
        default=...,
        alias="id",
    )

    object: PaymentObjectEnum = Field(
        default=...,
        alias="object",
    )

    order: Order | None = Field(
        default=None,
        alias="order",
    )

    tip_amount: int = Field(
        default=...,
        alias="tip_amount",
    )

    total_amount: int = Field(
        default=...,
        alias="total_amount",
    )

    type: PaymentTypeEnum = Field(
        default=...,
        alias="type",
    )


class PaymentGateway(BaseModel):
    """Aryeo API schema for `#/components/schemas/PaymentGateway`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id: str = Field(
        default=...,
        alias="id",
    )

    metadata: list[dict[str, JSONValue]] | None = Field(
        default=...,
        alias="metadata",
    )

    name: str = Field(
        default=...,
        alias="name",
    )

    object: PaymentGatewayObjectEnum = Field(
        default=...,
        alias="object",
    )

    provider: str = Field(
        default=...,
        alias="provider",
    )

    type: str = Field(
        default=...,
        alias="type",
    )


class PaymentInfo(BaseModel):
    """Aryeo API schema for `#/components/schemas/PaymentInfo`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    amount: int = Field(
        default=...,
        alias="amount",
    )

    can_save_card: bool = Field(
        default=...,
        alias="can_save_card",
    )

    config: PaymentInfoConfig = Field(
        default=...,
        alias="config",
    )

    currency: str = Field(
        default=...,
        alias="currency",
    )

    default_payment_gateway: PaymentGateway = Field(
        default=...,
        alias="default_payment_gateway",
    )

    default_payment_method_id: str | None = Field(
        default=...,
        alias="default_payment_method_id",
    )

    id: str = Field(
        default=...,
        alias="id",
    )

    is_authenticated: bool = Field(
        default=...,
        alias="is_authenticated",
    )

    is_tipping_enabled: bool = Field(
        default=...,
        alias="is_tipping_enabled",
    )

    object: PaymentInfoObjectEnum = Field(
        default=...,
        alias="object",
    )

    payment_gateway_is_available: bool = Field(
        default=...,
        alias="payment_gateway_is_available",
    )

    payment_methods: list[PaymentMethod] = Field(
        default=...,
        alias="payment_methods",
    )

    requires_billing_address_during_order_form_submission: bool = Field(
        default=...,
        alias="requires_billing_address_during_order_form_submission",
    )

    show_tipping_ui_expanded: bool = Field(
        default=...,
        alias="show_tipping_ui_expanded",
    )

    upfront_percentage: float = Field(
        default=...,
        alias="upfront_percentage",
    )


class PaymentInfoConfig(BaseModel):
    """Aryeo API schema for `#/components/schemas/PaymentInfoConfig`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    square_client_id: str | None = Field(
        default=...,
        alias="square_client_id",
    )

    vgs_environment: str | None = Field(
        default=...,
        alias="vgs_environment",
    )

    vgs_vault_id: str | None = Field(
        default=...,
        alias="vgs_vault_id",
    )


class PaymentInfoResource(BaseModel):
    """Aryeo API schema for `#/components/schemas/PaymentInfoResource`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: PaymentInfo = Field(
        default=...,
        alias="data",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class PaymentMethod(BaseModel):
    """Aryeo API schema for `#/components/schemas/PaymentMethod`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    brand: str = Field(
        default=...,
        alias="brand",
    )

    exp_month: int = Field(
        default=...,
        alias="exp_month",
    )

    exp_year: int = Field(
        default=...,
        alias="exp_year",
    )

    id: str = Field(
        default=...,
        alias="id",
    )

    is_expired: bool = Field(
        default=...,
        alias="is_expired",
    )

    last_4: str = Field(
        default=...,
        alias="last_4",
    )

    square_external_id: str = Field(
        default=...,
        alias="square_external_id",
    )

    stripe_external_id: str = Field(
        default=...,
        alias="stripe_external_id",
    )


class PaymentResource(BaseModel):
    """Aryeo API schema for `#/components/schemas/PaymentResource`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: Payment = Field(
        default=...,
        alias="data",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class PersonalAccessToken(BaseModel):
    """Aryeo API schema for `#/components/schemas/PersonalAccessToken`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    group: Group | None = Field(
        default=None,
        alias="group",
    )

    object: str | None = Field(
        default=None,
        alias="object",
    )

    token: str = Field(
        default=...,
        alias="token",
    )

    user: User = Field(
        default=...,
        alias="user",
    )


class PersonalAccessTokenCustomer(BaseModel):
    """Aryeo API schema for `#/components/schemas/PersonalAccessTokenCustomer`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    group: GroupCustomer | None = Field(
        default=None,
        alias="group",
    )

    object: str | None = Field(
        default=None,
        alias="object",
    )

    token: str = Field(
        default=...,
        alias="token",
    )

    user: User = Field(
        default=...,
        alias="user",
    )


class PersonalAccessTokenCustomerResource(BaseModel):
    """Aryeo API schema for `#/components/schemas/PersonalAccessTokenCustomerResource`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: PersonalAccessTokenCustomer | None = Field(
        default=None,
        alias="data",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class PersonalAccessTokenResource(BaseModel):
    """Aryeo API schema for `#/components/schemas/PersonalAccessTokenResource`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: PersonalAccessToken | None = Field(
        default=None,
        alias="data",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class PolotnoJson(BaseModel):
    """Aryeo API schema for `#/components/schemas/PolotnoJson`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    height: int = Field(
        default=...,
        alias="height",
    )

    width: int = Field(
        default=...,
        alias="width",
    )


class PortalAppColors(BaseModel):
    """Aryeo API schema for `#/components/schemas/PortalAppColors`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    dark: str | None = Field(
        default=None,
        alias="dark",
    )

    default: str | None = Field(
        default=None,
        alias="default",
    )

    light: str | None = Field(
        default=None,
        alias="light",
    )

    lightest: str | None = Field(
        default=None,
        alias="lightest",
    )

    loading_background: str | None = Field(
        default=None,
        alias="loading_background",
    )


class PortalAppConfig(BaseModel):
    """Aryeo API schema for `#/components/schemas/PortalAppConfig`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    android: AppAndroidDetails | None = Field(
        default=None,
        alias="android",
    )

    app_icon_url: str | None = Field(
        default=None,
        alias="app_icon_url",
    )

    app_name: str | None = Field(
        default=None,
        alias="app_name",
    )

    app_store: AppStoreDetails | None = Field(
        default=None,
        alias="app_store",
    )

    app_store_description: str | None = Field(
        default=None,
        alias="app_store_description",
    )

    app_store_subtitle: str | None = Field(
        default=None,
        alias="app_store_subtitle",
    )

    app_store_title: str | None = Field(
        default=None,
        alias="app_store_title",
    )

    aryeo_mobile_app_admin_account: str | None = Field(
        default=None,
        alias="aryeo_mobile_app_admin_account",
    )

    brand_color: str | None = Field(
        default=None,
        alias="brand_color",
    )

    brand_logo_url: str | None = Field(
        default=None,
        alias="brand_logo_url",
    )

    brand_name: str | None = Field(
        default=None,
        alias="brand_name",
    )

    colors: PortalAppColors | None = Field(
        default=None,
        alias="colors",
    )

    contact: PortalAppContactLegacy | None = Field(
        default=None,
        alias="contact",
    )

    contacts: list[PortalAppContact] | None = Field(
        default=None,
        alias="contacts",
    )

    dev_accounts: PortalAppDevAccounts | None = Field(
        default=None,
        alias="dev_accounts",
    )

    display_email_banner: bool | None = Field(
        default=None,
        alias="display_email_banner",
    )

    display_mobile_banner: bool | None = Field(
        default=None,
        alias="display_mobile_banner",
    )

    example_floorplan_url: str | None = Field(
        default=None,
        alias="example_floorplan_url",
    )

    example_hero_url: str | None = Field(
        default=None,
        alias="example_hero_url",
    )

    example_image_url: str | None = Field(
        default=None,
        alias="example_image_url",
    )

    example_order: PortalAppExampleOrder | None = Field(
        default=None,
        alias="example_order",
    )

    example_unparsed_address_part_one: str | None = Field(
        default=None,
        alias="example_unparsed_address_part_one",
    )

    example_unparsed_address_part_two: str | None = Field(
        default=None,
        alias="example_unparsed_address_part_two",
    )

    example_video_url: str | None = Field(
        default=None,
        alias="example_video_url",
    )

    firebase_project_number: str | None = Field(
        default=None,
        alias="firebase_project_number",
    )

    id: str = Field(
        default=...,
        alias="id",
    )

    images: PortalAppImages | None = Field(
        default=None,
        alias="images",
    )

    ios: AppIosdetails | None = Field(
        default=None,
        alias="ios",
    )

    last_revision: PortalAppRevision | None = Field(
        default=None,
        alias="last_revision",
    )

    last_revision_id: str | None = Field(
        default=None,
        alias="last_revision_id",
    )

    object: PortalAppConfigObjectEnum | None = Field(
        default=None,
        alias="object",
    )

    one_signal_app_id: str | None = Field(
        default=None,
        alias="one_signal_app_id",
    )

    one_signal_custom_app_group_name: str | None = Field(
        default=None,
        alias="one_signal_custom_app_group_name",
    )

    one_signal_rest_api_key: str | None = Field(
        default=None,
        alias="one_signal_rest_api_key",
    )

    primary_status: PortalAppConfigPrimaryStatusEnum | None = Field(
        default=None,
        alias="primary_status",
    )

    settings: PortalAppSettings | None = Field(
        default=None,
        alias="settings",
    )

    strings: PortalAppStrings | None = Field(
        default=None,
        alias="strings",
    )

    testing_user_email: str | None = Field(
        default=None,
        alias="testing_user_email",
    )

    updated_at: str | None = Field(
        default=None,
        alias="updated_at",
    )

    vendor: Group | None = Field(
        default=None,
        alias="vendor",
    )


class PortalAppConfigPutPayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/PortalAppConfigPutPayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    app_name: str | None = Field(
        default=None,
        alias="app_name",
    )

    app_store_name: str | None = Field(
        default=None,
        alias="app_store_name",
    )

    app_store_subtitle: str | None = Field(
        default=None,
        alias="app_store_subtitle",
    )

    aryeo_mobile_app_admin_account: str | None = Field(
        default=None,
        alias="aryeo_mobile_app_admin_account",
    )

    bundle_id: str | None = Field(
        default=None,
        alias="bundle_id",
    )

    contact_name: str | None = Field(
        default=None,
        alias="contact_name",
    )

    description: str | None = Field(
        default=None,
        alias="description",
    )

    firebase_project_number: str | None = Field(
        default=None,
        alias="firebase_project_number",
    )

    itunes_app_id: str | None = Field(
        default=None,
        alias="itunes_app_id",
    )

    keywords: str | None = Field(
        default=None,
        alias="keywords",
    )

    marketing_url: str | None = Field(
        default=None,
        alias="marketing_url",
    )

    one_signal_app_id: str | None = Field(
        default=None,
        alias="one_signal_app_id",
    )

    one_signal_custom_app_group_name: str | None = Field(
        default=None,
        alias="one_signal_custom_app_group_name",
    )

    one_signal_rest_api_key: str | None = Field(
        default=None,
        alias="one_signal_rest_api_key",
    )

    package_name: str | None = Field(
        default=None,
        alias="package_name",
    )

    primary_status: PortalAppConfigPutPayloadPrimaryStatusEnum | None = Field(
        default=None,
        alias="primary_status",
    )

    short_description: str | None = Field(
        default=None,
        alias="short_description",
    )

    support_url: str | None = Field(
        default=None,
        alias="support_url",
    )


class PortalAppConfigResource(BaseModel):
    """Aryeo API schema for `#/components/schemas/PortalAppConfigResource`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: PortalAppConfig | None = Field(
        default=None,
        alias="data",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class PortalAppContact(BaseModel):
    """Aryeo API schema for `#/components/schemas/PortalAppContact`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    call: str | None = Field(
        default=None,
        alias="call",
    )

    email: str | None = Field(
        default=None,
        alias="email",
    )

    id: str | None = Field(
        default=None,
        alias="id",
    )

    link: str | None = Field(
        default=None,
        alias="link",
    )

    link_title: str | None = Field(
        default=None,
        alias="link_title",
    )

    link_url: str | None = Field(
        default=None,
        alias="link_url",
    )

    text: str | None = Field(
        default=None,
        alias="text",
    )

    title: str | None = Field(
        default=None,
        alias="title",
    )


class PortalAppContactLegacy(BaseModel):
    """Aryeo API schema for `#/components/schemas/PortalAppContactLegacy`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    email: str | None = Field(
        default=None,
        alias="email",
    )

    name: str | None = Field(
        default=None,
        alias="name",
    )

    phone: str | None = Field(
        default=None,
        alias="phone",
    )


class PortalAppDevAccounts(BaseModel):
    """Aryeo API schema for `#/components/schemas/PortalAppDevAccounts`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    apple_asc_api_key_id: str | None = Field(
        default=None,
        alias="apple_asc_api_key_id",
    )

    apple_asc_api_key_issuer_id: str | None = Field(
        default=None,
        alias="apple_asc_api_key_issuer_id",
    )

    apple_asc_api_key_url: str | None = Field(
        default=None,
        alias="apple_asc_api_key_url",
    )

    apple_dev_entity_name: str | None = Field(
        default=None,
        alias="apple_dev_entity_name",
    )

    apple_dev_itc_team_id: str | None = Field(
        default=None,
        alias="apple_dev_itc_team_id",
    )

    apple_dev_team_id: str | None = Field(
        default=None,
        alias="apple_dev_team_id",
    )

    google_dev_account_name: str | None = Field(
        default=None,
        alias="google_dev_account_name",
    )

    google_dev_id: str | None = Field(
        default=None,
        alias="google_dev_id",
    )


class PortalAppExampleOrder(BaseModel):
    """Aryeo API schema for `#/components/schemas/PortalAppExampleOrder`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    image_url: str | None = Field(
        default=None,
        alias="image_url",
    )

    latitude: float | None = Field(
        default=None,
        alias="latitude",
    )

    longitude: float | None = Field(
        default=None,
        alias="longitude",
    )

    unparsed_address_part_one: str | None = Field(
        default=None,
        alias="unparsed_address_part_one",
    )

    unparsed_address_part_two: str | None = Field(
        default=None,
        alias="unparsed_address_part_two",
    )


class PortalAppImages(BaseModel):
    """Aryeo API schema for `#/components/schemas/PortalAppImages`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    app_icon_url: str | None = Field(
        default=None,
        alias="app_icon_url",
    )

    hero_url: str | None = Field(
        default=None,
        alias="hero_url",
    )

    logo_url: str | None = Field(
        default=None,
        alias="logo_url",
    )


class PortalAppRevision(BaseModel):
    """Aryeo API schema for `#/components/schemas/PortalAppRevision`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    changes: list[dict[str, JSONValue]] = Field(
        default=...,
        alias="changes",
    )

    created_at: str = Field(
        default=...,
        alias="created_at",
    )

    id: str = Field(
        default=...,
        alias="id",
    )

    object: PortalAppRevisionObjectEnum = Field(
        default=...,
        alias="object",
    )

    screenshots: list[dict[str, JSONValue]] = Field(
        default=...,
        alias="screenshots",
    )

    screenshots_ready_at: str | None = Field(
        default=...,
        alias="screenshots_ready_at",
    )

    screenshots_started_at: str | None = Field(
        default=...,
        alias="screenshots_started_at",
    )

    updated_at: str = Field(
        default=...,
        alias="updated_at",
    )

    version: str = Field(
        default=...,
        alias="version",
    )


class PortalAppSettings(BaseModel):
    """Aryeo API schema for `#/components/schemas/PortalAppSettings`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    external_form_domain_whitelist: str | None = Field(
        default=None,
        alias="external_form_domain_whitelist",
    )


class PortalAppStrings(BaseModel):
    """Aryeo API schema for `#/components/schemas/PortalAppStrings`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    headline: str | None = Field(
        default=None,
        alias="headline",
    )


class PortalCustomerJoinPostPayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/PortalCustomerJoinPostPayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    creator_group_id: str | None = Field(
        default=None,
        alias="creator_group_id",
    )


class PortalCustomerRegisterPostPayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/PortalCustomerRegisterPostPayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    client: PortalCustomerRegisterPostPayloadClientEnum = Field(
        default=...,
        alias="client",
    )

    creator_group_id: str = Field(
        default=...,
        alias="creator_group_id",
    )

    email: str = Field(
        default=...,
        alias="email",
    )

    first_name: str = Field(
        default=...,
        alias="first_name",
    )

    last_name: str = Field(
        default=...,
        alias="last_name",
    )

    password: str = Field(
        default=...,
        alias="password",
    )

    password_confirmation: str = Field(
        default=...,
        alias="password_confirmation",
    )

    phone: str | None = Field(
        default=None,
        alias="phone",
    )


class PortalCustomerVerifyPostPayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/PortalCustomerVerifyPostPayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    client: PortalCustomerVerifyPostPayloadClientEnum = Field(
        default=...,
        alias="client",
    )

    company_id: str = Field(
        default=...,
        alias="company_id",
    )

    email: str = Field(
        default=...,
        alias="email",
    )

    password: str = Field(
        default=...,
        alias="password",
    )

    password_confirmation: str = Field(
        default=...,
        alias="password_confirmation",
    )

    verification_code: str = Field(
        default=...,
        alias="verification_code",
    )


class Product(BaseModel):
    """Aryeo API schema for `#/components/schemas/Product`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    active: bool | None = Field(
        default=None,
        alias="active",
    )

    always_display_addons: bool | None = Field(
        default=None,
        alias="always_display_addons",
    )

    avalara_tax_code: str | None = Field(
        default=None,
        alias="avalara_tax_code",
    )

    categories: list[ProductCategory] | None = Field(
        default=None,
        alias="categories",
    )

    description: str | None = Field(
        default=None,
        alias="description",
    )

    id: str = Field(
        default=...,
        alias="id",
    )

    image_url: str | None = Field(
        default=None,
        alias="image_url",
    )

    is_esoft_adjustment: bool | None = Field(
        default=None,
        alias="is_esoft_adjustment",
    )

    is_filterable: bool | None = Field(
        default=None,
        alias="is_filterable",
    )

    is_serviceable: bool | None = Field(
        default=None,
        alias="is_serviceable",
    )

    is_twilight: bool | None = Field(
        default=None,
        alias="is_twilight",
    )

    limit_quantity: bool | None = Field(
        default=None,
        alias="limit_quantity",
    )

    limit_quantity_amount: int | None = Field(
        default=None,
        alias="limit_quantity_amount",
    )

    object: ProductObjectEnum | None = Field(
        default=None,
        alias="object",
    )

    requires_separate_booking: bool | None = Field(
        default=None,
        alias="requires_separate_booking",
    )

    tags: list[ProductCategory] | None = Field(
        default=None,
        alias="tags",
    )

    title: str = Field(
        default=...,
        alias="title",
    )

    type: ProductTypeEnum = Field(
        default=...,
        alias="type",
    )

    variant_filter_type: str | None = Field(
        default=None,
        alias="variant_filter_type",
    )

    variants: list[ProductVariant] | None = Field(
        default=None,
        alias="variants",
    )


class ProductCategory(BaseModel):
    """Aryeo API schema for `#/components/schemas/ProductCategory`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    color: str | None = Field(
        default=None,
        alias="color",
    )

    id: str = Field(
        default=...,
        alias="id",
    )

    name: str | None = Field(
        default=None,
        alias="name",
    )

    object: ProductCategoryObjectEnum | None = Field(
        default=None,
        alias="object",
    )

    slug: str | None = Field(
        default=None,
        alias="slug",
    )

    title: str = Field(
        default=...,
        alias="title",
    )

    type: str | None = Field(
        default=None,
        alias="type",
    )


class ProductCategoryCollection(BaseModel):
    """Aryeo API schema for `#/components/schemas/ProductCategoryCollection`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: list[ProductCategory] | None = Field(
        default=None,
        alias="data",
    )

    links: PaginationLinks | None = Field(
        default=None,
        alias="links",
    )

    meta: PaginationMeta | None = Field(
        default=None,
        alias="meta",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class ProductCollection(BaseModel):
    """Aryeo API schema for `#/components/schemas/ProductCollection`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: list[Product] | None = Field(
        default=None,
        alias="data",
    )

    links: PaginationLinks | None = Field(
        default=None,
        alias="links",
    )

    meta: PaginationMeta | None = Field(
        default=None,
        alias="meta",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class ProductResource(BaseModel):
    """Aryeo API schema for `#/components/schemas/ProductResource`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: Product | None = Field(
        default=None,
        alias="data",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class ProductVariant(BaseModel):
    """Aryeo API schema for `#/components/schemas/ProductVariant`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    base_is_hidden: bool | None = Field(
        default=None,
        alias="base_is_hidden",
    )

    base_price_amount: int | None = Field(
        default=None,
        alias="base_price_amount",
    )

    display_original_price: bool | None = Field(
        default=None,
        alias="display_original_price",
    )

    duration: int | None = Field(
        default=None,
        alias="duration",
    )

    id: str = Field(
        default=...,
        alias="id",
    )

    object: ProductVariantObjectEnum | None = Field(
        default=None,
        alias="object",
    )

    price: int | None = Field(
        default=None,
        alias="price",
    )

    price_amount: int | None = Field(
        default=None,
        alias="price_amount",
    )

    title: str = Field(
        default=...,
        alias="title",
    )


class PromotionCode(BaseModel):
    """Aryeo API schema for `#/components/schemas/PromotionCode`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    code: str = Field(
        default=...,
        alias="code",
    )

    end_at: str | None = Field(
        default=None,
        alias="end_at",
    )

    first_time_only: bool | None = Field(
        default=None,
        alias="first_time_only",
    )

    id: str = Field(
        default=...,
        alias="id",
    )

    is_portal_mobile_app_only: bool | None = Field(
        default=None,
        alias="is_portal_mobile_app_only",
    )

    max_redemptions: int | None = Field(
        default=None,
        alias="max_redemptions",
    )

    max_redemptions_per_customer: int | None = Field(
        default=None,
        alias="max_redemptions_per_customer",
    )

    minimum_amount: int | None = Field(
        default=None,
        alias="minimum_amount",
    )

    start_at: str | None = Field(
        default=None,
        alias="start_at",
    )

    times_redeemed: int | None = Field(
        default=None,
        alias="times_redeemed",
    )


class PromotionCodeRedeemPostPayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/PromotionCodeRedeemPostPayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    code: str = Field(
        default=...,
        alias="code",
    )


class PropertyWebsite(BaseModel):
    """Aryeo API schema for `#/components/schemas/PropertyWebsite`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    branded_url: str = Field(
        default=...,
        alias="branded_url",
    )

    id: str = Field(
        default=...,
        alias="id",
    )

    unbranded_url: str = Field(
        default=...,
        alias="unbranded_url",
    )


class QuickBooksCustomer(BaseModel):
    """Aryeo API schema for `#/components/schemas/QuickBooksCustomer`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    active: bool | None = Field(
        default=None,
        alias="active",
    )

    display_name: str | None = Field(
        default=None,
        alias="display_name",
    )

    email: str | None = Field(
        default=None,
        alias="email",
    )

    id: str = Field(
        default=...,
        alias="id",
    )

    name: str | None = Field(
        default=None,
        alias="name",
    )

    object: str | None = Field(
        default=None,
        alias="object",
    )


class QuickBooksCustomerCollection(BaseModel):
    """Aryeo API schema for `#/components/schemas/QuickBooksCustomerCollection`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: list[QuickBooksCustomer] | None = Field(
        default=None,
        alias="data",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class QuickBooksItem(BaseModel):
    """Aryeo API schema for `#/components/schemas/QuickBooksItem`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    active: bool | None = Field(
        default=None,
        alias="active",
    )

    description: str | None = Field(
        default=None,
        alias="description",
    )

    display_name: str | None = Field(
        default=None,
        alias="display_name",
    )

    id: str = Field(
        default=...,
        alias="id",
    )

    name: str | None = Field(
        default=None,
        alias="name",
    )

    object: str | None = Field(
        default=None,
        alias="object",
    )

    type: str | None = Field(
        default=None,
        alias="type",
    )


class QuickBooksItemCollection(BaseModel):
    """Aryeo API schema for `#/components/schemas/QuickBooksItemCollection`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: list[QuickBooksItem] | None = Field(
        default=None,
        alias="data",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class QuickBooksItemResource(BaseModel):
    """Aryeo API schema for `#/components/schemas/QuickBooksItemResource`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: QuickBooksItem | None = Field(
        default=None,
        alias="data",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class Region(BaseModel):
    """Aryeo API schema for `#/components/schemas/Region`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    code: str = Field(
        default=...,
        alias="code",
    )

    country_code: str | None = Field(
        default=...,
        alias="country_code",
    )

    description: str | None = Field(
        default=...,
        alias="description",
    )

    id: str = Field(
        default=...,
        alias="id",
    )

    name: str = Field(
        default=...,
        alias="name",
    )

    slug: str | None = Field(
        default=...,
        alias="slug",
    )

    state_code: str | None = Field(
        default=...,
        alias="state_code",
    )

    type: RegionTypeEnum = Field(
        default=...,
        alias="type",
    )


class RegionCollection(BaseModel):
    """Aryeo API schema for `#/components/schemas/RegionCollection`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: list[Region] | None = Field(
        default=...,
        alias="data",
    )

    links: PaginationLinks | None = Field(
        default=None,
        alias="links",
    )

    meta: PaginationMeta | None = Field(
        default=None,
        alias="meta",
    )

    status: str | None = Field(
        default=None,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class Review(BaseModel):
    """Aryeo API schema for `#/components/schemas/Review`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    created_at: str = Field(
        default=...,
        alias="created_at",
    )

    id: str = Field(
        default=...,
        alias="id",
    )

    notes: str | None = Field(
        default=None,
        alias="notes",
    )

    object: str | None = Field(
        default=None,
        alias="object",
    )

    rating: float | None = Field(
        default=None,
        alias="rating",
    )

    review_campaign_id: str | None = Field(
        default=None,
        alias="review_campaign_id",
    )

    source_type: ReviewSourceTypeEnum = Field(
        default=...,
        alias="source_type",
    )

    updated_at: str = Field(
        default=...,
        alias="updated_at",
    )

    user_id: str = Field(
        default=...,
        alias="user_id",
    )


class ReviewCollection(BaseModel):
    """Aryeo API schema for `#/components/schemas/ReviewCollection`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: list[Review] | None = Field(
        default=None,
        alias="data",
    )

    links: PaginationLinks | None = Field(
        default=None,
        alias="links",
    )

    meta: PaginationMeta | None = Field(
        default=None,
        alias="meta",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class ReviewPostPayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/ReviewPostPayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    campaign_slug: str = Field(
        default=...,
        alias="campaign_slug",
    )

    notes: str | None = Field(
        default=None,
        alias="notes",
    )

    rating: float | None = Field(
        default=None,
        alias="rating",
    )

    source_type: ReviewPostPayloadSourceTypeEnum = Field(
        default=...,
        alias="source_type",
    )


class ReviewResource(BaseModel):
    """Aryeo API schema for `#/components/schemas/ReviewResource`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: Review | None = Field(
        default=None,
        alias="data",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class SavedView(BaseModel):
    """Aryeo API schema for `#/components/schemas/SavedView`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    can_edit: bool = Field(
        default=...,
        alias="can_edit",
    )

    created_at: str | None = Field(
        default=None,
        alias="created_at",
    )

    created_by: str = Field(
        default=...,
        alias="created_by",
    )

    filters: list[SavedViewFilter] | None = Field(
        default=None,
        alias="filters",
    )

    id: str = Field(
        default=...,
        alias="id",
    )

    object: SavedViewObjectEnum = Field(
        default=...,
        alias="object",
    )

    order_index: int | None = Field(
        default=None,
        alias="order_index",
    )

    owner_id: str = Field(
        default=...,
        alias="owner_id",
    )

    owner_type: SavedViewOwnerTypeEnum = Field(
        default=...,
        alias="owner_type",
    )

    scope: SavedViewScopeEnum = Field(
        default=...,
        alias="scope",
    )

    sort_by: str | None = Field(
        default=None,
        alias="sort_by",
    )

    title: str = Field(
        default=...,
        alias="title",
    )

    updated_at: str | None = Field(
        default=None,
        alias="updated_at",
    )

    view_access: SavedViewViewAccessEnum | None = Field(
        default=None,
        alias="view_access",
    )


class SavedViewCollection(BaseModel):
    """Aryeo API schema for `#/components/schemas/SavedViewCollection`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: list[SavedView] | None = Field(
        default=...,
        alias="data",
    )

    links: PaginationLinks = Field(
        default=...,
        alias="links",
    )

    meta: PaginationMeta = Field(
        default=...,
        alias="meta",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class SavedViewFilter(BaseModel):
    """Aryeo API schema for `#/components/schemas/SavedViewFilter`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    created_at: str | None = Field(
        default=None,
        alias="created_at",
    )

    id: str = Field(
        default=...,
        alias="id",
    )

    object: SavedViewFilterObjectEnum = Field(
        default=...,
        alias="object",
    )

    saved_view_id: str = Field(
        default=...,
        alias="saved_view_id",
    )

    type: SavedViewFilterTypeEnum = Field(
        default=...,
        alias="type",
    )

    updated_at: str | None = Field(
        default=None,
        alias="updated_at",
    )

    value: JSONValue = Field(
        default=...,
        alias="value",
    )


class SavedViewPatchPayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/SavedViewPatchPayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    filters: list[dict[str, JSONValue]] | None = Field(
        default=None,
        alias="filters",
    )

    owner_type: SavedViewPatchPayloadOwnerTypeEnum | None = Field(
        default=None,
        alias="owner_type",
    )

    scope: SavedViewPatchPayloadScopeEnum | None = Field(
        default=None,
        alias="scope",
    )

    sort_by: str | None = Field(
        default=None,
        alias="sort_by",
    )

    title: str | None = Field(
        default=None,
        alias="title",
    )


class SavedViewPostPayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/SavedViewPostPayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    filters: list[dict[str, JSONValue]] | None = Field(
        default=None,
        alias="filters",
    )

    owner_type: SavedViewPostPayloadOwnerTypeEnum = Field(
        default=...,
        alias="owner_type",
    )

    scope: SavedViewPostPayloadScopeEnum = Field(
        default=...,
        alias="scope",
    )

    sort_by: str | None = Field(
        default=None,
        alias="sort_by",
    )

    title: str = Field(
        default=...,
        alias="title",
    )


class SavedViewRearrangePayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/SavedViewRearrangePayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    order: list[str] = Field(
        default=...,
        alias="order",
    )


class SavedViewResource(BaseModel):
    """Aryeo API schema for `#/components/schemas/SavedViewResource`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: SavedView = Field(
        default=...,
        alias="data",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class SetupIntentResponse(BaseModel):
    """Aryeo API schema for `#/components/schemas/SetupIntentResponse`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    client_secret: str | None = Field(
        default=...,
        alias="client_secret",
    )


class SocialProfiles(BaseModel):
    """Aryeo API schema for `#/components/schemas/SocialProfiles`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    facebook_profile_url: str | None = Field(
        default=None,
        alias="facebook_profile_url",
    )

    instagram_profile_url: str | None = Field(
        default=None,
        alias="instagram_profile_url",
    )

    linkedin_profile_url: str | None = Field(
        default=None,
        alias="linkedin_profile_url",
    )

    twitter_profile_url: str | None = Field(
        default=None,
        alias="twitter_profile_url",
    )

    zillow_profile_url: str | None = Field(
        default=None,
        alias="zillow_profile_url",
    )


class SsoProvider(BaseModel):
    """Aryeo API schema for `#/components/schemas/SsoProvider`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    name: str = Field(
        default=...,
        alias="name",
    )

    provider: str = Field(
        default=...,
        alias="provider",
    )


class SsoUser(BaseModel):
    """Aryeo API schema for `#/components/schemas/SsoUser`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    sso_id: str = Field(
        default=...,
        alias="sso_id",
    )

    sso_provider: SsoProvider | None = Field(
        default=None,
        alias="sso_provider",
    )


class Tag(BaseModel):
    """Aryeo API schema for `#/components/schemas/Tag`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    color: str = Field(
        default=...,
        alias="color",
    )

    font_color: str = Field(
        default=...,
        alias="font_color",
    )

    id: str = Field(
        default=...,
        alias="id",
    )

    name: str = Field(
        default=...,
        alias="name",
    )

    object: TagObjectEnum | None = Field(
        default=None,
        alias="object",
    )

    slug: str = Field(
        default=...,
        alias="slug",
    )

    type: TagTypeEnum | None = Field(
        default=None,
        alias="type",
    )


class TagCollection(BaseModel):
    """Aryeo API schema for `#/components/schemas/TagCollection`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: list[Tag] | None = Field(
        default=None,
        alias="data",
    )

    links: PaginationLinks | None = Field(
        default=None,
        alias="links",
    )

    meta: PaginationMeta | None = Field(
        default=None,
        alias="meta",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class TagOnlyPostPayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/TagOnlyPostPayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    color: str = Field(
        default=...,
        alias="color",
    )

    name: str = Field(
        default=...,
        alias="name",
    )

    type: TagOnlyPostPayloadTypeEnum = Field(
        default=...,
        alias="type",
    )


class TagPutPayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/TagPutPayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    color: str | None = Field(
        default=None,
        alias="color",
    )

    name: str | None = Field(
        default=None,
        alias="name",
    )


class TagResource(BaseModel):
    """Aryeo API schema for `#/components/schemas/TagResource`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: Tag | None = Field(
        default=None,
        alias="data",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class TagsPostPayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/TagsPostPayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    tag: dict[str, JSONValue] | None = Field(
        default=None,
        alias="tag",
    )

    tag_id: str | None = Field(
        default=None,
        alias="tag_id",
    )


class TagsPutPayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/TagsPutPayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    tag_ids: list[str] = Field(
        default=...,
        alias="tag_ids",
    )


class Task(BaseModel):
    """Aryeo API schema for `#/components/schemas/Task`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    assignee: CompanyTeamMember | None = Field(
        default=None,
        alias="assignee",
    )

    completed_at: str | None = Field(
        default=None,
        alias="completed_at",
    )

    completed_by: CompanyTeamMember | None = Field(
        default=None,
        alias="completed_by",
    )

    description: str | None = Field(
        default=None,
        alias="description",
    )

    due_at: str | None = Field(
        default=None,
        alias="due_at",
    )

    id: str = Field(
        default=...,
        alias="id",
    )

    is_completed: bool = Field(
        default=...,
        alias="is_completed",
    )

    name: str = Field(
        default=...,
        alias="name",
    )

    pay_run_item_amount: float | None = Field(
        default=None,
        alias="pay_run_item_amount",
    )

    quantity: int | None = Field(
        default=None,
        alias="quantity",
    )

    task_template: TaskTemplate | None = Field(
        default=None,
        alias="task_template",
    )


class TaskCollection(BaseModel):
    """Aryeo API schema for `#/components/schemas/TaskCollection`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: list[Task] | None = Field(
        default=None,
        alias="data",
    )

    links: PaginationLinks | None = Field(
        default=None,
        alias="links",
    )

    meta: PaginationMeta | None = Field(
        default=None,
        alias="meta",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class TaskCompletePutPayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/TaskCompletePutPayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    completed_at: str | None = Field(
        default=...,
        alias="completed_at",
    )


class TaskPostPayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/TaskPostPayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    company_team_member_id: str | None = Field(
        default=None,
        alias="company_team_member_id",
    )

    completed_at: str | None = Field(
        default=None,
        alias="completed_at",
    )

    description: str | None = Field(
        default=None,
        alias="description",
    )

    due_at: str | None = Field(
        default=None,
        alias="due_at",
    )

    name: str = Field(
        default=...,
        alias="name",
    )


class TaskPutPayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/TaskPutPayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    company_team_member_id: str | None = Field(
        default=None,
        alias="company_team_member_id",
    )

    completed_at: str | None = Field(
        default=None,
        alias="completed_at",
    )

    description: str | None = Field(
        default=None,
        alias="description",
    )

    due_at: str | None = Field(
        default=None,
        alias="due_at",
    )

    name: str = Field(
        default=...,
        alias="name",
    )


class TaskReinstatePutPayload(RootModel[dict[str, JSONValue]]):
    """Aryeo API root schema for `#/components/schemas/TaskReinstatePutPayload`."""


class TaskResource(BaseModel):
    """Aryeo API schema for `#/components/schemas/TaskResource`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: Task | None = Field(
        default=None,
        alias="data",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class TaskTemplate(BaseModel):
    """Aryeo API schema for `#/components/schemas/TaskTemplate`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    default_pay_run_item_amount: int | None = Field(
        default=None,
        alias="default_pay_run_item_amount",
    )

    default_pay_run_item_amount_type: (
        TaskTemplateDefaultPayRunItemAmountTypeEnum | None
    ) = Field(
        default=None,
        alias="default_pay_run_item_amount_type",
    )

    description: str | None = Field(
        default=None,
        alias="description",
    )

    id: str | None = Field(
        default=None,
        alias="id",
    )

    name: str | None = Field(
        default=None,
        alias="name",
    )

    pay_run_item_amount_overrides: list[PayRunItemAmountOverride] | None = Field(
        default=None,
        alias="pay_run_item_amount_overrides",
    )

    product_variant: ProductVariant | None = Field(
        default=None,
        alias="product_variant",
    )


class Tax(BaseModel):
    """Aryeo API schema for `#/components/schemas/Tax`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    applied_rate: float | None = Field(
        default=None,
        alias="applied_rate",
    )

    id: str = Field(
        default=...,
        alias="id",
    )

    object: str = Field(
        default=...,
        alias="object",
    )

    tax_rate: TaxRate | None = Field(
        default=None,
        alias="tax_rate",
    )

    total_tax_amount: int | None = Field(
        default=None,
        alias="total_tax_amount",
    )


class TaxPostPayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/TaxPostPayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    order_id: str = Field(
        default=...,
        alias="order_id",
    )

    tax_rate_data: dict[str, JSONValue] | None = Field(
        default=None,
        alias="tax_rate_data",
    )


class TaxRate(BaseModel):
    """Aryeo API schema for `#/components/schemas/TaxRate`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    applied_rate: float | None = Field(
        default=None,
        alias="applied_rate",
    )

    description: str | None = Field(
        default=None,
        alias="description",
    )

    id: str = Field(
        default=...,
        alias="id",
    )

    is_active: bool | None = Field(
        default=None,
        alias="is_active",
    )

    is_inclusive: bool | None = Field(
        default=None,
        alias="is_inclusive",
    )

    name: str | None = Field(
        default=None,
        alias="name",
    )

    object: str = Field(
        default=...,
        alias="object",
    )

    rate: str | None = Field(
        default=None,
        alias="rate",
    )


class TaxResource(BaseModel):
    """Aryeo API schema for `#/components/schemas/TaxResource`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: Tax | None = Field(
        default=None,
        alias="data",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class Territory(BaseModel):
    """Aryeo API schema for `#/components/schemas/Territory`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id: str = Field(
        default=...,
        alias="id",
    )

    name: str = Field(
        default=...,
        alias="name",
    )

    object: TerritoryObjectEnum | None = Field(
        default=None,
        alias="object",
    )


class TerritoryCollection(BaseModel):
    """Aryeo API schema for `#/components/schemas/TerritoryCollection`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: list[Territory] | None = Field(
        default=None,
        alias="data",
    )

    links: PaginationLinks | None = Field(
        default=None,
        alias="links",
    )

    meta: PaginationMeta | None = Field(
        default=None,
        alias="meta",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class Timeslot(BaseModel):
    """Aryeo API schema for `#/components/schemas/Timeslot`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    end_at: str = Field(
        default=...,
        alias="end_at",
    )

    start_at: str = Field(
        default=...,
        alias="start_at",
    )

    users: list[User] | None = Field(
        default=None,
        alias="users",
    )


class TimeslotCollection(BaseModel):
    """Aryeo API schema for `#/components/schemas/TimeslotCollection`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: list[Timeslot] | None = Field(
        default=None,
        alias="data",
    )

    links: PaginationLinks | None = Field(
        default=None,
        alias="links",
    )

    meta: CalendarDayCollectionMeta | None = Field(
        default=None,
        alias="meta",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class User(BaseModel):
    """Aryeo API schema for `#/components/schemas/User`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    avatar_url: str | None = Field(
        default=None,
        alias="avatar_url",
    )

    created_at: str | None = Field(
        default=None,
        alias="created_at",
    )

    email: str = Field(
        default=...,
        alias="email",
    )

    first_name: str | None = Field(
        default=None,
        alias="first_name",
    )

    full_name: str | None = Field(
        default=None,
        alias="full_name",
    )

    id: str = Field(
        default=...,
        alias="id",
    )

    internal_notes: str | None = Field(
        default=None,
        alias="internal_notes",
    )

    is_super: bool | None = Field(
        default=None,
        alias="is_super",
    )

    last_name: str | None = Field(
        default=None,
        alias="last_name",
    )

    object: str | None = Field(
        default=None,
        alias="object",
    )

    password_expiration_days: int | None = Field(
        default=None,
        alias="password_expiration_days",
    )

    phone: str | None = Field(
        default=None,
        alias="phone",
    )

    relationship: str | None = Field(
        default=None,
        alias="relationship",
    )

    sso_users: list[SsoUser] | None = Field(
        default=None,
        alias="sso_users",
    )

    status: UserStatusEnum | None = Field(
        default=None,
        alias="status",
    )

    timezone: str | None = Field(
        default=None,
        alias="timezone",
    )

    verification_status: UserVerificationStatusEnum | None = Field(
        default=None,
        alias="verification_status",
    )


class UserCollection(BaseModel):
    """Aryeo API schema for `#/components/schemas/UserCollection`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: list[User] | None = Field(
        default=None,
        alias="data",
    )

    links: PaginationLinks | None = Field(
        default=None,
        alias="links",
    )

    meta: PaginationMeta | None = Field(
        default=None,
        alias="meta",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class UserResource(BaseModel):
    """Aryeo API schema for `#/components/schemas/UserResource`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: User | None = Field(
        default=None,
        alias="data",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


class Video(BaseModel):
    """Aryeo API schema for `#/components/schemas/Video`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    display_type: VideoDisplayTypeEnum = Field(
        default=...,
        alias="display_type",
    )

    download_url: str | None = Field(
        default=None,
        alias="download_url",
    )

    duration: int | None = Field(
        default=None,
        alias="duration",
    )

    id: str = Field(
        default=...,
        alias="id",
    )

    object: VideoObjectEnum | None = Field(
        default=None,
        alias="object",
    )

    playback_url: str | None = Field(
        default=...,
        alias="playback_url",
    )

    share_url: str | None = Field(
        default=None,
        alias="share_url",
    )

    source_type: VideoSourceTypeEnum = Field(
        default=...,
        alias="source_type",
    )

    thumbnail_url: str = Field(
        default=...,
        alias="thumbnail_url",
    )

    title: str | None = Field(
        default=None,
        alias="title",
    )


class VideoPutPayload(BaseModel):
    """Aryeo API schema for `#/components/schemas/VideoPutPayload`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    title: str = Field(
        default=...,
        alias="title",
    )


class VideoResource(BaseModel):
    """Aryeo API schema for `#/components/schemas/VideoResource`."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    data: Video | None = Field(
        default=None,
        alias="data",
    )

    status: str = Field(
        default=...,
        alias="status",
    )

    timestamp: str | None = Field(
        default=None,
        alias="timestamp",
    )


__all__ = [
    "Activity",
    "ActivityCollection",
    "ActivityPostPayload",
    "ActivityResource",
    "Address",
    "AddressPatchPayload",
    "AddressPostPayload",
    "AddressPredictionResult",
    "AddressPredictionResultCollection",
    "AddressResource",
    "AddressSearchResult",
    "AddressSearchResultResource",
    "ApiError403",
    "ApiError404",
    "ApiError409",
    "ApiError500",
    "ApiFail422",
    "ApiSuccess2xx",
    "AppAndroidDetails",
    "AppIosdetails",
    "AppStoreDetails",
    "Appointment",
    "Appointment3dhTourLinkResponse",
    "AppointmentAcceptPutPayload",
    "AppointmentAttendance",
    "AppointmentCancelPutPayload",
    "AppointmentCollection",
    "AppointmentDeclinePutPayload",
    "AppointmentPostponePutPayload",
    "AppointmentReschedulePutPayload",
    "AppointmentResource",
    "AppointmentSchedulePutPayload",
    "AppointmentStorePostPayload",
    "AppointmentUpdatePutPayload",
    "AryeoGoConfig",
    "AryeoGoConfigResource",
    "AuthActivationStageResource",
    "AuthEmailCheckPostPayload",
    "AvailabilityResponse",
    "BlockPostPayload",
    "BookingLimits",
    "CalendarBlock",
    "CalendarBlockResource",
    "CalendarDay",
    "CalendarDayCollection",
    "CalendarDayCollectionMeta",
    "CalendarEvent",
    "CalendarEventCollection",
    "CalendarEventResource",
    "CompanyTeamMember",
    "CompanyTeamMemberCollection",
    "CompanyTeamMemberPermission",
    "CompanyTeamMemberResource",
    "Coupon",
    "CouponCollection",
    "CreditTransaction",
    "CreditTransactionResource",
    "CubiCasaFloorplan",
    "CubiCasaFloorplanResource",
    "CubiCasaFloorplanResult",
    "CustomerGroup",
    "CustomerPostPayload",
    "CustomerTeamAffiliateMembershipPostPayload",
    "CustomerTeamMembership",
    "CustomerTeamMembershipCollection",
    "CustomerTeamMembershipResource",
    "CustomerTeamNotesPutPayload",
    "CustomerTeamResource",
    "CustomerUser",
    "CustomerUserCollection",
    "CustomerUserPostPayload",
    "DeleteUserPostPayload",
    "Discount",
    "DiscountAmount",
    "DiscountPostPayload",
    "DiscountResource",
    "Discountable",
    "DiscountableItem",
    "Dots",
    "DotsResource",
    "DraftOrderCustomerUserPutPayload",
    "EsoftOrderLine",
    "Export",
    "FeatureFlags",
    "Fee",
    "File",
    "FloorPlan",
    "ForgotPasswordPostPayload",
    "Group",
    "GroupCollection",
    "GroupCustomer",
    "GroupCustomerCollection",
    "GroupCustomerResource",
    "GroupResource",
    "Image",
    "ImpersonatePostPayload",
    "InteractiveContent",
    "Listing",
    "ListingBuilding",
    "ListingCollection",
    "ListingCountsPayload",
    "ListingCountsResource",
    "ListingDetailSearch",
    "ListingDetailSearchResource",
    "ListingLot",
    "ListingMarketingContent",
    "ListingMarketingContentResource",
    "ListingPostPayload",
    "ListingPrice",
    "ListingPutPayload",
    "ListingPutShowcasePayload",
    "ListingResource",
    "ListingStats",
    "ListingStatsResource",
    "LoginPostPayload",
    "LoginViaTokenPostPayload",
    "MarketingMaterial",
    "MarketingMaterialCategory",
    "MarketingMaterialPublishPayload",
    "MarketingMaterialResource",
    "MarketingMaterialStorePayload",
    "MarketingMaterialTemplate",
    "MarketingMaterialTemplateCollection",
    "MarketingMaterialTemplatePublishPayload",
    "MarketingMaterialTemplateResource",
    "MarketingMaterialTemplateStorePayload",
    "MarketingMaterialTemplateUpdatePayload",
    "MarketingMaterialUpdatePayload",
    "MePasswordPutPayload",
    "MediaRequestMediaSearchPayload",
    "MediaSearchResource",
    "NotificationPreference",
    "NotificationPreference2",
    "NotificationPreferencesCollection",
    "NotificationPreferencesPutPayload",
    "Order",
    "OrderBillingAddressPutPayload",
    "OrderCollection",
    "OrderForm",
    "OrderFormCollection",
    "OrderFormSession",
    "OrderFormSessionPostPayload",
    "OrderFormSessionResource",
    "OrderItem",
    "OrderItemGrouping",
    "OrderItemGroupingCollection",
    "OrderItemPayRunItemDefaults",
    "OrderItemPostPayload",
    "OrderItemResource",
    "OrderNotesPutPayload",
    "OrderPayment",
    "OrderPostPayload",
    "OrderRefund",
    "OrderRefundPostPayload",
    "OrderRefundResource",
    "OrderResource",
    "OrderTagsPostPayload",
    "PaginationLink",
    "PaginationLinks",
    "PaginationMeta",
    "PayRunItemAmountOverride",
    "Payment",
    "PaymentGateway",
    "PaymentInfo",
    "PaymentInfoConfig",
    "PaymentInfoResource",
    "PaymentMethod",
    "PaymentResource",
    "PersonalAccessToken",
    "PersonalAccessTokenCustomer",
    "PersonalAccessTokenCustomerResource",
    "PersonalAccessTokenResource",
    "PolotnoJson",
    "PortalAppColors",
    "PortalAppConfig",
    "PortalAppConfigPutPayload",
    "PortalAppConfigResource",
    "PortalAppContact",
    "PortalAppContactLegacy",
    "PortalAppDevAccounts",
    "PortalAppExampleOrder",
    "PortalAppImages",
    "PortalAppRevision",
    "PortalAppSettings",
    "PortalAppStrings",
    "PortalCustomerJoinPostPayload",
    "PortalCustomerRegisterPostPayload",
    "PortalCustomerVerifyPostPayload",
    "Product",
    "ProductCategory",
    "ProductCategoryCollection",
    "ProductCollection",
    "ProductResource",
    "ProductVariant",
    "PromotionCode",
    "PromotionCodeRedeemPostPayload",
    "PropertyWebsite",
    "QuickBooksCustomer",
    "QuickBooksCustomerCollection",
    "QuickBooksItem",
    "QuickBooksItemCollection",
    "QuickBooksItemResource",
    "Region",
    "RegionCollection",
    "Review",
    "ReviewCollection",
    "ReviewPostPayload",
    "ReviewResource",
    "SavedView",
    "SavedViewCollection",
    "SavedViewFilter",
    "SavedViewPatchPayload",
    "SavedViewPostPayload",
    "SavedViewRearrangePayload",
    "SavedViewResource",
    "SetupIntentResponse",
    "SocialProfiles",
    "SsoProvider",
    "SsoUser",
    "Tag",
    "TagCollection",
    "TagOnlyPostPayload",
    "TagPutPayload",
    "TagResource",
    "TagsPostPayload",
    "TagsPutPayload",
    "Task",
    "TaskCollection",
    "TaskCompletePutPayload",
    "TaskPostPayload",
    "TaskPutPayload",
    "TaskReinstatePutPayload",
    "TaskResource",
    "TaskTemplate",
    "Tax",
    "TaxPostPayload",
    "TaxRate",
    "TaxResource",
    "Territory",
    "TerritoryCollection",
    "Timeslot",
    "TimeslotCollection",
    "User",
    "UserCollection",
    "UserResource",
    "Video",
    "VideoPutPayload",
    "VideoResource",
]
