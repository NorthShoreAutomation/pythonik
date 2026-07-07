from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.metadata_category_schema import MetadataCategorySchema
from ...models.put_by_object_type_categories_by_name_response_default_type_0 import (
    PutByObjectTypeCategoriesByNameResponseDefaultType0,
)
from ...models.put_by_object_type_categories_by_name_response_default_type_1 import (
    PutByObjectTypeCategoriesByNameResponseDefaultType1,
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
) -> (
    Any
    | MetadataCategorySchema
    | PutByObjectTypeCategoriesByNameResponseDefaultType0
    | PutByObjectTypeCategoriesByNameResponseDefaultType1
):
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

    def _parse_response_default(
        data: object,
    ) -> (
        PutByObjectTypeCategoriesByNameResponseDefaultType0
        | PutByObjectTypeCategoriesByNameResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                PutByObjectTypeCategoriesByNameResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PutByObjectTypeCategoriesByNameResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | MetadataCategorySchema
    | PutByObjectTypeCategoriesByNameResponseDefaultType0
    | PutByObjectTypeCategoriesByNameResponseDefaultType1
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
    Any
    | MetadataCategorySchema
    | PutByObjectTypeCategoriesByNameResponseDefaultType0
    | PutByObjectTypeCategoriesByNameResponseDefaultType1
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
        Response[Any | MetadataCategorySchema | PutByObjectTypeCategoriesByNameResponseDefaultType0 | PutByObjectTypeCategoriesByNameResponseDefaultType1]
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
    Any
    | MetadataCategorySchema
    | PutByObjectTypeCategoriesByNameResponseDefaultType0
    | PutByObjectTypeCategoriesByNameResponseDefaultType1
    | None
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
        Any | MetadataCategorySchema | PutByObjectTypeCategoriesByNameResponseDefaultType0 | PutByObjectTypeCategoriesByNameResponseDefaultType1
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
    Any
    | MetadataCategorySchema
    | PutByObjectTypeCategoriesByNameResponseDefaultType0
    | PutByObjectTypeCategoriesByNameResponseDefaultType1
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
        Response[Any | MetadataCategorySchema | PutByObjectTypeCategoriesByNameResponseDefaultType0 | PutByObjectTypeCategoriesByNameResponseDefaultType1]
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
    Any
    | MetadataCategorySchema
    | PutByObjectTypeCategoriesByNameResponseDefaultType0
    | PutByObjectTypeCategoriesByNameResponseDefaultType1
    | None
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
        Any | MetadataCategorySchema | PutByObjectTypeCategoriesByNameResponseDefaultType0 | PutByObjectTypeCategoriesByNameResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            object_type=object_type,
            name=name,
            client=client,
            body=body,
        )
    ).parsed
