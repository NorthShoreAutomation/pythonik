from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bulk_acl_schema import BulkACLSchema
from ...models.check_bulk_ac_ls_schema import CheckBulkACLsSchema
from ...models.post_acl_response_default import PostAclResponseDefault
from ...types import Response


def _get_kwargs(
    *,
    body: CheckBulkACLsSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/acl/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | BulkACLSchema | PostAclResponseDefault:
    if response.status_code == 200:
        response_200 = BulkACLSchema.from_dict(response.json())

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

    response_default = PostAclResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | BulkACLSchema | PostAclResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CheckBulkACLsSchema,
) -> Response[Any | BulkACLSchema | PostAclResponseDefault]:
    """Check if objects have required permission


    Required roles:
     - can_read_acls

    Args:
        body (CheckBulkACLsSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BulkACLSchema | PostAclResponseDefault]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CheckBulkACLsSchema,
) -> Any | BulkACLSchema | PostAclResponseDefault | None:
    """Check if objects have required permission


    Required roles:
     - can_read_acls

    Args:
        body (CheckBulkACLsSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BulkACLSchema | PostAclResponseDefault
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CheckBulkACLsSchema,
) -> Response[Any | BulkACLSchema | PostAclResponseDefault]:
    """Check if objects have required permission


    Required roles:
     - can_read_acls

    Args:
        body (CheckBulkACLsSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BulkACLSchema | PostAclResponseDefault]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CheckBulkACLsSchema,
) -> Any | BulkACLSchema | PostAclResponseDefault | None:
    """Check if objects have required permission


    Required roles:
     - can_read_acls

    Args:
        body (CheckBulkACLsSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BulkACLSchema | PostAclResponseDefault
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
