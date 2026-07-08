from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.notification_setting_schema import NotificationSettingSchema
from ...models.put_notification_settings_by_object_type_by_sub_object_type_by_event_type_by_protocol_response_default import (
    PutNotificationSettingsByObjectTypeBySubObjectTypeByEventTypeByProtocolResponseDefault,
)
from ...types import Response


def _get_kwargs(
    object_type: str,
    sub_object_type: str,
    event_type: str,
    protocol: str,
    *,
    body: NotificationSettingSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/notification_settings/{object_type}/{sub_object_type}/{event_type}/{protocol}/".format(
            object_type=quote(str(object_type), safe=""),
            sub_object_type=quote(str(sub_object_type), safe=""),
            event_type=quote(str(event_type), safe=""),
            protocol=quote(str(protocol), safe=""),
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
    | NotificationSettingSchema
    | PutNotificationSettingsByObjectTypeBySubObjectTypeByEventTypeByProtocolResponseDefault
):
    if response.status_code == 201:
        response_201 = NotificationSettingSchema.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = PutNotificationSettingsByObjectTypeBySubObjectTypeByEventTypeByProtocolResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | NotificationSettingSchema
    | PutNotificationSettingsByObjectTypeBySubObjectTypeByEventTypeByProtocolResponseDefault
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    object_type: str,
    sub_object_type: str,
    event_type: str,
    protocol: str,
    *,
    client: AuthenticatedClient | Client,
    body: NotificationSettingSchema,
) -> Response[
    Any
    | NotificationSettingSchema
    | PutNotificationSettingsByObjectTypeBySubObjectTypeByEventTypeByProtocolResponseDefault
]:
    """Create a new notification_setting

    Args:
        object_type (str):
        sub_object_type (str):
        event_type (str):
        protocol (str):
        body (NotificationSettingSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | NotificationSettingSchema | PutNotificationSettingsByObjectTypeBySubObjectTypeByEventTypeByProtocolResponseDefault]
    """

    kwargs = _get_kwargs(
        object_type=object_type,
        sub_object_type=sub_object_type,
        event_type=event_type,
        protocol=protocol,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    object_type: str,
    sub_object_type: str,
    event_type: str,
    protocol: str,
    *,
    client: AuthenticatedClient | Client,
    body: NotificationSettingSchema,
) -> (
    Any
    | NotificationSettingSchema
    | PutNotificationSettingsByObjectTypeBySubObjectTypeByEventTypeByProtocolResponseDefault
    | None
):
    """Create a new notification_setting

    Args:
        object_type (str):
        sub_object_type (str):
        event_type (str):
        protocol (str):
        body (NotificationSettingSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | NotificationSettingSchema | PutNotificationSettingsByObjectTypeBySubObjectTypeByEventTypeByProtocolResponseDefault
    """

    return sync_detailed(
        object_type=object_type,
        sub_object_type=sub_object_type,
        event_type=event_type,
        protocol=protocol,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    object_type: str,
    sub_object_type: str,
    event_type: str,
    protocol: str,
    *,
    client: AuthenticatedClient | Client,
    body: NotificationSettingSchema,
) -> Response[
    Any
    | NotificationSettingSchema
    | PutNotificationSettingsByObjectTypeBySubObjectTypeByEventTypeByProtocolResponseDefault
]:
    """Create a new notification_setting

    Args:
        object_type (str):
        sub_object_type (str):
        event_type (str):
        protocol (str):
        body (NotificationSettingSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | NotificationSettingSchema | PutNotificationSettingsByObjectTypeBySubObjectTypeByEventTypeByProtocolResponseDefault]
    """

    kwargs = _get_kwargs(
        object_type=object_type,
        sub_object_type=sub_object_type,
        event_type=event_type,
        protocol=protocol,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    object_type: str,
    sub_object_type: str,
    event_type: str,
    protocol: str,
    *,
    client: AuthenticatedClient | Client,
    body: NotificationSettingSchema,
) -> (
    Any
    | NotificationSettingSchema
    | PutNotificationSettingsByObjectTypeBySubObjectTypeByEventTypeByProtocolResponseDefault
    | None
):
    """Create a new notification_setting

    Args:
        object_type (str):
        sub_object_type (str):
        event_type (str):
        protocol (str):
        body (NotificationSettingSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | NotificationSettingSchema | PutNotificationSettingsByObjectTypeBySubObjectTypeByEventTypeByProtocolResponseDefault
    """

    return (
        await asyncio_detailed(
            object_type=object_type,
            sub_object_type=sub_object_type,
            event_type=event_type,
            protocol=protocol,
            client=client,
            body=body,
        )
    ).parsed
