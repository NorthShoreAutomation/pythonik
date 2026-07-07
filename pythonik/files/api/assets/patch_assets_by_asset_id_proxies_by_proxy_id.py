from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.patch_assets_by_asset_id_proxies_by_proxy_id_response_default_type_0 import (
    PatchAssetsByAssetIdProxiesByProxyIdResponseDefaultType0,
)
from ...models.patch_assets_by_asset_id_proxies_by_proxy_id_response_default_type_1 import (
    PatchAssetsByAssetIdProxiesByProxyIdResponseDefaultType1,
)
from ...models.proxy_schema import ProxySchema
from ...models.proxy_update_schema import ProxyUpdateSchema
from ...types import Response


def _get_kwargs(
    asset_id: str,
    proxy_id: str,
    *,
    body: ProxyUpdateSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/assets/{asset_id}/proxies/{proxy_id}/".format(
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
    | PatchAssetsByAssetIdProxiesByProxyIdResponseDefaultType0
    | PatchAssetsByAssetIdProxiesByProxyIdResponseDefaultType1
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
        PatchAssetsByAssetIdProxiesByProxyIdResponseDefaultType0
        | PatchAssetsByAssetIdProxiesByProxyIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                PatchAssetsByAssetIdProxiesByProxyIdResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PatchAssetsByAssetIdProxiesByProxyIdResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PatchAssetsByAssetIdProxiesByProxyIdResponseDefaultType0
    | PatchAssetsByAssetIdProxiesByProxyIdResponseDefaultType1
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
    body: ProxyUpdateSchema,
) -> Response[
    Any
    | PatchAssetsByAssetIdProxiesByProxyIdResponseDefaultType0
    | PatchAssetsByAssetIdProxiesByProxyIdResponseDefaultType1
    | ProxySchema
]:
    """Update proxy information


    Required roles:
     - can_write_proxies

    Args:
        asset_id (str):
        proxy_id (str):
        body (ProxyUpdateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PatchAssetsByAssetIdProxiesByProxyIdResponseDefaultType0 | PatchAssetsByAssetIdProxiesByProxyIdResponseDefaultType1 | ProxySchema]
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
    body: ProxyUpdateSchema,
) -> (
    Any
    | PatchAssetsByAssetIdProxiesByProxyIdResponseDefaultType0
    | PatchAssetsByAssetIdProxiesByProxyIdResponseDefaultType1
    | ProxySchema
    | None
):
    """Update proxy information


    Required roles:
     - can_write_proxies

    Args:
        asset_id (str):
        proxy_id (str):
        body (ProxyUpdateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PatchAssetsByAssetIdProxiesByProxyIdResponseDefaultType0 | PatchAssetsByAssetIdProxiesByProxyIdResponseDefaultType1 | ProxySchema
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
    body: ProxyUpdateSchema,
) -> Response[
    Any
    | PatchAssetsByAssetIdProxiesByProxyIdResponseDefaultType0
    | PatchAssetsByAssetIdProxiesByProxyIdResponseDefaultType1
    | ProxySchema
]:
    """Update proxy information


    Required roles:
     - can_write_proxies

    Args:
        asset_id (str):
        proxy_id (str):
        body (ProxyUpdateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PatchAssetsByAssetIdProxiesByProxyIdResponseDefaultType0 | PatchAssetsByAssetIdProxiesByProxyIdResponseDefaultType1 | ProxySchema]
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
    body: ProxyUpdateSchema,
) -> (
    Any
    | PatchAssetsByAssetIdProxiesByProxyIdResponseDefaultType0
    | PatchAssetsByAssetIdProxiesByProxyIdResponseDefaultType1
    | ProxySchema
    | None
):
    """Update proxy information


    Required roles:
     - can_write_proxies

    Args:
        asset_id (str):
        proxy_id (str):
        body (ProxyUpdateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PatchAssetsByAssetIdProxiesByProxyIdResponseDefaultType0 | PatchAssetsByAssetIdProxiesByProxyIdResponseDefaultType1 | ProxySchema
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            proxy_id=proxy_id,
            client=client,
            body=body,
        )
    ).parsed
