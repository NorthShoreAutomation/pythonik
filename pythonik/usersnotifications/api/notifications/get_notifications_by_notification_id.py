from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_notifications_by_notification_id_response_default_type_0 import (
    GetNotificationsByNotificationIdResponseDefaultType0,
)
from ...models.get_notifications_by_notification_id_response_default_type_1 import (
    GetNotificationsByNotificationIdResponseDefaultType1,
)
from ...models.notification_schema import NotificationSchema
from ...types import Response


def _get_kwargs(
    notification_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/notifications/{notification_id}/".format(
            notification_id=quote(str(notification_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetNotificationsByNotificationIdResponseDefaultType0
    | GetNotificationsByNotificationIdResponseDefaultType1
    | NotificationSchema
):
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

    def _parse_response_default(
        data: object,
    ) -> (
        GetNotificationsByNotificationIdResponseDefaultType0
        | GetNotificationsByNotificationIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetNotificationsByNotificationIdResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            GetNotificationsByNotificationIdResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetNotificationsByNotificationIdResponseDefaultType0
    | GetNotificationsByNotificationIdResponseDefaultType1
    | NotificationSchema
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
    Any
    | GetNotificationsByNotificationIdResponseDefaultType0
    | GetNotificationsByNotificationIdResponseDefaultType1
    | NotificationSchema
]:
    """Returns a particular notification by id


    Required roles:
     - can_read_notifications

    Args:
        notification_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetNotificationsByNotificationIdResponseDefaultType0 | GetNotificationsByNotificationIdResponseDefaultType1 | NotificationSchema]
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
    | GetNotificationsByNotificationIdResponseDefaultType0
    | GetNotificationsByNotificationIdResponseDefaultType1
    | NotificationSchema
    | None
):
    """Returns a particular notification by id


    Required roles:
     - can_read_notifications

    Args:
        notification_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetNotificationsByNotificationIdResponseDefaultType0 | GetNotificationsByNotificationIdResponseDefaultType1 | NotificationSchema
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
    Any
    | GetNotificationsByNotificationIdResponseDefaultType0
    | GetNotificationsByNotificationIdResponseDefaultType1
    | NotificationSchema
]:
    """Returns a particular notification by id


    Required roles:
     - can_read_notifications

    Args:
        notification_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetNotificationsByNotificationIdResponseDefaultType0 | GetNotificationsByNotificationIdResponseDefaultType1 | NotificationSchema]
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
    | GetNotificationsByNotificationIdResponseDefaultType0
    | GetNotificationsByNotificationIdResponseDefaultType1
    | NotificationSchema
    | None
):
    """Returns a particular notification by id


    Required roles:
     - can_read_notifications

    Args:
        notification_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetNotificationsByNotificationIdResponseDefaultType0 | GetNotificationsByNotificationIdResponseDefaultType1 | NotificationSchema
    """

    return (
        await asyncio_detailed(
            notification_id=notification_id,
            client=client,
        )
    ).parsed
