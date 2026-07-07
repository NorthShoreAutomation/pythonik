from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_users_by_user_id_photo_response_default_type_0 import (
    DeleteUsersByUserIdPhotoResponseDefaultType0,
)
from ...models.delete_users_by_user_id_photo_response_default_type_1 import (
    DeleteUsersByUserIdPhotoResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    user_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/users/{user_id}/photo/".format(
            user_id=quote(str(user_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | DeleteUsersByUserIdPhotoResponseDefaultType0
    | DeleteUsersByUserIdPhotoResponseDefaultType1
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
        DeleteUsersByUserIdPhotoResponseDefaultType0
        | DeleteUsersByUserIdPhotoResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                DeleteUsersByUserIdPhotoResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            DeleteUsersByUserIdPhotoResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | DeleteUsersByUserIdPhotoResponseDefaultType0
    | DeleteUsersByUserIdPhotoResponseDefaultType1
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
    | DeleteUsersByUserIdPhotoResponseDefaultType0
    | DeleteUsersByUserIdPhotoResponseDefaultType1
]:
    """Delete a photo image of a specified user.


    Required roles:
     - can_write_users

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteUsersByUserIdPhotoResponseDefaultType0 | DeleteUsersByUserIdPhotoResponseDefaultType1]
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
    | DeleteUsersByUserIdPhotoResponseDefaultType0
    | DeleteUsersByUserIdPhotoResponseDefaultType1
    | None
):
    """Delete a photo image of a specified user.


    Required roles:
     - can_write_users

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteUsersByUserIdPhotoResponseDefaultType0 | DeleteUsersByUserIdPhotoResponseDefaultType1
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
    | DeleteUsersByUserIdPhotoResponseDefaultType0
    | DeleteUsersByUserIdPhotoResponseDefaultType1
]:
    """Delete a photo image of a specified user.


    Required roles:
     - can_write_users

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteUsersByUserIdPhotoResponseDefaultType0 | DeleteUsersByUserIdPhotoResponseDefaultType1]
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
    | DeleteUsersByUserIdPhotoResponseDefaultType0
    | DeleteUsersByUserIdPhotoResponseDefaultType1
    | None
):
    """Delete a photo image of a specified user.


    Required roles:
     - can_write_users

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteUsersByUserIdPhotoResponseDefaultType0 | DeleteUsersByUserIdPhotoResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
        )
    ).parsed
