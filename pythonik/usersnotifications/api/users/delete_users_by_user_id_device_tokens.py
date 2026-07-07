from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_users_by_user_id_device_tokens_response_default_type_0 import (
    DeleteUsersByUserIdDeviceTokensResponseDefaultType0,
)
from ...models.delete_users_by_user_id_device_tokens_response_default_type_1 import (
    DeleteUsersByUserIdDeviceTokensResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    user_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/users/{user_id}/device_tokens/".format(
            user_id=quote(str(user_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | DeleteUsersByUserIdDeviceTokensResponseDefaultType0
    | DeleteUsersByUserIdDeviceTokensResponseDefaultType1
):
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    def _parse_response_default(
        data: object,
    ) -> (
        DeleteUsersByUserIdDeviceTokensResponseDefaultType0
        | DeleteUsersByUserIdDeviceTokensResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                DeleteUsersByUserIdDeviceTokensResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            DeleteUsersByUserIdDeviceTokensResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | DeleteUsersByUserIdDeviceTokensResponseDefaultType0
    | DeleteUsersByUserIdDeviceTokensResponseDefaultType1
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
) -> Response[
    Any
    | DeleteUsersByUserIdDeviceTokensResponseDefaultType0
    | DeleteUsersByUserIdDeviceTokensResponseDefaultType1
]:
    """Unregister all device tokens for a user (e.g., on account deletion)

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteUsersByUserIdDeviceTokensResponseDefaultType0 | DeleteUsersByUserIdDeviceTokensResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | DeleteUsersByUserIdDeviceTokensResponseDefaultType0
    | DeleteUsersByUserIdDeviceTokensResponseDefaultType1
    | None
):
    """Unregister all device tokens for a user (e.g., on account deletion)

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteUsersByUserIdDeviceTokensResponseDefaultType0 | DeleteUsersByUserIdDeviceTokensResponseDefaultType1
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | DeleteUsersByUserIdDeviceTokensResponseDefaultType0
    | DeleteUsersByUserIdDeviceTokensResponseDefaultType1
]:
    """Unregister all device tokens for a user (e.g., on account deletion)

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteUsersByUserIdDeviceTokensResponseDefaultType0 | DeleteUsersByUserIdDeviceTokensResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | DeleteUsersByUserIdDeviceTokensResponseDefaultType0
    | DeleteUsersByUserIdDeviceTokensResponseDefaultType1
    | None
):
    """Unregister all device tokens for a user (e.g., on account deletion)

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteUsersByUserIdDeviceTokensResponseDefaultType0 | DeleteUsersByUserIdDeviceTokensResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
        )
    ).parsed
