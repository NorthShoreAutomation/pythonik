from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_storages_by_storage_id_gateway_events_response_default_type_0 import (
    GetStoragesByStorageIdGatewayEventsResponseDefaultType0,
)
from ...models.get_storages_by_storage_id_gateway_events_response_default_type_1 import (
    GetStoragesByStorageIdGatewayEventsResponseDefaultType1,
)
from ...models.iconik_storage_gateway_events_schema import (
    IconikStorageGatewayEventsSchema,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    storage_id: str,
    *,
    last_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["last_id"] = last_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/storages/{storage_id}/gateway/events/".format(
            storage_id=quote(str(storage_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetStoragesByStorageIdGatewayEventsResponseDefaultType0
    | GetStoragesByStorageIdGatewayEventsResponseDefaultType1
    | IconikStorageGatewayEventsSchema
):
    if response.status_code == 201:
        response_201 = IconikStorageGatewayEventsSchema.from_dict(response.json())

        return response_201

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
        GetStoragesByStorageIdGatewayEventsResponseDefaultType0
        | GetStoragesByStorageIdGatewayEventsResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetStoragesByStorageIdGatewayEventsResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            GetStoragesByStorageIdGatewayEventsResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetStoragesByStorageIdGatewayEventsResponseDefaultType0
    | GetStoragesByStorageIdGatewayEventsResponseDefaultType1
    | IconikStorageGatewayEventsSchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    last_id: str | Unset = UNSET,
) -> Response[
    Any
    | GetStoragesByStorageIdGatewayEventsResponseDefaultType0
    | GetStoragesByStorageIdGatewayEventsResponseDefaultType1
    | IconikStorageGatewayEventsSchema
]:
    """Get pending storage gateway events

    Args:
        storage_id (str):
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetStoragesByStorageIdGatewayEventsResponseDefaultType0 | GetStoragesByStorageIdGatewayEventsResponseDefaultType1 | IconikStorageGatewayEventsSchema]
    """

    kwargs = _get_kwargs(
        storage_id=storage_id,
        last_id=last_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    last_id: str | Unset = UNSET,
) -> (
    Any
    | GetStoragesByStorageIdGatewayEventsResponseDefaultType0
    | GetStoragesByStorageIdGatewayEventsResponseDefaultType1
    | IconikStorageGatewayEventsSchema
    | None
):
    """Get pending storage gateway events

    Args:
        storage_id (str):
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetStoragesByStorageIdGatewayEventsResponseDefaultType0 | GetStoragesByStorageIdGatewayEventsResponseDefaultType1 | IconikStorageGatewayEventsSchema
    """

    return sync_detailed(
        storage_id=storage_id,
        client=client,
        last_id=last_id,
    ).parsed


async def asyncio_detailed(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    last_id: str | Unset = UNSET,
) -> Response[
    Any
    | GetStoragesByStorageIdGatewayEventsResponseDefaultType0
    | GetStoragesByStorageIdGatewayEventsResponseDefaultType1
    | IconikStorageGatewayEventsSchema
]:
    """Get pending storage gateway events

    Args:
        storage_id (str):
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetStoragesByStorageIdGatewayEventsResponseDefaultType0 | GetStoragesByStorageIdGatewayEventsResponseDefaultType1 | IconikStorageGatewayEventsSchema]
    """

    kwargs = _get_kwargs(
        storage_id=storage_id,
        last_id=last_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    last_id: str | Unset = UNSET,
) -> (
    Any
    | GetStoragesByStorageIdGatewayEventsResponseDefaultType0
    | GetStoragesByStorageIdGatewayEventsResponseDefaultType1
    | IconikStorageGatewayEventsSchema
    | None
):
    """Get pending storage gateway events

    Args:
        storage_id (str):
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetStoragesByStorageIdGatewayEventsResponseDefaultType0 | GetStoragesByStorageIdGatewayEventsResponseDefaultType1 | IconikStorageGatewayEventsSchema
    """

    return (
        await asyncio_detailed(
            storage_id=storage_id,
            client=client,
            last_id=last_id,
        )
    ).parsed
