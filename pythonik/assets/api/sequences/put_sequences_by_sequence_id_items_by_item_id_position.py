from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.put_sequences_by_sequence_id_items_by_item_id_position_response_default_type_0 import (
    PutSequencesBySequenceIdItemsByItemIdPositionResponseDefaultType0,
)
from ...models.put_sequences_by_sequence_id_items_by_item_id_position_response_default_type_1 import (
    PutSequencesBySequenceIdItemsByItemIdPositionResponseDefaultType1,
)
from ...models.sequence_item_schema import SequenceItemSchema
from ...models.sequence_item_update_position_schema import (
    SequenceItemUpdatePositionSchema,
)
from ...types import Response


def _get_kwargs(
    sequence_id: str,
    item_id: str,
    *,
    body: SequenceItemUpdatePositionSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/sequences/{sequence_id}/items/{item_id}/position/".format(
            sequence_id=quote(str(sequence_id), safe=""),
            item_id=quote(str(item_id), safe=""),
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
    | PutSequencesBySequenceIdItemsByItemIdPositionResponseDefaultType0
    | PutSequencesBySequenceIdItemsByItemIdPositionResponseDefaultType1
    | SequenceItemSchema
):
    if response.status_code == 201:
        response_201 = SequenceItemSchema.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    def _parse_response_default(
        data: object,
    ) -> (
        PutSequencesBySequenceIdItemsByItemIdPositionResponseDefaultType0
        | PutSequencesBySequenceIdItemsByItemIdPositionResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = PutSequencesBySequenceIdItemsByItemIdPositionResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PutSequencesBySequenceIdItemsByItemIdPositionResponseDefaultType1.from_dict(
                data
            )
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PutSequencesBySequenceIdItemsByItemIdPositionResponseDefaultType0
    | PutSequencesBySequenceIdItemsByItemIdPositionResponseDefaultType1
    | SequenceItemSchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    sequence_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SequenceItemUpdatePositionSchema,
) -> Response[
    Any
    | PutSequencesBySequenceIdItemsByItemIdPositionResponseDefaultType0
    | PutSequencesBySequenceIdItemsByItemIdPositionResponseDefaultType1
    | SequenceItemSchema
]:
    """Update a sequence item position


    Required roles:
     - can_add_sequence_items

    Args:
        sequence_id (str):
        item_id (str):
        body (SequenceItemUpdatePositionSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutSequencesBySequenceIdItemsByItemIdPositionResponseDefaultType0 | PutSequencesBySequenceIdItemsByItemIdPositionResponseDefaultType1 | SequenceItemSchema]
    """

    kwargs = _get_kwargs(
        sequence_id=sequence_id,
        item_id=item_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    sequence_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SequenceItemUpdatePositionSchema,
) -> (
    Any
    | PutSequencesBySequenceIdItemsByItemIdPositionResponseDefaultType0
    | PutSequencesBySequenceIdItemsByItemIdPositionResponseDefaultType1
    | SequenceItemSchema
    | None
):
    """Update a sequence item position


    Required roles:
     - can_add_sequence_items

    Args:
        sequence_id (str):
        item_id (str):
        body (SequenceItemUpdatePositionSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutSequencesBySequenceIdItemsByItemIdPositionResponseDefaultType0 | PutSequencesBySequenceIdItemsByItemIdPositionResponseDefaultType1 | SequenceItemSchema
    """

    return sync_detailed(
        sequence_id=sequence_id,
        item_id=item_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    sequence_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SequenceItemUpdatePositionSchema,
) -> Response[
    Any
    | PutSequencesBySequenceIdItemsByItemIdPositionResponseDefaultType0
    | PutSequencesBySequenceIdItemsByItemIdPositionResponseDefaultType1
    | SequenceItemSchema
]:
    """Update a sequence item position


    Required roles:
     - can_add_sequence_items

    Args:
        sequence_id (str):
        item_id (str):
        body (SequenceItemUpdatePositionSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutSequencesBySequenceIdItemsByItemIdPositionResponseDefaultType0 | PutSequencesBySequenceIdItemsByItemIdPositionResponseDefaultType1 | SequenceItemSchema]
    """

    kwargs = _get_kwargs(
        sequence_id=sequence_id,
        item_id=item_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sequence_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SequenceItemUpdatePositionSchema,
) -> (
    Any
    | PutSequencesBySequenceIdItemsByItemIdPositionResponseDefaultType0
    | PutSequencesBySequenceIdItemsByItemIdPositionResponseDefaultType1
    | SequenceItemSchema
    | None
):
    """Update a sequence item position


    Required roles:
     - can_add_sequence_items

    Args:
        sequence_id (str):
        item_id (str):
        body (SequenceItemUpdatePositionSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutSequencesBySequenceIdItemsByItemIdPositionResponseDefaultType0 | PutSequencesBySequenceIdItemsByItemIdPositionResponseDefaultType1 | SequenceItemSchema
    """

    return (
        await asyncio_detailed(
            sequence_id=sequence_id,
            item_id=item_id,
            client=client,
            body=body,
        )
    ).parsed
