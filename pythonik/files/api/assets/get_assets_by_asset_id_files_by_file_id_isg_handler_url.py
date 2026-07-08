from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_assets_by_asset_id_files_by_file_id_isg_handler_url_response_default import (
    GetAssetsByAssetIdFilesByFileIdIsgHandlerUrlResponseDefault,
)
from ...models.isg_handler_url_schema import ISGHandlerURLSchema
from ...types import Response


def _get_kwargs(
    asset_id: str,
    file_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/assets/{asset_id}/files/{file_id}/isg_handler_url/".format(
            asset_id=quote(str(asset_id), safe=""),
            file_id=quote(str(file_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetAssetsByAssetIdFilesByFileIdIsgHandlerUrlResponseDefault
    | ISGHandlerURLSchema
):
    if response.status_code == 200:
        response_200 = ISGHandlerURLSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = (
        GetAssetsByAssetIdFilesByFileIdIsgHandlerUrlResponseDefault.from_dict(
            response.json()
        )
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetAssetsByAssetIdFilesByFileIdIsgHandlerUrlResponseDefault
    | ISGHandlerURLSchema
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
    | GetAssetsByAssetIdFilesByFileIdIsgHandlerUrlResponseDefault
    | ISGHandlerURLSchema
]:
    """Get asset's file handler URL for ISG


    Required roles:
     - can_read_files

    Args:
        asset_id (str):
        file_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAssetsByAssetIdFilesByFileIdIsgHandlerUrlResponseDefault | ISGHandlerURLSchema]
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
    | GetAssetsByAssetIdFilesByFileIdIsgHandlerUrlResponseDefault
    | ISGHandlerURLSchema
    | None
):
    """Get asset's file handler URL for ISG


    Required roles:
     - can_read_files

    Args:
        asset_id (str):
        file_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAssetsByAssetIdFilesByFileIdIsgHandlerUrlResponseDefault | ISGHandlerURLSchema
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
    | GetAssetsByAssetIdFilesByFileIdIsgHandlerUrlResponseDefault
    | ISGHandlerURLSchema
]:
    """Get asset's file handler URL for ISG


    Required roles:
     - can_read_files

    Args:
        asset_id (str):
        file_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAssetsByAssetIdFilesByFileIdIsgHandlerUrlResponseDefault | ISGHandlerURLSchema]
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
    | GetAssetsByAssetIdFilesByFileIdIsgHandlerUrlResponseDefault
    | ISGHandlerURLSchema
    | None
):
    """Get asset's file handler URL for ISG


    Required roles:
     - can_read_files

    Args:
        asset_id (str):
        file_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAssetsByAssetIdFilesByFileIdIsgHandlerUrlResponseDefault | ISGHandlerURLSchema
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            file_id=file_id,
            client=client,
        )
    ).parsed
