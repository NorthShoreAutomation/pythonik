from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.multipart_b2_start_upload import MultipartB2StartUpload
from ...models.post_assets_by_asset_id_files_by_file_id_multipart_b2_start_response_default import (
    PostAssetsByAssetIdFilesByFileIdMultipartB2StartResponseDefault,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    asset_id: str,
    file_id: str,
    *,
    body: MultipartB2StartUpload | Unset = UNSET,
    temporary: bool | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["temporary"] = temporary

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/assets/{asset_id}/files/{file_id}/multipart/b2/start/".format(
            asset_id=quote(str(asset_id), safe=""),
            file_id=quote(str(file_id), safe=""),
        ),
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | MultipartB2StartUpload
    | PostAssetsByAssetIdFilesByFileIdMultipartB2StartResponseDefault
):
    if response.status_code == 200:
        response_200 = MultipartB2StartUpload.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = (
        PostAssetsByAssetIdFilesByFileIdMultipartB2StartResponseDefault.from_dict(
            response.json()
        )
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | MultipartB2StartUpload
    | PostAssetsByAssetIdFilesByFileIdMultipartB2StartResponseDefault
]:
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
    body: MultipartB2StartUpload | Unset = UNSET,
    temporary: bool | Unset = UNSET,
) -> Response[
    Any
    | MultipartB2StartUpload
    | PostAssetsByAssetIdFilesByFileIdMultipartB2StartResponseDefault
]:
    """Start Backblaze B2 multipart upload.


    Required roles:
     - can_write_files

    Args:
        asset_id (str):
        file_id (str):
        temporary (bool | Unset):
        body (MultipartB2StartUpload | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | MultipartB2StartUpload | PostAssetsByAssetIdFilesByFileIdMultipartB2StartResponseDefault]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        file_id=file_id,
        body=body,
        temporary=temporary,
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
    body: MultipartB2StartUpload | Unset = UNSET,
    temporary: bool | Unset = UNSET,
) -> (
    Any
    | MultipartB2StartUpload
    | PostAssetsByAssetIdFilesByFileIdMultipartB2StartResponseDefault
    | None
):
    """Start Backblaze B2 multipart upload.


    Required roles:
     - can_write_files

    Args:
        asset_id (str):
        file_id (str):
        temporary (bool | Unset):
        body (MultipartB2StartUpload | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | MultipartB2StartUpload | PostAssetsByAssetIdFilesByFileIdMultipartB2StartResponseDefault
    """

    return sync_detailed(
        asset_id=asset_id,
        file_id=file_id,
        client=client,
        body=body,
        temporary=temporary,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    file_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: MultipartB2StartUpload | Unset = UNSET,
    temporary: bool | Unset = UNSET,
) -> Response[
    Any
    | MultipartB2StartUpload
    | PostAssetsByAssetIdFilesByFileIdMultipartB2StartResponseDefault
]:
    """Start Backblaze B2 multipart upload.


    Required roles:
     - can_write_files

    Args:
        asset_id (str):
        file_id (str):
        temporary (bool | Unset):
        body (MultipartB2StartUpload | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | MultipartB2StartUpload | PostAssetsByAssetIdFilesByFileIdMultipartB2StartResponseDefault]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        file_id=file_id,
        body=body,
        temporary=temporary,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    file_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: MultipartB2StartUpload | Unset = UNSET,
    temporary: bool | Unset = UNSET,
) -> (
    Any
    | MultipartB2StartUpload
    | PostAssetsByAssetIdFilesByFileIdMultipartB2StartResponseDefault
    | None
):
    """Start Backblaze B2 multipart upload.


    Required roles:
     - can_write_files

    Args:
        asset_id (str):
        file_id (str):
        temporary (bool | Unset):
        body (MultipartB2StartUpload | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | MultipartB2StartUpload | PostAssetsByAssetIdFilesByFileIdMultipartB2StartResponseDefault
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            file_id=file_id,
            client=client,
            body=body,
            temporary=temporary,
        )
    ).parsed
