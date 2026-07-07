from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_users_by_user_id_reindex_response_default_type_0 import (
    PostUsersByUserIdReindexResponseDefaultType0,
)
from ...models.post_users_by_user_id_reindex_response_default_type_1 import (
    PostUsersByUserIdReindexResponseDefaultType1,
)
from ...models.user_schema import UserSchema
from ...types import Response


def _get_kwargs(
    user_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/users/{user_id}/reindex/".format(
            user_id=quote(str(user_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | PostUsersByUserIdReindexResponseDefaultType0
    | PostUsersByUserIdReindexResponseDefaultType1
    | UserSchema
):
    if response.status_code == 200:
        response_200 = UserSchema.from_dict(response.json())

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
        PostUsersByUserIdReindexResponseDefaultType0
        | PostUsersByUserIdReindexResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                PostUsersByUserIdReindexResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PostUsersByUserIdReindexResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostUsersByUserIdReindexResponseDefaultType0
    | PostUsersByUserIdReindexResponseDefaultType1
    | UserSchema
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
    | PostUsersByUserIdReindexResponseDefaultType0
    | PostUsersByUserIdReindexResponseDefaultType1
    | UserSchema
]:
    """Reindex a particular user by id


    Required roles:
     - can_reindex_users

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostUsersByUserIdReindexResponseDefaultType0 | PostUsersByUserIdReindexResponseDefaultType1 | UserSchema]
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
    | PostUsersByUserIdReindexResponseDefaultType0
    | PostUsersByUserIdReindexResponseDefaultType1
    | UserSchema
    | None
):
    """Reindex a particular user by id


    Required roles:
     - can_reindex_users

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostUsersByUserIdReindexResponseDefaultType0 | PostUsersByUserIdReindexResponseDefaultType1 | UserSchema
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
    | PostUsersByUserIdReindexResponseDefaultType0
    | PostUsersByUserIdReindexResponseDefaultType1
    | UserSchema
]:
    """Reindex a particular user by id


    Required roles:
     - can_reindex_users

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostUsersByUserIdReindexResponseDefaultType0 | PostUsersByUserIdReindexResponseDefaultType1 | UserSchema]
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
    | PostUsersByUserIdReindexResponseDefaultType0
    | PostUsersByUserIdReindexResponseDefaultType1
    | UserSchema
    | None
):
    """Reindex a particular user by id


    Required roles:
     - can_reindex_users

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostUsersByUserIdReindexResponseDefaultType0 | PostUsersByUserIdReindexResponseDefaultType1 | UserSchema
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
        )
    ).parsed
