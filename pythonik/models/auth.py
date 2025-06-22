"""
Iconik Auth Models
This module contains Pydantic models for the Iconik Auth API.
"""

from __future__ import annotations

from datetime import datetime
from typing import (
    Any,
    Dict,
    List,
    Literal,
    Optional,
    Union,
)

from pydantic import (
    BaseModel,
    Field,
    HttpUrl,
)


class WebflowContentSchema(BaseModel):
    """Represents a WebflowContentSchema in the Iconik system."""

    caption: Optional[str] = None
    category: Optional[str] = None
    image: Optional[str] = None
    name: Optional[str] = None
    slug: str


class VerificationResponseSchema(BaseModel):
    """Represents a VerificationResponseSchema in the Iconik system."""

    auto_login: Optional[bool] = None
    domain_data: Optional["SystemDomainFromTemplateSchema"] = None
    login_data: Optional["AutoLoginSchema"] = None


class UserSystemDomainInviteSchema(BaseModel):
    """Represents a UserSystemDomainInviteSchema in the Iconik system."""

    id: str
    is_existing_user_invitation: Optional[bool] = None
    system_domain_id: str


class TokensSchema(BaseModel):
    """Represents a TokensSchema in the Iconik system."""

    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[List["TokenOutputSchema"]] = Field(default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    total: Optional[int] = Field(None,
                                 ge=-9223372036854775808,
                                 le=9223372036854775807)


class TokenSchema(BaseModel):
    """Represents a TokenSchema in the Iconik system."""

    app_id: Optional[str] = None
    auth_system_domains: Optional[List["MultiDomainUserSystemSchema"]] = Field(
        default_factory=list)
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    expires: Optional[datetime] = None
    id: Optional[str] = None
    is_admin: Optional[bool] = None
    is_mfa_authenticated: Optional[bool] = None
    is_super_admin: Optional[bool] = None
    is_super_admin_light: Optional[bool] = None
    system_domain_id: Optional[str] = None
    system_domain_is_plg: Optional[bool] = None
    system_domain_status: Optional[Literal["ACTIVE", "WARNING", "FROZEN",
                                           "DEACTIVATED"]] = None
    system_domain_type: Optional[str] = None
    system_domain_warning_message: Optional[str] = None
    system_domains: Optional[List[str]] = Field(default_factory=list)
    token: str
    user_id: Optional[str] = None


class TokenOutputSchema(BaseModel):
    """Represents a TokenOutputSchema in the Iconik system."""

    app_id: Optional[str] = None
    auth_system_domains: Optional[List["MultiDomainUserSystemSchema"]] = Field(
        default_factory=list)
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    expires: Optional[datetime] = None
    id: Optional[str] = None
    is_admin: Optional[bool] = None
    is_mfa_authenticated: Optional[bool] = None
    is_super_admin: Optional[bool] = None
    is_super_admin_light: Optional[bool] = None
    system_domain_id: Optional[str] = None
    system_domain_is_plg: Optional[bool] = None
    system_domain_status: Optional[Literal["ACTIVE", "WARNING", "FROZEN",
                                           "DEACTIVATED"]] = None
    system_domain_type: Optional[str] = None
    system_domain_warning_message: Optional[str] = None
    system_domains: Optional[List[str]] = Field(default_factory=list)
    user_id: Optional[str] = None


class TokenMultiplatformLoginSchema(BaseModel):
    """Represents a TokenMultiplatformLoginSchema in the Iconik system."""

    app_id: Optional[str] = None
    auth_system_domains: Optional[
        List["MultiPlatformDomainUserSystemSchema"]] = Field(
            default_factory=list)
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    expires: Optional[datetime] = None
    id: Optional[str] = None
    is_admin: Optional[bool] = None
    is_mfa_authenticated: Optional[bool] = None
    is_super_admin: Optional[bool] = None
    is_super_admin_light: Optional[bool] = None
    system_domain_id: Optional[str] = None
    system_domain_is_plg: Optional[bool] = None
    system_domain_status: Optional[Literal["ACTIVE", "WARNING", "FROZEN",
                                           "DEACTIVATED"]] = None
    system_domain_type: Optional[str] = None
    system_domain_warning_message: Optional[str] = None
    system_domains: Optional[List[str]] = Field(default_factory=list)
    token: Optional[str] = Field(
        None,
        description=
        "Deprecated field. Use the token field from the `auth_system_domains` items instead.",  # pylint: disable=line-too-long
    )
    user_id: Optional[str] = None


class TokenBaseSchema(BaseModel):
    """Represents a TokenBaseSchema in the Iconik system."""

    app_id: Optional[str] = None
    auth_system_domains: Optional[List["MultiDomainUserSystemSchema"]] = Field(
        default_factory=list)
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    expires: Optional[datetime] = None
    id: Optional[str] = None
    is_admin: Optional[bool] = None
    is_mfa_authenticated: Optional[bool] = None
    is_super_admin: Optional[bool] = None
    is_super_admin_light: Optional[bool] = None
    system_domain_id: Optional[str] = None
    system_domain_is_plg: Optional[bool] = None
    system_domain_status: Optional[Literal["ACTIVE", "WARNING", "FROZEN",
                                           "DEACTIVATED"]] = None
    system_domain_type: Optional[str] = None
    system_domain_warning_message: Optional[str] = None
    system_domains: Optional[List[str]] = Field(default_factory=list)
    user_id: Optional[str] = None


class TemporaryPasswordTokenSchema(BaseModel):
    """Represents a TemporaryPasswordTokenSchema in the Iconik system."""

    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    email: str
    expires: Optional[datetime] = None
    id: Optional[str] = None
    token: str


class SystemDomainsSchema(BaseModel):
    """Represents a SystemDomainsSchema in the Iconik system."""

    objects: Optional[List["SystemDomainSchema"]] = Field(default_factory=list)


class SystemDomainSuperAdminSchema(BaseModel):
    """Represents a SystemDomainSuperAdminSchema in the Iconik system."""

    base_url: str
    billing_limits: Optional[Any] = None
    billing_tier: Optional[Literal["PAYGO", "PRO", "ENTERPRISE"]] = None
    country: Optional[str] = None
    creating_user_id: Optional[str] = None
    custom_terms: Optional[bool] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    deactivate_date: Optional[datetime] = None
    description: Optional[str] = None
    disable_billing_page: Optional[bool] = None
    discount_percent: Optional[float] = None
    do_not_charge_edge_transcoder: Optional[bool] = None
    do_not_charge_remote_proxies: Optional[bool] = None
    do_not_charge_shield: Optional[bool] = None
    features: Optional[List[str]] = Field(default_factory=list)
    freeze_date: Optional[datetime] = None
    has_preloaded_assets: Optional[bool] = None
    id: Optional[str] = None
    invoice_end_of_month: Optional[bool] = None
    is_plg: Optional[bool] = None
    is_template: Optional[bool] = None
    marketplace_customer_id: Optional[str] = None
    marketplace_entitlement_id: Optional[str] = None
    name: str
    ordway_customer_id: Optional[str] = None
    ordway_subscription_id: Optional[str] = None
    price_list: Optional[str] = None
    referral_code: Optional[str] = None
    sales_force_id: Optional[str] = None
    status: Optional[Literal["ACTIVE", "WARNING", "FROZEN",
                             "DEACTIVATED"]] = None  # fmt: skip
    stripe_id: Optional[str] = None
    type: Optional[Literal["TRIAL", "CUSTOMER", "PARTNER", "INTERNAL"]] = None
    warning_message: Optional[str] = None


class SystemDomainSchema(BaseModel):
    """Represents a SystemDomainSchema in the Iconik system."""

    base_url: str
    billing_limits: Optional[Any] = None
    billing_tier: Optional[Literal["PAYGO", "PRO", "ENTERPRISE"]] = None
    country: Optional[str] = None
    creating_user_id: Optional[str] = None
    custom_terms: Optional[bool] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    deactivate_date: Optional[datetime] = None
    description: Optional[str] = None
    disable_billing_page: Optional[bool] = None
    discount_percent: Optional[float] = None
    do_not_charge_edge_transcoder: Optional[bool] = None
    do_not_charge_remote_proxies: Optional[bool] = None
    do_not_charge_shield: Optional[bool] = None
    features: Optional[List[str]] = Field(default_factory=list)
    freeze_date: Optional[datetime] = None
    has_preloaded_assets: Optional[bool] = None
    id: Optional[str] = None
    invoice_end_of_month: Optional[bool] = None
    is_plg: Optional[bool] = None
    is_template: Optional[bool] = None
    marketplace_customer_id: Optional[str] = None
    marketplace_entitlement_id: Optional[str] = None
    name: str
    ordway_customer_id: Optional[str] = None
    ordway_subscription_id: Optional[str] = None
    price_list: Optional[str] = None
    referral_code: Optional[str] = None
    sales_force_id: Optional[str] = None
    status: Optional[Literal["ACTIVE", "WARNING", "FROZEN",
                             "DEACTIVATED"]] = None  # fmt: skip
    stripe_id: Optional[str] = None
    type: Optional[Literal["TRIAL", "CUSTOMER", "PARTNER", "INTERNAL"]] = None
    warning_message: Optional[str] = None


class SystemDomainFromTemplateSchema(BaseModel):
    """Represents a SystemDomainFromTemplateSchema in the Iconik system."""

    admin_email: str
    admin_first_name: Optional[str] = None
    admin_id: Optional[str] = None
    admin_last_name: Optional[str] = None
    admin_password: Optional[str] = None
    base_url: Optional[str] = None
    billing_tier: Optional[Literal["PAYGO", "PRO", "ENTERPRISE"]] = None
    custom_terms: Optional[bool] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    description: Optional[str] = None
    id: Optional[str] = None
    name: str
    status: Optional[Literal["ACTIVE", "WARNING", "FROZEN",
                             "DEACTIVATED"]] = None  # fmt: skip
    type: Optional[Literal["TRIAL", "CUSTOMER", "PARTNER", "INTERNAL"]] = None


class SystemDomainFromReferralCodeSchema(BaseModel):
    """Represents a SystemDomainFromReferralCodeSchema in the Iconik system."""

    admin_email: str
    admin_first_name: str
    admin_last_name: Optional[str] = None
    admin_password: str
    billing_tier: Optional[Literal["PAYGO", "PRO", "ENTERPRISE"]] = None
    country_code: str
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    description: Optional[str] = None
    id: Optional[str] = None
    name: str


class SimpleLoginSchema(BaseModel):
    """Represents a SimpleLoginSchema in the Iconik system."""

    app_name: Optional[str] = None
    email: str
    marketplace_signup_nonce: Optional[str] = None
    password: str


class SAMLLoginSchema(BaseModel):
    """Represents a SAMLLoginSchema in the Iconik system."""

    email: str


class ResetPasswordSchema(BaseModel):
    """Represents a ResetPasswordSchema in the Iconik system."""

    password: str
    repeat_password: str


class RegistrationSchema(BaseModel):
    """Represents a RegistrationSchema in the Iconik system."""

    base_url: Optional[str] = None
    company_name: Optional[str] = None
    country: str
    date_created: Optional[datetime] = None
    email: str
    email_marketing_consent: Optional[bool] = None
    first_name: str
    id: Optional[str] = None
    last_name: str
    marketplace_signup_nonce: Optional[str] = None
    ordway_customer_id: Optional[str] = None
    ordway_subscription_id: Optional[str] = None
    password: str
    referral_code: Optional[str] = None
    stripe_id: Optional[str] = None


class ReferralCodesSchema(BaseModel):
    """Represents a ReferralCodesSchema in the Iconik system."""

    objects: Optional[List["ReferralCodeSchema"]] = Field(default_factory=list)


class ReferralCodeSchema(BaseModel):
    """Represents a ReferralCodeSchema in the Iconik system."""

    code: str
    credit_expiry_days: Optional[int] = None
    do_not_delete: Optional[bool] = None
    is_plg: Optional[bool] = None
    manage_system_domain_id: Optional[str] = None
    ordway_customer_id: Optional[str] = None
    sales_force_id: Optional[str] = None
    valid_to: datetime
    value: float


class RedirectInfoTypeSchema(BaseModel):
    """Represents a RedirectInfoTypeSchema in the Iconik system."""

    headers: Optional[Dict[str, Any]] = Field(default_factory=dict)
    url: Optional[Union[HttpUrl, str]] = None


class PasswordChecksSchema(BaseModel):
    """Represents a PasswordChecksSchema in the Iconik system."""

    digits: Optional[int] = Field(None, ge=0)
    lowercase: Optional[int] = Field(None, ge=0)
    max_length: Optional[int] = Field(None, ge=8, le=64)
    min_length: Optional[int] = Field(None, ge=8, le=56)
    special_symbols: Optional[int] = Field(None, ge=0)
    uppercase: Optional[int] = Field(None, ge=0)


class OneloginSettingsSchema(BaseModel):
    """Represents a OneloginSettingsSchema in the Iconik system."""

    cert_fingerprint: Optional[str] = None
    cert_fingerprint_algorithm: Optional[Literal[
        "http://www.w3.org/2000/09/xmldsig#sha1",
        "http://www.w3.org/2001/04/xmlenc#sha256",
        "http://www.w3.org/2001/04/xmldsig-more#sha384",
        "http://www.w3.org/2001/04/xmlenc#sha512",
    ]] = None
    digest_algorithm: Optional[Literal[
        "http://www.w3.org/2000/09/xmldsig#sha1",
        "http://www.w3.org/2001/04/xmlenc#sha256",
        "http://www.w3.org/2001/04/xmldsig-more#sha384",
        "http://www.w3.org/2001/04/xmlenc#sha512",
    ]] = None
    domain_name: Optional[str] = None
    idp_x509cert: Optional[str] = None
    onelogin_client_id: str
    onelogin_name: str
    signature_algorithm: Optional[Literal[
        "http://www.w3.org/2000/09/xmldsig#dsa-sha1",
        "http://www.w3.org/2000/09/xmldsig#rsa-sha1",
        "http://www.w3.org/2001/04/xmldsig-more#rsa-sha256",
        "http://www.w3.org/2001/04/xmldsig-more#rsa-sha384",
        "http://www.w3.org/2001/04/xmldsig-more#rsa-sha512",
    ]] = None


class OktaSettingsSchema(BaseModel):
    """Represents a OktaSettingsSchema in the Iconik system."""

    cert_fingerprint: Optional[str] = None
    cert_fingerprint_algorithm: Optional[Literal[
        "http://www.w3.org/2000/09/xmldsig#sha1",
        "http://www.w3.org/2001/04/xmlenc#sha256",
        "http://www.w3.org/2001/04/xmldsig-more#sha384",
        "http://www.w3.org/2001/04/xmlenc#sha512",
    ]] = None
    digest_algorithm: Optional[Literal[
        "http://www.w3.org/2000/09/xmldsig#sha1",
        "http://www.w3.org/2001/04/xmlenc#sha256",
        "http://www.w3.org/2001/04/xmldsig-more#sha384",
        "http://www.w3.org/2001/04/xmlenc#sha512",
    ]] = None
    domain_name: Optional[str] = None
    idp_x509cert: Optional[str] = None
    okta_app_id: Optional[str] = None
    okta_name: str
    okta_preview: Optional[bool] = None
    okta_sso: Optional[str] = None
    signature_algorithm: Optional[Literal[
        "http://www.w3.org/2000/09/xmldsig#dsa-sha1",
        "http://www.w3.org/2000/09/xmldsig#rsa-sha1",
        "http://www.w3.org/2001/04/xmldsig-more#rsa-sha256",
        "http://www.w3.org/2001/04/xmldsig-more#rsa-sha384",
        "http://www.w3.org/2001/04/xmldsig-more#rsa-sha512",
    ]] = None


class NotifySystemDomainOTPConfigurationChangedSchema(BaseModel):
    """
    Represents a NotifySystemDomainOTPConfigurationChangedSchema in the Iconik
    system.
    """

    message_type: Literal["otp_enabled", "otp_disabled", "totp_enabled",
                          "totp_disabled"]
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)
    user_id: str


class NotifyOTPConfigurationChangedSchema(BaseModel):
    """Represents a NotifyOTPConfigurationChangedSchema in the Iconik system."""

    email: str
    message_type: Literal["otp_enabled", "otp_disabled", "totp_enabled",
                          "totp_disabled"]
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)


class MultiPlatformDomainUserSystemSchema(BaseModel):
    """Represents a MultiPlatformDomainUserSystemSchema in the Iconik system."""

    logo_url: Optional[Union[HttpUrl, str]] = None
    mfa_methods: Optional[List[Literal["TOTP", "MAIL_2SV"]]] = Field(
        default_factory=list)
    mfa_methods_configured: Optional[List[Literal["TOTP",
                                                  "MAIL_2SV"]]] = Field(
                                                      default_factory=list)
    mfa_required: Optional[bool] = None
    mfa_required_configured: Optional[bool] = None
    platform_url: Optional[Union[HttpUrl, str]] = None
    system_domain_id: str
    system_domain_name: Optional[str] = None
    token: str
    url: Optional[Union[HttpUrl, str]] = None


class MultiDomainUserSystemsSchema(BaseModel):
    """Represents a MultiDomainUserSystemsSchema in the Iconik system."""

    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[List["MultiDomainUserSystemSchema"]] = Field(
        default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    total: Optional[int] = Field(None,
                                 ge=-9223372036854775808,
                                 le=9223372036854775807)


class MultiDomainUserSystemSchema(BaseModel):
    """Represents a MultiDomainUserSystemSchema in the Iconik system."""

    logo_url: Optional[Union[HttpUrl, str]] = None
    mfa_methods: Optional[List[Literal["TOTP", "MAIL_2SV"]]] = Field(
        default_factory=list)
    mfa_methods_configured: Optional[List[Literal["TOTP",
                                                  "MAIL_2SV"]]] = Field(
                                                      default_factory=list)
    mfa_required: Optional[bool] = None
    mfa_required_configured: Optional[bool] = None
    platform_url: Optional[Union[HttpUrl, str]] = None
    system_domain_id: str
    system_domain_name: Optional[str] = None
    url: Optional[Union[HttpUrl, str]] = None


class MultiDomainLoginSchema(BaseModel):
    """Represents a MultiDomainLoginSchema in the Iconik system."""

    app_name: Optional[str] = None
    email: str
    marketplace_signup_nonce: Optional[str] = None
    otp: Optional[str] = None
    otp_type: Optional[str] = None
    system_domain_id: str


class MarketplaceGoogleSignupSchema(BaseModel):
    """Represents a MarketplaceGoogleSignupSchema in the Iconik system."""

    x_gcp_marketplace_token: Optional[str] = Field(
        None, alias="x-gcp-marketplace-token")


class MarketplaceGoogleLinkSchema(BaseModel):
    """Represents a MarketplaceGoogleLinkSchema in the Iconik system."""

    marketplace_signup_nonce: str


class ListObjectsSchema(BaseModel):
    """Represents a ListObjectsSchema in the Iconik system."""

    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    total: Optional[int] = Field(None,
                                 ge=-9223372036854775808,
                                 le=9223372036854775807)


class InvitationResponseSchema(BaseModel):
    """Represents a InvitationResponseSchema in the Iconik system."""

    auto_login: Optional[bool] = None
    domain_status: Optional[Literal["ACTIVE", "WARNING", "FROZEN",
                                    "DEACTIVATED"]] = None
    login_data: Optional["AutoLoginSchema"] = None
    user_id: Optional[str] = None


class InternalTempTokenSchema(BaseModel):
    """Represents a InternalTempTokenSchema in the Iconik system."""

    email: str
    expires_in: int


class InternalAuthenticateUserSchema(BaseModel):
    """Represents a InternalAuthenticateUserSchema in the Iconik system."""

    app_name: str
    marketplace_signup_nonce: Optional[str] = None
    user: Dict[str, Any]


class IdentityProvidersSchema(BaseModel):
    """Represents a IdentityProvidersSchema in the Iconik system."""

    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[List["IdentityProviderSchema"]] = Field(
        default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    total: Optional[int] = Field(None,
                                 ge=-9223372036854775808,
                                 le=9223372036854775807)


class IdentityProviderSchema(BaseModel):
    """Represents a IdentityProviderSchema in the Iconik system."""

    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    id: Optional[str] = None
    public_id: Optional[str] = None
    saml_settings: Optional[Dict[str, Any]] = Field(default_factory=dict)
    settings: Dict[str, Any]
    type: Literal["onelogin.com", "auth0.com", "okta.com", "GENERIC"]
    verbose_logging: Optional[bool] = None


class IdentityProviderBaseSettingsSchema(BaseModel):
    """Represents a IdentityProviderBaseSettingsSchema in the Iconik system."""

    cert_fingerprint: Optional[str] = None
    cert_fingerprint_algorithm: Optional[Literal[
        "http://www.w3.org/2000/09/xmldsig#sha1",
        "http://www.w3.org/2001/04/xmlenc#sha256",
        "http://www.w3.org/2001/04/xmldsig-more#sha384",
        "http://www.w3.org/2001/04/xmlenc#sha512",
    ]] = None
    digest_algorithm: Optional[Literal[
        "http://www.w3.org/2000/09/xmldsig#sha1",
        "http://www.w3.org/2001/04/xmlenc#sha256",
        "http://www.w3.org/2001/04/xmldsig-more#sha384",
        "http://www.w3.org/2001/04/xmlenc#sha512",
    ]] = None
    domain_name: Optional[str] = None
    idp_x509cert: Optional[str] = None
    signature_algorithm: Optional[Literal[
        "http://www.w3.org/2000/09/xmldsig#dsa-sha1",
        "http://www.w3.org/2000/09/xmldsig#rsa-sha1",
        "http://www.w3.org/2001/04/xmldsig-more#rsa-sha256",
        "http://www.w3.org/2001/04/xmldsig-more#rsa-sha384",
        "http://www.w3.org/2001/04/xmldsig-more#rsa-sha512",
    ]] = None


class IdentityProviderBaseSchema(BaseModel):
    """Represents a IdentityProviderBaseSchema in the Iconik system."""

    saml_settings: Optional[Dict[str, Any]] = Field(default_factory=dict)


class GenericSettingsSchema(BaseModel):
    """Represents a GenericSettingsSchema in the Iconik system."""

    cert_fingerprint: Optional[str] = None
    cert_fingerprint_algorithm: Optional[Literal[
        "http://www.w3.org/2000/09/xmldsig#sha1",
        "http://www.w3.org/2001/04/xmlenc#sha256",
        "http://www.w3.org/2001/04/xmldsig-more#sha384",
        "http://www.w3.org/2001/04/xmlenc#sha512",
    ]] = None
    digest_algorithm: Optional[Literal[
        "http://www.w3.org/2000/09/xmldsig#sha1",
        "http://www.w3.org/2001/04/xmlenc#sha256",
        "http://www.w3.org/2001/04/xmldsig-more#sha384",
        "http://www.w3.org/2001/04/xmlenc#sha512",
    ]] = None
    domain_name: Optional[str] = None
    idp_entity_id: str
    idp_sls_redirect_url: Optional[str] = None
    idp_sso_post_url: str
    idp_x509cert: Optional[str] = None
    name: str
    name_id_encrypted: Optional[bool] = None
    signature_algorithm: Optional[Literal[
        "http://www.w3.org/2000/09/xmldsig#dsa-sha1",
        "http://www.w3.org/2000/09/xmldsig#rsa-sha1",
        "http://www.w3.org/2001/04/xmldsig-more#rsa-sha256",
        "http://www.w3.org/2001/04/xmldsig-more#rsa-sha384",
        "http://www.w3.org/2001/04/xmldsig-more#rsa-sha512",
    ]] = None
    want_assertions_signed: Optional[bool] = None
    want_messages_signed: Optional[bool] = None


class ForgotPasswordSchema(BaseModel):
    """Represents a ForgotPasswordSchema in the Iconik system."""

    email: str
    reset_hash: Optional[str] = None


class ExternalAuthSchema(BaseModel):
    """Represents a ExternalAuthSchema in the Iconik system."""

    app_id: Optional[str] = None
    date_created: Optional[datetime] = None
    redirect_info: Optional["RedirectInfoType"] = None
    token: Optional[str] = None


class ExternalAuthRequestSchema(BaseModel):
    """Represents a ExternalAuthRequestSchema in the Iconik system."""

    app_id: Optional[str] = None
    app_name: Optional[str] = None
    redirect_info: Optional[Any] = None
    secret: str


class ExternalAuthRequestResponseSchema(BaseModel):
    """Represents a ExternalAuthRequestResponseSchema in the Iconik system."""

    app_id: Optional[str] = None
    redirect_info: Optional["RedirectInfoType"] = None


class RedirectInfoType(BaseModel):
    """Represents a RedirectInfoType in the Iconik system."""

    headers: Optional[Dict[str, Any]] = Field(default_factory=dict)
    url: Optional[Union[HttpUrl, str]] = None


class EmailLoginSchema(BaseModel):
    """Represents a EmailLoginSchema in the Iconik system."""

    app_name: Optional[str] = None
    email: str


class DomainIdentityProviderMapSchema(BaseModel):
    """Represents a DomainIdentityProviderMapSchema in the Iconik system."""

    domain: str
    identity_provider_id: str
    system_domain_id: str


class CountrySchema(BaseModel):
    """Represents a CountrySchema in the Iconik system."""

    alpha2: Optional[str] = None
    alpha3: Optional[str] = None
    apolitical_name: Optional[str] = None
    name: str
    numeric: Optional[str] = None


class CountriesSchema(BaseModel):
    """Represents a CountriesSchema in the Iconik system."""

    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[List["Country"]] = Field(default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    total: Optional[int] = Field(None,
                                 ge=-9223372036854775808,
                                 le=9223372036854775807)


class Country(BaseModel):
    """Represents a Country in the Iconik system."""

    alpha2: Optional[str] = None
    alpha3: Optional[str] = None
    apolitical_name: Optional[str] = None
    name: str
    numeric: Optional[str] = None


class CompleteInvitationSchema(BaseModel):
    """Represents a CompleteInvitationSchema in the Iconik system."""

    email_marketing_consent: Optional[bool] = None
    password: str
    repeat_password: str


class BillingLimitsSchema(BaseModel):
    """Represents a BillingLimitsSchema in the Iconik system."""

    ai_object_detection_hours: Optional[int] = None
    automation_tasks: Optional[int] = None
    browse_users: Optional[int] = None
    edge_transcoders: Optional[int] = None
    egress_gb: Optional[int] = None
    image_recognition: Optional[int] = None
    multiregion_storage_gb: Optional[int] = None
    power_users: Optional[int] = None
    proxy_storage_gb: Optional[int] = None
    regional_storage_gb: Optional[int] = None
    shield_enabled: Optional[bool] = None
    standard_users: Optional[int] = None
    transcription_hours: Optional[int] = None


class AutoLoginSchema(BaseModel):
    """Represents a AutoLoginSchema in the Iconik system."""

    app_id: str
    token: str


class Auth0SettingsSchema(BaseModel):
    """Represents a Auth0SettingsSchema in the Iconik system."""

    auth0_client_id: str
    auth0_name: str
    auth0_region: str
    cert_fingerprint: Optional[str] = None
    cert_fingerprint_algorithm: Optional[Literal[
        "http://www.w3.org/2000/09/xmldsig#sha1",
        "http://www.w3.org/2001/04/xmlenc#sha256",
        "http://www.w3.org/2001/04/xmldsig-more#sha384",
        "http://www.w3.org/2001/04/xmlenc#sha512",
    ]] = None
    digest_algorithm: Optional[Literal[
        "http://www.w3.org/2000/09/xmldsig#sha1",
        "http://www.w3.org/2001/04/xmlenc#sha256",
        "http://www.w3.org/2001/04/xmldsig-more#sha384",
        "http://www.w3.org/2001/04/xmlenc#sha512",
    ]] = None
    domain_name: Optional[str] = None
    idp_x509cert: Optional[str] = None
    signature_algorithm: Optional[Literal[
        "http://www.w3.org/2000/09/xmldsig#dsa-sha1",
        "http://www.w3.org/2000/09/xmldsig#rsa-sha1",
        "http://www.w3.org/2001/04/xmldsig-more#rsa-sha256",
        "http://www.w3.org/2001/04/xmldsig-more#rsa-sha384",
        "http://www.w3.org/2001/04/xmldsig-more#rsa-sha512",
    ]] = None


class AppsSchema(BaseModel):
    """Represents a AppsSchema in the Iconik system."""

    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[List["AppSchema"]] = Field(default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    total: Optional[int] = Field(None,
                                 ge=-9223372036854775808,
                                 le=9223372036854775807)


class ApprovedAppInstanceSchema(BaseModel):
    """Represents a ApprovedAppInstanceSchema in the Iconik system."""

    app_id: str
    date_created: Optional[datetime] = None
    id: str


class AppSchema(BaseModel):
    """Represents a AppSchema in the Iconik system."""

    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    default_user_id: Optional[str] = None
    description: Optional[str] = None
    id: Optional[str] = None
    name: str
    system_domain_id: Optional[str] = None
    url: Optional[Union[HttpUrl, str]] = None


# Update forward references
WebflowContentSchema.model_rebuild()
VerificationResponseSchema.model_rebuild()
UserSystemDomainInviteSchema.model_rebuild()
TokensSchema.model_rebuild()
TokenSchema.model_rebuild()
TokenOutputSchema.model_rebuild()
TokenMultiplatformLoginSchema.model_rebuild()
TokenBaseSchema.model_rebuild()
TemporaryPasswordTokenSchema.model_rebuild()
SystemDomainsSchema.model_rebuild()
SystemDomainSuperAdminSchema.model_rebuild()
SystemDomainSchema.model_rebuild()
SystemDomainFromTemplateSchema.model_rebuild()
SystemDomainFromReferralCodeSchema.model_rebuild()
SimpleLoginSchema.model_rebuild()
SAMLLoginSchema.model_rebuild()
ResetPasswordSchema.model_rebuild()
RegistrationSchema.model_rebuild()
ReferralCodesSchema.model_rebuild()
ReferralCodeSchema.model_rebuild()
RedirectInfoTypeSchema.model_rebuild()
PasswordChecksSchema.model_rebuild()
OneloginSettingsSchema.model_rebuild()
OktaSettingsSchema.model_rebuild()
NotifySystemDomainOTPConfigurationChangedSchema.model_rebuild()
NotifyOTPConfigurationChangedSchema.model_rebuild()
MultiPlatformDomainUserSystemSchema.model_rebuild()
MultiDomainUserSystemsSchema.model_rebuild()
MultiDomainUserSystemSchema.model_rebuild()
MultiDomainLoginSchema.model_rebuild()
MarketplaceGoogleSignupSchema.model_rebuild()
MarketplaceGoogleLinkSchema.model_rebuild()
ListObjectsSchema.model_rebuild()
InvitationResponseSchema.model_rebuild()
InternalTempTokenSchema.model_rebuild()
InternalAuthenticateUserSchema.model_rebuild()
IdentityProvidersSchema.model_rebuild()
IdentityProviderSchema.model_rebuild()
IdentityProviderBaseSettingsSchema.model_rebuild()
IdentityProviderBaseSchema.model_rebuild()
GenericSettingsSchema.model_rebuild()
ForgotPasswordSchema.model_rebuild()
ExternalAuthSchema.model_rebuild()
ExternalAuthRequestSchema.model_rebuild()
ExternalAuthRequestResponseSchema.model_rebuild()
RedirectInfoType.model_rebuild()
EmailLoginSchema.model_rebuild()
DomainIdentityProviderMapSchema.model_rebuild()
CountrySchema.model_rebuild()
CountriesSchema.model_rebuild()
Country.model_rebuild()
CompleteInvitationSchema.model_rebuild()
BillingLimitsSchema.model_rebuild()
AutoLoginSchema.model_rebuild()
Auth0SettingsSchema.model_rebuild()
AppsSchema.model_rebuild()
ApprovedAppInstanceSchema.model_rebuild()
AppSchema.model_rebuild()
