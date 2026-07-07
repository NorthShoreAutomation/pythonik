from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_auth_saml_acs_by_system_domain_id_by_identity_provider_id_response_default_type_0 import (
    PostAuthSamlAcsBySystemDomainIdByIdentityProviderIdResponseDefaultType0,
)
from ...models.post_auth_saml_acs_by_system_domain_id_by_identity_provider_id_response_default_type_1 import (
    PostAuthSamlAcsBySystemDomainIdByIdentityProviderIdResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    system_domain_id: str,
    identity_provider_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/auth/saml/acs/{system_domain_id}/{identity_provider_id}/".format(
            system_domain_id=quote(str(system_domain_id), safe=""),
            identity_provider_id=quote(str(identity_provider_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | PostAuthSamlAcsBySystemDomainIdByIdentityProviderIdResponseDefaultType0
    | PostAuthSamlAcsBySystemDomainIdByIdentityProviderIdResponseDefaultType1
):
    if response.status_code == 302:
        response_302 = cast(Any, None)
        return response_302

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    def _parse_response_default(
        data: object,
    ) -> (
        PostAuthSamlAcsBySystemDomainIdByIdentityProviderIdResponseDefaultType0
        | PostAuthSamlAcsBySystemDomainIdByIdentityProviderIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = PostAuthSamlAcsBySystemDomainIdByIdentityProviderIdResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = PostAuthSamlAcsBySystemDomainIdByIdentityProviderIdResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostAuthSamlAcsBySystemDomainIdByIdentityProviderIdResponseDefaultType0
    | PostAuthSamlAcsBySystemDomainIdByIdentityProviderIdResponseDefaultType1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    system_domain_id: str,
    identity_provider_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | PostAuthSamlAcsBySystemDomainIdByIdentityProviderIdResponseDefaultType0
    | PostAuthSamlAcsBySystemDomainIdByIdentityProviderIdResponseDefaultType1
]:
    """SAML Assertion Consumer Service

    Args:
        system_domain_id (str):
        identity_provider_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostAuthSamlAcsBySystemDomainIdByIdentityProviderIdResponseDefaultType0 | PostAuthSamlAcsBySystemDomainIdByIdentityProviderIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        system_domain_id=system_domain_id,
        identity_provider_id=identity_provider_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    system_domain_id: str,
    identity_provider_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | PostAuthSamlAcsBySystemDomainIdByIdentityProviderIdResponseDefaultType0
    | PostAuthSamlAcsBySystemDomainIdByIdentityProviderIdResponseDefaultType1
    | None
):
    """SAML Assertion Consumer Service

    Args:
        system_domain_id (str):
        identity_provider_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostAuthSamlAcsBySystemDomainIdByIdentityProviderIdResponseDefaultType0 | PostAuthSamlAcsBySystemDomainIdByIdentityProviderIdResponseDefaultType1
    """

    return sync_detailed(
        system_domain_id=system_domain_id,
        identity_provider_id=identity_provider_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    system_domain_id: str,
    identity_provider_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | PostAuthSamlAcsBySystemDomainIdByIdentityProviderIdResponseDefaultType0
    | PostAuthSamlAcsBySystemDomainIdByIdentityProviderIdResponseDefaultType1
]:
    """SAML Assertion Consumer Service

    Args:
        system_domain_id (str):
        identity_provider_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostAuthSamlAcsBySystemDomainIdByIdentityProviderIdResponseDefaultType0 | PostAuthSamlAcsBySystemDomainIdByIdentityProviderIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        system_domain_id=system_domain_id,
        identity_provider_id=identity_provider_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    system_domain_id: str,
    identity_provider_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | PostAuthSamlAcsBySystemDomainIdByIdentityProviderIdResponseDefaultType0
    | PostAuthSamlAcsBySystemDomainIdByIdentityProviderIdResponseDefaultType1
    | None
):
    """SAML Assertion Consumer Service

    Args:
        system_domain_id (str):
        identity_provider_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostAuthSamlAcsBySystemDomainIdByIdentityProviderIdResponseDefaultType0 | PostAuthSamlAcsBySystemDomainIdByIdentityProviderIdResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            system_domain_id=system_domain_id,
            identity_provider_id=identity_provider_id,
            client=client,
        )
    ).parsed
