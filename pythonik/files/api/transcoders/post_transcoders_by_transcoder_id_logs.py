from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_transcoders_by_transcoder_id_logs_response_200 import (
    PostTranscodersByTranscoderIdLogsResponse200,
)
from ...models.post_transcoders_by_transcoder_id_logs_response_default import (
    PostTranscodersByTranscoderIdLogsResponseDefault,
)
from ...types import UNSET, Response


def _get_kwargs(
    transcoder_id: str,
    *,
    filename: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["filename"] = filename

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/transcoders/{transcoder_id}/logs/".format(
            transcoder_id=quote(str(transcoder_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | PostTranscodersByTranscoderIdLogsResponse200
    | PostTranscodersByTranscoderIdLogsResponseDefault
):
    if response.status_code == 200:
        response_200 = PostTranscodersByTranscoderIdLogsResponse200.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = PostTranscodersByTranscoderIdLogsResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostTranscodersByTranscoderIdLogsResponse200
    | PostTranscodersByTranscoderIdLogsResponseDefault
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
    filename: str,
) -> Response[
    Any
    | PostTranscodersByTranscoderIdLogsResponse200
    | PostTranscodersByTranscoderIdLogsResponseDefault
]:
    """Upload transcoder logs


    Required roles:
     - is_storage_worker

    Args:
        transcoder_id (str):
        filename (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostTranscodersByTranscoderIdLogsResponse200 | PostTranscodersByTranscoderIdLogsResponseDefault]
    """

    kwargs = _get_kwargs(
        transcoder_id=transcoder_id,
        filename=filename,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    transcoder_id: str,
    *,
    client: AuthenticatedClient | Client,
    filename: str,
) -> (
    Any
    | PostTranscodersByTranscoderIdLogsResponse200
    | PostTranscodersByTranscoderIdLogsResponseDefault
    | None
):
    """Upload transcoder logs


    Required roles:
     - is_storage_worker

    Args:
        transcoder_id (str):
        filename (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostTranscodersByTranscoderIdLogsResponse200 | PostTranscodersByTranscoderIdLogsResponseDefault
    """

    return sync_detailed(
        transcoder_id=transcoder_id,
        client=client,
        filename=filename,
    ).parsed


async def asyncio_detailed(
    transcoder_id: str,
    *,
    client: AuthenticatedClient | Client,
    filename: str,
) -> Response[
    Any
    | PostTranscodersByTranscoderIdLogsResponse200
    | PostTranscodersByTranscoderIdLogsResponseDefault
]:
    """Upload transcoder logs


    Required roles:
     - is_storage_worker

    Args:
        transcoder_id (str):
        filename (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostTranscodersByTranscoderIdLogsResponse200 | PostTranscodersByTranscoderIdLogsResponseDefault]
    """

    kwargs = _get_kwargs(
        transcoder_id=transcoder_id,
        filename=filename,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    transcoder_id: str,
    *,
    client: AuthenticatedClient | Client,
    filename: str,
) -> (
    Any
    | PostTranscodersByTranscoderIdLogsResponse200
    | PostTranscodersByTranscoderIdLogsResponseDefault
    | None
):
    """Upload transcoder logs


    Required roles:
     - is_storage_worker

    Args:
        transcoder_id (str):
        filename (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostTranscodersByTranscoderIdLogsResponse200 | PostTranscodersByTranscoderIdLogsResponseDefault
    """

    return (
        await asyncio_detailed(
            transcoder_id=transcoder_id,
            client=client,
            filename=filename,
        )
    ).parsed
