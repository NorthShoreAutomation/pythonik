from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_shares_by_share_id_acl_by_object_type_by_object_key_response_default import (
    PostSharesByShareIdAclByObjectTypeByObjectKeyResponseDefault,
)
from ...models.share_acl_schema import ShareACLSchema
from ...types import Response


def _get_kwargs(
    share_id: str,
    object_type: str,
    object_key: str,
    *,
    body: ShareACLSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/shares/{share_id}/acl/{object_type}/{object_key}/".format(
            share_id=quote(str(share_id), safe=""),
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
    Any | PostSharesByShareIdAclByObjectTypeByObjectKeyResponseDefault | ShareACLSchema
):
    if response.status_code == 201:
        response_201 = ShareACLSchema.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = (
        PostSharesByShareIdAclByObjectTypeByObjectKeyResponseDefault.from_dict(
            response.json()
        )
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | PostSharesByShareIdAclByObjectTypeByObjectKeyResponseDefault | ShareACLSchema
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
    *,
    client: AuthenticatedClient | Client,
    body: ShareACLSchema,
) -> Response[
    Any | PostSharesByShareIdAclByObjectTypeByObjectKeyResponseDefault | ShareACLSchema
]:
    """Create a new share acl for an object


    Required roles:
     - can_write_acls

    Args:
        share_id (str):
        object_type (str):
        object_key (str):
        body (ShareACLSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostSharesByShareIdAclByObjectTypeByObjectKeyResponseDefault | ShareACLSchema]
    """

    kwargs = _get_kwargs(
        share_id=share_id,
        object_type=object_type,
        object_key=object_key,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    share_id: str,
    object_type: str,
    object_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: ShareACLSchema,
) -> (
    Any
    | PostSharesByShareIdAclByObjectTypeByObjectKeyResponseDefault
    | ShareACLSchema
    | None
):
    """Create a new share acl for an object


    Required roles:
     - can_write_acls

    Args:
        share_id (str):
        object_type (str):
        object_key (str):
        body (ShareACLSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostSharesByShareIdAclByObjectTypeByObjectKeyResponseDefault | ShareACLSchema
    """

    return sync_detailed(
        share_id=share_id,
        object_type=object_type,
        object_key=object_key,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    share_id: str,
    object_type: str,
    object_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: ShareACLSchema,
) -> Response[
    Any | PostSharesByShareIdAclByObjectTypeByObjectKeyResponseDefault | ShareACLSchema
]:
    """Create a new share acl for an object


    Required roles:
     - can_write_acls

    Args:
        share_id (str):
        object_type (str):
        object_key (str):
        body (ShareACLSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostSharesByShareIdAclByObjectTypeByObjectKeyResponseDefault | ShareACLSchema]
    """

    kwargs = _get_kwargs(
        share_id=share_id,
        object_type=object_type,
        object_key=object_key,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    share_id: str,
    object_type: str,
    object_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: ShareACLSchema,
) -> (
    Any
    | PostSharesByShareIdAclByObjectTypeByObjectKeyResponseDefault
    | ShareACLSchema
    | None
):
    """Create a new share acl for an object


    Required roles:
     - can_write_acls

    Args:
        share_id (str):
        object_type (str):
        object_key (str):
        body (ShareACLSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostSharesByShareIdAclByObjectTypeByObjectKeyResponseDefault | ShareACLSchema
    """

    return (
        await asyncio_detailed(
            share_id=share_id,
            object_type=object_type,
            object_key=object_key,
            client=client,
            body=body,
        )
    ).parsed
