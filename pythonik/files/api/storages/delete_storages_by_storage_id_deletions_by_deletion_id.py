from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_storages_by_storage_id_deletions_by_deletion_id_response_default_type_0 import (
    DeleteStoragesByStorageIdDeletionsByDeletionIdResponseDefaultType0,
)
from ...models.delete_storages_by_storage_id_deletions_by_deletion_id_response_default_type_1 import (
    DeleteStoragesByStorageIdDeletionsByDeletionIdResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    storage_id: str,
    deletion_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/storages/{storage_id}/deletions/{deletion_id}/".format(
            storage_id=quote(str(storage_id), safe=""),
            deletion_id=quote(str(deletion_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | DeleteStoragesByStorageIdDeletionsByDeletionIdResponseDefaultType0
    | DeleteStoragesByStorageIdDeletionsByDeletionIdResponseDefaultType1
):
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    def _parse_response_default(
        data: object,
    ) -> (
        DeleteStoragesByStorageIdDeletionsByDeletionIdResponseDefaultType0
        | DeleteStoragesByStorageIdDeletionsByDeletionIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = DeleteStoragesByStorageIdDeletionsByDeletionIdResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = DeleteStoragesByStorageIdDeletionsByDeletionIdResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | DeleteStoragesByStorageIdDeletionsByDeletionIdResponseDefaultType0
    | DeleteStoragesByStorageIdDeletionsByDeletionIdResponseDefaultType1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    storage_id: str,
    deletion_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | DeleteStoragesByStorageIdDeletionsByDeletionIdResponseDefaultType0
    | DeleteStoragesByStorageIdDeletionsByDeletionIdResponseDefaultType1
]:
    """Delete file deletion job after handling it


    Required roles:
     - is_storage_worker

    Args:
        storage_id (str):
        deletion_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteStoragesByStorageIdDeletionsByDeletionIdResponseDefaultType0 | DeleteStoragesByStorageIdDeletionsByDeletionIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        storage_id=storage_id,
        deletion_id=deletion_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    storage_id: str,
    deletion_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | DeleteStoragesByStorageIdDeletionsByDeletionIdResponseDefaultType0
    | DeleteStoragesByStorageIdDeletionsByDeletionIdResponseDefaultType1
    | None
):
    """Delete file deletion job after handling it


    Required roles:
     - is_storage_worker

    Args:
        storage_id (str):
        deletion_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteStoragesByStorageIdDeletionsByDeletionIdResponseDefaultType0 | DeleteStoragesByStorageIdDeletionsByDeletionIdResponseDefaultType1
    """

    return sync_detailed(
        storage_id=storage_id,
        deletion_id=deletion_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    storage_id: str,
    deletion_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | DeleteStoragesByStorageIdDeletionsByDeletionIdResponseDefaultType0
    | DeleteStoragesByStorageIdDeletionsByDeletionIdResponseDefaultType1
]:
    """Delete file deletion job after handling it


    Required roles:
     - is_storage_worker

    Args:
        storage_id (str):
        deletion_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteStoragesByStorageIdDeletionsByDeletionIdResponseDefaultType0 | DeleteStoragesByStorageIdDeletionsByDeletionIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        storage_id=storage_id,
        deletion_id=deletion_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    storage_id: str,
    deletion_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | DeleteStoragesByStorageIdDeletionsByDeletionIdResponseDefaultType0
    | DeleteStoragesByStorageIdDeletionsByDeletionIdResponseDefaultType1
    | None
):
    """Delete file deletion job after handling it


    Required roles:
     - is_storage_worker

    Args:
        storage_id (str):
        deletion_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteStoragesByStorageIdDeletionsByDeletionIdResponseDefaultType0 | DeleteStoragesByStorageIdDeletionsByDeletionIdResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            storage_id=storage_id,
            deletion_id=deletion_id,
            client=client,
        )
    ).parsed
