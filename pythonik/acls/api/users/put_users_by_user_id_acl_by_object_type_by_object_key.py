from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.put_users_by_user_id_acl_by_object_type_by_object_key_response_default_type_0 import (
    PutUsersByUserIdAclByObjectTypeByObjectKeyResponseDefaultType0,
)
from ...models.put_users_by_user_id_acl_by_object_type_by_object_key_response_default_type_1 import (
    PutUsersByUserIdAclByObjectTypeByObjectKeyResponseDefaultType1,
)
from ...models.user_acl_schema import UserACLSchema
from ...types import Response


def _get_kwargs(
    user_id: str,
    object_type: str,
    object_key: str,
    *,
    body: UserACLSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/users/{user_id}/acl/{object_type}/{object_key}/".format(
            user_id=quote(str(user_id), safe=""),
            object_type=quote(str(object_type), safe=""),
            object_key=quote(str(object_key), safe=""),
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
    | PutUsersByUserIdAclByObjectTypeByObjectKeyResponseDefaultType0
    | PutUsersByUserIdAclByObjectTypeByObjectKeyResponseDefaultType1
    | UserACLSchema
):
    if response.status_code == 200:
        response_200 = UserACLSchema.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = UserACLSchema.from_dict(response.json())

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

    def _parse_response_default(
        data: object,
    ) -> (
        PutUsersByUserIdAclByObjectTypeByObjectKeyResponseDefaultType0
        | PutUsersByUserIdAclByObjectTypeByObjectKeyResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = PutUsersByUserIdAclByObjectTypeByObjectKeyResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PutUsersByUserIdAclByObjectTypeByObjectKeyResponseDefaultType1.from_dict(
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
    | PutUsersByUserIdAclByObjectTypeByObjectKeyResponseDefaultType0
    | PutUsersByUserIdAclByObjectTypeByObjectKeyResponseDefaultType1
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
    *,
    client: AuthenticatedClient | Client,
    body: UserACLSchema,
) -> Response[
    Any
    | PutUsersByUserIdAclByObjectTypeByObjectKeyResponseDefaultType0
    | PutUsersByUserIdAclByObjectTypeByObjectKeyResponseDefaultType1
    | UserACLSchema
]:
    """Update or create user acl for an object


    Required roles:
     - can_write_acls

    Args:
        user_id (str):
        object_type (str):
        object_key (str):
        body (UserACLSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutUsersByUserIdAclByObjectTypeByObjectKeyResponseDefaultType0 | PutUsersByUserIdAclByObjectTypeByObjectKeyResponseDefaultType1 | UserACLSchema]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        object_type=object_type,
        object_key=object_key,
        body=body,
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
    body: UserACLSchema,
) -> (
    Any
    | PutUsersByUserIdAclByObjectTypeByObjectKeyResponseDefaultType0
    | PutUsersByUserIdAclByObjectTypeByObjectKeyResponseDefaultType1
    | UserACLSchema
    | None
):
    """Update or create user acl for an object


    Required roles:
     - can_write_acls

    Args:
        user_id (str):
        object_type (str):
        object_key (str):
        body (UserACLSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutUsersByUserIdAclByObjectTypeByObjectKeyResponseDefaultType0 | PutUsersByUserIdAclByObjectTypeByObjectKeyResponseDefaultType1 | UserACLSchema
    """

    return sync_detailed(
        user_id=user_id,
        object_type=object_type,
        object_key=object_key,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    object_type: str,
    object_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: UserACLSchema,
) -> Response[
    Any
    | PutUsersByUserIdAclByObjectTypeByObjectKeyResponseDefaultType0
    | PutUsersByUserIdAclByObjectTypeByObjectKeyResponseDefaultType1
    | UserACLSchema
]:
    """Update or create user acl for an object


    Required roles:
     - can_write_acls

    Args:
        user_id (str):
        object_type (str):
        object_key (str):
        body (UserACLSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutUsersByUserIdAclByObjectTypeByObjectKeyResponseDefaultType0 | PutUsersByUserIdAclByObjectTypeByObjectKeyResponseDefaultType1 | UserACLSchema]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        object_type=object_type,
        object_key=object_key,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    object_type: str,
    object_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: UserACLSchema,
) -> (
    Any
    | PutUsersByUserIdAclByObjectTypeByObjectKeyResponseDefaultType0
    | PutUsersByUserIdAclByObjectTypeByObjectKeyResponseDefaultType1
    | UserACLSchema
    | None
):
    """Update or create user acl for an object


    Required roles:
     - can_write_acls

    Args:
        user_id (str):
        object_type (str):
        object_key (str):
        body (UserACLSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutUsersByUserIdAclByObjectTypeByObjectKeyResponseDefaultType0 | PutUsersByUserIdAclByObjectTypeByObjectKeyResponseDefaultType1 | UserACLSchema
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            object_type=object_type,
            object_key=object_key,
            client=client,
            body=body,
        )
    ).parsed
