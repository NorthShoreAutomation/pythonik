from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.asset_history_entities_schema import AssetHistoryEntitiesSchema
from ...models.get_assets_by_asset_id_history_response_default_type_0 import (
    GetAssetsByAssetIdHistoryResponseDefaultType0,
)
from ...models.get_assets_by_asset_id_history_response_default_type_1 import (
    GetAssetsByAssetIdHistoryResponseDefaultType1,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    asset_id: str,
    *,
    per_page: int | Unset = UNSET,
    page: int | Unset = 1,
    sort: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["per_page"] = per_page

    params["page"] = page

    params["sort"] = sort

    params["filter"] = filter_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/assets/{asset_id}/history/".format(
            asset_id=quote(str(asset_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | AssetHistoryEntitiesSchema
    | GetAssetsByAssetIdHistoryResponseDefaultType0
    | GetAssetsByAssetIdHistoryResponseDefaultType1
):
    if response.status_code == 200:
        response_200 = AssetHistoryEntitiesSchema.from_dict(response.json())

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
        GetAssetsByAssetIdHistoryResponseDefaultType0
        | GetAssetsByAssetIdHistoryResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetAssetsByAssetIdHistoryResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            GetAssetsByAssetIdHistoryResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | AssetHistoryEntitiesSchema
    | GetAssetsByAssetIdHistoryResponseDefaultType0
    | GetAssetsByAssetIdHistoryResponseDefaultType1
]:
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
    page: int | Unset = 1,
    sort: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
) -> Response[
    Any
    | AssetHistoryEntitiesSchema
    | GetAssetsByAssetIdHistoryResponseDefaultType0
    | GetAssetsByAssetIdHistoryResponseDefaultType1
]:
    """Get list of history entities for asset


    Required roles:
     - can_read_assets_history

    Args:
        asset_id (str):
        per_page (int | Unset):
        page (int | Unset):  Default: 1.
        sort (str | Unset):
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AssetHistoryEntitiesSchema | GetAssetsByAssetIdHistoryResponseDefaultType0 | GetAssetsByAssetIdHistoryResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        per_page=per_page,
        page=page,
        sort=sort,
        filter_=filter_,
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
    page: int | Unset = 1,
    sort: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
) -> (
    Any
    | AssetHistoryEntitiesSchema
    | GetAssetsByAssetIdHistoryResponseDefaultType0
    | GetAssetsByAssetIdHistoryResponseDefaultType1
    | None
):
    """Get list of history entities for asset


    Required roles:
     - can_read_assets_history

    Args:
        asset_id (str):
        per_page (int | Unset):
        page (int | Unset):  Default: 1.
        sort (str | Unset):
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AssetHistoryEntitiesSchema | GetAssetsByAssetIdHistoryResponseDefaultType0 | GetAssetsByAssetIdHistoryResponseDefaultType1
    """

    return sync_detailed(
        asset_id=asset_id,
        client=client,
        per_page=per_page,
        page=page,
        sort=sort,
        filter_=filter_,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    page: int | Unset = 1,
    sort: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
) -> Response[
    Any
    | AssetHistoryEntitiesSchema
    | GetAssetsByAssetIdHistoryResponseDefaultType0
    | GetAssetsByAssetIdHistoryResponseDefaultType1
]:
    """Get list of history entities for asset


    Required roles:
     - can_read_assets_history

    Args:
        asset_id (str):
        per_page (int | Unset):
        page (int | Unset):  Default: 1.
        sort (str | Unset):
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AssetHistoryEntitiesSchema | GetAssetsByAssetIdHistoryResponseDefaultType0 | GetAssetsByAssetIdHistoryResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        per_page=per_page,
        page=page,
        sort=sort,
        filter_=filter_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    page: int | Unset = 1,
    sort: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
) -> (
    Any
    | AssetHistoryEntitiesSchema
    | GetAssetsByAssetIdHistoryResponseDefaultType0
    | GetAssetsByAssetIdHistoryResponseDefaultType1
    | None
):
    """Get list of history entities for asset


    Required roles:
     - can_read_assets_history

    Args:
        asset_id (str):
        per_page (int | Unset):
        page (int | Unset):  Default: 1.
        sort (str | Unset):
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AssetHistoryEntitiesSchema | GetAssetsByAssetIdHistoryResponseDefaultType0 | GetAssetsByAssetIdHistoryResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            client=client,
            per_page=per_page,
            page=page,
            sort=sort,
            filter_=filter_,
        )
    ).parsed
