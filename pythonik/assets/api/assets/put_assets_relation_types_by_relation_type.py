from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.put_assets_relation_types_by_relation_type_response_default_type_0 import (
    PutAssetsRelationTypesByRelationTypeResponseDefaultType0,
)
from ...models.put_assets_relation_types_by_relation_type_response_default_type_1 import (
    PutAssetsRelationTypesByRelationTypeResponseDefaultType1,
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
        "method": "put",
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
) -> (
    Any
    | PutAssetsRelationTypesByRelationTypeResponseDefaultType0
    | PutAssetsRelationTypesByRelationTypeResponseDefaultType1
    | RelationTypeSchema
):
    if response.status_code == 200:
        response_200 = RelationTypeSchema.from_dict(response.json())

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
        PutAssetsRelationTypesByRelationTypeResponseDefaultType0
        | PutAssetsRelationTypesByRelationTypeResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                PutAssetsRelationTypesByRelationTypeResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PutAssetsRelationTypesByRelationTypeResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PutAssetsRelationTypesByRelationTypeResponseDefaultType0
    | PutAssetsRelationTypesByRelationTypeResponseDefaultType1
    | RelationTypeSchema
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
    Any
    | PutAssetsRelationTypesByRelationTypeResponseDefaultType0
    | PutAssetsRelationTypesByRelationTypeResponseDefaultType1
    | RelationTypeSchema
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
        Response[Any | PutAssetsRelationTypesByRelationTypeResponseDefaultType0 | PutAssetsRelationTypesByRelationTypeResponseDefaultType1 | RelationTypeSchema]
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
    | PutAssetsRelationTypesByRelationTypeResponseDefaultType0
    | PutAssetsRelationTypesByRelationTypeResponseDefaultType1
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
        Any | PutAssetsRelationTypesByRelationTypeResponseDefaultType0 | PutAssetsRelationTypesByRelationTypeResponseDefaultType1 | RelationTypeSchema
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
    Any
    | PutAssetsRelationTypesByRelationTypeResponseDefaultType0
    | PutAssetsRelationTypesByRelationTypeResponseDefaultType1
    | RelationTypeSchema
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
        Response[Any | PutAssetsRelationTypesByRelationTypeResponseDefaultType0 | PutAssetsRelationTypesByRelationTypeResponseDefaultType1 | RelationTypeSchema]
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
    | PutAssetsRelationTypesByRelationTypeResponseDefaultType0
    | PutAssetsRelationTypesByRelationTypeResponseDefaultType1
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
        Any | PutAssetsRelationTypesByRelationTypeResponseDefaultType0 | PutAssetsRelationTypesByRelationTypeResponseDefaultType1 | RelationTypeSchema
    """

    return (
        await asyncio_detailed(
            relation_type=relation_type,
            client=client,
            body=body,
        )
    ).parsed
