from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_assets_by_asset_id_relations_by_relation_type_by_related_to_asset_id_response_default_type_0 import (
    PostAssetsByAssetIdRelationsByRelationTypeByRelatedToAssetIdResponseDefaultType0,
)
from ...models.post_assets_by_asset_id_relations_by_relation_type_by_related_to_asset_id_response_default_type_1 import (
    PostAssetsByAssetIdRelationsByRelationTypeByRelatedToAssetIdResponseDefaultType1,
)
from ...models.relation_schema import RelationSchema
from ...types import Response


def _get_kwargs(
    asset_id: str,
    relation_type: str,
    related_to_asset_id: str,
    *,
    body: RelationSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/assets/{asset_id}/relations/{relation_type}/{related_to_asset_id}/".format(
            asset_id=quote(str(asset_id), safe=""),
            relation_type=quote(str(relation_type), safe=""),
            related_to_asset_id=quote(str(related_to_asset_id), safe=""),
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
    | PostAssetsByAssetIdRelationsByRelationTypeByRelatedToAssetIdResponseDefaultType0
    | PostAssetsByAssetIdRelationsByRelationTypeByRelatedToAssetIdResponseDefaultType1
    | RelationSchema
):
    if response.status_code == 200:
        response_200 = RelationSchema.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = RelationSchema.from_dict(response.json())

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
        PostAssetsByAssetIdRelationsByRelationTypeByRelatedToAssetIdResponseDefaultType0
        | PostAssetsByAssetIdRelationsByRelationTypeByRelatedToAssetIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = PostAssetsByAssetIdRelationsByRelationTypeByRelatedToAssetIdResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = PostAssetsByAssetIdRelationsByRelationTypeByRelatedToAssetIdResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostAssetsByAssetIdRelationsByRelationTypeByRelatedToAssetIdResponseDefaultType0
    | PostAssetsByAssetIdRelationsByRelationTypeByRelatedToAssetIdResponseDefaultType1
    | RelationSchema
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
    body: RelationSchema,
) -> Response[
    Any
    | PostAssetsByAssetIdRelationsByRelationTypeByRelatedToAssetIdResponseDefaultType0
    | PostAssetsByAssetIdRelationsByRelationTypeByRelatedToAssetIdResponseDefaultType1
    | RelationSchema
]:
    """Create a new asset relation


    Required roles:
     - can_create_asset_relations

    Args:
        asset_id (str):
        relation_type (str):
        related_to_asset_id (str):
        body (RelationSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostAssetsByAssetIdRelationsByRelationTypeByRelatedToAssetIdResponseDefaultType0 | PostAssetsByAssetIdRelationsByRelationTypeByRelatedToAssetIdResponseDefaultType1 | RelationSchema]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        relation_type=relation_type,
        related_to_asset_id=related_to_asset_id,
        body=body,
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
    body: RelationSchema,
) -> (
    Any
    | PostAssetsByAssetIdRelationsByRelationTypeByRelatedToAssetIdResponseDefaultType0
    | PostAssetsByAssetIdRelationsByRelationTypeByRelatedToAssetIdResponseDefaultType1
    | RelationSchema
    | None
):
    """Create a new asset relation


    Required roles:
     - can_create_asset_relations

    Args:
        asset_id (str):
        relation_type (str):
        related_to_asset_id (str):
        body (RelationSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostAssetsByAssetIdRelationsByRelationTypeByRelatedToAssetIdResponseDefaultType0 | PostAssetsByAssetIdRelationsByRelationTypeByRelatedToAssetIdResponseDefaultType1 | RelationSchema
    """

    return sync_detailed(
        asset_id=asset_id,
        relation_type=relation_type,
        related_to_asset_id=related_to_asset_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    relation_type: str,
    related_to_asset_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RelationSchema,
) -> Response[
    Any
    | PostAssetsByAssetIdRelationsByRelationTypeByRelatedToAssetIdResponseDefaultType0
    | PostAssetsByAssetIdRelationsByRelationTypeByRelatedToAssetIdResponseDefaultType1
    | RelationSchema
]:
    """Create a new asset relation


    Required roles:
     - can_create_asset_relations

    Args:
        asset_id (str):
        relation_type (str):
        related_to_asset_id (str):
        body (RelationSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostAssetsByAssetIdRelationsByRelationTypeByRelatedToAssetIdResponseDefaultType0 | PostAssetsByAssetIdRelationsByRelationTypeByRelatedToAssetIdResponseDefaultType1 | RelationSchema]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        relation_type=relation_type,
        related_to_asset_id=related_to_asset_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    relation_type: str,
    related_to_asset_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RelationSchema,
) -> (
    Any
    | PostAssetsByAssetIdRelationsByRelationTypeByRelatedToAssetIdResponseDefaultType0
    | PostAssetsByAssetIdRelationsByRelationTypeByRelatedToAssetIdResponseDefaultType1
    | RelationSchema
    | None
):
    """Create a new asset relation


    Required roles:
     - can_create_asset_relations

    Args:
        asset_id (str):
        relation_type (str):
        related_to_asset_id (str):
        body (RelationSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostAssetsByAssetIdRelationsByRelationTypeByRelatedToAssetIdResponseDefaultType0 | PostAssetsByAssetIdRelationsByRelationTypeByRelatedToAssetIdResponseDefaultType1 | RelationSchema
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            relation_type=relation_type,
            related_to_asset_id=related_to_asset_id,
            client=client,
            body=body,
        )
    ).parsed
