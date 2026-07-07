from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_storage_gateways_telemetry_by_worker_id_response_default_type_0 import (
    GetStorageGatewaysTelemetryByWorkerIdResponseDefaultType0,
)
from ...models.get_storage_gateways_telemetry_by_worker_id_response_default_type_1 import (
    GetStorageGatewaysTelemetryByWorkerIdResponseDefaultType1,
)
from ...models.iconik_storage_gateway_telemetry_schema import (
    IconikStorageGatewayTelemetrySchema,
)
from ...types import Response


def _get_kwargs(
    worker_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/storage_gateways/telemetry/{worker_id}/".format(
            worker_id=quote(str(worker_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetStorageGatewaysTelemetryByWorkerIdResponseDefaultType0
    | GetStorageGatewaysTelemetryByWorkerIdResponseDefaultType1
    | IconikStorageGatewayTelemetrySchema
):
    if response.status_code == 200:
        response_200 = IconikStorageGatewayTelemetrySchema.from_dict(response.json())

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
        GetStorageGatewaysTelemetryByWorkerIdResponseDefaultType0
        | GetStorageGatewaysTelemetryByWorkerIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetStorageGatewaysTelemetryByWorkerIdResponseDefaultType0.from_dict(
                    data
                )
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            GetStorageGatewaysTelemetryByWorkerIdResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetStorageGatewaysTelemetryByWorkerIdResponseDefaultType0
    | GetStorageGatewaysTelemetryByWorkerIdResponseDefaultType1
    | IconikStorageGatewayTelemetrySchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    worker_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetStorageGatewaysTelemetryByWorkerIdResponseDefaultType0
    | GetStorageGatewaysTelemetryByWorkerIdResponseDefaultType1
    | IconikStorageGatewayTelemetrySchema
]:
    """Get telemetry for a specific worker


    Required roles:
     - can_read_storages

    Args:
        worker_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetStorageGatewaysTelemetryByWorkerIdResponseDefaultType0 | GetStorageGatewaysTelemetryByWorkerIdResponseDefaultType1 | IconikStorageGatewayTelemetrySchema]
    """

    kwargs = _get_kwargs(
        worker_id=worker_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    worker_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetStorageGatewaysTelemetryByWorkerIdResponseDefaultType0
    | GetStorageGatewaysTelemetryByWorkerIdResponseDefaultType1
    | IconikStorageGatewayTelemetrySchema
    | None
):
    """Get telemetry for a specific worker


    Required roles:
     - can_read_storages

    Args:
        worker_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetStorageGatewaysTelemetryByWorkerIdResponseDefaultType0 | GetStorageGatewaysTelemetryByWorkerIdResponseDefaultType1 | IconikStorageGatewayTelemetrySchema
    """

    return sync_detailed(
        worker_id=worker_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    worker_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetStorageGatewaysTelemetryByWorkerIdResponseDefaultType0
    | GetStorageGatewaysTelemetryByWorkerIdResponseDefaultType1
    | IconikStorageGatewayTelemetrySchema
]:
    """Get telemetry for a specific worker


    Required roles:
     - can_read_storages

    Args:
        worker_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetStorageGatewaysTelemetryByWorkerIdResponseDefaultType0 | GetStorageGatewaysTelemetryByWorkerIdResponseDefaultType1 | IconikStorageGatewayTelemetrySchema]
    """

    kwargs = _get_kwargs(
        worker_id=worker_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    worker_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetStorageGatewaysTelemetryByWorkerIdResponseDefaultType0
    | GetStorageGatewaysTelemetryByWorkerIdResponseDefaultType1
    | IconikStorageGatewayTelemetrySchema
    | None
):
    """Get telemetry for a specific worker


    Required roles:
     - can_read_storages

    Args:
        worker_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetStorageGatewaysTelemetryByWorkerIdResponseDefaultType0 | GetStorageGatewaysTelemetryByWorkerIdResponseDefaultType1 | IconikStorageGatewayTelemetrySchema
    """

    return (
        await asyncio_detailed(
            worker_id=worker_id,
            client=client,
        )
    ).parsed
