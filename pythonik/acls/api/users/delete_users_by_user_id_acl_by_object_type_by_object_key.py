from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_users_by_user_id_acl_by_object_type_by_object_key_response_default import (
    DeleteUsersByUserIdAclByObjectTypeByObjectKeyResponseDefault,
)
from ...types import Response


def _get_kwargs(
    user_id: str,
    object_type: str,
    object_key: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/users/{user_id}/acl/{object_type}/{object_key}/".format(
            user_id=quote(str(user_id), safe=""),
            object_type=quote(str(object_type), safe=""),
            object_key=quote(str(object_key), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DeleteUsersByUserIdAclByObjectTypeByObjectKeyResponseDefault:
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

    response_default = (
        DeleteUsersByUserIdAclByObjectTypeByObjectKeyResponseDefault.from_dict(
            response.json()
        )
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DeleteUsersByUserIdAclByObjectTypeByObjectKeyResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: str,
    object_type: str,
    object_key: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DeleteUsersByUserIdAclByObjectTypeByObjectKeyResponseDefault]:
    """Delete a user acl for an object


    Required roles:
     - can_delete_acls

    Args:
        user_id (str):
        object_type (str):
        object_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteUsersByUserIdAclByObjectTypeByObjectKeyResponseDefault]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        object_type=object_type,
        object_key=object_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: str,
    object_type: str,
    object_key: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | DeleteUsersByUserIdAclByObjectTypeByObjectKeyResponseDefault | None:
    """Delete a user acl for an object


    Required roles:
     - can_delete_acls

    Args:
        user_id (str):
        object_type (str):
        object_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteUsersByUserIdAclByObjectTypeByObjectKeyResponseDefault
    """

    return sync_detailed(
        user_id=user_id,
        object_type=object_type,
        object_key=object_key,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    object_type: str,
    object_key: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DeleteUsersByUserIdAclByObjectTypeByObjectKeyResponseDefault]:
    """Delete a user acl for an object


    Required roles:
     - can_delete_acls

    Args:
        user_id (str):
        object_type (str):
        object_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteUsersByUserIdAclByObjectTypeByObjectKeyResponseDefault]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        object_type=object_type,
        object_key=object_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    object_type: str,
    object_key: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | DeleteUsersByUserIdAclByObjectTypeByObjectKeyResponseDefault | None:
    """Delete a user acl for an object


    Required roles:
     - can_delete_acls

    Args:
        user_id (str):
        object_type (str):
        object_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteUsersByUserIdAclByObjectTypeByObjectKeyResponseDefault
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            object_type=object_type,
            object_key=object_key,
            client=client,
        )
    ).parsed
