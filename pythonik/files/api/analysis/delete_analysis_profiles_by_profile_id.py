from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_analysis_profiles_by_profile_id_response_default import (
    DeleteAnalysisProfilesByProfileIdResponseDefault,
)
from ...types import Response


def _get_kwargs(
    profile_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/analysis/profiles/{profile_id}/".format(
            profile_id=quote(str(profile_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DeleteAnalysisProfilesByProfileIdResponseDefault:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = DeleteAnalysisProfilesByProfileIdResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DeleteAnalysisProfilesByProfileIdResponseDefault]:
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
) -> Response[Any | DeleteAnalysisProfilesByProfileIdResponseDefault]:
    """Delete an analysis profile


    Required roles:
     - can_delete_analysis_profiles

    Args:
        profile_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteAnalysisProfilesByProfileIdResponseDefault]
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
) -> Any | DeleteAnalysisProfilesByProfileIdResponseDefault | None:
    """Delete an analysis profile


    Required roles:
     - can_delete_analysis_profiles

    Args:
        profile_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteAnalysisProfilesByProfileIdResponseDefault
    """

    return sync_detailed(
        profile_id=profile_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    profile_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DeleteAnalysisProfilesByProfileIdResponseDefault]:
    """Delete an analysis profile


    Required roles:
     - can_delete_analysis_profiles

    Args:
        profile_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteAnalysisProfilesByProfileIdResponseDefault]
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
) -> Any | DeleteAnalysisProfilesByProfileIdResponseDefault | None:
    """Delete an analysis profile


    Required roles:
     - can_delete_analysis_profiles

    Args:
        profile_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteAnalysisProfilesByProfileIdResponseDefault
    """

    return (
        await asyncio_detailed(
            profile_id=profile_id,
            client=client,
        )
    ).parsed
