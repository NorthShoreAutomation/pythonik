from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_sequences_by_sequence_id_items_response_default import (
    GetSequencesBySequenceIdItemsResponseDefault,
)
from ...models.sequence_items_schema import SequenceItemsSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    sequence_id: str,
    *,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["per_page"] = per_page

    params["page"] = page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/sequences/{sequence_id}/items/".format(
            sequence_id=quote(str(sequence_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetSequencesBySequenceIdItemsResponseDefault | SequenceItemsSchema:
    if response.status_code == 200:
        response_200 = SequenceItemsSchema.from_dict(response.json())

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

    response_default = GetSequencesBySequenceIdItemsResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetSequencesBySequenceIdItemsResponseDefault | SequenceItemsSchema]:
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
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
) -> Response[Any | GetSequencesBySequenceIdItemsResponseDefault | SequenceItemsSchema]:
    """Get list of sequence's items


    Required roles:
     - can_read_sequences

    Args:
        sequence_id (str):
        per_page (int | Unset):
        page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSequencesBySequenceIdItemsResponseDefault | SequenceItemsSchema]
    """

    kwargs = _get_kwargs(
        sequence_id=sequence_id,
        per_page=per_page,
        page=page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    sequence_id: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
) -> Any | GetSequencesBySequenceIdItemsResponseDefault | SequenceItemsSchema | None:
    """Get list of sequence's items


    Required roles:
     - can_read_sequences

    Args:
        sequence_id (str):
        per_page (int | Unset):
        page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSequencesBySequenceIdItemsResponseDefault | SequenceItemsSchema
    """

    return sync_detailed(
        sequence_id=sequence_id,
        client=client,
        per_page=per_page,
        page=page,
    ).parsed


async def asyncio_detailed(
    sequence_id: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
) -> Response[Any | GetSequencesBySequenceIdItemsResponseDefault | SequenceItemsSchema]:
    """Get list of sequence's items


    Required roles:
     - can_read_sequences

    Args:
        sequence_id (str):
        per_page (int | Unset):
        page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSequencesBySequenceIdItemsResponseDefault | SequenceItemsSchema]
    """

    kwargs = _get_kwargs(
        sequence_id=sequence_id,
        per_page=per_page,
        page=page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sequence_id: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
) -> Any | GetSequencesBySequenceIdItemsResponseDefault | SequenceItemsSchema | None:
    """Get list of sequence's items


    Required roles:
     - can_read_sequences

    Args:
        sequence_id (str):
        per_page (int | Unset):
        page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSequencesBySequenceIdItemsResponseDefault | SequenceItemsSchema
    """

    return (
        await asyncio_detailed(
            sequence_id=sequence_id,
            client=client,
            per_page=per_page,
            page=page,
        )
    ).parsed
