from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.analysis_profile_schema import AnalysisProfileSchema
from ...models.patch_analysis_profiles_by_profile_id_response_default import (
    PatchAnalysisProfilesByProfileIdResponseDefault,
)
from ...types import Response


def _get_kwargs(
    profile_id: str,
    *,
    body: AnalysisProfileSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/analysis/profiles/{profile_id}/".format(
            profile_id=quote(str(profile_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AnalysisProfileSchema | Any | PatchAnalysisProfilesByProfileIdResponseDefault:
    if response.status_code == 200:
        response_200 = AnalysisProfileSchema.from_dict(response.json())

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

    response_default = PatchAnalysisProfilesByProfileIdResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AnalysisProfileSchema | Any | PatchAnalysisProfilesByProfileIdResponseDefault
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    profile_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AnalysisProfileSchema,
) -> Response[
    AnalysisProfileSchema | Any | PatchAnalysisProfilesByProfileIdResponseDefault
]:
    """Update an analysis profile information


    Required roles:
     - can_write_analysis_profiles

    Args:
        profile_id (str):
        body (AnalysisProfileSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalysisProfileSchema | Any | PatchAnalysisProfilesByProfileIdResponseDefault]
    """

    kwargs = _get_kwargs(
        profile_id=profile_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    profile_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AnalysisProfileSchema,
) -> (
    AnalysisProfileSchema | Any | PatchAnalysisProfilesByProfileIdResponseDefault | None
):
    """Update an analysis profile information


    Required roles:
     - can_write_analysis_profiles

    Args:
        profile_id (str):
        body (AnalysisProfileSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalysisProfileSchema | Any | PatchAnalysisProfilesByProfileIdResponseDefault
    """

    return sync_detailed(
        profile_id=profile_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    profile_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AnalysisProfileSchema,
) -> Response[
    AnalysisProfileSchema | Any | PatchAnalysisProfilesByProfileIdResponseDefault
]:
    """Update an analysis profile information


    Required roles:
     - can_write_analysis_profiles

    Args:
        profile_id (str):
        body (AnalysisProfileSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalysisProfileSchema | Any | PatchAnalysisProfilesByProfileIdResponseDefault]
    """

    kwargs = _get_kwargs(
        profile_id=profile_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    profile_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AnalysisProfileSchema,
) -> (
    AnalysisProfileSchema | Any | PatchAnalysisProfilesByProfileIdResponseDefault | None
):
    """Update an analysis profile information


    Required roles:
     - can_write_analysis_profiles

    Args:
        profile_id (str):
        body (AnalysisProfileSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalysisProfileSchema | Any | PatchAnalysisProfilesByProfileIdResponseDefault
    """

    return (
        await asyncio_detailed(
            profile_id=profile_id,
            client=client,
            body=body,
        )
    ).parsed
