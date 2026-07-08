from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.identity_provider_schema import IdentityProviderSchema
from ...models.post_auth_saml_idp_response_default import PostAuthSamlIdpResponseDefault
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: IdentityProviderSchema | IdentityProviderSchema | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/auth/saml/idp/",
    }

    if isinstance(body, IdentityProviderSchema):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, IdentityProviderSchema):
        _kwargs["content"] = body.payload
        headers["Content-Type"] = "application/xml"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | IdentityProviderSchema | PostAuthSamlIdpResponseDefault:
    if response.status_code == 201:
        response_201 = IdentityProviderSchema.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = PostAuthSamlIdpResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | IdentityProviderSchema | PostAuthSamlIdpResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: IdentityProviderSchema | IdentityProviderSchema | Unset = UNSET,
) -> Response[Any | IdentityProviderSchema | PostAuthSamlIdpResponseDefault]:
    """Create a new identity provider.

     <br/>Input can either be an IdentityProviderSchema as json or a SAML<br/>EntityDescriptor
    XML.<br/>Input can either be an IdentityProviderSchema as json or a SAML<br/>EntityDescriptor XML.
    Required roles:
     - can_write_identity_providers

    Args:
        body (IdentityProviderSchema):
        body (IdentityProviderSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | IdentityProviderSchema | PostAuthSamlIdpResponseDefault]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: IdentityProviderSchema | IdentityProviderSchema | Unset = UNSET,
) -> Any | IdentityProviderSchema | PostAuthSamlIdpResponseDefault | None:
    """Create a new identity provider.

     <br/>Input can either be an IdentityProviderSchema as json or a SAML<br/>EntityDescriptor
    XML.<br/>Input can either be an IdentityProviderSchema as json or a SAML<br/>EntityDescriptor XML.
    Required roles:
     - can_write_identity_providers

    Args:
        body (IdentityProviderSchema):
        body (IdentityProviderSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | IdentityProviderSchema | PostAuthSamlIdpResponseDefault
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: IdentityProviderSchema | IdentityProviderSchema | Unset = UNSET,
) -> Response[Any | IdentityProviderSchema | PostAuthSamlIdpResponseDefault]:
    """Create a new identity provider.

     <br/>Input can either be an IdentityProviderSchema as json or a SAML<br/>EntityDescriptor
    XML.<br/>Input can either be an IdentityProviderSchema as json or a SAML<br/>EntityDescriptor XML.
    Required roles:
     - can_write_identity_providers

    Args:
        body (IdentityProviderSchema):
        body (IdentityProviderSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | IdentityProviderSchema | PostAuthSamlIdpResponseDefault]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: IdentityProviderSchema | IdentityProviderSchema | Unset = UNSET,
) -> Any | IdentityProviderSchema | PostAuthSamlIdpResponseDefault | None:
    """Create a new identity provider.

     <br/>Input can either be an IdentityProviderSchema as json or a SAML<br/>EntityDescriptor
    XML.<br/>Input can either be an IdentityProviderSchema as json or a SAML<br/>EntityDescriptor XML.
    Required roles:
     - can_write_identity_providers

    Args:
        body (IdentityProviderSchema):
        body (IdentityProviderSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | IdentityProviderSchema | PostAuthSamlIdpResponseDefault
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
