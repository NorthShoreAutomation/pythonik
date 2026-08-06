from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.patch_assets_relation_types_by_relation_type_response_default import (
    PatchAssetsRelationTypesByRelationTypeResponseDefault,
)
from ...models.relation_type_schema import RelationTypeSchema
from ...types import Response


def _get_kwargs(
    relation_type: str,
    *,
    body: RelationTypeSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/assets/relation_types/{relation_type}/".format(
            relation_type=quote(str(relation_type), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PatchAssetsRelationTypesByRelationTypeResponseDefault | RelationTypeSchema:
    if response.status_code == 200:
        response_200 = RelationTypeSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = PatchAssetsRelationTypesByRelationTypeResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | PatchAssetsRelationTypesByRelationTypeResponseDefault | RelationTypeSchema
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
    body: RelationTypeSchema,
) -> Response[
    Any | PatchAssetsRelationTypesByRelationTypeResponseDefault | RelationTypeSchema
]:
    """Update an asset relation type


    Required roles:
     - can_write_asset_relation_types

    Args:
        relation_type (str):
        body (RelationTypeSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PatchAssetsRelationTypesByRelationTypeResponseDefault | RelationTypeSchema]
    """

    kwargs = _get_kwargs(
        relation_type=relation_type,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    relation_type: str,
    *,
    client: AuthenticatedClient | Client,
    body: RelationTypeSchema,
) -> (
    Any
    | PatchAssetsRelationTypesByRelationTypeResponseDefault
    | RelationTypeSchema
    | None
):
    """Update an asset relation type


    Required roles:
     - can_write_asset_relation_types

    Args:
        relation_type (str):
        body (RelationTypeSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PatchAssetsRelationTypesByRelationTypeResponseDefault | RelationTypeSchema
    """

    return sync_detailed(
        relation_type=relation_type,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    relation_type: str,
    *,
    client: AuthenticatedClient | Client,
    body: RelationTypeSchema,
) -> Response[
    Any | PatchAssetsRelationTypesByRelationTypeResponseDefault | RelationTypeSchema
]:
    """Update an asset relation type


    Required roles:
     - can_write_asset_relation_types

    Args:
        relation_type (str):
        body (RelationTypeSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PatchAssetsRelationTypesByRelationTypeResponseDefault | RelationTypeSchema]
    """

    kwargs = _get_kwargs(
        relation_type=relation_type,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    relation_type: str,
    *,
    client: AuthenticatedClient | Client,
    body: RelationTypeSchema,
) -> (
    Any
    | PatchAssetsRelationTypesByRelationTypeResponseDefault
    | RelationTypeSchema
    | None
):
    """Update an asset relation type


    Required roles:
     - can_write_asset_relation_types

    Args:
        relation_type (str):
        body (RelationTypeSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PatchAssetsRelationTypesByRelationTypeResponseDefault | RelationTypeSchema
    """

    return (
        await asyncio_detailed(
            relation_type=relation_type,
            client=client,
            body=body,
        )
    ).parsed
