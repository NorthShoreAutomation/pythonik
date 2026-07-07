from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.favorites_schema import FavoritesSchema
from ...models.get_favorites_response_default_type_0 import (
    GetFavoritesResponseDefaultType0,
)
from ...models.get_favorites_response_default_type_1 import (
    GetFavoritesResponseDefaultType1,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    per_page: int | Unset = UNSET,
    page: int | Unset = 1,
    sort: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["per_page"] = per_page

    params["page"] = page

    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/favorites/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | FavoritesSchema
    | GetFavoritesResponseDefaultType0
    | GetFavoritesResponseDefaultType1
):
    if response.status_code == 200:
        response_200 = FavoritesSchema.from_dict(response.json())

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
    ) -> GetFavoritesResponseDefaultType0 | GetFavoritesResponseDefaultType1:
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = GetFavoritesResponseDefaultType0.from_dict(data)

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = GetFavoritesResponseDefaultType1.from_dict(data)

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | FavoritesSchema
    | GetFavoritesResponseDefaultType0
    | GetFavoritesResponseDefaultType1
]:
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
    page: int | Unset = 1,
    sort: str | Unset = UNSET,
) -> Response[
    Any
    | FavoritesSchema
    | GetFavoritesResponseDefaultType0
    | GetFavoritesResponseDefaultType1
]:
    """Get list of favorite objects


    Required roles:
     - can_read_assets

    Args:
        per_page (int | Unset):
        page (int | Unset):  Default: 1.
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FavoritesSchema | GetFavoritesResponseDefaultType0 | GetFavoritesResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        per_page=per_page,
        page=page,
        sort=sort,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    page: int | Unset = 1,
    sort: str | Unset = UNSET,
) -> (
    Any
    | FavoritesSchema
    | GetFavoritesResponseDefaultType0
    | GetFavoritesResponseDefaultType1
    | None
):
    """Get list of favorite objects


    Required roles:
     - can_read_assets

    Args:
        per_page (int | Unset):
        page (int | Unset):  Default: 1.
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FavoritesSchema | GetFavoritesResponseDefaultType0 | GetFavoritesResponseDefaultType1
    """

    return sync_detailed(
        client=client,
        per_page=per_page,
        page=page,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    page: int | Unset = 1,
    sort: str | Unset = UNSET,
) -> Response[
    Any
    | FavoritesSchema
    | GetFavoritesResponseDefaultType0
    | GetFavoritesResponseDefaultType1
]:
    """Get list of favorite objects


    Required roles:
     - can_read_assets

    Args:
        per_page (int | Unset):
        page (int | Unset):  Default: 1.
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FavoritesSchema | GetFavoritesResponseDefaultType0 | GetFavoritesResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        per_page=per_page,
        page=page,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    page: int | Unset = 1,
    sort: str | Unset = UNSET,
) -> (
    Any
    | FavoritesSchema
    | GetFavoritesResponseDefaultType0
    | GetFavoritesResponseDefaultType1
    | None
):
    """Get list of favorite objects


    Required roles:
     - can_read_assets

    Args:
        per_page (int | Unset):
        page (int | Unset):  Default: 1.
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FavoritesSchema | GetFavoritesResponseDefaultType0 | GetFavoritesResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            client=client,
            per_page=per_page,
            page=page,
            sort=sort,
        )
    ).parsed
