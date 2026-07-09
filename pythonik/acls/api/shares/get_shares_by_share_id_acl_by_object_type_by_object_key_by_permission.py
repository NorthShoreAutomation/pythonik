from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_shares_by_share_id_acl_by_object_type_by_object_key_by_permission_response_default import (
    GetSharesByShareIdAclByObjectTypeByObjectKeyByPermissionResponseDefault,
)
from ...types import Response


def _get_kwargs(
    share_id: str,
    object_type: str,
    object_key: str,
    permission: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/shares/{share_id}/acl/{object_type}/{object_key}/{permission}/".format(
            share_id=quote(str(share_id), safe=""),
            object_type=quote(str(object_type), safe=""),
            object_key=quote(str(object_key), safe=""),
            permission=quote(str(permission), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetSharesByShareIdAclByObjectTypeByObjectKeyByPermissionResponseDefault:
    if response.status_code == 200:
        response_200 = cast(Any, None)
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

    response_default = GetSharesByShareIdAclByObjectTypeByObjectKeyByPermissionResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | GetSharesByShareIdAclByObjectTypeByObjectKeyByPermissionResponseDefault
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    share_id: str,
    object_type: str,
    object_key: str,
    permission: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any | GetSharesByShareIdAclByObjectTypeByObjectKeyByPermissionResponseDefault
]:
    """Returns a share acl for an object


    Required roles:
     - can_read_acls

    Args:
        share_id (str):
        object_type (str):
        object_key (str):
        permission (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSharesByShareIdAclByObjectTypeByObjectKeyByPermissionResponseDefault]
    """

    kwargs = _get_kwargs(
        share_id=share_id,
        object_type=object_type,
        object_key=object_key,
        permission=permission,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    share_id: str,
    object_type: str,
    object_key: str,
    permission: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any | GetSharesByShareIdAclByObjectTypeByObjectKeyByPermissionResponseDefault | None
):
    """Returns a share acl for an object


    Required roles:
     - can_read_acls

    Args:
        share_id (str):
        object_type (str):
        object_key (str):
        permission (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSharesByShareIdAclByObjectTypeByObjectKeyByPermissionResponseDefault
    """

    return sync_detailed(
        share_id=share_id,
        object_type=object_type,
        object_key=object_key,
        permission=permission,
        client=client,
    ).parsed


async def asyncio_detailed(
    share_id: str,
    object_type: str,
    object_key: str,
    permission: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any | GetSharesByShareIdAclByObjectTypeByObjectKeyByPermissionResponseDefault
]:
    """Returns a share acl for an object


    Required roles:
     - can_read_acls

    Args:
        share_id (str):
        object_type (str):
        object_key (str):
        permission (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSharesByShareIdAclByObjectTypeByObjectKeyByPermissionResponseDefault]
    """

    kwargs = _get_kwargs(
        share_id=share_id,
        object_type=object_type,
        object_key=object_key,
        permission=permission,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    share_id: str,
    object_type: str,
    object_key: str,
    permission: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any | GetSharesByShareIdAclByObjectTypeByObjectKeyByPermissionResponseDefault | None
):
    """Returns a share acl for an object


    Required roles:
     - can_read_acls

    Args:
        share_id (str):
        object_type (str):
        object_key (str):
        permission (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSharesByShareIdAclByObjectTypeByObjectKeyByPermissionResponseDefault
    """

    return (
        await asyncio_detailed(
            share_id=share_id,
            object_type=object_type,
            object_key=object_key,
            permission=permission,
            client=client,
        )
    ).parsed
