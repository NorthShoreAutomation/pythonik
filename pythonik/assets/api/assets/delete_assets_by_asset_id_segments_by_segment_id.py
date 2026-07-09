from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_assets_by_asset_id_segments_by_segment_id_response_default import (
    DeleteAssetsByAssetIdSegmentsBySegmentIdResponseDefault,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    asset_id: str,
    segment_id: str,
    *,
    soft_delete: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["soft_delete"] = soft_delete

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/assets/{asset_id}/segments/{segment_id}/".format(
            asset_id=quote(str(asset_id), safe=""),
            segment_id=quote(str(segment_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DeleteAssetsByAssetIdSegmentsBySegmentIdResponseDefault:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = (
        DeleteAssetsByAssetIdSegmentsBySegmentIdResponseDefault.from_dict(
            response.json()
        )
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DeleteAssetsByAssetIdSegmentsBySegmentIdResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    asset_id: str,
    segment_id: str,
    *,
    client: AuthenticatedClient | Client,
    soft_delete: bool | Unset = UNSET,
) -> Response[Any | DeleteAssetsByAssetIdSegmentsBySegmentIdResponseDefault]:
    """Delete a particular segment from an asset by id


    Required roles:
     - can_delete_segments

    Args:
        asset_id (str):
        segment_id (str):
        soft_delete (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteAssetsByAssetIdSegmentsBySegmentIdResponseDefault]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        segment_id=segment_id,
        soft_delete=soft_delete,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: str,
    segment_id: str,
    *,
    client: AuthenticatedClient | Client,
    soft_delete: bool | Unset = UNSET,
) -> Any | DeleteAssetsByAssetIdSegmentsBySegmentIdResponseDefault | None:
    """Delete a particular segment from an asset by id


    Required roles:
     - can_delete_segments

    Args:
        asset_id (str):
        segment_id (str):
        soft_delete (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteAssetsByAssetIdSegmentsBySegmentIdResponseDefault
    """

    return sync_detailed(
        asset_id=asset_id,
        segment_id=segment_id,
        client=client,
        soft_delete=soft_delete,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    segment_id: str,
    *,
    client: AuthenticatedClient | Client,
    soft_delete: bool | Unset = UNSET,
) -> Response[Any | DeleteAssetsByAssetIdSegmentsBySegmentIdResponseDefault]:
    """Delete a particular segment from an asset by id


    Required roles:
     - can_delete_segments

    Args:
        asset_id (str):
        segment_id (str):
        soft_delete (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteAssetsByAssetIdSegmentsBySegmentIdResponseDefault]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        segment_id=segment_id,
        soft_delete=soft_delete,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    segment_id: str,
    *,
    client: AuthenticatedClient | Client,
    soft_delete: bool | Unset = UNSET,
) -> Any | DeleteAssetsByAssetIdSegmentsBySegmentIdResponseDefault | None:
    """Delete a particular segment from an asset by id


    Required roles:
     - can_delete_segments

    Args:
        asset_id (str):
        segment_id (str):
        soft_delete (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteAssetsByAssetIdSegmentsBySegmentIdResponseDefault
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            segment_id=segment_id,
            client=client,
            soft_delete=soft_delete,
        )
    ).parsed
