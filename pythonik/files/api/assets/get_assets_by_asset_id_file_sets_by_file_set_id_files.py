from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.files_schema import FilesSchema
from ...models.get_assets_by_asset_id_file_sets_by_file_set_id_files_response_default import (
    GetAssetsByAssetIdFileSetsByFileSetIdFilesResponseDefault,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    asset_id: str,
    file_set_id: str,
    *,
    per_page: int | Unset = UNSET,
    last_id: str | Unset = UNSET,
    generate_signed_url: bool | Unset = UNSET,
    file_count: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["per_page"] = per_page

    params["last_id"] = last_id

    params["generate_signed_url"] = generate_signed_url

    params["file_count"] = file_count

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/assets/{asset_id}/file_sets/{file_set_id}/files/".format(
            asset_id=quote(str(asset_id), safe=""),
            file_set_id=quote(str(file_set_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FilesSchema | GetAssetsByAssetIdFileSetsByFileSetIdFilesResponseDefault:
    if response.status_code == 200:
        response_200 = FilesSchema.from_dict(response.json())

        return response_200

    response_default = (
        GetAssetsByAssetIdFileSetsByFileSetIdFilesResponseDefault.from_dict(
            response.json()
        )
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[FilesSchema | GetAssetsByAssetIdFileSetsByFileSetIdFilesResponseDefault]:
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
    per_page: int | Unset = UNSET,
    last_id: str | Unset = UNSET,
    generate_signed_url: bool | Unset = UNSET,
    file_count: bool | Unset = UNSET,
) -> Response[FilesSchema | GetAssetsByAssetIdFileSetsByFileSetIdFilesResponseDefault]:
    """Get files from a file set


    Required roles:
     - can_read_files

    Args:
        asset_id (str):
        file_set_id (str):
        per_page (int | Unset):
        last_id (str | Unset):
        generate_signed_url (bool | Unset):
        file_count (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FilesSchema | GetAssetsByAssetIdFileSetsByFileSetIdFilesResponseDefault]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        file_set_id=file_set_id,
        per_page=per_page,
        last_id=last_id,
        generate_signed_url=generate_signed_url,
        file_count=file_count,
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
    per_page: int | Unset = UNSET,
    last_id: str | Unset = UNSET,
    generate_signed_url: bool | Unset = UNSET,
    file_count: bool | Unset = UNSET,
) -> FilesSchema | GetAssetsByAssetIdFileSetsByFileSetIdFilesResponseDefault | None:
    """Get files from a file set


    Required roles:
     - can_read_files

    Args:
        asset_id (str):
        file_set_id (str):
        per_page (int | Unset):
        last_id (str | Unset):
        generate_signed_url (bool | Unset):
        file_count (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FilesSchema | GetAssetsByAssetIdFileSetsByFileSetIdFilesResponseDefault
    """

    return sync_detailed(
        asset_id=asset_id,
        file_set_id=file_set_id,
        client=client,
        per_page=per_page,
        last_id=last_id,
        generate_signed_url=generate_signed_url,
        file_count=file_count,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    file_set_id: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    last_id: str | Unset = UNSET,
    generate_signed_url: bool | Unset = UNSET,
    file_count: bool | Unset = UNSET,
) -> Response[FilesSchema | GetAssetsByAssetIdFileSetsByFileSetIdFilesResponseDefault]:
    """Get files from a file set


    Required roles:
     - can_read_files

    Args:
        asset_id (str):
        file_set_id (str):
        per_page (int | Unset):
        last_id (str | Unset):
        generate_signed_url (bool | Unset):
        file_count (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FilesSchema | GetAssetsByAssetIdFileSetsByFileSetIdFilesResponseDefault]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        file_set_id=file_set_id,
        per_page=per_page,
        last_id=last_id,
        generate_signed_url=generate_signed_url,
        file_count=file_count,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    file_set_id: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    last_id: str | Unset = UNSET,
    generate_signed_url: bool | Unset = UNSET,
    file_count: bool | Unset = UNSET,
) -> FilesSchema | GetAssetsByAssetIdFileSetsByFileSetIdFilesResponseDefault | None:
    """Get files from a file set


    Required roles:
     - can_read_files

    Args:
        asset_id (str):
        file_set_id (str):
        per_page (int | Unset):
        last_id (str | Unset):
        generate_signed_url (bool | Unset):
        file_count (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FilesSchema | GetAssetsByAssetIdFileSetsByFileSetIdFilesResponseDefault
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            file_set_id=file_set_id,
            client=client,
            per_page=per_page,
            last_id=last_id,
            generate_signed_url=generate_signed_url,
            file_count=file_count,
        )
    ).parsed
