from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_transcoders_by_transcoder_id_response_default import (
    GetTranscodersByTranscoderIdResponseDefault,
)
from ...models.transcoder_schema import TranscoderSchema
from ...types import Response


def _get_kwargs(
    transcoder_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/transcoders/{transcoder_id}/".format(
            transcoder_id=quote(str(transcoder_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetTranscodersByTranscoderIdResponseDefault | TranscoderSchema:
    if response.status_code == 200:
        response_200 = TranscoderSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = GetTranscodersByTranscoderIdResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetTranscodersByTranscoderIdResponseDefault | TranscoderSchema]:
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
) -> Response[Any | GetTranscodersByTranscoderIdResponseDefault | TranscoderSchema]:
    """Returns a particular transcoder by id


    Required roles:
     - can_read_transcoders

    Args:
        transcoder_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetTranscodersByTranscoderIdResponseDefault | TranscoderSchema]
    """

    kwargs = _get_kwargs(
        transcoder_id=transcoder_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    transcoder_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetTranscodersByTranscoderIdResponseDefault | TranscoderSchema | None:
    """Returns a particular transcoder by id


    Required roles:
     - can_read_transcoders

    Args:
        transcoder_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetTranscodersByTranscoderIdResponseDefault | TranscoderSchema
    """

    return sync_detailed(
        transcoder_id=transcoder_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    transcoder_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetTranscodersByTranscoderIdResponseDefault | TranscoderSchema]:
    """Returns a particular transcoder by id


    Required roles:
     - can_read_transcoders

    Args:
        transcoder_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetTranscodersByTranscoderIdResponseDefault | TranscoderSchema]
    """

    kwargs = _get_kwargs(
        transcoder_id=transcoder_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    transcoder_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetTranscodersByTranscoderIdResponseDefault | TranscoderSchema | None:
    """Returns a particular transcoder by id


    Required roles:
     - can_read_transcoders

    Args:
        transcoder_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetTranscodersByTranscoderIdResponseDefault | TranscoderSchema
    """

    return (
        await asyncio_detailed(
            transcoder_id=transcoder_id,
            client=client,
        )
    ).parsed
