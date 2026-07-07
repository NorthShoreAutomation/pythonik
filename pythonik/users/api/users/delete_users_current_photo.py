from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_users_current_photo_response_default_type_0 import (
    DeleteUsersCurrentPhotoResponseDefaultType0,
)
from ...models.delete_users_current_photo_response_default_type_1 import (
    DeleteUsersCurrentPhotoResponseDefaultType1,
)
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/users/current/photo/",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | DeleteUsersCurrentPhotoResponseDefaultType0
    | DeleteUsersCurrentPhotoResponseDefaultType1
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
        DeleteUsersCurrentPhotoResponseDefaultType0
        | DeleteUsersCurrentPhotoResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                DeleteUsersCurrentPhotoResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = DeleteUsersCurrentPhotoResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | DeleteUsersCurrentPhotoResponseDefaultType0
    | DeleteUsersCurrentPhotoResponseDefaultType1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | DeleteUsersCurrentPhotoResponseDefaultType0
    | DeleteUsersCurrentPhotoResponseDefaultType1
]:
    """Delete current user photo image.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteUsersCurrentPhotoResponseDefaultType0 | DeleteUsersCurrentPhotoResponseDefaultType1]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | DeleteUsersCurrentPhotoResponseDefaultType0
    | DeleteUsersCurrentPhotoResponseDefaultType1
    | None
):
    """Delete current user photo image.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteUsersCurrentPhotoResponseDefaultType0 | DeleteUsersCurrentPhotoResponseDefaultType1
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | DeleteUsersCurrentPhotoResponseDefaultType0
    | DeleteUsersCurrentPhotoResponseDefaultType1
]:
    """Delete current user photo image.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteUsersCurrentPhotoResponseDefaultType0 | DeleteUsersCurrentPhotoResponseDefaultType1]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | DeleteUsersCurrentPhotoResponseDefaultType0
    | DeleteUsersCurrentPhotoResponseDefaultType1
    | None
):
    """Delete current user photo image.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteUsersCurrentPhotoResponseDefaultType0 | DeleteUsersCurrentPhotoResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
