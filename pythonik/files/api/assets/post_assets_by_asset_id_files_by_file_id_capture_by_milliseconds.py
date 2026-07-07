from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_assets_by_asset_id_files_by_file_id_capture_by_milliseconds_response_default_type_0 import (
    PostAssetsByAssetIdFilesByFileIdCaptureByMillisecondsResponseDefaultType0,
)
from ...models.post_assets_by_asset_id_files_by_file_id_capture_by_milliseconds_response_default_type_1 import (
    PostAssetsByAssetIdFilesByFileIdCaptureByMillisecondsResponseDefaultType1,
)
from ...models.transcode_request_schema import TranscodeRequestSchema
from ...models.transcode_response_schema import TranscodeResponseSchema
from ...types import Response


def _get_kwargs(
    asset_id: str,
    file_id: str,
    milliseconds: int,
    *,
    body: TranscodeRequestSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/assets/{asset_id}/files/{file_id}/capture/{milliseconds}/".format(
            asset_id=quote(str(asset_id), safe=""),
            file_id=quote(str(file_id), safe=""),
            milliseconds=quote(str(milliseconds), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | PostAssetsByAssetIdFilesByFileIdCaptureByMillisecondsResponseDefaultType0
    | PostAssetsByAssetIdFilesByFileIdCaptureByMillisecondsResponseDefaultType1
    | TranscodeResponseSchema
):
    if response.status_code == 200:
        response_200 = TranscodeResponseSchema.from_dict(response.json())

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
        PostAssetsByAssetIdFilesByFileIdCaptureByMillisecondsResponseDefaultType0
        | PostAssetsByAssetIdFilesByFileIdCaptureByMillisecondsResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = PostAssetsByAssetIdFilesByFileIdCaptureByMillisecondsResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = PostAssetsByAssetIdFilesByFileIdCaptureByMillisecondsResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostAssetsByAssetIdFilesByFileIdCaptureByMillisecondsResponseDefaultType0
    | PostAssetsByAssetIdFilesByFileIdCaptureByMillisecondsResponseDefaultType1
    | TranscodeResponseSchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    asset_id: str,
    file_id: str,
    milliseconds: int,
    *,
    client: AuthenticatedClient | Client,
    body: TranscodeRequestSchema,
) -> Response[
    Any
    | PostAssetsByAssetIdFilesByFileIdCaptureByMillisecondsResponseDefaultType0
    | PostAssetsByAssetIdFilesByFileIdCaptureByMillisecondsResponseDefaultType1
    | TranscodeResponseSchema
]:
    """Create a transcode job for creating still keyframe


    Required roles:
     - can_create_poster

    Args:
        asset_id (str):
        file_id (str):
        milliseconds (int):
        body (TranscodeRequestSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostAssetsByAssetIdFilesByFileIdCaptureByMillisecondsResponseDefaultType0 | PostAssetsByAssetIdFilesByFileIdCaptureByMillisecondsResponseDefaultType1 | TranscodeResponseSchema]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        file_id=file_id,
        milliseconds=milliseconds,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: str,
    file_id: str,
    milliseconds: int,
    *,
    client: AuthenticatedClient | Client,
    body: TranscodeRequestSchema,
) -> (
    Any
    | PostAssetsByAssetIdFilesByFileIdCaptureByMillisecondsResponseDefaultType0
    | PostAssetsByAssetIdFilesByFileIdCaptureByMillisecondsResponseDefaultType1
    | TranscodeResponseSchema
    | None
):
    """Create a transcode job for creating still keyframe


    Required roles:
     - can_create_poster

    Args:
        asset_id (str):
        file_id (str):
        milliseconds (int):
        body (TranscodeRequestSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostAssetsByAssetIdFilesByFileIdCaptureByMillisecondsResponseDefaultType0 | PostAssetsByAssetIdFilesByFileIdCaptureByMillisecondsResponseDefaultType1 | TranscodeResponseSchema
    """

    return sync_detailed(
        asset_id=asset_id,
        file_id=file_id,
        milliseconds=milliseconds,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    file_id: str,
    milliseconds: int,
    *,
    client: AuthenticatedClient | Client,
    body: TranscodeRequestSchema,
) -> Response[
    Any
    | PostAssetsByAssetIdFilesByFileIdCaptureByMillisecondsResponseDefaultType0
    | PostAssetsByAssetIdFilesByFileIdCaptureByMillisecondsResponseDefaultType1
    | TranscodeResponseSchema
]:
    """Create a transcode job for creating still keyframe


    Required roles:
     - can_create_poster

    Args:
        asset_id (str):
        file_id (str):
        milliseconds (int):
        body (TranscodeRequestSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostAssetsByAssetIdFilesByFileIdCaptureByMillisecondsResponseDefaultType0 | PostAssetsByAssetIdFilesByFileIdCaptureByMillisecondsResponseDefaultType1 | TranscodeResponseSchema]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        file_id=file_id,
        milliseconds=milliseconds,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    file_id: str,
    milliseconds: int,
    *,
    client: AuthenticatedClient | Client,
    body: TranscodeRequestSchema,
) -> (
    Any
    | PostAssetsByAssetIdFilesByFileIdCaptureByMillisecondsResponseDefaultType0
    | PostAssetsByAssetIdFilesByFileIdCaptureByMillisecondsResponseDefaultType1
    | TranscodeResponseSchema
    | None
):
    """Create a transcode job for creating still keyframe


    Required roles:
     - can_create_poster

    Args:
        asset_id (str):
        file_id (str):
        milliseconds (int):
        body (TranscodeRequestSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostAssetsByAssetIdFilesByFileIdCaptureByMillisecondsResponseDefaultType0 | PostAssetsByAssetIdFilesByFileIdCaptureByMillisecondsResponseDefaultType1 | TranscodeResponseSchema
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            file_id=file_id,
            milliseconds=milliseconds,
            client=client,
            body=body,
        )
    ).parsed
