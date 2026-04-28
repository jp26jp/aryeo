"""Generated enum values for the Aryeo API.

Do not edit by hand; regenerate from docs/api/aryeo.json.
"""

from __future__ import annotations

from enum import Enum


class ActivityNameEnum(str, Enum):
    """Allowed values for `Activity.properties.name`."""

    USER_LOGGED_IN = "USER_LOGGED_IN"
    USER_LOGGED_OUT = "USER_LOGGED_OUT"
    USER_REGISTERED = "USER_REGISTERED"
    ORDER_FEE_CREATED = "ORDER_FEE_CREATED"
    ORDER_FEE_DELETED = "ORDER_FEE_DELETED"
    ORDER_MEDIA_DOWNLOADED = "ORDER_MEDIA_DOWNLOADED"
    ORDER_PLACED = "ORDER_PLACED"
    ORDER_RECEIVED = "ORDER_RECEIVED"
    ORDER_CREATED = "ORDER_CREATED"
    ORDER_VIEWED = "ORDER_VIEWED"
    ORDER_REFUNDED = "ORDER_REFUNDED"
    ORDER_PAYMENT_COMPLETED = "ORDER_PAYMENT_COMPLETED"
    ORDER_PAYMENT_DELETED = "ORDER_PAYMENT_DELETED"
    ORDER_PAYMENT_ENTERED = "ORDER_PAYMENT_ENTERED"
    ORDER_ATTACHED_TO_LISTING = "ORDER_ATTACHED_TO_LISTING"
    ORDER_SYNCED_TO_QUICKBOOKS = "ORDER_SYNCED_TO_QUICKBOOKS"
    ORDER_SYNC_TO_QUICKBOOKS_FAILED = "ORDER_SYNC_TO_QUICKBOOKS_FAILED"
    ORDER_PAYMENT_SYNCED_TO_QUICKBOOKS = "ORDER_PAYMENT_SYNCED_TO_QUICKBOOKS"
    APPOINTMENT_ACCEPTED = "APPOINTMENT_ACCEPTED"
    APPOINTMENT_DECLINED = "APPOINTMENT_DECLINED"
    APPOINTMENT_SCHEDULED = "APPOINTMENT_SCHEDULED"
    APPOINTMENT_REQUESTED = "APPOINTMENT_REQUESTED"
    APPOINTMENT_RESCHEDULED = "APPOINTMENT_RESCHEDULED"
    APPOINTMENT_POSTPONED = "APPOINTMENT_POSTPONED"
    APPOINTMENT_CANCELED = "APPOINTMENT_CANCELED"
    APPOINTMENT_ASSIGNED = "APPOINTMENT_ASSIGNED"
    APPOINTMENT_UNASSIGNED = "APPOINTMENT_UNASSIGNED"
    APPOINTMENT_CREATOR_REMINDER_SENT = "APPOINTMENT_CREATOR_REMINDER_SENT"
    APPOINTMENT_CUSTOMER_REMINDER_SENT = "APPOINTMENT_CUSTOMER_REMINDER_SENT"
    LISTING_CREATED = "LISTING_CREATED"
    LISTING_UPDATED = "LISTING_UPDATED"
    LISTING_DELIVERED = "LISTING_DELIVERED"
    LISTING_CONTENT_DOWNLOADED = "LISTING_CONTENT_DOWNLOADED"
    LISTING_VIEWED = "LISTING_VIEWED"
    MARKETING_MATERIAL_CREATED = "MARKETING_MATERIAL_CREATED"
    NOTIFICATION_SENT = "NOTIFICATION_SENT"
    CUSTOMER_TEAM_CREATED = "CUSTOMER_TEAM_CREATED"
    CUSTOMER_TEAM_ARCHIVED = "CUSTOMER_TEAM_ARCHIVED"
    CUSTOMER_TEAM_PRICING_PLAN_APPLIED = "CUSTOMER_TEAM_PRICING_PLAN_APPLIED"
    CUSTOMER_TEAM_PRICING_PLAN_REMOVED = "CUSTOMER_TEAM_PRICING_PLAN_REMOVED"
    CUSTOMER_TEAM_INTERNAL_NOTE_UPDATED = "CUSTOMER_TEAM_INTERNAL_NOTE_UPDATED"
    CUSTOMER_TEAM_PRESELECTED_PRODUCTS_UPDATED = (
        "CUSTOMER_TEAM_PRESELECTED_PRODUCTS_UPDATED"
    )
    CUSTOMER_TEAM_DOWNLOAD_SETTINGS_UPDATED = "CUSTOMER_TEAM_DOWNLOAD_SETTINGS_UPDATED"
    CUSTOMER_TEAM_BILLING_TEAM_MEMBERSHIP_UPDATED = (
        "CUSTOMER_TEAM_BILLING_TEAM_MEMBERSHIP_UPDATED"
    )
    CUSTOMER_TEAM_BILLING_TEAM_MEMBERSHIP_REMOVED = (
        "CUSTOMER_TEAM_BILLING_TEAM_MEMBERSHIP_REMOVED"
    )
    CUSTOMER_TEAM_PRICE_OVERRIDES_UPDATED = "CUSTOMER_TEAM_PRICE_OVERRIDES_UPDATED"
    CUSTOMER_TEAM_MEMBERSHIP_CREATED = "CUSTOMER_TEAM_MEMBERSHIP_CREATED"
    CUSTOMER_TEAM_MEMBERSHIP_ARCHIVED = "CUSTOMER_TEAM_MEMBERSHIP_ARCHIVED"
    CUSTOMER_TEAM_MEMBERSHIP_DELETED = "CUSTOMER_TEAM_MEMBERSHIP_DELETED"
    CUSTOMER_TEAM_MEMBERSHIP_REACTIVATED = "CUSTOMER_TEAM_MEMBERSHIP_REACTIVATED"
    CUSTOMER_TEAM_MEMBERSHIP_INVITATION_ACCEPTED = (
        "CUSTOMER_TEAM_MEMBERSHIP_INVITATION_ACCEPTED"
    )
    CUSTOMER_TEAM_MEMBERSHIP_REVOKED = "CUSTOMER_TEAM_MEMBERSHIP_REVOKED"
    DEFAULT_CUSTOMER_TEAM_MEMBERSHIP_ADDED = "DEFAULT_CUSTOMER_TEAM_MEMBERSHIP_ADDED"
    DEFAULT_CUSTOMER_TEAM_MEMBERSHIP_REMOVED = (
        "DEFAULT_CUSTOMER_TEAM_MEMBERSHIP_REMOVED"
    )
    MEDIA_REQUEST_CREATED = "MEDIA_REQUEST_CREATED"
    MEDIA_REQUEST_CANCELED = "MEDIA_REQUEST_CANCELED"
    MEDIA_REQUEST_ACCEPTED = "MEDIA_REQUEST_ACCEPTED"
    MEDIA_REQUEST_ASSIGNED = "MEDIA_REQUEST_ASSIGNED"
    MEDIA_REQUEST_DECLINED = "MEDIA_REQUEST_DECLINED"
    MEDIA_REQUEST_DELIVERED = "MEDIA_REQUEST_DELIVERED"
    MEDIA_REQUEST_TRANSFERRED = "MEDIA_REQUEST_TRANSFERRED"


class ActivityPostPayloadNameEnum(str, Enum):
    """Allowed values for `ActivityPostPayload.properties.name`."""

    USER_LOGGED_IN = "USER_LOGGED_IN"
    USER_LOGGED_OUT = "USER_LOGGED_OUT"
    USER_REGISTERED = "USER_REGISTERED"
    ORDER_MEDIA_DOWNLOADED = "ORDER_MEDIA_DOWNLOADED"
    ORDER_PLACED = "ORDER_PLACED"
    ORDER_VIEWED = "ORDER_VIEWED"


class ActivityPostPayloadResourceTypeEnum(str, Enum):
    """Allowed values for `ActivityPostPayload.properties.resource_type`."""

    LISTING = "LISTING"
    ORDER = "ORDER"


class ActivityPostPayloadSourceEnum(str, Enum):
    """Allowed values for `ActivityPostPayload.properties.source`."""

    WEB = "WEB"
    IOS = "IOS"
    API = "API"


class ActivitySourceEnum(str, Enum):
    """Allowed values for `Activity.properties.source`."""

    ANDROID = "ANDROID"
    ANDROID_ARYEO_GO = "ANDROID_ARYEO_GO"
    API = "API"
    IOS = "IOS"
    IOS_ARYEO_GO = "IOS_ARYEO_GO"
    WEB = "WEB"


class AddressPatchPayloadExternalTypeEnum(str, Enum):
    """Allowed values for `AddressPatchPayload.properties.external_type`."""

    GOOGLE = "GOOGLE"


class AddressPredictionResultExternalTypeEnum(str, Enum):
    """Allowed values for `AddressPredictionResult.properties.external_type`."""

    GOOGLE = "GOOGLE"


class AddressSearchResultExternalTypeEnum(str, Enum):
    """Allowed values for `AddressSearchResult.properties.external_type`."""

    GOOGLE = "GOOGLE"


class AppointmentAttendanceObjectEnum(str, Enum):
    """Allowed values for `AppointmentAttendance.properties.object`."""

    APPOINTMENT_ATTENDANCE = "APPOINTMENT_ATTENDANCE"


class AppointmentPreferenceTypeEnum(str, Enum):
    """Allowed values for `Appointment.properties.preference_type`."""

    ASAP = "ASAP"
    TIME = "TIME"
    TIME_OF_DAY = "TIME_OF_DAY"
    NONE = "NONE"


class AppointmentPreferredStartAtTimeOfDayEnum(str, Enum):
    """Allowed values for `Appointment.properties.preferred_start_at_time_of_day`."""

    MORNING = "MORNING"
    MIDDAY = "MIDDAY"
    AFTERNOON = "AFTERNOON"
    TWILIGHT = "TWILIGHT"


class AppointmentStatusEnum(str, Enum):
    """Allowed values for `Appointment.properties.status`."""

    SCHEDULED = "SCHEDULED"
    UNSCHEDULED = "UNSCHEDULED"
    CANCELED = "CANCELED"


class AuthActivationStageResourceStatusEnum(str, Enum):
    """Allowed values for `AuthActivationStageResource.properties.status`."""

    ACTIVE = "ACTIVE"
    INVITED = "INVITED"
    NEW = "NEW"


class BookingLimitsAutomatedUserAssignmentStrategyEnum(str, Enum):
    """Allowed values for `BookingLimits.properties.automated_user_assignment_strategy`."""

    RECOMMENDED = "RECOMMENDED"
    HOURS_PRIORITY = "HOURS_PRIORITY"
    DISTANCE = "DISTANCE"
    ROUND_ROBIN = "ROUND_ROBIN"
    PRIORITY_LIST = "PRIORITY_LIST"


class BookingLimitsAvailabilityStyleEnum(str, Enum):
    """Allowed values for `BookingLimits.properties.availability_style`."""

    TIME = "TIME"
    TIME_OF_DAY = "TIME_OF_DAY"
    LEGACY = "LEGACY"
    DATETIME_PICKER = "DATETIME_PICKER"


class BookingLimitsObjectEnum(str, Enum):
    """Allowed values for `BookingLimits.properties.object`."""

    COMPANY = "COMPANY"


class CalendarBlockTypeEnum(str, Enum):
    """Allowed values for `CalendarBlock.properties.type`."""

    APPOINTMENT = "APPOINTMENT"
    CALENDAR_BLOCK = "CALENDAR_BLOCK"
    EXTERNAL = "EXTERNAL"
    BUFFER = "BUFFER"
    DECLINED_APPOINTMENT = "DECLINED_APPOINTMENT"
    UNSCHEDULED_APPOINTMENT = "UNSCHEDULED_APPOINTMENT"


class CalendarEventTypeEnum(str, Enum):
    """Allowed values for `CalendarEvent.properties.type`."""

    APPOINTMENT = "APPOINTMENT"
    CALENDAR_BLOCK = "CALENDAR_BLOCK"
    EXTERNAL = "EXTERNAL"
    BUFFER = "BUFFER"
    DECLINED_APPOINTMENT = "DECLINED_APPOINTMENT"
    UNSCHEDULED_APPOINTMENT = "UNSCHEDULED_APPOINTMENT"


class CompanyTeamMemberObjectEnum(str, Enum):
    """Allowed values for `CompanyTeamMember.properties.object`."""

    COMPANY_TEAM_MEMBER = "COMPANY_TEAM_MEMBER"


class CompanyTeamMemberPermissionNameEnum(str, Enum):
    """Allowed values for `CompanyTeamMemberPermission.properties.name`."""

    ACTIVITY_LOG_VIEW = "ACTIVITY_LOG_VIEW"
    APP_STORE_VIEW_ANY = "APP_STORE_VIEW_ANY"
    APPOINTMENTS_MANAGE = "APPOINTMENTS_MANAGE"
    AVAILABILITY_VIEW_ANY = "AVAILABILITY_VIEW_ANY"
    CALENDAR_VIEW_ANY = "CALENDAR_VIEW_ANY"
    CUSTOMER_CREATE = "CUSTOMER_CREATE"
    CUSTOMER_DELETE = "CUSTOMER_DELETE"
    CUSTOMER_EXPORT_CREATE = "CUSTOMER_EXPORT_CREATE"
    CUSTOMER_IMPORT_CREATE = "CUSTOMER_IMPORT_CREATE"
    CUSTOMER_VIEW_ANY = "CUSTOMER_VIEW_ANY"
    FEE_VIEW_ANY = "FEE_VIEW_ANY"
    LISTING_CREATE = "LISTING_CREATE"
    LISTING_DELETE = "LISTING_DELETE"
    LISTING_VIEW_ANY = "LISTING_VIEW_ANY"
    MEDIA_REQUEST_MANAGE = "MEDIA_REQUEST_MANAGE"
    ORDER_AMOUNT_VIEW_ANY = "ORDER_AMOUNT_VIEW_ANY"
    ORDER_FORM_VIEW_ANY = "ORDER_FORM_VIEW_ANY"
    ORDER_NOTES_MANAGE = "ORDER_NOTES_MANAGE"
    ORDER_VIEW_ANY = "ORDER_VIEW_ANY"
    ORDERS_MANAGE = "ORDERS_MANAGE"
    PAYMENT_METHODS_MANAGE = "PAYMENT_METHODS_MANAGE"
    PAYROLL_MANAGE = "PAYROLL_MANAGE"
    PAYROLL_PERSONAL_MANAGE = "PAYROLL_PERSONAL_MANAGE"
    PAYROLL_PERSONAL_VIEW = "PAYROLL_PERSONAL_VIEW"
    PRODUCT_VIEW_ANY = "PRODUCT_VIEW_ANY"
    REPORT_VIEW_ANY = "REPORT_VIEW_ANY"
    SETTINGS_MANAGE = "SETTINGS_MANAGE"
    TAX_VIEW_ANY = "TAX_VIEW_ANY"
    TERRITORY_VIEW_ANY = "TERRITORY_VIEW_ANY"
    ZILLOW_MEDIA_EXCLUSIVES_MANAGE = "ZILLOW_MEDIA_EXCLUSIVES_MANAGE"
    SAVED_VIEWS_MANAGE = "SAVED_VIEWS_MANAGE"


class CompanyTeamMemberPermissionObjectEnum(str, Enum):
    """Allowed values for `CompanyTeamMemberPermission.properties.object`."""

    PERMISSION = "PERMISSION"


class CompanyTeamMemberResourceStrategyTypeEnum(str, Enum):
    """Allowed values for `CompanyTeamMemberResource.properties.strategy_type`."""

    DISTANCE = "DISTANCE"
    HOURS_PRIORITY = "HOURS_PRIORITY"
    ROUND_ROBIN = "ROUND_ROBIN"
    RECOMMENDED = "RECOMMENDED"
    PRIORITY_LIST = "PRIORITY_LIST"


class CompanyTeamMemberRoleEnum(str, Enum):
    """Allowed values for `CompanyTeamMember.properties.role`."""

    ADMIN = "ADMIN"
    MEMBER = "MEMBER"
    OWNER = "OWNER"


class CompanyTeamMemberStatusEnum(str, Enum):
    """Allowed values for `CompanyTeamMember.properties.status`."""

    ACTIVE = "active"
    INVITED = "invited"
    REVOKED = "revoked"


class CreditTransactionTypeEnum(str, Enum):
    """Allowed values for `CreditTransaction.properties.type`."""

    CREDIT = "credit"
    DEBIT = "debit"


class CustomerGroupObjectEnum(str, Enum):
    """Allowed values for `CustomerGroup.properties.object`."""

    CUSTOMER_TEAM = "CUSTOMER_TEAM"


class CustomerGroupStatusEnum(str, Enum):
    """Allowed values for `CustomerGroup.properties.status`."""

    ANY_STATUS = "any_status"
    ACTIVE = "active"
    ARCHIVED = "archived"


class CustomerTeamMembershipObjectEnum(str, Enum):
    """Allowed values for `CustomerTeamMembership.properties.object`."""

    CUSTOMER_TEAM_MEMBERSHIP = "CUSTOMER_TEAM_MEMBERSHIP"


class CustomerTeamMembershipRoleEnum(str, Enum):
    """Allowed values for `CustomerTeamMembership.properties.role`."""

    ADMIN = "admin"
    MEMBER = "member"


class CustomerTeamMembershipStatusEnum(str, Enum):
    """Allowed values for `CustomerTeamMembership.properties.status`."""

    DELETED = "deleted"
    ARCHIVED = "archived"
    REVOKED = "revoked"
    ACTIVE = "active"
    INVITED = "invited"


class CustomerUserPostPayloadRoleEnum(str, Enum):
    """Allowed values for `CustomerUserPostPayload.properties.role`."""

    ADMIN = "admin"
    MEMBER = "member"


class CustomerUserStatusEnum(str, Enum):
    """Allowed values for `CustomerUser.properties.status`."""

    ACTIVE = "active"
    INACTIVE = "inactive"
    NEW = "new"
    SSO = "sso"


class CustomerUserVerificationStatusEnum(str, Enum):
    """Allowed values for `CustomerUser.properties.verification_status`."""

    VERIFIED = "verified"
    UNVERIFIED = "unverified"
    NEW = "new"
    SSO = "sso"


class DeleteUserPostPayloadClientEnum(str, Enum):
    """Allowed values for `DeleteUserPostPayload.properties.client`."""

    IOS = "IOS"
    ANDROID = "ANDROID"
    PHPUNIT = "PHPUNIT"


class DiscountAmountObjectEnum(str, Enum):
    """Allowed values for `DiscountAmount.properties.object`."""

    APP_DISCOUNTS_MODELS_DISCOUNTAMOUNT = "APP\\DISCOUNTS\\MODELS\\DISCOUNTAMOUNT"


class DiscountObjectEnum(str, Enum):
    """Allowed values for `Discount.properties.object`."""

    DISCOUNT = "DISCOUNT"


class EsoftOrderLineObjectEnum(str, Enum):
    """Allowed values for `EsoftOrderLine.properties.object`."""

    ESOFT_ORDER_LINE = "ESOFT_ORDER_LINE"


class EsoftOrderLineStatusEnum(str, Enum):
    """Allowed values for `EsoftOrderLine.properties.status`."""

    COMPLETE = "complete"
    CANCELLED = "cancelled"
    DRAFT = "draft"
    ERROR = "error"
    SUBMITTED = "submitted"


class FeatureFlagsEnum(str, Enum):
    """Allowed values for `FeatureFlags.items`."""

    ALTERNATE_UNBRANDED_PROPERTY_SITE_URL = "alternate_unbranded_property_site_url"
    AVALARA_TAX_SYNCING = "avalara_tax_syncing"
    AVALARA_TAXES = "avalara_taxes"
    BYOP = "byop"
    CALENDAR_EVENT_TITLE_MODIFIED = "calendar_event_title_modified"
    CUSTOM_FIELD_UPLOADS = "custom_field_uploads"
    CUSTOMER_TEAMS_ORDER_FORM_LANDING_PAGE_OVERRIDE = (
        "customer_teams_order_form_landing_page_override"
    )
    CUSTOMER_TEAMS_PRODUCT_PRESELECT = "customer_teams_product_preselect"
    CUSTOMER_TEAMS_EXTERNAL_PAYMENTS = "customer_teams_external_payments"
    CUSTOMER_PORTAL_MOBILE_APP_AUTOMATED_SCREENSHOTS = (
        "customer_portal_mobile_app_automated_screenshots"
    )
    DATABASE_EXTERNAL_CALENDAR_EVENTS = "database_external_calendar_events"
    DEFAULT_RESCHEDULE_TOGGLE_FALSE = "default_reschedule_toggle_false"
    IDP_MIGRATION_IN_PROGRESS = "idp_migration_in_progress"
    LISTINGS_NEW_CREATION_FLOW = "listings_new_creation_flow"
    LISTINGS_NEW_EDIT_PAGE = "listings_new_edit_page"
    MIN_HOUR_TARGETS = "min_hour_targets"
    MAX_TRAVEL_DISTANCE = "max_travel_distance"
    ORDER_FORM_CATEGORIES = "order_form_categories"
    REQUIRE_PHOTOGRAPHER_CONFIRMATIONS = "require_photographer_confirmations"
    SHOWCASE_ORDER_FORM_VISIBILITY_DESIGNATIONS = (
        "showcase_order_form_visibility_designations"
    )
    TEAM_MEMBER_RESTRICTIONS = "team_member_restrictions"
    TEAM_MEMBER_HIDE_CUSTOMER_PII = "team_member_hide_customer_pii"
    VIRTUAL_STAGING_AI_V2 = "virtual_staging_ai_v2"
    VIRTUAL_STAGING_AI_V2_PRICING = "virtual_staging_ai_v2_pricing"
    VIRTUALS1_CUSTOM_SMS_NOTIFICATION_MESSAGES = (
        "virtuals1_custom_sms_notification_messages"
    )
    QUICKBOOKS_APP = "quickbooks_app"
    WEBHOOKS = "webhooks"
    ZILLOW_3D_HOME = "zillow_3d_home"
    ZILLOW_STREETEASY = "zillow_streeteasy"
    ZILLOW_RENTALS = "zillow_rentals"


class FeeObjectEnum(str, Enum):
    """Allowed values for `Fee.properties.object`."""

    FEE = "FEE"


class FeeTypeEnum(str, Enum):
    """Allowed values for `Fee.properties.type`."""

    FLAT = "FLAT"
    PERCENT = "PERCENT"
    BASIC_METERED = "BASIC_METERED"
    GRADUATED_METERED = "GRADUATED_METERED"
    VOLUME_METERED = "VOLUME_METERED"
    TERRITORY = "TERRITORY"


class FileDisplayTypeEnum(str, Enum):
    """Allowed values for `File.properties.display_type`."""

    NONE = "none"
    BOTH = "both"


class FloorPlanObjectEnum(str, Enum):
    """Allowed values for `FloorPlan.properties.object`."""

    FLOORPLAN = "FLOORPLAN"


class GroupAutomatedUserAssignmentStrategyEnum(str, Enum):
    """Allowed values for `Group.properties.automated_user_assignment_strategy`."""

    RECOMMENDED = "RECOMMENDED"
    HOURS_PRIORITY = "HOURS_PRIORITY"
    DISTANCE = "DISTANCE"
    ROUND_ROBIN = "ROUND_ROBIN"
    PRIORITY_LIST = "PRIORITY_LIST"


class GroupAvailabilityStyleEnum(str, Enum):
    """Allowed values for `Group.properties.availability_style`."""

    TIME = "TIME"
    TIME_OF_DAY = "TIME_OF_DAY"
    LEGACY = "LEGACY"


class GroupCurrencyEnum(str, Enum):
    """Allowed values for `Group.properties.currency`."""

    USD = "USD"
    CAD = "CAD"
    GBP = "GBP"
    CHF = "CHF"
    EUR = "EUR"
    AUD = "AUD"
    NZD = "NZD"
    ZAR = "ZAR"
    DKK = "DKK"


class GroupCustomerAutomatedUserAssignmentStrategyEnum(str, Enum):
    """Allowed values for `GroupCustomer.properties.automated_user_assignment_strategy`."""

    RECOMMENDED = "RECOMMENDED"
    HOURS_PRIORITY = "HOURS_PRIORITY"
    DISTANCE = "DISTANCE"
    ROUND_ROBIN = "ROUND_ROBIN"
    PRIORITY_LIST = "PRIORITY_LIST"


class GroupCustomerAvailabilityStyleEnum(str, Enum):
    """Allowed values for `GroupCustomer.properties.availability_style`."""

    TIME = "TIME"
    TIME_OF_DAY = "TIME_OF_DAY"
    LEGACY = "LEGACY"


class GroupCustomerCurrencyEnum(str, Enum):
    """Allowed values for `GroupCustomer.properties.currency`."""

    USD = "USD"
    CAD = "CAD"
    GBP = "GBP"
    CHF = "CHF"
    EUR = "EUR"
    AUD = "AUD"
    NZD = "NZD"
    ZAR = "ZAR"
    DKK = "DKK"


class GroupCustomerTypeEnum(str, Enum):
    """Allowed values for `GroupCustomer.properties.type`."""

    CREATOR = "CREATOR"
    AGENT = "AGENT"
    BROKERAGE = "BROKERAGE"


class GroupCustomerVerificationStatusEnum(str, Enum):
    """Allowed values for `GroupCustomer.properties.verification_status`."""

    VERIFIED = "verified"
    UNVERIFIED = "unverified"
    NEW = "new"
    SSO = "sso"


class GroupObjectEnum(str, Enum):
    """Allowed values for `Group.properties.object`."""

    GROUP = "GROUP"


class GroupTypeEnum(str, Enum):
    """Allowed values for `Group.properties.type`."""

    CREATOR = "CREATOR"
    AGENT = "AGENT"
    BROKERAGE = "BROKERAGE"


class ImpersonatePostPayloadClientEnum(str, Enum):
    """Allowed values for `ImpersonatePostPayload.properties.client`."""

    IOS = "IOS"
    ANDROID = "ANDROID"
    PHPUNIT = "PHPUNIT"


class InteractiveContentContentTypeEnum(str, Enum):
    """Allowed values for `InteractiveContent.properties.content_type`."""

    MATTERPORT = "MATTERPORT"
    OTHER = "OTHER"


class InteractiveContentDisplayTypeEnum(str, Enum):
    """Allowed values for `InteractiveContent.properties.display_type`."""

    BRANDED = "BRANDED"
    UNBRANDED = "UNBRANDED"
    BOTH = "BOTH"


class ListingDeliveryStatusEnum(str, Enum):
    """Allowed values for `Listing.properties.delivery_status`."""

    DELIVERED = "DELIVERED"
    UNDELIVERED = "UNDELIVERED"
    SCHEDULED = "SCHEDULED"


class ListingMarketingContentObjectEnum(str, Enum):
    """Allowed values for `ListingMarketingContent.properties.object`."""

    LISTING = "LISTING"


class ListingMarketingContentStatusEnum(str, Enum):
    """Allowed values for `ListingMarketingContent.properties.status`."""

    DRAFT = "DRAFT"
    COMING_SOON = "COMING_SOON"
    FOR_SALE = "FOR_SALE"
    FOR_LEASE = "FOR_LEASE"
    PENDING_SALE = "PENDING_SALE"
    PENDING_LEASE = "PENDING_LEASE"
    FOR_RENT = "FOR_RENT"
    SOLD = "SOLD"
    LEASED = "LEASED"
    OFF_MARKET = "OFF_MARKET"


class ListingMarketingContentSubTypeEnum(str, Enum):
    """Allowed values for `ListingMarketingContent.properties.sub_type`."""

    SINGLE_FAMILY = "SINGLE_FAMILY"
    SINGLE_FAMILY_ATTACHED = "SINGLE_FAMILY_ATTACHED"
    SINGLE_FAMILY_DETACHED = "SINGLE_FAMILY_DETACHED"
    COLONIAL = "COLONIAL"
    CONDO = "CONDO"
    TOWNHOME = "TOWNHOME"
    TWINHOME = "TWINHOME"
    DUPLEX = "DUPLEX"
    LOT = "LOT"
    LAND = "LAND"
    MANUFACTURED_HOME = "MANUFACTURED_HOME"
    SEMI_DETACHED = "SEMI_DETACHED"
    MULTI_FAMILY = "MULTI_FAMILY"
    RENTAL = "RENTAL"
    ROW_HOUSE = "ROW_HOUSE"
    HORSE_FARM = "HORSE_FARM"
    OTHER = "OTHER"


class ListingObjectEnum(str, Enum):
    """Allowed values for `Listing.properties.object`."""

    LISTING = "LISTING"


class ListingPutPayloadPropertyTypeEnum(str, Enum):
    """Allowed values for `ListingPutPayload.properties.property_type`."""

    SINGLE_FAMILY = "Single Family"
    SINGLE_FAMILY_ATTACHED = "Single Family Attached"
    SINGLE_FAMILY_DETACHED = "Single Family Detached"
    COLONIAL = "Colonial"
    CONDO = "Condo"
    TOWNHOME = "Townhome"
    TWINHOME = "Twinhome"
    DUPLEX = "Duplex"
    LOT = "Lot"
    LAND = "Land"
    MANUFACTURED_HOME = "Manufactured Home"
    SEMI_DETACHED = "Semi-Detached"
    MULTI_FAMILY = "Multi Family"
    RENTAL = "Rental"
    ROW_HOUSE = "Row House"
    HORSE_FARM = "Horse Farm"
    OTHER = "Other"


class ListingStandardStatusEnum(str, Enum):
    """Allowed values for `Listing.properties.standard_status`."""

    ACTIVE = "ACTIVE"
    ACTIVE_UNDER_CONTRACT = "ACTIVE_UNDER_CONTRACT"
    CLOSED = "CLOSED"
    COMING_SOON = "COMING_SOON"
    HOLD = "HOLD"
    INCOMPLETE = "INCOMPLETE"


class ListingStatusEnum(str, Enum):
    """Allowed values for `Listing.properties.status`."""

    DRAFT = "DRAFT"
    COMING_SOON = "COMING_SOON"
    FOR_SALE = "FOR_SALE"
    FOR_LEASE = "FOR_LEASE"
    PENDING_SALE = "PENDING_SALE"
    PENDING_LEASE = "PENDING_LEASE"
    FOR_RENT = "FOR_RENT"
    SOLD = "SOLD"
    LEASED = "LEASED"
    OFF_MARKET = "OFF_MARKET"


class ListingSubTypeEnum(str, Enum):
    """Allowed values for `Listing.properties.sub_type`."""

    SINGLE_FAMILY = "SINGLE_FAMILY"
    SINGLE_FAMILY_ATTACHED = "SINGLE_FAMILY_ATTACHED"
    SINGLE_FAMILY_DETACHED = "SINGLE_FAMILY_DETACHED"
    COLONIAL = "COLONIAL"
    CONDO = "CONDO"
    TOWNHOME = "TOWNHOME"
    TWINHOME = "TWINHOME"
    DUPLEX = "DUPLEX"
    LOT = "LOT"
    LAND = "LAND"
    MANUFACTURED_HOME = "MANUFACTURED_HOME"
    SEMI_DETACHED = "SEMI_DETACHED"
    MULTI_FAMILY = "MULTI_FAMILY"
    RENTAL = "RENTAL"
    ROW_HOUSE = "ROW_HOUSE"
    HORSE_FARM = "HORSE_FARM"
    OTHER = "OTHER"


class ListingTypeEnum(str, Enum):
    """Allowed values for `Listing.properties.type`."""

    SINGLE_FAMILY = "SINGLE_FAMILY"
    SINGLE_FAMILY_ATTACHED = "SINGLE_FAMILY_ATTACHED"
    SINGLE_FAMILY_DETACHED = "SINGLE_FAMILY_DETACHED"
    COLONIAL = "COLONIAL"
    CONDO = "CONDO"
    TOWNHOME = "TOWNHOME"
    TWINHOME = "TWINHOME"
    DUPLEX = "DUPLEX"
    LOT = "LOT"
    LAND = "LAND"
    MANUFACTURED_HOME = "MANUFACTURED_HOME"
    SEMI_DETACHED = "SEMI_DETACHED"
    MULTI_FAMILY = "MULTI_FAMILY"
    RENTAL = "RENTAL"
    ROW_HOUSE = "ROW_HOUSE"
    HORSE_FARM = "HORSE_FARM"
    OTHER = "OTHER"


class LoginPostPayloadClientEnum(str, Enum):
    """Allowed values for `LoginPostPayload.properties.client`."""

    IOS = "IOS"
    ANDROID = "ANDROID"
    PHPUNIT = "PHPUNIT"


class LoginViaTokenPostPayloadClientEnum(str, Enum):
    """Allowed values for `LoginViaTokenPostPayload.properties.client`."""

    IOS = "IOS"
    ANDROID = "ANDROID"
    PHPUNIT = "PHPUNIT"


class MarketingMaterialObjectEnum(str, Enum):
    """Allowed values for `MarketingMaterial.properties.object`."""

    MARKETING_MATERIAL = "MARKETING_MATERIAL"


class MarketingMaterialTemplateObjectEnum(str, Enum):
    """Allowed values for `MarketingMaterialTemplate.properties.object`."""

    MARKETING_MATERIAL_TEMPLATE = "MARKETING_MATERIAL_TEMPLATE"


class MediaSearchResourceDataObjectEnum(str, Enum):
    """Allowed values for `MediaSearchResource.properties.data.properties.object`."""

    MEDIA_REQUEST_MEDIA_SEARCH = "MEDIA_REQUEST_MEDIA_SEARCH"


class NotificationPreference2NotificationTypeEnum(str, Enum):
    """Allowed values for `NotificationPreference-2.properties.notification_type`."""

    CREATOR_ORDER_RECEIVED = "CREATOR_ORDER_RECEIVED"
    CREATOR_ORDER_PAYMENT_PROCESSED = "CREATOR_ORDER_PAYMENT_PROCESSED"
    CREATOR_APPOINTMENT_SCHEDULED = "CREATOR_APPOINTMENT_SCHEDULED"
    CREATOR_APPOINTMENT_RESCHEDULED = "CREATOR_APPOINTMENT_RESCHEDULED"
    CREATOR_APPOINTMENT_CANCELED = "CREATOR_APPOINTMENT_CANCELED"
    CREATOR_APPOINTMENT_POSTPONED = "CREATOR_APPOINTMENT_POSTPONED"
    CREATOR_APPOINTMENT_ASSIGNED = "CREATOR_APPOINTMENT_ASSIGNED"
    CREATOR_APPOINTMENT_UNASSIGNED = "CREATOR_APPOINTMENT_UNASSIGNED"
    CREATOR_APPOINTMENT_REMINDER = "CREATOR_APPOINTMENT_REMINDER"
    CREATOR_CUSTOMER_TEAM_INVITATION = "CREATOR_CUSTOMER_TEAM_INVITATION"
    CREATOR_UPCOMING_APPOINTMENTS_SUMMARY = "CREATOR_UPCOMING_APPOINTMENTS_SUMMARY"
    CREATOR_EXPORT_READY = "CREATOR_EXPORT_READY"
    CREATOR_TEAM_MEMBER_INVITATION = "CREATOR_TEAM_MEMBER_INVITATION"
    LISTING_DELIVERY = "LISTING_DELIVERY"
    CUSTOMER_ORDER_CONFIRMATION = "CUSTOMER_ORDER_CONFIRMATION"
    CUSTOMER_ORDER_PAYMENT_REQUIRED = "CUSTOMER_ORDER_PAYMENT_REQUIRED"
    CUSTOMER_APPOINTMENT_SCHEDULED = "CUSTOMER_APPOINTMENT_SCHEDULED"
    CUSTOMER_APPOINTMENT_RESCHEDULED = "CUSTOMER_APPOINTMENT_RESCHEDULED"
    CUSTOMER_APPOINTMENT_CANCELED = "CUSTOMER_APPOINTMENT_CANCELED"
    CUSTOMER_APPOINTMENT_POSTPONED = "CUSTOMER_APPOINTMENT_POSTPONED"
    CUSTOMER_APPOINTMENT_REMINDER = "CUSTOMER_APPOINTMENT_REMINDER"
    CUSTOMER_NEW_LEAD = "CUSTOMER_NEW_LEAD"
    CUSTOMER_TEAM_INVITATION = "CUSTOMER_TEAM_INVITATION"
    CUSTOMER_USER_VERIFICATION = "CUSTOMER_USER_VERIFICATION"
    CUSTOMER_USER_RESET_PASSWORD = "CUSTOMER_USER_RESET_PASSWORD"
    CUSTOMER_USER_ACTIVATION = "CUSTOMER_USER_ACTIVATION"
    PORTAL_CUSTOM = "PORTAL_CUSTOM"


class NotificationPreference2ObjectEnum(str, Enum):
    """Allowed values for `NotificationPreference-2.properties.object`."""

    APP_NOTIFICATIONS_MODELS_NOTIFICATIONCHANNEL = (
        "APP\\NOTIFICATIONS\\MODELS\\NOTIFICATIONCHANNEL"
    )


class NotificationPreferenceChannelsEnum(str, Enum):
    """Allowed values for `NotificationPreference.properties.channels.items`."""

    EMAIL = "email"
    SMS = "sms"
    IN_APP = "in_app"
    PUSH = "push"


class NotificationPreferenceNotificationTypeEnum(str, Enum):
    """Allowed values for `NotificationPreference.properties.notification_type`."""

    CREATOR_ORDER_RECEIVED = "CREATOR_ORDER_RECEIVED"
    CREATOR_ORDER_PAYMENT_PROCESSED = "CREATOR_ORDER_PAYMENT_PROCESSED"
    CREATOR_APPOINTMENT_SCHEDULED = "CREATOR_APPOINTMENT_SCHEDULED"
    CREATOR_APPOINTMENT_RESCHEDULED = "CREATOR_APPOINTMENT_RESCHEDULED"
    CREATOR_APPOINTMENT_CANCELED = "CREATOR_APPOINTMENT_CANCELED"
    CREATOR_APPOINTMENT_POSTPONED = "CREATOR_APPOINTMENT_POSTPONED"
    CREATOR_APPOINTMENT_ASSIGNED = "CREATOR_APPOINTMENT_ASSIGNED"
    CREATOR_APPOINTMENT_UNASSIGNED = "CREATOR_APPOINTMENT_UNASSIGNED"
    CREATOR_APPOINTMENT_REMINDER = "CREATOR_APPOINTMENT_REMINDER"
    CREATOR_CUSTOMER_TEAM_INVITATION = "CREATOR_CUSTOMER_TEAM_INVITATION"
    CREATOR_UPCOMING_APPOINTMENTS_SUMMARY = "CREATOR_UPCOMING_APPOINTMENTS_SUMMARY"
    CREATOR_EXPORT_READY = "CREATOR_EXPORT_READY"
    CREATOR_TEAM_MEMBER_INVITATION = "CREATOR_TEAM_MEMBER_INVITATION"
    LISTING_DELIVERY = "LISTING_DELIVERY"
    CUSTOMER_ORDER_CONFIRMATION = "CUSTOMER_ORDER_CONFIRMATION"
    CUSTOMER_ORDER_PAYMENT_REQUIRED = "CUSTOMER_ORDER_PAYMENT_REQUIRED"
    CUSTOMER_APPOINTMENT_SCHEDULED = "CUSTOMER_APPOINTMENT_SCHEDULED"
    CUSTOMER_APPOINTMENT_RESCHEDULED = "CUSTOMER_APPOINTMENT_RESCHEDULED"
    CUSTOMER_APPOINTMENT_CANCELED = "CUSTOMER_APPOINTMENT_CANCELED"
    CUSTOMER_APPOINTMENT_POSTPONED = "CUSTOMER_APPOINTMENT_POSTPONED"
    CUSTOMER_APPOINTMENT_REMINDER = "CUSTOMER_APPOINTMENT_REMINDER"
    CUSTOMER_NEW_LEAD = "CUSTOMER_NEW_LEAD"
    CUSTOMER_TEAM_INVITATION = "CUSTOMER_TEAM_INVITATION"
    CUSTOMER_USER_VERIFICATION = "CUSTOMER_USER_VERIFICATION"
    CUSTOMER_USER_RESET_PASSWORD = "CUSTOMER_USER_RESET_PASSWORD"
    CUSTOMER_USER_ACTIVATION = "CUSTOMER_USER_ACTIVATION"
    PORTAL_CUSTOM = "PORTAL_CUSTOM"


class NotificationPreferenceObjectEnum(str, Enum):
    """Allowed values for `NotificationPreference.properties.object`."""

    APP_NOTIFICATIONS_MODELS_NOTIFICATIONCHANNEL = (
        "APP\\NOTIFICATIONS\\MODELS\\NOTIFICATIONCHANNEL"
    )


class OrderCurrencyEnum(str, Enum):
    """Allowed values for `Order.properties.currency`."""

    USD = "USD"
    CAD = "CAD"
    GBP = "GBP"
    CHF = "CHF"
    EUR = "EUR"
    AUD = "AUD"
    NZD = "NZD"
    ZAR = "ZAR"


class OrderFormAutomatedUserAssignmentStrategyEnum(str, Enum):
    """Allowed values for `OrderForm.properties.automated_user_assignment_strategy`."""

    RECOMMENDED = "RECOMMENDED"
    HOURS_PRIORITY = "HOURS_PRIORITY"
    DISTANCE = "DISTANCE"
    ROUND_ROBIN = "ROUND_ROBIN"
    PRIORITY_LIST = "PRIORITY_LIST"


class OrderFormAvailabilityStyleEnum(str, Enum):
    """Allowed values for `OrderForm.properties.availability_style`."""

    TIME = "TIME"
    TIME_OF_DAY = "TIME_OF_DAY"
    LEGACY = "LEGACY"
    DATETIME_PICKER = "DATETIME_PICKER"


class OrderFormObjectEnum(str, Enum):
    """Allowed values for `OrderForm.properties.object`."""

    ORDER_FORM = "ORDER_FORM"


class OrderFormSessionObjectEnum(str, Enum):
    """Allowed values for `OrderFormSession.properties.object`."""

    ORDER_FORM_SESSION = "ORDER_FORM_SESSION"


class OrderFormTypeEnum(str, Enum):
    """Allowed values for `OrderForm.properties.type`."""

    ARYEO = "ARYEO"
    EXTERNAL = "EXTERNAL"


class OrderFulfillmentStatusEnum(str, Enum):
    """Allowed values for `Order.properties.fulfillment_status`."""

    FULFILLED = "FULFILLED"
    UNFULFILLED = "UNFULFILLED"


class OrderItemObjectEnum(str, Enum):
    """Allowed values for `OrderItem.properties.object`."""

    ORDER_ITEM = "ORDER_ITEM"


class OrderItemPurchasableTypeEnum(str, Enum):
    """Allowed values for `OrderItem.properties.purchasable_type`."""

    PRODUCT_VARIANT = "PRODUCT_VARIANT"
    FEE = "FEE"
    CUSTOM = "CUSTOM"


class OrderObjectEnum(str, Enum):
    """Allowed values for `Order.properties.object`."""

    ORDER = "ORDER"


class OrderOrderStatusEnum(str, Enum):
    """Allowed values for `Order.properties.order_status`."""

    DRAFT = "DRAFT"
    OPEN = "OPEN"
    CANCELED = "CANCELED"


class OrderPaymentObjectEnum(str, Enum):
    """Allowed values for `OrderPayment.properties.object`."""

    ORDER_PAYMENT = "ORDER_PAYMENT"


class OrderPaymentStatusEnum(str, Enum):
    """Allowed values for `Order.properties.payment_status`."""

    PAID = "PAID"
    PARTIALLY_PAID = "PARTIALLY_PAID"
    UNPAID = "UNPAID"


class OrderPaymentTypeEnum(str, Enum):
    """Allowed values for `OrderPayment.properties.type`."""

    MANUAL = "MANUAL"
    CREDIT = "CREDIT"
    CHECKOUT = "CHECKOUT"


class OrderPostPayloadFulfillmentStatusEnum(str, Enum):
    """Allowed values for `OrderPostPayload.properties.fulfillment_status`."""

    FULFILLED = "FULFILLED"
    UNFULFILLED = "UNFULFILLED"


class OrderRefundObjectEnum(str, Enum):
    """Allowed values for `OrderRefund.properties.object`."""

    ORDER_REFUND = "ORDER_REFUND"


class OrderRefundPostPayloadReasonEnum(str, Enum):
    """Allowed values for `OrderRefundPostPayload.properties.reason`."""

    DUPLICATE = "duplicate"
    REQUESTED_BY_CUSTOMER = "requested_by_customer"
    FRAUDULENT = "fraudulent"
    EXTERNAL = "external"


class OrderRefundReasonEnum(str, Enum):
    """Allowed values for `OrderRefund.properties.reason`."""

    DUPLICATE = "DUPLICATE"
    REQUESTED_BY_CUSTOMER = "REQUESTED_BY_CUSTOMER"
    FRAUDULENT = "FRAUDULENT"
    EXTERNAL = "EXTERNAL"


class OrderSchedulingAssignmentStrategyEnum(str, Enum):
    """Allowed values for `Order.properties.scheduling_assignment_strategy`."""

    RECOMMENDED = "RECOMMENDED"
    HOURS_PRIORITY = "HOURS_PRIORITY"
    DISTANCE = "DISTANCE"
    ROUND_ROBIN = "ROUND_ROBIN"
    PRIORITY_LIST = "PRIORITY_LIST"


class OrderStatusEnum(str, Enum):
    """Allowed values for `Order.properties.status`."""

    CONFIRMED = "CONFIRMED"
    GHOST = "GHOST"


class PayRunItemAmountOverrideAmountTypeEnum(str, Enum):
    """Allowed values for `PayRunItemAmountOverride.properties.amount_type`."""

    FLAT = "flat"
    PERCENTAGE = "percentage"


class PaymentCollectionSourceEnum(str, Enum):
    """Allowed values for `Payment.properties.collection_source`."""

    PAYPAL = "PAYPAL"
    VENMO = "VENMO"
    STRIPE = "STRIPE"
    SQUARE = "SQUARE"
    QUICKBOOKS = "QUICKBOOKS"
    CONCIERGE = "CONCIERGE"
    CASH = "CASH"
    CHECK = "CHECK"
    OTHER = "OTHER"


class PaymentGatewayObjectEnum(str, Enum):
    """Allowed values for `PaymentGateway.properties.object`."""

    INTEGRATION = "INTEGRATION"


class PaymentInfoObjectEnum(str, Enum):
    """Allowed values for `PaymentInfo.properties.object`."""

    PAYMENT_INFO = "PAYMENT_INFO"


class PaymentObjectEnum(str, Enum):
    """Allowed values for `Payment.properties.object`."""

    ORDER_PAYMENT = "ORDER_PAYMENT"


class PaymentTypeEnum(str, Enum):
    """Allowed values for `Payment.properties.type`."""

    MANUAL = "MANUAL"
    CREDIT = "CREDIT"
    CHECKOUT = "CHECKOUT"


class PortalAppConfigObjectEnum(str, Enum):
    """Allowed values for `PortalAppConfig.properties.object`."""

    PORTAL_APP_CONFIG = "PORTAL_APP_CONFIG"


class PortalAppConfigPrimaryStatusEnum(str, Enum):
    """Allowed values for `PortalAppConfig.properties.primary_status`."""

    INFO_SUBMITTED = "INFO_SUBMITTED"
    READY_TO_BUILD = "READY_TO_BUILD"
    IN_REVIEW = "IN_REVIEW"
    LIVE = "LIVE"
    LIVE_NEEDS_TRANSFER = "LIVE_NEEDS_TRANSFER"
    DISCONTINUED = "DISCONTINUED"


class PortalAppConfigPutPayloadPrimaryStatusEnum(str, Enum):
    """Allowed values for `PortalAppConfigPutPayload.properties.primary_status`."""

    INFO_SUBMITTED = "INFO_SUBMITTED"
    READY_TO_BUILD = "READY_TO_BUILD"
    IN_REVIEW = "IN_REVIEW"
    LIVE = "LIVE"
    LIVE_NEEDS_TRANSFER = "LIVE_NEEDS_TRANSFER"
    DISCONTINUED = "DISCONTINUED"


class PortalAppRevisionObjectEnum(str, Enum):
    """Allowed values for `PortalAppRevision.properties.object`."""

    APP_PORTALAPPS_MODELS_PORTALAPPREVISION = (
        "APP\\PORTALAPPS\\MODELS\\PORTALAPPREVISION"
    )


class PortalCustomerRegisterPostPayloadClientEnum(str, Enum):
    """Allowed values for `PortalCustomerRegisterPostPayload.properties.client`."""

    IOS = "IOS"
    ANDROID = "ANDROID"
    PHPUNIT = "PHPUNIT"


class PortalCustomerVerifyPostPayloadClientEnum(str, Enum):
    """Allowed values for `PortalCustomerVerifyPostPayload.properties.client`."""

    IOS = "IOS"
    ANDROID = "ANDROID"
    PHPUNIT = "PHPUNIT"


class ProductCategoryObjectEnum(str, Enum):
    """Allowed values for `ProductCategory.properties.object`."""

    PRODUCT_CATEGORY = "PRODUCT_CATEGORY"


class ProductObjectEnum(str, Enum):
    """Allowed values for `Product.properties.object`."""

    PRODUCT = "PRODUCT"


class ProductTypeEnum(str, Enum):
    """Allowed values for `Product.properties.type`."""

    MAIN = "MAIN"
    ADDON = "ADDON"


class ProductVariantObjectEnum(str, Enum):
    """Allowed values for `ProductVariant.properties.object`."""

    PRODUCT_VARIANT = "PRODUCT_VARIANT"


class RegionTypeEnum(str, Enum):
    """Allowed values for `Region.properties.type`."""

    COUNTRY = "COUNTRY"
    STATE = "STATE"
    COUNTY = "COUNTY"


class ReviewPostPayloadSourceTypeEnum(str, Enum):
    """Allowed values for `ReviewPostPayload.properties.source_type`."""

    IOS = "ios"
    ANDROID = "android"
    WEB = "web"


class ReviewSourceTypeEnum(str, Enum):
    """Allowed values for `Review.properties.source_type`."""

    IOS = "ios"
    ANDROID = "android"
    WEB = "web"


class SavedViewFilterObjectEnum(str, Enum):
    """Allowed values for `SavedViewFilter.properties.object`."""

    SAVED_VIEW_FILTER = "SAVED_VIEW_FILTER"


class SavedViewFilterTypeEnum(str, Enum):
    """Allowed values for `SavedViewFilter.properties.type`."""

    DELIVERY_STATUS = "delivery_status"
    PAYMENT_STATUS = "payment_status"


class SavedViewObjectEnum(str, Enum):
    """Allowed values for `SavedView.properties.object`."""

    SAVED_VIEW = "SAVED_VIEW"


class SavedViewOwnerTypeEnum(str, Enum):
    """Allowed values for `SavedView.properties.owner_type`."""

    COMPANY = "company"
    COMPANY_TEAM_MEMBER = "company_team_member"


class SavedViewPatchPayloadFiltersTypeEnum(str, Enum):
    """Allowed values for `SavedViewPatchPayload.properties.filters.items.properties.type`."""

    DELIVERY_STATUS = "delivery_status"
    PAYMENT_STATUS = "payment_status"


class SavedViewPatchPayloadOwnerTypeEnum(str, Enum):
    """Allowed values for `SavedViewPatchPayload.properties.owner_type`."""

    COMPANY = "company"
    COMPANY_TEAM_MEMBER = "company_team_member"


class SavedViewPatchPayloadScopeEnum(str, Enum):
    """Allowed values for `SavedViewPatchPayload.properties.scope`."""

    LISTING = "listing"
    ORDER = "order"


class SavedViewPostPayloadFiltersTypeEnum(str, Enum):
    """Allowed values for `SavedViewPostPayload.properties.filters.items.properties.type`."""

    DELIVERY_STATUS = "delivery_status"
    PAYMENT_STATUS = "payment_status"


class SavedViewPostPayloadOwnerTypeEnum(str, Enum):
    """Allowed values for `SavedViewPostPayload.properties.owner_type`."""

    COMPANY = "company"
    COMPANY_TEAM_MEMBER = "company_team_member"


class SavedViewPostPayloadScopeEnum(str, Enum):
    """Allowed values for `SavedViewPostPayload.properties.scope`."""

    LISTING = "listing"
    ORDER = "order"


class SavedViewScopeEnum(str, Enum):
    """Allowed values for `SavedView.properties.scope`."""

    LISTING = "listing"
    ORDER = "order"


class SavedViewViewAccessEnum(str, Enum):
    """Allowed values for `SavedView.properties.view_access`."""

    WHOLE_TEAM = "Whole team"
    ONLY_ME = "Only me"


class TagObjectEnum(str, Enum):
    """Allowed values for `Tag.properties.object`."""

    APP_TAGS_MODELS_TAG = "APP\\TAGS\\MODELS\\TAG"


class TagOnlyPostPayloadTypeEnum(str, Enum):
    """Allowed values for `TagOnlyPostPayload.properties.type`."""

    ORDER = "order"
    CUSTOMER_TEAM = "customer_team"
    PRODUCT = "product"
    ORDER_FORM = "order_form"
    VIRTUAL_STAGING_AI = "virtual_staging_ai"


class TagTypeEnum(str, Enum):
    """Allowed values for `Tag.properties.type`."""

    ORDER = "order"
    CUSTOMER_TEAM = "customer_team"
    PRODUCT = "product"
    ORDER_FORM = "order_form"
    VIRTUAL_STAGING_AI = "virtual_staging_ai"


class TagsPostPayloadTagTypeEnum(str, Enum):
    """Allowed values for `TagsPostPayload.properties.tag.properties.type`."""

    ORDER = "order"
    CUSTOMER_TEAM = "customer_team"
    PRODUCT = "product"
    ORDER_FORM = "order_form"
    VIRTUAL_STAGING_AI = "virtual_staging_ai"


class TaskTemplateDefaultPayRunItemAmountTypeEnum(str, Enum):
    """Allowed values for `TaskTemplate.properties.default_pay_run_item_amount_type`."""

    FLAT = "flat"
    PERCENTAGE = "percentage"


class TerritoryObjectEnum(str, Enum):
    """Allowed values for `Territory.properties.object`."""

    TERRITORY = "TERRITORY"


class UserStatusEnum(str, Enum):
    """Allowed values for `User.properties.status`."""

    ACTIVE = "active"
    INACTIVE = "inactive"
    NEW = "new"
    SSO = "sso"


class UserVerificationStatusEnum(str, Enum):
    """Allowed values for `User.properties.verification_status`."""

    VERIFIED = "verified"
    UNVERIFIED = "unverified"
    NEW = "new"
    SSO = "sso"


class VideoDisplayTypeEnum(str, Enum):
    """Allowed values for `Video.properties.display_type`."""

    BRANDED = "BRANDED"
    UNBRANDED = "UNBRANDED"
    BOTH = "BOTH"
    NONE = "NONE"


class VideoObjectEnum(str, Enum):
    """Allowed values for `Video.properties.object`."""

    VIDEO = "VIDEO"


class VideoSourceTypeEnum(str, Enum):
    """Allowed values for `Video.properties.source_type`."""

    YOUTUBE = "YOUTUBE"
    VIMEO = "VIMEO"
    OPTIMIZED = "OPTIMIZED"
    UPLOADED = "UPLOADED"
    LINK = "LINK"


__all__ = [
    "ActivityNameEnum",
    "ActivityPostPayloadNameEnum",
    "ActivityPostPayloadResourceTypeEnum",
    "ActivityPostPayloadSourceEnum",
    "ActivitySourceEnum",
    "AddressPatchPayloadExternalTypeEnum",
    "AddressPredictionResultExternalTypeEnum",
    "AddressSearchResultExternalTypeEnum",
    "AppointmentAttendanceObjectEnum",
    "AppointmentPreferenceTypeEnum",
    "AppointmentPreferredStartAtTimeOfDayEnum",
    "AppointmentStatusEnum",
    "AuthActivationStageResourceStatusEnum",
    "BookingLimitsAutomatedUserAssignmentStrategyEnum",
    "BookingLimitsAvailabilityStyleEnum",
    "BookingLimitsObjectEnum",
    "CalendarBlockTypeEnum",
    "CalendarEventTypeEnum",
    "CompanyTeamMemberObjectEnum",
    "CompanyTeamMemberPermissionNameEnum",
    "CompanyTeamMemberPermissionObjectEnum",
    "CompanyTeamMemberResourceStrategyTypeEnum",
    "CompanyTeamMemberRoleEnum",
    "CompanyTeamMemberStatusEnum",
    "CreditTransactionTypeEnum",
    "CustomerGroupObjectEnum",
    "CustomerGroupStatusEnum",
    "CustomerTeamMembershipObjectEnum",
    "CustomerTeamMembershipRoleEnum",
    "CustomerTeamMembershipStatusEnum",
    "CustomerUserPostPayloadRoleEnum",
    "CustomerUserStatusEnum",
    "CustomerUserVerificationStatusEnum",
    "DeleteUserPostPayloadClientEnum",
    "DiscountAmountObjectEnum",
    "DiscountObjectEnum",
    "EsoftOrderLineObjectEnum",
    "EsoftOrderLineStatusEnum",
    "FeatureFlagsEnum",
    "FeeObjectEnum",
    "FeeTypeEnum",
    "FileDisplayTypeEnum",
    "FloorPlanObjectEnum",
    "GroupAutomatedUserAssignmentStrategyEnum",
    "GroupAvailabilityStyleEnum",
    "GroupCurrencyEnum",
    "GroupCustomerAutomatedUserAssignmentStrategyEnum",
    "GroupCustomerAvailabilityStyleEnum",
    "GroupCustomerCurrencyEnum",
    "GroupCustomerTypeEnum",
    "GroupCustomerVerificationStatusEnum",
    "GroupObjectEnum",
    "GroupTypeEnum",
    "ImpersonatePostPayloadClientEnum",
    "InteractiveContentContentTypeEnum",
    "InteractiveContentDisplayTypeEnum",
    "ListingDeliveryStatusEnum",
    "ListingMarketingContentObjectEnum",
    "ListingMarketingContentStatusEnum",
    "ListingMarketingContentSubTypeEnum",
    "ListingObjectEnum",
    "ListingPutPayloadPropertyTypeEnum",
    "ListingStandardStatusEnum",
    "ListingStatusEnum",
    "ListingSubTypeEnum",
    "ListingTypeEnum",
    "LoginPostPayloadClientEnum",
    "LoginViaTokenPostPayloadClientEnum",
    "MarketingMaterialObjectEnum",
    "MarketingMaterialTemplateObjectEnum",
    "MediaSearchResourceDataObjectEnum",
    "NotificationPreference2NotificationTypeEnum",
    "NotificationPreference2ObjectEnum",
    "NotificationPreferenceChannelsEnum",
    "NotificationPreferenceNotificationTypeEnum",
    "NotificationPreferenceObjectEnum",
    "OrderCurrencyEnum",
    "OrderFormAutomatedUserAssignmentStrategyEnum",
    "OrderFormAvailabilityStyleEnum",
    "OrderFormObjectEnum",
    "OrderFormSessionObjectEnum",
    "OrderFormTypeEnum",
    "OrderFulfillmentStatusEnum",
    "OrderItemObjectEnum",
    "OrderItemPurchasableTypeEnum",
    "OrderObjectEnum",
    "OrderOrderStatusEnum",
    "OrderPaymentObjectEnum",
    "OrderPaymentStatusEnum",
    "OrderPaymentTypeEnum",
    "OrderPostPayloadFulfillmentStatusEnum",
    "OrderRefundObjectEnum",
    "OrderRefundPostPayloadReasonEnum",
    "OrderRefundReasonEnum",
    "OrderSchedulingAssignmentStrategyEnum",
    "OrderStatusEnum",
    "PayRunItemAmountOverrideAmountTypeEnum",
    "PaymentCollectionSourceEnum",
    "PaymentGatewayObjectEnum",
    "PaymentInfoObjectEnum",
    "PaymentObjectEnum",
    "PaymentTypeEnum",
    "PortalAppConfigObjectEnum",
    "PortalAppConfigPrimaryStatusEnum",
    "PortalAppConfigPutPayloadPrimaryStatusEnum",
    "PortalAppRevisionObjectEnum",
    "PortalCustomerRegisterPostPayloadClientEnum",
    "PortalCustomerVerifyPostPayloadClientEnum",
    "ProductCategoryObjectEnum",
    "ProductObjectEnum",
    "ProductTypeEnum",
    "ProductVariantObjectEnum",
    "RegionTypeEnum",
    "ReviewPostPayloadSourceTypeEnum",
    "ReviewSourceTypeEnum",
    "SavedViewFilterObjectEnum",
    "SavedViewFilterTypeEnum",
    "SavedViewObjectEnum",
    "SavedViewOwnerTypeEnum",
    "SavedViewPatchPayloadFiltersTypeEnum",
    "SavedViewPatchPayloadOwnerTypeEnum",
    "SavedViewPatchPayloadScopeEnum",
    "SavedViewPostPayloadFiltersTypeEnum",
    "SavedViewPostPayloadOwnerTypeEnum",
    "SavedViewPostPayloadScopeEnum",
    "SavedViewScopeEnum",
    "SavedViewViewAccessEnum",
    "TagObjectEnum",
    "TagOnlyPostPayloadTypeEnum",
    "TagTypeEnum",
    "TagsPostPayloadTagTypeEnum",
    "TaskTemplateDefaultPayRunItemAmountTypeEnum",
    "TerritoryObjectEnum",
    "UserStatusEnum",
    "UserVerificationStatusEnum",
    "VideoDisplayTypeEnum",
    "VideoObjectEnum",
    "VideoSourceTypeEnum",
]
