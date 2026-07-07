from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_assets_by_asset_id_files_by_file_id_response_default_type_0 import (
    DeleteAssetsByAssetIdFilesByFileIdResponseDefaultType0,
)
from ...models.delete_assets_by_asset_id_files_by_file_id_response_default_type_1 import (
    DeleteAssetsByAssetIdFilesByFileIdResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    asset_id: str,
    file_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/assets/{asset_id}/files/{file_id}/".format(
            asset_id=quote(str(asset_id), safe=""),
            file_id=quote(str(file_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | DeleteAssetsByAssetIdFilesByFileIdResponseDefaultType0
    | DeleteAssetsByAssetIdFilesByFileIdResponseDefaultType1
):
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    def _parse_response_default(
        data: object,
    ) -> (
        DeleteAssetsByAssetIdFilesByFileIdResponseDefaultType0
        | DeleteAssetsByAssetIdFilesByFileIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                DeleteAssetsByAssetIdFilesByFileIdResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            DeleteAssetsByAssetIdFilesByFileIdResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | DeleteAssetsByAssetIdFilesByFileIdResponseDefaultType0
    | DeleteAssetsByAssetIdFilesByFileIdResponseDefaultType1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    asset_id: str,
    file_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | DeleteAssetsByAssetIdFilesByFileIdResponseDefaultType0
    | DeleteAssetsByAssetIdFilesByFileIdResponseDefaultType1
]:
    """Delete asset's file entry (Not the actual file, use DELETE file_set for that)


    Required roles:
     - can_delete_files

    Args:
        asset_id (str):
        file_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteAssetsByAssetIdFilesByFileIdResponseDefaultType0 | DeleteAssetsByAssetIdFilesByFileIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        file_id=file_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: str,
    file_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | DeleteAssetsByAssetIdFilesByFileIdResponseDefaultType0
    | DeleteAssetsByAssetIdFilesByFileIdResponseDefaultType1
    | None
):
    """Delete asset's file entry (Not the actual file, use DELETE file_set for that)


    Required roles:
     - can_delete_files

    Args:
        asset_id (str):
        file_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteAssetsByAssetIdFilesByFileIdResponseDefaultType0 | DeleteAssetsByAssetIdFilesByFileIdResponseDefaultType1
    """

    return sync_detailed(
        asset_id=asset_id,
        file_id=file_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    file_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | DeleteAssetsByAssetIdFilesByFileIdResponseDefaultType0
    | DeleteAssetsByAssetIdFilesByFileIdResponseDefaultType1
]:
    """Delete asset's file entry (Not the actual file, use DELETE file_set for that)


    Required roles:
     - can_delete_files

    Args:
        asset_id (str):
        file_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteAssetsByAssetIdFilesByFileIdResponseDefaultType0 | DeleteAssetsByAssetIdFilesByFileIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        file_id=file_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    file_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | DeleteAssetsByAssetIdFilesByFileIdResponseDefaultType0
    | DeleteAssetsByAssetIdFilesByFileIdResponseDefaultType1
    | None
):
    """Delete asset's file entry (Not the actual file, use DELETE file_set for that)


    Required roles:
     - can_delete_files

    Args:
        asset_id (str):
        file_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteAssetsByAssetIdFilesByFileIdResponseDefaultType0 | DeleteAssetsByAssetIdFilesByFileIdResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            file_id=file_id,
            client=client,
        )
    ).parsed
