from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_assets_by_asset_id_file_sets_by_file_set_id_response_default import (
    DeleteAssetsByAssetIdFileSetsByFileSetIdResponseDefault,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    asset_id: str,
    file_set_id: str,
    *,
    keep_source: bool | Unset = UNSET,
    immediately: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["keep_source"] = keep_source

    params["immediately"] = immediately

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/assets/{asset_id}/file_sets/{file_set_id}/".format(
            asset_id=quote(str(asset_id), safe=""),
            file_set_id=quote(str(file_set_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DeleteAssetsByAssetIdFileSetsByFileSetIdResponseDefault:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = (
        DeleteAssetsByAssetIdFileSetsByFileSetIdResponseDefault.from_dict(
            response.json()
        )
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DeleteAssetsByAssetIdFileSetsByFileSetIdResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    asset_id: str,
    file_set_id: str,
    *,
    client: AuthenticatedClient | Client,
    keep_source: bool | Unset = UNSET,
    immediately: bool | Unset = UNSET,
) -> Response[Any | DeleteAssetsByAssetIdFileSetsByFileSetIdResponseDefault]:
    """Delete asset's file set, file entries, and actual files


    Required roles:
     - can_delete_files

    Args:
        asset_id (str):
        file_set_id (str):
        keep_source (bool | Unset):
        immediately (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteAssetsByAssetIdFileSetsByFileSetIdResponseDefault]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        file_set_id=file_set_id,
        keep_source=keep_source,
        immediately=immediately,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: str,
    file_set_id: str,
    *,
    client: AuthenticatedClient | Client,
    keep_source: bool | Unset = UNSET,
    immediately: bool | Unset = UNSET,
) -> Any | DeleteAssetsByAssetIdFileSetsByFileSetIdResponseDefault | None:
    """Delete asset's file set, file entries, and actual files


    Required roles:
     - can_delete_files

    Args:
        asset_id (str):
        file_set_id (str):
        keep_source (bool | Unset):
        immediately (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteAssetsByAssetIdFileSetsByFileSetIdResponseDefault
    """

    return sync_detailed(
        asset_id=asset_id,
        file_set_id=file_set_id,
        client=client,
        keep_source=keep_source,
        immediately=immediately,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    file_set_id: str,
    *,
    client: AuthenticatedClient | Client,
    keep_source: bool | Unset = UNSET,
    immediately: bool | Unset = UNSET,
) -> Response[Any | DeleteAssetsByAssetIdFileSetsByFileSetIdResponseDefault]:
    """Delete asset's file set, file entries, and actual files


    Required roles:
     - can_delete_files

    Args:
        asset_id (str):
        file_set_id (str):
        keep_source (bool | Unset):
        immediately (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteAssetsByAssetIdFileSetsByFileSetIdResponseDefault]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        file_set_id=file_set_id,
        keep_source=keep_source,
        immediately=immediately,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    file_set_id: str,
    *,
    client: AuthenticatedClient | Client,
    keep_source: bool | Unset = UNSET,
    immediately: bool | Unset = UNSET,
) -> Any | DeleteAssetsByAssetIdFileSetsByFileSetIdResponseDefault | None:
    """Delete asset's file set, file entries, and actual files


    Required roles:
     - can_delete_files

    Args:
        asset_id (str):
        file_set_id (str):
        keep_source (bool | Unset):
        immediately (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteAssetsByAssetIdFileSetsByFileSetIdResponseDefault
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            file_set_id=file_set_id,
            client=client,
            keep_source=keep_source,
            immediately=immediately,
        )
    ).parsed
