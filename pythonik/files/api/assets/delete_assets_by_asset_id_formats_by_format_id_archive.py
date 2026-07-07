from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_assets_by_asset_id_formats_by_format_id_archive_response_default_type_0 import (
    DeleteAssetsByAssetIdFormatsByFormatIdArchiveResponseDefaultType0,
)
from ...models.delete_assets_by_asset_id_formats_by_format_id_archive_response_default_type_1 import (
    DeleteAssetsByAssetIdFormatsByFormatIdArchiveResponseDefaultType1,
)
from ...models.format_delete_archive_schema import FormatDeleteArchiveSchema
from ...types import Response


def _get_kwargs(
    asset_id: str,
    format_id: str,
    *,
    body: FormatDeleteArchiveSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/assets/{asset_id}/formats/{format_id}/archive/".format(
            asset_id=quote(str(asset_id), safe=""),
            format_id=quote(str(format_id), safe=""),
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
    | DeleteAssetsByAssetIdFormatsByFormatIdArchiveResponseDefaultType0
    | DeleteAssetsByAssetIdFormatsByFormatIdArchiveResponseDefaultType1
):
    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

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
        DeleteAssetsByAssetIdFormatsByFormatIdArchiveResponseDefaultType0
        | DeleteAssetsByAssetIdFormatsByFormatIdArchiveResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = DeleteAssetsByAssetIdFormatsByFormatIdArchiveResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            DeleteAssetsByAssetIdFormatsByFormatIdArchiveResponseDefaultType1.from_dict(
                data
            )
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | DeleteAssetsByAssetIdFormatsByFormatIdArchiveResponseDefaultType0
    | DeleteAssetsByAssetIdFormatsByFormatIdArchiveResponseDefaultType1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    asset_id: str,
    format_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: FormatDeleteArchiveSchema,
) -> Response[
    Any
    | DeleteAssetsByAssetIdFormatsByFormatIdArchiveResponseDefaultType0
    | DeleteAssetsByAssetIdFormatsByFormatIdArchiveResponseDefaultType1
]:
    """Delete archived format


    Required roles:
     - can_delete_archived_formats

    Args:
        asset_id (str):
        format_id (str):
        body (FormatDeleteArchiveSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteAssetsByAssetIdFormatsByFormatIdArchiveResponseDefaultType0 | DeleteAssetsByAssetIdFormatsByFormatIdArchiveResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        format_id=format_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: str,
    format_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: FormatDeleteArchiveSchema,
) -> (
    Any
    | DeleteAssetsByAssetIdFormatsByFormatIdArchiveResponseDefaultType0
    | DeleteAssetsByAssetIdFormatsByFormatIdArchiveResponseDefaultType1
    | None
):
    """Delete archived format


    Required roles:
     - can_delete_archived_formats

    Args:
        asset_id (str):
        format_id (str):
        body (FormatDeleteArchiveSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteAssetsByAssetIdFormatsByFormatIdArchiveResponseDefaultType0 | DeleteAssetsByAssetIdFormatsByFormatIdArchiveResponseDefaultType1
    """

    return sync_detailed(
        asset_id=asset_id,
        format_id=format_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    format_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: FormatDeleteArchiveSchema,
) -> Response[
    Any
    | DeleteAssetsByAssetIdFormatsByFormatIdArchiveResponseDefaultType0
    | DeleteAssetsByAssetIdFormatsByFormatIdArchiveResponseDefaultType1
]:
    """Delete archived format


    Required roles:
     - can_delete_archived_formats

    Args:
        asset_id (str):
        format_id (str):
        body (FormatDeleteArchiveSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteAssetsByAssetIdFormatsByFormatIdArchiveResponseDefaultType0 | DeleteAssetsByAssetIdFormatsByFormatIdArchiveResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        format_id=format_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    format_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: FormatDeleteArchiveSchema,
) -> (
    Any
    | DeleteAssetsByAssetIdFormatsByFormatIdArchiveResponseDefaultType0
    | DeleteAssetsByAssetIdFormatsByFormatIdArchiveResponseDefaultType1
    | None
):
    """Delete archived format


    Required roles:
     - can_delete_archived_formats

    Args:
        asset_id (str):
        format_id (str):
        body (FormatDeleteArchiveSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteAssetsByAssetIdFormatsByFormatIdArchiveResponseDefaultType0 | DeleteAssetsByAssetIdFormatsByFormatIdArchiveResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            format_id=format_id,
            client=client,
            body=body,
        )
    ).parsed
