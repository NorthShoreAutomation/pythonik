from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.notification_schema import NotificationSchema
from ...models.post_notifications_system_response_default import (
    PostNotificationsSystemResponseDefault,
)
from ...models.system_notification_schema import SystemNotificationSchema
from ...types import Response


def _get_kwargs(
    *,
    body: SystemNotificationSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/notifications/system/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | NotificationSchema | PostNotificationsSystemResponseDefault:
    if response.status_code == 201:
        response_201 = NotificationSchema.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = PostNotificationsSystemResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | NotificationSchema | PostNotificationsSystemResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SystemNotificationSchema,
) -> Response[Any | NotificationSchema | PostNotificationsSystemResponseDefault]:
    """Create a new system notification

    Args:
        body (SystemNotificationSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | NotificationSchema | PostNotificationsSystemResponseDefault]
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
    body: SystemNotificationSchema,
) -> Any | NotificationSchema | PostNotificationsSystemResponseDefault | None:
    """Create a new system notification

    Args:
        body (SystemNotificationSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | NotificationSchema | PostNotificationsSystemResponseDefault
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SystemNotificationSchema,
) -> Response[Any | NotificationSchema | PostNotificationsSystemResponseDefault]:
    """Create a new system notification

    Args:
        body (SystemNotificationSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | NotificationSchema | PostNotificationsSystemResponseDefault]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SystemNotificationSchema,
) -> Any | NotificationSchema | PostNotificationsSystemResponseDefault | None:
    """Create a new system notification

    Args:
        body (SystemNotificationSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | NotificationSchema | PostNotificationsSystemResponseDefault
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
