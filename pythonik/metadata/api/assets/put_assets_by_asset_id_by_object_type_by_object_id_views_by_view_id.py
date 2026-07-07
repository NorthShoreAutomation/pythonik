from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.metadata_values_schema import MetadataValuesSchema
from ...models.put_assets_by_asset_id_by_object_type_by_object_id_views_by_view_id_response_default_type_0 import (
    PutAssetsByAssetIdByObjectTypeByObjectIdViewsByViewIdResponseDefaultType0,
)
from ...models.put_assets_by_asset_id_by_object_type_by_object_id_views_by_view_id_response_default_type_1 import (
    PutAssetsByAssetIdByObjectTypeByObjectIdViewsByViewIdResponseDefaultType1,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    asset_id: str,
    object_type: str,
    object_id: str,
    view_id: str,
    *,
    body: MetadataValuesSchema,
    ignore_unchanged: bool | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["ignore_unchanged"] = ignore_unchanged

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/assets/{asset_id}/{object_type}/{object_id}/views/{view_id}/".format(
            asset_id=quote(str(asset_id), safe=""),
            object_type=quote(str(object_type), safe=""),
            object_id=quote(str(object_id), safe=""),
            view_id=quote(str(view_id), safe=""),
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
    | MetadataValuesSchema
    | PutAssetsByAssetIdByObjectTypeByObjectIdViewsByViewIdResponseDefaultType0
    | PutAssetsByAssetIdByObjectTypeByObjectIdViewsByViewIdResponseDefaultType1
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
        PutAssetsByAssetIdByObjectTypeByObjectIdViewsByViewIdResponseDefaultType0
        | PutAssetsByAssetIdByObjectTypeByObjectIdViewsByViewIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = PutAssetsByAssetIdByObjectTypeByObjectIdViewsByViewIdResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = PutAssetsByAssetIdByObjectTypeByObjectIdViewsByViewIdResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | MetadataValuesSchema
    | PutAssetsByAssetIdByObjectTypeByObjectIdViewsByViewIdResponseDefaultType0
    | PutAssetsByAssetIdByObjectTypeByObjectIdViewsByViewIdResponseDefaultType1
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
    body: MetadataValuesSchema,
    ignore_unchanged: bool | Unset = UNSET,
) -> Response[
    Any
    | MetadataValuesSchema
    | PutAssetsByAssetIdByObjectTypeByObjectIdViewsByViewIdResponseDefaultType0
    | PutAssetsByAssetIdByObjectTypeByObjectIdViewsByViewIdResponseDefaultType1
]:
    """Edit view metadata values for sub-objects of an asset (Such as segments)


    Required roles:
     - can_write_metadata_values

    Args:
        asset_id (str):
        object_type (str):
        object_id (str):
        view_id (str):
        ignore_unchanged (bool | Unset):
        body (MetadataValuesSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | MetadataValuesSchema | PutAssetsByAssetIdByObjectTypeByObjectIdViewsByViewIdResponseDefaultType0 | PutAssetsByAssetIdByObjectTypeByObjectIdViewsByViewIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        object_type=object_type,
        object_id=object_id,
        view_id=view_id,
        body=body,
        ignore_unchanged=ignore_unchanged,
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
    body: MetadataValuesSchema,
    ignore_unchanged: bool | Unset = UNSET,
) -> (
    Any
    | MetadataValuesSchema
    | PutAssetsByAssetIdByObjectTypeByObjectIdViewsByViewIdResponseDefaultType0
    | PutAssetsByAssetIdByObjectTypeByObjectIdViewsByViewIdResponseDefaultType1
    | None
):
    """Edit view metadata values for sub-objects of an asset (Such as segments)


    Required roles:
     - can_write_metadata_values

    Args:
        asset_id (str):
        object_type (str):
        object_id (str):
        view_id (str):
        ignore_unchanged (bool | Unset):
        body (MetadataValuesSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | MetadataValuesSchema | PutAssetsByAssetIdByObjectTypeByObjectIdViewsByViewIdResponseDefaultType0 | PutAssetsByAssetIdByObjectTypeByObjectIdViewsByViewIdResponseDefaultType1
    """

    return sync_detailed(
        asset_id=asset_id,
        object_type=object_type,
        object_id=object_id,
        view_id=view_id,
        client=client,
        body=body,
        ignore_unchanged=ignore_unchanged,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    object_type: str,
    object_id: str,
    view_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: MetadataValuesSchema,
    ignore_unchanged: bool | Unset = UNSET,
) -> Response[
    Any
    | MetadataValuesSchema
    | PutAssetsByAssetIdByObjectTypeByObjectIdViewsByViewIdResponseDefaultType0
    | PutAssetsByAssetIdByObjectTypeByObjectIdViewsByViewIdResponseDefaultType1
]:
    """Edit view metadata values for sub-objects of an asset (Such as segments)


    Required roles:
     - can_write_metadata_values

    Args:
        asset_id (str):
        object_type (str):
        object_id (str):
        view_id (str):
        ignore_unchanged (bool | Unset):
        body (MetadataValuesSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | MetadataValuesSchema | PutAssetsByAssetIdByObjectTypeByObjectIdViewsByViewIdResponseDefaultType0 | PutAssetsByAssetIdByObjectTypeByObjectIdViewsByViewIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        object_type=object_type,
        object_id=object_id,
        view_id=view_id,
        body=body,
        ignore_unchanged=ignore_unchanged,
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
    body: MetadataValuesSchema,
    ignore_unchanged: bool | Unset = UNSET,
) -> (
    Any
    | MetadataValuesSchema
    | PutAssetsByAssetIdByObjectTypeByObjectIdViewsByViewIdResponseDefaultType0
    | PutAssetsByAssetIdByObjectTypeByObjectIdViewsByViewIdResponseDefaultType1
    | None
):
    """Edit view metadata values for sub-objects of an asset (Such as segments)


    Required roles:
     - can_write_metadata_values

    Args:
        asset_id (str):
        object_type (str):
        object_id (str):
        view_id (str):
        ignore_unchanged (bool | Unset):
        body (MetadataValuesSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | MetadataValuesSchema | PutAssetsByAssetIdByObjectTypeByObjectIdViewsByViewIdResponseDefaultType0 | PutAssetsByAssetIdByObjectTypeByObjectIdViewsByViewIdResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            object_type=object_type,
            object_id=object_id,
            view_id=view_id,
            client=client,
            body=body,
            ignore_unchanged=ignore_unchanged,
        )
    ).parsed
