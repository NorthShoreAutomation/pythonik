from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_assets_by_asset_id_proxies_response_default_type_0 import (
    PostAssetsByAssetIdProxiesResponseDefaultType0,
)
from ...models.post_assets_by_asset_id_proxies_response_default_type_1 import (
    PostAssetsByAssetIdProxiesResponseDefaultType1,
)
from ...models.proxy_create_schema import ProxyCreateSchema
from ...types import Response


def _get_kwargs(
    asset_id: str,
    *,
    body: ProxyCreateSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/assets/{asset_id}/proxies/".format(
            asset_id=quote(str(asset_id), safe=""),
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
    | PostAssetsByAssetIdProxiesResponseDefaultType0
    | PostAssetsByAssetIdProxiesResponseDefaultType1
    | ProxyCreateSchema
):
    if response.status_code == 201:
        response_201 = ProxyCreateSchema.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    def _parse_response_default(
        data: object,
    ) -> (
        PostAssetsByAssetIdProxiesResponseDefaultType0
        | PostAssetsByAssetIdProxiesResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                PostAssetsByAssetIdProxiesResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PostAssetsByAssetIdProxiesResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostAssetsByAssetIdProxiesResponseDefaultType0
    | PostAssetsByAssetIdProxiesResponseDefaultType1
    | ProxyCreateSchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ProxyCreateSchema,
) -> Response[
    Any
    | PostAssetsByAssetIdProxiesResponseDefaultType0
    | PostAssetsByAssetIdProxiesResponseDefaultType1
    | ProxyCreateSchema
]:
    """Create proxy and associate to asset


    Required roles:
     - can_write_proxies

    Args:
        asset_id (str):
        body (ProxyCreateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostAssetsByAssetIdProxiesResponseDefaultType0 | PostAssetsByAssetIdProxiesResponseDefaultType1 | ProxyCreateSchema]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ProxyCreateSchema,
) -> (
    Any
    | PostAssetsByAssetIdProxiesResponseDefaultType0
    | PostAssetsByAssetIdProxiesResponseDefaultType1
    | ProxyCreateSchema
    | None
):
    """Create proxy and associate to asset


    Required roles:
     - can_write_proxies

    Args:
        asset_id (str):
        body (ProxyCreateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostAssetsByAssetIdProxiesResponseDefaultType0 | PostAssetsByAssetIdProxiesResponseDefaultType1 | ProxyCreateSchema
    """

    return sync_detailed(
        asset_id=asset_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ProxyCreateSchema,
) -> Response[
    Any
    | PostAssetsByAssetIdProxiesResponseDefaultType0
    | PostAssetsByAssetIdProxiesResponseDefaultType1
    | ProxyCreateSchema
]:
    """Create proxy and associate to asset


    Required roles:
     - can_write_proxies

    Args:
        asset_id (str):
        body (ProxyCreateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostAssetsByAssetIdProxiesResponseDefaultType0 | PostAssetsByAssetIdProxiesResponseDefaultType1 | ProxyCreateSchema]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ProxyCreateSchema,
) -> (
    Any
    | PostAssetsByAssetIdProxiesResponseDefaultType0
    | PostAssetsByAssetIdProxiesResponseDefaultType1
    | ProxyCreateSchema
    | None
):
    """Create proxy and associate to asset


    Required roles:
     - can_write_proxies

    Args:
        asset_id (str):
        body (ProxyCreateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostAssetsByAssetIdProxiesResponseDefaultType0 | PostAssetsByAssetIdProxiesResponseDefaultType1 | ProxyCreateSchema
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            client=client,
            body=body,
        )
    ).parsed
