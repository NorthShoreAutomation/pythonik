from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_apps_by_app_id_token_response_default import (
    PostAppsByAppIdTokenResponseDefault,
)
from ...models.token_schema import TokenSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    app_id: str,
    *,
    expires_in: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["expires_in"] = expires_in

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/apps/{app_id}/token/".format(
            app_id=quote(str(app_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostAppsByAppIdTokenResponseDefault | TokenSchema:
    if response.status_code == 200:
        response_200 = TokenSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = PostAppsByAppIdTokenResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PostAppsByAppIdTokenResponseDefault | TokenSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    app_id: str,
    *,
    client: AuthenticatedClient | Client,
    expires_in: int | Unset = UNSET,
) -> Response[Any | PostAppsByAppIdTokenResponseDefault | TokenSchema]:
    """Creates app token by id and returns it's data


    Required roles:
     - can_read_apps

    Args:
        app_id (str):
        expires_in (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostAppsByAppIdTokenResponseDefault | TokenSchema]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        expires_in=expires_in,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    app_id: str,
    *,
    client: AuthenticatedClient | Client,
    expires_in: int | Unset = UNSET,
) -> Any | PostAppsByAppIdTokenResponseDefault | TokenSchema | None:
    """Creates app token by id and returns it's data


    Required roles:
     - can_read_apps

    Args:
        app_id (str):
        expires_in (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostAppsByAppIdTokenResponseDefault | TokenSchema
    """

    return sync_detailed(
        app_id=app_id,
        client=client,
        expires_in=expires_in,
    ).parsed


async def asyncio_detailed(
    app_id: str,
    *,
    client: AuthenticatedClient | Client,
    expires_in: int | Unset = UNSET,
) -> Response[Any | PostAppsByAppIdTokenResponseDefault | TokenSchema]:
    """Creates app token by id and returns it's data


    Required roles:
     - can_read_apps

    Args:
        app_id (str):
        expires_in (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostAppsByAppIdTokenResponseDefault | TokenSchema]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        expires_in=expires_in,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_id: str,
    *,
    client: AuthenticatedClient | Client,
    expires_in: int | Unset = UNSET,
) -> Any | PostAppsByAppIdTokenResponseDefault | TokenSchema | None:
    """Creates app token by id and returns it's data


    Required roles:
     - can_read_apps

    Args:
        app_id (str):
        expires_in (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostAppsByAppIdTokenResponseDefault | TokenSchema
    """

    return (
        await asyncio_detailed(
            app_id=app_id,
            client=client,
            expires_in=expires_in,
        )
    ).parsed
