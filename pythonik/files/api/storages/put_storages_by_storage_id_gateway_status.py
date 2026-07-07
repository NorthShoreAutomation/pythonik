from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.gateway_status_schema import GatewayStatusSchema
from ...models.put_storages_by_storage_id_gateway_status_response_default_type_0 import (
    PutStoragesByStorageIdGatewayStatusResponseDefaultType0,
)
from ...models.put_storages_by_storage_id_gateway_status_response_default_type_1 import (
    PutStoragesByStorageIdGatewayStatusResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    storage_id: str,
    *,
    body: GatewayStatusSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/storages/{storage_id}/gateway/status/".format(
            storage_id=quote(str(storage_id), safe=""),
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
    | PutStoragesByStorageIdGatewayStatusResponseDefaultType0
    | PutStoragesByStorageIdGatewayStatusResponseDefaultType1
):
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

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
        PutStoragesByStorageIdGatewayStatusResponseDefaultType0
        | PutStoragesByStorageIdGatewayStatusResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                PutStoragesByStorageIdGatewayStatusResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PutStoragesByStorageIdGatewayStatusResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PutStoragesByStorageIdGatewayStatusResponseDefaultType0
    | PutStoragesByStorageIdGatewayStatusResponseDefaultType1
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
    body: GatewayStatusSchema,
) -> Response[
    Any
    | PutStoragesByStorageIdGatewayStatusResponseDefaultType0
    | PutStoragesByStorageIdGatewayStatusResponseDefaultType1
]:
    """Update storage gateway status


    Required roles:
     - is_storage_worker

    Args:
        storage_id (str):
        body (GatewayStatusSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutStoragesByStorageIdGatewayStatusResponseDefaultType0 | PutStoragesByStorageIdGatewayStatusResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        storage_id=storage_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: GatewayStatusSchema,
) -> (
    Any
    | PutStoragesByStorageIdGatewayStatusResponseDefaultType0
    | PutStoragesByStorageIdGatewayStatusResponseDefaultType1
    | None
):
    """Update storage gateway status


    Required roles:
     - is_storage_worker

    Args:
        storage_id (str):
        body (GatewayStatusSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutStoragesByStorageIdGatewayStatusResponseDefaultType0 | PutStoragesByStorageIdGatewayStatusResponseDefaultType1
    """

    return sync_detailed(
        storage_id=storage_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: GatewayStatusSchema,
) -> Response[
    Any
    | PutStoragesByStorageIdGatewayStatusResponseDefaultType0
    | PutStoragesByStorageIdGatewayStatusResponseDefaultType1
]:
    """Update storage gateway status


    Required roles:
     - is_storage_worker

    Args:
        storage_id (str):
        body (GatewayStatusSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutStoragesByStorageIdGatewayStatusResponseDefaultType0 | PutStoragesByStorageIdGatewayStatusResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        storage_id=storage_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: GatewayStatusSchema,
) -> (
    Any
    | PutStoragesByStorageIdGatewayStatusResponseDefaultType0
    | PutStoragesByStorageIdGatewayStatusResponseDefaultType1
    | None
):
    """Update storage gateway status


    Required roles:
     - is_storage_worker

    Args:
        storage_id (str):
        body (GatewayStatusSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutStoragesByStorageIdGatewayStatusResponseDefaultType0 | PutStoragesByStorageIdGatewayStatusResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            storage_id=storage_id,
            client=client,
            body=body,
        )
    ).parsed
