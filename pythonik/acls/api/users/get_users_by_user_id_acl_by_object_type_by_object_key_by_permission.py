from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_users_by_user_id_acl_by_object_type_by_object_key_by_permission_response_default_type_0 import (
    GetUsersByUserIdAclByObjectTypeByObjectKeyByPermissionResponseDefaultType0,
)
from ...models.get_users_by_user_id_acl_by_object_type_by_object_key_by_permission_response_default_type_1 import (
    GetUsersByUserIdAclByObjectTypeByObjectKeyByPermissionResponseDefaultType1,
)
from ...models.user_acl_schema import UserACLSchema
from ...types import Response


def _get_kwargs(
    user_id: str,
    object_type: str,
    object_key: str,
    permission: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/users/{user_id}/acl/{object_type}/{object_key}/{permission}/".format(
            user_id=quote(str(user_id), safe=""),
            object_type=quote(str(object_type), safe=""),
            object_key=quote(str(object_key), safe=""),
            permission=quote(str(permission), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetUsersByUserIdAclByObjectTypeByObjectKeyByPermissionResponseDefaultType0
    | GetUsersByUserIdAclByObjectTypeByObjectKeyByPermissionResponseDefaultType1
    | UserACLSchema
):
    if response.status_code == 200:
        response_200 = UserACLSchema.from_dict(response.json())

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

    def _parse_response_default(
        data: object,
    ) -> (
        GetUsersByUserIdAclByObjectTypeByObjectKeyByPermissionResponseDefaultType0
        | GetUsersByUserIdAclByObjectTypeByObjectKeyByPermissionResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = GetUsersByUserIdAclByObjectTypeByObjectKeyByPermissionResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = GetUsersByUserIdAclByObjectTypeByObjectKeyByPermissionResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetUsersByUserIdAclByObjectTypeByObjectKeyByPermissionResponseDefaultType0
    | GetUsersByUserIdAclByObjectTypeByObjectKeyByPermissionResponseDefaultType1
    | UserACLSchema
]:
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
    permission: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetUsersByUserIdAclByObjectTypeByObjectKeyByPermissionResponseDefaultType0
    | GetUsersByUserIdAclByObjectTypeByObjectKeyByPermissionResponseDefaultType1
    | UserACLSchema
]:
    """Returns a user acl for an object


    Required roles:
     - can_read_acls

    Args:
        user_id (str):
        object_type (str):
        object_key (str):
        permission (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetUsersByUserIdAclByObjectTypeByObjectKeyByPermissionResponseDefaultType0 | GetUsersByUserIdAclByObjectTypeByObjectKeyByPermissionResponseDefaultType1 | UserACLSchema]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        object_type=object_type,
        object_key=object_key,
        permission=permission,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: str,
    object_type: str,
    object_key: str,
    permission: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetUsersByUserIdAclByObjectTypeByObjectKeyByPermissionResponseDefaultType0
    | GetUsersByUserIdAclByObjectTypeByObjectKeyByPermissionResponseDefaultType1
    | UserACLSchema
    | None
):
    """Returns a user acl for an object


    Required roles:
     - can_read_acls

    Args:
        user_id (str):
        object_type (str):
        object_key (str):
        permission (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetUsersByUserIdAclByObjectTypeByObjectKeyByPermissionResponseDefaultType0 | GetUsersByUserIdAclByObjectTypeByObjectKeyByPermissionResponseDefaultType1 | UserACLSchema
    """

    return sync_detailed(
        user_id=user_id,
        object_type=object_type,
        object_key=object_key,
        permission=permission,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    object_type: str,
    object_key: str,
    permission: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetUsersByUserIdAclByObjectTypeByObjectKeyByPermissionResponseDefaultType0
    | GetUsersByUserIdAclByObjectTypeByObjectKeyByPermissionResponseDefaultType1
    | UserACLSchema
]:
    """Returns a user acl for an object


    Required roles:
     - can_read_acls

    Args:
        user_id (str):
        object_type (str):
        object_key (str):
        permission (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetUsersByUserIdAclByObjectTypeByObjectKeyByPermissionResponseDefaultType0 | GetUsersByUserIdAclByObjectTypeByObjectKeyByPermissionResponseDefaultType1 | UserACLSchema]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        object_type=object_type,
        object_key=object_key,
        permission=permission,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    object_type: str,
    object_key: str,
    permission: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetUsersByUserIdAclByObjectTypeByObjectKeyByPermissionResponseDefaultType0
    | GetUsersByUserIdAclByObjectTypeByObjectKeyByPermissionResponseDefaultType1
    | UserACLSchema
    | None
):
    """Returns a user acl for an object


    Required roles:
     - can_read_acls

    Args:
        user_id (str):
        object_type (str):
        object_key (str):
        permission (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetUsersByUserIdAclByObjectTypeByObjectKeyByPermissionResponseDefaultType0 | GetUsersByUserIdAclByObjectTypeByObjectKeyByPermissionResponseDefaultType1 | UserACLSchema
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            object_type=object_type,
            object_key=object_key,
            permission=permission,
            client=client,
        )
    ).parsed
