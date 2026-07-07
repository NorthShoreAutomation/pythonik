from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_assets_by_asset_id_subtitles_by_subtitle_id_response_default_type_0 import (
    GetAssetsByAssetIdSubtitlesBySubtitleIdResponseDefaultType0,
)
from ...models.get_assets_by_asset_id_subtitles_by_subtitle_id_response_default_type_1 import (
    GetAssetsByAssetIdSubtitlesBySubtitleIdResponseDefaultType1,
)
from ...models.subtitle_schema import SubtitleSchema
from ...types import Response


def _get_kwargs(
    asset_id: str,
    subtitle_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/assets/{asset_id}/subtitles/{subtitle_id}/".format(
            asset_id=quote(str(asset_id), safe=""),
            subtitle_id=quote(str(subtitle_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetAssetsByAssetIdSubtitlesBySubtitleIdResponseDefaultType0
    | GetAssetsByAssetIdSubtitlesBySubtitleIdResponseDefaultType1
    | SubtitleSchema
):
    if response.status_code == 200:
        response_200 = SubtitleSchema.from_dict(response.json())

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
        GetAssetsByAssetIdSubtitlesBySubtitleIdResponseDefaultType0
        | GetAssetsByAssetIdSubtitlesBySubtitleIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetAssetsByAssetIdSubtitlesBySubtitleIdResponseDefaultType0.from_dict(
                    data
                )
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            GetAssetsByAssetIdSubtitlesBySubtitleIdResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetAssetsByAssetIdSubtitlesBySubtitleIdResponseDefaultType0
    | GetAssetsByAssetIdSubtitlesBySubtitleIdResponseDefaultType1
    | SubtitleSchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    asset_id: str,
    subtitle_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetAssetsByAssetIdSubtitlesBySubtitleIdResponseDefaultType0
    | GetAssetsByAssetIdSubtitlesBySubtitleIdResponseDefaultType1
    | SubtitleSchema
]:
    """Get asset's subtitle for a language


    Required roles:
     - can_read_asset_subtitles

    Args:
        asset_id (str):
        subtitle_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAssetsByAssetIdSubtitlesBySubtitleIdResponseDefaultType0 | GetAssetsByAssetIdSubtitlesBySubtitleIdResponseDefaultType1 | SubtitleSchema]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        subtitle_id=subtitle_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: str,
    subtitle_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetAssetsByAssetIdSubtitlesBySubtitleIdResponseDefaultType0
    | GetAssetsByAssetIdSubtitlesBySubtitleIdResponseDefaultType1
    | SubtitleSchema
    | None
):
    """Get asset's subtitle for a language


    Required roles:
     - can_read_asset_subtitles

    Args:
        asset_id (str):
        subtitle_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAssetsByAssetIdSubtitlesBySubtitleIdResponseDefaultType0 | GetAssetsByAssetIdSubtitlesBySubtitleIdResponseDefaultType1 | SubtitleSchema
    """

    return sync_detailed(
        asset_id=asset_id,
        subtitle_id=subtitle_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    subtitle_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetAssetsByAssetIdSubtitlesBySubtitleIdResponseDefaultType0
    | GetAssetsByAssetIdSubtitlesBySubtitleIdResponseDefaultType1
    | SubtitleSchema
]:
    """Get asset's subtitle for a language


    Required roles:
     - can_read_asset_subtitles

    Args:
        asset_id (str):
        subtitle_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAssetsByAssetIdSubtitlesBySubtitleIdResponseDefaultType0 | GetAssetsByAssetIdSubtitlesBySubtitleIdResponseDefaultType1 | SubtitleSchema]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        subtitle_id=subtitle_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    subtitle_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetAssetsByAssetIdSubtitlesBySubtitleIdResponseDefaultType0
    | GetAssetsByAssetIdSubtitlesBySubtitleIdResponseDefaultType1
    | SubtitleSchema
    | None
):
    """Get asset's subtitle for a language


    Required roles:
     - can_read_asset_subtitles

    Args:
        asset_id (str):
        subtitle_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAssetsByAssetIdSubtitlesBySubtitleIdResponseDefaultType0 | GetAssetsByAssetIdSubtitlesBySubtitleIdResponseDefaultType1 | SubtitleSchema
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            subtitle_id=subtitle_id,
            client=client,
        )
    ).parsed
