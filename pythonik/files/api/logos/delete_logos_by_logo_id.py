from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_logos_by_logo_id_response_default import (
    DeleteLogosByLogoIdResponseDefault,
)
from ...types import Response


def _get_kwargs(
    logo_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/logos/{logo_id}/".format(
            logo_id=quote(str(logo_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DeleteLogosByLogoIdResponseDefault:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = DeleteLogosByLogoIdResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DeleteLogosByLogoIdResponseDefault]:
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
) -> Response[Any | DeleteLogosByLogoIdResponseDefault]:
    """Delete a particular logo by id, removing the stored image


    Required roles:
     - can_write_portals

    Args:
        logo_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteLogosByLogoIdResponseDefault]
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
) -> Any | DeleteLogosByLogoIdResponseDefault | None:
    """Delete a particular logo by id, removing the stored image


    Required roles:
     - can_write_portals

    Args:
        logo_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteLogosByLogoIdResponseDefault
    """

    return sync_detailed(
        logo_id=logo_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    logo_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DeleteLogosByLogoIdResponseDefault]:
    """Delete a particular logo by id, removing the stored image


    Required roles:
     - can_write_portals

    Args:
        logo_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteLogosByLogoIdResponseDefault]
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
) -> Any | DeleteLogosByLogoIdResponseDefault | None:
    """Delete a particular logo by id, removing the stored image


    Required roles:
     - can_write_portals

    Args:
        logo_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteLogosByLogoIdResponseDefault
    """

    return (
        await asyncio_detailed(
            logo_id=logo_id,
            client=client,
        )
    ).parsed
