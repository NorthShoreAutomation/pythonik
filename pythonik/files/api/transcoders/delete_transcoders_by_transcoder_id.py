from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_transcoders_by_transcoder_id_response_default_type_0 import (
    DeleteTranscodersByTranscoderIdResponseDefaultType0,
)
from ...models.delete_transcoders_by_transcoder_id_response_default_type_1 import (
    DeleteTranscodersByTranscoderIdResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    transcoder_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/transcoders/{transcoder_id}/".format(
            transcoder_id=quote(str(transcoder_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | DeleteTranscodersByTranscoderIdResponseDefaultType0
    | DeleteTranscodersByTranscoderIdResponseDefaultType1
):
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    def _parse_response_default(
        data: object,
    ) -> (
        DeleteTranscodersByTranscoderIdResponseDefaultType0
        | DeleteTranscodersByTranscoderIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                DeleteTranscodersByTranscoderIdResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            DeleteTranscodersByTranscoderIdResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | DeleteTranscodersByTranscoderIdResponseDefaultType0
    | DeleteTranscodersByTranscoderIdResponseDefaultType1
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
) -> Response[
    Any
    | DeleteTranscodersByTranscoderIdResponseDefaultType0
    | DeleteTranscodersByTranscoderIdResponseDefaultType1
]:
    """Delete a particular transcoder by id


    Required roles:
     - can_delete_transcoders

    Args:
        transcoder_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteTranscodersByTranscoderIdResponseDefaultType0 | DeleteTranscodersByTranscoderIdResponseDefaultType1]
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
) -> (
    Any
    | DeleteTranscodersByTranscoderIdResponseDefaultType0
    | DeleteTranscodersByTranscoderIdResponseDefaultType1
    | None
):
    """Delete a particular transcoder by id


    Required roles:
     - can_delete_transcoders

    Args:
        transcoder_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteTranscodersByTranscoderIdResponseDefaultType0 | DeleteTranscodersByTranscoderIdResponseDefaultType1
    """

    return sync_detailed(
        transcoder_id=transcoder_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    transcoder_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | DeleteTranscodersByTranscoderIdResponseDefaultType0
    | DeleteTranscodersByTranscoderIdResponseDefaultType1
]:
    """Delete a particular transcoder by id


    Required roles:
     - can_delete_transcoders

    Args:
        transcoder_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteTranscodersByTranscoderIdResponseDefaultType0 | DeleteTranscodersByTranscoderIdResponseDefaultType1]
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
) -> (
    Any
    | DeleteTranscodersByTranscoderIdResponseDefaultType0
    | DeleteTranscodersByTranscoderIdResponseDefaultType1
    | None
):
    """Delete a particular transcoder by id


    Required roles:
     - can_delete_transcoders

    Args:
        transcoder_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteTranscodersByTranscoderIdResponseDefaultType0 | DeleteTranscodersByTranscoderIdResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            transcoder_id=transcoder_id,
            client=client,
        )
    ).parsed
