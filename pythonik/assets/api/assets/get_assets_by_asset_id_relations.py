from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.assets_schema import AssetsSchema
from ...models.get_assets_by_asset_id_relations_response_default import (
    GetAssetsByAssetIdRelationsResponseDefault,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    asset_id: str,
    *,
    include_deleted: bool | Unset = UNSET,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    search_after: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["include_deleted"] = include_deleted

    params["per_page"] = per_page

    params["page"] = page

    params["sort"] = sort

    params["search_after"] = search_after

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/assets/{asset_id}/relations/".format(
            asset_id=quote(str(asset_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | AssetsSchema | GetAssetsByAssetIdRelationsResponseDefault:
    if response.status_code == 200:
        response_200 = AssetsSchema.from_dict(response.json())

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

    response_default = GetAssetsByAssetIdRelationsResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | AssetsSchema | GetAssetsByAssetIdRelationsResponseDefault]:
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
    include_deleted: bool | Unset = UNSET,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    search_after: str | Unset = UNSET,
) -> Response[Any | AssetsSchema | GetAssetsByAssetIdRelationsResponseDefault]:
    """Returns an assets relations


    Required roles:
     - can_read_asset_relations

    Args:
        asset_id (str):
        include_deleted (bool | Unset):
        per_page (int | Unset):
        page (int | Unset):
        sort (str | Unset):
        search_after (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AssetsSchema | GetAssetsByAssetIdRelationsResponseDefault]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        include_deleted=include_deleted,
        per_page=per_page,
        page=page,
        sort=sort,
        search_after=search_after,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
    include_deleted: bool | Unset = UNSET,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    search_after: str | Unset = UNSET,
) -> Any | AssetsSchema | GetAssetsByAssetIdRelationsResponseDefault | None:
    """Returns an assets relations


    Required roles:
     - can_read_asset_relations

    Args:
        asset_id (str):
        include_deleted (bool | Unset):
        per_page (int | Unset):
        page (int | Unset):
        sort (str | Unset):
        search_after (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AssetsSchema | GetAssetsByAssetIdRelationsResponseDefault
    """

    return sync_detailed(
        asset_id=asset_id,
        client=client,
        include_deleted=include_deleted,
        per_page=per_page,
        page=page,
        sort=sort,
        search_after=search_after,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
    include_deleted: bool | Unset = UNSET,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    search_after: str | Unset = UNSET,
) -> Response[Any | AssetsSchema | GetAssetsByAssetIdRelationsResponseDefault]:
    """Returns an assets relations


    Required roles:
     - can_read_asset_relations

    Args:
        asset_id (str):
        include_deleted (bool | Unset):
        per_page (int | Unset):
        page (int | Unset):
        sort (str | Unset):
        search_after (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AssetsSchema | GetAssetsByAssetIdRelationsResponseDefault]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        include_deleted=include_deleted,
        per_page=per_page,
        page=page,
        sort=sort,
        search_after=search_after,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
    include_deleted: bool | Unset = UNSET,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    search_after: str | Unset = UNSET,
) -> Any | AssetsSchema | GetAssetsByAssetIdRelationsResponseDefault | None:
    """Returns an assets relations


    Required roles:
     - can_read_asset_relations

    Args:
        asset_id (str):
        include_deleted (bool | Unset):
        per_page (int | Unset):
        page (int | Unset):
        sort (str | Unset):
        search_after (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AssetsSchema | GetAssetsByAssetIdRelationsResponseDefault
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            client=client,
            include_deleted=include_deleted,
            per_page=per_page,
            page=page,
            sort=sort,
            search_after=search_after,
        )
    ).parsed
