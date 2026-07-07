from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.asset_post_schema import AssetPostSchema
from ...models.asset_schema import AssetSchema
from ...models.post_assets_by_asset_id_views_response_default_type_0 import (
    PostAssetsByAssetIdViewsResponseDefaultType0,
)
from ...models.post_assets_by_asset_id_views_response_default_type_1 import (
    PostAssetsByAssetIdViewsResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    asset_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/assets/{asset_id}/views/".format(
            asset_id=quote(str(asset_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | AssetPostSchema
    | AssetSchema
    | PostAssetsByAssetIdViewsResponseDefaultType0
    | PostAssetsByAssetIdViewsResponseDefaultType1
):
    if response.status_code == 200:

        def _parse_response_200(data: object) -> AssetPostSchema | AssetSchema:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_asset_schema_typed_type_0 = AssetSchema.from_dict(
                    data
                )

                return componentsschemas_asset_schema_typed_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_asset_schema_typed_type_1 = AssetPostSchema.from_dict(
                data
            )

            return componentsschemas_asset_schema_typed_type_1

        response_200 = _parse_response_200(response.json())

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
        PostAssetsByAssetIdViewsResponseDefaultType0
        | PostAssetsByAssetIdViewsResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                PostAssetsByAssetIdViewsResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PostAssetsByAssetIdViewsResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | AssetPostSchema
    | AssetSchema
    | PostAssetsByAssetIdViewsResponseDefaultType0
    | PostAssetsByAssetIdViewsResponseDefaultType1
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
) -> Response[
    Any
    | AssetPostSchema
    | AssetSchema
    | PostAssetsByAssetIdViewsResponseDefaultType0
    | PostAssetsByAssetIdViewsResponseDefaultType1
]:
    """Mark asset as viewed


    Required roles:
     - can_read_assets

    Args:
        asset_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AssetPostSchema | AssetSchema | PostAssetsByAssetIdViewsResponseDefaultType0 | PostAssetsByAssetIdViewsResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | AssetPostSchema
    | AssetSchema
    | PostAssetsByAssetIdViewsResponseDefaultType0
    | PostAssetsByAssetIdViewsResponseDefaultType1
    | None
):
    """Mark asset as viewed


    Required roles:
     - can_read_assets

    Args:
        asset_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AssetPostSchema | AssetSchema | PostAssetsByAssetIdViewsResponseDefaultType0 | PostAssetsByAssetIdViewsResponseDefaultType1
    """

    return sync_detailed(
        asset_id=asset_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | AssetPostSchema
    | AssetSchema
    | PostAssetsByAssetIdViewsResponseDefaultType0
    | PostAssetsByAssetIdViewsResponseDefaultType1
]:
    """Mark asset as viewed


    Required roles:
     - can_read_assets

    Args:
        asset_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AssetPostSchema | AssetSchema | PostAssetsByAssetIdViewsResponseDefaultType0 | PostAssetsByAssetIdViewsResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | AssetPostSchema
    | AssetSchema
    | PostAssetsByAssetIdViewsResponseDefaultType0
    | PostAssetsByAssetIdViewsResponseDefaultType1
    | None
):
    """Mark asset as viewed


    Required roles:
     - can_read_assets

    Args:
        asset_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AssetPostSchema | AssetSchema | PostAssetsByAssetIdViewsResponseDefaultType0 | PostAssetsByAssetIdViewsResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            client=client,
        )
    ).parsed
