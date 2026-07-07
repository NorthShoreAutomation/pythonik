from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bulk_create_segments_schema import BulkCreateSegmentsSchema
from ...models.post_assets_by_asset_id_segments_bulk_response_default_type_0 import (
    PostAssetsByAssetIdSegmentsBulkResponseDefaultType0,
)
from ...models.post_assets_by_asset_id_segments_bulk_response_default_type_1 import (
    PostAssetsByAssetIdSegmentsBulkResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    asset_id: str,
    *,
    body: BulkCreateSegmentsSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/assets/{asset_id}/segments/bulk/".format(
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
    | PostAssetsByAssetIdSegmentsBulkResponseDefaultType0
    | PostAssetsByAssetIdSegmentsBulkResponseDefaultType1
):
    if response.status_code == 201:
        response_201 = cast(Any, None)
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
        PostAssetsByAssetIdSegmentsBulkResponseDefaultType0
        | PostAssetsByAssetIdSegmentsBulkResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                PostAssetsByAssetIdSegmentsBulkResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PostAssetsByAssetIdSegmentsBulkResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostAssetsByAssetIdSegmentsBulkResponseDefaultType0
    | PostAssetsByAssetIdSegmentsBulkResponseDefaultType1
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
    body: BulkCreateSegmentsSchema,
) -> Response[
    Any
    | PostAssetsByAssetIdSegmentsBulkResponseDefaultType0
    | PostAssetsByAssetIdSegmentsBulkResponseDefaultType1
]:
    """Create multiple new segments for a single asset


    Required roles:
     - can_create_segments

    Args:
        asset_id (str):
        body (BulkCreateSegmentsSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostAssetsByAssetIdSegmentsBulkResponseDefaultType0 | PostAssetsByAssetIdSegmentsBulkResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BulkCreateSegmentsSchema,
) -> (
    Any
    | PostAssetsByAssetIdSegmentsBulkResponseDefaultType0
    | PostAssetsByAssetIdSegmentsBulkResponseDefaultType1
    | None
):
    """Create multiple new segments for a single asset


    Required roles:
     - can_create_segments

    Args:
        asset_id (str):
        body (BulkCreateSegmentsSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostAssetsByAssetIdSegmentsBulkResponseDefaultType0 | PostAssetsByAssetIdSegmentsBulkResponseDefaultType1
    """

    return sync_detailed(
        asset_id=asset_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BulkCreateSegmentsSchema,
) -> Response[
    Any
    | PostAssetsByAssetIdSegmentsBulkResponseDefaultType0
    | PostAssetsByAssetIdSegmentsBulkResponseDefaultType1
]:
    """Create multiple new segments for a single asset


    Required roles:
     - can_create_segments

    Args:
        asset_id (str):
        body (BulkCreateSegmentsSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostAssetsByAssetIdSegmentsBulkResponseDefaultType0 | PostAssetsByAssetIdSegmentsBulkResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BulkCreateSegmentsSchema,
) -> (
    Any
    | PostAssetsByAssetIdSegmentsBulkResponseDefaultType0
    | PostAssetsByAssetIdSegmentsBulkResponseDefaultType1
    | None
):
    """Create multiple new segments for a single asset


    Required roles:
     - can_create_segments

    Args:
        asset_id (str):
        body (BulkCreateSegmentsSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostAssetsByAssetIdSegmentsBulkResponseDefaultType0 | PostAssetsByAssetIdSegmentsBulkResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            client=client,
            body=body,
        )
    ).parsed
