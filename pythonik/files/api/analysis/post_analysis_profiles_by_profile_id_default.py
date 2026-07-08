from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_analysis_profiles_by_profile_id_default_response_default import (
    PostAnalysisProfilesByProfileIdDefaultResponseDefault,
)
from ...types import Response


def _get_kwargs(
    profile_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/analysis/profiles/{profile_id}/default/".format(
            profile_id=quote(str(profile_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostAnalysisProfilesByProfileIdDefaultResponseDefault:
    if response.status_code == 201:
        response_201 = cast(Any, None)
        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = PostAnalysisProfilesByProfileIdDefaultResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PostAnalysisProfilesByProfileIdDefaultResponseDefault]:
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
) -> Response[Any | PostAnalysisProfilesByProfileIdDefaultResponseDefault]:
    """Set an analysis profile to the default of its media type


    Required roles:
     - can_write_analysis_profiles

    Args:
        profile_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostAnalysisProfilesByProfileIdDefaultResponseDefault]
    """

    kwargs = _get_kwargs(
        profile_id=profile_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    profile_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | PostAnalysisProfilesByProfileIdDefaultResponseDefault | None:
    """Set an analysis profile to the default of its media type


    Required roles:
     - can_write_analysis_profiles

    Args:
        profile_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostAnalysisProfilesByProfileIdDefaultResponseDefault
    """

    return sync_detailed(
        profile_id=profile_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    profile_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | PostAnalysisProfilesByProfileIdDefaultResponseDefault]:
    """Set an analysis profile to the default of its media type


    Required roles:
     - can_write_analysis_profiles

    Args:
        profile_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostAnalysisProfilesByProfileIdDefaultResponseDefault]
    """

    kwargs = _get_kwargs(
        profile_id=profile_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    profile_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | PostAnalysisProfilesByProfileIdDefaultResponseDefault | None:
    """Set an analysis profile to the default of its media type


    Required roles:
     - can_write_analysis_profiles

    Args:
        profile_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostAnalysisProfilesByProfileIdDefaultResponseDefault
    """

    return (
        await asyncio_detailed(
            profile_id=profile_id,
            client=client,
        )
    ).parsed
