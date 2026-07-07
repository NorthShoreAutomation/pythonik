from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.file_sets_schema import FileSetsSchema
from ...models.get_assets_by_asset_id_formats_by_format_id_file_sets_sources_by_storage_method_response_default_type_0 import (
    GetAssetsByAssetIdFormatsByFormatIdFileSetsSourcesByStorageMethodResponseDefaultType0,
)
from ...models.get_assets_by_asset_id_formats_by_format_id_file_sets_sources_by_storage_method_response_default_type_1 import (
    GetAssetsByAssetIdFormatsByFormatIdFileSetsSourcesByStorageMethodResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    asset_id: str,
    format_id: str,
    storage_method: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/assets/{asset_id}/formats/{format_id}/file_sets/sources/{storage_method}/".format(
            asset_id=quote(str(asset_id), safe=""),
            format_id=quote(str(format_id), safe=""),
            storage_method=quote(str(storage_method), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | FileSetsSchema
    | GetAssetsByAssetIdFormatsByFormatIdFileSetsSourcesByStorageMethodResponseDefaultType0
    | GetAssetsByAssetIdFormatsByFormatIdFileSetsSourcesByStorageMethodResponseDefaultType1
):
    if response.status_code == 200:
        response_200 = FileSetsSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    def _parse_response_default(
        data: object,
    ) -> (
        GetAssetsByAssetIdFormatsByFormatIdFileSetsSourcesByStorageMethodResponseDefaultType0
        | GetAssetsByAssetIdFormatsByFormatIdFileSetsSourcesByStorageMethodResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = GetAssetsByAssetIdFormatsByFormatIdFileSetsSourcesByStorageMethodResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = GetAssetsByAssetIdFormatsByFormatIdFileSetsSourcesByStorageMethodResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | FileSetsSchema
    | GetAssetsByAssetIdFormatsByFormatIdFileSetsSourcesByStorageMethodResponseDefaultType0
    | GetAssetsByAssetIdFormatsByFormatIdFileSetsSourcesByStorageMethodResponseDefaultType1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    asset_id: str,
    format_id: str,
    storage_method: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | FileSetsSchema
    | GetAssetsByAssetIdFormatsByFormatIdFileSetsSourcesByStorageMethodResponseDefaultType0
    | GetAssetsByAssetIdFormatsByFormatIdFileSetsSourcesByStorageMethodResponseDefaultType1
]:
    """Get all file sets with matching format and storage method


    Required roles:
     - can_read_files

    Args:
        asset_id (str):
        format_id (str):
        storage_method (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FileSetsSchema | GetAssetsByAssetIdFormatsByFormatIdFileSetsSourcesByStorageMethodResponseDefaultType0 | GetAssetsByAssetIdFormatsByFormatIdFileSetsSourcesByStorageMethodResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        format_id=format_id,
        storage_method=storage_method,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: str,
    format_id: str,
    storage_method: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | FileSetsSchema
    | GetAssetsByAssetIdFormatsByFormatIdFileSetsSourcesByStorageMethodResponseDefaultType0
    | GetAssetsByAssetIdFormatsByFormatIdFileSetsSourcesByStorageMethodResponseDefaultType1
    | None
):
    """Get all file sets with matching format and storage method


    Required roles:
     - can_read_files

    Args:
        asset_id (str):
        format_id (str):
        storage_method (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FileSetsSchema | GetAssetsByAssetIdFormatsByFormatIdFileSetsSourcesByStorageMethodResponseDefaultType0 | GetAssetsByAssetIdFormatsByFormatIdFileSetsSourcesByStorageMethodResponseDefaultType1
    """

    return sync_detailed(
        asset_id=asset_id,
        format_id=format_id,
        storage_method=storage_method,
        client=client,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    format_id: str,
    storage_method: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | FileSetsSchema
    | GetAssetsByAssetIdFormatsByFormatIdFileSetsSourcesByStorageMethodResponseDefaultType0
    | GetAssetsByAssetIdFormatsByFormatIdFileSetsSourcesByStorageMethodResponseDefaultType1
]:
    """Get all file sets with matching format and storage method


    Required roles:
     - can_read_files

    Args:
        asset_id (str):
        format_id (str):
        storage_method (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FileSetsSchema | GetAssetsByAssetIdFormatsByFormatIdFileSetsSourcesByStorageMethodResponseDefaultType0 | GetAssetsByAssetIdFormatsByFormatIdFileSetsSourcesByStorageMethodResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        format_id=format_id,
        storage_method=storage_method,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    format_id: str,
    storage_method: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | FileSetsSchema
    | GetAssetsByAssetIdFormatsByFormatIdFileSetsSourcesByStorageMethodResponseDefaultType0
    | GetAssetsByAssetIdFormatsByFormatIdFileSetsSourcesByStorageMethodResponseDefaultType1
    | None
):
    """Get all file sets with matching format and storage method


    Required roles:
     - can_read_files

    Args:
        asset_id (str):
        format_id (str):
        storage_method (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FileSetsSchema | GetAssetsByAssetIdFormatsByFormatIdFileSetsSourcesByStorageMethodResponseDefaultType0 | GetAssetsByAssetIdFormatsByFormatIdFileSetsSourcesByStorageMethodResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            format_id=format_id,
            storage_method=storage_method,
            client=client,
        )
    ).parsed
