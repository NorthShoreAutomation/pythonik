from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.put_themes_by_theme_id_response_default import (
    PutThemesByThemeIdResponseDefault,
)
from ...models.theme_schema import ThemeSchema
from ...types import Response


def _get_kwargs(
    theme_id: str,
    *,
    body: ThemeSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/themes/{theme_id}/".format(
            theme_id=quote(str(theme_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PutThemesByThemeIdResponseDefault | ThemeSchema:
    if response.status_code == 200:
        response_200 = ThemeSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = PutThemesByThemeIdResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PutThemesByThemeIdResponseDefault | ThemeSchema]:
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
    body: ThemeSchema,
) -> Response[Any | PutThemesByThemeIdResponseDefault | ThemeSchema]:
    """Update a theme


    Required roles:
     - can_write_themes

    Args:
        theme_id (str):
        body (ThemeSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutThemesByThemeIdResponseDefault | ThemeSchema]
    """

    kwargs = _get_kwargs(
        theme_id=theme_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    theme_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ThemeSchema,
) -> Any | PutThemesByThemeIdResponseDefault | ThemeSchema | None:
    """Update a theme


    Required roles:
     - can_write_themes

    Args:
        theme_id (str):
        body (ThemeSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutThemesByThemeIdResponseDefault | ThemeSchema
    """

    return sync_detailed(
        theme_id=theme_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    theme_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ThemeSchema,
) -> Response[Any | PutThemesByThemeIdResponseDefault | ThemeSchema]:
    """Update a theme


    Required roles:
     - can_write_themes

    Args:
        theme_id (str):
        body (ThemeSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutThemesByThemeIdResponseDefault | ThemeSchema]
    """

    kwargs = _get_kwargs(
        theme_id=theme_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    theme_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ThemeSchema,
) -> Any | PutThemesByThemeIdResponseDefault | ThemeSchema | None:
    """Update a theme


    Required roles:
     - can_write_themes

    Args:
        theme_id (str):
        body (ThemeSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutThemesByThemeIdResponseDefault | ThemeSchema
    """

    return (
        await asyncio_detailed(
            theme_id=theme_id,
            client=client,
            body=body,
        )
    ).parsed
