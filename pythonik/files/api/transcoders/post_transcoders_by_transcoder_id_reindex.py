from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_transcoders_by_transcoder_id_reindex_body import (
    PostTranscodersByTranscoderIdReindexBody,
)
from ...models.post_transcoders_by_transcoder_id_reindex_response_default import (
    PostTranscodersByTranscoderIdReindexResponseDefault,
)
from ...types import Response


def _get_kwargs(
    transcoder_id: str,
    *,
    body: PostTranscodersByTranscoderIdReindexBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/transcoders/{transcoder_id}/reindex/".format(
            transcoder_id=quote(str(transcoder_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostTranscodersByTranscoderIdReindexResponseDefault:
    if response.status_code == 201:
        response_201 = cast(Any, None)
        return response_201

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = PostTranscodersByTranscoderIdReindexResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PostTranscodersByTranscoderIdReindexResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    transcoder_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostTranscodersByTranscoderIdReindexBody,
) -> Response[Any | PostTranscodersByTranscoderIdReindexResponseDefault]:
    """Trigger reindexing of a transcoder


    Required roles:
     - can_reindex_transcoders

    Args:
        transcoder_id (str):
        body (PostTranscodersByTranscoderIdReindexBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostTranscodersByTranscoderIdReindexResponseDefault]
    """

    kwargs = _get_kwargs(
        transcoder_id=transcoder_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    transcoder_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostTranscodersByTranscoderIdReindexBody,
) -> Any | PostTranscodersByTranscoderIdReindexResponseDefault | None:
    """Trigger reindexing of a transcoder


    Required roles:
     - can_reindex_transcoders

    Args:
        transcoder_id (str):
        body (PostTranscodersByTranscoderIdReindexBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostTranscodersByTranscoderIdReindexResponseDefault
    """

    return sync_detailed(
        transcoder_id=transcoder_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    transcoder_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostTranscodersByTranscoderIdReindexBody,
) -> Response[Any | PostTranscodersByTranscoderIdReindexResponseDefault]:
    """Trigger reindexing of a transcoder


    Required roles:
     - can_reindex_transcoders

    Args:
        transcoder_id (str):
        body (PostTranscodersByTranscoderIdReindexBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostTranscodersByTranscoderIdReindexResponseDefault]
    """

    kwargs = _get_kwargs(
        transcoder_id=transcoder_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    transcoder_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostTranscodersByTranscoderIdReindexBody,
) -> Any | PostTranscodersByTranscoderIdReindexResponseDefault | None:
    """Trigger reindexing of a transcoder


    Required roles:
     - can_reindex_transcoders

    Args:
        transcoder_id (str):
        body (PostTranscodersByTranscoderIdReindexBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostTranscodersByTranscoderIdReindexResponseDefault
    """

    return (
        await asyncio_detailed(
            transcoder_id=transcoder_id,
            client=client,
            body=body,
        )
    ).parsed
