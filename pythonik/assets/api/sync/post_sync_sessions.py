from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_sync_sessions_response_default_type_0 import (
    PostSyncSessionsResponseDefaultType0,
)
from ...models.post_sync_sessions_response_default_type_1 import (
    PostSyncSessionsResponseDefaultType1,
)
from ...models.sync_session_create_schema import SyncSessionCreateSchema
from ...models.sync_session_schema import SyncSessionSchema
from ...types import Response


def _get_kwargs(
    *,
    body: SyncSessionCreateSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/sync/sessions/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | PostSyncSessionsResponseDefaultType0
    | PostSyncSessionsResponseDefaultType1
    | SyncSessionSchema
):
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
    ) -> PostSyncSessionsResponseDefaultType0 | PostSyncSessionsResponseDefaultType1:
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = PostSyncSessionsResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = PostSyncSessionsResponseDefaultType1.from_dict(data)

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostSyncSessionsResponseDefaultType0
    | PostSyncSessionsResponseDefaultType1
    | SyncSessionSchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SyncSessionCreateSchema,
) -> Response[
    Any
    | PostSyncSessionsResponseDefaultType0
    | PostSyncSessionsResponseDefaultType1
    | SyncSessionSchema
]:
    """Create a new sync session

    Args:
        body (SyncSessionCreateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostSyncSessionsResponseDefaultType0 | PostSyncSessionsResponseDefaultType1 | SyncSessionSchema]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: SyncSessionCreateSchema,
) -> (
    Any
    | PostSyncSessionsResponseDefaultType0
    | PostSyncSessionsResponseDefaultType1
    | SyncSessionSchema
    | None
):
    """Create a new sync session

    Args:
        body (SyncSessionCreateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostSyncSessionsResponseDefaultType0 | PostSyncSessionsResponseDefaultType1 | SyncSessionSchema
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SyncSessionCreateSchema,
) -> Response[
    Any
    | PostSyncSessionsResponseDefaultType0
    | PostSyncSessionsResponseDefaultType1
    | SyncSessionSchema
]:
    """Create a new sync session

    Args:
        body (SyncSessionCreateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostSyncSessionsResponseDefaultType0 | PostSyncSessionsResponseDefaultType1 | SyncSessionSchema]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SyncSessionCreateSchema,
) -> (
    Any
    | PostSyncSessionsResponseDefaultType0
    | PostSyncSessionsResponseDefaultType1
    | SyncSessionSchema
    | None
):
    """Create a new sync session

    Args:
        body (SyncSessionCreateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostSyncSessionsResponseDefaultType0 | PostSyncSessionsResponseDefaultType1 | SyncSessionSchema
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
