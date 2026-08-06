from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_assets_by_asset_id_segments_text_response_default import (
    GetAssetsByAssetIdSegmentsTextResponseDefault,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    asset_id: str,
    *,
    ids: str | Unset = UNSET,
    query: str | Unset = UNSET,
    transcription_id: str | Unset = UNSET,
    version_id: str | Unset = UNSET,
    segment_type: str | Unset = UNSET,
    segment_color: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["ids"] = ids

    params["query"] = query

    params["transcription_id"] = transcription_id

    params["version_id"] = version_id

    params["segment_type"] = segment_type

    params["segment_color"] = segment_color

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/assets/{asset_id}/segments/text/".format(
            asset_id=quote(str(asset_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetAssetsByAssetIdSegmentsTextResponseDefault | str:
    if response.status_code == 200:
        response_200 = response.text
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

    response_default = GetAssetsByAssetIdSegmentsTextResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetAssetsByAssetIdSegmentsTextResponseDefault | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
    ids: str | Unset = UNSET,
    query: str | Unset = UNSET,
    transcription_id: str | Unset = UNSET,
    version_id: str | Unset = UNSET,
    segment_type: str | Unset = UNSET,
    segment_color: str | Unset = UNSET,
) -> Response[Any | GetAssetsByAssetIdSegmentsTextResponseDefault | str]:
    """List of segments as text file


    Required roles:
     - can_read_segments

    Args:
        asset_id (str):
        ids (str | Unset):
        query (str | Unset):
        transcription_id (str | Unset):
        version_id (str | Unset):
        segment_type (str | Unset):
        segment_color (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAssetsByAssetIdSegmentsTextResponseDefault | str]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        ids=ids,
        query=query,
        transcription_id=transcription_id,
        version_id=version_id,
        segment_type=segment_type,
        segment_color=segment_color,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
    ids: str | Unset = UNSET,
    query: str | Unset = UNSET,
    transcription_id: str | Unset = UNSET,
    version_id: str | Unset = UNSET,
    segment_type: str | Unset = UNSET,
    segment_color: str | Unset = UNSET,
) -> Any | GetAssetsByAssetIdSegmentsTextResponseDefault | str | None:
    """List of segments as text file


    Required roles:
     - can_read_segments

    Args:
        asset_id (str):
        ids (str | Unset):
        query (str | Unset):
        transcription_id (str | Unset):
        version_id (str | Unset):
        segment_type (str | Unset):
        segment_color (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAssetsByAssetIdSegmentsTextResponseDefault | str
    """

    return sync_detailed(
        asset_id=asset_id,
        client=client,
        ids=ids,
        query=query,
        transcription_id=transcription_id,
        version_id=version_id,
        segment_type=segment_type,
        segment_color=segment_color,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
    ids: str | Unset = UNSET,
    query: str | Unset = UNSET,
    transcription_id: str | Unset = UNSET,
    version_id: str | Unset = UNSET,
    segment_type: str | Unset = UNSET,
    segment_color: str | Unset = UNSET,
) -> Response[Any | GetAssetsByAssetIdSegmentsTextResponseDefault | str]:
    """List of segments as text file


    Required roles:
     - can_read_segments

    Args:
        asset_id (str):
        ids (str | Unset):
        query (str | Unset):
        transcription_id (str | Unset):
        version_id (str | Unset):
        segment_type (str | Unset):
        segment_color (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAssetsByAssetIdSegmentsTextResponseDefault | str]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        ids=ids,
        query=query,
        transcription_id=transcription_id,
        version_id=version_id,
        segment_type=segment_type,
        segment_color=segment_color,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
    ids: str | Unset = UNSET,
    query: str | Unset = UNSET,
    transcription_id: str | Unset = UNSET,
    version_id: str | Unset = UNSET,
    segment_type: str | Unset = UNSET,
    segment_color: str | Unset = UNSET,
) -> Any | GetAssetsByAssetIdSegmentsTextResponseDefault | str | None:
    """List of segments as text file


    Required roles:
     - can_read_segments

    Args:
        asset_id (str):
        ids (str | Unset):
        query (str | Unset):
        transcription_id (str | Unset):
        version_id (str | Unset):
        segment_type (str | Unset):
        segment_color (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAssetsByAssetIdSegmentsTextResponseDefault | str
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            client=client,
            ids=ids,
            query=query,
            transcription_id=transcription_id,
            version_id=version_id,
            segment_type=segment_type,
            segment_color=segment_color,
        )
    ).parsed
