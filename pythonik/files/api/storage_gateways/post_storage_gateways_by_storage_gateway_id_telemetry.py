from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.iconik_storage_gateway_telemetry_schema import (
    IconikStorageGatewayTelemetrySchema,
)
from ...models.post_storage_gateways_by_storage_gateway_id_telemetry_response_default import (
    PostStorageGatewaysByStorageGatewayIdTelemetryResponseDefault,
)
from ...types import Response


def _get_kwargs(
    storage_gateway_id: str,
    *,
    body: IconikStorageGatewayTelemetrySchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/storage_gateways/{storage_gateway_id}/telemetry/".format(
            storage_gateway_id=quote(str(storage_gateway_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostStorageGatewaysByStorageGatewayIdTelemetryResponseDefault:
    if response.status_code == 201:
        response_201 = cast(Any, None)
        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = (
        PostStorageGatewaysByStorageGatewayIdTelemetryResponseDefault.from_dict(
            response.json()
        )
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PostStorageGatewaysByStorageGatewayIdTelemetryResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    storage_gateway_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: IconikStorageGatewayTelemetrySchema,
) -> Response[Any | PostStorageGatewaysByStorageGatewayIdTelemetryResponseDefault]:
    """Create telemetry

    Args:
        storage_gateway_id (str):
        body (IconikStorageGatewayTelemetrySchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostStorageGatewaysByStorageGatewayIdTelemetryResponseDefault]
    """

    kwargs = _get_kwargs(
        storage_gateway_id=storage_gateway_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    storage_gateway_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: IconikStorageGatewayTelemetrySchema,
) -> Any | PostStorageGatewaysByStorageGatewayIdTelemetryResponseDefault | None:
    """Create telemetry

    Args:
        storage_gateway_id (str):
        body (IconikStorageGatewayTelemetrySchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostStorageGatewaysByStorageGatewayIdTelemetryResponseDefault
    """

    return sync_detailed(
        storage_gateway_id=storage_gateway_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    storage_gateway_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: IconikStorageGatewayTelemetrySchema,
) -> Response[Any | PostStorageGatewaysByStorageGatewayIdTelemetryResponseDefault]:
    """Create telemetry

    Args:
        storage_gateway_id (str):
        body (IconikStorageGatewayTelemetrySchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostStorageGatewaysByStorageGatewayIdTelemetryResponseDefault]
    """

    kwargs = _get_kwargs(
        storage_gateway_id=storage_gateway_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    storage_gateway_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: IconikStorageGatewayTelemetrySchema,
) -> Any | PostStorageGatewaysByStorageGatewayIdTelemetryResponseDefault | None:
    """Create telemetry

    Args:
        storage_gateway_id (str):
        body (IconikStorageGatewayTelemetrySchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostStorageGatewaysByStorageGatewayIdTelemetryResponseDefault
    """

    return (
        await asyncio_detailed(
            storage_gateway_id=storage_gateway_id,
            client=client,
            body=body,
        )
    ).parsed
