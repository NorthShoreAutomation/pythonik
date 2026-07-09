from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.magic_link_request_schema import MagicLinkRequestSchema
from ...models.post_shares_by_share_id_magic_link_request_response_200 import (
    PostSharesByShareIdMagicLinkRequestResponse200,
)
from ...models.post_shares_by_share_id_magic_link_request_response_default import (
    PostSharesByShareIdMagicLinkRequestResponseDefault,
)
from ...types import Response


def _get_kwargs(
    share_id: str,
    *,
    body: MagicLinkRequestSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/shares/{share_id}/magic_link/request/".format(
            share_id=quote(str(share_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | PostSharesByShareIdMagicLinkRequestResponse200
    | PostSharesByShareIdMagicLinkRequestResponseDefault
):
    if response.status_code == 200:
        response_200 = PostSharesByShareIdMagicLinkRequestResponse200.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429

    response_default = PostSharesByShareIdMagicLinkRequestResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostSharesByShareIdMagicLinkRequestResponse200
    | PostSharesByShareIdMagicLinkRequestResponseDefault
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    share_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: MagicLinkRequestSchema,
) -> Response[
    Any
    | PostSharesByShareIdMagicLinkRequestResponse200
    | PostSharesByShareIdMagicLinkRequestResponseDefault
]:
    """Request a magic link for share access.

     <br/>Creates a ShareUser and generates a magic link token for the recipient.

    Args:
        share_id (str):
        body (MagicLinkRequestSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostSharesByShareIdMagicLinkRequestResponse200 | PostSharesByShareIdMagicLinkRequestResponseDefault]
    """

    kwargs = _get_kwargs(
        share_id=share_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    share_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: MagicLinkRequestSchema,
) -> (
    Any
    | PostSharesByShareIdMagicLinkRequestResponse200
    | PostSharesByShareIdMagicLinkRequestResponseDefault
    | None
):
    """Request a magic link for share access.

     <br/>Creates a ShareUser and generates a magic link token for the recipient.

    Args:
        share_id (str):
        body (MagicLinkRequestSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostSharesByShareIdMagicLinkRequestResponse200 | PostSharesByShareIdMagicLinkRequestResponseDefault
    """

    return sync_detailed(
        share_id=share_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    share_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: MagicLinkRequestSchema,
) -> Response[
    Any
    | PostSharesByShareIdMagicLinkRequestResponse200
    | PostSharesByShareIdMagicLinkRequestResponseDefault
]:
    """Request a magic link for share access.

     <br/>Creates a ShareUser and generates a magic link token for the recipient.

    Args:
        share_id (str):
        body (MagicLinkRequestSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostSharesByShareIdMagicLinkRequestResponse200 | PostSharesByShareIdMagicLinkRequestResponseDefault]
    """

    kwargs = _get_kwargs(
        share_id=share_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    share_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: MagicLinkRequestSchema,
) -> (
    Any
    | PostSharesByShareIdMagicLinkRequestResponse200
    | PostSharesByShareIdMagicLinkRequestResponseDefault
    | None
):
    """Request a magic link for share access.

     <br/>Creates a ShareUser and generates a magic link token for the recipient.

    Args:
        share_id (str):
        body (MagicLinkRequestSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostSharesByShareIdMagicLinkRequestResponse200 | PostSharesByShareIdMagicLinkRequestResponseDefault
    """

    return (
        await asyncio_detailed(
            share_id=share_id,
            client=client,
            body=body,
        )
    ).parsed
