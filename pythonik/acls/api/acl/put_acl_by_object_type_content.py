from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.create_bulk_ac_ls_schema import CreateBulkACLsSchema
from ...models.put_acl_by_object_type_content_response_default import (
    PutAclByObjectTypeContentResponseDefault,
)
from ...types import Response


def _get_kwargs(
    object_type: str,
    *,
    body: CreateBulkACLsSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/acl/{object_type}/content/".format(
            object_type=quote(str(object_type), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PutAclByObjectTypeContentResponseDefault:
    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 501:
        response_501 = cast(Any, None)
        return response_501

    response_default = PutAclByObjectTypeContentResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PutAclByObjectTypeContentResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    object_type: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateBulkACLsSchema,
) -> Response[Any | PutAclByObjectTypeContentResponseDefault]:
    """Create a new acl for content of multiple objects


    Required roles:
     - can_write_acls

    Args:
        object_type (str):
        body (CreateBulkACLsSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutAclByObjectTypeContentResponseDefault]
    """

    kwargs = _get_kwargs(
        object_type=object_type,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    object_type: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateBulkACLsSchema,
) -> Any | PutAclByObjectTypeContentResponseDefault | None:
    """Create a new acl for content of multiple objects


    Required roles:
     - can_write_acls

    Args:
        object_type (str):
        body (CreateBulkACLsSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutAclByObjectTypeContentResponseDefault
    """

    return sync_detailed(
        object_type=object_type,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    object_type: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateBulkACLsSchema,
) -> Response[Any | PutAclByObjectTypeContentResponseDefault]:
    """Create a new acl for content of multiple objects


    Required roles:
     - can_write_acls

    Args:
        object_type (str):
        body (CreateBulkACLsSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutAclByObjectTypeContentResponseDefault]
    """

    kwargs = _get_kwargs(
        object_type=object_type,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    object_type: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateBulkACLsSchema,
) -> Any | PutAclByObjectTypeContentResponseDefault | None:
    """Create a new acl for content of multiple objects


    Required roles:
     - can_write_acls

    Args:
        object_type (str):
        body (CreateBulkACLsSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutAclByObjectTypeContentResponseDefault
    """

    return (
        await asyncio_detailed(
            object_type=object_type,
            client=client,
            body=body,
        )
    ).parsed
