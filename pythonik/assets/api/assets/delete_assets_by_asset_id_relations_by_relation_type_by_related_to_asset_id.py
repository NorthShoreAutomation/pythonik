from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_assets_by_asset_id_relations_by_relation_type_by_related_to_asset_id_response_default import (
    DeleteAssetsByAssetIdRelationsByRelationTypeByRelatedToAssetIdResponseDefault,
)
from ...types import Response


def _get_kwargs(
    asset_id: str,
    relation_type: str,
    related_to_asset_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/assets/{asset_id}/relations/{relation_type}/{related_to_asset_id}/".format(
            asset_id=quote(str(asset_id), safe=""),
            relation_type=quote(str(relation_type), safe=""),
            related_to_asset_id=quote(str(related_to_asset_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any | DeleteAssetsByAssetIdRelationsByRelationTypeByRelatedToAssetIdResponseDefault
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

    response_default = DeleteAssetsByAssetIdRelationsByRelationTypeByRelatedToAssetIdResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | DeleteAssetsByAssetIdRelationsByRelationTypeByRelatedToAssetIdResponseDefault
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    asset_id: str,
    relation_type: str,
    related_to_asset_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any | DeleteAssetsByAssetIdRelationsByRelationTypeByRelatedToAssetIdResponseDefault
]:
    """Delete a particular asset by id


    Required roles:
     - can_delete_asset_relations

    Args:
        asset_id (str):
        relation_type (str):
        related_to_asset_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteAssetsByAssetIdRelationsByRelationTypeByRelatedToAssetIdResponseDefault]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        relation_type=relation_type,
        related_to_asset_id=related_to_asset_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: str,
    relation_type: str,
    related_to_asset_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | DeleteAssetsByAssetIdRelationsByRelationTypeByRelatedToAssetIdResponseDefault
    | None
):
    """Delete a particular asset by id


    Required roles:
     - can_delete_asset_relations

    Args:
        asset_id (str):
        relation_type (str):
        related_to_asset_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteAssetsByAssetIdRelationsByRelationTypeByRelatedToAssetIdResponseDefault
    """

    return sync_detailed(
        asset_id=asset_id,
        relation_type=relation_type,
        related_to_asset_id=related_to_asset_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    relation_type: str,
    related_to_asset_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any | DeleteAssetsByAssetIdRelationsByRelationTypeByRelatedToAssetIdResponseDefault
]:
    """Delete a particular asset by id


    Required roles:
     - can_delete_asset_relations

    Args:
        asset_id (str):
        relation_type (str):
        related_to_asset_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteAssetsByAssetIdRelationsByRelationTypeByRelatedToAssetIdResponseDefault]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        relation_type=relation_type,
        related_to_asset_id=related_to_asset_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    relation_type: str,
    related_to_asset_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | DeleteAssetsByAssetIdRelationsByRelationTypeByRelatedToAssetIdResponseDefault
    | None
):
    """Delete a particular asset by id


    Required roles:
     - can_delete_asset_relations

    Args:
        asset_id (str):
        relation_type (str):
        related_to_asset_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteAssetsByAssetIdRelationsByRelationTypeByRelatedToAssetIdResponseDefault
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            relation_type=relation_type,
            related_to_asset_id=related_to_asset_id,
            client=client,
        )
    ).parsed
