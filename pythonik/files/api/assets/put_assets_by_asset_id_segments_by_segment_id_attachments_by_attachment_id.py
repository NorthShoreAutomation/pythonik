from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.attachment_schema import AttachmentSchema
from ...models.attachment_update_schema import AttachmentUpdateSchema
from ...models.put_assets_by_asset_id_segments_by_segment_id_attachments_by_attachment_id_response_default import (
    PutAssetsByAssetIdSegmentsBySegmentIdAttachmentsByAttachmentIdResponseDefault,
)
from ...types import Response


def _get_kwargs(
    asset_id: str,
    segment_id: str,
    attachment_id: str,
    *,
    body: AttachmentUpdateSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/assets/{asset_id}/segments/{segment_id}/attachments/{attachment_id}/".format(
            asset_id=quote(str(asset_id), safe=""),
            segment_id=quote(str(segment_id), safe=""),
            attachment_id=quote(str(attachment_id), safe=""),
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
    | AttachmentSchema
    | PutAssetsByAssetIdSegmentsBySegmentIdAttachmentsByAttachmentIdResponseDefault
):
    if response.status_code == 200:
        response_200 = AttachmentSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = PutAssetsByAssetIdSegmentsBySegmentIdAttachmentsByAttachmentIdResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | AttachmentSchema
    | PutAssetsByAssetIdSegmentsBySegmentIdAttachmentsByAttachmentIdResponseDefault
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
    body: AttachmentUpdateSchema,
) -> Response[
    Any
    | AttachmentSchema
    | PutAssetsByAssetIdSegmentsBySegmentIdAttachmentsByAttachmentIdResponseDefault
]:
    """Update attachment information


    Required roles:
     - can_write_segments

    Args:
        asset_id (str):
        segment_id (str):
        attachment_id (str):
        body (AttachmentUpdateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AttachmentSchema | PutAssetsByAssetIdSegmentsBySegmentIdAttachmentsByAttachmentIdResponseDefault]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        segment_id=segment_id,
        attachment_id=attachment_id,
        body=body,
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
    body: AttachmentUpdateSchema,
) -> (
    Any
    | AttachmentSchema
    | PutAssetsByAssetIdSegmentsBySegmentIdAttachmentsByAttachmentIdResponseDefault
    | None
):
    """Update attachment information


    Required roles:
     - can_write_segments

    Args:
        asset_id (str):
        segment_id (str):
        attachment_id (str):
        body (AttachmentUpdateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AttachmentSchema | PutAssetsByAssetIdSegmentsBySegmentIdAttachmentsByAttachmentIdResponseDefault
    """

    return sync_detailed(
        asset_id=asset_id,
        segment_id=segment_id,
        attachment_id=attachment_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    segment_id: str,
    attachment_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AttachmentUpdateSchema,
) -> Response[
    Any
    | AttachmentSchema
    | PutAssetsByAssetIdSegmentsBySegmentIdAttachmentsByAttachmentIdResponseDefault
]:
    """Update attachment information


    Required roles:
     - can_write_segments

    Args:
        asset_id (str):
        segment_id (str):
        attachment_id (str):
        body (AttachmentUpdateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AttachmentSchema | PutAssetsByAssetIdSegmentsBySegmentIdAttachmentsByAttachmentIdResponseDefault]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        segment_id=segment_id,
        attachment_id=attachment_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    segment_id: str,
    attachment_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AttachmentUpdateSchema,
) -> (
    Any
    | AttachmentSchema
    | PutAssetsByAssetIdSegmentsBySegmentIdAttachmentsByAttachmentIdResponseDefault
    | None
):
    """Update attachment information


    Required roles:
     - can_write_segments

    Args:
        asset_id (str):
        segment_id (str):
        attachment_id (str):
        body (AttachmentUpdateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AttachmentSchema | PutAssetsByAssetIdSegmentsBySegmentIdAttachmentsByAttachmentIdResponseDefault
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            segment_id=segment_id,
            attachment_id=attachment_id,
            client=client,
            body=body,
        )
    ).parsed
