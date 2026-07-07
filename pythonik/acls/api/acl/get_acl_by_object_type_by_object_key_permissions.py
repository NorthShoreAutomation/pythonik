from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.combined_permissions_schema import CombinedPermissionsSchema
from ...models.get_acl_by_object_type_by_object_key_permissions_response_default_type_0 import (
    GetAclByObjectTypeByObjectKeyPermissionsResponseDefaultType0,
)
from ...models.get_acl_by_object_type_by_object_key_permissions_response_default_type_1 import (
    GetAclByObjectTypeByObjectKeyPermissionsResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    object_type: str,
    object_key: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/acl/{object_type}/{object_key}/permissions/".format(
            object_type=quote(str(object_type), safe=""),
            object_key=quote(str(object_key), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | CombinedPermissionsSchema
    | GetAclByObjectTypeByObjectKeyPermissionsResponseDefaultType0
    | GetAclByObjectTypeByObjectKeyPermissionsResponseDefaultType1
):
    if response.status_code == 200:
        response_200 = CombinedPermissionsSchema.from_dict(response.json())

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
        GetAclByObjectTypeByObjectKeyPermissionsResponseDefaultType0
        | GetAclByObjectTypeByObjectKeyPermissionsResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetAclByObjectTypeByObjectKeyPermissionsResponseDefaultType0.from_dict(
                    data
                )
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            GetAclByObjectTypeByObjectKeyPermissionsResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | CombinedPermissionsSchema
    | GetAclByObjectTypeByObjectKeyPermissionsResponseDefaultType0
    | GetAclByObjectTypeByObjectKeyPermissionsResponseDefaultType1
]:
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
) -> Response[
    Any
    | CombinedPermissionsSchema
    | GetAclByObjectTypeByObjectKeyPermissionsResponseDefaultType0
    | GetAclByObjectTypeByObjectKeyPermissionsResponseDefaultType1
]:
    """List of permissions for the user

    Args:
        object_type (str):
        object_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CombinedPermissionsSchema | GetAclByObjectTypeByObjectKeyPermissionsResponseDefaultType0 | GetAclByObjectTypeByObjectKeyPermissionsResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        object_type=object_type,
        object_key=object_key,
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
) -> (
    Any
    | CombinedPermissionsSchema
    | GetAclByObjectTypeByObjectKeyPermissionsResponseDefaultType0
    | GetAclByObjectTypeByObjectKeyPermissionsResponseDefaultType1
    | None
):
    """List of permissions for the user

    Args:
        object_type (str):
        object_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CombinedPermissionsSchema | GetAclByObjectTypeByObjectKeyPermissionsResponseDefaultType0 | GetAclByObjectTypeByObjectKeyPermissionsResponseDefaultType1
    """

    return sync_detailed(
        object_type=object_type,
        object_key=object_key,
        client=client,
    ).parsed


async def asyncio_detailed(
    object_type: str,
    object_key: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | CombinedPermissionsSchema
    | GetAclByObjectTypeByObjectKeyPermissionsResponseDefaultType0
    | GetAclByObjectTypeByObjectKeyPermissionsResponseDefaultType1
]:
    """List of permissions for the user

    Args:
        object_type (str):
        object_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CombinedPermissionsSchema | GetAclByObjectTypeByObjectKeyPermissionsResponseDefaultType0 | GetAclByObjectTypeByObjectKeyPermissionsResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        object_type=object_type,
        object_key=object_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    object_type: str,
    object_key: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | CombinedPermissionsSchema
    | GetAclByObjectTypeByObjectKeyPermissionsResponseDefaultType0
    | GetAclByObjectTypeByObjectKeyPermissionsResponseDefaultType1
    | None
):
    """List of permissions for the user

    Args:
        object_type (str):
        object_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CombinedPermissionsSchema | GetAclByObjectTypeByObjectKeyPermissionsResponseDefaultType0 | GetAclByObjectTypeByObjectKeyPermissionsResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            object_type=object_type,
            object_key=object_key,
            client=client,
        )
    ).parsed
