from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_groups_by_group_id_acl_by_object_type_by_object_key_response_default_type_0 import (
    DeleteGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType0,
)
from ...models.delete_groups_by_group_id_acl_by_object_type_by_object_key_response_default_type_1 import (
    DeleteGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    group_id: str,
    object_type: str,
    object_key: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
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
    | DeleteGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType0
    | DeleteGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType1
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
        DeleteGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType0
        | DeleteGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = DeleteGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = DeleteGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | DeleteGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType0
    | DeleteGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType1
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
    | DeleteGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType0
    | DeleteGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType1
]:
    """Delete a particular acl by id for an object


    Required roles:
     - can_delete_acls

    Args:
        group_id (str):
        object_type (str):
        object_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType0 | DeleteGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType1]
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
    | DeleteGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType0
    | DeleteGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType1
    | None
):
    """Delete a particular acl by id for an object


    Required roles:
     - can_delete_acls

    Args:
        group_id (str):
        object_type (str):
        object_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType0 | DeleteGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType1
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
    | DeleteGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType0
    | DeleteGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType1
]:
    """Delete a particular acl by id for an object


    Required roles:
     - can_delete_acls

    Args:
        group_id (str):
        object_type (str):
        object_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType0 | DeleteGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType1]
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
    | DeleteGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType0
    | DeleteGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType1
    | None
):
    """Delete a particular acl by id for an object


    Required roles:
     - can_delete_acls

    Args:
        group_id (str):
        object_type (str):
        object_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType0 | DeleteGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            object_type=object_type,
            object_key=object_key,
            client=client,
        )
    ).parsed
