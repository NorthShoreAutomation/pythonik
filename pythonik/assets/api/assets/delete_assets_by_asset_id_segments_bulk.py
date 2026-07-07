from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_assets_by_asset_id_segments_bulk_response_default_type_0 import (
    DeleteAssetsByAssetIdSegmentsBulkResponseDefaultType0,
)
from ...models.delete_assets_by_asset_id_segments_bulk_response_default_type_1 import (
    DeleteAssetsByAssetIdSegmentsBulkResponseDefaultType1,
)
from ...models.delete_segments_schema import DeleteSegmentsSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    asset_id: str,
    *,
    body: DeleteSegmentsSchema,
    immediately: bool | Unset = True,
    ignore_reindexing: bool | Unset = True,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["immediately"] = immediately

    params["ignore_reindexing"] = ignore_reindexing

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/assets/{asset_id}/segments/bulk/".format(
            asset_id=quote(str(asset_id), safe=""),
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
    | DeleteAssetsByAssetIdSegmentsBulkResponseDefaultType0
    | DeleteAssetsByAssetIdSegmentsBulkResponseDefaultType1
):
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

    def _parse_response_default(
        data: object,
    ) -> (
        DeleteAssetsByAssetIdSegmentsBulkResponseDefaultType0
        | DeleteAssetsByAssetIdSegmentsBulkResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                DeleteAssetsByAssetIdSegmentsBulkResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            DeleteAssetsByAssetIdSegmentsBulkResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | DeleteAssetsByAssetIdSegmentsBulkResponseDefaultType0
    | DeleteAssetsByAssetIdSegmentsBulkResponseDefaultType1
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
    body: DeleteSegmentsSchema,
    immediately: bool | Unset = True,
    ignore_reindexing: bool | Unset = True,
) -> Response[
    Any
    | DeleteAssetsByAssetIdSegmentsBulkResponseDefaultType0
    | DeleteAssetsByAssetIdSegmentsBulkResponseDefaultType1
]:
    """Delete segments with either ids or by type


    Required roles:
     - can_delete_segments

    Args:
        asset_id (str):
        immediately (bool | Unset):  Default: True.
        ignore_reindexing (bool | Unset):  Default: True.
        body (DeleteSegmentsSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteAssetsByAssetIdSegmentsBulkResponseDefaultType0 | DeleteAssetsByAssetIdSegmentsBulkResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        body=body,
        immediately=immediately,
        ignore_reindexing=ignore_reindexing,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DeleteSegmentsSchema,
    immediately: bool | Unset = True,
    ignore_reindexing: bool | Unset = True,
) -> (
    Any
    | DeleteAssetsByAssetIdSegmentsBulkResponseDefaultType0
    | DeleteAssetsByAssetIdSegmentsBulkResponseDefaultType1
    | None
):
    """Delete segments with either ids or by type


    Required roles:
     - can_delete_segments

    Args:
        asset_id (str):
        immediately (bool | Unset):  Default: True.
        ignore_reindexing (bool | Unset):  Default: True.
        body (DeleteSegmentsSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteAssetsByAssetIdSegmentsBulkResponseDefaultType0 | DeleteAssetsByAssetIdSegmentsBulkResponseDefaultType1
    """

    return sync_detailed(
        asset_id=asset_id,
        client=client,
        body=body,
        immediately=immediately,
        ignore_reindexing=ignore_reindexing,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DeleteSegmentsSchema,
    immediately: bool | Unset = True,
    ignore_reindexing: bool | Unset = True,
) -> Response[
    Any
    | DeleteAssetsByAssetIdSegmentsBulkResponseDefaultType0
    | DeleteAssetsByAssetIdSegmentsBulkResponseDefaultType1
]:
    """Delete segments with either ids or by type


    Required roles:
     - can_delete_segments

    Args:
        asset_id (str):
        immediately (bool | Unset):  Default: True.
        ignore_reindexing (bool | Unset):  Default: True.
        body (DeleteSegmentsSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteAssetsByAssetIdSegmentsBulkResponseDefaultType0 | DeleteAssetsByAssetIdSegmentsBulkResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        body=body,
        immediately=immediately,
        ignore_reindexing=ignore_reindexing,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DeleteSegmentsSchema,
    immediately: bool | Unset = True,
    ignore_reindexing: bool | Unset = True,
) -> (
    Any
    | DeleteAssetsByAssetIdSegmentsBulkResponseDefaultType0
    | DeleteAssetsByAssetIdSegmentsBulkResponseDefaultType1
    | None
):
    """Delete segments with either ids or by type


    Required roles:
     - can_delete_segments

    Args:
        asset_id (str):
        immediately (bool | Unset):  Default: True.
        ignore_reindexing (bool | Unset):  Default: True.
        body (DeleteSegmentsSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteAssetsByAssetIdSegmentsBulkResponseDefaultType0 | DeleteAssetsByAssetIdSegmentsBulkResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            client=client,
            body=body,
            immediately=immediately,
            ignore_reindexing=ignore_reindexing,
        )
    ).parsed
