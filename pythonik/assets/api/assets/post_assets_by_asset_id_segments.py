from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_assets_by_asset_id_segments_response_default_type_0 import (
    PostAssetsByAssetIdSegmentsResponseDefaultType0,
)
from ...models.post_assets_by_asset_id_segments_response_default_type_1 import (
    PostAssetsByAssetIdSegmentsResponseDefaultType1,
)
from ...models.segment_schema import SegmentSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    asset_id: str,
    *,
    body: SegmentSchema,
    share_user_email: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(share_user_email, Unset):
        headers["Share-User-Email"] = share_user_email

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/assets/{asset_id}/segments/".format(
            asset_id=quote(str(asset_id), safe=""),
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
    | PostAssetsByAssetIdSegmentsResponseDefaultType0
    | PostAssetsByAssetIdSegmentsResponseDefaultType1
    | SegmentSchema
):
    if response.status_code == 201:
        response_201 = SegmentSchema.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    def _parse_response_default(
        data: object,
    ) -> (
        PostAssetsByAssetIdSegmentsResponseDefaultType0
        | PostAssetsByAssetIdSegmentsResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                PostAssetsByAssetIdSegmentsResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PostAssetsByAssetIdSegmentsResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostAssetsByAssetIdSegmentsResponseDefaultType0
    | PostAssetsByAssetIdSegmentsResponseDefaultType1
    | SegmentSchema
]:
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
    body: SegmentSchema,
    share_user_email: str | Unset = UNSET,
) -> Response[
    Any
    | PostAssetsByAssetIdSegmentsResponseDefaultType0
    | PostAssetsByAssetIdSegmentsResponseDefaultType1
    | SegmentSchema
]:
    """Create a new segment


    Required roles:
     - can_create_segments

    Args:
        asset_id (str):
        share_user_email (str | Unset):
        body (SegmentSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostAssetsByAssetIdSegmentsResponseDefaultType0 | PostAssetsByAssetIdSegmentsResponseDefaultType1 | SegmentSchema]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        body=body,
        share_user_email=share_user_email,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SegmentSchema,
    share_user_email: str | Unset = UNSET,
) -> (
    Any
    | PostAssetsByAssetIdSegmentsResponseDefaultType0
    | PostAssetsByAssetIdSegmentsResponseDefaultType1
    | SegmentSchema
    | None
):
    """Create a new segment


    Required roles:
     - can_create_segments

    Args:
        asset_id (str):
        share_user_email (str | Unset):
        body (SegmentSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostAssetsByAssetIdSegmentsResponseDefaultType0 | PostAssetsByAssetIdSegmentsResponseDefaultType1 | SegmentSchema
    """

    return sync_detailed(
        asset_id=asset_id,
        client=client,
        body=body,
        share_user_email=share_user_email,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SegmentSchema,
    share_user_email: str | Unset = UNSET,
) -> Response[
    Any
    | PostAssetsByAssetIdSegmentsResponseDefaultType0
    | PostAssetsByAssetIdSegmentsResponseDefaultType1
    | SegmentSchema
]:
    """Create a new segment


    Required roles:
     - can_create_segments

    Args:
        asset_id (str):
        share_user_email (str | Unset):
        body (SegmentSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostAssetsByAssetIdSegmentsResponseDefaultType0 | PostAssetsByAssetIdSegmentsResponseDefaultType1 | SegmentSchema]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        body=body,
        share_user_email=share_user_email,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SegmentSchema,
    share_user_email: str | Unset = UNSET,
) -> (
    Any
    | PostAssetsByAssetIdSegmentsResponseDefaultType0
    | PostAssetsByAssetIdSegmentsResponseDefaultType1
    | SegmentSchema
    | None
):
    """Create a new segment


    Required roles:
     - can_create_segments

    Args:
        asset_id (str):
        share_user_email (str | Unset):
        body (SegmentSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostAssetsByAssetIdSegmentsResponseDefaultType0 | PostAssetsByAssetIdSegmentsResponseDefaultType1 | SegmentSchema
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            client=client,
            body=body,
            share_user_email=share_user_email,
        )
    ).parsed
