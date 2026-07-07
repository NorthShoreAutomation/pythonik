from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_acl_by_object_type_content_response_default_type_0 import (
    DeleteAclByObjectTypeContentResponseDefaultType0,
)
from ...models.delete_acl_by_object_type_content_response_default_type_1 import (
    DeleteAclByObjectTypeContentResponseDefaultType1,
)
from ...models.delete_bulk_ac_ls_schema import DeleteBulkACLsSchema
from ...types import Response


def _get_kwargs(
    object_type: str,
    *,
    body: DeleteBulkACLsSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "delete",
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
) -> (
    Any
    | DeleteAclByObjectTypeContentResponseDefaultType0
    | DeleteAclByObjectTypeContentResponseDefaultType1
):
    if response.status_code == 200:
        response_200 = cast(Any, None)
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
        DeleteAclByObjectTypeContentResponseDefaultType0
        | DeleteAclByObjectTypeContentResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                DeleteAclByObjectTypeContentResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            DeleteAclByObjectTypeContentResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | DeleteAclByObjectTypeContentResponseDefaultType0
    | DeleteAclByObjectTypeContentResponseDefaultType1
]:
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
    body: DeleteBulkACLsSchema,
) -> Response[
    Any
    | DeleteAclByObjectTypeContentResponseDefaultType0
    | DeleteAclByObjectTypeContentResponseDefaultType1
]:
    """Delete acls for content of multiple objects


    Required roles:
     - can_delete_acls

    Args:
        object_type (str):
        body (DeleteBulkACLsSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteAclByObjectTypeContentResponseDefaultType0 | DeleteAclByObjectTypeContentResponseDefaultType1]
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
    body: DeleteBulkACLsSchema,
) -> (
    Any
    | DeleteAclByObjectTypeContentResponseDefaultType0
    | DeleteAclByObjectTypeContentResponseDefaultType1
    | None
):
    """Delete acls for content of multiple objects


    Required roles:
     - can_delete_acls

    Args:
        object_type (str):
        body (DeleteBulkACLsSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteAclByObjectTypeContentResponseDefaultType0 | DeleteAclByObjectTypeContentResponseDefaultType1
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
    body: DeleteBulkACLsSchema,
) -> Response[
    Any
    | DeleteAclByObjectTypeContentResponseDefaultType0
    | DeleteAclByObjectTypeContentResponseDefaultType1
]:
    """Delete acls for content of multiple objects


    Required roles:
     - can_delete_acls

    Args:
        object_type (str):
        body (DeleteBulkACLsSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteAclByObjectTypeContentResponseDefaultType0 | DeleteAclByObjectTypeContentResponseDefaultType1]
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
    body: DeleteBulkACLsSchema,
) -> (
    Any
    | DeleteAclByObjectTypeContentResponseDefaultType0
    | DeleteAclByObjectTypeContentResponseDefaultType1
    | None
):
    """Delete acls for content of multiple objects


    Required roles:
     - can_delete_acls

    Args:
        object_type (str):
        body (DeleteBulkACLsSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteAclByObjectTypeContentResponseDefaultType0 | DeleteAclByObjectTypeContentResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            object_type=object_type,
            client=client,
            body=body,
        )
    ).parsed
