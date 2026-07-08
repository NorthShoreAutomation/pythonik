from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_storages_by_storage_id_transcoders_response_default import (
    GetStoragesByStorageIdTranscodersResponseDefault,
)
from ...models.transcoders_by_storage_schema import TranscodersByStorageSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    storage_id: str,
    *,
    per_page: int | Unset = UNSET,
    last_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["per_page"] = per_page

    params["last_id"] = last_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/storages/{storage_id}/transcoders/".format(
            storage_id=quote(str(storage_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any | GetStoragesByStorageIdTranscodersResponseDefault | TranscodersByStorageSchema
):
    if response.status_code == 200:
        response_200 = TranscodersByStorageSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = GetStoragesByStorageIdTranscodersResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | GetStoragesByStorageIdTranscodersResponseDefault | TranscodersByStorageSchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    last_id: str | Unset = UNSET,
) -> Response[
    Any | GetStoragesByStorageIdTranscodersResponseDefault | TranscodersByStorageSchema
]:
    """Get all transcoders for a particular storage


    Required roles:
     - can_read_storages
    - can_read_transcoders

    Args:
        storage_id (str):
        per_page (int | Unset):
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetStoragesByStorageIdTranscodersResponseDefault | TranscodersByStorageSchema]
    """

    kwargs = _get_kwargs(
        storage_id=storage_id,
        per_page=per_page,
        last_id=last_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    last_id: str | Unset = UNSET,
) -> (
    Any
    | GetStoragesByStorageIdTranscodersResponseDefault
    | TranscodersByStorageSchema
    | None
):
    """Get all transcoders for a particular storage


    Required roles:
     - can_read_storages
    - can_read_transcoders

    Args:
        storage_id (str):
        per_page (int | Unset):
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetStoragesByStorageIdTranscodersResponseDefault | TranscodersByStorageSchema
    """

    return sync_detailed(
        storage_id=storage_id,
        client=client,
        per_page=per_page,
        last_id=last_id,
    ).parsed


async def asyncio_detailed(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    last_id: str | Unset = UNSET,
) -> Response[
    Any | GetStoragesByStorageIdTranscodersResponseDefault | TranscodersByStorageSchema
]:
    """Get all transcoders for a particular storage


    Required roles:
     - can_read_storages
    - can_read_transcoders

    Args:
        storage_id (str):
        per_page (int | Unset):
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetStoragesByStorageIdTranscodersResponseDefault | TranscodersByStorageSchema]
    """

    kwargs = _get_kwargs(
        storage_id=storage_id,
        per_page=per_page,
        last_id=last_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    last_id: str | Unset = UNSET,
) -> (
    Any
    | GetStoragesByStorageIdTranscodersResponseDefault
    | TranscodersByStorageSchema
    | None
):
    """Get all transcoders for a particular storage


    Required roles:
     - can_read_storages
    - can_read_transcoders

    Args:
        storage_id (str):
        per_page (int | Unset):
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetStoragesByStorageIdTranscodersResponseDefault | TranscodersByStorageSchema
    """

    return (
        await asyncio_detailed(
            storage_id=storage_id,
            client=client,
            per_page=per_page,
            last_id=last_id,
        )
    ).parsed
