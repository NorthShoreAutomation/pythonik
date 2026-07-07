from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_assets_by_asset_id_files_by_file_id_multipart_url_part_response_default_type_0 import (
    GetAssetsByAssetIdFilesByFileIdMultipartUrlPartResponseDefaultType0,
)
from ...models.get_assets_by_asset_id_files_by_file_id_multipart_url_part_response_default_type_1 import (
    GetAssetsByAssetIdFilesByFileIdMultipartUrlPartResponseDefaultType1,
)
from ...models.multi_part_upload_ur_ls_schema import MultiPartUploadURLsSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    asset_id: str,
    file_id: str,
    *,
    upload_id: str | Unset = UNSET,
    parts_num: int,
    per_page: int | Unset = 10,
    page: int | Unset = 1,
    temporary: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["upload_id"] = upload_id

    params["parts_num"] = parts_num

    params["per_page"] = per_page

    params["page"] = page

    params["temporary"] = temporary

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/assets/{asset_id}/files/{file_id}/multipart_url/part/".format(
            asset_id=quote(str(asset_id), safe=""),
            file_id=quote(str(file_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetAssetsByAssetIdFilesByFileIdMultipartUrlPartResponseDefaultType0
    | GetAssetsByAssetIdFilesByFileIdMultipartUrlPartResponseDefaultType1
    | MultiPartUploadURLsSchema
):
    if response.status_code == 200:
        response_200 = MultiPartUploadURLsSchema.from_dict(response.json())

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
        GetAssetsByAssetIdFilesByFileIdMultipartUrlPartResponseDefaultType0
        | GetAssetsByAssetIdFilesByFileIdMultipartUrlPartResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = GetAssetsByAssetIdFilesByFileIdMultipartUrlPartResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = GetAssetsByAssetIdFilesByFileIdMultipartUrlPartResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetAssetsByAssetIdFilesByFileIdMultipartUrlPartResponseDefaultType0
    | GetAssetsByAssetIdFilesByFileIdMultipartUrlPartResponseDefaultType1
    | MultiPartUploadURLsSchema
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
    upload_id: str | Unset = UNSET,
    parts_num: int,
    per_page: int | Unset = 10,
    page: int | Unset = 1,
    temporary: bool | Unset = False,
) -> Response[
    Any
    | GetAssetsByAssetIdFilesByFileIdMultipartUrlPartResponseDefaultType0
    | GetAssetsByAssetIdFilesByFileIdMultipartUrlPartResponseDefaultType1
    | MultiPartUploadURLsSchema
]:
    """Get presigned urls for multipart part upload (S3 & GCS).


    Required roles:
     - can_write_files

    Args:
        asset_id (str):
        file_id (str):
        upload_id (str | Unset):
        parts_num (int):
        per_page (int | Unset):  Default: 10.
        page (int | Unset):  Default: 1.
        temporary (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAssetsByAssetIdFilesByFileIdMultipartUrlPartResponseDefaultType0 | GetAssetsByAssetIdFilesByFileIdMultipartUrlPartResponseDefaultType1 | MultiPartUploadURLsSchema]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        file_id=file_id,
        upload_id=upload_id,
        parts_num=parts_num,
        per_page=per_page,
        page=page,
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
    upload_id: str | Unset = UNSET,
    parts_num: int,
    per_page: int | Unset = 10,
    page: int | Unset = 1,
    temporary: bool | Unset = False,
) -> (
    Any
    | GetAssetsByAssetIdFilesByFileIdMultipartUrlPartResponseDefaultType0
    | GetAssetsByAssetIdFilesByFileIdMultipartUrlPartResponseDefaultType1
    | MultiPartUploadURLsSchema
    | None
):
    """Get presigned urls for multipart part upload (S3 & GCS).


    Required roles:
     - can_write_files

    Args:
        asset_id (str):
        file_id (str):
        upload_id (str | Unset):
        parts_num (int):
        per_page (int | Unset):  Default: 10.
        page (int | Unset):  Default: 1.
        temporary (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAssetsByAssetIdFilesByFileIdMultipartUrlPartResponseDefaultType0 | GetAssetsByAssetIdFilesByFileIdMultipartUrlPartResponseDefaultType1 | MultiPartUploadURLsSchema
    """

    return sync_detailed(
        asset_id=asset_id,
        file_id=file_id,
        client=client,
        upload_id=upload_id,
        parts_num=parts_num,
        per_page=per_page,
        page=page,
        temporary=temporary,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    file_id: str,
    *,
    client: AuthenticatedClient | Client,
    upload_id: str | Unset = UNSET,
    parts_num: int,
    per_page: int | Unset = 10,
    page: int | Unset = 1,
    temporary: bool | Unset = False,
) -> Response[
    Any
    | GetAssetsByAssetIdFilesByFileIdMultipartUrlPartResponseDefaultType0
    | GetAssetsByAssetIdFilesByFileIdMultipartUrlPartResponseDefaultType1
    | MultiPartUploadURLsSchema
]:
    """Get presigned urls for multipart part upload (S3 & GCS).


    Required roles:
     - can_write_files

    Args:
        asset_id (str):
        file_id (str):
        upload_id (str | Unset):
        parts_num (int):
        per_page (int | Unset):  Default: 10.
        page (int | Unset):  Default: 1.
        temporary (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAssetsByAssetIdFilesByFileIdMultipartUrlPartResponseDefaultType0 | GetAssetsByAssetIdFilesByFileIdMultipartUrlPartResponseDefaultType1 | MultiPartUploadURLsSchema]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        file_id=file_id,
        upload_id=upload_id,
        parts_num=parts_num,
        per_page=per_page,
        page=page,
        temporary=temporary,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    file_id: str,
    *,
    client: AuthenticatedClient | Client,
    upload_id: str | Unset = UNSET,
    parts_num: int,
    per_page: int | Unset = 10,
    page: int | Unset = 1,
    temporary: bool | Unset = False,
) -> (
    Any
    | GetAssetsByAssetIdFilesByFileIdMultipartUrlPartResponseDefaultType0
    | GetAssetsByAssetIdFilesByFileIdMultipartUrlPartResponseDefaultType1
    | MultiPartUploadURLsSchema
    | None
):
    """Get presigned urls for multipart part upload (S3 & GCS).


    Required roles:
     - can_write_files

    Args:
        asset_id (str):
        file_id (str):
        upload_id (str | Unset):
        parts_num (int):
        per_page (int | Unset):  Default: 10.
        page (int | Unset):  Default: 1.
        temporary (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAssetsByAssetIdFilesByFileIdMultipartUrlPartResponseDefaultType0 | GetAssetsByAssetIdFilesByFileIdMultipartUrlPartResponseDefaultType1 | MultiPartUploadURLsSchema
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            file_id=file_id,
            client=client,
            upload_id=upload_id,
            parts_num=parts_num,
            per_page=per_page,
            page=page,
            temporary=temporary,
        )
    ).parsed
