from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.analysis_profile_schema import AnalysisProfileSchema
from ...models.get_analysis_profiles_by_media_type_default_response_default_type_0 import (
    GetAnalysisProfilesByMediaTypeDefaultResponseDefaultType0,
)
from ...models.get_analysis_profiles_by_media_type_default_response_default_type_1 import (
    GetAnalysisProfilesByMediaTypeDefaultResponseDefaultType1,
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
) -> (
    AnalysisProfileSchema
    | Any
    | GetAnalysisProfilesByMediaTypeDefaultResponseDefaultType0
    | GetAnalysisProfilesByMediaTypeDefaultResponseDefaultType1
):
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

    def _parse_response_default(
        data: object,
    ) -> (
        GetAnalysisProfilesByMediaTypeDefaultResponseDefaultType0
        | GetAnalysisProfilesByMediaTypeDefaultResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetAnalysisProfilesByMediaTypeDefaultResponseDefaultType0.from_dict(
                    data
                )
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            GetAnalysisProfilesByMediaTypeDefaultResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AnalysisProfileSchema
    | Any
    | GetAnalysisProfilesByMediaTypeDefaultResponseDefaultType0
    | GetAnalysisProfilesByMediaTypeDefaultResponseDefaultType1
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
    AnalysisProfileSchema
    | Any
    | GetAnalysisProfilesByMediaTypeDefaultResponseDefaultType0
    | GetAnalysisProfilesByMediaTypeDefaultResponseDefaultType1
]:
    """Get a default analysis profile

    Args:
        media_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalysisProfileSchema | Any | GetAnalysisProfilesByMediaTypeDefaultResponseDefaultType0 | GetAnalysisProfilesByMediaTypeDefaultResponseDefaultType1]
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
    | GetAnalysisProfilesByMediaTypeDefaultResponseDefaultType0
    | GetAnalysisProfilesByMediaTypeDefaultResponseDefaultType1
    | None
):
    """Get a default analysis profile

    Args:
        media_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalysisProfileSchema | Any | GetAnalysisProfilesByMediaTypeDefaultResponseDefaultType0 | GetAnalysisProfilesByMediaTypeDefaultResponseDefaultType1
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
    AnalysisProfileSchema
    | Any
    | GetAnalysisProfilesByMediaTypeDefaultResponseDefaultType0
    | GetAnalysisProfilesByMediaTypeDefaultResponseDefaultType1
]:
    """Get a default analysis profile

    Args:
        media_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalysisProfileSchema | Any | GetAnalysisProfilesByMediaTypeDefaultResponseDefaultType0 | GetAnalysisProfilesByMediaTypeDefaultResponseDefaultType1]
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
    | GetAnalysisProfilesByMediaTypeDefaultResponseDefaultType0
    | GetAnalysisProfilesByMediaTypeDefaultResponseDefaultType1
    | None
):
    """Get a default analysis profile

    Args:
        media_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalysisProfileSchema | Any | GetAnalysisProfilesByMediaTypeDefaultResponseDefaultType0 | GetAnalysisProfilesByMediaTypeDefaultResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            media_type=media_type,
            client=client,
        )
    ).parsed
