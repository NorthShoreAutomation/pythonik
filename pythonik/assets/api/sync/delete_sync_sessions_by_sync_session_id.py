from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_sync_sessions_by_sync_session_id_response_default_type_0 import (
    DeleteSyncSessionsBySyncSessionIdResponseDefaultType0,
)
from ...models.delete_sync_sessions_by_sync_session_id_response_default_type_1 import (
    DeleteSyncSessionsBySyncSessionIdResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    sync_session_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/sync/sessions/{sync_session_id}/".format(
            sync_session_id=quote(str(sync_session_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | DeleteSyncSessionsBySyncSessionIdResponseDefaultType0
    | DeleteSyncSessionsBySyncSessionIdResponseDefaultType1
):
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

    def _parse_response_default(
        data: object,
    ) -> (
        DeleteSyncSessionsBySyncSessionIdResponseDefaultType0
        | DeleteSyncSessionsBySyncSessionIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                DeleteSyncSessionsBySyncSessionIdResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            DeleteSyncSessionsBySyncSessionIdResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | DeleteSyncSessionsBySyncSessionIdResponseDefaultType0
    | DeleteSyncSessionsBySyncSessionIdResponseDefaultType1
]:
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
) -> Response[
    Any
    | DeleteSyncSessionsBySyncSessionIdResponseDefaultType0
    | DeleteSyncSessionsBySyncSessionIdResponseDefaultType1
]:
    """Delete a particular sync session by id

    Args:
        sync_session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteSyncSessionsBySyncSessionIdResponseDefaultType0 | DeleteSyncSessionsBySyncSessionIdResponseDefaultType1]
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
) -> (
    Any
    | DeleteSyncSessionsBySyncSessionIdResponseDefaultType0
    | DeleteSyncSessionsBySyncSessionIdResponseDefaultType1
    | None
):
    """Delete a particular sync session by id

    Args:
        sync_session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteSyncSessionsBySyncSessionIdResponseDefaultType0 | DeleteSyncSessionsBySyncSessionIdResponseDefaultType1
    """

    return sync_detailed(
        sync_session_id=sync_session_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    sync_session_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | DeleteSyncSessionsBySyncSessionIdResponseDefaultType0
    | DeleteSyncSessionsBySyncSessionIdResponseDefaultType1
]:
    """Delete a particular sync session by id

    Args:
        sync_session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteSyncSessionsBySyncSessionIdResponseDefaultType0 | DeleteSyncSessionsBySyncSessionIdResponseDefaultType1]
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
) -> (
    Any
    | DeleteSyncSessionsBySyncSessionIdResponseDefaultType0
    | DeleteSyncSessionsBySyncSessionIdResponseDefaultType1
    | None
):
    """Delete a particular sync session by id

    Args:
        sync_session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteSyncSessionsBySyncSessionIdResponseDefaultType0 | DeleteSyncSessionsBySyncSessionIdResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            sync_session_id=sync_session_id,
            client=client,
        )
    ).parsed
