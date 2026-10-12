from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_apps_oauth_scopes_response_default import (
    GetAppsOauthScopesResponseDefault,
)
from ...models.o_auth_scopes_schema import OAuthScopesSchema
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/apps/oauth_scopes/",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetAppsOauthScopesResponseDefault | OAuthScopesSchema:
    if response.status_code == 200:
        response_200 = OAuthScopesSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = GetAppsOauthScopesResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetAppsOauthScopesResponseDefault | OAuthScopesSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetAppsOauthScopesResponseDefault | OAuthScopesSchema]:
    """List of OAuth scopes currently supported by the platform


    Required roles:
     - can_read_apps

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAppsOauthScopesResponseDefault | OAuthScopesSchema]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetAppsOauthScopesResponseDefault | OAuthScopesSchema | None:
    """List of OAuth scopes currently supported by the platform


    Required roles:
     - can_read_apps

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAppsOauthScopesResponseDefault | OAuthScopesSchema
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetAppsOauthScopesResponseDefault | OAuthScopesSchema]:
    """List of OAuth scopes currently supported by the platform


    Required roles:
     - can_read_apps

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAppsOauthScopesResponseDefault | OAuthScopesSchema]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetAppsOauthScopesResponseDefault | OAuthScopesSchema | None:
    """List of OAuth scopes currently supported by the platform


    Required roles:
     - can_read_apps

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAppsOauthScopesResponseDefault | OAuthScopesSchema
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
