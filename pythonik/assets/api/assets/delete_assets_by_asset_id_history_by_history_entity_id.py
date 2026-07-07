from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.asset_history_schema import AssetHistorySchema
from ...models.delete_assets_by_asset_id_history_by_history_entity_id_response_default_type_0 import (
    DeleteAssetsByAssetIdHistoryByHistoryEntityIdResponseDefaultType0,
)
from ...models.delete_assets_by_asset_id_history_by_history_entity_id_response_default_type_1 import (
    DeleteAssetsByAssetIdHistoryByHistoryEntityIdResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    asset_id: str,
    history_entity_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/assets/{asset_id}/history/{history_entity_id}/".format(
            asset_id=quote(str(asset_id), safe=""),
            history_entity_id=quote(str(history_entity_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | AssetHistorySchema
    | DeleteAssetsByAssetIdHistoryByHistoryEntityIdResponseDefaultType0
    | DeleteAssetsByAssetIdHistoryByHistoryEntityIdResponseDefaultType1
):
    if response.status_code == 201:
        response_201 = AssetHistorySchema.from_dict(response.json())

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
        DeleteAssetsByAssetIdHistoryByHistoryEntityIdResponseDefaultType0
        | DeleteAssetsByAssetIdHistoryByHistoryEntityIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = DeleteAssetsByAssetIdHistoryByHistoryEntityIdResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            DeleteAssetsByAssetIdHistoryByHistoryEntityIdResponseDefaultType1.from_dict(
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
    | AssetHistorySchema
    | DeleteAssetsByAssetIdHistoryByHistoryEntityIdResponseDefaultType0
    | DeleteAssetsByAssetIdHistoryByHistoryEntityIdResponseDefaultType1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    asset_id: str,
    history_entity_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | AssetHistorySchema
    | DeleteAssetsByAssetIdHistoryByHistoryEntityIdResponseDefaultType0
    | DeleteAssetsByAssetIdHistoryByHistoryEntityIdResponseDefaultType1
]:
    """Deletes an asset history entity


    Required roles:
     - can_delete_assets_history

    Args:
        asset_id (str):
        history_entity_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AssetHistorySchema | DeleteAssetsByAssetIdHistoryByHistoryEntityIdResponseDefaultType0 | DeleteAssetsByAssetIdHistoryByHistoryEntityIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        history_entity_id=history_entity_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: str,
    history_entity_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | AssetHistorySchema
    | DeleteAssetsByAssetIdHistoryByHistoryEntityIdResponseDefaultType0
    | DeleteAssetsByAssetIdHistoryByHistoryEntityIdResponseDefaultType1
    | None
):
    """Deletes an asset history entity


    Required roles:
     - can_delete_assets_history

    Args:
        asset_id (str):
        history_entity_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AssetHistorySchema | DeleteAssetsByAssetIdHistoryByHistoryEntityIdResponseDefaultType0 | DeleteAssetsByAssetIdHistoryByHistoryEntityIdResponseDefaultType1
    """

    return sync_detailed(
        asset_id=asset_id,
        history_entity_id=history_entity_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    history_entity_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | AssetHistorySchema
    | DeleteAssetsByAssetIdHistoryByHistoryEntityIdResponseDefaultType0
    | DeleteAssetsByAssetIdHistoryByHistoryEntityIdResponseDefaultType1
]:
    """Deletes an asset history entity


    Required roles:
     - can_delete_assets_history

    Args:
        asset_id (str):
        history_entity_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AssetHistorySchema | DeleteAssetsByAssetIdHistoryByHistoryEntityIdResponseDefaultType0 | DeleteAssetsByAssetIdHistoryByHistoryEntityIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        history_entity_id=history_entity_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    history_entity_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | AssetHistorySchema
    | DeleteAssetsByAssetIdHistoryByHistoryEntityIdResponseDefaultType0
    | DeleteAssetsByAssetIdHistoryByHistoryEntityIdResponseDefaultType1
    | None
):
    """Deletes an asset history entity


    Required roles:
     - can_delete_assets_history

    Args:
        asset_id (str):
        history_entity_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AssetHistorySchema | DeleteAssetsByAssetIdHistoryByHistoryEntityIdResponseDefaultType0 | DeleteAssetsByAssetIdHistoryByHistoryEntityIdResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            history_entity_id=history_entity_id,
            client=client,
        )
    ).parsed
