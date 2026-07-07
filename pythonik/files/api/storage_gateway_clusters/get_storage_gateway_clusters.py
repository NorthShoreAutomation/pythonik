from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_storage_gateway_clusters_response_default_type_0 import (
    GetStorageGatewayClustersResponseDefaultType0,
)
from ...models.get_storage_gateway_clusters_response_default_type_1 import (
    GetStorageGatewayClustersResponseDefaultType1,
)
from ...models.iconik_storage_gateway_clusters_schema import (
    IconikStorageGatewayClustersSchema,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = 1,
    per_page: int | Unset = 10,
    sort: str | Unset = UNSET,
    query: str | Unset = UNSET,
    view_nodes: bool | Unset = UNSET,
    view_stats: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["per_page"] = per_page

    params["sort"] = sort

    params["query"] = query

    params["view_nodes"] = view_nodes

    params["view_stats"] = view_stats

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/storage_gateway_clusters/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetStorageGatewayClustersResponseDefaultType0
    | GetStorageGatewayClustersResponseDefaultType1
    | IconikStorageGatewayClustersSchema
):
    if response.status_code == 200:
        response_200 = IconikStorageGatewayClustersSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    def _parse_response_default(
        data: object,
    ) -> (
        GetStorageGatewayClustersResponseDefaultType0
        | GetStorageGatewayClustersResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetStorageGatewayClustersResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            GetStorageGatewayClustersResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetStorageGatewayClustersResponseDefaultType0
    | GetStorageGatewayClustersResponseDefaultType1
    | IconikStorageGatewayClustersSchema
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
    page: int | Unset = 1,
    per_page: int | Unset = 10,
    sort: str | Unset = UNSET,
    query: str | Unset = UNSET,
    view_nodes: bool | Unset = UNSET,
    view_stats: bool | Unset = UNSET,
) -> Response[
    Any
    | GetStorageGatewayClustersResponseDefaultType0
    | GetStorageGatewayClustersResponseDefaultType1
    | IconikStorageGatewayClustersSchema
]:
    """Get all storage gateway clusters

    Args:
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 10.
        sort (str | Unset):
        query (str | Unset):
        view_nodes (bool | Unset):
        view_stats (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetStorageGatewayClustersResponseDefaultType0 | GetStorageGatewayClustersResponseDefaultType1 | IconikStorageGatewayClustersSchema]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        sort=sort,
        query=query,
        view_nodes=view_nodes,
        view_stats=view_stats,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    per_page: int | Unset = 10,
    sort: str | Unset = UNSET,
    query: str | Unset = UNSET,
    view_nodes: bool | Unset = UNSET,
    view_stats: bool | Unset = UNSET,
) -> (
    Any
    | GetStorageGatewayClustersResponseDefaultType0
    | GetStorageGatewayClustersResponseDefaultType1
    | IconikStorageGatewayClustersSchema
    | None
):
    """Get all storage gateway clusters

    Args:
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 10.
        sort (str | Unset):
        query (str | Unset):
        view_nodes (bool | Unset):
        view_stats (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetStorageGatewayClustersResponseDefaultType0 | GetStorageGatewayClustersResponseDefaultType1 | IconikStorageGatewayClustersSchema
    """

    return sync_detailed(
        client=client,
        page=page,
        per_page=per_page,
        sort=sort,
        query=query,
        view_nodes=view_nodes,
        view_stats=view_stats,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    per_page: int | Unset = 10,
    sort: str | Unset = UNSET,
    query: str | Unset = UNSET,
    view_nodes: bool | Unset = UNSET,
    view_stats: bool | Unset = UNSET,
) -> Response[
    Any
    | GetStorageGatewayClustersResponseDefaultType0
    | GetStorageGatewayClustersResponseDefaultType1
    | IconikStorageGatewayClustersSchema
]:
    """Get all storage gateway clusters

    Args:
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 10.
        sort (str | Unset):
        query (str | Unset):
        view_nodes (bool | Unset):
        view_stats (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetStorageGatewayClustersResponseDefaultType0 | GetStorageGatewayClustersResponseDefaultType1 | IconikStorageGatewayClustersSchema]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        sort=sort,
        query=query,
        view_nodes=view_nodes,
        view_stats=view_stats,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    per_page: int | Unset = 10,
    sort: str | Unset = UNSET,
    query: str | Unset = UNSET,
    view_nodes: bool | Unset = UNSET,
    view_stats: bool | Unset = UNSET,
) -> (
    Any
    | GetStorageGatewayClustersResponseDefaultType0
    | GetStorageGatewayClustersResponseDefaultType1
    | IconikStorageGatewayClustersSchema
    | None
):
    """Get all storage gateway clusters

    Args:
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 10.
        sort (str | Unset):
        query (str | Unset):
        view_nodes (bool | Unset):
        view_stats (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetStorageGatewayClustersResponseDefaultType0 | GetStorageGatewayClustersResponseDefaultType1 | IconikStorageGatewayClustersSchema
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            per_page=per_page,
            sort=sort,
            query=query,
            view_nodes=view_nodes,
            view_stats=view_stats,
        )
    ).parsed
