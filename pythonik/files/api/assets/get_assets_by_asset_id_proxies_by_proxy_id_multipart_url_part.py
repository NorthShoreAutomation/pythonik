from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_assets_by_asset_id_proxies_by_proxy_id_multipart_url_part_response_default import (
    GetAssetsByAssetIdProxiesByProxyIdMultipartUrlPartResponseDefault,
)
from ...models.multi_part_upload_ur_ls_schema import MultiPartUploadURLsSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    asset_id: str,
    proxy_id: str,
    *,
    upload_id: str | Unset = UNSET,
    parts_num: int,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["upload_id"] = upload_id

    params["parts_num"] = parts_num

    params["per_page"] = per_page

    params["page"] = page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/assets/{asset_id}/proxies/{proxy_id}/multipart_url/part/".format(
            asset_id=quote(str(asset_id), safe=""),
            proxy_id=quote(str(proxy_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetAssetsByAssetIdProxiesByProxyIdMultipartUrlPartResponseDefault
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

    response_default = (
        GetAssetsByAssetIdProxiesByProxyIdMultipartUrlPartResponseDefault.from_dict(
            response.json()
        )
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetAssetsByAssetIdProxiesByProxyIdMultipartUrlPartResponseDefault
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
    proxy_id: str,
    *,
    client: AuthenticatedClient | Client,
    upload_id: str | Unset = UNSET,
    parts_num: int,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
) -> Response[
    Any
    | GetAssetsByAssetIdProxiesByProxyIdMultipartUrlPartResponseDefault
    | MultiPartUploadURLsSchema
]:
    """Get presigned urls for S3 multipart part upload.


    Required roles:
     - can_write_proxies

    Args:
        asset_id (str):
        proxy_id (str):
        upload_id (str | Unset):
        parts_num (int):
        per_page (int | Unset):
        page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAssetsByAssetIdProxiesByProxyIdMultipartUrlPartResponseDefault | MultiPartUploadURLsSchema]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        proxy_id=proxy_id,
        upload_id=upload_id,
        parts_num=parts_num,
        per_page=per_page,
        page=page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: str,
    proxy_id: str,
    *,
    client: AuthenticatedClient | Client,
    upload_id: str | Unset = UNSET,
    parts_num: int,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
) -> (
    Any
    | GetAssetsByAssetIdProxiesByProxyIdMultipartUrlPartResponseDefault
    | MultiPartUploadURLsSchema
    | None
):
    """Get presigned urls for S3 multipart part upload.


    Required roles:
     - can_write_proxies

    Args:
        asset_id (str):
        proxy_id (str):
        upload_id (str | Unset):
        parts_num (int):
        per_page (int | Unset):
        page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAssetsByAssetIdProxiesByProxyIdMultipartUrlPartResponseDefault | MultiPartUploadURLsSchema
    """

    return sync_detailed(
        asset_id=asset_id,
        proxy_id=proxy_id,
        client=client,
        upload_id=upload_id,
        parts_num=parts_num,
        per_page=per_page,
        page=page,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    proxy_id: str,
    *,
    client: AuthenticatedClient | Client,
    upload_id: str | Unset = UNSET,
    parts_num: int,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
) -> Response[
    Any
    | GetAssetsByAssetIdProxiesByProxyIdMultipartUrlPartResponseDefault
    | MultiPartUploadURLsSchema
]:
    """Get presigned urls for S3 multipart part upload.


    Required roles:
     - can_write_proxies

    Args:
        asset_id (str):
        proxy_id (str):
        upload_id (str | Unset):
        parts_num (int):
        per_page (int | Unset):
        page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAssetsByAssetIdProxiesByProxyIdMultipartUrlPartResponseDefault | MultiPartUploadURLsSchema]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        proxy_id=proxy_id,
        upload_id=upload_id,
        parts_num=parts_num,
        per_page=per_page,
        page=page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    proxy_id: str,
    *,
    client: AuthenticatedClient | Client,
    upload_id: str | Unset = UNSET,
    parts_num: int,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
) -> (
    Any
    | GetAssetsByAssetIdProxiesByProxyIdMultipartUrlPartResponseDefault
    | MultiPartUploadURLsSchema
    | None
):
    """Get presigned urls for S3 multipart part upload.


    Required roles:
     - can_write_proxies

    Args:
        asset_id (str):
        proxy_id (str):
        upload_id (str | Unset):
        parts_num (int):
        per_page (int | Unset):
        page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAssetsByAssetIdProxiesByProxyIdMultipartUrlPartResponseDefault | MultiPartUploadURLsSchema
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            proxy_id=proxy_id,
            client=client,
            upload_id=upload_id,
            parts_num=parts_num,
            per_page=per_page,
            page=page,
        )
    ).parsed
