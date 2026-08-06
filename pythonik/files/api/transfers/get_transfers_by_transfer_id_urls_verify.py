from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_transfers_by_transfer_id_urls_verify_response_default import (
    GetTransfersByTransferIdUrlsVerifyResponseDefault,
)
from ...types import UNSET, Response


def _get_kwargs(
    transfer_id: str,
    *,
    user_id: str,
    signature: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["user_id"] = user_id

    params["signature"] = signature

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/transfers/{transfer_id}/urls/verify/".format(
            transfer_id=quote(str(transfer_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetTransfersByTransferIdUrlsVerifyResponseDefault:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    response_default = GetTransfersByTransferIdUrlsVerifyResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetTransfersByTransferIdUrlsVerifyResponseDefault]:
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
    user_id: str,
    signature: str,
) -> Response[Any | GetTransfersByTransferIdUrlsVerifyResponseDefault]:
    """Verifies the signature of a url

    Args:
        transfer_id (str):
        user_id (str):
        signature (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetTransfersByTransferIdUrlsVerifyResponseDefault]
    """

    kwargs = _get_kwargs(
        transfer_id=transfer_id,
        user_id=user_id,
        signature=signature,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    transfer_id: str,
    *,
    client: AuthenticatedClient | Client,
    user_id: str,
    signature: str,
) -> Any | GetTransfersByTransferIdUrlsVerifyResponseDefault | None:
    """Verifies the signature of a url

    Args:
        transfer_id (str):
        user_id (str):
        signature (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetTransfersByTransferIdUrlsVerifyResponseDefault
    """

    return sync_detailed(
        transfer_id=transfer_id,
        client=client,
        user_id=user_id,
        signature=signature,
    ).parsed


async def asyncio_detailed(
    transfer_id: str,
    *,
    client: AuthenticatedClient | Client,
    user_id: str,
    signature: str,
) -> Response[Any | GetTransfersByTransferIdUrlsVerifyResponseDefault]:
    """Verifies the signature of a url

    Args:
        transfer_id (str):
        user_id (str):
        signature (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetTransfersByTransferIdUrlsVerifyResponseDefault]
    """

    kwargs = _get_kwargs(
        transfer_id=transfer_id,
        user_id=user_id,
        signature=signature,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    transfer_id: str,
    *,
    client: AuthenticatedClient | Client,
    user_id: str,
    signature: str,
) -> Any | GetTransfersByTransferIdUrlsVerifyResponseDefault | None:
    """Verifies the signature of a url

    Args:
        transfer_id (str):
        user_id (str):
        signature (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetTransfersByTransferIdUrlsVerifyResponseDefault
    """

    return (
        await asyncio_detailed(
            transfer_id=transfer_id,
            client=client,
            user_id=user_id,
            signature=signature,
        )
    ).parsed
