from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.create_ac_ls_result_schema import CreateACLsResultSchema
from ...models.create_share_ac_ls_schema import CreateShareACLsSchema
from ...models.put_shares_by_share_id_acl_by_object_type_response_default_type_0 import (
    PutSharesByShareIdAclByObjectTypeResponseDefaultType0,
)
from ...models.put_shares_by_share_id_acl_by_object_type_response_default_type_1 import (
    PutSharesByShareIdAclByObjectTypeResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    share_id: str,
    object_type: str,
    *,
    body: CreateShareACLsSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/shares/{share_id}/acl/{object_type}/".format(
            share_id=quote(str(share_id), safe=""),
            object_type=quote(str(object_type), safe=""),
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
    | CreateACLsResultSchema
    | PutSharesByShareIdAclByObjectTypeResponseDefaultType0
    | PutSharesByShareIdAclByObjectTypeResponseDefaultType1
):
    if response.status_code == 200:
        response_200 = CreateACLsResultSchema.from_dict(response.json())

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
        PutSharesByShareIdAclByObjectTypeResponseDefaultType0
        | PutSharesByShareIdAclByObjectTypeResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                PutSharesByShareIdAclByObjectTypeResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PutSharesByShareIdAclByObjectTypeResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | CreateACLsResultSchema
    | PutSharesByShareIdAclByObjectTypeResponseDefaultType0
    | PutSharesByShareIdAclByObjectTypeResponseDefaultType1
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
    *,
    client: AuthenticatedClient | Client,
    body: CreateShareACLsSchema,
) -> Response[
    Any
    | CreateACLsResultSchema
    | PutSharesByShareIdAclByObjectTypeResponseDefaultType0
    | PutSharesByShareIdAclByObjectTypeResponseDefaultType1
]:
    """Create a new acl for multiple share objects


    Required roles:
     - can_write_acls

    Args:
        share_id (str):
        object_type (str):
        body (CreateShareACLsSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateACLsResultSchema | PutSharesByShareIdAclByObjectTypeResponseDefaultType0 | PutSharesByShareIdAclByObjectTypeResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        share_id=share_id,
        object_type=object_type,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    share_id: str,
    object_type: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateShareACLsSchema,
) -> (
    Any
    | CreateACLsResultSchema
    | PutSharesByShareIdAclByObjectTypeResponseDefaultType0
    | PutSharesByShareIdAclByObjectTypeResponseDefaultType1
    | None
):
    """Create a new acl for multiple share objects


    Required roles:
     - can_write_acls

    Args:
        share_id (str):
        object_type (str):
        body (CreateShareACLsSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateACLsResultSchema | PutSharesByShareIdAclByObjectTypeResponseDefaultType0 | PutSharesByShareIdAclByObjectTypeResponseDefaultType1
    """

    return sync_detailed(
        share_id=share_id,
        object_type=object_type,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    share_id: str,
    object_type: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateShareACLsSchema,
) -> Response[
    Any
    | CreateACLsResultSchema
    | PutSharesByShareIdAclByObjectTypeResponseDefaultType0
    | PutSharesByShareIdAclByObjectTypeResponseDefaultType1
]:
    """Create a new acl for multiple share objects


    Required roles:
     - can_write_acls

    Args:
        share_id (str):
        object_type (str):
        body (CreateShareACLsSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateACLsResultSchema | PutSharesByShareIdAclByObjectTypeResponseDefaultType0 | PutSharesByShareIdAclByObjectTypeResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        share_id=share_id,
        object_type=object_type,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    share_id: str,
    object_type: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateShareACLsSchema,
) -> (
    Any
    | CreateACLsResultSchema
    | PutSharesByShareIdAclByObjectTypeResponseDefaultType0
    | PutSharesByShareIdAclByObjectTypeResponseDefaultType1
    | None
):
    """Create a new acl for multiple share objects


    Required roles:
     - can_write_acls

    Args:
        share_id (str):
        object_type (str):
        body (CreateShareACLsSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateACLsResultSchema | PutSharesByShareIdAclByObjectTypeResponseDefaultType0 | PutSharesByShareIdAclByObjectTypeResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            share_id=share_id,
            object_type=object_type,
            client=client,
            body=body,
        )
    ).parsed
