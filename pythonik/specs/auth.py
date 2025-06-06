from typing import (
    Any,
    Dict,
    Optional,
    TypeVar,
    Union,
)

from pythonik.models.auth import (
    ApprovedAppInstanceSchema,
    AppSchema,
    AppsSchema,
    CompleteInvitationSchema,
    CountriesSchema,
    DomainIdentityProviderMapSchema,
    ExternalAuthRequestResponseSchema,
    ExternalAuthRequestSchema,
    ExternalAuthSchema,
    ForgotPasswordSchema,
    IdentityProviderSchema,
    IdentityProvidersSchema,
    InvitationResponseSchema,
    MarketplaceGoogleLinkSchema,
    MultiDomainLoginSchema,
    MultiDomainUserSystemsSchema,
    NotifyOTPConfigurationChangedSchema,
    PasswordChecksSchema,
    ReferralCodeSchema,
    ReferralCodesSchema,
    RegistrationSchema,
    ResetPasswordSchema,
    SAMLLoginSchema,
    SimpleLoginSchema,
    SystemDomainFromReferralCodeSchema,
    SystemDomainFromTemplateSchema,
    SystemDomainSchema,
    SystemDomainsSchema,
    SystemDomainSuperAdminSchema,
    TokenMultiplatformLoginSchema,
    TokenOutputSchema,
    TokenSchema,
    TokensSchema,
    UserSystemDomainInviteSchema,
    VerificationResponseSchema,
    WebflowContentSchema,
)
from pythonik.models.base import Response
from pythonik.specs._internal_utils import is_pydantic_model
from pythonik.specs.base import Spec

T = TypeVar("T")


class AuthSpec(Spec):
    server = "API/auth/"

    def list_apps(self,
                  per_page: int = 10,
                  last_id: Optional[str] = None,
                  **kwargs) -> Response:
        """
        List of apps

        Args:
            per_page: The number of items for each page (default: 10)
            last_id: ID of a last file set on previous page
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=AppsSchema)

        Raises:
            - 401 Token is invalid
        """
        params = {}
        if per_page is not None:
            params["per_page"] = per_page
        if last_id is not None:
            params["last_id"] = last_id

        url = self.gen_url("apps/")
        resp = self._get(url, params=params, **kwargs)
        return self.parse_response(resp, AppsSchema)

    def create_app(
        self,
        app: Union[AppSchema, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Create a new app

        Args:
            app: App data, either as AppSchema or dict
            exclude_defaults: Whether to exclude default values when dumping
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=AppSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        body = (app.model_dump(exclude_defaults=exclude_defaults)
                if is_pydantic_model(app) else app)
        url = self.gen_url("apps/")
        resp = self._post(url, json=body, **kwargs)
        return self.parse_response(resp, AppSchema)

    def get_app(self, app_id: str, **kwargs) -> Response:
        """
        Returns a particular app by id

        Args:
            app_id: ID of the app
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=AppSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        url = self.gen_url(f"apps/{app_id}/")
        resp = self._get(url, **kwargs)
        return self.parse_response(resp, AppSchema)

    def update_app(
        self,
        app_id: str,
        app: Union[AppSchema, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Update app

        Args:
            app_id: ID of the app
            app: App data, either as AppSchema or dict
            exclude_defaults: Whether to exclude default values when dumping
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=AppSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        body = (app.model_dump(exclude_defaults=exclude_defaults)
                if is_pydantic_model(app) else app)
        url = self.gen_url(f"apps/{app_id}/")
        resp = self._put(url, json=body, **kwargs)
        return self.parse_response(resp, AppSchema)

    def partial_update_app(
        self,
        app_id: str,
        app: Union[AppSchema, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Update app

        Args:
            app_id: ID of the app
            app: App data, either as AppSchema or dict
            exclude_defaults: Whether to exclude default values when dumping
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=AppSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        body = (app.model_dump(exclude_defaults=exclude_defaults,
                               exclude_unset=True)
                if is_pydantic_model(app) else app)
        url = self.gen_url(f"apps/{app_id}/")
        resp = self._patch(url, json=body, **kwargs)
        return self.parse_response(resp, AppSchema)

    def delete_app(self, app_id: str, **kwargs) -> Response:
        """
        Delete a particular app by id

        Args:
            app_id: ID of the app to delete
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=None)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        url = self.gen_url(f"apps/{app_id}/")
        resp = self._delete(url, **kwargs)
        return self.parse_response(resp, None)

    def create_external_auth_request(
        self,
        request: Union[ExternalAuthRequestSchema, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Create a new token for the logged-in user and store it for an
        external app

        Args:
            request: Request data, either as ExternalAuthRequestSchema or dict
            exclude_defaults: Whether to exclude default values when dumping
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=ExternalAuthRequestResponseSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        body = (request.model_dump(exclude_defaults=exclude_defaults)
                if is_pydantic_model(request) else request)
        url = self.gen_url("apps/external/auth/")
        resp = self._post(url, json=body, **kwargs)
        return self.parse_response(resp, ExternalAuthRequestResponseSchema)

    def get_external_auth(self, secret: str, **kwargs) -> Response:
        """
        Gets a token requested by an external app

        Args:
            secret: Secret key
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=ExternalAuthSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        url = self.gen_url(f"apps/external/auth/{secret}/")
        resp = self._get(url, **kwargs)
        return self.parse_response(resp, ExternalAuthSchema)

    def create_app_instance(
        self,
        instance: Union[ApprovedAppInstanceSchema, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Create a new app instance

        Args:
            instance: Instance data, either as ApprovedAppInstanceSchema or dict
            exclude_defaults: Whether to exclude default values when dumping
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=ApprovedAppInstanceSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        body = (instance.model_dump(exclude_defaults=exclude_defaults)
                if is_pydantic_model(instance) else instance)
        url = self.gen_url("apps/instance/")
        resp = self._post(url, json=body, **kwargs)
        return self.parse_response(resp, ApprovedAppInstanceSchema)

    def get_app_instance(self, approved_instance_id: str,
                         **kwargs) -> Response:
        """
        Gets an approved instance of an app

        Args:
            approved_instance_id: ID of the approved instance
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=ExternalAuthSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        url = self.gen_url(f"apps/instance/{approved_instance_id}/")
        resp = self._get(url, **kwargs)
        return self.parse_response(resp, ExternalAuthSchema)

    def delete_app_instance(self, approved_instance_id: str,
                            **kwargs) -> Response:
        """
        Delete an approved instance of an app

        Args:
            approved_instance_id: ID of the approved instance to delete
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=None)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        url = self.gen_url(f"apps/instance/{approved_instance_id}/")
        resp = self._delete(url, **kwargs)
        return self.parse_response(resp, None)

    def create_app_token(self, app_id: str, **kwargs) -> Response:
        """
        Creates app token by id and returns it's data

        Args:
            app_id: ID of the app
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=TokenSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        url = self.gen_url(f"apps/{app_id}/token/")
        resp = self._post(url, **kwargs)
        return self.parse_response(resp, TokenSchema)

    def login_active_directory(self, body: Dict[str, Any],
                               **kwargs) -> Response:
        """
        Login by ActiveDirectory

        Args:
            body: Request body
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=TokenSchema)

        Raises:
            - 400 Bad request
        """
        url = self.gen_url("auth/ad/login/")
        resp = self._post(url, json=body, **kwargs)
        return self.parse_response(resp, TokenSchema)

    def generate_current_otp(self, **kwargs) -> Response:
        """
        Request OTP code as an authenticated user

        Args:
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=None)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        url = self.gen_url("auth/current/otp/generate/")
        resp = self._post(url, **kwargs)
        return self.parse_response(resp, None)

    def login_multidomain(
        self,
        login: Union[MultiDomainLoginSchema, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Login by using temp token

        Args:
            login: Login data, either as MultiDomainLoginSchema or dict
            exclude_defaults: Whether to exclude default values when dumping
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=TokenSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        body = (login.model_dump(exclude_defaults=exclude_defaults)
                if is_pydantic_model(login) else login)
        url = self.gen_url("auth/multidomain/login/")
        resp = self._post(url, json=body, **kwargs)
        return self.parse_response(resp, TokenSchema)

    def login_oauth(self, body: Dict[str, Any], **kwargs) -> Response:
        """
        Login by OAuth

        Args:
            body: Request body
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=TokenSchema)

        Raises:
            - 400 Bad request
        """
        url = self.gen_url("auth/oauth/login/")
        resp = self._post(url, json=body, **kwargs)
        return self.parse_response(resp, TokenSchema)

    def generate_otp(
        self,
        login: Union[MultiDomainLoginSchema, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Request OTP code

        Args:
            login: Login data, either as MultiDomainLoginSchema or dict
            exclude_defaults: Whether to exclude default values when dumping
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=None)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        body = (login.model_dump(exclude_defaults=exclude_defaults)
                if is_pydantic_model(login) else login)
        url = self.gen_url("auth/otp/generate/")
        resp = self._post(url, json=body, **kwargs)
        return self.parse_response(resp, None)

    def saml_assertion_consumer_service(self,
                                        public_id: str,
                                        data: Any = None,
                                        **kwargs) -> Response:
        """
        SAML Assertion Consumer Service

        Args:
            public_id: Public ID
            data: POST data
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=None)

        Raises:
            - 400 Bad request
            - 401 Unauthorized request
            - 404 Requested page does not exist
        """
        url = self.gen_url(f"auth/saml/acs/{public_id}/")
        resp = self._post(url, data=data, **kwargs)
        return self.parse_response(resp, None)

    def bind_domain_to_identity_provider(
        self,
        map_data: Union[DomainIdentityProviderMapSchema, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Bind domain to identity provider

        Args:
            map_data: Mapping data, either as DomainIdentityProviderMapSchema
                     or dict
            exclude_defaults: Whether to exclude default values when dumping
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=DomainIdentityProviderMapSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        body = (map_data.model_dump(exclude_defaults=exclude_defaults)
                if is_pydantic_model(map_data) else map_data)
        url = self.gen_url("auth/saml/domains/")
        resp = self._post(url, json=body, **kwargs)
        return self.parse_response(resp, DomainIdentityProviderMapSchema)

    def unbind_domain_from_identity_provider(self, domain: str,
                                             **kwargs) -> Response:
        """
        Unbind domain from identity provider

        Args:
            domain: Domain name
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=None)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
            - 404 Does not exist
        """
        url = self.gen_url(f"auth/saml/domains/{domain}/")
        resp = self._delete(url, **kwargs)
        return self.parse_response(resp, None)

    def list_identity_providers(
        self,
        per_page: Optional[int] = None,
        last_id: Optional[str] = None,
        **kwargs,
    ) -> Response:
        """
        Get list of identity providers

        Args:
            per_page: The number of items for each page
            last_id: ID of a last file set on previous page
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=IdentityProvidersSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
            - 404 Requested page does not exist
        """
        params = {}
        if per_page is not None:
            params["per_page"] = per_page
        if last_id is not None:
            params["last_id"] = last_id

        url = self.gen_url("auth/saml/idp/")
        resp = self._get(url, params=params, **kwargs)
        return self.parse_response(resp, IdentityProvidersSchema)

    def create_identity_provider(
        self,
        provider: Union[IdentityProviderSchema, Dict[str, Any], str],
        exclude_defaults: bool = True,
        is_xml: bool = False,
        **kwargs,
    ) -> Response:
        """
        Create a new identity provider.

        Input can either be an IdentityProviderSchema as json or a SAML
        EntityDescriptor XML.

        Args:
            provider: Provider data, either as IdentityProviderSchema, dict,
                     or XML string
            exclude_defaults: Whether to exclude default values when dumping
            is_xml: Whether the provider data is an XML string
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=IdentityProviderSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        url = self.gen_url("auth/saml/idp/")

        if is_xml:
            # Ensure provider is a string for XML
            if not isinstance(provider, str):
                raise ValueError("Provider must be a string for XML content")
            resp = self._post(
                url,
                data=provider,
                headers={"Content-Type": "application/xml"},
                **kwargs,
            )
        else:
            # JSON body
            body = (provider.model_dump(exclude_defaults=exclude_defaults)
                    if is_pydantic_model(provider) else provider)
            resp = self._post(url, json=body, **kwargs)

        return self.parse_response(resp, IdentityProviderSchema)

    def convert_idp_entity_descriptor(self, xml_data: str,
                                      **kwargs) -> Response:
        """
        Convert an IdP EntityDescriptor XML into json suitable as a settings
        configuration.

        Args:
            xml_data: SAML EntityDescriptor XML
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=IdentityProviderSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        url = self.gen_url("auth/saml/idp/convert/")
        resp = self._post(
            url,
            data=xml_data,
            headers={"Content-Type": "application/xml"},
            **kwargs,
        )
        return self.parse_response(resp, IdentityProviderSchema)

    def get_identity_provider(self, identity_provider_id: str,
                              **kwargs) -> Response:
        """
        Get a particular identity provider by id

        Args:
            identity_provider_id: ID of the identity provider
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=IdentityProviderSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
            - 404 Identity provider does not exist
        """
        url = self.gen_url(f"auth/saml/idp/{identity_provider_id}/")
        resp = self._get(url, **kwargs)
        return self.parse_response(resp, IdentityProviderSchema)

    def update_identity_provider(
        self,
        identity_provider_id: str,
        provider: Union[IdentityProviderSchema, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Update a particular identity provider by id

        Args:
            identity_provider_id: ID of the identity provider
            provider: Provider data, either as IdentityProviderSchema or dict
            exclude_defaults: Whether to exclude default values when dumping
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=IdentityProviderSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
            - 404 Identity provider does not exist
        """
        body = (provider.model_dump(exclude_defaults=exclude_defaults)
                if is_pydantic_model(provider) else provider)
        url = self.gen_url(f"auth/saml/idp/{identity_provider_id}/")
        resp = self._put(url, json=body, **kwargs)
        return self.parse_response(resp, IdentityProviderSchema)

    def partial_update_identity_provider(
        self,
        identity_provider_id: str,
        provider: Union[IdentityProviderSchema, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Update a particular identity provider by id

        Args:
            identity_provider_id: ID of the identity provider
            provider: Provider data, either as IdentityProviderSchema or dict
            exclude_defaults: Whether to exclude default values when dumping
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=IdentityProviderSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
            - 404 Identity provider does not exist
        """
        body = (provider.model_dump(exclude_defaults=exclude_defaults,
                                    exclude_unset=True)
                if is_pydantic_model(provider) else provider)
        url = self.gen_url(f"auth/saml/idp/{identity_provider_id}/")
        resp = self._patch(url, json=body, **kwargs)
        return self.parse_response(resp, IdentityProviderSchema)

    def delete_identity_provider(self, identity_provider_id: str,
                                 **kwargs) -> Response:
        """
        Delete a particular identity provider by id

        Args:
            identity_provider_id: ID of the identity provider to delete
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=None)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
            - 404 Identity provider does not exist
        """
        url = self.gen_url(f"auth/saml/idp/{identity_provider_id}/")
        resp = self._delete(url, **kwargs)
        return self.parse_response(resp, None)

    def saml_login(
        self,
        login: Union[SAMLLoginSchema, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        SAML Single sign-on url by domain

        Args:
            login: Login data, either as SAMLLoginSchema or dict
            exclude_defaults: Whether to exclude default values when dumping
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=None)

        Raises:
            - 404 Requested page does not exist
        """
        body = (login.model_dump(exclude_defaults=exclude_defaults)
                if is_pydantic_model(login) else login)
        url = self.gen_url("auth/saml/login/")
        resp = self._post(url, json=body, **kwargs)
        return self.parse_response(resp, None)

    def saml_logout(self, public_id: str, **kwargs) -> Response:
        """
        Initiate SAML Single logout

        Args:
            public_id: Public ID
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=None)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        url = self.gen_url(f"auth/saml/logout/{public_id}/")
        resp = self._post(url, **kwargs)
        return self.parse_response(resp, None)

    def get_saml_metadata(self, public_id: str, **kwargs) -> Response:
        """
        SAML Single Logout Service

        Args:
            public_id: Public ID
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=None)

        Raises:
            - 400 Bad request
            - 404 Requested page does not exist
        """
        url = self.gen_url(f"auth/saml/metadata/{public_id}/")
        resp = self._get(url, **kwargs)
        return self.parse_response(resp, None)

    def saml_multidomain_login(
        self,
        login: Union[SAMLLoginSchema, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        SAML Single sign-on url by domain

        Args:
            login: Login data, either as SAMLLoginSchema or dict
            exclude_defaults: Whether to exclude default values when dumping
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=MultiDomainUserSystemsSchema)

        Raises:
            - 404 Requested page does not exist
        """
        body = (login.model_dump(exclude_defaults=exclude_defaults)
                if is_pydantic_model(login) else login)
        url = self.gen_url("auth/saml/multidomain/login/")
        resp = self._post(url, json=body, **kwargs)
        return self.parse_response(resp, MultiDomainUserSystemsSchema)

    def get_saml_slo(self, public_id: str, **kwargs) -> Response:
        """
        SAML Single Logout Service

        Args:
            public_id: Public ID
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=None)

        Raises:
            - 400 Bad request
            - 404 Requested page does not exist
        """
        url = self.gen_url(f"auth/saml/slo/{public_id}/")
        resp = self._get(url, **kwargs)
        return self.parse_response(resp, None)

    def get_saml_sso(self, public_id: str, **kwargs) -> Response:
        """
        SAML Single sign-on Service

        Args:
            public_id: Public ID
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=None)

        Raises:
            - 404 Requested page does not exist
        """
        url = self.gen_url(f"auth/saml/sso/{public_id}/")
        resp = self._get(url, **kwargs)
        return self.parse_response(resp, None)

    def simple_login(
        self,
        login: Union[SimpleLoginSchema, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Login by using email and password

        Args:
            login: Login data, either as SimpleLoginSchema or dict
            exclude_defaults: Whether to exclude default values when dumping
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=TokenMultiplatformLoginSchema)

        Raises:
            - 400 Bad request
        """
        body = (login.model_dump(exclude_defaults=exclude_defaults)
                if is_pydantic_model(login) else login)
        url = self.gen_url("auth/simple/login/")
        resp = self._post(url, json=body, **kwargs)
        return self.parse_response(resp, TokenMultiplatformLoginSchema)

    def check_token(self, **kwargs) -> Response:
        """
        Check if auth token valid

        Args:
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=None)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        url = self.gen_url("auth/token/")
        resp = self._get(url, **kwargs)
        return self.parse_response(resp, None)

    def create_token(self, **kwargs) -> Response:
        """
        Create new token without invalidating the old one

        Args:
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=TokenSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        url = self.gen_url("auth/token/")
        resp = self._post(url, **kwargs)
        return self.parse_response(resp, TokenSchema)

    def refresh_token(self, **kwargs) -> Response:
        """
        Refresh token

        Args:
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=TokenSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        url = self.gen_url("auth/token/")
        resp = self._put(url, **kwargs)
        return self.parse_response(resp, TokenSchema)

    def revoke_token(self, **kwargs) -> Response:
        """
        Revoke token

        Args:
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=None)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        url = self.gen_url("auth/token/")
        resp = self._delete(url, **kwargs)
        return self.parse_response(resp, None)

    def get_token(self, token_id: str, **kwargs) -> Response:
        """
        Get token by ID

        Args:
            token_id: ID of the token
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=TokenOutputSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        url = self.gen_url(f"auth/token/{token_id}/")
        resp = self._get(url, **kwargs)
        return self.parse_response(resp, TokenOutputSchema)

    def revoke_token_by_id(self, token_id: str, **kwargs) -> Response:
        """
        Revoke token by ID

        Args:
            token_id: ID of the token to revoke
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=None)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        url = self.gen_url(f"auth/token/{token_id}/")
        resp = self._delete(url, **kwargs)
        return self.parse_response(resp, None)

    def list_tokens(self,
                    per_page: int = 10,
                    last_id: Optional[str] = None,
                    **kwargs) -> Response:
        """
        List of tokens

        Args:
            per_page: The number of items for each page (default: 10)
            last_id: ID of a last file set on previous page
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=TokensSchema)

        Raises:
            - 401 Token is invalid
        """
        params: Dict[str, Any] = {"per_page": per_page}
        if last_id is not None:
            params["last_id"] = last_id

        url = self.gen_url("auth/tokens/")
        resp = self._get(url, params=params, **kwargs)
        return self.parse_response(resp, TokensSchema)

    def complete_invitation(
        self,
        reset_hash: str,
        invitation: Union[CompleteInvitationSchema, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Completes invitation by setting password and other user details

        Args:
            reset_hash: Reset hash
            invitation: Invitation data, either as CompleteInvitationSchema or
                        dict
            exclude_defaults: Whether to exclude default values when dumping
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=InvitationResponseSchema)

        Raises:
            - 400 Bad request
            - 419 Authentication token expired
        """
        body = (invitation.model_dump(exclude_defaults=exclude_defaults)
                if is_pydantic_model(invitation) else invitation)
        url = self.gen_url(f"invitation/complete/{reset_hash}/")
        resp = self._put(url, json=body, **kwargs)
        return self.parse_response(resp, InvitationResponseSchema)

    def link_google_marketplace(
        self,
        link_data: Union[MarketplaceGoogleLinkSchema, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Google cloud marketplace link to existing system domain

        Args:
            link_data: Link data, either as MarketplaceGoogleLinkSchema or dict
            exclude_defaults: Whether to exclude default values when dumping
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=None)

        Raises:
            - 400 Bad request
        """
        body = (link_data.model_dump(exclude_defaults=exclude_defaults)
                if is_pydantic_model(link_data) else link_data)
        url = self.gen_url("marketplace/google/link/")
        resp = self._post(url, json=body, **kwargs)
        return self.parse_response(resp, None)

    def signup_google_marketplace(self, token: str, **kwargs) -> Response:
        """
        Google cloud marketplace signup

        Args:
            token: GCP marketplace token
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=None)

        Raises:
            - 400 Bad request
        """
        form_data = {"x-gcp-marketplace-token": token}
        url = self.gen_url("marketplace/google/signup/")
        resp = self._post(
            url,
            data=form_data,
            headers={"Content-Type": "multipart/form-data"},
            **kwargs,
        )
        return self.parse_response(resp, None)

    def get_password_checks(self, **kwargs) -> Response:
        """
        Returns a list of password checks required for the password to be safe

        Args:
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=PasswordChecksSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        url = self.gen_url("password/checks/")
        resp = self._get(url, **kwargs)
        return self.parse_response(resp, PasswordChecksSchema)

    def forgot_password(
        self,
        request: Union[ForgotPasswordSchema, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Receives email address and sends email to this address with a link for
        resetting password.

        Args:
            request: Request data, either as ForgotPasswordSchema or dict
            exclude_defaults: Whether to exclude default values when dumping
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=None)

        Raises:
            - 400 Bad request
        """
        body = (request.model_dump(exclude_defaults=exclude_defaults)
                if is_pydantic_model(request) else request)
        url = self.gen_url("password/forgot/")
        resp = self._post(url, json=body, **kwargs)
        return self.parse_response(resp, None)

    def reset_password(
        self,
        reset_hash: str,
        reset_data: Union[ResetPasswordSchema, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Changes password to a new one

        Args:
            reset_hash: Reset hash
            reset_data: Reset data, either as ResetPasswordSchema or dict
            exclude_defaults: Whether to exclude default values when dumping
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=None)

        Raises:
            - 400 Bad request
            - 419 Authentication token expired
        """
        body = (reset_data.model_dump(exclude_defaults=exclude_defaults)
                if is_pydantic_model(reset_data) else reset_data)
        url = self.gen_url(f"password/reset/{reset_hash}/")
        resp = self._put(url, json=body, **kwargs)
        return self.parse_response(resp, None)

    def get_password_checks_for_reset(self, reset_hash: str,
                                      **kwargs) -> Response:
        """
        Returns a list of password checks required for the password to be safe

        Args:
            reset_hash: Reset hash
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=PasswordChecksSchema)

        Raises:
            - 400 Bad request
            - 419 Reset password token expired
        """
        url = self.gen_url(f"password/{reset_hash}/checks/")
        resp = self._get(url, **kwargs)
        return self.parse_response(resp, PasswordChecksSchema)

    def list_referral_codes(self, **kwargs) -> Response:
        """
        Get all referral_codes

        Args:
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=ReferralCodesSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        url = self.gen_url("referral_codes/")
        resp = self._get(url, **kwargs)
        return self.parse_response(resp, ReferralCodesSchema)

    def create_referral_code(
        self,
        code: Union[ReferralCodeSchema, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Create a new referral_code

        Args:
            code: Referral code data, either as ReferralCodeSchema or dict
            exclude_defaults: Whether to exclude default values when dumping
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=ReferralCodeSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
            - 409 Code already exists
        """
        body = (code.model_dump(exclude_defaults=exclude_defaults)
                if is_pydantic_model(code) else code)
        url = self.gen_url("referral_codes/")
        resp = self._post(url, json=body, **kwargs)
        return self.parse_response(resp, ReferralCodeSchema)

    def get_referral_code(self, code: str, **kwargs) -> Response:
        """
        Get a referral_code

        Args:
            code: Referral code
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=ReferralCodeSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        url = self.gen_url(f"referral_codes/{code}/")
        resp = self._get(url, **kwargs)
        return self.parse_response(resp, ReferralCodeSchema)

    def delete_referral_code(self, code: str, **kwargs) -> Response:
        """
        Delete a referral_code

        Args:
            code: Referral code to delete
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=None)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        url = self.gen_url(f"referral_codes/{code}/")
        resp = self._delete(url, **kwargs)
        return self.parse_response(resp, None)

    def create_registration(
        self,
        registration: Union[RegistrationSchema, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Create a new registration

        Args:
            registration: Registration data, either as RegistrationSchema
                or dict
            exclude_defaults: Whether to exclude default values when dumping
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=RegistrationSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        body = (registration.model_dump(exclude_defaults=exclude_defaults)
                if is_pydantic_model(registration) else registration)
        url = self.gen_url("registrations/")
        resp = self._post(url, json=body, **kwargs)
        return self.parse_response(resp, RegistrationSchema)

    def get_registration_content(self, page_route: str, **kwargs) -> Response:
        """
        Returns page content from Webflow collection

        Args:
            page_route: Page route to fetch content for
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=WebflowContentSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        params = {"page_route": page_route}
        url = self.gen_url("registrations/content/")
        resp = self._get(url, params=params, **kwargs)
        return self.parse_response(resp, WebflowContentSchema)

    def list_countries(self, **kwargs) -> Response:
        """
        Returns list of countries

        Args:
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=CountriesSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        url = self.gen_url("registrations/countries/")
        resp = self._get(url, **kwargs)
        return self.parse_response(resp, CountriesSchema)

    def verify_email(self, email_hash: str, **kwargs) -> Response:
        """
        Verify email address, create system domain from template, and
        authenticate user

        Args:
            email_hash: Email hash
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=VerificationResponseSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        url = self.gen_url(f"registrations/verify/{email_hash}/")
        resp = self._post(url, **kwargs)
        return self.parse_response(resp, VerificationResponseSchema)

    def list_system_domains(
        self,
        query: Optional[str] = None,
        statuses: Optional[str] = None,
        **kwargs,
    ) -> Response:
        """
        List of system domains

        Args:
            query: Query the name
            statuses: Comma separated list of statuses to show
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=SystemDomainsSchema)

        Raises:
            - 401 Token is invalid
        """
        params = {}
        if query is not None:
            params["query"] = query
        if statuses is not None:
            params["statuses"] = statuses

        url = self.gen_url("system_domains/")
        resp = self._get(url, params=params, **kwargs)
        return self.parse_response(resp, SystemDomainsSchema)

    def create_system_domain(
        self,
        domain: Union[SystemDomainSchema, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Create a new system domain

        Args:
            domain: Domain data, either as SystemDomainSchema or dict
            exclude_defaults: Whether to exclude default values when dumping
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=SystemDomainSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        body = (domain.model_dump(exclude_defaults=exclude_defaults)
                if is_pydantic_model(domain) else domain)
        url = self.gen_url("system_domains/")
        resp = self._post(url, json=body, **kwargs)
        return self.parse_response(resp, SystemDomainSchema)

    def create_system_domain_from_referral_code(
        self,
        referral_code: str,
        domain: Union[SystemDomainFromReferralCodeSchema, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Create a new system domain from a referral code (That is associated to
        your domain)

        Args:
            referral_code: Referral code
            domain: Domain data, either as SystemDomainFromReferralCodeSchema
                   or dict
            exclude_defaults: Whether to exclude default values when dumping
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=SystemDomainFromTemplateSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        body = (domain.model_dump(exclude_defaults=exclude_defaults)
                if is_pydantic_model(domain) else domain)
        url = self.gen_url(f"system_domains/referral_code/{referral_code}/")
        resp = self._post(url, json=body, **kwargs)
        return self.parse_response(resp, SystemDomainFromTemplateSchema)

    def list_system_domain_templates(self, **kwargs) -> Response:
        """
        List of system domain templates

        Args:
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=SystemDomainsSchema)

        Raises:
            - 401 Token is invalid
        """
        url = self.gen_url("system_domains/templates/")
        resp = self._get(url, **kwargs)
        return self.parse_response(resp, SystemDomainsSchema)

    def get_system_domain(self, system_domain_id: str, **kwargs) -> Response:
        """
        Returns a particular system domain by id

        Args:
            system_domain_id: ID of the system domain
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=SystemDomainSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
            - 404 System domain does not exist
        """
        url = self.gen_url(f"system_domains/{system_domain_id}/")
        resp = self._get(url, **kwargs)
        return self.parse_response(resp, SystemDomainSchema)

    def update_system_domain(
        self,
        system_domain_id: str,
        domain: Union[SystemDomainSuperAdminSchema, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Update system domain

        Args:
            system_domain_id: ID of the system domain
            domain: Domain data, either as SystemDomainSuperAdminSchema or dict
            exclude_defaults: Whether to exclude default values when dumping
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=SystemDomainSuperAdminSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
            - 404 System domain does not exist
        """
        body = (domain.model_dump(exclude_defaults=exclude_defaults)
                if is_pydantic_model(domain) else domain)
        url = self.gen_url(f"system_domains/{system_domain_id}/")
        resp = self._put(url, json=body, **kwargs)
        return self.parse_response(resp, SystemDomainSuperAdminSchema)

    def partial_update_system_domain(
        self,
        system_domain_id: str,
        domain: Union[SystemDomainSuperAdminSchema, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Update system domain

        Args:
            system_domain_id: ID of the system domain
            domain: Domain data, either as SystemDomainSuperAdminSchema or dict
            exclude_defaults: Whether to exclude default values when dumping
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=SystemDomainSuperAdminSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
            - 404 System domain does not exist
        """
        body = (domain.model_dump(exclude_defaults=exclude_defaults,
                                  exclude_unset=True)
                if is_pydantic_model(domain) else domain)
        url = self.gen_url(f"system_domains/{system_domain_id}/")
        resp = self._patch(url, json=body, **kwargs)
        return self.parse_response(resp, SystemDomainSuperAdminSchema)

    def delete_system_domain(self, system_domain_id: str,
                             **kwargs) -> Response:
        """
        Delete a particular system_domain by id

        Args:
            system_domain_id: ID of the system domain to delete
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=None)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        url = self.gen_url(f"system_domains/{system_domain_id}/")
        resp = self._delete(url, **kwargs)
        return self.parse_response(resp, None)

    def upload_system_domain_logo(
        self,
        system_domain_id: str,
        logo: bytes,
        content_type: str = "image/png",
        **kwargs,
    ) -> Response:
        """
        Upload system domain logo image.

        Args:
            system_domain_id: ID of the system domain
            logo: Logo image data
            content_type: Content type of the image (default: "image/png")
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=None)

        Raises:
            - 400 Bad request
            - 404 System domain does not exist
        """
        url = self.gen_url(f"system_domains/{system_domain_id}/logo/")
        resp = self._post(url,
                          data=logo,
                          headers={"Content-Type": content_type},
                          **kwargs)
        return self.parse_response(resp, None)

    def delete_system_domain_logo(self, system_domain_id: str,
                                  **kwargs) -> Response:
        """
        Delete system domain logo image.

        Args:
            system_domain_id: ID of the system domain
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=None)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
            - 404 System domain does not exist
        """
        url = self.gen_url(f"system_domains/{system_domain_id}/logo/")
        resp = self._delete(url, **kwargs)
        return self.parse_response(resp, None)

    def notify_otp_configuration_changed(
        self,
        notification: Union[NotifyOTPConfigurationChangedSchema, Dict[str,
                                                                      Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Notify about OTP configuration changes

        Args:
            notification: Notification data, either as
                          NotifyOTPConfigurationChangedSchema or dict
            exclude_defaults: Whether to exclude default values when dumping
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=None)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        body = (notification.model_dump(exclude_defaults=exclude_defaults)
                if is_pydantic_model(notification) else notification)
        url = self.gen_url("auth/notify/otp/")
        resp = self._post(url, json=body, **kwargs)
        return self.parse_response(resp, None)

    def invite_user_to_system_domain(
        self,
        invite: Union[UserSystemDomainInviteSchema, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Invite a user to a system domain

        Args:
            invite: Invite data, either as UserSystemDomainInviteSchema or dict
            exclude_defaults: Whether to exclude default values when dumping
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=None)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        body = (invite.model_dump(exclude_defaults=exclude_defaults)
                if is_pydantic_model(invite) else invite)
        url = self.gen_url("invitation/")
        resp = self._post(url, json=body, **kwargs)
        return self.parse_response(resp, None)
