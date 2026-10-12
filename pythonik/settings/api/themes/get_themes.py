from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_themes_response_default import GetThemesResponseDefault
from ...models.themes_schema import ThemesSchema
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/themes/",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetThemesResponseDefault | ThemesSchema:
    if response.status_code == 200:
        response_200 = ThemesSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = GetThemesResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetThemesResponseDefault | ThemesSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetThemesResponseDefault | ThemesSchema]:
    """Get list of themes


    Required roles:
     - can_read_themes

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetThemesResponseDefault | ThemesSchema]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetThemesResponseDefault | ThemesSchema | None:
    """Get list of themes


    Required roles:
     - can_read_themes

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetThemesResponseDefault | ThemesSchema
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetThemesResponseDefault | ThemesSchema]:
    """Get list of themes


    Required roles:
     - can_read_themes

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetThemesResponseDefault | ThemesSchema]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetThemesResponseDefault | ThemesSchema | None:
    """Get list of themes


    Required roles:
     - can_read_themes

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetThemesResponseDefault | ThemesSchema
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
