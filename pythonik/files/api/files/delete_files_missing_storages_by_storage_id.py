from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_files_missing_storages_by_storage_id_response_default_type_0 import (
    DeleteFilesMissingStoragesByStorageIdResponseDefaultType0,
)
from ...models.delete_files_missing_storages_by_storage_id_response_default_type_1 import (
    DeleteFilesMissingStoragesByStorageIdResponseDefaultType1,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    storage_id: str,
    *,
    remove_assets: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["remove_assets"] = remove_assets

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/files/missing/storages/{storage_id}/".format(
            storage_id=quote(str(storage_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | DeleteFilesMissingStoragesByStorageIdResponseDefaultType0
    | DeleteFilesMissingStoragesByStorageIdResponseDefaultType1
):
    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    def _parse_response_default(
        data: object,
    ) -> (
        DeleteFilesMissingStoragesByStorageIdResponseDefaultType0
        | DeleteFilesMissingStoragesByStorageIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                DeleteFilesMissingStoragesByStorageIdResponseDefaultType0.from_dict(
                    data
                )
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            DeleteFilesMissingStoragesByStorageIdResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | DeleteFilesMissingStoragesByStorageIdResponseDefaultType0
    | DeleteFilesMissingStoragesByStorageIdResponseDefaultType1
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
    remove_assets: bool | Unset = UNSET,
) -> Response[
    Any
    | DeleteFilesMissingStoragesByStorageIdResponseDefaultType0
    | DeleteFilesMissingStoragesByStorageIdResponseDefaultType1
]:
    """Delete all missing files from storage


    Required roles:
     - can_delete_files

    Args:
        storage_id (str):
        remove_assets (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteFilesMissingStoragesByStorageIdResponseDefaultType0 | DeleteFilesMissingStoragesByStorageIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        storage_id=storage_id,
        remove_assets=remove_assets,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    remove_assets: bool | Unset = UNSET,
) -> (
    Any
    | DeleteFilesMissingStoragesByStorageIdResponseDefaultType0
    | DeleteFilesMissingStoragesByStorageIdResponseDefaultType1
    | None
):
    """Delete all missing files from storage


    Required roles:
     - can_delete_files

    Args:
        storage_id (str):
        remove_assets (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteFilesMissingStoragesByStorageIdResponseDefaultType0 | DeleteFilesMissingStoragesByStorageIdResponseDefaultType1
    """

    return sync_detailed(
        storage_id=storage_id,
        client=client,
        remove_assets=remove_assets,
    ).parsed


async def asyncio_detailed(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    remove_assets: bool | Unset = UNSET,
) -> Response[
    Any
    | DeleteFilesMissingStoragesByStorageIdResponseDefaultType0
    | DeleteFilesMissingStoragesByStorageIdResponseDefaultType1
]:
    """Delete all missing files from storage


    Required roles:
     - can_delete_files

    Args:
        storage_id (str):
        remove_assets (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteFilesMissingStoragesByStorageIdResponseDefaultType0 | DeleteFilesMissingStoragesByStorageIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        storage_id=storage_id,
        remove_assets=remove_assets,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    remove_assets: bool | Unset = UNSET,
) -> (
    Any
    | DeleteFilesMissingStoragesByStorageIdResponseDefaultType0
    | DeleteFilesMissingStoragesByStorageIdResponseDefaultType1
    | None
):
    """Delete all missing files from storage


    Required roles:
     - can_delete_files

    Args:
        storage_id (str):
        remove_assets (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteFilesMissingStoragesByStorageIdResponseDefaultType0 | DeleteFilesMissingStoragesByStorageIdResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            storage_id=storage_id,
            client=client,
            remove_assets=remove_assets,
        )
    ).parsed
