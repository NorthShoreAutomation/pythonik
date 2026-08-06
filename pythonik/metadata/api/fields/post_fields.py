from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.metadata_field_create_schema import MetadataFieldCreateSchema
from ...models.metadata_field_schema import MetadataFieldSchema
from ...models.post_fields_response_default import PostFieldsResponseDefault
from ...types import Response


def _get_kwargs(
    *,
    body: MetadataFieldCreateSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/fields/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | MetadataFieldSchema | PostFieldsResponseDefault:
    if response.status_code == 201:
        response_201 = MetadataFieldSchema.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = PostFieldsResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | MetadataFieldSchema | PostFieldsResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: MetadataFieldCreateSchema,
) -> Response[Any | MetadataFieldSchema | PostFieldsResponseDefault]:
    """Create a new field


    Required roles:
     - can_write_metadata_fields

    Args:
        body (MetadataFieldCreateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | MetadataFieldSchema | PostFieldsResponseDefault]
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
    body: MetadataFieldCreateSchema,
) -> Any | MetadataFieldSchema | PostFieldsResponseDefault | None:
    """Create a new field


    Required roles:
     - can_write_metadata_fields

    Args:
        body (MetadataFieldCreateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | MetadataFieldSchema | PostFieldsResponseDefault
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: MetadataFieldCreateSchema,
) -> Response[Any | MetadataFieldSchema | PostFieldsResponseDefault]:
    """Create a new field


    Required roles:
     - can_write_metadata_fields

    Args:
        body (MetadataFieldCreateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | MetadataFieldSchema | PostFieldsResponseDefault]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: MetadataFieldCreateSchema,
) -> Any | MetadataFieldSchema | PostFieldsResponseDefault | None:
    """Create a new field


    Required roles:
     - can_write_metadata_fields

    Args:
        body (MetadataFieldCreateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | MetadataFieldSchema | PostFieldsResponseDefault
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
