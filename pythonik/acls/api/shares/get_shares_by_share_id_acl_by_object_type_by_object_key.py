from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_shares_by_share_id_acl_by_object_type_by_object_key_response_default_type_0 import (
    GetSharesByShareIdAclByObjectTypeByObjectKeyResponseDefaultType0,
)
from ...models.get_shares_by_share_id_acl_by_object_type_by_object_key_response_default_type_1 import (
    GetSharesByShareIdAclByObjectTypeByObjectKeyResponseDefaultType1,
)
from ...models.share_acl_schema import ShareACLSchema
from ...types import Response


def _get_kwargs(
    share_id: str,
    object_type: str,
    object_key: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/shares/{share_id}/acl/{object_type}/{object_key}/".format(
            share_id=quote(str(share_id), safe=""),
            object_type=quote(str(object_type), safe=""),
            object_key=quote(str(object_key), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetSharesByShareIdAclByObjectTypeByObjectKeyResponseDefaultType0
    | GetSharesByShareIdAclByObjectTypeByObjectKeyResponseDefaultType1
    | ShareACLSchema
):
    if response.status_code == 200:
        response_200 = ShareACLSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    def _parse_response_default(
        data: object,
    ) -> (
        GetSharesByShareIdAclByObjectTypeByObjectKeyResponseDefaultType0
        | GetSharesByShareIdAclByObjectTypeByObjectKeyResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = GetSharesByShareIdAclByObjectTypeByObjectKeyResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            GetSharesByShareIdAclByObjectTypeByObjectKeyResponseDefaultType1.from_dict(
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
    | GetSharesByShareIdAclByObjectTypeByObjectKeyResponseDefaultType0
    | GetSharesByShareIdAclByObjectTypeByObjectKeyResponseDefaultType1
    | ShareACLSchema
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
) -> Response[
    Any
    | GetSharesByShareIdAclByObjectTypeByObjectKeyResponseDefaultType0
    | GetSharesByShareIdAclByObjectTypeByObjectKeyResponseDefaultType1
    | ShareACLSchema
]:
    """List of share permissions for an object


    Required roles:
     - can_read_acls

    Args:
        share_id (str):
        object_type (str):
        object_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSharesByShareIdAclByObjectTypeByObjectKeyResponseDefaultType0 | GetSharesByShareIdAclByObjectTypeByObjectKeyResponseDefaultType1 | ShareACLSchema]
    """

    kwargs = _get_kwargs(
        share_id=share_id,
        object_type=object_type,
        object_key=object_key,
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
) -> (
    Any
    | GetSharesByShareIdAclByObjectTypeByObjectKeyResponseDefaultType0
    | GetSharesByShareIdAclByObjectTypeByObjectKeyResponseDefaultType1
    | ShareACLSchema
    | None
):
    """List of share permissions for an object


    Required roles:
     - can_read_acls

    Args:
        share_id (str):
        object_type (str):
        object_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSharesByShareIdAclByObjectTypeByObjectKeyResponseDefaultType0 | GetSharesByShareIdAclByObjectTypeByObjectKeyResponseDefaultType1 | ShareACLSchema
    """

    return sync_detailed(
        share_id=share_id,
        object_type=object_type,
        object_key=object_key,
        client=client,
    ).parsed


async def asyncio_detailed(
    share_id: str,
    object_type: str,
    object_key: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetSharesByShareIdAclByObjectTypeByObjectKeyResponseDefaultType0
    | GetSharesByShareIdAclByObjectTypeByObjectKeyResponseDefaultType1
    | ShareACLSchema
]:
    """List of share permissions for an object


    Required roles:
     - can_read_acls

    Args:
        share_id (str):
        object_type (str):
        object_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSharesByShareIdAclByObjectTypeByObjectKeyResponseDefaultType0 | GetSharesByShareIdAclByObjectTypeByObjectKeyResponseDefaultType1 | ShareACLSchema]
    """

    kwargs = _get_kwargs(
        share_id=share_id,
        object_type=object_type,
        object_key=object_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    share_id: str,
    object_type: str,
    object_key: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetSharesByShareIdAclByObjectTypeByObjectKeyResponseDefaultType0
    | GetSharesByShareIdAclByObjectTypeByObjectKeyResponseDefaultType1
    | ShareACLSchema
    | None
):
    """List of share permissions for an object


    Required roles:
     - can_read_acls

    Args:
        share_id (str):
        object_type (str):
        object_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSharesByShareIdAclByObjectTypeByObjectKeyResponseDefaultType0 | GetSharesByShareIdAclByObjectTypeByObjectKeyResponseDefaultType1 | ShareACLSchema
    """

    return (
        await asyncio_detailed(
            share_id=share_id,
            object_type=object_type,
            object_key=object_key,
            client=client,
        )
    ).parsed
