from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_portals_by_portal_id_response_default import (
    GetPortalsByPortalIdResponseDefault,
)
from ...models.portal_schema import PortalSchema
from ...types import Response


def _get_kwargs(
    portal_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/portals/{portal_id}/".format(
            portal_id=quote(str(portal_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetPortalsByPortalIdResponseDefault | PortalSchema:
    if response.status_code == 200:
        response_200 = PortalSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = GetPortalsByPortalIdResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetPortalsByPortalIdResponseDefault | PortalSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    portal_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetPortalsByPortalIdResponseDefault | PortalSchema]:
    """Returns a particular portal by id


    Required roles:
     - can_read_portals

    Args:
        portal_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetPortalsByPortalIdResponseDefault | PortalSchema]
    """

    kwargs = _get_kwargs(
        portal_id=portal_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    portal_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetPortalsByPortalIdResponseDefault | PortalSchema | None:
    """Returns a particular portal by id


    Required roles:
     - can_read_portals

    Args:
        portal_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetPortalsByPortalIdResponseDefault | PortalSchema
    """

    return sync_detailed(
        portal_id=portal_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    portal_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetPortalsByPortalIdResponseDefault | PortalSchema]:
    """Returns a particular portal by id


    Required roles:
     - can_read_portals

    Args:
        portal_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetPortalsByPortalIdResponseDefault | PortalSchema]
    """

    kwargs = _get_kwargs(
        portal_id=portal_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    portal_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetPortalsByPortalIdResponseDefault | PortalSchema | None:
    """Returns a particular portal by id


    Required roles:
     - can_read_portals

    Args:
        portal_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetPortalsByPortalIdResponseDefault | PortalSchema
    """

    return (
        await asyncio_detailed(
            portal_id=portal_id,
            client=client,
        )
    ).parsed
