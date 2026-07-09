from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_assets_by_asset_id_formats_by_format_id_response_default import (
    DeleteAssetsByAssetIdFormatsByFormatIdResponseDefault,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    asset_id: str,
    format_id: str,
    *,
    immediately: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["immediately"] = immediately

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/assets/{asset_id}/formats/{format_id}/".format(
            asset_id=quote(str(asset_id), safe=""),
            format_id=quote(str(format_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DeleteAssetsByAssetIdFormatsByFormatIdResponseDefault:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = DeleteAssetsByAssetIdFormatsByFormatIdResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DeleteAssetsByAssetIdFormatsByFormatIdResponseDefault]:
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
    immediately: bool | Unset = UNSET,
) -> Response[Any | DeleteAssetsByAssetIdFormatsByFormatIdResponseDefault]:
    """Delete asset's format


    Required roles:
     - can_delete_formats

    Args:
        asset_id (str):
        format_id (str):
        immediately (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteAssetsByAssetIdFormatsByFormatIdResponseDefault]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        format_id=format_id,
        immediately=immediately,
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
    immediately: bool | Unset = UNSET,
) -> Any | DeleteAssetsByAssetIdFormatsByFormatIdResponseDefault | None:
    """Delete asset's format


    Required roles:
     - can_delete_formats

    Args:
        asset_id (str):
        format_id (str):
        immediately (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteAssetsByAssetIdFormatsByFormatIdResponseDefault
    """

    return sync_detailed(
        asset_id=asset_id,
        format_id=format_id,
        client=client,
        immediately=immediately,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    format_id: str,
    *,
    client: AuthenticatedClient | Client,
    immediately: bool | Unset = UNSET,
) -> Response[Any | DeleteAssetsByAssetIdFormatsByFormatIdResponseDefault]:
    """Delete asset's format


    Required roles:
     - can_delete_formats

    Args:
        asset_id (str):
        format_id (str):
        immediately (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteAssetsByAssetIdFormatsByFormatIdResponseDefault]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        format_id=format_id,
        immediately=immediately,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    format_id: str,
    *,
    client: AuthenticatedClient | Client,
    immediately: bool | Unset = UNSET,
) -> Any | DeleteAssetsByAssetIdFormatsByFormatIdResponseDefault | None:
    """Delete asset's format


    Required roles:
     - can_delete_formats

    Args:
        asset_id (str):
        format_id (str):
        immediately (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteAssetsByAssetIdFormatsByFormatIdResponseDefault
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            format_id=format_id,
            client=client,
            immediately=immediately,
        )
    ).parsed
