from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_assets_relation_types_by_relation_type_response_default import (
    GetAssetsRelationTypesByRelationTypeResponseDefault,
)
from ...models.relation_type_schema import RelationTypeSchema
from ...types import Response


def _get_kwargs(
    relation_type: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/assets/relation_types/{relation_type}/".format(
            relation_type=quote(str(relation_type), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetAssetsRelationTypesByRelationTypeResponseDefault | RelationTypeSchema:
    if response.status_code == 200:
        response_200 = RelationTypeSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = GetAssetsRelationTypesByRelationTypeResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | GetAssetsRelationTypesByRelationTypeResponseDefault | RelationTypeSchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    relation_type: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any | GetAssetsRelationTypesByRelationTypeResponseDefault | RelationTypeSchema
]:
    """Get a relation type


    Required roles:
     - can_read_asset_relations

    Args:
        relation_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAssetsRelationTypesByRelationTypeResponseDefault | RelationTypeSchema]
    """

    kwargs = _get_kwargs(
        relation_type=relation_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    relation_type: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetAssetsRelationTypesByRelationTypeResponseDefault
    | RelationTypeSchema
    | None
):
    """Get a relation type


    Required roles:
     - can_read_asset_relations

    Args:
        relation_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAssetsRelationTypesByRelationTypeResponseDefault | RelationTypeSchema
    """

    return sync_detailed(
        relation_type=relation_type,
        client=client,
    ).parsed


async def asyncio_detailed(
    relation_type: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any | GetAssetsRelationTypesByRelationTypeResponseDefault | RelationTypeSchema
]:
    """Get a relation type


    Required roles:
     - can_read_asset_relations

    Args:
        relation_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAssetsRelationTypesByRelationTypeResponseDefault | RelationTypeSchema]
    """

    kwargs = _get_kwargs(
        relation_type=relation_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    relation_type: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetAssetsRelationTypesByRelationTypeResponseDefault
    | RelationTypeSchema
    | None
):
    """Get a relation type


    Required roles:
     - can_read_asset_relations

    Args:
        relation_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAssetsRelationTypesByRelationTypeResponseDefault | RelationTypeSchema
    """

    return (
        await asyncio_detailed(
            relation_type=relation_type,
            client=client,
        )
    ).parsed
