from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_assets_by_asset_id_temporary_file_sets_by_file_set_id_response_default_type_0 import (
    DeleteAssetsByAssetIdTemporaryFileSetsByFileSetIdResponseDefaultType0,
)
from ...models.delete_assets_by_asset_id_temporary_file_sets_by_file_set_id_response_default_type_1 import (
    DeleteAssetsByAssetIdTemporaryFileSetsByFileSetIdResponseDefaultType1,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    asset_id: str,
    file_set_id: str,
    *,
    delete_cloud_objects: bool | Unset = True,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["delete_cloud_objects"] = delete_cloud_objects

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/assets/{asset_id}/temporary_file_sets/{file_set_id}/".format(
            asset_id=quote(str(asset_id), safe=""),
            file_set_id=quote(str(file_set_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | DeleteAssetsByAssetIdTemporaryFileSetsByFileSetIdResponseDefaultType0
    | DeleteAssetsByAssetIdTemporaryFileSetsByFileSetIdResponseDefaultType1
):
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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
        DeleteAssetsByAssetIdTemporaryFileSetsByFileSetIdResponseDefaultType0
        | DeleteAssetsByAssetIdTemporaryFileSetsByFileSetIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = DeleteAssetsByAssetIdTemporaryFileSetsByFileSetIdResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = DeleteAssetsByAssetIdTemporaryFileSetsByFileSetIdResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | DeleteAssetsByAssetIdTemporaryFileSetsByFileSetIdResponseDefaultType0
    | DeleteAssetsByAssetIdTemporaryFileSetsByFileSetIdResponseDefaultType1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    asset_id: str,
    file_set_id: str,
    *,
    client: AuthenticatedClient | Client,
    delete_cloud_objects: bool | Unset = True,
) -> Response[
    Any
    | DeleteAssetsByAssetIdTemporaryFileSetsByFileSetIdResponseDefaultType0
    | DeleteAssetsByAssetIdTemporaryFileSetsByFileSetIdResponseDefaultType1
]:
    """Delete temporary file set with files


    Required roles:
     - can_delete_files

    Args:
        asset_id (str):
        file_set_id (str):
        delete_cloud_objects (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteAssetsByAssetIdTemporaryFileSetsByFileSetIdResponseDefaultType0 | DeleteAssetsByAssetIdTemporaryFileSetsByFileSetIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        file_set_id=file_set_id,
        delete_cloud_objects=delete_cloud_objects,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: str,
    file_set_id: str,
    *,
    client: AuthenticatedClient | Client,
    delete_cloud_objects: bool | Unset = True,
) -> (
    Any
    | DeleteAssetsByAssetIdTemporaryFileSetsByFileSetIdResponseDefaultType0
    | DeleteAssetsByAssetIdTemporaryFileSetsByFileSetIdResponseDefaultType1
    | None
):
    """Delete temporary file set with files


    Required roles:
     - can_delete_files

    Args:
        asset_id (str):
        file_set_id (str):
        delete_cloud_objects (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteAssetsByAssetIdTemporaryFileSetsByFileSetIdResponseDefaultType0 | DeleteAssetsByAssetIdTemporaryFileSetsByFileSetIdResponseDefaultType1
    """

    return sync_detailed(
        asset_id=asset_id,
        file_set_id=file_set_id,
        client=client,
        delete_cloud_objects=delete_cloud_objects,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    file_set_id: str,
    *,
    client: AuthenticatedClient | Client,
    delete_cloud_objects: bool | Unset = True,
) -> Response[
    Any
    | DeleteAssetsByAssetIdTemporaryFileSetsByFileSetIdResponseDefaultType0
    | DeleteAssetsByAssetIdTemporaryFileSetsByFileSetIdResponseDefaultType1
]:
    """Delete temporary file set with files


    Required roles:
     - can_delete_files

    Args:
        asset_id (str):
        file_set_id (str):
        delete_cloud_objects (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteAssetsByAssetIdTemporaryFileSetsByFileSetIdResponseDefaultType0 | DeleteAssetsByAssetIdTemporaryFileSetsByFileSetIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        file_set_id=file_set_id,
        delete_cloud_objects=delete_cloud_objects,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    file_set_id: str,
    *,
    client: AuthenticatedClient | Client,
    delete_cloud_objects: bool | Unset = True,
) -> (
    Any
    | DeleteAssetsByAssetIdTemporaryFileSetsByFileSetIdResponseDefaultType0
    | DeleteAssetsByAssetIdTemporaryFileSetsByFileSetIdResponseDefaultType1
    | None
):
    """Delete temporary file set with files


    Required roles:
     - can_delete_files

    Args:
        asset_id (str):
        file_set_id (str):
        delete_cloud_objects (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteAssetsByAssetIdTemporaryFileSetsByFileSetIdResponseDefaultType0 | DeleteAssetsByAssetIdTemporaryFileSetsByFileSetIdResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            file_set_id=file_set_id,
            client=client,
            delete_cloud_objects=delete_cloud_objects,
        )
    ).parsed
