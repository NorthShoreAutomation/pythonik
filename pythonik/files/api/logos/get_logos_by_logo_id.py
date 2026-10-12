from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_logos_by_logo_id_response_default import (
    GetLogosByLogoIdResponseDefault,
)
from ...models.logo_schema import LogoSchema
from ...types import Response


def _get_kwargs(
    logo_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/logos/{logo_id}/".format(
            logo_id=quote(str(logo_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetLogosByLogoIdResponseDefault | LogoSchema:
    if response.status_code == 200:
        response_200 = LogoSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = GetLogosByLogoIdResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetLogosByLogoIdResponseDefault | LogoSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    logo_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetLogosByLogoIdResponseDefault | LogoSchema]:
    """Returns a particular logo by id


    Required roles:
     - can_read_portals

    Args:
        logo_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetLogosByLogoIdResponseDefault | LogoSchema]
    """

    kwargs = _get_kwargs(
        logo_id=logo_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    logo_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetLogosByLogoIdResponseDefault | LogoSchema | None:
    """Returns a particular logo by id


    Required roles:
     - can_read_portals

    Args:
        logo_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetLogosByLogoIdResponseDefault | LogoSchema
    """

    return sync_detailed(
        logo_id=logo_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    logo_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetLogosByLogoIdResponseDefault | LogoSchema]:
    """Returns a particular logo by id


    Required roles:
     - can_read_portals

    Args:
        logo_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetLogosByLogoIdResponseDefault | LogoSchema]
    """

    kwargs = _get_kwargs(
        logo_id=logo_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    logo_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetLogosByLogoIdResponseDefault | LogoSchema | None:
    """Returns a particular logo by id


    Required roles:
     - can_read_portals

    Args:
        logo_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetLogosByLogoIdResponseDefault | LogoSchema
    """

    return (
        await asyncio_detailed(
            logo_id=logo_id,
            client=client,
        )
    ).parsed
