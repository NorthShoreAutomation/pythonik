from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_assets_by_asset_id_versions_by_version_id_transcode_response_default_type_0 import (
    PostAssetsByAssetIdVersionsByVersionIdTranscodeResponseDefaultType0,
)
from ...models.post_assets_by_asset_id_versions_by_version_id_transcode_response_default_type_1 import (
    PostAssetsByAssetIdVersionsByVersionIdTranscodeResponseDefaultType1,
)
from ...models.transcode_request_schema import TranscodeRequestSchema
from ...types import Response


def _get_kwargs(
    asset_id: str,
    version_id: str,
    *,
    body: TranscodeRequestSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/assets/{asset_id}/versions/{version_id}/transcode/".format(
            asset_id=quote(str(asset_id), safe=""),
            version_id=quote(str(version_id), safe=""),
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
    | PostAssetsByAssetIdVersionsByVersionIdTranscodeResponseDefaultType0
    | PostAssetsByAssetIdVersionsByVersionIdTranscodeResponseDefaultType1
):
    if response.status_code == 200:
        response_200 = cast(Any, None)
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
        PostAssetsByAssetIdVersionsByVersionIdTranscodeResponseDefaultType0
        | PostAssetsByAssetIdVersionsByVersionIdTranscodeResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = PostAssetsByAssetIdVersionsByVersionIdTranscodeResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = PostAssetsByAssetIdVersionsByVersionIdTranscodeResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostAssetsByAssetIdVersionsByVersionIdTranscodeResponseDefaultType0
    | PostAssetsByAssetIdVersionsByVersionIdTranscodeResponseDefaultType1
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
    body: TranscodeRequestSchema,
) -> Response[
    Any
    | PostAssetsByAssetIdVersionsByVersionIdTranscodeResponseDefaultType0
    | PostAssetsByAssetIdVersionsByVersionIdTranscodeResponseDefaultType1
]:
    """Create a transcode job for a specific asset version


    Required roles:
     - can_create_transcode_jobs

    Args:
        asset_id (str):
        version_id (str):
        body (TranscodeRequestSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostAssetsByAssetIdVersionsByVersionIdTranscodeResponseDefaultType0 | PostAssetsByAssetIdVersionsByVersionIdTranscodeResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        version_id=version_id,
        body=body,
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
    body: TranscodeRequestSchema,
) -> (
    Any
    | PostAssetsByAssetIdVersionsByVersionIdTranscodeResponseDefaultType0
    | PostAssetsByAssetIdVersionsByVersionIdTranscodeResponseDefaultType1
    | None
):
    """Create a transcode job for a specific asset version


    Required roles:
     - can_create_transcode_jobs

    Args:
        asset_id (str):
        version_id (str):
        body (TranscodeRequestSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostAssetsByAssetIdVersionsByVersionIdTranscodeResponseDefaultType0 | PostAssetsByAssetIdVersionsByVersionIdTranscodeResponseDefaultType1
    """

    return sync_detailed(
        asset_id=asset_id,
        version_id=version_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    version_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: TranscodeRequestSchema,
) -> Response[
    Any
    | PostAssetsByAssetIdVersionsByVersionIdTranscodeResponseDefaultType0
    | PostAssetsByAssetIdVersionsByVersionIdTranscodeResponseDefaultType1
]:
    """Create a transcode job for a specific asset version


    Required roles:
     - can_create_transcode_jobs

    Args:
        asset_id (str):
        version_id (str):
        body (TranscodeRequestSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostAssetsByAssetIdVersionsByVersionIdTranscodeResponseDefaultType0 | PostAssetsByAssetIdVersionsByVersionIdTranscodeResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        version_id=version_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    version_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: TranscodeRequestSchema,
) -> (
    Any
    | PostAssetsByAssetIdVersionsByVersionIdTranscodeResponseDefaultType0
    | PostAssetsByAssetIdVersionsByVersionIdTranscodeResponseDefaultType1
    | None
):
    """Create a transcode job for a specific asset version


    Required roles:
     - can_create_transcode_jobs

    Args:
        asset_id (str):
        version_id (str):
        body (TranscodeRequestSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostAssetsByAssetIdVersionsByVersionIdTranscodeResponseDefaultType0 | PostAssetsByAssetIdVersionsByVersionIdTranscodeResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            version_id=version_id,
            client=client,
            body=body,
        )
    ).parsed
