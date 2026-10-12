from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_themes_by_theme_id_response_default import (
    DeleteThemesByThemeIdResponseDefault,
)
from ...types import Response


def _get_kwargs(
    theme_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/themes/{theme_id}/".format(
            theme_id=quote(str(theme_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DeleteThemesByThemeIdResponseDefault:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = DeleteThemesByThemeIdResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DeleteThemesByThemeIdResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    theme_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DeleteThemesByThemeIdResponseDefault]:
    """Delete a particular theme by id


    Required roles:
     - can_delete_themes

    Args:
        theme_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteThemesByThemeIdResponseDefault]
    """

    kwargs = _get_kwargs(
        theme_id=theme_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    theme_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | DeleteThemesByThemeIdResponseDefault | None:
    """Delete a particular theme by id


    Required roles:
     - can_delete_themes

    Args:
        theme_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteThemesByThemeIdResponseDefault
    """

    return sync_detailed(
        theme_id=theme_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    theme_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DeleteThemesByThemeIdResponseDefault]:
    """Delete a particular theme by id


    Required roles:
     - can_delete_themes

    Args:
        theme_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteThemesByThemeIdResponseDefault]
    """

    kwargs = _get_kwargs(
        theme_id=theme_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    theme_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | DeleteThemesByThemeIdResponseDefault | None:
    """Delete a particular theme by id


    Required roles:
     - can_delete_themes

    Args:
        theme_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteThemesByThemeIdResponseDefault
    """

    return (
        await asyncio_detailed(
            theme_id=theme_id,
            client=client,
        )
    ).parsed
