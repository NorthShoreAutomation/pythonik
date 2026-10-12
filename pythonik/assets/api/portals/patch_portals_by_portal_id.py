from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.patch_portals_by_portal_id_response_default import (
    PatchPortalsByPortalIdResponseDefault,
)
from ...models.portal_schema import PortalSchema
from ...types import Response


def _get_kwargs(
    portal_id: str,
    *,
    body: PortalSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/portals/{portal_id}/".format(
            portal_id=quote(str(portal_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PatchPortalsByPortalIdResponseDefault | PortalSchema:
    if response.status_code == 200:
        response_200 = PortalSchema.from_dict(response.json())

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

    response_default = PatchPortalsByPortalIdResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PatchPortalsByPortalIdResponseDefault | PortalSchema]:
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
    body: PortalSchema,
) -> Response[Any | PatchPortalsByPortalIdResponseDefault | PortalSchema]:
    """Update a portal


    Required roles:
     - can_write_portals

    Args:
        portal_id (str):
        body (PortalSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PatchPortalsByPortalIdResponseDefault | PortalSchema]
    """

    kwargs = _get_kwargs(
        portal_id=portal_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    portal_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PortalSchema,
) -> Any | PatchPortalsByPortalIdResponseDefault | PortalSchema | None:
    """Update a portal


    Required roles:
     - can_write_portals

    Args:
        portal_id (str):
        body (PortalSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PatchPortalsByPortalIdResponseDefault | PortalSchema
    """

    return sync_detailed(
        portal_id=portal_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    portal_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PortalSchema,
) -> Response[Any | PatchPortalsByPortalIdResponseDefault | PortalSchema]:
    """Update a portal


    Required roles:
     - can_write_portals

    Args:
        portal_id (str):
        body (PortalSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PatchPortalsByPortalIdResponseDefault | PortalSchema]
    """

    kwargs = _get_kwargs(
        portal_id=portal_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    portal_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PortalSchema,
) -> Any | PatchPortalsByPortalIdResponseDefault | PortalSchema | None:
    """Update a portal


    Required roles:
     - can_write_portals

    Args:
        portal_id (str):
        body (PortalSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PatchPortalsByPortalIdResponseDefault | PortalSchema
    """

    return (
        await asyncio_detailed(
            portal_id=portal_id,
            client=client,
            body=body,
        )
    ).parsed
