from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.notification_schema import NotificationSchema
from ...models.put_notifications_by_notification_id_read_response_default import (
    PutNotificationsByNotificationIdReadResponseDefault,
)
from ...types import Response


def _get_kwargs(
    notification_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/notifications/{notification_id}/read/".format(
            notification_id=quote(str(notification_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | NotificationSchema | PutNotificationsByNotificationIdReadResponseDefault:
    if response.status_code == 200:
        response_200 = NotificationSchema.from_dict(response.json())

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

    response_default = PutNotificationsByNotificationIdReadResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | NotificationSchema | PutNotificationsByNotificationIdReadResponseDefault
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    notification_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any | NotificationSchema | PutNotificationsByNotificationIdReadResponseDefault
]:
    """Mark a particular notification as read


    Required roles:
     - can_read_notifications

    Args:
        notification_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | NotificationSchema | PutNotificationsByNotificationIdReadResponseDefault]
    """

    kwargs = _get_kwargs(
        notification_id=notification_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    notification_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | NotificationSchema
    | PutNotificationsByNotificationIdReadResponseDefault
    | None
):
    """Mark a particular notification as read


    Required roles:
     - can_read_notifications

    Args:
        notification_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | NotificationSchema | PutNotificationsByNotificationIdReadResponseDefault
    """

    return sync_detailed(
        notification_id=notification_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    notification_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any | NotificationSchema | PutNotificationsByNotificationIdReadResponseDefault
]:
    """Mark a particular notification as read


    Required roles:
     - can_read_notifications

    Args:
        notification_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | NotificationSchema | PutNotificationsByNotificationIdReadResponseDefault]
    """

    kwargs = _get_kwargs(
        notification_id=notification_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    notification_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | NotificationSchema
    | PutNotificationsByNotificationIdReadResponseDefault
    | None
):
    """Mark a particular notification as read


    Required roles:
     - can_read_notifications

    Args:
        notification_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | NotificationSchema | PutNotificationsByNotificationIdReadResponseDefault
    """

    return (
        await asyncio_detailed(
            notification_id=notification_id,
            client=client,
        )
    ).parsed
