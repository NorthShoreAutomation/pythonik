from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.metadata_category_schema import MetadataCategorySchema
from ...models.post_by_object_type_categories_response_default_type_0 import (
    PostByObjectTypeCategoriesResponseDefaultType0,
)
from ...models.post_by_object_type_categories_response_default_type_1 import (
    PostByObjectTypeCategoriesResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    object_type: str,
    *,
    body: MetadataCategorySchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/{object_type}/categories/".format(
            object_type=quote(str(object_type), safe=""),
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
    | PostByObjectTypeCategoriesResponseDefaultType0
    | PostByObjectTypeCategoriesResponseDefaultType1
):
    if response.status_code == 201:
        response_201 = MetadataCategorySchema.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409

    def _parse_response_default(
        data: object,
    ) -> (
        PostByObjectTypeCategoriesResponseDefaultType0
        | PostByObjectTypeCategoriesResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                PostByObjectTypeCategoriesResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PostByObjectTypeCategoriesResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | MetadataCategorySchema
    | PostByObjectTypeCategoriesResponseDefaultType0
    | PostByObjectTypeCategoriesResponseDefaultType1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    object_type: str,
    *,
    client: AuthenticatedClient | Client,
    body: MetadataCategorySchema,
) -> Response[
    Any
    | MetadataCategorySchema
    | PostByObjectTypeCategoriesResponseDefaultType0
    | PostByObjectTypeCategoriesResponseDefaultType1
]:
    """Add a metadata category for an object type


    Required roles:
     - can_write_metadata_categories

    Args:
        object_type (str):
        body (MetadataCategorySchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | MetadataCategorySchema | PostByObjectTypeCategoriesResponseDefaultType0 | PostByObjectTypeCategoriesResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        object_type=object_type,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    object_type: str,
    *,
    client: AuthenticatedClient | Client,
    body: MetadataCategorySchema,
) -> (
    Any
    | MetadataCategorySchema
    | PostByObjectTypeCategoriesResponseDefaultType0
    | PostByObjectTypeCategoriesResponseDefaultType1
    | None
):
    """Add a metadata category for an object type


    Required roles:
     - can_write_metadata_categories

    Args:
        object_type (str):
        body (MetadataCategorySchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | MetadataCategorySchema | PostByObjectTypeCategoriesResponseDefaultType0 | PostByObjectTypeCategoriesResponseDefaultType1
    """

    return sync_detailed(
        object_type=object_type,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    object_type: str,
    *,
    client: AuthenticatedClient | Client,
    body: MetadataCategorySchema,
) -> Response[
    Any
    | MetadataCategorySchema
    | PostByObjectTypeCategoriesResponseDefaultType0
    | PostByObjectTypeCategoriesResponseDefaultType1
]:
    """Add a metadata category for an object type


    Required roles:
     - can_write_metadata_categories

    Args:
        object_type (str):
        body (MetadataCategorySchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | MetadataCategorySchema | PostByObjectTypeCategoriesResponseDefaultType0 | PostByObjectTypeCategoriesResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        object_type=object_type,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    object_type: str,
    *,
    client: AuthenticatedClient | Client,
    body: MetadataCategorySchema,
) -> (
    Any
    | MetadataCategorySchema
    | PostByObjectTypeCategoriesResponseDefaultType0
    | PostByObjectTypeCategoriesResponseDefaultType1
    | None
):
    """Add a metadata category for an object type


    Required roles:
     - can_write_metadata_categories

    Args:
        object_type (str):
        body (MetadataCategorySchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | MetadataCategorySchema | PostByObjectTypeCategoriesResponseDefaultType0 | PostByObjectTypeCategoriesResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            object_type=object_type,
            client=client,
            body=body,
        )
    ).parsed
