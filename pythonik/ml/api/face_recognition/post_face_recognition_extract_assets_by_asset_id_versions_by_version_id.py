from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_face_recognition_extract_assets_by_asset_id_versions_by_version_id_response_default import (
    PostFaceRecognitionExtractAssetsByAssetIdVersionsByVersionIdResponseDefault,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    asset_id: str,
    version_id: str,
    *,
    face_image_analysis_profile_id: str | Unset = UNSET,
    face_video_analysis_profile_id: str | Unset = UNSET,
    force: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["face_image_analysis_profile_id"] = face_image_analysis_profile_id

    params["face_video_analysis_profile_id"] = face_video_analysis_profile_id

    params["force"] = force

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/face_recognition/extract/assets/{asset_id}/versions/{version_id}/".format(
            asset_id=quote(str(asset_id), safe=""),
            version_id=quote(str(version_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostFaceRecognitionExtractAssetsByAssetIdVersionsByVersionIdResponseDefault:
    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    response_default = PostFaceRecognitionExtractAssetsByAssetIdVersionsByVersionIdResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | PostFaceRecognitionExtractAssetsByAssetIdVersionsByVersionIdResponseDefault
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
    face_image_analysis_profile_id: str | Unset = UNSET,
    face_video_analysis_profile_id: str | Unset = UNSET,
    force: bool | Unset = UNSET,
) -> Response[
    Any | PostFaceRecognitionExtractAssetsByAssetIdVersionsByVersionIdResponseDefault
]:
    """Extract face images and face data for an asset


    Required roles:
     - can_trigger_face_recognition

    Args:
        asset_id (str):
        version_id (str):
        face_image_analysis_profile_id (str | Unset):
        face_video_analysis_profile_id (str | Unset):
        force (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostFaceRecognitionExtractAssetsByAssetIdVersionsByVersionIdResponseDefault]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        version_id=version_id,
        face_image_analysis_profile_id=face_image_analysis_profile_id,
        face_video_analysis_profile_id=face_video_analysis_profile_id,
        force=force,
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
    face_image_analysis_profile_id: str | Unset = UNSET,
    face_video_analysis_profile_id: str | Unset = UNSET,
    force: bool | Unset = UNSET,
) -> (
    Any
    | PostFaceRecognitionExtractAssetsByAssetIdVersionsByVersionIdResponseDefault
    | None
):
    """Extract face images and face data for an asset


    Required roles:
     - can_trigger_face_recognition

    Args:
        asset_id (str):
        version_id (str):
        face_image_analysis_profile_id (str | Unset):
        face_video_analysis_profile_id (str | Unset):
        force (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostFaceRecognitionExtractAssetsByAssetIdVersionsByVersionIdResponseDefault
    """

    return sync_detailed(
        asset_id=asset_id,
        version_id=version_id,
        client=client,
        face_image_analysis_profile_id=face_image_analysis_profile_id,
        face_video_analysis_profile_id=face_video_analysis_profile_id,
        force=force,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    version_id: str,
    *,
    client: AuthenticatedClient | Client,
    face_image_analysis_profile_id: str | Unset = UNSET,
    face_video_analysis_profile_id: str | Unset = UNSET,
    force: bool | Unset = UNSET,
) -> Response[
    Any | PostFaceRecognitionExtractAssetsByAssetIdVersionsByVersionIdResponseDefault
]:
    """Extract face images and face data for an asset


    Required roles:
     - can_trigger_face_recognition

    Args:
        asset_id (str):
        version_id (str):
        face_image_analysis_profile_id (str | Unset):
        face_video_analysis_profile_id (str | Unset):
        force (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostFaceRecognitionExtractAssetsByAssetIdVersionsByVersionIdResponseDefault]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        version_id=version_id,
        face_image_analysis_profile_id=face_image_analysis_profile_id,
        face_video_analysis_profile_id=face_video_analysis_profile_id,
        force=force,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    version_id: str,
    *,
    client: AuthenticatedClient | Client,
    face_image_analysis_profile_id: str | Unset = UNSET,
    face_video_analysis_profile_id: str | Unset = UNSET,
    force: bool | Unset = UNSET,
) -> (
    Any
    | PostFaceRecognitionExtractAssetsByAssetIdVersionsByVersionIdResponseDefault
    | None
):
    """Extract face images and face data for an asset


    Required roles:
     - can_trigger_face_recognition

    Args:
        asset_id (str):
        version_id (str):
        face_image_analysis_profile_id (str | Unset):
        face_video_analysis_profile_id (str | Unset):
        force (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostFaceRecognitionExtractAssetsByAssetIdVersionsByVersionIdResponseDefault
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            version_id=version_id,
            client=client,
            face_image_analysis_profile_id=face_image_analysis_profile_id,
            face_video_analysis_profile_id=face_video_analysis_profile_id,
            force=force,
        )
    ).parsed
