from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.asset_post_schema import AssetPostSchema
from ...models.asset_schema import AssetSchema
from ...models.patch_assets_by_asset_id_response_default import (
    PatchAssetsByAssetIdResponseDefault,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    asset_id: str,
    *,
    body: AssetPostSchema | AssetSchema,
    generate_subclip_keyframes: bool | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["generate_subclip_keyframes"] = generate_subclip_keyframes

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/assets/{asset_id}/".format(
            asset_id=quote(str(asset_id), safe=""),
        ),
        "params": params,
    }

    if isinstance(body, AssetSchema):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | AssetPostSchema | AssetSchema | PatchAssetsByAssetIdResponseDefault:
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

    response_default = PatchAssetsByAssetIdResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | AssetPostSchema | AssetSchema | PatchAssetsByAssetIdResponseDefault
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
    body: AssetPostSchema | AssetSchema,
    generate_subclip_keyframes: bool | Unset = UNSET,
) -> Response[
    Any | AssetPostSchema | AssetSchema | PatchAssetsByAssetIdResponseDefault
]:
    """Update asset


    Required roles:
     - can_write_assets

    Args:
        asset_id (str):
        generate_subclip_keyframes (bool | Unset):
        body (AssetPostSchema | AssetSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AssetPostSchema | AssetSchema | PatchAssetsByAssetIdResponseDefault]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        body=body,
        generate_subclip_keyframes=generate_subclip_keyframes,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AssetPostSchema | AssetSchema,
    generate_subclip_keyframes: bool | Unset = UNSET,
) -> Any | AssetPostSchema | AssetSchema | PatchAssetsByAssetIdResponseDefault | None:
    """Update asset


    Required roles:
     - can_write_assets

    Args:
        asset_id (str):
        generate_subclip_keyframes (bool | Unset):
        body (AssetPostSchema | AssetSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AssetPostSchema | AssetSchema | PatchAssetsByAssetIdResponseDefault
    """

    return sync_detailed(
        asset_id=asset_id,
        client=client,
        body=body,
        generate_subclip_keyframes=generate_subclip_keyframes,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AssetPostSchema | AssetSchema,
    generate_subclip_keyframes: bool | Unset = UNSET,
) -> Response[
    Any | AssetPostSchema | AssetSchema | PatchAssetsByAssetIdResponseDefault
]:
    """Update asset


    Required roles:
     - can_write_assets

    Args:
        asset_id (str):
        generate_subclip_keyframes (bool | Unset):
        body (AssetPostSchema | AssetSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AssetPostSchema | AssetSchema | PatchAssetsByAssetIdResponseDefault]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        body=body,
        generate_subclip_keyframes=generate_subclip_keyframes,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AssetPostSchema | AssetSchema,
    generate_subclip_keyframes: bool | Unset = UNSET,
) -> Any | AssetPostSchema | AssetSchema | PatchAssetsByAssetIdResponseDefault | None:
    """Update asset


    Required roles:
     - can_write_assets

    Args:
        asset_id (str):
        generate_subclip_keyframes (bool | Unset):
        body (AssetPostSchema | AssetSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AssetPostSchema | AssetSchema | PatchAssetsByAssetIdResponseDefault
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            client=client,
            body=body,
            generate_subclip_keyframes=generate_subclip_keyframes,
        )
    ).parsed
