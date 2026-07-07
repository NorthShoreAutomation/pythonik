from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_assets_relation_types_by_relation_type_response_default_type_0 import (
    DeleteAssetsRelationTypesByRelationTypeResponseDefaultType0,
)
from ...models.delete_assets_relation_types_by_relation_type_response_default_type_1 import (
    DeleteAssetsRelationTypesByRelationTypeResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    relation_type: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/assets/relation_types/{relation_type}/".format(
            relation_type=quote(str(relation_type), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | DeleteAssetsRelationTypesByRelationTypeResponseDefaultType0
    | DeleteAssetsRelationTypesByRelationTypeResponseDefaultType1
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

    def _parse_response_default(
        data: object,
    ) -> (
        DeleteAssetsRelationTypesByRelationTypeResponseDefaultType0
        | DeleteAssetsRelationTypesByRelationTypeResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                DeleteAssetsRelationTypesByRelationTypeResponseDefaultType0.from_dict(
                    data
                )
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            DeleteAssetsRelationTypesByRelationTypeResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | DeleteAssetsRelationTypesByRelationTypeResponseDefaultType0
    | DeleteAssetsRelationTypesByRelationTypeResponseDefaultType1
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
    Any
    | DeleteAssetsRelationTypesByRelationTypeResponseDefaultType0
    | DeleteAssetsRelationTypesByRelationTypeResponseDefaultType1
]:
    """Delete an asset relation type


    Required roles:
     - can_delete_asset_relation_types

    Args:
        relation_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteAssetsRelationTypesByRelationTypeResponseDefaultType0 | DeleteAssetsRelationTypesByRelationTypeResponseDefaultType1]
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
    | DeleteAssetsRelationTypesByRelationTypeResponseDefaultType0
    | DeleteAssetsRelationTypesByRelationTypeResponseDefaultType1
    | None
):
    """Delete an asset relation type


    Required roles:
     - can_delete_asset_relation_types

    Args:
        relation_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteAssetsRelationTypesByRelationTypeResponseDefaultType0 | DeleteAssetsRelationTypesByRelationTypeResponseDefaultType1
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
    Any
    | DeleteAssetsRelationTypesByRelationTypeResponseDefaultType0
    | DeleteAssetsRelationTypesByRelationTypeResponseDefaultType1
]:
    """Delete an asset relation type


    Required roles:
     - can_delete_asset_relation_types

    Args:
        relation_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteAssetsRelationTypesByRelationTypeResponseDefaultType0 | DeleteAssetsRelationTypesByRelationTypeResponseDefaultType1]
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
    | DeleteAssetsRelationTypesByRelationTypeResponseDefaultType0
    | DeleteAssetsRelationTypesByRelationTypeResponseDefaultType1
    | None
):
    """Delete an asset relation type


    Required roles:
     - can_delete_asset_relation_types

    Args:
        relation_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteAssetsRelationTypesByRelationTypeResponseDefaultType0 | DeleteAssetsRelationTypesByRelationTypeResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            relation_type=relation_type,
            client=client,
        )
    ).parsed
