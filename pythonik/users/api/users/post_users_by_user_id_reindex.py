from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_users_by_user_id_reindex_body import PostUsersByUserIdReindexBody
from ...models.post_users_by_user_id_reindex_response_201 import (
    PostUsersByUserIdReindexResponse201,
)
from ...models.post_users_by_user_id_reindex_response_default import (
    PostUsersByUserIdReindexResponseDefault,
)
from ...types import Response


def _get_kwargs(
    user_id: str,
    *,
    body: PostUsersByUserIdReindexBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/users/{user_id}/reindex/".format(
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
    Any | PostUsersByUserIdReindexResponse201 | PostUsersByUserIdReindexResponseDefault
):
    if response.status_code == 201:
        response_201 = PostUsersByUserIdReindexResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = PostUsersByUserIdReindexResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | PostUsersByUserIdReindexResponse201 | PostUsersByUserIdReindexResponseDefault
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
    body: PostUsersByUserIdReindexBody,
) -> Response[
    Any | PostUsersByUserIdReindexResponse201 | PostUsersByUserIdReindexResponseDefault
]:
    """Reindex a particular user by id


    Required roles:
     - can_reindex_users

    Args:
        user_id (str):
        body (PostUsersByUserIdReindexBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostUsersByUserIdReindexResponse201 | PostUsersByUserIdReindexResponseDefault]
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
    body: PostUsersByUserIdReindexBody,
) -> (
    Any
    | PostUsersByUserIdReindexResponse201
    | PostUsersByUserIdReindexResponseDefault
    | None
):
    """Reindex a particular user by id


    Required roles:
     - can_reindex_users

    Args:
        user_id (str):
        body (PostUsersByUserIdReindexBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostUsersByUserIdReindexResponse201 | PostUsersByUserIdReindexResponseDefault
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
    body: PostUsersByUserIdReindexBody,
) -> Response[
    Any | PostUsersByUserIdReindexResponse201 | PostUsersByUserIdReindexResponseDefault
]:
    """Reindex a particular user by id


    Required roles:
     - can_reindex_users

    Args:
        user_id (str):
        body (PostUsersByUserIdReindexBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostUsersByUserIdReindexResponse201 | PostUsersByUserIdReindexResponseDefault]
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
    body: PostUsersByUserIdReindexBody,
) -> (
    Any
    | PostUsersByUserIdReindexResponse201
    | PostUsersByUserIdReindexResponseDefault
    | None
):
    """Reindex a particular user by id


    Required roles:
     - can_reindex_users

    Args:
        user_id (str):
        body (PostUsersByUserIdReindexBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostUsersByUserIdReindexResponse201 | PostUsersByUserIdReindexResponseDefault
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            body=body,
        )
    ).parsed
