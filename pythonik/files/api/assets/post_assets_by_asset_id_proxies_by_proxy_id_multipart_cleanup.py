from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.multipart_upload_proxy_cleanup_schema import (
    MultipartUploadProxyCleanupSchema,
)
from ...models.post_assets_by_asset_id_proxies_by_proxy_id_multipart_cleanup_response_default import (
    PostAssetsByAssetIdProxiesByProxyIdMultipartCleanupResponseDefault,
)
from ...types import Response


def _get_kwargs(
    asset_id: str,
    proxy_id: str,
    *,
    body: MultipartUploadProxyCleanupSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/assets/{asset_id}/proxies/{proxy_id}/multipart/cleanup/".format(
            asset_id=quote(str(asset_id), safe=""),
            proxy_id=quote(str(proxy_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostAssetsByAssetIdProxiesByProxyIdMultipartCleanupResponseDefault:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = (
        PostAssetsByAssetIdProxiesByProxyIdMultipartCleanupResponseDefault.from_dict(
            response.json()
        )
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PostAssetsByAssetIdProxiesByProxyIdMultipartCleanupResponseDefault]:
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
    body: MultipartUploadProxyCleanupSchema,
) -> Response[Any | PostAssetsByAssetIdProxiesByProxyIdMultipartCleanupResponseDefault]:
    """Cleanup S3 multipart upload


    Required roles:
     - can_write_proxies

    Args:
        asset_id (str):
        proxy_id (str):
        body (MultipartUploadProxyCleanupSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostAssetsByAssetIdProxiesByProxyIdMultipartCleanupResponseDefault]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        proxy_id=proxy_id,
        body=body,
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
    body: MultipartUploadProxyCleanupSchema,
) -> Any | PostAssetsByAssetIdProxiesByProxyIdMultipartCleanupResponseDefault | None:
    """Cleanup S3 multipart upload


    Required roles:
     - can_write_proxies

    Args:
        asset_id (str):
        proxy_id (str):
        body (MultipartUploadProxyCleanupSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostAssetsByAssetIdProxiesByProxyIdMultipartCleanupResponseDefault
    """

    return sync_detailed(
        asset_id=asset_id,
        proxy_id=proxy_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    proxy_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: MultipartUploadProxyCleanupSchema,
) -> Response[Any | PostAssetsByAssetIdProxiesByProxyIdMultipartCleanupResponseDefault]:
    """Cleanup S3 multipart upload


    Required roles:
     - can_write_proxies

    Args:
        asset_id (str):
        proxy_id (str):
        body (MultipartUploadProxyCleanupSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostAssetsByAssetIdProxiesByProxyIdMultipartCleanupResponseDefault]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        proxy_id=proxy_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    proxy_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: MultipartUploadProxyCleanupSchema,
) -> Any | PostAssetsByAssetIdProxiesByProxyIdMultipartCleanupResponseDefault | None:
    """Cleanup S3 multipart upload


    Required roles:
     - can_write_proxies

    Args:
        asset_id (str):
        proxy_id (str):
        body (MultipartUploadProxyCleanupSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostAssetsByAssetIdProxiesByProxyIdMultipartCleanupResponseDefault
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            proxy_id=proxy_id,
            client=client,
            body=body,
        )
    ).parsed
