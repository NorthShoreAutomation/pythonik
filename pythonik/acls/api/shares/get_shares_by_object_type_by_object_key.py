from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_shares_by_object_type_by_object_key_response_default_type_0 import (
    GetSharesByObjectTypeByObjectKeyResponseDefaultType0,
)
from ...models.get_shares_by_object_type_by_object_key_response_default_type_1 import (
    GetSharesByObjectTypeByObjectKeyResponseDefaultType1,
)
from ...models.shares_acl_schema import SharesACLSchema
from ...types import Response


def _get_kwargs(
    object_type: str,
    object_key: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/shares/{object_type}/{object_key}/".format(
            object_type=quote(str(object_type), safe=""),
            object_key=quote(str(object_key), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetSharesByObjectTypeByObjectKeyResponseDefaultType0
    | GetSharesByObjectTypeByObjectKeyResponseDefaultType1
    | SharesACLSchema
):
    if response.status_code == 200:
        response_200 = SharesACLSchema.from_dict(response.json())

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
        GetSharesByObjectTypeByObjectKeyResponseDefaultType0
        | GetSharesByObjectTypeByObjectKeyResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetSharesByObjectTypeByObjectKeyResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            GetSharesByObjectTypeByObjectKeyResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetSharesByObjectTypeByObjectKeyResponseDefaultType0
    | GetSharesByObjectTypeByObjectKeyResponseDefaultType1
    | SharesACLSchema
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
    | GetSharesByObjectTypeByObjectKeyResponseDefaultType0
    | GetSharesByObjectTypeByObjectKeyResponseDefaultType1
    | SharesACLSchema
]:
    """List of share acls


    Required roles:
     - can_read_acls

    Args:
        object_type (str):
        object_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSharesByObjectTypeByObjectKeyResponseDefaultType0 | GetSharesByObjectTypeByObjectKeyResponseDefaultType1 | SharesACLSchema]
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
    | GetSharesByObjectTypeByObjectKeyResponseDefaultType0
    | GetSharesByObjectTypeByObjectKeyResponseDefaultType1
    | SharesACLSchema
    | None
):
    """List of share acls


    Required roles:
     - can_read_acls

    Args:
        object_type (str):
        object_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSharesByObjectTypeByObjectKeyResponseDefaultType0 | GetSharesByObjectTypeByObjectKeyResponseDefaultType1 | SharesACLSchema
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
    | GetSharesByObjectTypeByObjectKeyResponseDefaultType0
    | GetSharesByObjectTypeByObjectKeyResponseDefaultType1
    | SharesACLSchema
]:
    """List of share acls


    Required roles:
     - can_read_acls

    Args:
        object_type (str):
        object_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSharesByObjectTypeByObjectKeyResponseDefaultType0 | GetSharesByObjectTypeByObjectKeyResponseDefaultType1 | SharesACLSchema]
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
    | GetSharesByObjectTypeByObjectKeyResponseDefaultType0
    | GetSharesByObjectTypeByObjectKeyResponseDefaultType1
    | SharesACLSchema
    | None
):
    """List of share acls


    Required roles:
     - can_read_acls

    Args:
        object_type (str):
        object_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSharesByObjectTypeByObjectKeyResponseDefaultType0 | GetSharesByObjectTypeByObjectKeyResponseDefaultType1 | SharesACLSchema
    """

    return (
        await asyncio_detailed(
            object_type=object_type,
            object_key=object_key,
            client=client,
        )
    ).parsed
