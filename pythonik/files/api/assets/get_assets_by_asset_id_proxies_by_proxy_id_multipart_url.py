from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_assets_by_asset_id_proxies_by_proxy_id_multipart_url_response_default import (
    GetAssetsByAssetIdProxiesByProxyIdMultipartUrlResponseDefault,
)
from ...models.multi_part_ur_ls_schema import MultiPartURLsSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    asset_id: str,
    proxy_id: str,
    *,
    upload_id: str,
    type_: str | Unset = UNSET,
    max_part_number: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["upload_id"] = upload_id

    params["type"] = type_

    params["max_part_number"] = max_part_number

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/assets/{asset_id}/proxies/{proxy_id}/multipart_url/".format(
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
    | GetAssetsByAssetIdProxiesByProxyIdMultipartUrlResponseDefault
    | MultiPartURLsSchema
):
    if response.status_code == 200:
        response_200 = MultiPartURLsSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = (
        GetAssetsByAssetIdProxiesByProxyIdMultipartUrlResponseDefault.from_dict(
            response.json()
        )
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetAssetsByAssetIdProxiesByProxyIdMultipartUrlResponseDefault
    | MultiPartURLsSchema
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
    upload_id: str,
    type_: str | Unset = UNSET,
    max_part_number: int | Unset = UNSET,
) -> Response[
    Any
    | GetAssetsByAssetIdProxiesByProxyIdMultipartUrlResponseDefault
    | MultiPartURLsSchema
]:
    """Get presigned urls for S3 multipart upload.


    Required roles:
     - can_write_proxies

    Args:
        asset_id (str):
        proxy_id (str):
        upload_id (str):
        type_ (str | Unset):
        max_part_number (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAssetsByAssetIdProxiesByProxyIdMultipartUrlResponseDefault | MultiPartURLsSchema]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        proxy_id=proxy_id,
        upload_id=upload_id,
        type_=type_,
        max_part_number=max_part_number,
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
    upload_id: str,
    type_: str | Unset = UNSET,
    max_part_number: int | Unset = UNSET,
) -> (
    Any
    | GetAssetsByAssetIdProxiesByProxyIdMultipartUrlResponseDefault
    | MultiPartURLsSchema
    | None
):
    """Get presigned urls for S3 multipart upload.


    Required roles:
     - can_write_proxies

    Args:
        asset_id (str):
        proxy_id (str):
        upload_id (str):
        type_ (str | Unset):
        max_part_number (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAssetsByAssetIdProxiesByProxyIdMultipartUrlResponseDefault | MultiPartURLsSchema
    """

    return sync_detailed(
        asset_id=asset_id,
        proxy_id=proxy_id,
        client=client,
        upload_id=upload_id,
        type_=type_,
        max_part_number=max_part_number,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    proxy_id: str,
    *,
    client: AuthenticatedClient | Client,
    upload_id: str,
    type_: str | Unset = UNSET,
    max_part_number: int | Unset = UNSET,
) -> Response[
    Any
    | GetAssetsByAssetIdProxiesByProxyIdMultipartUrlResponseDefault
    | MultiPartURLsSchema
]:
    """Get presigned urls for S3 multipart upload.


    Required roles:
     - can_write_proxies

    Args:
        asset_id (str):
        proxy_id (str):
        upload_id (str):
        type_ (str | Unset):
        max_part_number (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAssetsByAssetIdProxiesByProxyIdMultipartUrlResponseDefault | MultiPartURLsSchema]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        proxy_id=proxy_id,
        upload_id=upload_id,
        type_=type_,
        max_part_number=max_part_number,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    proxy_id: str,
    *,
    client: AuthenticatedClient | Client,
    upload_id: str,
    type_: str | Unset = UNSET,
    max_part_number: int | Unset = UNSET,
) -> (
    Any
    | GetAssetsByAssetIdProxiesByProxyIdMultipartUrlResponseDefault
    | MultiPartURLsSchema
    | None
):
    """Get presigned urls for S3 multipart upload.


    Required roles:
     - can_write_proxies

    Args:
        asset_id (str):
        proxy_id (str):
        upload_id (str):
        type_ (str | Unset):
        max_part_number (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAssetsByAssetIdProxiesByProxyIdMultipartUrlResponseDefault | MultiPartURLsSchema
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            proxy_id=proxy_id,
            client=client,
            upload_id=upload_id,
            type_=type_,
            max_part_number=max_part_number,
        )
    ).parsed
