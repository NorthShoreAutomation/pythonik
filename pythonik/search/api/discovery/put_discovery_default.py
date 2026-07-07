from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.discovery_view_settings_schema import DiscoveryViewSettingsSchema
from ...models.put_discovery_default_response_default_type_0 import (
    PutDiscoveryDefaultResponseDefaultType0,
)
from ...models.put_discovery_default_response_default_type_1 import (
    PutDiscoveryDefaultResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    *,
    body: DiscoveryViewSettingsSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/discovery/default/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | DiscoveryViewSettingsSchema
    | PutDiscoveryDefaultResponseDefaultType0
    | PutDiscoveryDefaultResponseDefaultType1
):
    if response.status_code == 200:
        response_200 = DiscoveryViewSettingsSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    def _parse_response_default(
        data: object,
    ) -> (
        PutDiscoveryDefaultResponseDefaultType0
        | PutDiscoveryDefaultResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = PutDiscoveryDefaultResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = PutDiscoveryDefaultResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | DiscoveryViewSettingsSchema
    | PutDiscoveryDefaultResponseDefaultType0
    | PutDiscoveryDefaultResponseDefaultType1
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
    body: DiscoveryViewSettingsSchema,
) -> Response[
    Any
    | DiscoveryViewSettingsSchema
    | PutDiscoveryDefaultResponseDefaultType0
    | PutDiscoveryDefaultResponseDefaultType1
]:
    """Update default discovery view


    Required roles:
     - can_write_discovery_entities

    Args:
        body (DiscoveryViewSettingsSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DiscoveryViewSettingsSchema | PutDiscoveryDefaultResponseDefaultType0 | PutDiscoveryDefaultResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: DiscoveryViewSettingsSchema,
) -> (
    Any
    | DiscoveryViewSettingsSchema
    | PutDiscoveryDefaultResponseDefaultType0
    | PutDiscoveryDefaultResponseDefaultType1
    | None
):
    """Update default discovery view


    Required roles:
     - can_write_discovery_entities

    Args:
        body (DiscoveryViewSettingsSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DiscoveryViewSettingsSchema | PutDiscoveryDefaultResponseDefaultType0 | PutDiscoveryDefaultResponseDefaultType1
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DiscoveryViewSettingsSchema,
) -> Response[
    Any
    | DiscoveryViewSettingsSchema
    | PutDiscoveryDefaultResponseDefaultType0
    | PutDiscoveryDefaultResponseDefaultType1
]:
    """Update default discovery view


    Required roles:
     - can_write_discovery_entities

    Args:
        body (DiscoveryViewSettingsSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DiscoveryViewSettingsSchema | PutDiscoveryDefaultResponseDefaultType0 | PutDiscoveryDefaultResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: DiscoveryViewSettingsSchema,
) -> (
    Any
    | DiscoveryViewSettingsSchema
    | PutDiscoveryDefaultResponseDefaultType0
    | PutDiscoveryDefaultResponseDefaultType1
    | None
):
    """Update default discovery view


    Required roles:
     - can_write_discovery_entities

    Args:
        body (DiscoveryViewSettingsSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DiscoveryViewSettingsSchema | PutDiscoveryDefaultResponseDefaultType0 | PutDiscoveryDefaultResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
