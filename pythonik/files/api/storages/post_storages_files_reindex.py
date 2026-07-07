from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_storages_files_reindex_response_default_type_0 import (
    PostStoragesFilesReindexResponseDefaultType0,
)
from ...models.post_storages_files_reindex_response_default_type_1 import (
    PostStoragesFilesReindexResponseDefaultType1,
)
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/storages/files/reindex/",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | PostStoragesFilesReindexResponseDefaultType0
    | PostStoragesFilesReindexResponseDefaultType1
):
    if response.status_code == 201:
        response_201 = cast(Any, None)
        return response_201

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    def _parse_response_default(
        data: object,
    ) -> (
        PostStoragesFilesReindexResponseDefaultType0
        | PostStoragesFilesReindexResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                PostStoragesFilesReindexResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PostStoragesFilesReindexResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostStoragesFilesReindexResponseDefaultType0
    | PostStoragesFilesReindexResponseDefaultType1
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
) -> Response[
    Any
    | PostStoragesFilesReindexResponseDefaultType0
    | PostStoragesFilesReindexResponseDefaultType1
]:
    """Trigger reindexing of all files


    Required roles:
     - can_reindex_storages

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostStoragesFilesReindexResponseDefaultType0 | PostStoragesFilesReindexResponseDefaultType1]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | PostStoragesFilesReindexResponseDefaultType0
    | PostStoragesFilesReindexResponseDefaultType1
    | None
):
    """Trigger reindexing of all files


    Required roles:
     - can_reindex_storages

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostStoragesFilesReindexResponseDefaultType0 | PostStoragesFilesReindexResponseDefaultType1
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | PostStoragesFilesReindexResponseDefaultType0
    | PostStoragesFilesReindexResponseDefaultType1
]:
    """Trigger reindexing of all files


    Required roles:
     - can_reindex_storages

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostStoragesFilesReindexResponseDefaultType0 | PostStoragesFilesReindexResponseDefaultType1]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | PostStoragesFilesReindexResponseDefaultType0
    | PostStoragesFilesReindexResponseDefaultType1
    | None
):
    """Trigger reindexing of all files


    Required roles:
     - can_reindex_storages

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostStoragesFilesReindexResponseDefaultType0 | PostStoragesFilesReindexResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
