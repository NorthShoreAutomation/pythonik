from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.analysis_profile_schema import AnalysisProfileSchema
from ...models.get_analysis_profiles_by_media_type_default_response_default import (
    GetAnalysisProfilesByMediaTypeDefaultResponseDefault,
)
from ...types import Response


def _get_kwargs(
    media_type: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/analysis/profiles/{media_type}/default/".format(
            media_type=quote(str(media_type), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AnalysisProfileSchema | Any | GetAnalysisProfilesByMediaTypeDefaultResponseDefault:
    if response.status_code == 200:
        response_200 = AnalysisProfileSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = GetAnalysisProfilesByMediaTypeDefaultResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AnalysisProfileSchema | Any | GetAnalysisProfilesByMediaTypeDefaultResponseDefault
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    media_type: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    AnalysisProfileSchema | Any | GetAnalysisProfilesByMediaTypeDefaultResponseDefault
]:
    """Get a default analysis profile

    Args:
        media_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalysisProfileSchema | Any | GetAnalysisProfilesByMediaTypeDefaultResponseDefault]
    """

    kwargs = _get_kwargs(
        media_type=media_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    media_type: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    AnalysisProfileSchema
    | Any
    | GetAnalysisProfilesByMediaTypeDefaultResponseDefault
    | None
):
    """Get a default analysis profile

    Args:
        media_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalysisProfileSchema | Any | GetAnalysisProfilesByMediaTypeDefaultResponseDefault
    """

    return sync_detailed(
        media_type=media_type,
        client=client,
    ).parsed


async def asyncio_detailed(
    media_type: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    AnalysisProfileSchema | Any | GetAnalysisProfilesByMediaTypeDefaultResponseDefault
]:
    """Get a default analysis profile

    Args:
        media_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalysisProfileSchema | Any | GetAnalysisProfilesByMediaTypeDefaultResponseDefault]
    """

    kwargs = _get_kwargs(
        media_type=media_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    media_type: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    AnalysisProfileSchema
    | Any
    | GetAnalysisProfilesByMediaTypeDefaultResponseDefault
    | None
):
    """Get a default analysis profile

    Args:
        media_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalysisProfileSchema | Any | GetAnalysisProfilesByMediaTypeDefaultResponseDefault
    """

    return (
        await asyncio_detailed(
            media_type=media_type,
            client=client,
        )
    ).parsed
