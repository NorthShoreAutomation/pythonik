from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_queue_schema import DeleteQueueSchema
from ...models.post_delete_queue_file_sets_purge_response_default import (
    PostDeleteQueueFileSetsPurgeResponseDefault,
)
from ...types import Response


def _get_kwargs(
    *,
    body: DeleteQueueSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/delete_queue/file_sets/purge/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostDeleteQueueFileSetsPurgeResponseDefault:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = PostDeleteQueueFileSetsPurgeResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PostDeleteQueueFileSetsPurgeResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DeleteQueueSchema,
) -> Response[Any | PostDeleteQueueFileSetsPurgeResponseDefault]:
    """Purge file sets from delete queue (Permanently delete)


    Required roles:
     - can_purge_files

    Args:
        body (DeleteQueueSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostDeleteQueueFileSetsPurgeResponseDefault]
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
    body: DeleteQueueSchema,
) -> Any | PostDeleteQueueFileSetsPurgeResponseDefault | None:
    """Purge file sets from delete queue (Permanently delete)


    Required roles:
     - can_purge_files

    Args:
        body (DeleteQueueSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostDeleteQueueFileSetsPurgeResponseDefault
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DeleteQueueSchema,
) -> Response[Any | PostDeleteQueueFileSetsPurgeResponseDefault]:
    """Purge file sets from delete queue (Permanently delete)


    Required roles:
     - can_purge_files

    Args:
        body (DeleteQueueSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostDeleteQueueFileSetsPurgeResponseDefault]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: DeleteQueueSchema,
) -> Any | PostDeleteQueueFileSetsPurgeResponseDefault | None:
    """Purge file sets from delete queue (Permanently delete)


    Required roles:
     - can_purge_files

    Args:
        body (DeleteQueueSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostDeleteQueueFileSetsPurgeResponseDefault
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
