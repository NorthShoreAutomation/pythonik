from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bulk_metadata_filling_schema import BulkMetadataFillingSchema
from ...models.post_metadata_filling_bulk_response_default_type_0 import (
    PostMetadataFillingBulkResponseDefaultType0,
)
from ...models.post_metadata_filling_bulk_response_default_type_1 import (
    PostMetadataFillingBulkResponseDefaultType1,
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
) -> (
    Any
    | PostMetadataFillingBulkResponseDefaultType0
    | PostMetadataFillingBulkResponseDefaultType1
):
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

    def _parse_response_default(
        data: object,
    ) -> (
        PostMetadataFillingBulkResponseDefaultType0
        | PostMetadataFillingBulkResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                PostMetadataFillingBulkResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = PostMetadataFillingBulkResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostMetadataFillingBulkResponseDefaultType0
    | PostMetadataFillingBulkResponseDefaultType1
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
    body: BulkMetadataFillingSchema,
) -> Response[
    Any
    | PostMetadataFillingBulkResponseDefaultType0
    | PostMetadataFillingBulkResponseDefaultType1
]:
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
        Response[Any | PostMetadataFillingBulkResponseDefaultType0 | PostMetadataFillingBulkResponseDefaultType1]
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
) -> (
    Any
    | PostMetadataFillingBulkResponseDefaultType0
    | PostMetadataFillingBulkResponseDefaultType1
    | None
):
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
        Any | PostMetadataFillingBulkResponseDefaultType0 | PostMetadataFillingBulkResponseDefaultType1
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BulkMetadataFillingSchema,
) -> Response[
    Any
    | PostMetadataFillingBulkResponseDefaultType0
    | PostMetadataFillingBulkResponseDefaultType1
]:
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
        Response[Any | PostMetadataFillingBulkResponseDefaultType0 | PostMetadataFillingBulkResponseDefaultType1]
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
) -> (
    Any
    | PostMetadataFillingBulkResponseDefaultType0
    | PostMetadataFillingBulkResponseDefaultType1
    | None
):
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
        Any | PostMetadataFillingBulkResponseDefaultType0 | PostMetadataFillingBulkResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
