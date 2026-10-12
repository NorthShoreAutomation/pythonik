from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.attachment_create_schema import AttachmentCreateSchema
from ...models.post_assets_by_asset_id_segments_by_segment_id_attachments_response_default import (
    PostAssetsByAssetIdSegmentsBySegmentIdAttachmentsResponseDefault,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    asset_id: str,
    segment_id: str,
    *,
    body: AttachmentCreateSchema,
    use_google_resumable_upload: bool | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["use_google_resumable_upload"] = use_google_resumable_upload

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/assets/{asset_id}/segments/{segment_id}/attachments/".format(
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
) -> (
    Any
    | AttachmentCreateSchema
    | PostAssetsByAssetIdSegmentsBySegmentIdAttachmentsResponseDefault
):
    if response.status_code == 201:
        response_201 = AttachmentCreateSchema.from_dict(response.json())

        return response_201

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

    response_default = (
        PostAssetsByAssetIdSegmentsBySegmentIdAttachmentsResponseDefault.from_dict(
            response.json()
        )
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | AttachmentCreateSchema
    | PostAssetsByAssetIdSegmentsBySegmentIdAttachmentsResponseDefault
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
    body: AttachmentCreateSchema,
    use_google_resumable_upload: bool | Unset = UNSET,
) -> Response[
    Any
    | AttachmentCreateSchema
    | PostAssetsByAssetIdSegmentsBySegmentIdAttachmentsResponseDefault
]:
    """Create an attachment and associate it with a segment


    Required roles:
     - can_write_segments

    Args:
        asset_id (str):
        segment_id (str):
        use_google_resumable_upload (bool | Unset):
        body (AttachmentCreateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AttachmentCreateSchema | PostAssetsByAssetIdSegmentsBySegmentIdAttachmentsResponseDefault]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        segment_id=segment_id,
        body=body,
        use_google_resumable_upload=use_google_resumable_upload,
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
    body: AttachmentCreateSchema,
    use_google_resumable_upload: bool | Unset = UNSET,
) -> (
    Any
    | AttachmentCreateSchema
    | PostAssetsByAssetIdSegmentsBySegmentIdAttachmentsResponseDefault
    | None
):
    """Create an attachment and associate it with a segment


    Required roles:
     - can_write_segments

    Args:
        asset_id (str):
        segment_id (str):
        use_google_resumable_upload (bool | Unset):
        body (AttachmentCreateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AttachmentCreateSchema | PostAssetsByAssetIdSegmentsBySegmentIdAttachmentsResponseDefault
    """

    return sync_detailed(
        asset_id=asset_id,
        segment_id=segment_id,
        client=client,
        body=body,
        use_google_resumable_upload=use_google_resumable_upload,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    segment_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AttachmentCreateSchema,
    use_google_resumable_upload: bool | Unset = UNSET,
) -> Response[
    Any
    | AttachmentCreateSchema
    | PostAssetsByAssetIdSegmentsBySegmentIdAttachmentsResponseDefault
]:
    """Create an attachment and associate it with a segment


    Required roles:
     - can_write_segments

    Args:
        asset_id (str):
        segment_id (str):
        use_google_resumable_upload (bool | Unset):
        body (AttachmentCreateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AttachmentCreateSchema | PostAssetsByAssetIdSegmentsBySegmentIdAttachmentsResponseDefault]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        segment_id=segment_id,
        body=body,
        use_google_resumable_upload=use_google_resumable_upload,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    segment_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AttachmentCreateSchema,
    use_google_resumable_upload: bool | Unset = UNSET,
) -> (
    Any
    | AttachmentCreateSchema
    | PostAssetsByAssetIdSegmentsBySegmentIdAttachmentsResponseDefault
    | None
):
    """Create an attachment and associate it with a segment


    Required roles:
     - can_write_segments

    Args:
        asset_id (str):
        segment_id (str):
        use_google_resumable_upload (bool | Unset):
        body (AttachmentCreateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AttachmentCreateSchema | PostAssetsByAssetIdSegmentsBySegmentIdAttachmentsResponseDefault
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            segment_id=segment_id,
            client=client,
            body=body,
            use_google_resumable_upload=use_google_resumable_upload,
        )
    ).parsed
