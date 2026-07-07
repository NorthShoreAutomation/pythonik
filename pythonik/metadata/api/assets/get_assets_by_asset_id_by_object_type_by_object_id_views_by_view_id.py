from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_assets_by_asset_id_by_object_type_by_object_id_views_by_view_id_response_default_type_0 import (
    GetAssetsByAssetIdByObjectTypeByObjectIdViewsByViewIdResponseDefaultType0,
)
from ...models.get_assets_by_asset_id_by_object_type_by_object_id_views_by_view_id_response_default_type_1 import (
    GetAssetsByAssetIdByObjectTypeByObjectIdViewsByViewIdResponseDefaultType1,
)
from ...models.metadata_values_schema import MetadataValuesSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    asset_id: str,
    object_type: str,
    object_id: str,
    view_id: str,
    *,
    reencode_values_to_string: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["reencode_values_to_string"] = reencode_values_to_string

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/assets/{asset_id}/{object_type}/{object_id}/views/{view_id}/".format(
            asset_id=quote(str(asset_id), safe=""),
            object_type=quote(str(object_type), safe=""),
            object_id=quote(str(object_id), safe=""),
            view_id=quote(str(view_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetAssetsByAssetIdByObjectTypeByObjectIdViewsByViewIdResponseDefaultType0
    | GetAssetsByAssetIdByObjectTypeByObjectIdViewsByViewIdResponseDefaultType1
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
        GetAssetsByAssetIdByObjectTypeByObjectIdViewsByViewIdResponseDefaultType0
        | GetAssetsByAssetIdByObjectTypeByObjectIdViewsByViewIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = GetAssetsByAssetIdByObjectTypeByObjectIdViewsByViewIdResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = GetAssetsByAssetIdByObjectTypeByObjectIdViewsByViewIdResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetAssetsByAssetIdByObjectTypeByObjectIdViewsByViewIdResponseDefaultType0
    | GetAssetsByAssetIdByObjectTypeByObjectIdViewsByViewIdResponseDefaultType1
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
    view_id: str,
    *,
    client: AuthenticatedClient | Client,
    reencode_values_to_string: bool | Unset = False,
) -> Response[
    Any
    | GetAssetsByAssetIdByObjectTypeByObjectIdViewsByViewIdResponseDefaultType0
    | GetAssetsByAssetIdByObjectTypeByObjectIdViewsByViewIdResponseDefaultType1
    | MetadataValuesSchema
]:
    """Get asset metadata by object type, object ID and view ID


    Required roles:
     - can_read_metadata_values

    Args:
        asset_id (str):
        object_type (str):
        object_id (str):
        view_id (str):
        reencode_values_to_string (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAssetsByAssetIdByObjectTypeByObjectIdViewsByViewIdResponseDefaultType0 | GetAssetsByAssetIdByObjectTypeByObjectIdViewsByViewIdResponseDefaultType1 | MetadataValuesSchema]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        object_type=object_type,
        object_id=object_id,
        view_id=view_id,
        reencode_values_to_string=reencode_values_to_string,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: str,
    object_type: str,
    object_id: str,
    view_id: str,
    *,
    client: AuthenticatedClient | Client,
    reencode_values_to_string: bool | Unset = False,
) -> (
    Any
    | GetAssetsByAssetIdByObjectTypeByObjectIdViewsByViewIdResponseDefaultType0
    | GetAssetsByAssetIdByObjectTypeByObjectIdViewsByViewIdResponseDefaultType1
    | MetadataValuesSchema
    | None
):
    """Get asset metadata by object type, object ID and view ID


    Required roles:
     - can_read_metadata_values

    Args:
        asset_id (str):
        object_type (str):
        object_id (str):
        view_id (str):
        reencode_values_to_string (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAssetsByAssetIdByObjectTypeByObjectIdViewsByViewIdResponseDefaultType0 | GetAssetsByAssetIdByObjectTypeByObjectIdViewsByViewIdResponseDefaultType1 | MetadataValuesSchema
    """

    return sync_detailed(
        asset_id=asset_id,
        object_type=object_type,
        object_id=object_id,
        view_id=view_id,
        client=client,
        reencode_values_to_string=reencode_values_to_string,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    object_type: str,
    object_id: str,
    view_id: str,
    *,
    client: AuthenticatedClient | Client,
    reencode_values_to_string: bool | Unset = False,
) -> Response[
    Any
    | GetAssetsByAssetIdByObjectTypeByObjectIdViewsByViewIdResponseDefaultType0
    | GetAssetsByAssetIdByObjectTypeByObjectIdViewsByViewIdResponseDefaultType1
    | MetadataValuesSchema
]:
    """Get asset metadata by object type, object ID and view ID


    Required roles:
     - can_read_metadata_values

    Args:
        asset_id (str):
        object_type (str):
        object_id (str):
        view_id (str):
        reencode_values_to_string (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAssetsByAssetIdByObjectTypeByObjectIdViewsByViewIdResponseDefaultType0 | GetAssetsByAssetIdByObjectTypeByObjectIdViewsByViewIdResponseDefaultType1 | MetadataValuesSchema]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        object_type=object_type,
        object_id=object_id,
        view_id=view_id,
        reencode_values_to_string=reencode_values_to_string,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    object_type: str,
    object_id: str,
    view_id: str,
    *,
    client: AuthenticatedClient | Client,
    reencode_values_to_string: bool | Unset = False,
) -> (
    Any
    | GetAssetsByAssetIdByObjectTypeByObjectIdViewsByViewIdResponseDefaultType0
    | GetAssetsByAssetIdByObjectTypeByObjectIdViewsByViewIdResponseDefaultType1
    | MetadataValuesSchema
    | None
):
    """Get asset metadata by object type, object ID and view ID


    Required roles:
     - can_read_metadata_values

    Args:
        asset_id (str):
        object_type (str):
        object_id (str):
        view_id (str):
        reencode_values_to_string (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAssetsByAssetIdByObjectTypeByObjectIdViewsByViewIdResponseDefaultType0 | GetAssetsByAssetIdByObjectTypeByObjectIdViewsByViewIdResponseDefaultType1 | MetadataValuesSchema
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            object_type=object_type,
            object_id=object_id,
            view_id=view_id,
            client=client,
            reencode_values_to_string=reencode_values_to_string,
        )
    ).parsed
