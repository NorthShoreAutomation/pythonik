from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_transcoders_by_transcoder_id_options_by_option_name_response_default import (
    GetTranscodersByTranscoderIdOptionsByOptionNameResponseDefault,
)
from ...models.transcoder_options_schema import TranscoderOptionsSchema
from ...types import Response


def _get_kwargs(
    transcoder_id: str,
    option_name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/transcoders/{transcoder_id}/options/{option_name}/".format(
            transcoder_id=quote(str(transcoder_id), safe=""),
            option_name=quote(str(option_name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetTranscodersByTranscoderIdOptionsByOptionNameResponseDefault
    | TranscoderOptionsSchema
):
    if response.status_code == 200:
        response_200 = TranscoderOptionsSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = (
        GetTranscodersByTranscoderIdOptionsByOptionNameResponseDefault.from_dict(
            response.json()
        )
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetTranscodersByTranscoderIdOptionsByOptionNameResponseDefault
    | TranscoderOptionsSchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    transcoder_id: str,
    option_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetTranscodersByTranscoderIdOptionsByOptionNameResponseDefault
    | TranscoderOptionsSchema
]:
    """Get options for a transcoder configuration.


    Required roles:
     - can_read_transcoders

    Args:
        transcoder_id (str):
        option_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetTranscodersByTranscoderIdOptionsByOptionNameResponseDefault | TranscoderOptionsSchema]
    """

    kwargs = _get_kwargs(
        transcoder_id=transcoder_id,
        option_name=option_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    transcoder_id: str,
    option_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetTranscodersByTranscoderIdOptionsByOptionNameResponseDefault
    | TranscoderOptionsSchema
    | None
):
    """Get options for a transcoder configuration.


    Required roles:
     - can_read_transcoders

    Args:
        transcoder_id (str):
        option_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetTranscodersByTranscoderIdOptionsByOptionNameResponseDefault | TranscoderOptionsSchema
    """

    return sync_detailed(
        transcoder_id=transcoder_id,
        option_name=option_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    transcoder_id: str,
    option_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetTranscodersByTranscoderIdOptionsByOptionNameResponseDefault
    | TranscoderOptionsSchema
]:
    """Get options for a transcoder configuration.


    Required roles:
     - can_read_transcoders

    Args:
        transcoder_id (str):
        option_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetTranscodersByTranscoderIdOptionsByOptionNameResponseDefault | TranscoderOptionsSchema]
    """

    kwargs = _get_kwargs(
        transcoder_id=transcoder_id,
        option_name=option_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    transcoder_id: str,
    option_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetTranscodersByTranscoderIdOptionsByOptionNameResponseDefault
    | TranscoderOptionsSchema
    | None
):
    """Get options for a transcoder configuration.


    Required roles:
     - can_read_transcoders

    Args:
        transcoder_id (str):
        option_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetTranscodersByTranscoderIdOptionsByOptionNameResponseDefault | TranscoderOptionsSchema
    """

    return (
        await asyncio_detailed(
            transcoder_id=transcoder_id,
            option_name=option_name,
            client=client,
        )
    ).parsed
