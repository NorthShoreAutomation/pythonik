from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.acl_schema import ACLSchema
from ...models.get_acl_by_object_type_by_object_key_response_default import (
    GetAclByObjectTypeByObjectKeyResponseDefault,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    object_type: str,
    object_key: str,
    *,
    exclude_deleted: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["exclude_deleted"] = exclude_deleted

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/acl/{object_type}/{object_key}/".format(
            object_type=quote(str(object_type), safe=""),
            object_key=quote(str(object_key), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ACLSchema | Any | GetAclByObjectTypeByObjectKeyResponseDefault:
    if response.status_code == 200:
        response_200 = ACLSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = GetAclByObjectTypeByObjectKeyResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ACLSchema | Any | GetAclByObjectTypeByObjectKeyResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    object_type: str,
    object_key: str,
    *,
    client: AuthenticatedClient | Client,
    exclude_deleted: bool | Unset = UNSET,
) -> Response[ACLSchema | Any | GetAclByObjectTypeByObjectKeyResponseDefault]:
    """List of object permissions


    Required roles:
     - can_read_acls

    Args:
        object_type (str):
        object_key (str):
        exclude_deleted (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ACLSchema | Any | GetAclByObjectTypeByObjectKeyResponseDefault]
    """

    kwargs = _get_kwargs(
        object_type=object_type,
        object_key=object_key,
        exclude_deleted=exclude_deleted,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    object_type: str,
    object_key: str,
    *,
    client: AuthenticatedClient | Client,
    exclude_deleted: bool | Unset = UNSET,
) -> ACLSchema | Any | GetAclByObjectTypeByObjectKeyResponseDefault | None:
    """List of object permissions


    Required roles:
     - can_read_acls

    Args:
        object_type (str):
        object_key (str):
        exclude_deleted (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ACLSchema | Any | GetAclByObjectTypeByObjectKeyResponseDefault
    """

    return sync_detailed(
        object_type=object_type,
        object_key=object_key,
        client=client,
        exclude_deleted=exclude_deleted,
    ).parsed


async def asyncio_detailed(
    object_type: str,
    object_key: str,
    *,
    client: AuthenticatedClient | Client,
    exclude_deleted: bool | Unset = UNSET,
) -> Response[ACLSchema | Any | GetAclByObjectTypeByObjectKeyResponseDefault]:
    """List of object permissions


    Required roles:
     - can_read_acls

    Args:
        object_type (str):
        object_key (str):
        exclude_deleted (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ACLSchema | Any | GetAclByObjectTypeByObjectKeyResponseDefault]
    """

    kwargs = _get_kwargs(
        object_type=object_type,
        object_key=object_key,
        exclude_deleted=exclude_deleted,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    object_type: str,
    object_key: str,
    *,
    client: AuthenticatedClient | Client,
    exclude_deleted: bool | Unset = UNSET,
) -> ACLSchema | Any | GetAclByObjectTypeByObjectKeyResponseDefault | None:
    """List of object permissions


    Required roles:
     - can_read_acls

    Args:
        object_type (str):
        object_key (str):
        exclude_deleted (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ACLSchema | Any | GetAclByObjectTypeByObjectKeyResponseDefault
    """

    return (
        await asyncio_detailed(
            object_type=object_type,
            object_key=object_key,
            client=client,
            exclude_deleted=exclude_deleted,
        )
    ).parsed
