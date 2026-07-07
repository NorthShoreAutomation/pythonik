from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_storages_by_storage_id_transcoders_response_default_type_0 import (
    GetStoragesByStorageIdTranscodersResponseDefaultType0,
)
from ...models.get_storages_by_storage_id_transcoders_response_default_type_1 import (
    GetStoragesByStorageIdTranscodersResponseDefaultType1,
)
from ...models.transcoders_by_storage_schema import TranscodersByStorageSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    storage_id: str,
    *,
    per_page: int | Unset = 10,
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
    Any
    | GetStoragesByStorageIdTranscodersResponseDefaultType0
    | GetStoragesByStorageIdTranscodersResponseDefaultType1
    | TranscodersByStorageSchema
):
    if response.status_code == 200:
        response_200 = TranscodersByStorageSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    def _parse_response_default(
        data: object,
    ) -> (
        GetStoragesByStorageIdTranscodersResponseDefaultType0
        | GetStoragesByStorageIdTranscodersResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetStoragesByStorageIdTranscodersResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            GetStoragesByStorageIdTranscodersResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetStoragesByStorageIdTranscodersResponseDefaultType0
    | GetStoragesByStorageIdTranscodersResponseDefaultType1
    | TranscodersByStorageSchema
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
    per_page: int | Unset = 10,
    last_id: str | Unset = UNSET,
) -> Response[
    Any
    | GetStoragesByStorageIdTranscodersResponseDefaultType0
    | GetStoragesByStorageIdTranscodersResponseDefaultType1
    | TranscodersByStorageSchema
]:
    """Get all transcoders for a particular storage


    Required roles:
     - can_read_storages
    - can_read_transcoders

    Args:
        storage_id (str):
        per_page (int | Unset):  Default: 10.
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetStoragesByStorageIdTranscodersResponseDefaultType0 | GetStoragesByStorageIdTranscodersResponseDefaultType1 | TranscodersByStorageSchema]
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
    per_page: int | Unset = 10,
    last_id: str | Unset = UNSET,
) -> (
    Any
    | GetStoragesByStorageIdTranscodersResponseDefaultType0
    | GetStoragesByStorageIdTranscodersResponseDefaultType1
    | TranscodersByStorageSchema
    | None
):
    """Get all transcoders for a particular storage


    Required roles:
     - can_read_storages
    - can_read_transcoders

    Args:
        storage_id (str):
        per_page (int | Unset):  Default: 10.
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetStoragesByStorageIdTranscodersResponseDefaultType0 | GetStoragesByStorageIdTranscodersResponseDefaultType1 | TranscodersByStorageSchema
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
    per_page: int | Unset = 10,
    last_id: str | Unset = UNSET,
) -> Response[
    Any
    | GetStoragesByStorageIdTranscodersResponseDefaultType0
    | GetStoragesByStorageIdTranscodersResponseDefaultType1
    | TranscodersByStorageSchema
]:
    """Get all transcoders for a particular storage


    Required roles:
     - can_read_storages
    - can_read_transcoders

    Args:
        storage_id (str):
        per_page (int | Unset):  Default: 10.
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetStoragesByStorageIdTranscodersResponseDefaultType0 | GetStoragesByStorageIdTranscodersResponseDefaultType1 | TranscodersByStorageSchema]
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
    per_page: int | Unset = 10,
    last_id: str | Unset = UNSET,
) -> (
    Any
    | GetStoragesByStorageIdTranscodersResponseDefaultType0
    | GetStoragesByStorageIdTranscodersResponseDefaultType1
    | TranscodersByStorageSchema
    | None
):
    """Get all transcoders for a particular storage


    Required roles:
     - can_read_storages
    - can_read_transcoders

    Args:
        storage_id (str):
        per_page (int | Unset):  Default: 10.
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetStoragesByStorageIdTranscodersResponseDefaultType0 | GetStoragesByStorageIdTranscodersResponseDefaultType1 | TranscodersByStorageSchema
    """

    return (
        await asyncio_detailed(
            storage_id=storage_id,
            client=client,
            per_page=per_page,
            last_id=last_id,
        )
    ).parsed
