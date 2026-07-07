from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.device_token_schema import DeviceTokenSchema
from ...models.post_users_by_user_id_device_tokens_response_default_type_0 import (
    PostUsersByUserIdDeviceTokensResponseDefaultType0,
)
from ...models.post_users_by_user_id_device_tokens_response_default_type_1 import (
    PostUsersByUserIdDeviceTokensResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    user_id: str,
    *,
    body: DeviceTokenSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/users/{user_id}/device_tokens/".format(
            user_id=quote(str(user_id), safe=""),
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
    | DeviceTokenSchema
    | PostUsersByUserIdDeviceTokensResponseDefaultType0
    | PostUsersByUserIdDeviceTokensResponseDefaultType1
):
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

    def _parse_response_default(
        data: object,
    ) -> (
        PostUsersByUserIdDeviceTokensResponseDefaultType0
        | PostUsersByUserIdDeviceTokensResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                PostUsersByUserIdDeviceTokensResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PostUsersByUserIdDeviceTokensResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | DeviceTokenSchema
    | PostUsersByUserIdDeviceTokensResponseDefaultType0
    | PostUsersByUserIdDeviceTokensResponseDefaultType1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DeviceTokenSchema,
) -> Response[
    Any
    | DeviceTokenSchema
    | PostUsersByUserIdDeviceTokensResponseDefaultType0
    | PostUsersByUserIdDeviceTokensResponseDefaultType1
]:
    """Register a new device token for push notifications

    Args:
        user_id (str):
        body (DeviceTokenSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeviceTokenSchema | PostUsersByUserIdDeviceTokensResponseDefaultType0 | PostUsersByUserIdDeviceTokensResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DeviceTokenSchema,
) -> (
    Any
    | DeviceTokenSchema
    | PostUsersByUserIdDeviceTokensResponseDefaultType0
    | PostUsersByUserIdDeviceTokensResponseDefaultType1
    | None
):
    """Register a new device token for push notifications

    Args:
        user_id (str):
        body (DeviceTokenSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeviceTokenSchema | PostUsersByUserIdDeviceTokensResponseDefaultType0 | PostUsersByUserIdDeviceTokensResponseDefaultType1
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DeviceTokenSchema,
) -> Response[
    Any
    | DeviceTokenSchema
    | PostUsersByUserIdDeviceTokensResponseDefaultType0
    | PostUsersByUserIdDeviceTokensResponseDefaultType1
]:
    """Register a new device token for push notifications

    Args:
        user_id (str):
        body (DeviceTokenSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeviceTokenSchema | PostUsersByUserIdDeviceTokensResponseDefaultType0 | PostUsersByUserIdDeviceTokensResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DeviceTokenSchema,
) -> (
    Any
    | DeviceTokenSchema
    | PostUsersByUserIdDeviceTokensResponseDefaultType0
    | PostUsersByUserIdDeviceTokensResponseDefaultType1
    | None
):
    """Register a new device token for push notifications

    Args:
        user_id (str):
        body (DeviceTokenSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeviceTokenSchema | PostUsersByUserIdDeviceTokensResponseDefaultType0 | PostUsersByUserIdDeviceTokensResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            body=body,
        )
    ).parsed
