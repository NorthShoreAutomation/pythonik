from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.put_storages_by_storage_id_transcoders_by_transcoder_id_response_default import (
    PutStoragesByStorageIdTranscodersByTranscoderIdResponseDefault,
)
from ...models.transcoder_by_storage_read_schema import TranscoderByStorageReadSchema
from ...types import Response


def _get_kwargs(
    storage_id: str,
    transcoder_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/storages/{storage_id}/transcoders/{transcoder_id}/".format(
            storage_id=quote(str(storage_id), safe=""),
            transcoder_id=quote(str(transcoder_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | PutStoragesByStorageIdTranscodersByTranscoderIdResponseDefault
    | TranscoderByStorageReadSchema
):
    if response.status_code == 201:
        response_201 = TranscoderByStorageReadSchema.from_dict(response.json())

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

    response_default = (
        PutStoragesByStorageIdTranscodersByTranscoderIdResponseDefault.from_dict(
            response.json()
        )
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PutStoragesByStorageIdTranscodersByTranscoderIdResponseDefault
    | TranscoderByStorageReadSchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    storage_id: str,
    transcoder_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | PutStoragesByStorageIdTranscodersByTranscoderIdResponseDefault
    | TranscoderByStorageReadSchema
]:
    """Create a new transcoder for storage


    Required roles:
     - can_write_transcoders

    Args:
        storage_id (str):
        transcoder_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutStoragesByStorageIdTranscodersByTranscoderIdResponseDefault | TranscoderByStorageReadSchema]
    """

    kwargs = _get_kwargs(
        storage_id=storage_id,
        transcoder_id=transcoder_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    storage_id: str,
    transcoder_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | PutStoragesByStorageIdTranscodersByTranscoderIdResponseDefault
    | TranscoderByStorageReadSchema
    | None
):
    """Create a new transcoder for storage


    Required roles:
     - can_write_transcoders

    Args:
        storage_id (str):
        transcoder_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutStoragesByStorageIdTranscodersByTranscoderIdResponseDefault | TranscoderByStorageReadSchema
    """

    return sync_detailed(
        storage_id=storage_id,
        transcoder_id=transcoder_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    storage_id: str,
    transcoder_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | PutStoragesByStorageIdTranscodersByTranscoderIdResponseDefault
    | TranscoderByStorageReadSchema
]:
    """Create a new transcoder for storage


    Required roles:
     - can_write_transcoders

    Args:
        storage_id (str):
        transcoder_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutStoragesByStorageIdTranscodersByTranscoderIdResponseDefault | TranscoderByStorageReadSchema]
    """

    kwargs = _get_kwargs(
        storage_id=storage_id,
        transcoder_id=transcoder_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    storage_id: str,
    transcoder_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | PutStoragesByStorageIdTranscodersByTranscoderIdResponseDefault
    | TranscoderByStorageReadSchema
    | None
):
    """Create a new transcoder for storage


    Required roles:
     - can_write_transcoders

    Args:
        storage_id (str):
        transcoder_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutStoragesByStorageIdTranscodersByTranscoderIdResponseDefault | TranscoderByStorageReadSchema
    """

    return (
        await asyncio_detailed(
            storage_id=storage_id,
            transcoder_id=transcoder_id,
            client=client,
        )
    ).parsed
