from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_sequences_by_sequence_id_response_default import (
    GetSequencesBySequenceIdResponseDefault,
)
from ...models.sequence_schema import SequenceSchema
from ...types import Response


def _get_kwargs(
    sequence_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/sequences/{sequence_id}/".format(
            sequence_id=quote(str(sequence_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetSequencesBySequenceIdResponseDefault | SequenceSchema:
    if response.status_code == 200:
        response_200 = SequenceSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = GetSequencesBySequenceIdResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetSequencesBySequenceIdResponseDefault | SequenceSchema]:
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
) -> Response[Any | GetSequencesBySequenceIdResponseDefault | SequenceSchema]:
    """Returns a particular sequence by id


    Required roles:
     - can_read_sequences

    Args:
        sequence_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSequencesBySequenceIdResponseDefault | SequenceSchema]
    """

    kwargs = _get_kwargs(
        sequence_id=sequence_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    sequence_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetSequencesBySequenceIdResponseDefault | SequenceSchema | None:
    """Returns a particular sequence by id


    Required roles:
     - can_read_sequences

    Args:
        sequence_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSequencesBySequenceIdResponseDefault | SequenceSchema
    """

    return sync_detailed(
        sequence_id=sequence_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    sequence_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetSequencesBySequenceIdResponseDefault | SequenceSchema]:
    """Returns a particular sequence by id


    Required roles:
     - can_read_sequences

    Args:
        sequence_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSequencesBySequenceIdResponseDefault | SequenceSchema]
    """

    kwargs = _get_kwargs(
        sequence_id=sequence_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sequence_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetSequencesBySequenceIdResponseDefault | SequenceSchema | None:
    """Returns a particular sequence by id


    Required roles:
     - can_read_sequences

    Args:
        sequence_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSequencesBySequenceIdResponseDefault | SequenceSchema
    """

    return (
        await asyncio_detailed(
            sequence_id=sequence_id,
            client=client,
        )
    ).parsed
