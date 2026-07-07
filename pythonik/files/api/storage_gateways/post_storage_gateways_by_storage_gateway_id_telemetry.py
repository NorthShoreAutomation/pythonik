from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.iconik_storage_gateway_telemetry_schema import (
    IconikStorageGatewayTelemetrySchema,
)
from ...models.post_storage_gateways_by_storage_gateway_id_telemetry_response_default_type_0 import (
    PostStorageGatewaysByStorageGatewayIdTelemetryResponseDefaultType0,
)
from ...models.post_storage_gateways_by_storage_gateway_id_telemetry_response_default_type_1 import (
    PostStorageGatewaysByStorageGatewayIdTelemetryResponseDefaultType1,
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
) -> (
    Any
    | PostStorageGatewaysByStorageGatewayIdTelemetryResponseDefaultType0
    | PostStorageGatewaysByStorageGatewayIdTelemetryResponseDefaultType1
):
    if response.status_code == 201:
        response_201 = cast(Any, None)
        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    def _parse_response_default(
        data: object,
    ) -> (
        PostStorageGatewaysByStorageGatewayIdTelemetryResponseDefaultType0
        | PostStorageGatewaysByStorageGatewayIdTelemetryResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = PostStorageGatewaysByStorageGatewayIdTelemetryResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = PostStorageGatewaysByStorageGatewayIdTelemetryResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostStorageGatewaysByStorageGatewayIdTelemetryResponseDefaultType0
    | PostStorageGatewaysByStorageGatewayIdTelemetryResponseDefaultType1
]:
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
) -> Response[
    Any
    | PostStorageGatewaysByStorageGatewayIdTelemetryResponseDefaultType0
    | PostStorageGatewaysByStorageGatewayIdTelemetryResponseDefaultType1
]:
    """Create telemetry

    Args:
        storage_gateway_id (str):
        body (IconikStorageGatewayTelemetrySchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostStorageGatewaysByStorageGatewayIdTelemetryResponseDefaultType0 | PostStorageGatewaysByStorageGatewayIdTelemetryResponseDefaultType1]
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
) -> (
    Any
    | PostStorageGatewaysByStorageGatewayIdTelemetryResponseDefaultType0
    | PostStorageGatewaysByStorageGatewayIdTelemetryResponseDefaultType1
    | None
):
    """Create telemetry

    Args:
        storage_gateway_id (str):
        body (IconikStorageGatewayTelemetrySchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostStorageGatewaysByStorageGatewayIdTelemetryResponseDefaultType0 | PostStorageGatewaysByStorageGatewayIdTelemetryResponseDefaultType1
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
) -> Response[
    Any
    | PostStorageGatewaysByStorageGatewayIdTelemetryResponseDefaultType0
    | PostStorageGatewaysByStorageGatewayIdTelemetryResponseDefaultType1
]:
    """Create telemetry

    Args:
        storage_gateway_id (str):
        body (IconikStorageGatewayTelemetrySchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostStorageGatewaysByStorageGatewayIdTelemetryResponseDefaultType0 | PostStorageGatewaysByStorageGatewayIdTelemetryResponseDefaultType1]
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
) -> (
    Any
    | PostStorageGatewaysByStorageGatewayIdTelemetryResponseDefaultType0
    | PostStorageGatewaysByStorageGatewayIdTelemetryResponseDefaultType1
    | None
):
    """Create telemetry

    Args:
        storage_gateway_id (str):
        body (IconikStorageGatewayTelemetrySchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostStorageGatewaysByStorageGatewayIdTelemetryResponseDefaultType0 | PostStorageGatewaysByStorageGatewayIdTelemetryResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            storage_gateway_id=storage_gateway_id,
            client=client,
            body=body,
        )
    ).parsed
