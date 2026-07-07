from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_groups_by_group_id_acl_by_object_type_by_object_key_response_default_type_0 import (
    GetGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType0,
)
from ...models.get_groups_by_group_id_acl_by_object_type_by_object_key_response_default_type_1 import (
    GetGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType1,
)
from ...models.group_acl_schema import GroupACLSchema
from ...types import Response


def _get_kwargs(
    group_id: str,
    object_type: str,
    object_key: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/groups/{group_id}/acl/{object_type}/{object_key}/".format(
            group_id=quote(str(group_id), safe=""),
            object_type=quote(str(object_type), safe=""),
            object_key=quote(str(object_key), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType0
    | GetGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType1
    | GroupACLSchema
):
    if response.status_code == 200:
        response_200 = GroupACLSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    def _parse_response_default(
        data: object,
    ) -> (
        GetGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType0
        | GetGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = GetGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            GetGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType1.from_dict(
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
    | GetGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType0
    | GetGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType1
    | GroupACLSchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_id: str,
    object_type: str,
    object_key: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType0
    | GetGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType1
    | GroupACLSchema
]:
    """List of groups permissions for an object


    Required roles:
     - can_read_acls

    Args:
        group_id (str):
        object_type (str):
        object_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType0 | GetGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType1 | GroupACLSchema]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        object_type=object_type,
        object_key=object_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: str,
    object_type: str,
    object_key: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType0
    | GetGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType1
    | GroupACLSchema
    | None
):
    """List of groups permissions for an object


    Required roles:
     - can_read_acls

    Args:
        group_id (str):
        object_type (str):
        object_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType0 | GetGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType1 | GroupACLSchema
    """

    return sync_detailed(
        group_id=group_id,
        object_type=object_type,
        object_key=object_key,
        client=client,
    ).parsed


async def asyncio_detailed(
    group_id: str,
    object_type: str,
    object_key: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType0
    | GetGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType1
    | GroupACLSchema
]:
    """List of groups permissions for an object


    Required roles:
     - can_read_acls

    Args:
        group_id (str):
        object_type (str):
        object_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType0 | GetGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType1 | GroupACLSchema]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        object_type=object_type,
        object_key=object_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: str,
    object_type: str,
    object_key: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType0
    | GetGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType1
    | GroupACLSchema
    | None
):
    """List of groups permissions for an object


    Required roles:
     - can_read_acls

    Args:
        group_id (str):
        object_type (str):
        object_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType0 | GetGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType1 | GroupACLSchema
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            object_type=object_type,
            object_key=object_key,
            client=client,
        )
    ).parsed
