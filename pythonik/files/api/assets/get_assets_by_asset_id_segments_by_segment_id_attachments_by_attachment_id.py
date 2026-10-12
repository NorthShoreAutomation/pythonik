from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.attachment_schema import AttachmentSchema
from ...models.get_assets_by_asset_id_segments_by_segment_id_attachments_by_attachment_id_response_default import (
    GetAssetsByAssetIdSegmentsBySegmentIdAttachmentsByAttachmentIdResponseDefault,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    asset_id: str,
    segment_id: str,
    attachment_id: str,
    *,
    content_disposition: str | Unset = UNSET,
    content_type: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["content_disposition"] = content_disposition

    params["content_type"] = content_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/assets/{asset_id}/segments/{segment_id}/attachments/{attachment_id}/".format(
            asset_id=quote(str(asset_id), safe=""),
            segment_id=quote(str(segment_id), safe=""),
            attachment_id=quote(str(attachment_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | AttachmentSchema
    | GetAssetsByAssetIdSegmentsBySegmentIdAttachmentsByAttachmentIdResponseDefault
):
    if response.status_code == 200:
        response_200 = AttachmentSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = GetAssetsByAssetIdSegmentsBySegmentIdAttachmentsByAttachmentIdResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | AttachmentSchema
    | GetAssetsByAssetIdSegmentsBySegmentIdAttachmentsByAttachmentIdResponseDefault
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
    attachment_id: str,
    *,
    client: AuthenticatedClient | Client,
    content_disposition: str | Unset = UNSET,
    content_type: str | Unset = UNSET,
) -> Response[
    Any
    | AttachmentSchema
    | GetAssetsByAssetIdSegmentsBySegmentIdAttachmentsByAttachmentIdResponseDefault
]:
    """Get a segment's attachment


    Required roles:
     - can_read_assets
    - can_read_segments

    Args:
        asset_id (str):
        segment_id (str):
        attachment_id (str):
        content_disposition (str | Unset):
        content_type (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AttachmentSchema | GetAssetsByAssetIdSegmentsBySegmentIdAttachmentsByAttachmentIdResponseDefault]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        segment_id=segment_id,
        attachment_id=attachment_id,
        content_disposition=content_disposition,
        content_type=content_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: str,
    segment_id: str,
    attachment_id: str,
    *,
    client: AuthenticatedClient | Client,
    content_disposition: str | Unset = UNSET,
    content_type: str | Unset = UNSET,
) -> (
    Any
    | AttachmentSchema
    | GetAssetsByAssetIdSegmentsBySegmentIdAttachmentsByAttachmentIdResponseDefault
    | None
):
    """Get a segment's attachment


    Required roles:
     - can_read_assets
    - can_read_segments

    Args:
        asset_id (str):
        segment_id (str):
        attachment_id (str):
        content_disposition (str | Unset):
        content_type (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AttachmentSchema | GetAssetsByAssetIdSegmentsBySegmentIdAttachmentsByAttachmentIdResponseDefault
    """

    return sync_detailed(
        asset_id=asset_id,
        segment_id=segment_id,
        attachment_id=attachment_id,
        client=client,
        content_disposition=content_disposition,
        content_type=content_type,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    segment_id: str,
    attachment_id: str,
    *,
    client: AuthenticatedClient | Client,
    content_disposition: str | Unset = UNSET,
    content_type: str | Unset = UNSET,
) -> Response[
    Any
    | AttachmentSchema
    | GetAssetsByAssetIdSegmentsBySegmentIdAttachmentsByAttachmentIdResponseDefault
]:
    """Get a segment's attachment


    Required roles:
     - can_read_assets
    - can_read_segments

    Args:
        asset_id (str):
        segment_id (str):
        attachment_id (str):
        content_disposition (str | Unset):
        content_type (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AttachmentSchema | GetAssetsByAssetIdSegmentsBySegmentIdAttachmentsByAttachmentIdResponseDefault]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        segment_id=segment_id,
        attachment_id=attachment_id,
        content_disposition=content_disposition,
        content_type=content_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    segment_id: str,
    attachment_id: str,
    *,
    client: AuthenticatedClient | Client,
    content_disposition: str | Unset = UNSET,
    content_type: str | Unset = UNSET,
) -> (
    Any
    | AttachmentSchema
    | GetAssetsByAssetIdSegmentsBySegmentIdAttachmentsByAttachmentIdResponseDefault
    | None
):
    """Get a segment's attachment


    Required roles:
     - can_read_assets
    - can_read_segments

    Args:
        asset_id (str):
        segment_id (str):
        attachment_id (str):
        content_disposition (str | Unset):
        content_type (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AttachmentSchema | GetAssetsByAssetIdSegmentsBySegmentIdAttachmentsByAttachmentIdResponseDefault
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            segment_id=segment_id,
            attachment_id=attachment_id,
            client=client,
            content_disposition=content_disposition,
            content_type=content_type,
        )
    ).parsed
