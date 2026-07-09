from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.file_set_sources_schema import FileSetSourcesSchema
from ...models.get_assets_by_asset_id_formats_by_format_id_file_sets_sources_response_default import (
    GetAssetsByAssetIdFormatsByFormatIdFileSetsSourcesResponseDefault,
)
from ...types import Response


def _get_kwargs(
    asset_id: str,
    format_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/assets/{asset_id}/formats/{format_id}/file_sets/sources/".format(
            asset_id=quote(str(asset_id), safe=""),
            format_id=quote(str(format_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | FileSetSourcesSchema
    | GetAssetsByAssetIdFormatsByFormatIdFileSetsSourcesResponseDefault
):
    if response.status_code == 200:
        response_200 = FileSetSourcesSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    response_default = (
        GetAssetsByAssetIdFormatsByFormatIdFileSetsSourcesResponseDefault.from_dict(
            response.json()
        )
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | FileSetSourcesSchema
    | GetAssetsByAssetIdFormatsByFormatIdFileSetsSourcesResponseDefault
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
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | FileSetSourcesSchema
    | GetAssetsByAssetIdFormatsByFormatIdFileSetsSourcesResponseDefault
]:
    """Get all file sets with matching format and storage method


    Required roles:
     - can_read_files

    Args:
        asset_id (str):
        format_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FileSetSourcesSchema | GetAssetsByAssetIdFormatsByFormatIdFileSetsSourcesResponseDefault]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        format_id=format_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: str,
    format_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | FileSetSourcesSchema
    | GetAssetsByAssetIdFormatsByFormatIdFileSetsSourcesResponseDefault
    | None
):
    """Get all file sets with matching format and storage method


    Required roles:
     - can_read_files

    Args:
        asset_id (str):
        format_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FileSetSourcesSchema | GetAssetsByAssetIdFormatsByFormatIdFileSetsSourcesResponseDefault
    """

    return sync_detailed(
        asset_id=asset_id,
        format_id=format_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    format_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | FileSetSourcesSchema
    | GetAssetsByAssetIdFormatsByFormatIdFileSetsSourcesResponseDefault
]:
    """Get all file sets with matching format and storage method


    Required roles:
     - can_read_files

    Args:
        asset_id (str):
        format_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FileSetSourcesSchema | GetAssetsByAssetIdFormatsByFormatIdFileSetsSourcesResponseDefault]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        format_id=format_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    format_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | FileSetSourcesSchema
    | GetAssetsByAssetIdFormatsByFormatIdFileSetsSourcesResponseDefault
    | None
):
    """Get all file sets with matching format and storage method


    Required roles:
     - can_read_files

    Args:
        asset_id (str):
        format_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FileSetSourcesSchema | GetAssetsByAssetIdFormatsByFormatIdFileSetsSourcesResponseDefault
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            format_id=format_id,
            client=client,
        )
    ).parsed
