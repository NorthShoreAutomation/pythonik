from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_assets_relation_types_response_default_type_0 import (
    GetAssetsRelationTypesResponseDefaultType0,
)
from ...models.get_assets_relation_types_response_default_type_1 import (
    GetAssetsRelationTypesResponseDefaultType1,
)
from ...models.relation_types_schema import RelationTypesSchema
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/assets/relation_types/",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetAssetsRelationTypesResponseDefaultType0
    | GetAssetsRelationTypesResponseDefaultType1
    | RelationTypesSchema
):
    if response.status_code == 200:
        response_200 = RelationTypesSchema.from_dict(response.json())

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
        GetAssetsRelationTypesResponseDefaultType0
        | GetAssetsRelationTypesResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetAssetsRelationTypesResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = GetAssetsRelationTypesResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetAssetsRelationTypesResponseDefaultType0
    | GetAssetsRelationTypesResponseDefaultType1
    | RelationTypesSchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetAssetsRelationTypesResponseDefaultType0
    | GetAssetsRelationTypesResponseDefaultType1
    | RelationTypesSchema
]:
    """Create a new asset relation type


    Required roles:
     - can_read_asset_relations

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAssetsRelationTypesResponseDefaultType0 | GetAssetsRelationTypesResponseDefaultType1 | RelationTypesSchema]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetAssetsRelationTypesResponseDefaultType0
    | GetAssetsRelationTypesResponseDefaultType1
    | RelationTypesSchema
    | None
):
    """Create a new asset relation type


    Required roles:
     - can_read_asset_relations

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAssetsRelationTypesResponseDefaultType0 | GetAssetsRelationTypesResponseDefaultType1 | RelationTypesSchema
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetAssetsRelationTypesResponseDefaultType0
    | GetAssetsRelationTypesResponseDefaultType1
    | RelationTypesSchema
]:
    """Create a new asset relation type


    Required roles:
     - can_read_asset_relations

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAssetsRelationTypesResponseDefaultType0 | GetAssetsRelationTypesResponseDefaultType1 | RelationTypesSchema]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetAssetsRelationTypesResponseDefaultType0
    | GetAssetsRelationTypesResponseDefaultType1
    | RelationTypesSchema
    | None
):
    """Create a new asset relation type


    Required roles:
     - can_read_asset_relations

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAssetsRelationTypesResponseDefaultType0 | GetAssetsRelationTypesResponseDefaultType1 | RelationTypesSchema
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
