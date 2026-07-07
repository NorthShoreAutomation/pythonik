from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.iconik_storage_gateway_events_purge_schema import (
    IconikStorageGatewayEventsPurgeSchema,
)
from ...models.post_storages_by_storage_id_gateway_events_purge_response_default_type_0 import (
    PostStoragesByStorageIdGatewayEventsPurgeResponseDefaultType0,
)
from ...models.post_storages_by_storage_id_gateway_events_purge_response_default_type_1 import (
    PostStoragesByStorageIdGatewayEventsPurgeResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    storage_id: str,
    *,
    body: IconikStorageGatewayEventsPurgeSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/storages/{storage_id}/gateway/events/purge/".format(
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
    | PostStoragesByStorageIdGatewayEventsPurgeResponseDefaultType0
    | PostStoragesByStorageIdGatewayEventsPurgeResponseDefaultType1
):
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    def _parse_response_default(
        data: object,
    ) -> (
        PostStoragesByStorageIdGatewayEventsPurgeResponseDefaultType0
        | PostStoragesByStorageIdGatewayEventsPurgeResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                PostStoragesByStorageIdGatewayEventsPurgeResponseDefaultType0.from_dict(
                    data
                )
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PostStoragesByStorageIdGatewayEventsPurgeResponseDefaultType1.from_dict(
                data
            )
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostStoragesByStorageIdGatewayEventsPurgeResponseDefaultType0
    | PostStoragesByStorageIdGatewayEventsPurgeResponseDefaultType1
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
    body: IconikStorageGatewayEventsPurgeSchema,
) -> Response[
    Any
    | PostStoragesByStorageIdGatewayEventsPurgeResponseDefaultType0
    | PostStoragesByStorageIdGatewayEventsPurgeResponseDefaultType1
]:
    """Delete storage gateway events in bulk

    Args:
        storage_id (str):
        body (IconikStorageGatewayEventsPurgeSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostStoragesByStorageIdGatewayEventsPurgeResponseDefaultType0 | PostStoragesByStorageIdGatewayEventsPurgeResponseDefaultType1]
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
    body: IconikStorageGatewayEventsPurgeSchema,
) -> (
    Any
    | PostStoragesByStorageIdGatewayEventsPurgeResponseDefaultType0
    | PostStoragesByStorageIdGatewayEventsPurgeResponseDefaultType1
    | None
):
    """Delete storage gateway events in bulk

    Args:
        storage_id (str):
        body (IconikStorageGatewayEventsPurgeSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostStoragesByStorageIdGatewayEventsPurgeResponseDefaultType0 | PostStoragesByStorageIdGatewayEventsPurgeResponseDefaultType1
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
    body: IconikStorageGatewayEventsPurgeSchema,
) -> Response[
    Any
    | PostStoragesByStorageIdGatewayEventsPurgeResponseDefaultType0
    | PostStoragesByStorageIdGatewayEventsPurgeResponseDefaultType1
]:
    """Delete storage gateway events in bulk

    Args:
        storage_id (str):
        body (IconikStorageGatewayEventsPurgeSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostStoragesByStorageIdGatewayEventsPurgeResponseDefaultType0 | PostStoragesByStorageIdGatewayEventsPurgeResponseDefaultType1]
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
    body: IconikStorageGatewayEventsPurgeSchema,
) -> (
    Any
    | PostStoragesByStorageIdGatewayEventsPurgeResponseDefaultType0
    | PostStoragesByStorageIdGatewayEventsPurgeResponseDefaultType1
    | None
):
    """Delete storage gateway events in bulk

    Args:
        storage_id (str):
        body (IconikStorageGatewayEventsPurgeSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostStoragesByStorageIdGatewayEventsPurgeResponseDefaultType0 | PostStoragesByStorageIdGatewayEventsPurgeResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            storage_id=storage_id,
            client=client,
            body=body,
        )
    ).parsed
