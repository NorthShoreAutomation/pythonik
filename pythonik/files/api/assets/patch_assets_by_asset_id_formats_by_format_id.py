from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.format_schema import FormatSchema
from ...models.patch_assets_by_asset_id_formats_by_format_id_response_default import (
    PatchAssetsByAssetIdFormatsByFormatIdResponseDefault,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    asset_id: str,
    format_id: str,
    *,
    body: FormatSchema,
    sync_components: bool | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["sync_components"] = sync_components

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/assets/{asset_id}/formats/{format_id}/".format(
            asset_id=quote(str(asset_id), safe=""),
            format_id=quote(str(format_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | FormatSchema | PatchAssetsByAssetIdFormatsByFormatIdResponseDefault:
    if response.status_code == 200:
        response_200 = FormatSchema.from_dict(response.json())

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

    response_default = PatchAssetsByAssetIdFormatsByFormatIdResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | FormatSchema | PatchAssetsByAssetIdFormatsByFormatIdResponseDefault
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    asset_id: str,
    format_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: FormatSchema,
    sync_components: bool | Unset = UNSET,
) -> Response[
    Any | FormatSchema | PatchAssetsByAssetIdFormatsByFormatIdResponseDefault
]:
    """Update format information


    Required roles:
     - can_write_formats

    Args:
        asset_id (str):
        format_id (str):
        sync_components (bool | Unset):
        body (FormatSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FormatSchema | PatchAssetsByAssetIdFormatsByFormatIdResponseDefault]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        format_id=format_id,
        body=body,
        sync_components=sync_components,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: str,
    format_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: FormatSchema,
    sync_components: bool | Unset = UNSET,
) -> Any | FormatSchema | PatchAssetsByAssetIdFormatsByFormatIdResponseDefault | None:
    """Update format information


    Required roles:
     - can_write_formats

    Args:
        asset_id (str):
        format_id (str):
        sync_components (bool | Unset):
        body (FormatSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FormatSchema | PatchAssetsByAssetIdFormatsByFormatIdResponseDefault
    """

    return sync_detailed(
        asset_id=asset_id,
        format_id=format_id,
        client=client,
        body=body,
        sync_components=sync_components,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    format_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: FormatSchema,
    sync_components: bool | Unset = UNSET,
) -> Response[
    Any | FormatSchema | PatchAssetsByAssetIdFormatsByFormatIdResponseDefault
]:
    """Update format information


    Required roles:
     - can_write_formats

    Args:
        asset_id (str):
        format_id (str):
        sync_components (bool | Unset):
        body (FormatSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FormatSchema | PatchAssetsByAssetIdFormatsByFormatIdResponseDefault]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        format_id=format_id,
        body=body,
        sync_components=sync_components,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    format_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: FormatSchema,
    sync_components: bool | Unset = UNSET,
) -> Any | FormatSchema | PatchAssetsByAssetIdFormatsByFormatIdResponseDefault | None:
    """Update format information


    Required roles:
     - can_write_formats

    Args:
        asset_id (str):
        format_id (str):
        sync_components (bool | Unset):
        body (FormatSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FormatSchema | PatchAssetsByAssetIdFormatsByFormatIdResponseDefault
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            format_id=format_id,
            client=client,
            body=body,
            sync_components=sync_components,
        )
    ).parsed
