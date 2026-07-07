from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_assets_by_asset_id_proxies_by_proxy_id_response_default_type_0 import (
    GetAssetsByAssetIdProxiesByProxyIdResponseDefaultType0,
)
from ...models.get_assets_by_asset_id_proxies_by_proxy_id_response_default_type_1 import (
    GetAssetsByAssetIdProxiesByProxyIdResponseDefaultType1,
)
from ...models.proxy_schema import ProxySchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    asset_id: str,
    proxy_id: str,
    *,
    content_disposition: str | Unset = "inline",
    content_type: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["content_disposition"] = content_disposition

    params["content_type"] = content_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/assets/{asset_id}/proxies/{proxy_id}/".format(
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
    | GetAssetsByAssetIdProxiesByProxyIdResponseDefaultType0
    | GetAssetsByAssetIdProxiesByProxyIdResponseDefaultType1
    | ProxySchema
):
    if response.status_code == 200:
        response_200 = ProxySchema.from_dict(response.json())

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

    def _parse_response_default(
        data: object,
    ) -> (
        GetAssetsByAssetIdProxiesByProxyIdResponseDefaultType0
        | GetAssetsByAssetIdProxiesByProxyIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetAssetsByAssetIdProxiesByProxyIdResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            GetAssetsByAssetIdProxiesByProxyIdResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetAssetsByAssetIdProxiesByProxyIdResponseDefaultType0
    | GetAssetsByAssetIdProxiesByProxyIdResponseDefaultType1
    | ProxySchema
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
    content_disposition: str | Unset = "inline",
    content_type: str | Unset = UNSET,
) -> Response[
    Any
    | GetAssetsByAssetIdProxiesByProxyIdResponseDefaultType0
    | GetAssetsByAssetIdProxiesByProxyIdResponseDefaultType1
    | ProxySchema
]:
    """Get asset's proxy


    Required roles:
     - can_read_proxies

    Args:
        asset_id (str):
        proxy_id (str):
        content_disposition (str | Unset):  Default: 'inline'.
        content_type (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAssetsByAssetIdProxiesByProxyIdResponseDefaultType0 | GetAssetsByAssetIdProxiesByProxyIdResponseDefaultType1 | ProxySchema]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        proxy_id=proxy_id,
        content_disposition=content_disposition,
        content_type=content_type,
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
    content_disposition: str | Unset = "inline",
    content_type: str | Unset = UNSET,
) -> (
    Any
    | GetAssetsByAssetIdProxiesByProxyIdResponseDefaultType0
    | GetAssetsByAssetIdProxiesByProxyIdResponseDefaultType1
    | ProxySchema
    | None
):
    """Get asset's proxy


    Required roles:
     - can_read_proxies

    Args:
        asset_id (str):
        proxy_id (str):
        content_disposition (str | Unset):  Default: 'inline'.
        content_type (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAssetsByAssetIdProxiesByProxyIdResponseDefaultType0 | GetAssetsByAssetIdProxiesByProxyIdResponseDefaultType1 | ProxySchema
    """

    return sync_detailed(
        asset_id=asset_id,
        proxy_id=proxy_id,
        client=client,
        content_disposition=content_disposition,
        content_type=content_type,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    proxy_id: str,
    *,
    client: AuthenticatedClient | Client,
    content_disposition: str | Unset = "inline",
    content_type: str | Unset = UNSET,
) -> Response[
    Any
    | GetAssetsByAssetIdProxiesByProxyIdResponseDefaultType0
    | GetAssetsByAssetIdProxiesByProxyIdResponseDefaultType1
    | ProxySchema
]:
    """Get asset's proxy


    Required roles:
     - can_read_proxies

    Args:
        asset_id (str):
        proxy_id (str):
        content_disposition (str | Unset):  Default: 'inline'.
        content_type (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAssetsByAssetIdProxiesByProxyIdResponseDefaultType0 | GetAssetsByAssetIdProxiesByProxyIdResponseDefaultType1 | ProxySchema]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        proxy_id=proxy_id,
        content_disposition=content_disposition,
        content_type=content_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    proxy_id: str,
    *,
    client: AuthenticatedClient | Client,
    content_disposition: str | Unset = "inline",
    content_type: str | Unset = UNSET,
) -> (
    Any
    | GetAssetsByAssetIdProxiesByProxyIdResponseDefaultType0
    | GetAssetsByAssetIdProxiesByProxyIdResponseDefaultType1
    | ProxySchema
    | None
):
    """Get asset's proxy


    Required roles:
     - can_read_proxies

    Args:
        asset_id (str):
        proxy_id (str):
        content_disposition (str | Unset):  Default: 'inline'.
        content_type (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAssetsByAssetIdProxiesByProxyIdResponseDefaultType0 | GetAssetsByAssetIdProxiesByProxyIdResponseDefaultType1 | ProxySchema
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            proxy_id=proxy_id,
            client=client,
            content_disposition=content_disposition,
            content_type=content_type,
        )
    ).parsed
