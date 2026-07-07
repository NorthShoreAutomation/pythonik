from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_storage_gateway_clusters_by_cluster_id_response_default_type_0 import (
    DeleteStorageGatewayClustersByClusterIdResponseDefaultType0,
)
from ...models.delete_storage_gateway_clusters_by_cluster_id_response_default_type_1 import (
    DeleteStorageGatewayClustersByClusterIdResponseDefaultType1,
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
) -> (
    Any
    | DeleteStorageGatewayClustersByClusterIdResponseDefaultType0
    | DeleteStorageGatewayClustersByClusterIdResponseDefaultType1
):
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    def _parse_response_default(
        data: object,
    ) -> (
        DeleteStorageGatewayClustersByClusterIdResponseDefaultType0
        | DeleteStorageGatewayClustersByClusterIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                DeleteStorageGatewayClustersByClusterIdResponseDefaultType0.from_dict(
                    data
                )
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            DeleteStorageGatewayClustersByClusterIdResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | DeleteStorageGatewayClustersByClusterIdResponseDefaultType0
    | DeleteStorageGatewayClustersByClusterIdResponseDefaultType1
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
) -> Response[
    Any
    | DeleteStorageGatewayClustersByClusterIdResponseDefaultType0
    | DeleteStorageGatewayClustersByClusterIdResponseDefaultType1
]:
    """Delete a storage gateway cluster

    Args:
        cluster_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteStorageGatewayClustersByClusterIdResponseDefaultType0 | DeleteStorageGatewayClustersByClusterIdResponseDefaultType1]
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
) -> (
    Any
    | DeleteStorageGatewayClustersByClusterIdResponseDefaultType0
    | DeleteStorageGatewayClustersByClusterIdResponseDefaultType1
    | None
):
    """Delete a storage gateway cluster

    Args:
        cluster_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteStorageGatewayClustersByClusterIdResponseDefaultType0 | DeleteStorageGatewayClustersByClusterIdResponseDefaultType1
    """

    return sync_detailed(
        cluster_id=cluster_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    cluster_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | DeleteStorageGatewayClustersByClusterIdResponseDefaultType0
    | DeleteStorageGatewayClustersByClusterIdResponseDefaultType1
]:
    """Delete a storage gateway cluster

    Args:
        cluster_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteStorageGatewayClustersByClusterIdResponseDefaultType0 | DeleteStorageGatewayClustersByClusterIdResponseDefaultType1]
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
) -> (
    Any
    | DeleteStorageGatewayClustersByClusterIdResponseDefaultType0
    | DeleteStorageGatewayClustersByClusterIdResponseDefaultType1
    | None
):
    """Delete a storage gateway cluster

    Args:
        cluster_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteStorageGatewayClustersByClusterIdResponseDefaultType0 | DeleteStorageGatewayClustersByClusterIdResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            cluster_id=cluster_id,
            client=client,
        )
    ).parsed
