from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_assets_by_asset_id_proxies_by_proxy_id_keyframes_response_default import (
    PostAssetsByAssetIdProxiesByProxyIdKeyframesResponseDefault,
)
from ...models.transcode_request_schema import TranscodeRequestSchema
from ...models.transcode_response_schema import TranscodeResponseSchema
from ...types import Response


def _get_kwargs(
    asset_id: str,
    proxy_id: str,
    *,
    body: TranscodeRequestSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/assets/{asset_id}/proxies/{proxy_id}/keyframes/".format(
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
) -> (
    Any
    | PostAssetsByAssetIdProxiesByProxyIdKeyframesResponseDefault
    | TranscodeResponseSchema
):
    if response.status_code == 200:
        response_200 = TranscodeResponseSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = (
        PostAssetsByAssetIdProxiesByProxyIdKeyframesResponseDefault.from_dict(
            response.json()
        )
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostAssetsByAssetIdProxiesByProxyIdKeyframesResponseDefault
    | TranscodeResponseSchema
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
    body: TranscodeRequestSchema,
) -> Response[
    Any
    | PostAssetsByAssetIdProxiesByProxyIdKeyframesResponseDefault
    | TranscodeResponseSchema
]:
    """Create a transcode job for keyframes from a proxy


    Required roles:
     - can_create_transcode_jobs

    Args:
        asset_id (str):
        proxy_id (str):
        body (TranscodeRequestSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostAssetsByAssetIdProxiesByProxyIdKeyframesResponseDefault | TranscodeResponseSchema]
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
    body: TranscodeRequestSchema,
) -> (
    Any
    | PostAssetsByAssetIdProxiesByProxyIdKeyframesResponseDefault
    | TranscodeResponseSchema
    | None
):
    """Create a transcode job for keyframes from a proxy


    Required roles:
     - can_create_transcode_jobs

    Args:
        asset_id (str):
        proxy_id (str):
        body (TranscodeRequestSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostAssetsByAssetIdProxiesByProxyIdKeyframesResponseDefault | TranscodeResponseSchema
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
    body: TranscodeRequestSchema,
) -> Response[
    Any
    | PostAssetsByAssetIdProxiesByProxyIdKeyframesResponseDefault
    | TranscodeResponseSchema
]:
    """Create a transcode job for keyframes from a proxy


    Required roles:
     - can_create_transcode_jobs

    Args:
        asset_id (str):
        proxy_id (str):
        body (TranscodeRequestSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostAssetsByAssetIdProxiesByProxyIdKeyframesResponseDefault | TranscodeResponseSchema]
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
    body: TranscodeRequestSchema,
) -> (
    Any
    | PostAssetsByAssetIdProxiesByProxyIdKeyframesResponseDefault
    | TranscodeResponseSchema
    | None
):
    """Create a transcode job for keyframes from a proxy


    Required roles:
     - can_create_transcode_jobs

    Args:
        asset_id (str):
        proxy_id (str):
        body (TranscodeRequestSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostAssetsByAssetIdProxiesByProxyIdKeyframesResponseDefault | TranscodeResponseSchema
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            proxy_id=proxy_id,
            client=client,
            body=body,
        )
    ).parsed
