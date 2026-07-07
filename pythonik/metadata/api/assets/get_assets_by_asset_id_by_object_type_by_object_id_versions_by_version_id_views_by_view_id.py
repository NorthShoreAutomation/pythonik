from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_assets_by_asset_id_by_object_type_by_object_id_versions_by_version_id_views_by_view_id_response_default_type_0 import (
    GetAssetsByAssetIdByObjectTypeByObjectIdVersionsByVersionIdViewsByViewIdResponseDefaultType0,
)
from ...models.get_assets_by_asset_id_by_object_type_by_object_id_versions_by_version_id_views_by_view_id_response_default_type_1 import (
    GetAssetsByAssetIdByObjectTypeByObjectIdVersionsByVersionIdViewsByViewIdResponseDefaultType1,
)
from ...models.metadata_values_schema import MetadataValuesSchema
from ...types import Response


def _get_kwargs(
    asset_id: str,
    object_type: str,
    object_id: str,
    version_id: str,
    view_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/assets/{asset_id}/{object_type}/{object_id}/versions/{version_id}/views/{view_id}/".format(
            asset_id=quote(str(asset_id), safe=""),
            object_type=quote(str(object_type), safe=""),
            object_id=quote(str(object_id), safe=""),
            version_id=quote(str(version_id), safe=""),
            view_id=quote(str(view_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetAssetsByAssetIdByObjectTypeByObjectIdVersionsByVersionIdViewsByViewIdResponseDefaultType0
    | GetAssetsByAssetIdByObjectTypeByObjectIdVersionsByVersionIdViewsByViewIdResponseDefaultType1
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

    def _parse_response_default(
        data: object,
    ) -> (
        GetAssetsByAssetIdByObjectTypeByObjectIdVersionsByVersionIdViewsByViewIdResponseDefaultType0
        | GetAssetsByAssetIdByObjectTypeByObjectIdVersionsByVersionIdViewsByViewIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = GetAssetsByAssetIdByObjectTypeByObjectIdVersionsByVersionIdViewsByViewIdResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = GetAssetsByAssetIdByObjectTypeByObjectIdVersionsByVersionIdViewsByViewIdResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetAssetsByAssetIdByObjectTypeByObjectIdVersionsByVersionIdViewsByViewIdResponseDefaultType0
    | GetAssetsByAssetIdByObjectTypeByObjectIdVersionsByVersionIdViewsByViewIdResponseDefaultType1
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
    object_type: str,
    object_id: str,
    version_id: str,
    view_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetAssetsByAssetIdByObjectTypeByObjectIdVersionsByVersionIdViewsByViewIdResponseDefaultType0
    | GetAssetsByAssetIdByObjectTypeByObjectIdVersionsByVersionIdViewsByViewIdResponseDefaultType1
    | MetadataValuesSchema
]:
    """Get asset metadata by object type, object ID, version ID and view ID


    Required roles:
     - can_read_metadata_values

    Args:
        asset_id (str):
        object_type (str):
        object_id (str):
        version_id (str):
        view_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAssetsByAssetIdByObjectTypeByObjectIdVersionsByVersionIdViewsByViewIdResponseDefaultType0 | GetAssetsByAssetIdByObjectTypeByObjectIdVersionsByVersionIdViewsByViewIdResponseDefaultType1 | MetadataValuesSchema]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        object_type=object_type,
        object_id=object_id,
        version_id=version_id,
        view_id=view_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: str,
    object_type: str,
    object_id: str,
    version_id: str,
    view_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetAssetsByAssetIdByObjectTypeByObjectIdVersionsByVersionIdViewsByViewIdResponseDefaultType0
    | GetAssetsByAssetIdByObjectTypeByObjectIdVersionsByVersionIdViewsByViewIdResponseDefaultType1
    | MetadataValuesSchema
    | None
):
    """Get asset metadata by object type, object ID, version ID and view ID


    Required roles:
     - can_read_metadata_values

    Args:
        asset_id (str):
        object_type (str):
        object_id (str):
        version_id (str):
        view_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAssetsByAssetIdByObjectTypeByObjectIdVersionsByVersionIdViewsByViewIdResponseDefaultType0 | GetAssetsByAssetIdByObjectTypeByObjectIdVersionsByVersionIdViewsByViewIdResponseDefaultType1 | MetadataValuesSchema
    """

    return sync_detailed(
        asset_id=asset_id,
        object_type=object_type,
        object_id=object_id,
        version_id=version_id,
        view_id=view_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    object_type: str,
    object_id: str,
    version_id: str,
    view_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetAssetsByAssetIdByObjectTypeByObjectIdVersionsByVersionIdViewsByViewIdResponseDefaultType0
    | GetAssetsByAssetIdByObjectTypeByObjectIdVersionsByVersionIdViewsByViewIdResponseDefaultType1
    | MetadataValuesSchema
]:
    """Get asset metadata by object type, object ID, version ID and view ID


    Required roles:
     - can_read_metadata_values

    Args:
        asset_id (str):
        object_type (str):
        object_id (str):
        version_id (str):
        view_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAssetsByAssetIdByObjectTypeByObjectIdVersionsByVersionIdViewsByViewIdResponseDefaultType0 | GetAssetsByAssetIdByObjectTypeByObjectIdVersionsByVersionIdViewsByViewIdResponseDefaultType1 | MetadataValuesSchema]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        object_type=object_type,
        object_id=object_id,
        version_id=version_id,
        view_id=view_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    object_type: str,
    object_id: str,
    version_id: str,
    view_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetAssetsByAssetIdByObjectTypeByObjectIdVersionsByVersionIdViewsByViewIdResponseDefaultType0
    | GetAssetsByAssetIdByObjectTypeByObjectIdVersionsByVersionIdViewsByViewIdResponseDefaultType1
    | MetadataValuesSchema
    | None
):
    """Get asset metadata by object type, object ID, version ID and view ID


    Required roles:
     - can_read_metadata_values

    Args:
        asset_id (str):
        object_type (str):
        object_id (str):
        version_id (str):
        view_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAssetsByAssetIdByObjectTypeByObjectIdVersionsByVersionIdViewsByViewIdResponseDefaultType0 | GetAssetsByAssetIdByObjectTypeByObjectIdVersionsByVersionIdViewsByViewIdResponseDefaultType1 | MetadataValuesSchema
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            object_type=object_type,
            object_id=object_id,
            version_id=version_id,
            view_id=view_id,
            client=client,
        )
    ).parsed
