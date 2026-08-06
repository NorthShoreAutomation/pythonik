from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_storage_gateways_response_default import (
    GetStorageGatewaysResponseDefault,
)
from ...models.iconik_storage_gateways_schema import IconikStorageGatewaysSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    cluster_id: str | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    query: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["cluster_id"] = cluster_id

    params["page"] = page

    params["per_page"] = per_page

    params["query"] = query

    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/storage_gateways/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetStorageGatewaysResponseDefault | IconikStorageGatewaysSchema:
    if response.status_code == 200:
        response_200 = IconikStorageGatewaysSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = GetStorageGatewaysResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetStorageGatewaysResponseDefault | IconikStorageGatewaysSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    cluster_id: str | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    query: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> Response[Any | GetStorageGatewaysResponseDefault | IconikStorageGatewaysSchema]:
    """Get all storage gateways

    Args:
        cluster_id (str | Unset):
        page (int | Unset):
        per_page (int | Unset):
        query (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetStorageGatewaysResponseDefault | IconikStorageGatewaysSchema]
    """

    kwargs = _get_kwargs(
        cluster_id=cluster_id,
        page=page,
        per_page=per_page,
        query=query,
        sort=sort,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    cluster_id: str | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    query: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> Any | GetStorageGatewaysResponseDefault | IconikStorageGatewaysSchema | None:
    """Get all storage gateways

    Args:
        cluster_id (str | Unset):
        page (int | Unset):
        per_page (int | Unset):
        query (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetStorageGatewaysResponseDefault | IconikStorageGatewaysSchema
    """

    return sync_detailed(
        client=client,
        cluster_id=cluster_id,
        page=page,
        per_page=per_page,
        query=query,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    cluster_id: str | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    query: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> Response[Any | GetStorageGatewaysResponseDefault | IconikStorageGatewaysSchema]:
    """Get all storage gateways

    Args:
        cluster_id (str | Unset):
        page (int | Unset):
        per_page (int | Unset):
        query (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetStorageGatewaysResponseDefault | IconikStorageGatewaysSchema]
    """

    kwargs = _get_kwargs(
        cluster_id=cluster_id,
        page=page,
        per_page=per_page,
        query=query,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    cluster_id: str | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    query: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> Any | GetStorageGatewaysResponseDefault | IconikStorageGatewaysSchema | None:
    """Get all storage gateways

    Args:
        cluster_id (str | Unset):
        page (int | Unset):
        per_page (int | Unset):
        query (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetStorageGatewaysResponseDefault | IconikStorageGatewaysSchema
    """

    return (
        await asyncio_detailed(
            client=client,
            cluster_id=cluster_id,
            page=page,
            per_page=per_page,
            query=query,
            sort=sort,
        )
    ).parsed
