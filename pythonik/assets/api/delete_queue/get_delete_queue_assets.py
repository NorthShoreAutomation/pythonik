from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.assets_schema import AssetsSchema
from ...models.get_delete_queue_assets_response_default_type_0 import (
    GetDeleteQueueAssetsResponseDefaultType0,
)
from ...models.get_delete_queue_assets_response_default_type_1 import (
    GetDeleteQueueAssetsResponseDefaultType1,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
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
        "url": "/v1/delete_queue/assets/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | AssetsSchema
    | GetDeleteQueueAssetsResponseDefaultType0
    | GetDeleteQueueAssetsResponseDefaultType1
):
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

    def _parse_response_default(
        data: object,
    ) -> (
        GetDeleteQueueAssetsResponseDefaultType0
        | GetDeleteQueueAssetsResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetDeleteQueueAssetsResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = GetDeleteQueueAssetsResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | AssetsSchema
    | GetDeleteQueueAssetsResponseDefaultType0
    | GetDeleteQueueAssetsResponseDefaultType1
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
    filter_: str | Unset = UNSET,
) -> Response[
    Any
    | AssetsSchema
    | GetDeleteQueueAssetsResponseDefaultType0
    | GetDeleteQueueAssetsResponseDefaultType1
]:
    """Get deleted objects


    Required roles:
     - can_read_assets

    Args:
        per_page (int | Unset):
        page (int | Unset):  Default: 1.
        sort (str | Unset):
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AssetsSchema | GetDeleteQueueAssetsResponseDefaultType0 | GetDeleteQueueAssetsResponseDefaultType1]
    """

    kwargs = _get_kwargs(
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
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    page: int | Unset = 1,
    sort: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
) -> (
    Any
    | AssetsSchema
    | GetDeleteQueueAssetsResponseDefaultType0
    | GetDeleteQueueAssetsResponseDefaultType1
    | None
):
    """Get deleted objects


    Required roles:
     - can_read_assets

    Args:
        per_page (int | Unset):
        page (int | Unset):  Default: 1.
        sort (str | Unset):
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AssetsSchema | GetDeleteQueueAssetsResponseDefaultType0 | GetDeleteQueueAssetsResponseDefaultType1
    """

    return sync_detailed(
        client=client,
        per_page=per_page,
        page=page,
        sort=sort,
        filter_=filter_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    page: int | Unset = 1,
    sort: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
) -> Response[
    Any
    | AssetsSchema
    | GetDeleteQueueAssetsResponseDefaultType0
    | GetDeleteQueueAssetsResponseDefaultType1
]:
    """Get deleted objects


    Required roles:
     - can_read_assets

    Args:
        per_page (int | Unset):
        page (int | Unset):  Default: 1.
        sort (str | Unset):
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AssetsSchema | GetDeleteQueueAssetsResponseDefaultType0 | GetDeleteQueueAssetsResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        per_page=per_page,
        page=page,
        sort=sort,
        filter_=filter_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    page: int | Unset = 1,
    sort: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
) -> (
    Any
    | AssetsSchema
    | GetDeleteQueueAssetsResponseDefaultType0
    | GetDeleteQueueAssetsResponseDefaultType1
    | None
):
    """Get deleted objects


    Required roles:
     - can_read_assets

    Args:
        per_page (int | Unset):
        page (int | Unset):  Default: 1.
        sort (str | Unset):
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AssetsSchema | GetDeleteQueueAssetsResponseDefaultType0 | GetDeleteQueueAssetsResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            client=client,
            per_page=per_page,
            page=page,
            sort=sort,
            filter_=filter_,
        )
    ).parsed
