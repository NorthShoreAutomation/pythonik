from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_assets_by_asset_id_subtitles_by_language_cc_response_default import (
    GetAssetsByAssetIdSubtitlesByLanguageCcResponseDefault,
)
from ...models.subtitle_schema import SubtitleSchema
from ...types import Response


def _get_kwargs(
    asset_id: str,
    language: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/assets/{asset_id}/subtitles/{language}/cc/".format(
            asset_id=quote(str(asset_id), safe=""),
            language=quote(str(language), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetAssetsByAssetIdSubtitlesByLanguageCcResponseDefault | SubtitleSchema:
    if response.status_code == 200:
        response_200 = SubtitleSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = GetAssetsByAssetIdSubtitlesByLanguageCcResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | GetAssetsByAssetIdSubtitlesByLanguageCcResponseDefault | SubtitleSchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    asset_id: str,
    language: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any | GetAssetsByAssetIdSubtitlesByLanguageCcResponseDefault | SubtitleSchema
]:
    """Get asset's closed captions subtitle for a particular language


    Required roles:
     - can_read_asset_subtitles

    Args:
        asset_id (str):
        language (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAssetsByAssetIdSubtitlesByLanguageCcResponseDefault | SubtitleSchema]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        language=language,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: str,
    language: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any | GetAssetsByAssetIdSubtitlesByLanguageCcResponseDefault | SubtitleSchema | None
):
    """Get asset's closed captions subtitle for a particular language


    Required roles:
     - can_read_asset_subtitles

    Args:
        asset_id (str):
        language (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAssetsByAssetIdSubtitlesByLanguageCcResponseDefault | SubtitleSchema
    """

    return sync_detailed(
        asset_id=asset_id,
        language=language,
        client=client,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    language: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any | GetAssetsByAssetIdSubtitlesByLanguageCcResponseDefault | SubtitleSchema
]:
    """Get asset's closed captions subtitle for a particular language


    Required roles:
     - can_read_asset_subtitles

    Args:
        asset_id (str):
        language (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAssetsByAssetIdSubtitlesByLanguageCcResponseDefault | SubtitleSchema]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        language=language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    language: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any | GetAssetsByAssetIdSubtitlesByLanguageCcResponseDefault | SubtitleSchema | None
):
    """Get asset's closed captions subtitle for a particular language


    Required roles:
     - can_read_asset_subtitles

    Args:
        asset_id (str):
        language (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAssetsByAssetIdSubtitlesByLanguageCcResponseDefault | SubtitleSchema
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            language=language,
            client=client,
        )
    ).parsed
