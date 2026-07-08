from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_assets_by_asset_id_segments_by_segment_id_reindex_response_default import (
    PostAssetsByAssetIdSegmentsBySegmentIdReindexResponseDefault,
)
from ...models.reindex_segment_schema import ReindexSegmentSchema
from ...types import Response


def _get_kwargs(
    asset_id: str,
    segment_id: str,
    *,
    body: ReindexSegmentSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/assets/{asset_id}/segments/{segment_id}/reindex/".format(
            asset_id=quote(str(asset_id), safe=""),
            segment_id=quote(str(segment_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostAssetsByAssetIdSegmentsBySegmentIdReindexResponseDefault:
    if response.status_code == 201:
        response_201 = cast(Any, None)
        return response_201

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = (
        PostAssetsByAssetIdSegmentsBySegmentIdReindexResponseDefault.from_dict(
            response.json()
        )
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PostAssetsByAssetIdSegmentsBySegmentIdReindexResponseDefault]:
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
    body: ReindexSegmentSchema,
) -> Response[Any | PostAssetsByAssetIdSegmentsBySegmentIdReindexResponseDefault]:
    """Reindex assets segment


    Required roles:
     - can_reindex_segments

    Args:
        asset_id (str):
        segment_id (str):
        body (ReindexSegmentSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostAssetsByAssetIdSegmentsBySegmentIdReindexResponseDefault]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        segment_id=segment_id,
        body=body,
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
    body: ReindexSegmentSchema,
) -> Any | PostAssetsByAssetIdSegmentsBySegmentIdReindexResponseDefault | None:
    """Reindex assets segment


    Required roles:
     - can_reindex_segments

    Args:
        asset_id (str):
        segment_id (str):
        body (ReindexSegmentSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostAssetsByAssetIdSegmentsBySegmentIdReindexResponseDefault
    """

    return sync_detailed(
        asset_id=asset_id,
        segment_id=segment_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    segment_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ReindexSegmentSchema,
) -> Response[Any | PostAssetsByAssetIdSegmentsBySegmentIdReindexResponseDefault]:
    """Reindex assets segment


    Required roles:
     - can_reindex_segments

    Args:
        asset_id (str):
        segment_id (str):
        body (ReindexSegmentSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostAssetsByAssetIdSegmentsBySegmentIdReindexResponseDefault]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        segment_id=segment_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    segment_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ReindexSegmentSchema,
) -> Any | PostAssetsByAssetIdSegmentsBySegmentIdReindexResponseDefault | None:
    """Reindex assets segment


    Required roles:
     - can_reindex_segments

    Args:
        asset_id (str):
        segment_id (str):
        body (ReindexSegmentSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostAssetsByAssetIdSegmentsBySegmentIdReindexResponseDefault
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            segment_id=segment_id,
            client=client,
            body=body,
        )
    ).parsed
