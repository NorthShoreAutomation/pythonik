from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_storage_gateways_telemetry_response_default_type_0 import (
    GetStorageGatewaysTelemetryResponseDefaultType0,
)
from ...models.get_storage_gateways_telemetry_response_default_type_1 import (
    GetStorageGatewaysTelemetryResponseDefaultType1,
)
from ...models.iconik_storage_gateways_telemetry_schema import (
    IconikStorageGatewaysTelemetrySchema,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    per_page: int | Unset = 10,
    last_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["per_page"] = per_page

    params["last_id"] = last_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/storage_gateways/telemetry/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetStorageGatewaysTelemetryResponseDefaultType0
    | GetStorageGatewaysTelemetryResponseDefaultType1
    | IconikStorageGatewaysTelemetrySchema
):
    if response.status_code == 200:
        response_200 = IconikStorageGatewaysTelemetrySchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    def _parse_response_default(
        data: object,
    ) -> (
        GetStorageGatewaysTelemetryResponseDefaultType0
        | GetStorageGatewaysTelemetryResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetStorageGatewaysTelemetryResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            GetStorageGatewaysTelemetryResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetStorageGatewaysTelemetryResponseDefaultType0
    | GetStorageGatewaysTelemetryResponseDefaultType1
    | IconikStorageGatewaysTelemetrySchema
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
    per_page: int | Unset = 10,
    last_id: str | Unset = UNSET,
) -> Response[
    Any
    | GetStorageGatewaysTelemetryResponseDefaultType0
    | GetStorageGatewaysTelemetryResponseDefaultType1
    | IconikStorageGatewaysTelemetrySchema
]:
    """Get all telemetry records with optional filtering


    Required roles:
     - can_read_storages

    Args:
        per_page (int | Unset):  Default: 10.
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetStorageGatewaysTelemetryResponseDefaultType0 | GetStorageGatewaysTelemetryResponseDefaultType1 | IconikStorageGatewaysTelemetrySchema]
    """

    kwargs = _get_kwargs(
        per_page=per_page,
        last_id=last_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = 10,
    last_id: str | Unset = UNSET,
) -> (
    Any
    | GetStorageGatewaysTelemetryResponseDefaultType0
    | GetStorageGatewaysTelemetryResponseDefaultType1
    | IconikStorageGatewaysTelemetrySchema
    | None
):
    """Get all telemetry records with optional filtering


    Required roles:
     - can_read_storages

    Args:
        per_page (int | Unset):  Default: 10.
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetStorageGatewaysTelemetryResponseDefaultType0 | GetStorageGatewaysTelemetryResponseDefaultType1 | IconikStorageGatewaysTelemetrySchema
    """

    return sync_detailed(
        client=client,
        per_page=per_page,
        last_id=last_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = 10,
    last_id: str | Unset = UNSET,
) -> Response[
    Any
    | GetStorageGatewaysTelemetryResponseDefaultType0
    | GetStorageGatewaysTelemetryResponseDefaultType1
    | IconikStorageGatewaysTelemetrySchema
]:
    """Get all telemetry records with optional filtering


    Required roles:
     - can_read_storages

    Args:
        per_page (int | Unset):  Default: 10.
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetStorageGatewaysTelemetryResponseDefaultType0 | GetStorageGatewaysTelemetryResponseDefaultType1 | IconikStorageGatewaysTelemetrySchema]
    """

    kwargs = _get_kwargs(
        per_page=per_page,
        last_id=last_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = 10,
    last_id: str | Unset = UNSET,
) -> (
    Any
    | GetStorageGatewaysTelemetryResponseDefaultType0
    | GetStorageGatewaysTelemetryResponseDefaultType1
    | IconikStorageGatewaysTelemetrySchema
    | None
):
    """Get all telemetry records with optional filtering


    Required roles:
     - can_read_storages

    Args:
        per_page (int | Unset):  Default: 10.
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetStorageGatewaysTelemetryResponseDefaultType0 | GetStorageGatewaysTelemetryResponseDefaultType1 | IconikStorageGatewaysTelemetrySchema
    """

    return (
        await asyncio_detailed(
            client=client,
            per_page=per_page,
            last_id=last_id,
        )
    ).parsed
