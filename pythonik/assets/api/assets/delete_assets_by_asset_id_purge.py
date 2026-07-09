from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_assets_by_asset_id_purge_response_default import (
    DeleteAssetsByAssetIdPurgeResponseDefault,
)
from ...types import Response


def _get_kwargs(
    asset_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/assets/{asset_id}/purge/".format(
            asset_id=quote(str(asset_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DeleteAssetsByAssetIdPurgeResponseDefault:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = DeleteAssetsByAssetIdPurgeResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DeleteAssetsByAssetIdPurgeResponseDefault]:
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
) -> Response[Any | DeleteAssetsByAssetIdPurgeResponseDefault]:
    """Purges a particular asset by id immediately


    Required roles:
     - can_purge_assets

    Args:
        asset_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteAssetsByAssetIdPurgeResponseDefault]
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
) -> Any | DeleteAssetsByAssetIdPurgeResponseDefault | None:
    """Purges a particular asset by id immediately


    Required roles:
     - can_purge_assets

    Args:
        asset_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteAssetsByAssetIdPurgeResponseDefault
    """

    return sync_detailed(
        asset_id=asset_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DeleteAssetsByAssetIdPurgeResponseDefault]:
    """Purges a particular asset by id immediately


    Required roles:
     - can_purge_assets

    Args:
        asset_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteAssetsByAssetIdPurgeResponseDefault]
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
) -> Any | DeleteAssetsByAssetIdPurgeResponseDefault | None:
    """Purges a particular asset by id immediately


    Required roles:
     - can_purge_assets

    Args:
        asset_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteAssetsByAssetIdPurgeResponseDefault
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            client=client,
        )
    ).parsed
