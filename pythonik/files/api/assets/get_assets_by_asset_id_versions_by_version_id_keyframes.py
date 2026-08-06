from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_assets_by_asset_id_versions_by_version_id_keyframes_response_default import (
    GetAssetsByAssetIdVersionsByVersionIdKeyframesResponseDefault,
)
from ...models.keyframes_schema import KeyframesSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    asset_id: str,
    version_id: str,
    *,
    per_page: int | Unset = UNSET,
    generate_signed_url: bool | Unset = UNSET,
    content_disposition: str | Unset = UNSET,
    last_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["per_page"] = per_page

    params["generate_signed_url"] = generate_signed_url

    params["content_disposition"] = content_disposition

    params["last_id"] = last_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/assets/{asset_id}/versions/{version_id}/keyframes/".format(
            asset_id=quote(str(asset_id), safe=""),
            version_id=quote(str(version_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetAssetsByAssetIdVersionsByVersionIdKeyframesResponseDefault
    | KeyframesSchema
):
    if response.status_code == 200:
        response_200 = KeyframesSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = (
        GetAssetsByAssetIdVersionsByVersionIdKeyframesResponseDefault.from_dict(
            response.json()
        )
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetAssetsByAssetIdVersionsByVersionIdKeyframesResponseDefault
    | KeyframesSchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    asset_id: str,
    version_id: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    generate_signed_url: bool | Unset = UNSET,
    content_disposition: str | Unset = UNSET,
    last_id: str | Unset = UNSET,
) -> Response[
    Any
    | GetAssetsByAssetIdVersionsByVersionIdKeyframesResponseDefault
    | KeyframesSchema
]:
    """Get all asset's keyframes by version


    Required roles:
     - can_read_assets

    Args:
        asset_id (str):
        version_id (str):
        per_page (int | Unset):
        generate_signed_url (bool | Unset):
        content_disposition (str | Unset):
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAssetsByAssetIdVersionsByVersionIdKeyframesResponseDefault | KeyframesSchema]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        version_id=version_id,
        per_page=per_page,
        generate_signed_url=generate_signed_url,
        content_disposition=content_disposition,
        last_id=last_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: str,
    version_id: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    generate_signed_url: bool | Unset = UNSET,
    content_disposition: str | Unset = UNSET,
    last_id: str | Unset = UNSET,
) -> (
    Any
    | GetAssetsByAssetIdVersionsByVersionIdKeyframesResponseDefault
    | KeyframesSchema
    | None
):
    """Get all asset's keyframes by version


    Required roles:
     - can_read_assets

    Args:
        asset_id (str):
        version_id (str):
        per_page (int | Unset):
        generate_signed_url (bool | Unset):
        content_disposition (str | Unset):
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAssetsByAssetIdVersionsByVersionIdKeyframesResponseDefault | KeyframesSchema
    """

    return sync_detailed(
        asset_id=asset_id,
        version_id=version_id,
        client=client,
        per_page=per_page,
        generate_signed_url=generate_signed_url,
        content_disposition=content_disposition,
        last_id=last_id,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    version_id: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    generate_signed_url: bool | Unset = UNSET,
    content_disposition: str | Unset = UNSET,
    last_id: str | Unset = UNSET,
) -> Response[
    Any
    | GetAssetsByAssetIdVersionsByVersionIdKeyframesResponseDefault
    | KeyframesSchema
]:
    """Get all asset's keyframes by version


    Required roles:
     - can_read_assets

    Args:
        asset_id (str):
        version_id (str):
        per_page (int | Unset):
        generate_signed_url (bool | Unset):
        content_disposition (str | Unset):
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAssetsByAssetIdVersionsByVersionIdKeyframesResponseDefault | KeyframesSchema]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        version_id=version_id,
        per_page=per_page,
        generate_signed_url=generate_signed_url,
        content_disposition=content_disposition,
        last_id=last_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    version_id: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    generate_signed_url: bool | Unset = UNSET,
    content_disposition: str | Unset = UNSET,
    last_id: str | Unset = UNSET,
) -> (
    Any
    | GetAssetsByAssetIdVersionsByVersionIdKeyframesResponseDefault
    | KeyframesSchema
    | None
):
    """Get all asset's keyframes by version


    Required roles:
     - can_read_assets

    Args:
        asset_id (str):
        version_id (str):
        per_page (int | Unset):
        generate_signed_url (bool | Unset):
        content_disposition (str | Unset):
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAssetsByAssetIdVersionsByVersionIdKeyframesResponseDefault | KeyframesSchema
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            version_id=version_id,
            client=client,
            per_page=per_page,
            generate_signed_url=generate_signed_url,
            content_disposition=content_disposition,
            last_id=last_id,
        )
    ).parsed
