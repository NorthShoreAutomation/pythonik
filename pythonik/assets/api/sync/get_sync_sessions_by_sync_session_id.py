from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_sync_sessions_by_sync_session_id_response_default import (
    GetSyncSessionsBySyncSessionIdResponseDefault,
)
from ...models.sync_session_schema import SyncSessionSchema
from ...types import Response


def _get_kwargs(
    sync_session_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/sync/sessions/{sync_session_id}/".format(
            sync_session_id=quote(str(sync_session_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetSyncSessionsBySyncSessionIdResponseDefault | SyncSessionSchema:
    if response.status_code == 200:
        response_200 = SyncSessionSchema.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = SyncSessionSchema.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = GetSyncSessionsBySyncSessionIdResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetSyncSessionsBySyncSessionIdResponseDefault | SyncSessionSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    sync_session_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetSyncSessionsBySyncSessionIdResponseDefault | SyncSessionSchema]:
    """Returns a particular sync session by id. If a session with such id doesn't exist,

     a new one is created

    Args:
        sync_session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSyncSessionsBySyncSessionIdResponseDefault | SyncSessionSchema]
    """

    kwargs = _get_kwargs(
        sync_session_id=sync_session_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    sync_session_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetSyncSessionsBySyncSessionIdResponseDefault | SyncSessionSchema | None:
    """Returns a particular sync session by id. If a session with such id doesn't exist,

     a new one is created

    Args:
        sync_session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSyncSessionsBySyncSessionIdResponseDefault | SyncSessionSchema
    """

    return sync_detailed(
        sync_session_id=sync_session_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    sync_session_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetSyncSessionsBySyncSessionIdResponseDefault | SyncSessionSchema]:
    """Returns a particular sync session by id. If a session with such id doesn't exist,

     a new one is created

    Args:
        sync_session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSyncSessionsBySyncSessionIdResponseDefault | SyncSessionSchema]
    """

    kwargs = _get_kwargs(
        sync_session_id=sync_session_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sync_session_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetSyncSessionsBySyncSessionIdResponseDefault | SyncSessionSchema | None:
    """Returns a particular sync session by id. If a session with such id doesn't exist,

     a new one is created

    Args:
        sync_session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSyncSessionsBySyncSessionIdResponseDefault | SyncSessionSchema
    """

    return (
        await asyncio_detailed(
            sync_session_id=sync_session_id,
            client=client,
        )
    ).parsed
