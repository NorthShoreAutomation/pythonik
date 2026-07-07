from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.device_token_schema import DeviceTokenSchema
from ...models.patch_users_by_user_id_device_tokens_by_device_token_response_default_type_0 import (
    PatchUsersByUserIdDeviceTokensByDeviceTokenResponseDefaultType0,
)
from ...models.patch_users_by_user_id_device_tokens_by_device_token_response_default_type_1 import (
    PatchUsersByUserIdDeviceTokensByDeviceTokenResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    user_id: str,
    device_token: str,
    *,
    body: DeviceTokenSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/users/{user_id}/device_tokens/{device_token}/".format(
            user_id=quote(str(user_id), safe=""),
            device_token=quote(str(device_token), safe=""),
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
    | PatchUsersByUserIdDeviceTokensByDeviceTokenResponseDefaultType0
    | PatchUsersByUserIdDeviceTokensByDeviceTokenResponseDefaultType1
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
        PatchUsersByUserIdDeviceTokensByDeviceTokenResponseDefaultType0
        | PatchUsersByUserIdDeviceTokensByDeviceTokenResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = PatchUsersByUserIdDeviceTokensByDeviceTokenResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PatchUsersByUserIdDeviceTokensByDeviceTokenResponseDefaultType1.from_dict(
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
    | PatchUsersByUserIdDeviceTokensByDeviceTokenResponseDefaultType0
    | PatchUsersByUserIdDeviceTokensByDeviceTokenResponseDefaultType1
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
    body: DeviceTokenSchema,
) -> Response[
    Any
    | DeviceTokenSchema
    | PatchUsersByUserIdDeviceTokensByDeviceTokenResponseDefaultType0
    | PatchUsersByUserIdDeviceTokensByDeviceTokenResponseDefaultType1
]:
    """Update device token metadata

    Args:
        user_id (str):
        device_token (str):
        body (DeviceTokenSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeviceTokenSchema | PatchUsersByUserIdDeviceTokensByDeviceTokenResponseDefaultType0 | PatchUsersByUserIdDeviceTokensByDeviceTokenResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        device_token=device_token,
        body=body,
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
    body: DeviceTokenSchema,
) -> (
    Any
    | DeviceTokenSchema
    | PatchUsersByUserIdDeviceTokensByDeviceTokenResponseDefaultType0
    | PatchUsersByUserIdDeviceTokensByDeviceTokenResponseDefaultType1
    | None
):
    """Update device token metadata

    Args:
        user_id (str):
        device_token (str):
        body (DeviceTokenSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeviceTokenSchema | PatchUsersByUserIdDeviceTokensByDeviceTokenResponseDefaultType0 | PatchUsersByUserIdDeviceTokensByDeviceTokenResponseDefaultType1
    """

    return sync_detailed(
        user_id=user_id,
        device_token=device_token,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    device_token: str,
    *,
    client: AuthenticatedClient | Client,
    body: DeviceTokenSchema,
) -> Response[
    Any
    | DeviceTokenSchema
    | PatchUsersByUserIdDeviceTokensByDeviceTokenResponseDefaultType0
    | PatchUsersByUserIdDeviceTokensByDeviceTokenResponseDefaultType1
]:
    """Update device token metadata

    Args:
        user_id (str):
        device_token (str):
        body (DeviceTokenSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeviceTokenSchema | PatchUsersByUserIdDeviceTokensByDeviceTokenResponseDefaultType0 | PatchUsersByUserIdDeviceTokensByDeviceTokenResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        device_token=device_token,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    device_token: str,
    *,
    client: AuthenticatedClient | Client,
    body: DeviceTokenSchema,
) -> (
    Any
    | DeviceTokenSchema
    | PatchUsersByUserIdDeviceTokensByDeviceTokenResponseDefaultType0
    | PatchUsersByUserIdDeviceTokensByDeviceTokenResponseDefaultType1
    | None
):
    """Update device token metadata

    Args:
        user_id (str):
        device_token (str):
        body (DeviceTokenSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeviceTokenSchema | PatchUsersByUserIdDeviceTokensByDeviceTokenResponseDefaultType0 | PatchUsersByUserIdDeviceTokensByDeviceTokenResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            device_token=device_token,
            client=client,
            body=body,
        )
    ).parsed
