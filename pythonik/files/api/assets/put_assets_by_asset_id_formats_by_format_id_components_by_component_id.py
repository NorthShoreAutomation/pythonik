from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.component_schema import ComponentSchema
from ...models.put_assets_by_asset_id_formats_by_format_id_components_by_component_id_response_default import (
    PutAssetsByAssetIdFormatsByFormatIdComponentsByComponentIdResponseDefault,
)
from ...types import Response


def _get_kwargs(
    asset_id: str,
    format_id: str,
    component_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/assets/{asset_id}/formats/{format_id}/components/{component_id}/".format(
            asset_id=quote(str(asset_id), safe=""),
            format_id=quote(str(format_id), safe=""),
            component_id=quote(str(component_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | ComponentSchema
    | PutAssetsByAssetIdFormatsByFormatIdComponentsByComponentIdResponseDefault
):
    if response.status_code == 200:
        response_200 = ComponentSchema.from_dict(response.json())

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

    response_default = PutAssetsByAssetIdFormatsByFormatIdComponentsByComponentIdResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | ComponentSchema
    | PutAssetsByAssetIdFormatsByFormatIdComponentsByComponentIdResponseDefault
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    asset_id: str,
    format_id: str,
    component_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | ComponentSchema
    | PutAssetsByAssetIdFormatsByFormatIdComponentsByComponentIdResponseDefault
]:
    """Update a component in a format


    Required roles:
     - can_create_formats

    Args:
        asset_id (str):
        format_id (str):
        component_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ComponentSchema | PutAssetsByAssetIdFormatsByFormatIdComponentsByComponentIdResponseDefault]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        format_id=format_id,
        component_id=component_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: str,
    format_id: str,
    component_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | ComponentSchema
    | PutAssetsByAssetIdFormatsByFormatIdComponentsByComponentIdResponseDefault
    | None
):
    """Update a component in a format


    Required roles:
     - can_create_formats

    Args:
        asset_id (str):
        format_id (str):
        component_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ComponentSchema | PutAssetsByAssetIdFormatsByFormatIdComponentsByComponentIdResponseDefault
    """

    return sync_detailed(
        asset_id=asset_id,
        format_id=format_id,
        component_id=component_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    format_id: str,
    component_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | ComponentSchema
    | PutAssetsByAssetIdFormatsByFormatIdComponentsByComponentIdResponseDefault
]:
    """Update a component in a format


    Required roles:
     - can_create_formats

    Args:
        asset_id (str):
        format_id (str):
        component_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ComponentSchema | PutAssetsByAssetIdFormatsByFormatIdComponentsByComponentIdResponseDefault]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        format_id=format_id,
        component_id=component_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    format_id: str,
    component_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | ComponentSchema
    | PutAssetsByAssetIdFormatsByFormatIdComponentsByComponentIdResponseDefault
    | None
):
    """Update a component in a format


    Required roles:
     - can_create_formats

    Args:
        asset_id (str):
        format_id (str):
        component_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ComponentSchema | PutAssetsByAssetIdFormatsByFormatIdComponentsByComponentIdResponseDefault
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            format_id=format_id,
            component_id=component_id,
            client=client,
        )
    ).parsed
