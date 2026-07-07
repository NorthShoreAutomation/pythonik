from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.analysis_profiles_schema import AnalysisProfilesSchema
from ...models.get_analysis_profiles_response_default_type_0 import (
    GetAnalysisProfilesResponseDefaultType0,
)
from ...models.get_analysis_profiles_response_default_type_1 import (
    GetAnalysisProfilesResponseDefaultType1,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    per_page: int | Unset = 10,
    last_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["per_page"] = per_page

    params["last_id"] = last_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/analysis/profiles/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AnalysisProfilesSchema
    | Any
    | GetAnalysisProfilesResponseDefaultType0
    | GetAnalysisProfilesResponseDefaultType1
):
    if response.status_code == 200:
        response_200 = AnalysisProfilesSchema.from_dict(response.json())

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
        GetAnalysisProfilesResponseDefaultType0
        | GetAnalysisProfilesResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = GetAnalysisProfilesResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = GetAnalysisProfilesResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AnalysisProfilesSchema
    | Any
    | GetAnalysisProfilesResponseDefaultType0
    | GetAnalysisProfilesResponseDefaultType1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = 10,
    last_id: str | Unset = UNSET,
) -> Response[
    AnalysisProfilesSchema
    | Any
    | GetAnalysisProfilesResponseDefaultType0
    | GetAnalysisProfilesResponseDefaultType1
]:
    """Get analysis profiles

    Args:
        per_page (int | Unset):  Default: 10.
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalysisProfilesSchema | Any | GetAnalysisProfilesResponseDefaultType0 | GetAnalysisProfilesResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        per_page=per_page,
        last_id=last_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = 10,
    last_id: str | Unset = UNSET,
) -> (
    AnalysisProfilesSchema
    | Any
    | GetAnalysisProfilesResponseDefaultType0
    | GetAnalysisProfilesResponseDefaultType1
    | None
):
    """Get analysis profiles

    Args:
        per_page (int | Unset):  Default: 10.
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalysisProfilesSchema | Any | GetAnalysisProfilesResponseDefaultType0 | GetAnalysisProfilesResponseDefaultType1
    """

    return sync_detailed(
        client=client,
        per_page=per_page,
        last_id=last_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = 10,
    last_id: str | Unset = UNSET,
) -> Response[
    AnalysisProfilesSchema
    | Any
    | GetAnalysisProfilesResponseDefaultType0
    | GetAnalysisProfilesResponseDefaultType1
]:
    """Get analysis profiles

    Args:
        per_page (int | Unset):  Default: 10.
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalysisProfilesSchema | Any | GetAnalysisProfilesResponseDefaultType0 | GetAnalysisProfilesResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        per_page=per_page,
        last_id=last_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = 10,
    last_id: str | Unset = UNSET,
) -> (
    AnalysisProfilesSchema
    | Any
    | GetAnalysisProfilesResponseDefaultType0
    | GetAnalysisProfilesResponseDefaultType1
    | None
):
    """Get analysis profiles

    Args:
        per_page (int | Unset):  Default: 10.
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalysisProfilesSchema | Any | GetAnalysisProfilesResponseDefaultType0 | GetAnalysisProfilesResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            client=client,
            per_page=per_page,
            last_id=last_id,
        )
    ).parsed
