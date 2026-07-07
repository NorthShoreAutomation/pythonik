from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.asset_transcription_properties_schema import (
    AssetTranscriptionPropertiesSchema,
)
from ...models.patch_assets_by_asset_id_versions_by_version_id_transcriptions_by_transcription_id_properties_response_default_type_0 import (
    PatchAssetsByAssetIdVersionsByVersionIdTranscriptionsByTranscriptionIdPropertiesResponseDefaultType0,
)
from ...models.patch_assets_by_asset_id_versions_by_version_id_transcriptions_by_transcription_id_properties_response_default_type_1 import (
    PatchAssetsByAssetIdVersionsByVersionIdTranscriptionsByTranscriptionIdPropertiesResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    asset_id: str,
    version_id: str,
    transcription_id: str,
    *,
    body: AssetTranscriptionPropertiesSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/assets/{asset_id}/versions/{version_id}/transcriptions/{transcription_id}/properties/".format(
            asset_id=quote(str(asset_id), safe=""),
            version_id=quote(str(version_id), safe=""),
            transcription_id=quote(str(transcription_id), safe=""),
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
    | AssetTranscriptionPropertiesSchema
    | PatchAssetsByAssetIdVersionsByVersionIdTranscriptionsByTranscriptionIdPropertiesResponseDefaultType0
    | PatchAssetsByAssetIdVersionsByVersionIdTranscriptionsByTranscriptionIdPropertiesResponseDefaultType1
):
    if response.status_code == 200:
        response_200 = AssetTranscriptionPropertiesSchema.from_dict(response.json())

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
        PatchAssetsByAssetIdVersionsByVersionIdTranscriptionsByTranscriptionIdPropertiesResponseDefaultType0
        | PatchAssetsByAssetIdVersionsByVersionIdTranscriptionsByTranscriptionIdPropertiesResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = PatchAssetsByAssetIdVersionsByVersionIdTranscriptionsByTranscriptionIdPropertiesResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = PatchAssetsByAssetIdVersionsByVersionIdTranscriptionsByTranscriptionIdPropertiesResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | AssetTranscriptionPropertiesSchema
    | PatchAssetsByAssetIdVersionsByVersionIdTranscriptionsByTranscriptionIdPropertiesResponseDefaultType0
    | PatchAssetsByAssetIdVersionsByVersionIdTranscriptionsByTranscriptionIdPropertiesResponseDefaultType1
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
    transcription_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AssetTranscriptionPropertiesSchema,
) -> Response[
    Any
    | AssetTranscriptionPropertiesSchema
    | PatchAssetsByAssetIdVersionsByVersionIdTranscriptionsByTranscriptionIdPropertiesResponseDefaultType0
    | PatchAssetsByAssetIdVersionsByVersionIdTranscriptionsByTranscriptionIdPropertiesResponseDefaultType1
]:
    """Update transcription properties by ID


    Required roles:
     - can_write_transcriptions

    Args:
        asset_id (str):
        version_id (str):
        transcription_id (str):
        body (AssetTranscriptionPropertiesSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AssetTranscriptionPropertiesSchema | PatchAssetsByAssetIdVersionsByVersionIdTranscriptionsByTranscriptionIdPropertiesResponseDefaultType0 | PatchAssetsByAssetIdVersionsByVersionIdTranscriptionsByTranscriptionIdPropertiesResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        version_id=version_id,
        transcription_id=transcription_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: str,
    version_id: str,
    transcription_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AssetTranscriptionPropertiesSchema,
) -> (
    Any
    | AssetTranscriptionPropertiesSchema
    | PatchAssetsByAssetIdVersionsByVersionIdTranscriptionsByTranscriptionIdPropertiesResponseDefaultType0
    | PatchAssetsByAssetIdVersionsByVersionIdTranscriptionsByTranscriptionIdPropertiesResponseDefaultType1
    | None
):
    """Update transcription properties by ID


    Required roles:
     - can_write_transcriptions

    Args:
        asset_id (str):
        version_id (str):
        transcription_id (str):
        body (AssetTranscriptionPropertiesSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AssetTranscriptionPropertiesSchema | PatchAssetsByAssetIdVersionsByVersionIdTranscriptionsByTranscriptionIdPropertiesResponseDefaultType0 | PatchAssetsByAssetIdVersionsByVersionIdTranscriptionsByTranscriptionIdPropertiesResponseDefaultType1
    """

    return sync_detailed(
        asset_id=asset_id,
        version_id=version_id,
        transcription_id=transcription_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    version_id: str,
    transcription_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AssetTranscriptionPropertiesSchema,
) -> Response[
    Any
    | AssetTranscriptionPropertiesSchema
    | PatchAssetsByAssetIdVersionsByVersionIdTranscriptionsByTranscriptionIdPropertiesResponseDefaultType0
    | PatchAssetsByAssetIdVersionsByVersionIdTranscriptionsByTranscriptionIdPropertiesResponseDefaultType1
]:
    """Update transcription properties by ID


    Required roles:
     - can_write_transcriptions

    Args:
        asset_id (str):
        version_id (str):
        transcription_id (str):
        body (AssetTranscriptionPropertiesSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AssetTranscriptionPropertiesSchema | PatchAssetsByAssetIdVersionsByVersionIdTranscriptionsByTranscriptionIdPropertiesResponseDefaultType0 | PatchAssetsByAssetIdVersionsByVersionIdTranscriptionsByTranscriptionIdPropertiesResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        version_id=version_id,
        transcription_id=transcription_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    version_id: str,
    transcription_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AssetTranscriptionPropertiesSchema,
) -> (
    Any
    | AssetTranscriptionPropertiesSchema
    | PatchAssetsByAssetIdVersionsByVersionIdTranscriptionsByTranscriptionIdPropertiesResponseDefaultType0
    | PatchAssetsByAssetIdVersionsByVersionIdTranscriptionsByTranscriptionIdPropertiesResponseDefaultType1
    | None
):
    """Update transcription properties by ID


    Required roles:
     - can_write_transcriptions

    Args:
        asset_id (str):
        version_id (str):
        transcription_id (str):
        body (AssetTranscriptionPropertiesSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AssetTranscriptionPropertiesSchema | PatchAssetsByAssetIdVersionsByVersionIdTranscriptionsByTranscriptionIdPropertiesResponseDefaultType0 | PatchAssetsByAssetIdVersionsByVersionIdTranscriptionsByTranscriptionIdPropertiesResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            version_id=version_id,
            transcription_id=transcription_id,
            client=client,
            body=body,
        )
    ).parsed
