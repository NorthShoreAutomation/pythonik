from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_assets_by_asset_id_versions_by_version_id_subtitles_by_language_webvtt_response_default_type_0 import (
    GetAssetsByAssetIdVersionsByVersionIdSubtitlesByLanguageWebvttResponseDefaultType0,
)
from ...models.get_assets_by_asset_id_versions_by_version_id_subtitles_by_language_webvtt_response_default_type_1 import (
    GetAssetsByAssetIdVersionsByVersionIdSubtitlesByLanguageWebvttResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    asset_id: str,
    version_id: str,
    language: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/assets/{asset_id}/versions/{version_id}/subtitles/{language}/webvtt/".format(
            asset_id=quote(str(asset_id), safe=""),
            version_id=quote(str(version_id), safe=""),
            language=quote(str(language), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetAssetsByAssetIdVersionsByVersionIdSubtitlesByLanguageWebvttResponseDefaultType0
    | GetAssetsByAssetIdVersionsByVersionIdSubtitlesByLanguageWebvttResponseDefaultType1
    | str
):
    if response.status_code == 200:
        response_200 = response.text
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
        GetAssetsByAssetIdVersionsByVersionIdSubtitlesByLanguageWebvttResponseDefaultType0
        | GetAssetsByAssetIdVersionsByVersionIdSubtitlesByLanguageWebvttResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = GetAssetsByAssetIdVersionsByVersionIdSubtitlesByLanguageWebvttResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = GetAssetsByAssetIdVersionsByVersionIdSubtitlesByLanguageWebvttResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetAssetsByAssetIdVersionsByVersionIdSubtitlesByLanguageWebvttResponseDefaultType0
    | GetAssetsByAssetIdVersionsByVersionIdSubtitlesByLanguageWebvttResponseDefaultType1
    | str
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
    language: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetAssetsByAssetIdVersionsByVersionIdSubtitlesByLanguageWebvttResponseDefaultType0
    | GetAssetsByAssetIdVersionsByVersionIdSubtitlesByLanguageWebvttResponseDefaultType1
    | str
]:
    """Get asset's subtitle file for a particular language by version


    Required roles:
     - can_read_asset_subtitles

    Args:
        asset_id (str):
        version_id (str):
        language (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAssetsByAssetIdVersionsByVersionIdSubtitlesByLanguageWebvttResponseDefaultType0 | GetAssetsByAssetIdVersionsByVersionIdSubtitlesByLanguageWebvttResponseDefaultType1 | str]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        version_id=version_id,
        language=language,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: str,
    version_id: str,
    language: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetAssetsByAssetIdVersionsByVersionIdSubtitlesByLanguageWebvttResponseDefaultType0
    | GetAssetsByAssetIdVersionsByVersionIdSubtitlesByLanguageWebvttResponseDefaultType1
    | str
    | None
):
    """Get asset's subtitle file for a particular language by version


    Required roles:
     - can_read_asset_subtitles

    Args:
        asset_id (str):
        version_id (str):
        language (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAssetsByAssetIdVersionsByVersionIdSubtitlesByLanguageWebvttResponseDefaultType0 | GetAssetsByAssetIdVersionsByVersionIdSubtitlesByLanguageWebvttResponseDefaultType1 | str
    """

    return sync_detailed(
        asset_id=asset_id,
        version_id=version_id,
        language=language,
        client=client,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    version_id: str,
    language: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetAssetsByAssetIdVersionsByVersionIdSubtitlesByLanguageWebvttResponseDefaultType0
    | GetAssetsByAssetIdVersionsByVersionIdSubtitlesByLanguageWebvttResponseDefaultType1
    | str
]:
    """Get asset's subtitle file for a particular language by version


    Required roles:
     - can_read_asset_subtitles

    Args:
        asset_id (str):
        version_id (str):
        language (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAssetsByAssetIdVersionsByVersionIdSubtitlesByLanguageWebvttResponseDefaultType0 | GetAssetsByAssetIdVersionsByVersionIdSubtitlesByLanguageWebvttResponseDefaultType1 | str]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        version_id=version_id,
        language=language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    version_id: str,
    language: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetAssetsByAssetIdVersionsByVersionIdSubtitlesByLanguageWebvttResponseDefaultType0
    | GetAssetsByAssetIdVersionsByVersionIdSubtitlesByLanguageWebvttResponseDefaultType1
    | str
    | None
):
    """Get asset's subtitle file for a particular language by version


    Required roles:
     - can_read_asset_subtitles

    Args:
        asset_id (str):
        version_id (str):
        language (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAssetsByAssetIdVersionsByVersionIdSubtitlesByLanguageWebvttResponseDefaultType0 | GetAssetsByAssetIdVersionsByVersionIdSubtitlesByLanguageWebvttResponseDefaultType1 | str
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            version_id=version_id,
            language=language,
            client=client,
        )
    ).parsed
