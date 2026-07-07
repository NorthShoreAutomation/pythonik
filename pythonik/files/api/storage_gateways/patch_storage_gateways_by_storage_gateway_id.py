from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.iconik_storage_gateway_schema import IconikStorageGatewaySchema
from ...models.patch_storage_gateways_by_storage_gateway_id_response_default_type_0 import (
    PatchStorageGatewaysByStorageGatewayIdResponseDefaultType0,
)
from ...models.patch_storage_gateways_by_storage_gateway_id_response_default_type_1 import (
    PatchStorageGatewaysByStorageGatewayIdResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    storage_gateway_id: str,
    *,
    body: IconikStorageGatewaySchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/storage_gateways/{storage_gateway_id}/".format(
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
    | IconikStorageGatewaySchema
    | PatchStorageGatewaysByStorageGatewayIdResponseDefaultType0
    | PatchStorageGatewaysByStorageGatewayIdResponseDefaultType1
):
    if response.status_code == 200:
        response_200 = IconikStorageGatewaySchema.from_dict(response.json())

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
        PatchStorageGatewaysByStorageGatewayIdResponseDefaultType0
        | PatchStorageGatewaysByStorageGatewayIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                PatchStorageGatewaysByStorageGatewayIdResponseDefaultType0.from_dict(
                    data
                )
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PatchStorageGatewaysByStorageGatewayIdResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | IconikStorageGatewaySchema
    | PatchStorageGatewaysByStorageGatewayIdResponseDefaultType0
    | PatchStorageGatewaysByStorageGatewayIdResponseDefaultType1
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
    body: IconikStorageGatewaySchema,
) -> Response[
    Any
    | IconikStorageGatewaySchema
    | PatchStorageGatewaysByStorageGatewayIdResponseDefaultType0
    | PatchStorageGatewaysByStorageGatewayIdResponseDefaultType1
]:
    """Update a storage gateway

    Args:
        storage_gateway_id (str):
        body (IconikStorageGatewaySchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | IconikStorageGatewaySchema | PatchStorageGatewaysByStorageGatewayIdResponseDefaultType0 | PatchStorageGatewaysByStorageGatewayIdResponseDefaultType1]
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
    body: IconikStorageGatewaySchema,
) -> (
    Any
    | IconikStorageGatewaySchema
    | PatchStorageGatewaysByStorageGatewayIdResponseDefaultType0
    | PatchStorageGatewaysByStorageGatewayIdResponseDefaultType1
    | None
):
    """Update a storage gateway

    Args:
        storage_gateway_id (str):
        body (IconikStorageGatewaySchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | IconikStorageGatewaySchema | PatchStorageGatewaysByStorageGatewayIdResponseDefaultType0 | PatchStorageGatewaysByStorageGatewayIdResponseDefaultType1
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
    body: IconikStorageGatewaySchema,
) -> Response[
    Any
    | IconikStorageGatewaySchema
    | PatchStorageGatewaysByStorageGatewayIdResponseDefaultType0
    | PatchStorageGatewaysByStorageGatewayIdResponseDefaultType1
]:
    """Update a storage gateway

    Args:
        storage_gateway_id (str):
        body (IconikStorageGatewaySchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | IconikStorageGatewaySchema | PatchStorageGatewaysByStorageGatewayIdResponseDefaultType0 | PatchStorageGatewaysByStorageGatewayIdResponseDefaultType1]
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
    body: IconikStorageGatewaySchema,
) -> (
    Any
    | IconikStorageGatewaySchema
    | PatchStorageGatewaysByStorageGatewayIdResponseDefaultType0
    | PatchStorageGatewaysByStorageGatewayIdResponseDefaultType1
    | None
):
    """Update a storage gateway

    Args:
        storage_gateway_id (str):
        body (IconikStorageGatewaySchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | IconikStorageGatewaySchema | PatchStorageGatewaysByStorageGatewayIdResponseDefaultType0 | PatchStorageGatewaysByStorageGatewayIdResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            storage_gateway_id=storage_gateway_id,
            client=client,
            body=body,
        )
    ).parsed
