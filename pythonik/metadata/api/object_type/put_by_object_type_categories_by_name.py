from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.metadata_category_schema import MetadataCategorySchema
from ...models.put_by_object_type_categories_by_name_response_default import (
    PutByObjectTypeCategoriesByNameResponseDefault,
)
from ...types import Response


def _get_kwargs(
    object_type: str,
    name: str,
    *,
    body: MetadataCategorySchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/{object_type}/categories/{name}/".format(
            object_type=quote(str(object_type), safe=""),
            name=quote(str(name), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | MetadataCategorySchema | PutByObjectTypeCategoriesByNameResponseDefault:
    if response.status_code == 200:
        response_200 = MetadataCategorySchema.from_dict(response.json())

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

    response_default = PutByObjectTypeCategoriesByNameResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | MetadataCategorySchema | PutByObjectTypeCategoriesByNameResponseDefault
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    object_type: str,
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: MetadataCategorySchema,
) -> Response[
    Any | MetadataCategorySchema | PutByObjectTypeCategoriesByNameResponseDefault
]:
    """Edit metadata category for an object type


    Required roles:
     - can_write_metadata_categories

    Args:
        object_type (str):
        name (str):
        body (MetadataCategorySchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | MetadataCategorySchema | PutByObjectTypeCategoriesByNameResponseDefault]
    """

    kwargs = _get_kwargs(
        object_type=object_type,
        name=name,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    object_type: str,
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: MetadataCategorySchema,
) -> (
    Any | MetadataCategorySchema | PutByObjectTypeCategoriesByNameResponseDefault | None
):
    """Edit metadata category for an object type


    Required roles:
     - can_write_metadata_categories

    Args:
        object_type (str):
        name (str):
        body (MetadataCategorySchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | MetadataCategorySchema | PutByObjectTypeCategoriesByNameResponseDefault
    """

    return sync_detailed(
        object_type=object_type,
        name=name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    object_type: str,
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: MetadataCategorySchema,
) -> Response[
    Any | MetadataCategorySchema | PutByObjectTypeCategoriesByNameResponseDefault
]:
    """Edit metadata category for an object type


    Required roles:
     - can_write_metadata_categories

    Args:
        object_type (str):
        name (str):
        body (MetadataCategorySchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | MetadataCategorySchema | PutByObjectTypeCategoriesByNameResponseDefault]
    """

    kwargs = _get_kwargs(
        object_type=object_type,
        name=name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    object_type: str,
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: MetadataCategorySchema,
) -> (
    Any | MetadataCategorySchema | PutByObjectTypeCategoriesByNameResponseDefault | None
):
    """Edit metadata category for an object type


    Required roles:
     - can_write_metadata_categories

    Args:
        object_type (str):
        name (str):
        body (MetadataCategorySchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | MetadataCategorySchema | PutByObjectTypeCategoriesByNameResponseDefault
    """

    return (
        await asyncio_detailed(
            object_type=object_type,
            name=name,
            client=client,
            body=body,
        )
    ).parsed
