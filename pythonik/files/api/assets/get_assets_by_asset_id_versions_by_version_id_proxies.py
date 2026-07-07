from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_assets_by_asset_id_versions_by_version_id_proxies_response_default_type_0 import (
    GetAssetsByAssetIdVersionsByVersionIdProxiesResponseDefaultType0,
)
from ...models.get_assets_by_asset_id_versions_by_version_id_proxies_response_default_type_1 import (
    GetAssetsByAssetIdVersionsByVersionIdProxiesResponseDefaultType1,
)
from ...models.proxies_schema import ProxiesSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    asset_id: str,
    version_id: str,
    *,
    per_page: int | Unset = 10,
    generate_signed_url: bool | Unset = True,
    content_disposition: str | Unset = "inline",
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
        "url": "/v1/assets/{asset_id}/versions/{version_id}/proxies/".format(
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
    | GetAssetsByAssetIdVersionsByVersionIdProxiesResponseDefaultType0
    | GetAssetsByAssetIdVersionsByVersionIdProxiesResponseDefaultType1
    | ProxiesSchema
):
    if response.status_code == 200:
        response_200 = ProxiesSchema.from_dict(response.json())

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
        GetAssetsByAssetIdVersionsByVersionIdProxiesResponseDefaultType0
        | GetAssetsByAssetIdVersionsByVersionIdProxiesResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = GetAssetsByAssetIdVersionsByVersionIdProxiesResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            GetAssetsByAssetIdVersionsByVersionIdProxiesResponseDefaultType1.from_dict(
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
    | GetAssetsByAssetIdVersionsByVersionIdProxiesResponseDefaultType0
    | GetAssetsByAssetIdVersionsByVersionIdProxiesResponseDefaultType1
    | ProxiesSchema
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
    per_page: int | Unset = 10,
    generate_signed_url: bool | Unset = True,
    content_disposition: str | Unset = "inline",
    last_id: str | Unset = UNSET,
) -> Response[
    Any
    | GetAssetsByAssetIdVersionsByVersionIdProxiesResponseDefaultType0
    | GetAssetsByAssetIdVersionsByVersionIdProxiesResponseDefaultType1
    | ProxiesSchema
]:
    """Get all asset's proxies by version


    Required roles:
     - can_read_proxies

    Args:
        asset_id (str):
        version_id (str):
        per_page (int | Unset):  Default: 10.
        generate_signed_url (bool | Unset):  Default: True.
        content_disposition (str | Unset):  Default: 'inline'.
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAssetsByAssetIdVersionsByVersionIdProxiesResponseDefaultType0 | GetAssetsByAssetIdVersionsByVersionIdProxiesResponseDefaultType1 | ProxiesSchema]
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
    per_page: int | Unset = 10,
    generate_signed_url: bool | Unset = True,
    content_disposition: str | Unset = "inline",
    last_id: str | Unset = UNSET,
) -> (
    Any
    | GetAssetsByAssetIdVersionsByVersionIdProxiesResponseDefaultType0
    | GetAssetsByAssetIdVersionsByVersionIdProxiesResponseDefaultType1
    | ProxiesSchema
    | None
):
    """Get all asset's proxies by version


    Required roles:
     - can_read_proxies

    Args:
        asset_id (str):
        version_id (str):
        per_page (int | Unset):  Default: 10.
        generate_signed_url (bool | Unset):  Default: True.
        content_disposition (str | Unset):  Default: 'inline'.
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAssetsByAssetIdVersionsByVersionIdProxiesResponseDefaultType0 | GetAssetsByAssetIdVersionsByVersionIdProxiesResponseDefaultType1 | ProxiesSchema
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
    per_page: int | Unset = 10,
    generate_signed_url: bool | Unset = True,
    content_disposition: str | Unset = "inline",
    last_id: str | Unset = UNSET,
) -> Response[
    Any
    | GetAssetsByAssetIdVersionsByVersionIdProxiesResponseDefaultType0
    | GetAssetsByAssetIdVersionsByVersionIdProxiesResponseDefaultType1
    | ProxiesSchema
]:
    """Get all asset's proxies by version


    Required roles:
     - can_read_proxies

    Args:
        asset_id (str):
        version_id (str):
        per_page (int | Unset):  Default: 10.
        generate_signed_url (bool | Unset):  Default: True.
        content_disposition (str | Unset):  Default: 'inline'.
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAssetsByAssetIdVersionsByVersionIdProxiesResponseDefaultType0 | GetAssetsByAssetIdVersionsByVersionIdProxiesResponseDefaultType1 | ProxiesSchema]
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
    per_page: int | Unset = 10,
    generate_signed_url: bool | Unset = True,
    content_disposition: str | Unset = "inline",
    last_id: str | Unset = UNSET,
) -> (
    Any
    | GetAssetsByAssetIdVersionsByVersionIdProxiesResponseDefaultType0
    | GetAssetsByAssetIdVersionsByVersionIdProxiesResponseDefaultType1
    | ProxiesSchema
    | None
):
    """Get all asset's proxies by version


    Required roles:
     - can_read_proxies

    Args:
        asset_id (str):
        version_id (str):
        per_page (int | Unset):  Default: 10.
        generate_signed_url (bool | Unset):  Default: True.
        content_disposition (str | Unset):  Default: 'inline'.
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAssetsByAssetIdVersionsByVersionIdProxiesResponseDefaultType0 | GetAssetsByAssetIdVersionsByVersionIdProxiesResponseDefaultType1 | ProxiesSchema
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
