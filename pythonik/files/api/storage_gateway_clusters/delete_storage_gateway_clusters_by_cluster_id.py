from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_storage_gateway_clusters_by_cluster_id_response_default import (
    DeleteStorageGatewayClustersByClusterIdResponseDefault,
)
from ...types import Response


def _get_kwargs(
    cluster_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/storage_gateway_clusters/{cluster_id}/".format(
            cluster_id=quote(str(cluster_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DeleteStorageGatewayClustersByClusterIdResponseDefault:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = DeleteStorageGatewayClustersByClusterIdResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DeleteStorageGatewayClustersByClusterIdResponseDefault]:
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
) -> Response[Any | DeleteStorageGatewayClustersByClusterIdResponseDefault]:
    """Delete a storage gateway cluster

    Args:
        cluster_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteStorageGatewayClustersByClusterIdResponseDefault]
    """

    kwargs = _get_kwargs(
        cluster_id=cluster_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    cluster_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | DeleteStorageGatewayClustersByClusterIdResponseDefault | None:
    """Delete a storage gateway cluster

    Args:
        cluster_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteStorageGatewayClustersByClusterIdResponseDefault
    """

    return sync_detailed(
        cluster_id=cluster_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    cluster_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DeleteStorageGatewayClustersByClusterIdResponseDefault]:
    """Delete a storage gateway cluster

    Args:
        cluster_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteStorageGatewayClustersByClusterIdResponseDefault]
    """

    kwargs = _get_kwargs(
        cluster_id=cluster_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    cluster_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | DeleteStorageGatewayClustersByClusterIdResponseDefault | None:
    """Delete a storage gateway cluster

    Args:
        cluster_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteStorageGatewayClustersByClusterIdResponseDefault
    """

    return (
        await asyncio_detailed(
            cluster_id=cluster_id,
            client=client,
        )
    ).parsed
