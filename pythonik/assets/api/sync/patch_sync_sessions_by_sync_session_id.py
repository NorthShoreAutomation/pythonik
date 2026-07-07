from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.patch_sync_sessions_by_sync_session_id_response_default_type_0 import (
    PatchSyncSessionsBySyncSessionIdResponseDefaultType0,
)
from ...models.patch_sync_sessions_by_sync_session_id_response_default_type_1 import (
    PatchSyncSessionsBySyncSessionIdResponseDefaultType1,
)
from ...models.sync_session_schema import SyncSessionSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    sync_session_id: str,
    *,
    body: SyncSessionSchema,
    update_if_none: bool | Unset = False,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["update_if_none"] = update_if_none

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/sync/sessions/{sync_session_id}/".format(
            sync_session_id=quote(str(sync_session_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | PatchSyncSessionsBySyncSessionIdResponseDefaultType0
    | PatchSyncSessionsBySyncSessionIdResponseDefaultType1
    | SyncSessionSchema
):
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

    def _parse_response_default(
        data: object,
    ) -> (
        PatchSyncSessionsBySyncSessionIdResponseDefaultType0
        | PatchSyncSessionsBySyncSessionIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                PatchSyncSessionsBySyncSessionIdResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PatchSyncSessionsBySyncSessionIdResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PatchSyncSessionsBySyncSessionIdResponseDefaultType0
    | PatchSyncSessionsBySyncSessionIdResponseDefaultType1
    | SyncSessionSchema
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
    body: SyncSessionSchema,
    update_if_none: bool | Unset = False,
) -> Response[
    Any
    | PatchSyncSessionsBySyncSessionIdResponseDefaultType0
    | PatchSyncSessionsBySyncSessionIdResponseDefaultType1
    | SyncSessionSchema
]:
    """Edit a sync session. If the session doesn't exist, a new one is created

    Args:
        sync_session_id (str):
        update_if_none (bool | Unset):  Default: False.
        body (SyncSessionSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PatchSyncSessionsBySyncSessionIdResponseDefaultType0 | PatchSyncSessionsBySyncSessionIdResponseDefaultType1 | SyncSessionSchema]
    """

    kwargs = _get_kwargs(
        sync_session_id=sync_session_id,
        body=body,
        update_if_none=update_if_none,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    sync_session_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SyncSessionSchema,
    update_if_none: bool | Unset = False,
) -> (
    Any
    | PatchSyncSessionsBySyncSessionIdResponseDefaultType0
    | PatchSyncSessionsBySyncSessionIdResponseDefaultType1
    | SyncSessionSchema
    | None
):
    """Edit a sync session. If the session doesn't exist, a new one is created

    Args:
        sync_session_id (str):
        update_if_none (bool | Unset):  Default: False.
        body (SyncSessionSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PatchSyncSessionsBySyncSessionIdResponseDefaultType0 | PatchSyncSessionsBySyncSessionIdResponseDefaultType1 | SyncSessionSchema
    """

    return sync_detailed(
        sync_session_id=sync_session_id,
        client=client,
        body=body,
        update_if_none=update_if_none,
    ).parsed


async def asyncio_detailed(
    sync_session_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SyncSessionSchema,
    update_if_none: bool | Unset = False,
) -> Response[
    Any
    | PatchSyncSessionsBySyncSessionIdResponseDefaultType0
    | PatchSyncSessionsBySyncSessionIdResponseDefaultType1
    | SyncSessionSchema
]:
    """Edit a sync session. If the session doesn't exist, a new one is created

    Args:
        sync_session_id (str):
        update_if_none (bool | Unset):  Default: False.
        body (SyncSessionSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PatchSyncSessionsBySyncSessionIdResponseDefaultType0 | PatchSyncSessionsBySyncSessionIdResponseDefaultType1 | SyncSessionSchema]
    """

    kwargs = _get_kwargs(
        sync_session_id=sync_session_id,
        body=body,
        update_if_none=update_if_none,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sync_session_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SyncSessionSchema,
    update_if_none: bool | Unset = False,
) -> (
    Any
    | PatchSyncSessionsBySyncSessionIdResponseDefaultType0
    | PatchSyncSessionsBySyncSessionIdResponseDefaultType1
    | SyncSessionSchema
    | None
):
    """Edit a sync session. If the session doesn't exist, a new one is created

    Args:
        sync_session_id (str):
        update_if_none (bool | Unset):  Default: False.
        body (SyncSessionSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PatchSyncSessionsBySyncSessionIdResponseDefaultType0 | PatchSyncSessionsBySyncSessionIdResponseDefaultType1 | SyncSessionSchema
    """

    return (
        await asyncio_detailed(
            sync_session_id=sync_session_id,
            client=client,
            body=body,
            update_if_none=update_if_none,
        )
    ).parsed
