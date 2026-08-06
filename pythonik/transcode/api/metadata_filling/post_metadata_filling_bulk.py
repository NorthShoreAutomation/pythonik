from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bulk_metadata_filling_schema import BulkMetadataFillingSchema
from ...models.post_metadata_filling_bulk_response_default import (
    PostMetadataFillingBulkResponseDefault,
)
from ...types import Response


def _get_kwargs(
    *,
    body: BulkMetadataFillingSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/metadata_filling/bulk/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostMetadataFillingBulkResponseDefault:
    if response.status_code == 201:
        response_201 = cast(Any, None)
        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    response_default = PostMetadataFillingBulkResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PostMetadataFillingBulkResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BulkMetadataFillingSchema,
) -> Response[Any | PostMetadataFillingBulkResponseDefault]:
    """Run bulk AI metadata filling


    Required roles:
     - can_trigger_metadata_ai_filling
    - can_write_metadata_values

    Args:
        body (BulkMetadataFillingSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostMetadataFillingBulkResponseDefault]
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
    body: BulkMetadataFillingSchema,
) -> Any | PostMetadataFillingBulkResponseDefault | None:
    """Run bulk AI metadata filling


    Required roles:
     - can_trigger_metadata_ai_filling
    - can_write_metadata_values

    Args:
        body (BulkMetadataFillingSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostMetadataFillingBulkResponseDefault
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BulkMetadataFillingSchema,
) -> Response[Any | PostMetadataFillingBulkResponseDefault]:
    """Run bulk AI metadata filling


    Required roles:
     - can_trigger_metadata_ai_filling
    - can_write_metadata_values

    Args:
        body (BulkMetadataFillingSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostMetadataFillingBulkResponseDefault]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: BulkMetadataFillingSchema,
) -> Any | PostMetadataFillingBulkResponseDefault | None:
    """Run bulk AI metadata filling


    Required roles:
     - can_trigger_metadata_ai_filling
    - can_write_metadata_values

    Args:
        body (BulkMetadataFillingSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostMetadataFillingBulkResponseDefault
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
