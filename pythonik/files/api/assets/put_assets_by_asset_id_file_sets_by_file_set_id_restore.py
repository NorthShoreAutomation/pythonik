from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.put_assets_by_asset_id_file_sets_by_file_set_id_restore_response_default import (
    PutAssetsByAssetIdFileSetsByFileSetIdRestoreResponseDefault,
)
from ...types import Response


def _get_kwargs(
    asset_id: str,
    file_set_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/assets/{asset_id}/file_sets/{file_set_id}/restore/".format(
            asset_id=quote(str(asset_id), safe=""),
            file_set_id=quote(str(file_set_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PutAssetsByAssetIdFileSetsByFileSetIdRestoreResponseDefault:
    if response.status_code == 200:
        response_200 = cast(Any, None)
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

    response_default = (
        PutAssetsByAssetIdFileSetsByFileSetIdRestoreResponseDefault.from_dict(
            response.json()
        )
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PutAssetsByAssetIdFileSetsByFileSetIdRestoreResponseDefault]:
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
) -> Response[Any | PutAssetsByAssetIdFileSetsByFileSetIdRestoreResponseDefault]:
    """Restore delete asset's file set


    Required roles:
     - can_write_files

    Args:
        asset_id (str):
        file_set_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutAssetsByAssetIdFileSetsByFileSetIdRestoreResponseDefault]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        file_set_id=file_set_id,
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
) -> Any | PutAssetsByAssetIdFileSetsByFileSetIdRestoreResponseDefault | None:
    """Restore delete asset's file set


    Required roles:
     - can_write_files

    Args:
        asset_id (str):
        file_set_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutAssetsByAssetIdFileSetsByFileSetIdRestoreResponseDefault
    """

    return sync_detailed(
        asset_id=asset_id,
        file_set_id=file_set_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    file_set_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | PutAssetsByAssetIdFileSetsByFileSetIdRestoreResponseDefault]:
    """Restore delete asset's file set


    Required roles:
     - can_write_files

    Args:
        asset_id (str):
        file_set_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutAssetsByAssetIdFileSetsByFileSetIdRestoreResponseDefault]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        file_set_id=file_set_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    file_set_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | PutAssetsByAssetIdFileSetsByFileSetIdRestoreResponseDefault | None:
    """Restore delete asset's file set


    Required roles:
     - can_write_files

    Args:
        asset_id (str):
        file_set_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutAssetsByAssetIdFileSetsByFileSetIdRestoreResponseDefault
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            file_set_id=file_set_id,
            client=client,
        )
    ).parsed
