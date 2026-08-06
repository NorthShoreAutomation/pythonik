from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.file_schema import FileSchema
from ...models.get_assets_by_asset_id_files_by_file_id_response_default import (
    GetAssetsByAssetIdFilesByFileIdResponseDefault,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    asset_id: str,
    file_id: str,
    *,
    generate_signed_post_url: bool | Unset = UNSET,
    content_disposition: str | Unset = UNSET,
    content_type: str | Unset = UNSET,
    bypass_url_cache: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["generate_signed_post_url"] = generate_signed_post_url

    params["content_disposition"] = content_disposition

    params["content_type"] = content_type

    params["bypass_url_cache"] = bypass_url_cache

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/assets/{asset_id}/files/{file_id}/".format(
            asset_id=quote(str(asset_id), safe=""),
            file_id=quote(str(file_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | FileSchema | GetAssetsByAssetIdFilesByFileIdResponseDefault:
    if response.status_code == 200:
        response_200 = FileSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = GetAssetsByAssetIdFilesByFileIdResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | FileSchema | GetAssetsByAssetIdFilesByFileIdResponseDefault]:
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
    generate_signed_post_url: bool | Unset = UNSET,
    content_disposition: str | Unset = UNSET,
    content_type: str | Unset = UNSET,
    bypass_url_cache: bool | Unset = UNSET,
) -> Response[Any | FileSchema | GetAssetsByAssetIdFilesByFileIdResponseDefault]:
    """Get asset's file


    Required roles:
     - can_read_files

    Args:
        asset_id (str):
        file_id (str):
        generate_signed_post_url (bool | Unset):
        content_disposition (str | Unset):
        content_type (str | Unset):
        bypass_url_cache (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FileSchema | GetAssetsByAssetIdFilesByFileIdResponseDefault]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        file_id=file_id,
        generate_signed_post_url=generate_signed_post_url,
        content_disposition=content_disposition,
        content_type=content_type,
        bypass_url_cache=bypass_url_cache,
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
    generate_signed_post_url: bool | Unset = UNSET,
    content_disposition: str | Unset = UNSET,
    content_type: str | Unset = UNSET,
    bypass_url_cache: bool | Unset = UNSET,
) -> Any | FileSchema | GetAssetsByAssetIdFilesByFileIdResponseDefault | None:
    """Get asset's file


    Required roles:
     - can_read_files

    Args:
        asset_id (str):
        file_id (str):
        generate_signed_post_url (bool | Unset):
        content_disposition (str | Unset):
        content_type (str | Unset):
        bypass_url_cache (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FileSchema | GetAssetsByAssetIdFilesByFileIdResponseDefault
    """

    return sync_detailed(
        asset_id=asset_id,
        file_id=file_id,
        client=client,
        generate_signed_post_url=generate_signed_post_url,
        content_disposition=content_disposition,
        content_type=content_type,
        bypass_url_cache=bypass_url_cache,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    file_id: str,
    *,
    client: AuthenticatedClient | Client,
    generate_signed_post_url: bool | Unset = UNSET,
    content_disposition: str | Unset = UNSET,
    content_type: str | Unset = UNSET,
    bypass_url_cache: bool | Unset = UNSET,
) -> Response[Any | FileSchema | GetAssetsByAssetIdFilesByFileIdResponseDefault]:
    """Get asset's file


    Required roles:
     - can_read_files

    Args:
        asset_id (str):
        file_id (str):
        generate_signed_post_url (bool | Unset):
        content_disposition (str | Unset):
        content_type (str | Unset):
        bypass_url_cache (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FileSchema | GetAssetsByAssetIdFilesByFileIdResponseDefault]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        file_id=file_id,
        generate_signed_post_url=generate_signed_post_url,
        content_disposition=content_disposition,
        content_type=content_type,
        bypass_url_cache=bypass_url_cache,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    file_id: str,
    *,
    client: AuthenticatedClient | Client,
    generate_signed_post_url: bool | Unset = UNSET,
    content_disposition: str | Unset = UNSET,
    content_type: str | Unset = UNSET,
    bypass_url_cache: bool | Unset = UNSET,
) -> Any | FileSchema | GetAssetsByAssetIdFilesByFileIdResponseDefault | None:
    """Get asset's file


    Required roles:
     - can_read_files

    Args:
        asset_id (str):
        file_id (str):
        generate_signed_post_url (bool | Unset):
        content_disposition (str | Unset):
        content_type (str | Unset):
        bypass_url_cache (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FileSchema | GetAssetsByAssetIdFilesByFileIdResponseDefault
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            file_id=file_id,
            client=client,
            generate_signed_post_url=generate_signed_post_url,
            content_disposition=content_disposition,
            content_type=content_type,
            bypass_url_cache=bypass_url_cache,
        )
    ).parsed
