from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.edit_proxy_response_schema import EditProxyResponseSchema
from ...models.edit_proxy_schema import EditProxySchema
from ...models.post_assets_by_asset_id_files_by_file_id_edit_proxies_response_default import (
    PostAssetsByAssetIdFilesByFileIdEditProxiesResponseDefault,
)
from ...types import Response


def _get_kwargs(
    asset_id: str,
    file_id: str,
    *,
    body: EditProxySchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/assets/{asset_id}/files/{file_id}/edit_proxies/".format(
            asset_id=quote(str(asset_id), safe=""),
            file_id=quote(str(file_id), safe=""),
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
    | EditProxyResponseSchema
    | PostAssetsByAssetIdFilesByFileIdEditProxiesResponseDefault
):
    if response.status_code == 201:
        response_201 = EditProxyResponseSchema.from_dict(response.json())

        return response_201

    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = (
        PostAssetsByAssetIdFilesByFileIdEditProxiesResponseDefault.from_dict(
            response.json()
        )
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | EditProxyResponseSchema
    | PostAssetsByAssetIdFilesByFileIdEditProxiesResponseDefault
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    asset_id: str,
    file_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: EditProxySchema,
) -> Response[
    Any
    | EditProxyResponseSchema
    | PostAssetsByAssetIdFilesByFileIdEditProxiesResponseDefault
]:
    """Create format, file_set, and file for edit proxy if storage has edit proxy transcoder configured


    Required roles:
     - can_create_transcode_jobs
    - can_write_files

    Args:
        asset_id (str):
        file_id (str):
        body (EditProxySchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EditProxyResponseSchema | PostAssetsByAssetIdFilesByFileIdEditProxiesResponseDefault]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        file_id=file_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: str,
    file_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: EditProxySchema,
) -> (
    Any
    | EditProxyResponseSchema
    | PostAssetsByAssetIdFilesByFileIdEditProxiesResponseDefault
    | None
):
    """Create format, file_set, and file for edit proxy if storage has edit proxy transcoder configured


    Required roles:
     - can_create_transcode_jobs
    - can_write_files

    Args:
        asset_id (str):
        file_id (str):
        body (EditProxySchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EditProxyResponseSchema | PostAssetsByAssetIdFilesByFileIdEditProxiesResponseDefault
    """

    return sync_detailed(
        asset_id=asset_id,
        file_id=file_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    file_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: EditProxySchema,
) -> Response[
    Any
    | EditProxyResponseSchema
    | PostAssetsByAssetIdFilesByFileIdEditProxiesResponseDefault
]:
    """Create format, file_set, and file for edit proxy if storage has edit proxy transcoder configured


    Required roles:
     - can_create_transcode_jobs
    - can_write_files

    Args:
        asset_id (str):
        file_id (str):
        body (EditProxySchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EditProxyResponseSchema | PostAssetsByAssetIdFilesByFileIdEditProxiesResponseDefault]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        file_id=file_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    file_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: EditProxySchema,
) -> (
    Any
    | EditProxyResponseSchema
    | PostAssetsByAssetIdFilesByFileIdEditProxiesResponseDefault
    | None
):
    """Create format, file_set, and file for edit proxy if storage has edit proxy transcoder configured


    Required roles:
     - can_create_transcode_jobs
    - can_write_files

    Args:
        asset_id (str):
        file_id (str):
        body (EditProxySchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EditProxyResponseSchema | PostAssetsByAssetIdFilesByFileIdEditProxiesResponseDefault
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            file_id=file_id,
            client=client,
            body=body,
        )
    ).parsed
