from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_groups_by_group_id_reindex_response_default_type_0 import (
    PostGroupsByGroupIdReindexResponseDefaultType0,
)
from ...models.post_groups_by_group_id_reindex_response_default_type_1 import (
    PostGroupsByGroupIdReindexResponseDefaultType1,
)
from ...models.user_schema import UserSchema
from ...types import Response


def _get_kwargs(
    group_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/groups/{group_id}/reindex/".format(
            group_id=quote(str(group_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | PostGroupsByGroupIdReindexResponseDefaultType0
    | PostGroupsByGroupIdReindexResponseDefaultType1
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
        PostGroupsByGroupIdReindexResponseDefaultType0
        | PostGroupsByGroupIdReindexResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                PostGroupsByGroupIdReindexResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PostGroupsByGroupIdReindexResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostGroupsByGroupIdReindexResponseDefaultType0
    | PostGroupsByGroupIdReindexResponseDefaultType1
    | UserSchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | PostGroupsByGroupIdReindexResponseDefaultType0
    | PostGroupsByGroupIdReindexResponseDefaultType1
    | UserSchema
]:
    """Reindex a particular group by id


    Required roles:
     - can_reindex_groups

    Args:
        group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostGroupsByGroupIdReindexResponseDefaultType0 | PostGroupsByGroupIdReindexResponseDefaultType1 | UserSchema]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | PostGroupsByGroupIdReindexResponseDefaultType0
    | PostGroupsByGroupIdReindexResponseDefaultType1
    | UserSchema
    | None
):
    """Reindex a particular group by id


    Required roles:
     - can_reindex_groups

    Args:
        group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostGroupsByGroupIdReindexResponseDefaultType0 | PostGroupsByGroupIdReindexResponseDefaultType1 | UserSchema
    """

    return sync_detailed(
        group_id=group_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    group_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | PostGroupsByGroupIdReindexResponseDefaultType0
    | PostGroupsByGroupIdReindexResponseDefaultType1
    | UserSchema
]:
    """Reindex a particular group by id


    Required roles:
     - can_reindex_groups

    Args:
        group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostGroupsByGroupIdReindexResponseDefaultType0 | PostGroupsByGroupIdReindexResponseDefaultType1 | UserSchema]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | PostGroupsByGroupIdReindexResponseDefaultType0
    | PostGroupsByGroupIdReindexResponseDefaultType1
    | UserSchema
    | None
):
    """Reindex a particular group by id


    Required roles:
     - can_reindex_groups

    Args:
        group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostGroupsByGroupIdReindexResponseDefaultType0 | PostGroupsByGroupIdReindexResponseDefaultType1 | UserSchema
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
        )
    ).parsed
