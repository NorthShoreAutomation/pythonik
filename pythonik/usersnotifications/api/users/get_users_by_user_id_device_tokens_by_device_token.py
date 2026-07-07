from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.device_token_schema import DeviceTokenSchema
from ...models.get_users_by_user_id_device_tokens_by_device_token_response_default_type_0 import (
    GetUsersByUserIdDeviceTokensByDeviceTokenResponseDefaultType0,
)
from ...models.get_users_by_user_id_device_tokens_by_device_token_response_default_type_1 import (
    GetUsersByUserIdDeviceTokensByDeviceTokenResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    user_id: str,
    device_token: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/users/{user_id}/device_tokens/{device_token}/".format(
            user_id=quote(str(user_id), safe=""),
            device_token=quote(str(device_token), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | DeviceTokenSchema
    | GetUsersByUserIdDeviceTokensByDeviceTokenResponseDefaultType0
    | GetUsersByUserIdDeviceTokensByDeviceTokenResponseDefaultType1
):
    if response.status_code == 200:
        response_200 = DeviceTokenSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    def _parse_response_default(
        data: object,
    ) -> (
        GetUsersByUserIdDeviceTokensByDeviceTokenResponseDefaultType0
        | GetUsersByUserIdDeviceTokensByDeviceTokenResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetUsersByUserIdDeviceTokensByDeviceTokenResponseDefaultType0.from_dict(
                    data
                )
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            GetUsersByUserIdDeviceTokensByDeviceTokenResponseDefaultType1.from_dict(
                data
            )
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | DeviceTokenSchema
    | GetUsersByUserIdDeviceTokensByDeviceTokenResponseDefaultType0
    | GetUsersByUserIdDeviceTokensByDeviceTokenResponseDefaultType1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: str,
    device_token: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | DeviceTokenSchema
    | GetUsersByUserIdDeviceTokensByDeviceTokenResponseDefaultType0
    | GetUsersByUserIdDeviceTokensByDeviceTokenResponseDefaultType1
]:
    """Returns a particular device token

    Args:
        user_id (str):
        device_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeviceTokenSchema | GetUsersByUserIdDeviceTokensByDeviceTokenResponseDefaultType0 | GetUsersByUserIdDeviceTokensByDeviceTokenResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        device_token=device_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: str,
    device_token: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | DeviceTokenSchema
    | GetUsersByUserIdDeviceTokensByDeviceTokenResponseDefaultType0
    | GetUsersByUserIdDeviceTokensByDeviceTokenResponseDefaultType1
    | None
):
    """Returns a particular device token

    Args:
        user_id (str):
        device_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeviceTokenSchema | GetUsersByUserIdDeviceTokensByDeviceTokenResponseDefaultType0 | GetUsersByUserIdDeviceTokensByDeviceTokenResponseDefaultType1
    """

    return sync_detailed(
        user_id=user_id,
        device_token=device_token,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    device_token: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | DeviceTokenSchema
    | GetUsersByUserIdDeviceTokensByDeviceTokenResponseDefaultType0
    | GetUsersByUserIdDeviceTokensByDeviceTokenResponseDefaultType1
]:
    """Returns a particular device token

    Args:
        user_id (str):
        device_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeviceTokenSchema | GetUsersByUserIdDeviceTokensByDeviceTokenResponseDefaultType0 | GetUsersByUserIdDeviceTokensByDeviceTokenResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        device_token=device_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    device_token: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | DeviceTokenSchema
    | GetUsersByUserIdDeviceTokensByDeviceTokenResponseDefaultType0
    | GetUsersByUserIdDeviceTokensByDeviceTokenResponseDefaultType1
    | None
):
    """Returns a particular device token

    Args:
        user_id (str):
        device_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeviceTokenSchema | GetUsersByUserIdDeviceTokensByDeviceTokenResponseDefaultType0 | GetUsersByUserIdDeviceTokensByDeviceTokenResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            device_token=device_token,
            client=client,
        )
    ).parsed
