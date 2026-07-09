from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_sequences_by_sequence_id_items_by_item_id_response_default import (
    DeleteSequencesBySequenceIdItemsByItemIdResponseDefault,
)
from ...types import Response


def _get_kwargs(
    sequence_id: str,
    item_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/sequences/{sequence_id}/items/{item_id}/".format(
            sequence_id=quote(str(sequence_id), safe=""),
            item_id=quote(str(item_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DeleteSequencesBySequenceIdItemsByItemIdResponseDefault:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = (
        DeleteSequencesBySequenceIdItemsByItemIdResponseDefault.from_dict(
            response.json()
        )
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DeleteSequencesBySequenceIdItemsByItemIdResponseDefault]:
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
) -> Response[Any | DeleteSequencesBySequenceIdItemsByItemIdResponseDefault]:
    """Delete a particular sequence item by id


    Required roles:
     - can_delete_sequence_items

    Args:
        sequence_id (str):
        item_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteSequencesBySequenceIdItemsByItemIdResponseDefault]
    """

    kwargs = _get_kwargs(
        sequence_id=sequence_id,
        item_id=item_id,
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
) -> Any | DeleteSequencesBySequenceIdItemsByItemIdResponseDefault | None:
    """Delete a particular sequence item by id


    Required roles:
     - can_delete_sequence_items

    Args:
        sequence_id (str):
        item_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteSequencesBySequenceIdItemsByItemIdResponseDefault
    """

    return sync_detailed(
        sequence_id=sequence_id,
        item_id=item_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    sequence_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DeleteSequencesBySequenceIdItemsByItemIdResponseDefault]:
    """Delete a particular sequence item by id


    Required roles:
     - can_delete_sequence_items

    Args:
        sequence_id (str):
        item_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteSequencesBySequenceIdItemsByItemIdResponseDefault]
    """

    kwargs = _get_kwargs(
        sequence_id=sequence_id,
        item_id=item_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sequence_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | DeleteSequencesBySequenceIdItemsByItemIdResponseDefault | None:
    """Delete a particular sequence item by id


    Required roles:
     - can_delete_sequence_items

    Args:
        sequence_id (str):
        item_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteSequencesBySequenceIdItemsByItemIdResponseDefault
    """

    return (
        await asyncio_detailed(
            sequence_id=sequence_id,
            item_id=item_id,
            client=client,
        )
    ).parsed
