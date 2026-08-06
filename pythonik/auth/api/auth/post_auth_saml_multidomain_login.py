from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.multi_domain_user_systems_schema import MultiDomainUserSystemsSchema
from ...models.post_auth_saml_multidomain_login_response_default import (
    PostAuthSamlMultidomainLoginResponseDefault,
)
from ...models.saml_login_schema import SAMLLoginSchema
from ...types import Response


def _get_kwargs(
    *,
    body: SAMLLoginSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/auth/saml/multidomain/login/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | MultiDomainUserSystemsSchema | PostAuthSamlMultidomainLoginResponseDefault:
    if response.status_code == 200:
        response_200 = MultiDomainUserSystemsSchema.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = PostAuthSamlMultidomainLoginResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | MultiDomainUserSystemsSchema | PostAuthSamlMultidomainLoginResponseDefault
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SAMLLoginSchema,
) -> Response[
    Any | MultiDomainUserSystemsSchema | PostAuthSamlMultidomainLoginResponseDefault
]:
    """SAML Single sign-on url by domain

    Args:
        body (SAMLLoginSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | MultiDomainUserSystemsSchema | PostAuthSamlMultidomainLoginResponseDefault]
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
    body: SAMLLoginSchema,
) -> (
    Any
    | MultiDomainUserSystemsSchema
    | PostAuthSamlMultidomainLoginResponseDefault
    | None
):
    """SAML Single sign-on url by domain

    Args:
        body (SAMLLoginSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | MultiDomainUserSystemsSchema | PostAuthSamlMultidomainLoginResponseDefault
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SAMLLoginSchema,
) -> Response[
    Any | MultiDomainUserSystemsSchema | PostAuthSamlMultidomainLoginResponseDefault
]:
    """SAML Single sign-on url by domain

    Args:
        body (SAMLLoginSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | MultiDomainUserSystemsSchema | PostAuthSamlMultidomainLoginResponseDefault]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SAMLLoginSchema,
) -> (
    Any
    | MultiDomainUserSystemsSchema
    | PostAuthSamlMultidomainLoginResponseDefault
    | None
):
    """SAML Single sign-on url by domain

    Args:
        body (SAMLLoginSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | MultiDomainUserSystemsSchema | PostAuthSamlMultidomainLoginResponseDefault
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
