from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_assets_by_asset_id_versions_by_version_id_subtitles_response_default_type_0 import (
    GetAssetsByAssetIdVersionsByVersionIdSubtitlesResponseDefaultType0,
)
from ...models.get_assets_by_asset_id_versions_by_version_id_subtitles_response_default_type_1 import (
    GetAssetsByAssetIdVersionsByVersionIdSubtitlesResponseDefaultType1,
)
from ...models.subtitles_schema import SubtitlesSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    asset_id: str,
    version_id: str,
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
        "url": "/v1/assets/{asset_id}/versions/{version_id}/subtitles/".format(
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
    | GetAssetsByAssetIdVersionsByVersionIdSubtitlesResponseDefaultType0
    | GetAssetsByAssetIdVersionsByVersionIdSubtitlesResponseDefaultType1
    | SubtitlesSchema
):
    if response.status_code == 200:
        response_200 = SubtitlesSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    def _parse_response_default(
        data: object,
    ) -> (
        GetAssetsByAssetIdVersionsByVersionIdSubtitlesResponseDefaultType0
        | GetAssetsByAssetIdVersionsByVersionIdSubtitlesResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = GetAssetsByAssetIdVersionsByVersionIdSubtitlesResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = GetAssetsByAssetIdVersionsByVersionIdSubtitlesResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetAssetsByAssetIdVersionsByVersionIdSubtitlesResponseDefaultType0
    | GetAssetsByAssetIdVersionsByVersionIdSubtitlesResponseDefaultType1
    | SubtitlesSchema
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
    last_id: str | Unset = UNSET,
) -> Response[
    Any
    | GetAssetsByAssetIdVersionsByVersionIdSubtitlesResponseDefaultType0
    | GetAssetsByAssetIdVersionsByVersionIdSubtitlesResponseDefaultType1
    | SubtitlesSchema
]:
    """Get all asset's subtitles by version


    Required roles:
     - can_read_asset_subtitles

    Args:
        asset_id (str):
        version_id (str):
        per_page (int | Unset):  Default: 10.
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAssetsByAssetIdVersionsByVersionIdSubtitlesResponseDefaultType0 | GetAssetsByAssetIdVersionsByVersionIdSubtitlesResponseDefaultType1 | SubtitlesSchema]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        version_id=version_id,
        per_page=per_page,
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
    last_id: str | Unset = UNSET,
) -> (
    Any
    | GetAssetsByAssetIdVersionsByVersionIdSubtitlesResponseDefaultType0
    | GetAssetsByAssetIdVersionsByVersionIdSubtitlesResponseDefaultType1
    | SubtitlesSchema
    | None
):
    """Get all asset's subtitles by version


    Required roles:
     - can_read_asset_subtitles

    Args:
        asset_id (str):
        version_id (str):
        per_page (int | Unset):  Default: 10.
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAssetsByAssetIdVersionsByVersionIdSubtitlesResponseDefaultType0 | GetAssetsByAssetIdVersionsByVersionIdSubtitlesResponseDefaultType1 | SubtitlesSchema
    """

    return sync_detailed(
        asset_id=asset_id,
        version_id=version_id,
        client=client,
        per_page=per_page,
        last_id=last_id,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    version_id: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = 10,
    last_id: str | Unset = UNSET,
) -> Response[
    Any
    | GetAssetsByAssetIdVersionsByVersionIdSubtitlesResponseDefaultType0
    | GetAssetsByAssetIdVersionsByVersionIdSubtitlesResponseDefaultType1
    | SubtitlesSchema
]:
    """Get all asset's subtitles by version


    Required roles:
     - can_read_asset_subtitles

    Args:
        asset_id (str):
        version_id (str):
        per_page (int | Unset):  Default: 10.
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAssetsByAssetIdVersionsByVersionIdSubtitlesResponseDefaultType0 | GetAssetsByAssetIdVersionsByVersionIdSubtitlesResponseDefaultType1 | SubtitlesSchema]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        version_id=version_id,
        per_page=per_page,
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
    last_id: str | Unset = UNSET,
) -> (
    Any
    | GetAssetsByAssetIdVersionsByVersionIdSubtitlesResponseDefaultType0
    | GetAssetsByAssetIdVersionsByVersionIdSubtitlesResponseDefaultType1
    | SubtitlesSchema
    | None
):
    """Get all asset's subtitles by version


    Required roles:
     - can_read_asset_subtitles

    Args:
        asset_id (str):
        version_id (str):
        per_page (int | Unset):  Default: 10.
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAssetsByAssetIdVersionsByVersionIdSubtitlesResponseDefaultType0 | GetAssetsByAssetIdVersionsByVersionIdSubtitlesResponseDefaultType1 | SubtitlesSchema
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            version_id=version_id,
            client=client,
            per_page=per_page,
            last_id=last_id,
        )
    ).parsed
