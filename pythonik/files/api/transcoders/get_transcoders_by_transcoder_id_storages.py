from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_transcoders_by_transcoder_id_storages_response_default_type_0 import (
    GetTranscodersByTranscoderIdStoragesResponseDefaultType0,
)
from ...models.get_transcoders_by_transcoder_id_storages_response_default_type_1 import (
    GetTranscodersByTranscoderIdStoragesResponseDefaultType1,
)
from ...models.storages_read_schema import StoragesReadSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    transcoder_id: str,
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
        "url": "/v1/transcoders/{transcoder_id}/storages/".format(
            transcoder_id=quote(str(transcoder_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetTranscodersByTranscoderIdStoragesResponseDefaultType0
    | GetTranscodersByTranscoderIdStoragesResponseDefaultType1
    | StoragesReadSchema
):
    if response.status_code == 200:
        response_200 = StoragesReadSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    def _parse_response_default(
        data: object,
    ) -> (
        GetTranscodersByTranscoderIdStoragesResponseDefaultType0
        | GetTranscodersByTranscoderIdStoragesResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetTranscodersByTranscoderIdStoragesResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            GetTranscodersByTranscoderIdStoragesResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetTranscodersByTranscoderIdStoragesResponseDefaultType0
    | GetTranscodersByTranscoderIdStoragesResponseDefaultType1
    | StoragesReadSchema
]:
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
    per_page: int | Unset = 10,
    last_id: str | Unset = UNSET,
) -> Response[
    Any
    | GetTranscodersByTranscoderIdStoragesResponseDefaultType0
    | GetTranscodersByTranscoderIdStoragesResponseDefaultType1
    | StoragesReadSchema
]:
    """Get storages linked to a transcoder


    Required roles:
     - can_read_transcoders

    Args:
        transcoder_id (str):
        per_page (int | Unset):  Default: 10.
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetTranscodersByTranscoderIdStoragesResponseDefaultType0 | GetTranscodersByTranscoderIdStoragesResponseDefaultType1 | StoragesReadSchema]
    """

    kwargs = _get_kwargs(
        transcoder_id=transcoder_id,
        per_page=per_page,
        last_id=last_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    transcoder_id: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = 10,
    last_id: str | Unset = UNSET,
) -> (
    Any
    | GetTranscodersByTranscoderIdStoragesResponseDefaultType0
    | GetTranscodersByTranscoderIdStoragesResponseDefaultType1
    | StoragesReadSchema
    | None
):
    """Get storages linked to a transcoder


    Required roles:
     - can_read_transcoders

    Args:
        transcoder_id (str):
        per_page (int | Unset):  Default: 10.
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetTranscodersByTranscoderIdStoragesResponseDefaultType0 | GetTranscodersByTranscoderIdStoragesResponseDefaultType1 | StoragesReadSchema
    """

    return sync_detailed(
        transcoder_id=transcoder_id,
        client=client,
        per_page=per_page,
        last_id=last_id,
    ).parsed


async def asyncio_detailed(
    transcoder_id: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = 10,
    last_id: str | Unset = UNSET,
) -> Response[
    Any
    | GetTranscodersByTranscoderIdStoragesResponseDefaultType0
    | GetTranscodersByTranscoderIdStoragesResponseDefaultType1
    | StoragesReadSchema
]:
    """Get storages linked to a transcoder


    Required roles:
     - can_read_transcoders

    Args:
        transcoder_id (str):
        per_page (int | Unset):  Default: 10.
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetTranscodersByTranscoderIdStoragesResponseDefaultType0 | GetTranscodersByTranscoderIdStoragesResponseDefaultType1 | StoragesReadSchema]
    """

    kwargs = _get_kwargs(
        transcoder_id=transcoder_id,
        per_page=per_page,
        last_id=last_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    transcoder_id: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = 10,
    last_id: str | Unset = UNSET,
) -> (
    Any
    | GetTranscodersByTranscoderIdStoragesResponseDefaultType0
    | GetTranscodersByTranscoderIdStoragesResponseDefaultType1
    | StoragesReadSchema
    | None
):
    """Get storages linked to a transcoder


    Required roles:
     - can_read_transcoders

    Args:
        transcoder_id (str):
        per_page (int | Unset):  Default: 10.
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetTranscodersByTranscoderIdStoragesResponseDefaultType0 | GetTranscodersByTranscoderIdStoragesResponseDefaultType1 | StoragesReadSchema
    """

    return (
        await asyncio_detailed(
            transcoder_id=transcoder_id,
            client=client,
            per_page=per_page,
            last_id=last_id,
        )
    ).parsed
