from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_sequences_by_sequence_id_items_response_default import (
    PostSequencesBySequenceIdItemsResponseDefault,
)
from ...models.sequence_item_schema import SequenceItemSchema
from ...types import Response


def _get_kwargs(
    sequence_id: str,
    *,
    body: SequenceItemSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/sequences/{sequence_id}/items/".format(
            sequence_id=quote(str(sequence_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostSequencesBySequenceIdItemsResponseDefault | SequenceItemSchema:
    if response.status_code == 201:
        response_201 = SequenceItemSchema.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = PostSequencesBySequenceIdItemsResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PostSequencesBySequenceIdItemsResponseDefault | SequenceItemSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    sequence_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SequenceItemSchema,
) -> Response[Any | PostSequencesBySequenceIdItemsResponseDefault | SequenceItemSchema]:
    """Add an item to a sequence


    Required roles:
     - can_add_sequence_items

    Args:
        sequence_id (str):
        body (SequenceItemSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostSequencesBySequenceIdItemsResponseDefault | SequenceItemSchema]
    """

    kwargs = _get_kwargs(
        sequence_id=sequence_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    sequence_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SequenceItemSchema,
) -> Any | PostSequencesBySequenceIdItemsResponseDefault | SequenceItemSchema | None:
    """Add an item to a sequence


    Required roles:
     - can_add_sequence_items

    Args:
        sequence_id (str):
        body (SequenceItemSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostSequencesBySequenceIdItemsResponseDefault | SequenceItemSchema
    """

    return sync_detailed(
        sequence_id=sequence_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    sequence_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SequenceItemSchema,
) -> Response[Any | PostSequencesBySequenceIdItemsResponseDefault | SequenceItemSchema]:
    """Add an item to a sequence


    Required roles:
     - can_add_sequence_items

    Args:
        sequence_id (str):
        body (SequenceItemSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostSequencesBySequenceIdItemsResponseDefault | SequenceItemSchema]
    """

    kwargs = _get_kwargs(
        sequence_id=sequence_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sequence_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SequenceItemSchema,
) -> Any | PostSequencesBySequenceIdItemsResponseDefault | SequenceItemSchema | None:
    """Add an item to a sequence


    Required roles:
     - can_add_sequence_items

    Args:
        sequence_id (str):
        body (SequenceItemSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostSequencesBySequenceIdItemsResponseDefault | SequenceItemSchema
    """

    return (
        await asyncio_detailed(
            sequence_id=sequence_id,
            client=client,
            body=body,
        )
    ).parsed
