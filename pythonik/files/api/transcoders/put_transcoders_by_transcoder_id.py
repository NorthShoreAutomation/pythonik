from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.put_transcoders_by_transcoder_id_response_default import (
    PutTranscodersByTranscoderIdResponseDefault,
)
from ...models.transcoder_schema import TranscoderSchema
from ...types import Response


def _get_kwargs(
    transcoder_id: str,
    *,
    body: TranscoderSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/transcoders/{transcoder_id}/".format(
            transcoder_id=quote(str(transcoder_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PutTranscodersByTranscoderIdResponseDefault | TranscoderSchema:
    if response.status_code == 200:
        response_200 = TranscoderSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = PutTranscodersByTranscoderIdResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PutTranscodersByTranscoderIdResponseDefault | TranscoderSchema]:
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
    body: TranscoderSchema,
) -> Response[Any | PutTranscodersByTranscoderIdResponseDefault | TranscoderSchema]:
    """Update transcoder


    Required roles:
     - can_write_transcoders

    Args:
        transcoder_id (str):
        body (TranscoderSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutTranscodersByTranscoderIdResponseDefault | TranscoderSchema]
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
    body: TranscoderSchema,
) -> Any | PutTranscodersByTranscoderIdResponseDefault | TranscoderSchema | None:
    """Update transcoder


    Required roles:
     - can_write_transcoders

    Args:
        transcoder_id (str):
        body (TranscoderSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutTranscodersByTranscoderIdResponseDefault | TranscoderSchema
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
    body: TranscoderSchema,
) -> Response[Any | PutTranscodersByTranscoderIdResponseDefault | TranscoderSchema]:
    """Update transcoder


    Required roles:
     - can_write_transcoders

    Args:
        transcoder_id (str):
        body (TranscoderSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutTranscodersByTranscoderIdResponseDefault | TranscoderSchema]
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
    body: TranscoderSchema,
) -> Any | PutTranscodersByTranscoderIdResponseDefault | TranscoderSchema | None:
    """Update transcoder


    Required roles:
     - can_write_transcoders

    Args:
        transcoder_id (str):
        body (TranscoderSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutTranscodersByTranscoderIdResponseDefault | TranscoderSchema
    """

    return (
        await asyncio_detailed(
            transcoder_id=transcoder_id,
            client=client,
            body=body,
        )
    ).parsed
