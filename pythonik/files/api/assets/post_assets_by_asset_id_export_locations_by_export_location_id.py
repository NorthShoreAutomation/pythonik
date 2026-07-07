from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.asset_export_schema import AssetExportSchema
from ...models.post_assets_by_asset_id_export_locations_by_export_location_id_response_default_type_0 import (
    PostAssetsByAssetIdExportLocationsByExportLocationIdResponseDefaultType0,
)
from ...models.post_assets_by_asset_id_export_locations_by_export_location_id_response_default_type_1 import (
    PostAssetsByAssetIdExportLocationsByExportLocationIdResponseDefaultType1,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    asset_id: str,
    export_location_id: str,
    *,
    body: AssetExportSchema,
    allow_host_transfer: bool | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["allow_host_transfer"] = allow_host_transfer

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/assets/{asset_id}/export_locations/{export_location_id}/".format(
            asset_id=quote(str(asset_id), safe=""),
            export_location_id=quote(str(export_location_id), safe=""),
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
    | PostAssetsByAssetIdExportLocationsByExportLocationIdResponseDefaultType0
    | PostAssetsByAssetIdExportLocationsByExportLocationIdResponseDefaultType1
):
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    def _parse_response_default(
        data: object,
    ) -> (
        PostAssetsByAssetIdExportLocationsByExportLocationIdResponseDefaultType0
        | PostAssetsByAssetIdExportLocationsByExportLocationIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = PostAssetsByAssetIdExportLocationsByExportLocationIdResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = PostAssetsByAssetIdExportLocationsByExportLocationIdResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostAssetsByAssetIdExportLocationsByExportLocationIdResponseDefaultType0
    | PostAssetsByAssetIdExportLocationsByExportLocationIdResponseDefaultType1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    asset_id: str,
    export_location_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AssetExportSchema,
    allow_host_transfer: bool | Unset = UNSET,
) -> Response[
    Any
    | PostAssetsByAssetIdExportLocationsByExportLocationIdResponseDefaultType0
    | PostAssetsByAssetIdExportLocationsByExportLocationIdResponseDefaultType1
]:
    """Export asset to export location


    Required roles:
     - can_write_exports

    Args:
        asset_id (str):
        export_location_id (str):
        allow_host_transfer (bool | Unset):
        body (AssetExportSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostAssetsByAssetIdExportLocationsByExportLocationIdResponseDefaultType0 | PostAssetsByAssetIdExportLocationsByExportLocationIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        export_location_id=export_location_id,
        body=body,
        allow_host_transfer=allow_host_transfer,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: str,
    export_location_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AssetExportSchema,
    allow_host_transfer: bool | Unset = UNSET,
) -> (
    Any
    | PostAssetsByAssetIdExportLocationsByExportLocationIdResponseDefaultType0
    | PostAssetsByAssetIdExportLocationsByExportLocationIdResponseDefaultType1
    | None
):
    """Export asset to export location


    Required roles:
     - can_write_exports

    Args:
        asset_id (str):
        export_location_id (str):
        allow_host_transfer (bool | Unset):
        body (AssetExportSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostAssetsByAssetIdExportLocationsByExportLocationIdResponseDefaultType0 | PostAssetsByAssetIdExportLocationsByExportLocationIdResponseDefaultType1
    """

    return sync_detailed(
        asset_id=asset_id,
        export_location_id=export_location_id,
        client=client,
        body=body,
        allow_host_transfer=allow_host_transfer,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    export_location_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AssetExportSchema,
    allow_host_transfer: bool | Unset = UNSET,
) -> Response[
    Any
    | PostAssetsByAssetIdExportLocationsByExportLocationIdResponseDefaultType0
    | PostAssetsByAssetIdExportLocationsByExportLocationIdResponseDefaultType1
]:
    """Export asset to export location


    Required roles:
     - can_write_exports

    Args:
        asset_id (str):
        export_location_id (str):
        allow_host_transfer (bool | Unset):
        body (AssetExportSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostAssetsByAssetIdExportLocationsByExportLocationIdResponseDefaultType0 | PostAssetsByAssetIdExportLocationsByExportLocationIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        export_location_id=export_location_id,
        body=body,
        allow_host_transfer=allow_host_transfer,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    export_location_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AssetExportSchema,
    allow_host_transfer: bool | Unset = UNSET,
) -> (
    Any
    | PostAssetsByAssetIdExportLocationsByExportLocationIdResponseDefaultType0
    | PostAssetsByAssetIdExportLocationsByExportLocationIdResponseDefaultType1
    | None
):
    """Export asset to export location


    Required roles:
     - can_write_exports

    Args:
        asset_id (str):
        export_location_id (str):
        allow_host_transfer (bool | Unset):
        body (AssetExportSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostAssetsByAssetIdExportLocationsByExportLocationIdResponseDefaultType0 | PostAssetsByAssetIdExportLocationsByExportLocationIdResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            export_location_id=export_location_id,
            client=client,
            body=body,
            allow_host_transfer=allow_host_transfer,
        )
    ).parsed
