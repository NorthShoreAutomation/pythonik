from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.metadata_field_mapping_schema import MetadataFieldMappingSchema
from ...models.post_mapping_fields_response_default import (
    PostMappingFieldsResponseDefault,
)
from ...types import Response


def _get_kwargs(
    *,
    body: MetadataFieldMappingSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/mapping/fields/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | MetadataFieldMappingSchema | PostMappingFieldsResponseDefault:
    if response.status_code == 201:
        response_201 = MetadataFieldMappingSchema.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = PostMappingFieldsResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | MetadataFieldMappingSchema | PostMappingFieldsResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: MetadataFieldMappingSchema,
) -> Response[Any | MetadataFieldMappingSchema | PostMappingFieldsResponseDefault]:
    """Create a new metadata field mapping


    Required roles:
     - can_read_metadata_fields

    Args:
        body (MetadataFieldMappingSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | MetadataFieldMappingSchema | PostMappingFieldsResponseDefault]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: MetadataFieldMappingSchema,
) -> Any | MetadataFieldMappingSchema | PostMappingFieldsResponseDefault | None:
    """Create a new metadata field mapping


    Required roles:
     - can_read_metadata_fields

    Args:
        body (MetadataFieldMappingSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | MetadataFieldMappingSchema | PostMappingFieldsResponseDefault
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: MetadataFieldMappingSchema,
) -> Response[Any | MetadataFieldMappingSchema | PostMappingFieldsResponseDefault]:
    """Create a new metadata field mapping


    Required roles:
     - can_read_metadata_fields

    Args:
        body (MetadataFieldMappingSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | MetadataFieldMappingSchema | PostMappingFieldsResponseDefault]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: MetadataFieldMappingSchema,
) -> Any | MetadataFieldMappingSchema | PostMappingFieldsResponseDefault | None:
    """Create a new metadata field mapping


    Required roles:
     - can_read_metadata_fields

    Args:
        body (MetadataFieldMappingSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | MetadataFieldMappingSchema | PostMappingFieldsResponseDefault
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
