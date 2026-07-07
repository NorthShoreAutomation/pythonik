from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.multi_part_upload_compose_url_schema import (
    MultiPartUploadComposeURLSchema,
)
from ...models.multipart_upload_compose_schema import MultipartUploadComposeSchema
from ...models.post_assets_by_asset_id_files_by_file_id_multipart_gcs_compose_url_response_default_type_0 import (
    PostAssetsByAssetIdFilesByFileIdMultipartGcsComposeUrlResponseDefaultType0,
)
from ...models.post_assets_by_asset_id_files_by_file_id_multipart_gcs_compose_url_response_default_type_1 import (
    PostAssetsByAssetIdFilesByFileIdMultipartGcsComposeUrlResponseDefaultType1,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    asset_id: str,
    file_id: str,
    *,
    body: MultipartUploadComposeSchema,
    temporary: bool | Unset = False,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["temporary"] = temporary

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/assets/{asset_id}/files/{file_id}/multipart/gcs/compose_url/".format(
            asset_id=quote(str(asset_id), safe=""),
            file_id=quote(str(file_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | MultiPartUploadComposeURLSchema
    | PostAssetsByAssetIdFilesByFileIdMultipartGcsComposeUrlResponseDefaultType0
    | PostAssetsByAssetIdFilesByFileIdMultipartGcsComposeUrlResponseDefaultType1
):
    if response.status_code == 200:
        response_200 = MultiPartUploadComposeURLSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    def _parse_response_default(
        data: object,
    ) -> (
        PostAssetsByAssetIdFilesByFileIdMultipartGcsComposeUrlResponseDefaultType0
        | PostAssetsByAssetIdFilesByFileIdMultipartGcsComposeUrlResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = PostAssetsByAssetIdFilesByFileIdMultipartGcsComposeUrlResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = PostAssetsByAssetIdFilesByFileIdMultipartGcsComposeUrlResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | MultiPartUploadComposeURLSchema
    | PostAssetsByAssetIdFilesByFileIdMultipartGcsComposeUrlResponseDefaultType0
    | PostAssetsByAssetIdFilesByFileIdMultipartGcsComposeUrlResponseDefaultType1
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
    body: MultipartUploadComposeSchema,
    temporary: bool | Unset = False,
) -> Response[
    Any
    | MultiPartUploadComposeURLSchema
    | PostAssetsByAssetIdFilesByFileIdMultipartGcsComposeUrlResponseDefaultType0
    | PostAssetsByAssetIdFilesByFileIdMultipartGcsComposeUrlResponseDefaultType1
]:
    """Get object compose url for GCS parallel upload.


    Required roles:
     - can_write_files

    Args:
        asset_id (str):
        file_id (str):
        temporary (bool | Unset):  Default: False.
        body (MultipartUploadComposeSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | MultiPartUploadComposeURLSchema | PostAssetsByAssetIdFilesByFileIdMultipartGcsComposeUrlResponseDefaultType0 | PostAssetsByAssetIdFilesByFileIdMultipartGcsComposeUrlResponseDefaultType1]
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
    body: MultipartUploadComposeSchema,
    temporary: bool | Unset = False,
) -> (
    Any
    | MultiPartUploadComposeURLSchema
    | PostAssetsByAssetIdFilesByFileIdMultipartGcsComposeUrlResponseDefaultType0
    | PostAssetsByAssetIdFilesByFileIdMultipartGcsComposeUrlResponseDefaultType1
    | None
):
    """Get object compose url for GCS parallel upload.


    Required roles:
     - can_write_files

    Args:
        asset_id (str):
        file_id (str):
        temporary (bool | Unset):  Default: False.
        body (MultipartUploadComposeSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | MultiPartUploadComposeURLSchema | PostAssetsByAssetIdFilesByFileIdMultipartGcsComposeUrlResponseDefaultType0 | PostAssetsByAssetIdFilesByFileIdMultipartGcsComposeUrlResponseDefaultType1
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
    body: MultipartUploadComposeSchema,
    temporary: bool | Unset = False,
) -> Response[
    Any
    | MultiPartUploadComposeURLSchema
    | PostAssetsByAssetIdFilesByFileIdMultipartGcsComposeUrlResponseDefaultType0
    | PostAssetsByAssetIdFilesByFileIdMultipartGcsComposeUrlResponseDefaultType1
]:
    """Get object compose url for GCS parallel upload.


    Required roles:
     - can_write_files

    Args:
        asset_id (str):
        file_id (str):
        temporary (bool | Unset):  Default: False.
        body (MultipartUploadComposeSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | MultiPartUploadComposeURLSchema | PostAssetsByAssetIdFilesByFileIdMultipartGcsComposeUrlResponseDefaultType0 | PostAssetsByAssetIdFilesByFileIdMultipartGcsComposeUrlResponseDefaultType1]
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
    body: MultipartUploadComposeSchema,
    temporary: bool | Unset = False,
) -> (
    Any
    | MultiPartUploadComposeURLSchema
    | PostAssetsByAssetIdFilesByFileIdMultipartGcsComposeUrlResponseDefaultType0
    | PostAssetsByAssetIdFilesByFileIdMultipartGcsComposeUrlResponseDefaultType1
    | None
):
    """Get object compose url for GCS parallel upload.


    Required roles:
     - can_write_files

    Args:
        asset_id (str):
        file_id (str):
        temporary (bool | Unset):  Default: False.
        body (MultipartUploadComposeSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | MultiPartUploadComposeURLSchema | PostAssetsByAssetIdFilesByFileIdMultipartGcsComposeUrlResponseDefaultType0 | PostAssetsByAssetIdFilesByFileIdMultipartGcsComposeUrlResponseDefaultType1
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
