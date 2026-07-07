from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.analysis_profile_schema import AnalysisProfileSchema
from ...models.get_analysis_profiles_by_profile_id_response_default_type_0 import (
    GetAnalysisProfilesByProfileIdResponseDefaultType0,
)
from ...models.get_analysis_profiles_by_profile_id_response_default_type_1 import (
    GetAnalysisProfilesByProfileIdResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    profile_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/analysis/profiles/{profile_id}/".format(
            profile_id=quote(str(profile_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AnalysisProfileSchema
    | Any
    | GetAnalysisProfilesByProfileIdResponseDefaultType0
    | GetAnalysisProfilesByProfileIdResponseDefaultType1
):
    if response.status_code == 200:
        response_200 = AnalysisProfileSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    def _parse_response_default(
        data: object,
    ) -> (
        GetAnalysisProfilesByProfileIdResponseDefaultType0
        | GetAnalysisProfilesByProfileIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetAnalysisProfilesByProfileIdResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            GetAnalysisProfilesByProfileIdResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AnalysisProfileSchema
    | Any
    | GetAnalysisProfilesByProfileIdResponseDefaultType0
    | GetAnalysisProfilesByProfileIdResponseDefaultType1
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
) -> Response[
    AnalysisProfileSchema
    | Any
    | GetAnalysisProfilesByProfileIdResponseDefaultType0
    | GetAnalysisProfilesByProfileIdResponseDefaultType1
]:
    """Get an analysis profile

    Args:
        profile_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalysisProfileSchema | Any | GetAnalysisProfilesByProfileIdResponseDefaultType0 | GetAnalysisProfilesByProfileIdResponseDefaultType1]
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
) -> (
    AnalysisProfileSchema
    | Any
    | GetAnalysisProfilesByProfileIdResponseDefaultType0
    | GetAnalysisProfilesByProfileIdResponseDefaultType1
    | None
):
    """Get an analysis profile

    Args:
        profile_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalysisProfileSchema | Any | GetAnalysisProfilesByProfileIdResponseDefaultType0 | GetAnalysisProfilesByProfileIdResponseDefaultType1
    """

    return sync_detailed(
        profile_id=profile_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    profile_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    AnalysisProfileSchema
    | Any
    | GetAnalysisProfilesByProfileIdResponseDefaultType0
    | GetAnalysisProfilesByProfileIdResponseDefaultType1
]:
    """Get an analysis profile

    Args:
        profile_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalysisProfileSchema | Any | GetAnalysisProfilesByProfileIdResponseDefaultType0 | GetAnalysisProfilesByProfileIdResponseDefaultType1]
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
) -> (
    AnalysisProfileSchema
    | Any
    | GetAnalysisProfilesByProfileIdResponseDefaultType0
    | GetAnalysisProfilesByProfileIdResponseDefaultType1
    | None
):
    """Get an analysis profile

    Args:
        profile_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalysisProfileSchema | Any | GetAnalysisProfilesByProfileIdResponseDefaultType0 | GetAnalysisProfilesByProfileIdResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            profile_id=profile_id,
            client=client,
        )
    ).parsed
