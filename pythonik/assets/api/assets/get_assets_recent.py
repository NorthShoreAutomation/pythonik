from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_assets_recent_response_default import GetAssetsRecentResponseDefault
from ...models.recent_assets_schema import RecentAssetsSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
    search_after: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["per_page"] = per_page

    params["page"] = page

    params["search_after"] = search_after

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/assets/recent/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetAssetsRecentResponseDefault | RecentAssetsSchema:
    if response.status_code == 200:
        response_200 = RecentAssetsSchema.from_dict(response.json())

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

    response_default = GetAssetsRecentResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetAssetsRecentResponseDefault | RecentAssetsSchema]:
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
    search_after: str | Unset = UNSET,
) -> Response[Any | GetAssetsRecentResponseDefault | RecentAssetsSchema]:
    """Get list of recently viewed assets


    Required roles:
     - can_read_assets

    Args:
        per_page (int | Unset):
        page (int | Unset):
        search_after (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAssetsRecentResponseDefault | RecentAssetsSchema]
    """

    kwargs = _get_kwargs(
        per_page=per_page,
        page=page,
        search_after=search_after,
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
    search_after: str | Unset = UNSET,
) -> Any | GetAssetsRecentResponseDefault | RecentAssetsSchema | None:
    """Get list of recently viewed assets


    Required roles:
     - can_read_assets

    Args:
        per_page (int | Unset):
        page (int | Unset):
        search_after (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAssetsRecentResponseDefault | RecentAssetsSchema
    """

    return sync_detailed(
        client=client,
        per_page=per_page,
        page=page,
        search_after=search_after,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
    search_after: str | Unset = UNSET,
) -> Response[Any | GetAssetsRecentResponseDefault | RecentAssetsSchema]:
    """Get list of recently viewed assets


    Required roles:
     - can_read_assets

    Args:
        per_page (int | Unset):
        page (int | Unset):
        search_after (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAssetsRecentResponseDefault | RecentAssetsSchema]
    """

    kwargs = _get_kwargs(
        per_page=per_page,
        page=page,
        search_after=search_after,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
    search_after: str | Unset = UNSET,
) -> Any | GetAssetsRecentResponseDefault | RecentAssetsSchema | None:
    """Get list of recently viewed assets


    Required roles:
     - can_read_assets

    Args:
        per_page (int | Unset):
        page (int | Unset):
        search_after (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAssetsRecentResponseDefault | RecentAssetsSchema
    """

    return (
        await asyncio_detailed(
            client=client,
            per_page=per_page,
            page=page,
            search_after=search_after,
        )
    ).parsed
