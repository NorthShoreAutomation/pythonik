from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_assets_by_asset_id_file_sets_by_file_set_id_purge_response_default_type_0 import (
    DeleteAssetsByAssetIdFileSetsByFileSetIdPurgeResponseDefaultType0,
)
from ...models.delete_assets_by_asset_id_file_sets_by_file_set_id_purge_response_default_type_1 import (
    DeleteAssetsByAssetIdFileSetsByFileSetIdPurgeResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    asset_id: str,
    file_set_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/assets/{asset_id}/file_sets/{file_set_id}/purge/".format(
            asset_id=quote(str(asset_id), safe=""),
            file_set_id=quote(str(file_set_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | DeleteAssetsByAssetIdFileSetsByFileSetIdPurgeResponseDefaultType0
    | DeleteAssetsByAssetIdFileSetsByFileSetIdPurgeResponseDefaultType1
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
        DeleteAssetsByAssetIdFileSetsByFileSetIdPurgeResponseDefaultType0
        | DeleteAssetsByAssetIdFileSetsByFileSetIdPurgeResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = DeleteAssetsByAssetIdFileSetsByFileSetIdPurgeResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            DeleteAssetsByAssetIdFileSetsByFileSetIdPurgeResponseDefaultType1.from_dict(
                data
            )
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | DeleteAssetsByAssetIdFileSetsByFileSetIdPurgeResponseDefaultType0
    | DeleteAssetsByAssetIdFileSetsByFileSetIdPurgeResponseDefaultType1
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
) -> Response[
    Any
    | DeleteAssetsByAssetIdFileSetsByFileSetIdPurgeResponseDefaultType0
    | DeleteAssetsByAssetIdFileSetsByFileSetIdPurgeResponseDefaultType1
]:
    """Purge deleted asset's file set, file entries, and actual files.


    Required roles:
     - can_delete_files

    Args:
        asset_id (str):
        file_set_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteAssetsByAssetIdFileSetsByFileSetIdPurgeResponseDefaultType0 | DeleteAssetsByAssetIdFileSetsByFileSetIdPurgeResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        file_set_id=file_set_id,
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
) -> (
    Any
    | DeleteAssetsByAssetIdFileSetsByFileSetIdPurgeResponseDefaultType0
    | DeleteAssetsByAssetIdFileSetsByFileSetIdPurgeResponseDefaultType1
    | None
):
    """Purge deleted asset's file set, file entries, and actual files.


    Required roles:
     - can_delete_files

    Args:
        asset_id (str):
        file_set_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteAssetsByAssetIdFileSetsByFileSetIdPurgeResponseDefaultType0 | DeleteAssetsByAssetIdFileSetsByFileSetIdPurgeResponseDefaultType1
    """

    return sync_detailed(
        asset_id=asset_id,
        file_set_id=file_set_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    file_set_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | DeleteAssetsByAssetIdFileSetsByFileSetIdPurgeResponseDefaultType0
    | DeleteAssetsByAssetIdFileSetsByFileSetIdPurgeResponseDefaultType1
]:
    """Purge deleted asset's file set, file entries, and actual files.


    Required roles:
     - can_delete_files

    Args:
        asset_id (str):
        file_set_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteAssetsByAssetIdFileSetsByFileSetIdPurgeResponseDefaultType0 | DeleteAssetsByAssetIdFileSetsByFileSetIdPurgeResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        file_set_id=file_set_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    file_set_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | DeleteAssetsByAssetIdFileSetsByFileSetIdPurgeResponseDefaultType0
    | DeleteAssetsByAssetIdFileSetsByFileSetIdPurgeResponseDefaultType1
    | None
):
    """Purge deleted asset's file set, file entries, and actual files.


    Required roles:
     - can_delete_files

    Args:
        asset_id (str):
        file_set_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteAssetsByAssetIdFileSetsByFileSetIdPurgeResponseDefaultType0 | DeleteAssetsByAssetIdFileSetsByFileSetIdPurgeResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            file_set_id=file_set_id,
            client=client,
        )
    ).parsed
