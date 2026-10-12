from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.attachments_schema import AttachmentsSchema
from ...models.get_assets_by_asset_id_segments_by_segment_id_attachments_response_default import (
    GetAssetsByAssetIdSegmentsBySegmentIdAttachmentsResponseDefault,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    asset_id: str,
    segment_id: str,
    *,
    per_page: int | Unset = UNSET,
    generate_signed_url: bool | Unset = UNSET,
    content_disposition: str | Unset = UNSET,
    last_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["per_page"] = per_page

    params["generate_signed_url"] = generate_signed_url

    params["content_disposition"] = content_disposition

    params["last_id"] = last_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/assets/{asset_id}/segments/{segment_id}/attachments/".format(
            asset_id=quote(str(asset_id), safe=""),
            segment_id=quote(str(segment_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | AttachmentsSchema
    | GetAssetsByAssetIdSegmentsBySegmentIdAttachmentsResponseDefault
):
    if response.status_code == 200:
        response_200 = AttachmentsSchema.from_dict(response.json())

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

    response_default = (
        GetAssetsByAssetIdSegmentsBySegmentIdAttachmentsResponseDefault.from_dict(
            response.json()
        )
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | AttachmentsSchema
    | GetAssetsByAssetIdSegmentsBySegmentIdAttachmentsResponseDefault
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
    per_page: int | Unset = UNSET,
    generate_signed_url: bool | Unset = UNSET,
    content_disposition: str | Unset = UNSET,
    last_id: str | Unset = UNSET,
) -> Response[
    Any
    | AttachmentsSchema
    | GetAssetsByAssetIdSegmentsBySegmentIdAttachmentsResponseDefault
]:
    """Get all attachments for a segment


    Required roles:
     - can_read_assets
    - can_read_segments

    Args:
        asset_id (str):
        segment_id (str):
        per_page (int | Unset):
        generate_signed_url (bool | Unset):
        content_disposition (str | Unset):
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AttachmentsSchema | GetAssetsByAssetIdSegmentsBySegmentIdAttachmentsResponseDefault]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        segment_id=segment_id,
        per_page=per_page,
        generate_signed_url=generate_signed_url,
        content_disposition=content_disposition,
        last_id=last_id,
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
    per_page: int | Unset = UNSET,
    generate_signed_url: bool | Unset = UNSET,
    content_disposition: str | Unset = UNSET,
    last_id: str | Unset = UNSET,
) -> (
    Any
    | AttachmentsSchema
    | GetAssetsByAssetIdSegmentsBySegmentIdAttachmentsResponseDefault
    | None
):
    """Get all attachments for a segment


    Required roles:
     - can_read_assets
    - can_read_segments

    Args:
        asset_id (str):
        segment_id (str):
        per_page (int | Unset):
        generate_signed_url (bool | Unset):
        content_disposition (str | Unset):
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AttachmentsSchema | GetAssetsByAssetIdSegmentsBySegmentIdAttachmentsResponseDefault
    """

    return sync_detailed(
        asset_id=asset_id,
        segment_id=segment_id,
        client=client,
        per_page=per_page,
        generate_signed_url=generate_signed_url,
        content_disposition=content_disposition,
        last_id=last_id,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    segment_id: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    generate_signed_url: bool | Unset = UNSET,
    content_disposition: str | Unset = UNSET,
    last_id: str | Unset = UNSET,
) -> Response[
    Any
    | AttachmentsSchema
    | GetAssetsByAssetIdSegmentsBySegmentIdAttachmentsResponseDefault
]:
    """Get all attachments for a segment


    Required roles:
     - can_read_assets
    - can_read_segments

    Args:
        asset_id (str):
        segment_id (str):
        per_page (int | Unset):
        generate_signed_url (bool | Unset):
        content_disposition (str | Unset):
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AttachmentsSchema | GetAssetsByAssetIdSegmentsBySegmentIdAttachmentsResponseDefault]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        segment_id=segment_id,
        per_page=per_page,
        generate_signed_url=generate_signed_url,
        content_disposition=content_disposition,
        last_id=last_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    segment_id: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    generate_signed_url: bool | Unset = UNSET,
    content_disposition: str | Unset = UNSET,
    last_id: str | Unset = UNSET,
) -> (
    Any
    | AttachmentsSchema
    | GetAssetsByAssetIdSegmentsBySegmentIdAttachmentsResponseDefault
    | None
):
    """Get all attachments for a segment


    Required roles:
     - can_read_assets
    - can_read_segments

    Args:
        asset_id (str):
        segment_id (str):
        per_page (int | Unset):
        generate_signed_url (bool | Unset):
        content_disposition (str | Unset):
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AttachmentsSchema | GetAssetsByAssetIdSegmentsBySegmentIdAttachmentsResponseDefault
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            segment_id=segment_id,
            client=client,
            per_page=per_page,
            generate_signed_url=generate_signed_url,
            content_disposition=content_disposition,
            last_id=last_id,
        )
    ).parsed
