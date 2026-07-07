from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_notifications_by_notification_id_response_default_type_0 import (
    DeleteNotificationsByNotificationIdResponseDefaultType0,
)
from ...models.delete_notifications_by_notification_id_response_default_type_1 import (
    DeleteNotificationsByNotificationIdResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    notification_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/notifications/{notification_id}/".format(
            notification_id=quote(str(notification_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | DeleteNotificationsByNotificationIdResponseDefaultType0
    | DeleteNotificationsByNotificationIdResponseDefaultType1
):
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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
        DeleteNotificationsByNotificationIdResponseDefaultType0
        | DeleteNotificationsByNotificationIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                DeleteNotificationsByNotificationIdResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            DeleteNotificationsByNotificationIdResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | DeleteNotificationsByNotificationIdResponseDefaultType0
    | DeleteNotificationsByNotificationIdResponseDefaultType1
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
    | DeleteNotificationsByNotificationIdResponseDefaultType0
    | DeleteNotificationsByNotificationIdResponseDefaultType1
]:
    """Delete a particular notification by id


    Required roles:
     - can_delete_notifications

    Args:
        notification_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteNotificationsByNotificationIdResponseDefaultType0 | DeleteNotificationsByNotificationIdResponseDefaultType1]
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
    | DeleteNotificationsByNotificationIdResponseDefaultType0
    | DeleteNotificationsByNotificationIdResponseDefaultType1
    | None
):
    """Delete a particular notification by id


    Required roles:
     - can_delete_notifications

    Args:
        notification_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteNotificationsByNotificationIdResponseDefaultType0 | DeleteNotificationsByNotificationIdResponseDefaultType1
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
    | DeleteNotificationsByNotificationIdResponseDefaultType0
    | DeleteNotificationsByNotificationIdResponseDefaultType1
]:
    """Delete a particular notification by id


    Required roles:
     - can_delete_notifications

    Args:
        notification_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteNotificationsByNotificationIdResponseDefaultType0 | DeleteNotificationsByNotificationIdResponseDefaultType1]
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
    | DeleteNotificationsByNotificationIdResponseDefaultType0
    | DeleteNotificationsByNotificationIdResponseDefaultType1
    | None
):
    """Delete a particular notification by id


    Required roles:
     - can_delete_notifications

    Args:
        notification_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteNotificationsByNotificationIdResponseDefaultType0 | DeleteNotificationsByNotificationIdResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            notification_id=notification_id,
            client=client,
        )
    ).parsed
