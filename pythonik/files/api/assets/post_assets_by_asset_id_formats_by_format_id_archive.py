from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.format_archive_schema import FormatArchiveSchema
from ...models.post_assets_by_asset_id_formats_by_format_id_archive_response_default_type_0 import (
    PostAssetsByAssetIdFormatsByFormatIdArchiveResponseDefaultType0,
)
from ...models.post_assets_by_asset_id_formats_by_format_id_archive_response_default_type_1 import (
    PostAssetsByAssetIdFormatsByFormatIdArchiveResponseDefaultType1,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    asset_id: str,
    format_id: str,
    *,
    body: FormatArchiveSchema,
    allow_host_transfer: bool | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["allow_host_transfer"] = allow_host_transfer

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/assets/{asset_id}/formats/{format_id}/archive/".format(
            asset_id=quote(str(asset_id), safe=""),
            format_id=quote(str(format_id), safe=""),
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
    | PostAssetsByAssetIdFormatsByFormatIdArchiveResponseDefaultType0
    | PostAssetsByAssetIdFormatsByFormatIdArchiveResponseDefaultType1
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
        PostAssetsByAssetIdFormatsByFormatIdArchiveResponseDefaultType0
        | PostAssetsByAssetIdFormatsByFormatIdArchiveResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = PostAssetsByAssetIdFormatsByFormatIdArchiveResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PostAssetsByAssetIdFormatsByFormatIdArchiveResponseDefaultType1.from_dict(
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
    | PostAssetsByAssetIdFormatsByFormatIdArchiveResponseDefaultType0
    | PostAssetsByAssetIdFormatsByFormatIdArchiveResponseDefaultType1
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
    body: FormatArchiveSchema,
    allow_host_transfer: bool | Unset = UNSET,
) -> Response[
    Any
    | PostAssetsByAssetIdFormatsByFormatIdArchiveResponseDefaultType0
    | PostAssetsByAssetIdFormatsByFormatIdArchiveResponseDefaultType1
]:
    """Archive format


    Required roles:
     - can_archive_formats

    Args:
        asset_id (str):
        format_id (str):
        allow_host_transfer (bool | Unset):
        body (FormatArchiveSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostAssetsByAssetIdFormatsByFormatIdArchiveResponseDefaultType0 | PostAssetsByAssetIdFormatsByFormatIdArchiveResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        format_id=format_id,
        body=body,
        allow_host_transfer=allow_host_transfer,
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
    body: FormatArchiveSchema,
    allow_host_transfer: bool | Unset = UNSET,
) -> (
    Any
    | PostAssetsByAssetIdFormatsByFormatIdArchiveResponseDefaultType0
    | PostAssetsByAssetIdFormatsByFormatIdArchiveResponseDefaultType1
    | None
):
    """Archive format


    Required roles:
     - can_archive_formats

    Args:
        asset_id (str):
        format_id (str):
        allow_host_transfer (bool | Unset):
        body (FormatArchiveSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostAssetsByAssetIdFormatsByFormatIdArchiveResponseDefaultType0 | PostAssetsByAssetIdFormatsByFormatIdArchiveResponseDefaultType1
    """

    return sync_detailed(
        asset_id=asset_id,
        format_id=format_id,
        client=client,
        body=body,
        allow_host_transfer=allow_host_transfer,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    format_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: FormatArchiveSchema,
    allow_host_transfer: bool | Unset = UNSET,
) -> Response[
    Any
    | PostAssetsByAssetIdFormatsByFormatIdArchiveResponseDefaultType0
    | PostAssetsByAssetIdFormatsByFormatIdArchiveResponseDefaultType1
]:
    """Archive format


    Required roles:
     - can_archive_formats

    Args:
        asset_id (str):
        format_id (str):
        allow_host_transfer (bool | Unset):
        body (FormatArchiveSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostAssetsByAssetIdFormatsByFormatIdArchiveResponseDefaultType0 | PostAssetsByAssetIdFormatsByFormatIdArchiveResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        format_id=format_id,
        body=body,
        allow_host_transfer=allow_host_transfer,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    format_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: FormatArchiveSchema,
    allow_host_transfer: bool | Unset = UNSET,
) -> (
    Any
    | PostAssetsByAssetIdFormatsByFormatIdArchiveResponseDefaultType0
    | PostAssetsByAssetIdFormatsByFormatIdArchiveResponseDefaultType1
    | None
):
    """Archive format


    Required roles:
     - can_archive_formats

    Args:
        asset_id (str):
        format_id (str):
        allow_host_transfer (bool | Unset):
        body (FormatArchiveSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostAssetsByAssetIdFormatsByFormatIdArchiveResponseDefaultType0 | PostAssetsByAssetIdFormatsByFormatIdArchiveResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            format_id=format_id,
            client=client,
            body=body,
            allow_host_transfer=allow_host_transfer,
        )
    ).parsed
