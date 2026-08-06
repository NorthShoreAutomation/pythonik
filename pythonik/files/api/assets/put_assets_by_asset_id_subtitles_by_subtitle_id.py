from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.put_assets_by_asset_id_subtitles_by_subtitle_id_response_default import (
    PutAssetsByAssetIdSubtitlesBySubtitleIdResponseDefault,
)
from ...models.subtitle_schema import SubtitleSchema
from ...types import Response


def _get_kwargs(
    asset_id: str,
    subtitle_id: str,
    *,
    body: SubtitleSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/assets/{asset_id}/subtitles/{subtitle_id}/".format(
            asset_id=quote(str(asset_id), safe=""),
            subtitle_id=quote(str(subtitle_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PutAssetsByAssetIdSubtitlesBySubtitleIdResponseDefault | SubtitleSchema:
    if response.status_code == 200:
        response_200 = SubtitleSchema.from_dict(response.json())

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

    response_default = PutAssetsByAssetIdSubtitlesBySubtitleIdResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | PutAssetsByAssetIdSubtitlesBySubtitleIdResponseDefault | SubtitleSchema
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
    body: SubtitleSchema,
) -> Response[
    Any | PutAssetsByAssetIdSubtitlesBySubtitleIdResponseDefault | SubtitleSchema
]:
    """Update subtitle information


    Required roles:
     - can_write_asset_subtitles

    Args:
        asset_id (str):
        subtitle_id (str):
        body (SubtitleSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutAssetsByAssetIdSubtitlesBySubtitleIdResponseDefault | SubtitleSchema]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        subtitle_id=subtitle_id,
        body=body,
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
    body: SubtitleSchema,
) -> (
    Any | PutAssetsByAssetIdSubtitlesBySubtitleIdResponseDefault | SubtitleSchema | None
):
    """Update subtitle information


    Required roles:
     - can_write_asset_subtitles

    Args:
        asset_id (str):
        subtitle_id (str):
        body (SubtitleSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutAssetsByAssetIdSubtitlesBySubtitleIdResponseDefault | SubtitleSchema
    """

    return sync_detailed(
        asset_id=asset_id,
        subtitle_id=subtitle_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    subtitle_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SubtitleSchema,
) -> Response[
    Any | PutAssetsByAssetIdSubtitlesBySubtitleIdResponseDefault | SubtitleSchema
]:
    """Update subtitle information


    Required roles:
     - can_write_asset_subtitles

    Args:
        asset_id (str):
        subtitle_id (str):
        body (SubtitleSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutAssetsByAssetIdSubtitlesBySubtitleIdResponseDefault | SubtitleSchema]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        subtitle_id=subtitle_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    subtitle_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SubtitleSchema,
) -> (
    Any | PutAssetsByAssetIdSubtitlesBySubtitleIdResponseDefault | SubtitleSchema | None
):
    """Update subtitle information


    Required roles:
     - can_write_asset_subtitles

    Args:
        asset_id (str):
        subtitle_id (str):
        body (SubtitleSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutAssetsByAssetIdSubtitlesBySubtitleIdResponseDefault | SubtitleSchema
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            subtitle_id=subtitle_id,
            client=client,
            body=body,
        )
    ).parsed
