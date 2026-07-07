from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_sequences_by_sequence_id_reindex_response_default_type_0 import (
    PostSequencesBySequenceIdReindexResponseDefaultType0,
)
from ...models.post_sequences_by_sequence_id_reindex_response_default_type_1 import (
    PostSequencesBySequenceIdReindexResponseDefaultType1,
)
from ...models.reindex_sequence_schema import ReindexSequenceSchema
from ...types import Response


def _get_kwargs(
    sequence_id: str,
    *,
    body: ReindexSequenceSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/sequences/{sequence_id}/reindex/".format(
            sequence_id=quote(str(sequence_id), safe=""),
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
    | PostSequencesBySequenceIdReindexResponseDefaultType0
    | PostSequencesBySequenceIdReindexResponseDefaultType1
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

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    def _parse_response_default(
        data: object,
    ) -> (
        PostSequencesBySequenceIdReindexResponseDefaultType0
        | PostSequencesBySequenceIdReindexResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                PostSequencesBySequenceIdReindexResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PostSequencesBySequenceIdReindexResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostSequencesBySequenceIdReindexResponseDefaultType0
    | PostSequencesBySequenceIdReindexResponseDefaultType1
]:
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
    body: ReindexSequenceSchema,
) -> Response[
    Any
    | PostSequencesBySequenceIdReindexResponseDefaultType0
    | PostSequencesBySequenceIdReindexResponseDefaultType1
]:
    """Reindex the sequence


    Required roles:
     - can_reindex_sequences

    Args:
        sequence_id (str):
        body (ReindexSequenceSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostSequencesBySequenceIdReindexResponseDefaultType0 | PostSequencesBySequenceIdReindexResponseDefaultType1]
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
    body: ReindexSequenceSchema,
) -> (
    Any
    | PostSequencesBySequenceIdReindexResponseDefaultType0
    | PostSequencesBySequenceIdReindexResponseDefaultType1
    | None
):
    """Reindex the sequence


    Required roles:
     - can_reindex_sequences

    Args:
        sequence_id (str):
        body (ReindexSequenceSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostSequencesBySequenceIdReindexResponseDefaultType0 | PostSequencesBySequenceIdReindexResponseDefaultType1
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
    body: ReindexSequenceSchema,
) -> Response[
    Any
    | PostSequencesBySequenceIdReindexResponseDefaultType0
    | PostSequencesBySequenceIdReindexResponseDefaultType1
]:
    """Reindex the sequence


    Required roles:
     - can_reindex_sequences

    Args:
        sequence_id (str):
        body (ReindexSequenceSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostSequencesBySequenceIdReindexResponseDefaultType0 | PostSequencesBySequenceIdReindexResponseDefaultType1]
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
    body: ReindexSequenceSchema,
) -> (
    Any
    | PostSequencesBySequenceIdReindexResponseDefaultType0
    | PostSequencesBySequenceIdReindexResponseDefaultType1
    | None
):
    """Reindex the sequence


    Required roles:
     - can_reindex_sequences

    Args:
        sequence_id (str):
        body (ReindexSequenceSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostSequencesBySequenceIdReindexResponseDefaultType0 | PostSequencesBySequenceIdReindexResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            sequence_id=sequence_id,
            client=client,
            body=body,
        )
    ).parsed
