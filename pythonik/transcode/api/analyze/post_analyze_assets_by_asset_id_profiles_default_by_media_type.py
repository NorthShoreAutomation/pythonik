from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.analyze_schema import AnalyzeSchema
from ...models.post_analyze_assets_by_asset_id_profiles_default_by_media_type_response_default import (
    PostAnalyzeAssetsByAssetIdProfilesDefaultByMediaTypeResponseDefault,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    asset_id: str,
    media_type: str,
    *,
    body: AnalyzeSchema | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/analyze/assets/{asset_id}/profiles/default/{media_type}/".format(
            asset_id=quote(str(asset_id), safe=""),
            media_type=quote(str(media_type), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostAnalyzeAssetsByAssetIdProfilesDefaultByMediaTypeResponseDefault:
    if response.status_code == 201:
        response_201 = cast(Any, None)
        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = (
        PostAnalyzeAssetsByAssetIdProfilesDefaultByMediaTypeResponseDefault.from_dict(
            response.json()
        )
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | PostAnalyzeAssetsByAssetIdProfilesDefaultByMediaTypeResponseDefault
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    asset_id: str,
    media_type: str,
    *,
    client: AuthenticatedClient | Client,
    body: AnalyzeSchema | Unset = UNSET,
) -> Response[
    Any | PostAnalyzeAssetsByAssetIdProfilesDefaultByMediaTypeResponseDefault
]:
    """Start a job that sends an asset for analysis

     with a default analysis profile of specified media typewith a default analysis profile of specified
    media type
    Required roles:
     - can_analyze_content

    Args:
        asset_id (str):
        media_type (str):
        body (AnalyzeSchema | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostAnalyzeAssetsByAssetIdProfilesDefaultByMediaTypeResponseDefault]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        media_type=media_type,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: str,
    media_type: str,
    *,
    client: AuthenticatedClient | Client,
    body: AnalyzeSchema | Unset = UNSET,
) -> Any | PostAnalyzeAssetsByAssetIdProfilesDefaultByMediaTypeResponseDefault | None:
    """Start a job that sends an asset for analysis

     with a default analysis profile of specified media typewith a default analysis profile of specified
    media type
    Required roles:
     - can_analyze_content

    Args:
        asset_id (str):
        media_type (str):
        body (AnalyzeSchema | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostAnalyzeAssetsByAssetIdProfilesDefaultByMediaTypeResponseDefault
    """

    return sync_detailed(
        asset_id=asset_id,
        media_type=media_type,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    media_type: str,
    *,
    client: AuthenticatedClient | Client,
    body: AnalyzeSchema | Unset = UNSET,
) -> Response[
    Any | PostAnalyzeAssetsByAssetIdProfilesDefaultByMediaTypeResponseDefault
]:
    """Start a job that sends an asset for analysis

     with a default analysis profile of specified media typewith a default analysis profile of specified
    media type
    Required roles:
     - can_analyze_content

    Args:
        asset_id (str):
        media_type (str):
        body (AnalyzeSchema | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostAnalyzeAssetsByAssetIdProfilesDefaultByMediaTypeResponseDefault]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        media_type=media_type,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    media_type: str,
    *,
    client: AuthenticatedClient | Client,
    body: AnalyzeSchema | Unset = UNSET,
) -> Any | PostAnalyzeAssetsByAssetIdProfilesDefaultByMediaTypeResponseDefault | None:
    """Start a job that sends an asset for analysis

     with a default analysis profile of specified media typewith a default analysis profile of specified
    media type
    Required roles:
     - can_analyze_content

    Args:
        asset_id (str):
        media_type (str):
        body (AnalyzeSchema | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostAnalyzeAssetsByAssetIdProfilesDefaultByMediaTypeResponseDefault
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            media_type=media_type,
            client=client,
            body=body,
        )
    ).parsed
