from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.put_storages_by_storage_id_transcoders_by_transcoder_id_response_default_type_0 import (
    PutStoragesByStorageIdTranscodersByTranscoderIdResponseDefaultType0,
)
from ...models.put_storages_by_storage_id_transcoders_by_transcoder_id_response_default_type_1 import (
    PutStoragesByStorageIdTranscodersByTranscoderIdResponseDefaultType1,
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
    | PutStoragesByStorageIdTranscodersByTranscoderIdResponseDefaultType0
    | PutStoragesByStorageIdTranscodersByTranscoderIdResponseDefaultType1
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

    def _parse_response_default(
        data: object,
    ) -> (
        PutStoragesByStorageIdTranscodersByTranscoderIdResponseDefaultType0
        | PutStoragesByStorageIdTranscodersByTranscoderIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = PutStoragesByStorageIdTranscodersByTranscoderIdResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = PutStoragesByStorageIdTranscodersByTranscoderIdResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PutStoragesByStorageIdTranscodersByTranscoderIdResponseDefaultType0
    | PutStoragesByStorageIdTranscodersByTranscoderIdResponseDefaultType1
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
    | PutStoragesByStorageIdTranscodersByTranscoderIdResponseDefaultType0
    | PutStoragesByStorageIdTranscodersByTranscoderIdResponseDefaultType1
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
        Response[Any | PutStoragesByStorageIdTranscodersByTranscoderIdResponseDefaultType0 | PutStoragesByStorageIdTranscodersByTranscoderIdResponseDefaultType1 | TranscoderByStorageReadSchema]
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
    | PutStoragesByStorageIdTranscodersByTranscoderIdResponseDefaultType0
    | PutStoragesByStorageIdTranscodersByTranscoderIdResponseDefaultType1
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
        Any | PutStoragesByStorageIdTranscodersByTranscoderIdResponseDefaultType0 | PutStoragesByStorageIdTranscodersByTranscoderIdResponseDefaultType1 | TranscoderByStorageReadSchema
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
    | PutStoragesByStorageIdTranscodersByTranscoderIdResponseDefaultType0
    | PutStoragesByStorageIdTranscodersByTranscoderIdResponseDefaultType1
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
        Response[Any | PutStoragesByStorageIdTranscodersByTranscoderIdResponseDefaultType0 | PutStoragesByStorageIdTranscodersByTranscoderIdResponseDefaultType1 | TranscoderByStorageReadSchema]
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
    | PutStoragesByStorageIdTranscodersByTranscoderIdResponseDefaultType0
    | PutStoragesByStorageIdTranscodersByTranscoderIdResponseDefaultType1
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
        Any | PutStoragesByStorageIdTranscodersByTranscoderIdResponseDefaultType0 | PutStoragesByStorageIdTranscodersByTranscoderIdResponseDefaultType1 | TranscoderByStorageReadSchema
    """

    return (
        await asyncio_detailed(
            storage_id=storage_id,
            transcoder_id=transcoder_id,
            client=client,
        )
    ).parsed
