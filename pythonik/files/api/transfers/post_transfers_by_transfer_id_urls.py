from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_transfers_by_transfer_id_urls_response_default import (
    PostTransfersByTransferIdUrlsResponseDefault,
)
from ...models.transfer_signed_url_schema import TransferSignedURLSchema
from ...types import Response


def _get_kwargs(
    transfer_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/transfers/{transfer_id}/urls/".format(
            transfer_id=quote(str(transfer_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostTransfersByTransferIdUrlsResponseDefault | TransferSignedURLSchema:
    if response.status_code == 200:
        response_200 = TransferSignedURLSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = PostTransfersByTransferIdUrlsResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | PostTransfersByTransferIdUrlsResponseDefault | TransferSignedURLSchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    transfer_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any | PostTransfersByTransferIdUrlsResponseDefault | TransferSignedURLSchema
]:
    """Generates a url for direct file downloads (for IGSs)

    Args:
        transfer_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostTransfersByTransferIdUrlsResponseDefault | TransferSignedURLSchema]
    """

    kwargs = _get_kwargs(
        transfer_id=transfer_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    transfer_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any | PostTransfersByTransferIdUrlsResponseDefault | TransferSignedURLSchema | None
):
    """Generates a url for direct file downloads (for IGSs)

    Args:
        transfer_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostTransfersByTransferIdUrlsResponseDefault | TransferSignedURLSchema
    """

    return sync_detailed(
        transfer_id=transfer_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    transfer_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any | PostTransfersByTransferIdUrlsResponseDefault | TransferSignedURLSchema
]:
    """Generates a url for direct file downloads (for IGSs)

    Args:
        transfer_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostTransfersByTransferIdUrlsResponseDefault | TransferSignedURLSchema]
    """

    kwargs = _get_kwargs(
        transfer_id=transfer_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    transfer_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any | PostTransfersByTransferIdUrlsResponseDefault | TransferSignedURLSchema | None
):
    """Generates a url for direct file downloads (for IGSs)

    Args:
        transfer_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostTransfersByTransferIdUrlsResponseDefault | TransferSignedURLSchema
    """

    return (
        await asyncio_detailed(
            transfer_id=transfer_id,
            client=client,
        )
    ).parsed
