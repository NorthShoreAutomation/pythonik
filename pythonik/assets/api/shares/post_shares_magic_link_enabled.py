from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.magic_link_check_setting_schema import MagicLinkCheckSettingSchema
from ...models.post_shares_magic_link_enabled_response_200 import (
    PostSharesMagicLinkEnabledResponse200,
)
from ...models.post_shares_magic_link_enabled_response_default import (
    PostSharesMagicLinkEnabledResponseDefault,
)
from ...types import Response


def _get_kwargs(
    *,
    body: MagicLinkCheckSettingSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/shares/magic_link/enabled/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | PostSharesMagicLinkEnabledResponse200
    | PostSharesMagicLinkEnabledResponseDefault
):
    if response.status_code == 200:
        response_200 = PostSharesMagicLinkEnabledResponse200.from_dict(response.json())

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

    response_default = PostSharesMagicLinkEnabledResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostSharesMagicLinkEnabledResponse200
    | PostSharesMagicLinkEnabledResponseDefault
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: MagicLinkCheckSettingSchema,
) -> Response[
    Any
    | PostSharesMagicLinkEnabledResponse200
    | PostSharesMagicLinkEnabledResponseDefault
]:
    """Check if magic link authentication is enabled for the share's system domain.

    Args:
        body (MagicLinkCheckSettingSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostSharesMagicLinkEnabledResponse200 | PostSharesMagicLinkEnabledResponseDefault]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: MagicLinkCheckSettingSchema,
) -> (
    Any
    | PostSharesMagicLinkEnabledResponse200
    | PostSharesMagicLinkEnabledResponseDefault
    | None
):
    """Check if magic link authentication is enabled for the share's system domain.

    Args:
        body (MagicLinkCheckSettingSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostSharesMagicLinkEnabledResponse200 | PostSharesMagicLinkEnabledResponseDefault
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: MagicLinkCheckSettingSchema,
) -> Response[
    Any
    | PostSharesMagicLinkEnabledResponse200
    | PostSharesMagicLinkEnabledResponseDefault
]:
    """Check if magic link authentication is enabled for the share's system domain.

    Args:
        body (MagicLinkCheckSettingSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostSharesMagicLinkEnabledResponse200 | PostSharesMagicLinkEnabledResponseDefault]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: MagicLinkCheckSettingSchema,
) -> (
    Any
    | PostSharesMagicLinkEnabledResponse200
    | PostSharesMagicLinkEnabledResponseDefault
    | None
):
    """Check if magic link authentication is enabled for the share's system domain.

    Args:
        body (MagicLinkCheckSettingSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostSharesMagicLinkEnabledResponse200 | PostSharesMagicLinkEnabledResponseDefault
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
