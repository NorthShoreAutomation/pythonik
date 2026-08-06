from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.assets_schema import AssetsSchema
from ...models.get_assets_response_default import GetAssetsResponseDefault
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
    scroll: bool | Unset = UNSET,
    scroll_id: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    field_name: str | Unset = UNSET,
    favoured_by: str | Unset = UNSET,
    types: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["per_page"] = per_page

    params["page"] = page

    params["scroll"] = scroll

    params["scroll_id"] = scroll_id

    params["sort"] = sort

    params["field_name"] = field_name

    params["favoured_by"] = favoured_by

    params["types"] = types

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/assets/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | AssetsSchema | GetAssetsResponseDefault:
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

    response_default = GetAssetsResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | AssetsSchema | GetAssetsResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
    scroll: bool | Unset = UNSET,
    scroll_id: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    field_name: str | Unset = UNSET,
    favoured_by: str | Unset = UNSET,
    types: str | Unset = UNSET,
) -> Response[Any | AssetsSchema | GetAssetsResponseDefault]:
    """Get list of assets


    Required roles:
     - can_read_assets

    Args:
        per_page (int | Unset):
        page (int | Unset):
        scroll (bool | Unset):
        scroll_id (str | Unset):
        sort (str | Unset):
        field_name (str | Unset):
        favoured_by (str | Unset):
        types (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AssetsSchema | GetAssetsResponseDefault]
    """

    kwargs = _get_kwargs(
        per_page=per_page,
        page=page,
        scroll=scroll,
        scroll_id=scroll_id,
        sort=sort,
        field_name=field_name,
        favoured_by=favoured_by,
        types=types,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
    scroll: bool | Unset = UNSET,
    scroll_id: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    field_name: str | Unset = UNSET,
    favoured_by: str | Unset = UNSET,
    types: str | Unset = UNSET,
) -> Any | AssetsSchema | GetAssetsResponseDefault | None:
    """Get list of assets


    Required roles:
     - can_read_assets

    Args:
        per_page (int | Unset):
        page (int | Unset):
        scroll (bool | Unset):
        scroll_id (str | Unset):
        sort (str | Unset):
        field_name (str | Unset):
        favoured_by (str | Unset):
        types (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AssetsSchema | GetAssetsResponseDefault
    """

    return sync_detailed(
        client=client,
        per_page=per_page,
        page=page,
        scroll=scroll,
        scroll_id=scroll_id,
        sort=sort,
        field_name=field_name,
        favoured_by=favoured_by,
        types=types,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
    scroll: bool | Unset = UNSET,
    scroll_id: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    field_name: str | Unset = UNSET,
    favoured_by: str | Unset = UNSET,
    types: str | Unset = UNSET,
) -> Response[Any | AssetsSchema | GetAssetsResponseDefault]:
    """Get list of assets


    Required roles:
     - can_read_assets

    Args:
        per_page (int | Unset):
        page (int | Unset):
        scroll (bool | Unset):
        scroll_id (str | Unset):
        sort (str | Unset):
        field_name (str | Unset):
        favoured_by (str | Unset):
        types (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AssetsSchema | GetAssetsResponseDefault]
    """

    kwargs = _get_kwargs(
        per_page=per_page,
        page=page,
        scroll=scroll,
        scroll_id=scroll_id,
        sort=sort,
        field_name=field_name,
        favoured_by=favoured_by,
        types=types,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
    scroll: bool | Unset = UNSET,
    scroll_id: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    field_name: str | Unset = UNSET,
    favoured_by: str | Unset = UNSET,
    types: str | Unset = UNSET,
) -> Any | AssetsSchema | GetAssetsResponseDefault | None:
    """Get list of assets


    Required roles:
     - can_read_assets

    Args:
        per_page (int | Unset):
        page (int | Unset):
        scroll (bool | Unset):
        scroll_id (str | Unset):
        sort (str | Unset):
        field_name (str | Unset):
        favoured_by (str | Unset):
        types (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AssetsSchema | GetAssetsResponseDefault
    """

    return (
        await asyncio_detailed(
            client=client,
            per_page=per_page,
            page=page,
            scroll=scroll,
            scroll_id=scroll_id,
            sort=sort,
            field_name=field_name,
            favoured_by=favoured_by,
            types=types,
        )
    ).parsed
