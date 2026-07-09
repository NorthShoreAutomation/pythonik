from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.edit_segment_schema import EditSegmentSchema
from ...models.patch_assets_by_asset_id_segments_by_segment_id_response_default import (
    PatchAssetsByAssetIdSegmentsBySegmentIdResponseDefault,
)
from ...models.segment_schema import SegmentSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    asset_id: str,
    segment_id: str,
    *,
    body: EditSegmentSchema,
    generate_subclip_keyframes: bool | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["generate_subclip_keyframes"] = generate_subclip_keyframes

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/assets/{asset_id}/segments/{segment_id}/".format(
            asset_id=quote(str(asset_id), safe=""),
            segment_id=quote(str(segment_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PatchAssetsByAssetIdSegmentsBySegmentIdResponseDefault | SegmentSchema:
    if response.status_code == 200:
        response_200 = SegmentSchema.from_dict(response.json())

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

    response_default = PatchAssetsByAssetIdSegmentsBySegmentIdResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | PatchAssetsByAssetIdSegmentsBySegmentIdResponseDefault | SegmentSchema
]:
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
    body: EditSegmentSchema,
    generate_subclip_keyframes: bool | Unset = UNSET,
) -> Response[
    Any | PatchAssetsByAssetIdSegmentsBySegmentIdResponseDefault | SegmentSchema
]:
    """Update segment


    Required roles:
     - can_write_segments

    Args:
        asset_id (str):
        segment_id (str):
        generate_subclip_keyframes (bool | Unset):
        body (EditSegmentSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PatchAssetsByAssetIdSegmentsBySegmentIdResponseDefault | SegmentSchema]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        segment_id=segment_id,
        body=body,
        generate_subclip_keyframes=generate_subclip_keyframes,
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
    body: EditSegmentSchema,
    generate_subclip_keyframes: bool | Unset = UNSET,
) -> (
    Any | PatchAssetsByAssetIdSegmentsBySegmentIdResponseDefault | SegmentSchema | None
):
    """Update segment


    Required roles:
     - can_write_segments

    Args:
        asset_id (str):
        segment_id (str):
        generate_subclip_keyframes (bool | Unset):
        body (EditSegmentSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PatchAssetsByAssetIdSegmentsBySegmentIdResponseDefault | SegmentSchema
    """

    return sync_detailed(
        asset_id=asset_id,
        segment_id=segment_id,
        client=client,
        body=body,
        generate_subclip_keyframes=generate_subclip_keyframes,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    segment_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: EditSegmentSchema,
    generate_subclip_keyframes: bool | Unset = UNSET,
) -> Response[
    Any | PatchAssetsByAssetIdSegmentsBySegmentIdResponseDefault | SegmentSchema
]:
    """Update segment


    Required roles:
     - can_write_segments

    Args:
        asset_id (str):
        segment_id (str):
        generate_subclip_keyframes (bool | Unset):
        body (EditSegmentSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PatchAssetsByAssetIdSegmentsBySegmentIdResponseDefault | SegmentSchema]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        segment_id=segment_id,
        body=body,
        generate_subclip_keyframes=generate_subclip_keyframes,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    segment_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: EditSegmentSchema,
    generate_subclip_keyframes: bool | Unset = UNSET,
) -> (
    Any | PatchAssetsByAssetIdSegmentsBySegmentIdResponseDefault | SegmentSchema | None
):
    """Update segment


    Required roles:
     - can_write_segments

    Args:
        asset_id (str):
        segment_id (str):
        generate_subclip_keyframes (bool | Unset):
        body (EditSegmentSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PatchAssetsByAssetIdSegmentsBySegmentIdResponseDefault | SegmentSchema
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            segment_id=segment_id,
            client=client,
            body=body,
            generate_subclip_keyframes=generate_subclip_keyframes,
        )
    ).parsed
