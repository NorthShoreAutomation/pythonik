from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.group_schema import GroupSchema
from ...models.patch_groups_by_group_id_response_default import (
    PatchGroupsByGroupIdResponseDefault,
)
from ...types import Response


def _get_kwargs(
    group_id: str,
    *,
    body: GroupSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/groups/{group_id}/".format(
            group_id=quote(str(group_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GroupSchema | PatchGroupsByGroupIdResponseDefault:
    if response.status_code == 200:
        response_200 = GroupSchema.from_dict(response.json())

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

    response_default = PatchGroupsByGroupIdResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GroupSchema | PatchGroupsByGroupIdResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: GroupSchema,
) -> Response[Any | GroupSchema | PatchGroupsByGroupIdResponseDefault]:
    """Update group


    Required roles:
     - can_write_groups

    Args:
        group_id (str):
        body (GroupSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GroupSchema | PatchGroupsByGroupIdResponseDefault]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: GroupSchema,
) -> Any | GroupSchema | PatchGroupsByGroupIdResponseDefault | None:
    """Update group


    Required roles:
     - can_write_groups

    Args:
        group_id (str):
        body (GroupSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GroupSchema | PatchGroupsByGroupIdResponseDefault
    """

    return sync_detailed(
        group_id=group_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    group_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: GroupSchema,
) -> Response[Any | GroupSchema | PatchGroupsByGroupIdResponseDefault]:
    """Update group


    Required roles:
     - can_write_groups

    Args:
        group_id (str):
        body (GroupSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GroupSchema | PatchGroupsByGroupIdResponseDefault]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: GroupSchema,
) -> Any | GroupSchema | PatchGroupsByGroupIdResponseDefault | None:
    """Update group


    Required roles:
     - can_write_groups

    Args:
        group_id (str):
        body (GroupSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GroupSchema | PatchGroupsByGroupIdResponseDefault
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
            body=body,
        )
    ).parsed
