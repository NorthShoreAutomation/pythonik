from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_storage_gateway_clusters_by_cluster_id_response_default_type_0 import (
    GetStorageGatewayClustersByClusterIdResponseDefaultType0,
)
from ...models.get_storage_gateway_clusters_by_cluster_id_response_default_type_1 import (
    GetStorageGatewayClustersByClusterIdResponseDefaultType1,
)
from ...models.iconik_storage_gateway_cluster_read_schema import (
    IconikStorageGatewayClusterReadSchema,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    cluster_id: str,
    *,
    view_nodes: bool | Unset = UNSET,
    view_stats: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["view_nodes"] = view_nodes

    params["view_stats"] = view_stats

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/storage_gateway_clusters/{cluster_id}/".format(
            cluster_id=quote(str(cluster_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetStorageGatewayClustersByClusterIdResponseDefaultType0
    | GetStorageGatewayClustersByClusterIdResponseDefaultType1
    | IconikStorageGatewayClusterReadSchema
):
    if response.status_code == 200:
        response_200 = IconikStorageGatewayClusterReadSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    def _parse_response_default(
        data: object,
    ) -> (
        GetStorageGatewayClustersByClusterIdResponseDefaultType0
        | GetStorageGatewayClustersByClusterIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetStorageGatewayClustersByClusterIdResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            GetStorageGatewayClustersByClusterIdResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetStorageGatewayClustersByClusterIdResponseDefaultType0
    | GetStorageGatewayClustersByClusterIdResponseDefaultType1
    | IconikStorageGatewayClusterReadSchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    cluster_id: str,
    *,
    client: AuthenticatedClient | Client,
    view_nodes: bool | Unset = UNSET,
    view_stats: bool | Unset = UNSET,
) -> Response[
    Any
    | GetStorageGatewayClustersByClusterIdResponseDefaultType0
    | GetStorageGatewayClustersByClusterIdResponseDefaultType1
    | IconikStorageGatewayClusterReadSchema
]:
    """Get a specific storage gateway cluster

    Args:
        cluster_id (str):
        view_nodes (bool | Unset):
        view_stats (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetStorageGatewayClustersByClusterIdResponseDefaultType0 | GetStorageGatewayClustersByClusterIdResponseDefaultType1 | IconikStorageGatewayClusterReadSchema]
    """

    kwargs = _get_kwargs(
        cluster_id=cluster_id,
        view_nodes=view_nodes,
        view_stats=view_stats,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    cluster_id: str,
    *,
    client: AuthenticatedClient | Client,
    view_nodes: bool | Unset = UNSET,
    view_stats: bool | Unset = UNSET,
) -> (
    Any
    | GetStorageGatewayClustersByClusterIdResponseDefaultType0
    | GetStorageGatewayClustersByClusterIdResponseDefaultType1
    | IconikStorageGatewayClusterReadSchema
    | None
):
    """Get a specific storage gateway cluster

    Args:
        cluster_id (str):
        view_nodes (bool | Unset):
        view_stats (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetStorageGatewayClustersByClusterIdResponseDefaultType0 | GetStorageGatewayClustersByClusterIdResponseDefaultType1 | IconikStorageGatewayClusterReadSchema
    """

    return sync_detailed(
        cluster_id=cluster_id,
        client=client,
        view_nodes=view_nodes,
        view_stats=view_stats,
    ).parsed


async def asyncio_detailed(
    cluster_id: str,
    *,
    client: AuthenticatedClient | Client,
    view_nodes: bool | Unset = UNSET,
    view_stats: bool | Unset = UNSET,
) -> Response[
    Any
    | GetStorageGatewayClustersByClusterIdResponseDefaultType0
    | GetStorageGatewayClustersByClusterIdResponseDefaultType1
    | IconikStorageGatewayClusterReadSchema
]:
    """Get a specific storage gateway cluster

    Args:
        cluster_id (str):
        view_nodes (bool | Unset):
        view_stats (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetStorageGatewayClustersByClusterIdResponseDefaultType0 | GetStorageGatewayClustersByClusterIdResponseDefaultType1 | IconikStorageGatewayClusterReadSchema]
    """

    kwargs = _get_kwargs(
        cluster_id=cluster_id,
        view_nodes=view_nodes,
        view_stats=view_stats,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    cluster_id: str,
    *,
    client: AuthenticatedClient | Client,
    view_nodes: bool | Unset = UNSET,
    view_stats: bool | Unset = UNSET,
) -> (
    Any
    | GetStorageGatewayClustersByClusterIdResponseDefaultType0
    | GetStorageGatewayClustersByClusterIdResponseDefaultType1
    | IconikStorageGatewayClusterReadSchema
    | None
):
    """Get a specific storage gateway cluster

    Args:
        cluster_id (str):
        view_nodes (bool | Unset):
        view_stats (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetStorageGatewayClustersByClusterIdResponseDefaultType0 | GetStorageGatewayClustersByClusterIdResponseDefaultType1 | IconikStorageGatewayClusterReadSchema
    """

    return (
        await asyncio_detailed(
            cluster_id=cluster_id,
            client=client,
            view_nodes=view_nodes,
            view_stats=view_stats,
        )
    ).parsed
