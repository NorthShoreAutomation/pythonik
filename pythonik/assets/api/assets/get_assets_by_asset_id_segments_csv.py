from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_assets_by_asset_id_segments_csv_response_default_type_0 import (
    GetAssetsByAssetIdSegmentsCsvResponseDefaultType0,
)
from ...models.get_assets_by_asset_id_segments_csv_response_default_type_1 import (
    GetAssetsByAssetIdSegmentsCsvResponseDefaultType1,
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
        "url": "/v1/assets/{asset_id}/segments/csv/".format(
            asset_id=quote(str(asset_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetAssetsByAssetIdSegmentsCsvResponseDefaultType0
    | GetAssetsByAssetIdSegmentsCsvResponseDefaultType1
    | str
):
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

    def _parse_response_default(
        data: object,
    ) -> (
        GetAssetsByAssetIdSegmentsCsvResponseDefaultType0
        | GetAssetsByAssetIdSegmentsCsvResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetAssetsByAssetIdSegmentsCsvResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            GetAssetsByAssetIdSegmentsCsvResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetAssetsByAssetIdSegmentsCsvResponseDefaultType0
    | GetAssetsByAssetIdSegmentsCsvResponseDefaultType1
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
    *,
    client: AuthenticatedClient | Client,
    ids: str | Unset = UNSET,
    query: str | Unset = UNSET,
    transcription_id: str | Unset = UNSET,
    version_id: str | Unset = UNSET,
    segment_type: str | Unset = UNSET,
    segment_color: str | Unset = UNSET,
) -> Response[
    Any
    | GetAssetsByAssetIdSegmentsCsvResponseDefaultType0
    | GetAssetsByAssetIdSegmentsCsvResponseDefaultType1
    | str
]:
    """List of segments as CSV file


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
        Response[Any | GetAssetsByAssetIdSegmentsCsvResponseDefaultType0 | GetAssetsByAssetIdSegmentsCsvResponseDefaultType1 | str]
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
) -> (
    Any
    | GetAssetsByAssetIdSegmentsCsvResponseDefaultType0
    | GetAssetsByAssetIdSegmentsCsvResponseDefaultType1
    | str
    | None
):
    """List of segments as CSV file


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
        Any | GetAssetsByAssetIdSegmentsCsvResponseDefaultType0 | GetAssetsByAssetIdSegmentsCsvResponseDefaultType1 | str
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
) -> Response[
    Any
    | GetAssetsByAssetIdSegmentsCsvResponseDefaultType0
    | GetAssetsByAssetIdSegmentsCsvResponseDefaultType1
    | str
]:
    """List of segments as CSV file


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
        Response[Any | GetAssetsByAssetIdSegmentsCsvResponseDefaultType0 | GetAssetsByAssetIdSegmentsCsvResponseDefaultType1 | str]
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
) -> (
    Any
    | GetAssetsByAssetIdSegmentsCsvResponseDefaultType0
    | GetAssetsByAssetIdSegmentsCsvResponseDefaultType1
    | str
    | None
):
    """List of segments as CSV file


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
        Any | GetAssetsByAssetIdSegmentsCsvResponseDefaultType0 | GetAssetsByAssetIdSegmentsCsvResponseDefaultType1 | str
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
