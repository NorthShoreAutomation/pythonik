from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_assets_by_asset_id_files_by_file_id_reindex_body import (
    PostAssetsByAssetIdFilesByFileIdReindexBody,
)
from ...models.post_assets_by_asset_id_files_by_file_id_reindex_response_default import (
    PostAssetsByAssetIdFilesByFileIdReindexResponseDefault,
)
from ...types import Response


def _get_kwargs(
    asset_id: str,
    file_id: str,
    *,
    body: PostAssetsByAssetIdFilesByFileIdReindexBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/assets/{asset_id}/files/{file_id}/reindex/".format(
            asset_id=quote(str(asset_id), safe=""),
            file_id=quote(str(file_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostAssetsByAssetIdFilesByFileIdReindexResponseDefault:
    if response.status_code == 201:
        response_201 = cast(Any, None)
        return response_201

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = PostAssetsByAssetIdFilesByFileIdReindexResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PostAssetsByAssetIdFilesByFileIdReindexResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    asset_id: str,
    file_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostAssetsByAssetIdFilesByFileIdReindexBody,
) -> Response[Any | PostAssetsByAssetIdFilesByFileIdReindexResponseDefault]:
    """Trigger reindexing of a file


    Required roles:
     - can_reindex_storages

    Args:
        asset_id (str):
        file_id (str):
        body (PostAssetsByAssetIdFilesByFileIdReindexBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostAssetsByAssetIdFilesByFileIdReindexResponseDefault]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        file_id=file_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: str,
    file_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostAssetsByAssetIdFilesByFileIdReindexBody,
) -> Any | PostAssetsByAssetIdFilesByFileIdReindexResponseDefault | None:
    """Trigger reindexing of a file


    Required roles:
     - can_reindex_storages

    Args:
        asset_id (str):
        file_id (str):
        body (PostAssetsByAssetIdFilesByFileIdReindexBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostAssetsByAssetIdFilesByFileIdReindexResponseDefault
    """

    return sync_detailed(
        asset_id=asset_id,
        file_id=file_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    file_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostAssetsByAssetIdFilesByFileIdReindexBody,
) -> Response[Any | PostAssetsByAssetIdFilesByFileIdReindexResponseDefault]:
    """Trigger reindexing of a file


    Required roles:
     - can_reindex_storages

    Args:
        asset_id (str):
        file_id (str):
        body (PostAssetsByAssetIdFilesByFileIdReindexBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostAssetsByAssetIdFilesByFileIdReindexResponseDefault]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        file_id=file_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    file_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostAssetsByAssetIdFilesByFileIdReindexBody,
) -> Any | PostAssetsByAssetIdFilesByFileIdReindexResponseDefault | None:
    """Trigger reindexing of a file


    Required roles:
     - can_reindex_storages

    Args:
        asset_id (str):
        file_id (str):
        body (PostAssetsByAssetIdFilesByFileIdReindexBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostAssetsByAssetIdFilesByFileIdReindexResponseDefault
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            file_id=file_id,
            client=client,
            body=body,
        )
    ).parsed
