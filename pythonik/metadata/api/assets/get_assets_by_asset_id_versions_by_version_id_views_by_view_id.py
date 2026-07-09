from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_assets_by_asset_id_versions_by_version_id_views_by_view_id_response_default import (
    GetAssetsByAssetIdVersionsByVersionIdViewsByViewIdResponseDefault,
)
from ...models.metadata_values_schema import MetadataValuesSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    asset_id: str,
    version_id: str,
    view_id: str,
    *,
    reencode_values_to_string: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["reencode_values_to_string"] = reencode_values_to_string

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/assets/{asset_id}/versions/{version_id}/views/{view_id}/".format(
            asset_id=quote(str(asset_id), safe=""),
            version_id=quote(str(version_id), safe=""),
            view_id=quote(str(view_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetAssetsByAssetIdVersionsByVersionIdViewsByViewIdResponseDefault
    | MetadataValuesSchema
):
    if response.status_code == 200:
        response_200 = MetadataValuesSchema.from_dict(response.json())

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
        GetAssetsByAssetIdVersionsByVersionIdViewsByViewIdResponseDefault.from_dict(
            response.json()
        )
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetAssetsByAssetIdVersionsByVersionIdViewsByViewIdResponseDefault
    | MetadataValuesSchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    asset_id: str,
    version_id: str,
    view_id: str,
    *,
    client: AuthenticatedClient | Client,
    reencode_values_to_string: bool | Unset = UNSET,
) -> Response[
    Any
    | GetAssetsByAssetIdVersionsByVersionIdViewsByViewIdResponseDefault
    | MetadataValuesSchema
]:
    """Get object metadata by object type, object ID, version ID and view ID


    Required roles:
     - can_read_metadata_values

    Args:
        asset_id (str):
        version_id (str):
        view_id (str):
        reencode_values_to_string (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAssetsByAssetIdVersionsByVersionIdViewsByViewIdResponseDefault | MetadataValuesSchema]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        version_id=version_id,
        view_id=view_id,
        reencode_values_to_string=reencode_values_to_string,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: str,
    version_id: str,
    view_id: str,
    *,
    client: AuthenticatedClient | Client,
    reencode_values_to_string: bool | Unset = UNSET,
) -> (
    Any
    | GetAssetsByAssetIdVersionsByVersionIdViewsByViewIdResponseDefault
    | MetadataValuesSchema
    | None
):
    """Get object metadata by object type, object ID, version ID and view ID


    Required roles:
     - can_read_metadata_values

    Args:
        asset_id (str):
        version_id (str):
        view_id (str):
        reencode_values_to_string (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAssetsByAssetIdVersionsByVersionIdViewsByViewIdResponseDefault | MetadataValuesSchema
    """

    return sync_detailed(
        asset_id=asset_id,
        version_id=version_id,
        view_id=view_id,
        client=client,
        reencode_values_to_string=reencode_values_to_string,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    version_id: str,
    view_id: str,
    *,
    client: AuthenticatedClient | Client,
    reencode_values_to_string: bool | Unset = UNSET,
) -> Response[
    Any
    | GetAssetsByAssetIdVersionsByVersionIdViewsByViewIdResponseDefault
    | MetadataValuesSchema
]:
    """Get object metadata by object type, object ID, version ID and view ID


    Required roles:
     - can_read_metadata_values

    Args:
        asset_id (str):
        version_id (str):
        view_id (str):
        reencode_values_to_string (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAssetsByAssetIdVersionsByVersionIdViewsByViewIdResponseDefault | MetadataValuesSchema]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        version_id=version_id,
        view_id=view_id,
        reencode_values_to_string=reencode_values_to_string,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    version_id: str,
    view_id: str,
    *,
    client: AuthenticatedClient | Client,
    reencode_values_to_string: bool | Unset = UNSET,
) -> (
    Any
    | GetAssetsByAssetIdVersionsByVersionIdViewsByViewIdResponseDefault
    | MetadataValuesSchema
    | None
):
    """Get object metadata by object type, object ID, version ID and view ID


    Required roles:
     - can_read_metadata_values

    Args:
        asset_id (str):
        version_id (str):
        view_id (str):
        reencode_values_to_string (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAssetsByAssetIdVersionsByVersionIdViewsByViewIdResponseDefault | MetadataValuesSchema
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            version_id=version_id,
            view_id=view_id,
            client=client,
            reencode_values_to_string=reencode_values_to_string,
        )
    ).parsed
