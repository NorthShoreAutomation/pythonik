from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_storages_by_storage_id_verifications_permissions_response_200 import (
    GetStoragesByStorageIdVerificationsPermissionsResponse200,
)
from ...models.get_storages_by_storage_id_verifications_permissions_response_default_type_0 import (
    GetStoragesByStorageIdVerificationsPermissionsResponseDefaultType0,
)
from ...models.get_storages_by_storage_id_verifications_permissions_response_default_type_1 import (
    GetStoragesByStorageIdVerificationsPermissionsResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    storage_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/storages/{storage_id}/verifications/permissions/".format(
            storage_id=quote(str(storage_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetStoragesByStorageIdVerificationsPermissionsResponse200
    | GetStoragesByStorageIdVerificationsPermissionsResponseDefaultType0
    | GetStoragesByStorageIdVerificationsPermissionsResponseDefaultType1
):
    if response.status_code == 200:
        response_200 = (
            GetStoragesByStorageIdVerificationsPermissionsResponse200.from_dict(
                response.json()
            )
        )

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    def _parse_response_default(
        data: object,
    ) -> (
        GetStoragesByStorageIdVerificationsPermissionsResponseDefaultType0
        | GetStoragesByStorageIdVerificationsPermissionsResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = GetStoragesByStorageIdVerificationsPermissionsResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = GetStoragesByStorageIdVerificationsPermissionsResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetStoragesByStorageIdVerificationsPermissionsResponse200
    | GetStoragesByStorageIdVerificationsPermissionsResponseDefaultType0
    | GetStoragesByStorageIdVerificationsPermissionsResponseDefaultType1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetStoragesByStorageIdVerificationsPermissionsResponse200
    | GetStoragesByStorageIdVerificationsPermissionsResponseDefaultType0
    | GetStoragesByStorageIdVerificationsPermissionsResponseDefaultType1
]:
    """Verify storage permissions


    Required roles:
     - can_read_storages

    Args:
        storage_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetStoragesByStorageIdVerificationsPermissionsResponse200 | GetStoragesByStorageIdVerificationsPermissionsResponseDefaultType0 | GetStoragesByStorageIdVerificationsPermissionsResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        storage_id=storage_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetStoragesByStorageIdVerificationsPermissionsResponse200
    | GetStoragesByStorageIdVerificationsPermissionsResponseDefaultType0
    | GetStoragesByStorageIdVerificationsPermissionsResponseDefaultType1
    | None
):
    """Verify storage permissions


    Required roles:
     - can_read_storages

    Args:
        storage_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetStoragesByStorageIdVerificationsPermissionsResponse200 | GetStoragesByStorageIdVerificationsPermissionsResponseDefaultType0 | GetStoragesByStorageIdVerificationsPermissionsResponseDefaultType1
    """

    return sync_detailed(
        storage_id=storage_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetStoragesByStorageIdVerificationsPermissionsResponse200
    | GetStoragesByStorageIdVerificationsPermissionsResponseDefaultType0
    | GetStoragesByStorageIdVerificationsPermissionsResponseDefaultType1
]:
    """Verify storage permissions


    Required roles:
     - can_read_storages

    Args:
        storage_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetStoragesByStorageIdVerificationsPermissionsResponse200 | GetStoragesByStorageIdVerificationsPermissionsResponseDefaultType0 | GetStoragesByStorageIdVerificationsPermissionsResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        storage_id=storage_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetStoragesByStorageIdVerificationsPermissionsResponse200
    | GetStoragesByStorageIdVerificationsPermissionsResponseDefaultType0
    | GetStoragesByStorageIdVerificationsPermissionsResponseDefaultType1
    | None
):
    """Verify storage permissions


    Required roles:
     - can_read_storages

    Args:
        storage_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetStoragesByStorageIdVerificationsPermissionsResponse200 | GetStoragesByStorageIdVerificationsPermissionsResponseDefaultType0 | GetStoragesByStorageIdVerificationsPermissionsResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            storage_id=storage_id,
            client=client,
        )
    ).parsed
