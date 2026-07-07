from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_role_groups_by_group_id_response_default_type_0 import (
    DeleteRoleGroupsByGroupIdResponseDefaultType0,
)
from ...models.delete_role_groups_by_group_id_response_default_type_1 import (
    DeleteRoleGroupsByGroupIdResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    group_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/role_groups/{group_id}/".format(
            group_id=quote(str(group_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | DeleteRoleGroupsByGroupIdResponseDefaultType0
    | DeleteRoleGroupsByGroupIdResponseDefaultType1
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
        DeleteRoleGroupsByGroupIdResponseDefaultType0
        | DeleteRoleGroupsByGroupIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                DeleteRoleGroupsByGroupIdResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            DeleteRoleGroupsByGroupIdResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | DeleteRoleGroupsByGroupIdResponseDefaultType0
    | DeleteRoleGroupsByGroupIdResponseDefaultType1
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
    | DeleteRoleGroupsByGroupIdResponseDefaultType0
    | DeleteRoleGroupsByGroupIdResponseDefaultType1
]:
    """Delete a particular role group by id


    Required roles:
     - can_delete_role_groups

    Args:
        group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteRoleGroupsByGroupIdResponseDefaultType0 | DeleteRoleGroupsByGroupIdResponseDefaultType1]
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
    | DeleteRoleGroupsByGroupIdResponseDefaultType0
    | DeleteRoleGroupsByGroupIdResponseDefaultType1
    | None
):
    """Delete a particular role group by id


    Required roles:
     - can_delete_role_groups

    Args:
        group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteRoleGroupsByGroupIdResponseDefaultType0 | DeleteRoleGroupsByGroupIdResponseDefaultType1
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
    | DeleteRoleGroupsByGroupIdResponseDefaultType0
    | DeleteRoleGroupsByGroupIdResponseDefaultType1
]:
    """Delete a particular role group by id


    Required roles:
     - can_delete_role_groups

    Args:
        group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteRoleGroupsByGroupIdResponseDefaultType0 | DeleteRoleGroupsByGroupIdResponseDefaultType1]
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
    | DeleteRoleGroupsByGroupIdResponseDefaultType0
    | DeleteRoleGroupsByGroupIdResponseDefaultType1
    | None
):
    """Delete a particular role group by id


    Required roles:
     - can_delete_role_groups

    Args:
        group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteRoleGroupsByGroupIdResponseDefaultType0 | DeleteRoleGroupsByGroupIdResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
        )
    ).parsed
