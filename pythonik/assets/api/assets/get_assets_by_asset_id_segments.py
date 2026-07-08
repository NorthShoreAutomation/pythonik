from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_assets_by_asset_id_segments_response_default import (
    GetAssetsByAssetIdSegmentsResponseDefault,
)
from ...models.segments_schema import SegmentsSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    asset_id: str,
    *,
    sort: str | Unset = UNSET,
    ids: str | Unset = UNSET,
    query: str | Unset = UNSET,
    includes: str | Unset = UNSET,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
    scroll: bool | Unset = UNSET,
    scroll_id: str | Unset = UNSET,
    transcription_id: str | Unset = UNSET,
    version_id: str | Unset = UNSET,
    segment_type: str | Unset = UNSET,
    segment_color: str | Unset = UNSET,
    time_start_milliseconds: int | Unset = UNSET,
    time_end_milliseconds: int | Unset = UNSET,
    time_start_milliseconds_gte: int | Unset = UNSET,
    time_end_milliseconds_lte: int | Unset = UNSET,
    status: str | Unset = UNSET,
    person_id: str | Unset = UNSET,
    share_id: str | Unset = UNSET,
    project_id: str | Unset = UNSET,
    include_users: bool | Unset = UNSET,
    include_all_versions: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["sort"] = sort

    params["ids"] = ids

    params["query"] = query

    params["includes"] = includes

    params["per_page"] = per_page

    params["page"] = page

    params["scroll"] = scroll

    params["scroll_id"] = scroll_id

    params["transcription_id"] = transcription_id

    params["version_id"] = version_id

    params["segment_type"] = segment_type

    params["segment_color"] = segment_color

    params["time_start_milliseconds"] = time_start_milliseconds

    params["time_end_milliseconds"] = time_end_milliseconds

    params["time_start_milliseconds__gte"] = time_start_milliseconds_gte

    params["time_end_milliseconds__lte"] = time_end_milliseconds_lte

    params["status"] = status

    params["person_id"] = person_id

    params["share_id"] = share_id

    params["project_id"] = project_id

    params["include_users"] = include_users

    params["include_all_versions"] = include_all_versions

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/assets/{asset_id}/segments/".format(
            asset_id=quote(str(asset_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetAssetsByAssetIdSegmentsResponseDefault | SegmentsSchema:
    if response.status_code == 200:
        response_200 = SegmentsSchema.from_dict(response.json())

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

    response_default = GetAssetsByAssetIdSegmentsResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetAssetsByAssetIdSegmentsResponseDefault | SegmentsSchema]:
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
    sort: str | Unset = UNSET,
    ids: str | Unset = UNSET,
    query: str | Unset = UNSET,
    includes: str | Unset = UNSET,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
    scroll: bool | Unset = UNSET,
    scroll_id: str | Unset = UNSET,
    transcription_id: str | Unset = UNSET,
    version_id: str | Unset = UNSET,
    segment_type: str | Unset = UNSET,
    segment_color: str | Unset = UNSET,
    time_start_milliseconds: int | Unset = UNSET,
    time_end_milliseconds: int | Unset = UNSET,
    time_start_milliseconds_gte: int | Unset = UNSET,
    time_end_milliseconds_lte: int | Unset = UNSET,
    status: str | Unset = UNSET,
    person_id: str | Unset = UNSET,
    share_id: str | Unset = UNSET,
    project_id: str | Unset = UNSET,
    include_users: bool | Unset = UNSET,
    include_all_versions: bool | Unset = UNSET,
) -> Response[Any | GetAssetsByAssetIdSegmentsResponseDefault | SegmentsSchema]:
    """List of segments


    Required roles:
     - can_read_segments

    Args:
        asset_id (str):
        sort (str | Unset):
        ids (str | Unset):
        query (str | Unset):
        includes (str | Unset):
        per_page (int | Unset):
        page (int | Unset):
        scroll (bool | Unset):
        scroll_id (str | Unset):
        transcription_id (str | Unset):
        version_id (str | Unset):
        segment_type (str | Unset):
        segment_color (str | Unset):
        time_start_milliseconds (int | Unset):
        time_end_milliseconds (int | Unset):
        time_start_milliseconds_gte (int | Unset):
        time_end_milliseconds_lte (int | Unset):
        status (str | Unset):
        person_id (str | Unset):
        share_id (str | Unset):
        project_id (str | Unset):
        include_users (bool | Unset):
        include_all_versions (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAssetsByAssetIdSegmentsResponseDefault | SegmentsSchema]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        sort=sort,
        ids=ids,
        query=query,
        includes=includes,
        per_page=per_page,
        page=page,
        scroll=scroll,
        scroll_id=scroll_id,
        transcription_id=transcription_id,
        version_id=version_id,
        segment_type=segment_type,
        segment_color=segment_color,
        time_start_milliseconds=time_start_milliseconds,
        time_end_milliseconds=time_end_milliseconds,
        time_start_milliseconds_gte=time_start_milliseconds_gte,
        time_end_milliseconds_lte=time_end_milliseconds_lte,
        status=status,
        person_id=person_id,
        share_id=share_id,
        project_id=project_id,
        include_users=include_users,
        include_all_versions=include_all_versions,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
    sort: str | Unset = UNSET,
    ids: str | Unset = UNSET,
    query: str | Unset = UNSET,
    includes: str | Unset = UNSET,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
    scroll: bool | Unset = UNSET,
    scroll_id: str | Unset = UNSET,
    transcription_id: str | Unset = UNSET,
    version_id: str | Unset = UNSET,
    segment_type: str | Unset = UNSET,
    segment_color: str | Unset = UNSET,
    time_start_milliseconds: int | Unset = UNSET,
    time_end_milliseconds: int | Unset = UNSET,
    time_start_milliseconds_gte: int | Unset = UNSET,
    time_end_milliseconds_lte: int | Unset = UNSET,
    status: str | Unset = UNSET,
    person_id: str | Unset = UNSET,
    share_id: str | Unset = UNSET,
    project_id: str | Unset = UNSET,
    include_users: bool | Unset = UNSET,
    include_all_versions: bool | Unset = UNSET,
) -> Any | GetAssetsByAssetIdSegmentsResponseDefault | SegmentsSchema | None:
    """List of segments


    Required roles:
     - can_read_segments

    Args:
        asset_id (str):
        sort (str | Unset):
        ids (str | Unset):
        query (str | Unset):
        includes (str | Unset):
        per_page (int | Unset):
        page (int | Unset):
        scroll (bool | Unset):
        scroll_id (str | Unset):
        transcription_id (str | Unset):
        version_id (str | Unset):
        segment_type (str | Unset):
        segment_color (str | Unset):
        time_start_milliseconds (int | Unset):
        time_end_milliseconds (int | Unset):
        time_start_milliseconds_gte (int | Unset):
        time_end_milliseconds_lte (int | Unset):
        status (str | Unset):
        person_id (str | Unset):
        share_id (str | Unset):
        project_id (str | Unset):
        include_users (bool | Unset):
        include_all_versions (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAssetsByAssetIdSegmentsResponseDefault | SegmentsSchema
    """

    return sync_detailed(
        asset_id=asset_id,
        client=client,
        sort=sort,
        ids=ids,
        query=query,
        includes=includes,
        per_page=per_page,
        page=page,
        scroll=scroll,
        scroll_id=scroll_id,
        transcription_id=transcription_id,
        version_id=version_id,
        segment_type=segment_type,
        segment_color=segment_color,
        time_start_milliseconds=time_start_milliseconds,
        time_end_milliseconds=time_end_milliseconds,
        time_start_milliseconds_gte=time_start_milliseconds_gte,
        time_end_milliseconds_lte=time_end_milliseconds_lte,
        status=status,
        person_id=person_id,
        share_id=share_id,
        project_id=project_id,
        include_users=include_users,
        include_all_versions=include_all_versions,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
    sort: str | Unset = UNSET,
    ids: str | Unset = UNSET,
    query: str | Unset = UNSET,
    includes: str | Unset = UNSET,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
    scroll: bool | Unset = UNSET,
    scroll_id: str | Unset = UNSET,
    transcription_id: str | Unset = UNSET,
    version_id: str | Unset = UNSET,
    segment_type: str | Unset = UNSET,
    segment_color: str | Unset = UNSET,
    time_start_milliseconds: int | Unset = UNSET,
    time_end_milliseconds: int | Unset = UNSET,
    time_start_milliseconds_gte: int | Unset = UNSET,
    time_end_milliseconds_lte: int | Unset = UNSET,
    status: str | Unset = UNSET,
    person_id: str | Unset = UNSET,
    share_id: str | Unset = UNSET,
    project_id: str | Unset = UNSET,
    include_users: bool | Unset = UNSET,
    include_all_versions: bool | Unset = UNSET,
) -> Response[Any | GetAssetsByAssetIdSegmentsResponseDefault | SegmentsSchema]:
    """List of segments


    Required roles:
     - can_read_segments

    Args:
        asset_id (str):
        sort (str | Unset):
        ids (str | Unset):
        query (str | Unset):
        includes (str | Unset):
        per_page (int | Unset):
        page (int | Unset):
        scroll (bool | Unset):
        scroll_id (str | Unset):
        transcription_id (str | Unset):
        version_id (str | Unset):
        segment_type (str | Unset):
        segment_color (str | Unset):
        time_start_milliseconds (int | Unset):
        time_end_milliseconds (int | Unset):
        time_start_milliseconds_gte (int | Unset):
        time_end_milliseconds_lte (int | Unset):
        status (str | Unset):
        person_id (str | Unset):
        share_id (str | Unset):
        project_id (str | Unset):
        include_users (bool | Unset):
        include_all_versions (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAssetsByAssetIdSegmentsResponseDefault | SegmentsSchema]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        sort=sort,
        ids=ids,
        query=query,
        includes=includes,
        per_page=per_page,
        page=page,
        scroll=scroll,
        scroll_id=scroll_id,
        transcription_id=transcription_id,
        version_id=version_id,
        segment_type=segment_type,
        segment_color=segment_color,
        time_start_milliseconds=time_start_milliseconds,
        time_end_milliseconds=time_end_milliseconds,
        time_start_milliseconds_gte=time_start_milliseconds_gte,
        time_end_milliseconds_lte=time_end_milliseconds_lte,
        status=status,
        person_id=person_id,
        share_id=share_id,
        project_id=project_id,
        include_users=include_users,
        include_all_versions=include_all_versions,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
    sort: str | Unset = UNSET,
    ids: str | Unset = UNSET,
    query: str | Unset = UNSET,
    includes: str | Unset = UNSET,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
    scroll: bool | Unset = UNSET,
    scroll_id: str | Unset = UNSET,
    transcription_id: str | Unset = UNSET,
    version_id: str | Unset = UNSET,
    segment_type: str | Unset = UNSET,
    segment_color: str | Unset = UNSET,
    time_start_milliseconds: int | Unset = UNSET,
    time_end_milliseconds: int | Unset = UNSET,
    time_start_milliseconds_gte: int | Unset = UNSET,
    time_end_milliseconds_lte: int | Unset = UNSET,
    status: str | Unset = UNSET,
    person_id: str | Unset = UNSET,
    share_id: str | Unset = UNSET,
    project_id: str | Unset = UNSET,
    include_users: bool | Unset = UNSET,
    include_all_versions: bool | Unset = UNSET,
) -> Any | GetAssetsByAssetIdSegmentsResponseDefault | SegmentsSchema | None:
    """List of segments


    Required roles:
     - can_read_segments

    Args:
        asset_id (str):
        sort (str | Unset):
        ids (str | Unset):
        query (str | Unset):
        includes (str | Unset):
        per_page (int | Unset):
        page (int | Unset):
        scroll (bool | Unset):
        scroll_id (str | Unset):
        transcription_id (str | Unset):
        version_id (str | Unset):
        segment_type (str | Unset):
        segment_color (str | Unset):
        time_start_milliseconds (int | Unset):
        time_end_milliseconds (int | Unset):
        time_start_milliseconds_gte (int | Unset):
        time_end_milliseconds_lte (int | Unset):
        status (str | Unset):
        person_id (str | Unset):
        share_id (str | Unset):
        project_id (str | Unset):
        include_users (bool | Unset):
        include_all_versions (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAssetsByAssetIdSegmentsResponseDefault | SegmentsSchema
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            client=client,
            sort=sort,
            ids=ids,
            query=query,
            includes=includes,
            per_page=per_page,
            page=page,
            scroll=scroll,
            scroll_id=scroll_id,
            transcription_id=transcription_id,
            version_id=version_id,
            segment_type=segment_type,
            segment_color=segment_color,
            time_start_milliseconds=time_start_milliseconds,
            time_end_milliseconds=time_end_milliseconds,
            time_start_milliseconds_gte=time_start_milliseconds_gte,
            time_end_milliseconds_lte=time_end_milliseconds_lte,
            status=status,
            person_id=person_id,
            share_id=share_id,
            project_id=project_id,
            include_users=include_users,
            include_all_versions=include_all_versions,
        )
    ).parsed
