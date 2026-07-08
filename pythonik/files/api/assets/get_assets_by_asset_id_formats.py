from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.formats_schema import FormatsSchema
from ...models.get_assets_by_asset_id_formats_response_default import (
    GetAssetsByAssetIdFormatsResponseDefault,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    asset_id: str,
    *,
    per_page: int | Unset = UNSET,
    last_id: str | Unset = UNSET,
    include_all_versions: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["per_page"] = per_page

    params["last_id"] = last_id

    params["include_all_versions"] = include_all_versions

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/assets/{asset_id}/formats/".format(
            asset_id=quote(str(asset_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | FormatsSchema | GetAssetsByAssetIdFormatsResponseDefault:
    if response.status_code == 200:
        response_200 = FormatsSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = GetAssetsByAssetIdFormatsResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | FormatsSchema | GetAssetsByAssetIdFormatsResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    last_id: str | Unset = UNSET,
    include_all_versions: bool | Unset = UNSET,
) -> Response[Any | FormatsSchema | GetAssetsByAssetIdFormatsResponseDefault]:
    """Get all asset's formats


    Required roles:
     - can_read_formats

    Args:
        asset_id (str):
        per_page (int | Unset):
        last_id (str | Unset):
        include_all_versions (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FormatsSchema | GetAssetsByAssetIdFormatsResponseDefault]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        per_page=per_page,
        last_id=last_id,
        include_all_versions=include_all_versions,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    last_id: str | Unset = UNSET,
    include_all_versions: bool | Unset = UNSET,
) -> Any | FormatsSchema | GetAssetsByAssetIdFormatsResponseDefault | None:
    """Get all asset's formats


    Required roles:
     - can_read_formats

    Args:
        asset_id (str):
        per_page (int | Unset):
        last_id (str | Unset):
        include_all_versions (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FormatsSchema | GetAssetsByAssetIdFormatsResponseDefault
    """

    return sync_detailed(
        asset_id=asset_id,
        client=client,
        per_page=per_page,
        last_id=last_id,
        include_all_versions=include_all_versions,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    last_id: str | Unset = UNSET,
    include_all_versions: bool | Unset = UNSET,
) -> Response[Any | FormatsSchema | GetAssetsByAssetIdFormatsResponseDefault]:
    """Get all asset's formats


    Required roles:
     - can_read_formats

    Args:
        asset_id (str):
        per_page (int | Unset):
        last_id (str | Unset):
        include_all_versions (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FormatsSchema | GetAssetsByAssetIdFormatsResponseDefault]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        per_page=per_page,
        last_id=last_id,
        include_all_versions=include_all_versions,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    last_id: str | Unset = UNSET,
    include_all_versions: bool | Unset = UNSET,
) -> Any | FormatsSchema | GetAssetsByAssetIdFormatsResponseDefault | None:
    """Get all asset's formats


    Required roles:
     - can_read_formats

    Args:
        asset_id (str):
        per_page (int | Unset):
        last_id (str | Unset):
        include_all_versions (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FormatsSchema | GetAssetsByAssetIdFormatsResponseDefault
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            client=client,
            per_page=per_page,
            last_id=last_id,
            include_all_versions=include_all_versions,
        )
    ).parsed
