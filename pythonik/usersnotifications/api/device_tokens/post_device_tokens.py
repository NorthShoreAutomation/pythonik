from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.device_token_schema import DeviceTokenSchema
from ...models.post_device_tokens_response_default import (
    PostDeviceTokensResponseDefault,
)
from ...types import Response


def _get_kwargs(
    *,
    body: DeviceTokenSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/device_tokens/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DeviceTokenSchema | PostDeviceTokensResponseDefault:
    if response.status_code == 200:
        response_200 = DeviceTokenSchema.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = DeviceTokenSchema.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    response_default = PostDeviceTokensResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DeviceTokenSchema | PostDeviceTokensResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DeviceTokenSchema,
) -> Response[Any | DeviceTokenSchema | PostDeviceTokensResponseDefault]:
    """Register a new device token for push notifications

    Args:
        body (DeviceTokenSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeviceTokenSchema | PostDeviceTokensResponseDefault]
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
    body: DeviceTokenSchema,
) -> Any | DeviceTokenSchema | PostDeviceTokensResponseDefault | None:
    """Register a new device token for push notifications

    Args:
        body (DeviceTokenSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeviceTokenSchema | PostDeviceTokensResponseDefault
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DeviceTokenSchema,
) -> Response[Any | DeviceTokenSchema | PostDeviceTokensResponseDefault]:
    """Register a new device token for push notifications

    Args:
        body (DeviceTokenSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeviceTokenSchema | PostDeviceTokensResponseDefault]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: DeviceTokenSchema,
) -> Any | DeviceTokenSchema | PostDeviceTokensResponseDefault | None:
    """Register a new device token for push notifications

    Args:
        body (DeviceTokenSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeviceTokenSchema | PostDeviceTokensResponseDefault
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
