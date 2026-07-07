from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.analysis_service_account_read_schema import (
    AnalysisServiceAccountReadSchema,
)
from ...models.get_analysis_service_accounts_by_analysis_service_account_id_response_default_type_0 import (
    GetAnalysisServiceAccountsByAnalysisServiceAccountIdResponseDefaultType0,
)
from ...models.get_analysis_service_accounts_by_analysis_service_account_id_response_default_type_1 import (
    GetAnalysisServiceAccountsByAnalysisServiceAccountIdResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    analysis_service_account_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/analysis/service_accounts/{analysis_service_account_id}/".format(
            analysis_service_account_id=quote(
                str(analysis_service_account_id), safe=""
            ),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AnalysisServiceAccountReadSchema
    | Any
    | GetAnalysisServiceAccountsByAnalysisServiceAccountIdResponseDefaultType0
    | GetAnalysisServiceAccountsByAnalysisServiceAccountIdResponseDefaultType1
):
    if response.status_code == 200:
        response_200 = AnalysisServiceAccountReadSchema.from_dict(response.json())

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
        GetAnalysisServiceAccountsByAnalysisServiceAccountIdResponseDefaultType0
        | GetAnalysisServiceAccountsByAnalysisServiceAccountIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = GetAnalysisServiceAccountsByAnalysisServiceAccountIdResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = GetAnalysisServiceAccountsByAnalysisServiceAccountIdResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AnalysisServiceAccountReadSchema
    | Any
    | GetAnalysisServiceAccountsByAnalysisServiceAccountIdResponseDefaultType0
    | GetAnalysisServiceAccountsByAnalysisServiceAccountIdResponseDefaultType1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    analysis_service_account_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    AnalysisServiceAccountReadSchema
    | Any
    | GetAnalysisServiceAccountsByAnalysisServiceAccountIdResponseDefaultType0
    | GetAnalysisServiceAccountsByAnalysisServiceAccountIdResponseDefaultType1
]:
    """Get an analysis service account


    Required roles:
     - can_read_analysis_service_accounts

    Args:
        analysis_service_account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalysisServiceAccountReadSchema | Any | GetAnalysisServiceAccountsByAnalysisServiceAccountIdResponseDefaultType0 | GetAnalysisServiceAccountsByAnalysisServiceAccountIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        analysis_service_account_id=analysis_service_account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    analysis_service_account_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    AnalysisServiceAccountReadSchema
    | Any
    | GetAnalysisServiceAccountsByAnalysisServiceAccountIdResponseDefaultType0
    | GetAnalysisServiceAccountsByAnalysisServiceAccountIdResponseDefaultType1
    | None
):
    """Get an analysis service account


    Required roles:
     - can_read_analysis_service_accounts

    Args:
        analysis_service_account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalysisServiceAccountReadSchema | Any | GetAnalysisServiceAccountsByAnalysisServiceAccountIdResponseDefaultType0 | GetAnalysisServiceAccountsByAnalysisServiceAccountIdResponseDefaultType1
    """

    return sync_detailed(
        analysis_service_account_id=analysis_service_account_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    analysis_service_account_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    AnalysisServiceAccountReadSchema
    | Any
    | GetAnalysisServiceAccountsByAnalysisServiceAccountIdResponseDefaultType0
    | GetAnalysisServiceAccountsByAnalysisServiceAccountIdResponseDefaultType1
]:
    """Get an analysis service account


    Required roles:
     - can_read_analysis_service_accounts

    Args:
        analysis_service_account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalysisServiceAccountReadSchema | Any | GetAnalysisServiceAccountsByAnalysisServiceAccountIdResponseDefaultType0 | GetAnalysisServiceAccountsByAnalysisServiceAccountIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        analysis_service_account_id=analysis_service_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    analysis_service_account_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    AnalysisServiceAccountReadSchema
    | Any
    | GetAnalysisServiceAccountsByAnalysisServiceAccountIdResponseDefaultType0
    | GetAnalysisServiceAccountsByAnalysisServiceAccountIdResponseDefaultType1
    | None
):
    """Get an analysis service account


    Required roles:
     - can_read_analysis_service_accounts

    Args:
        analysis_service_account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalysisServiceAccountReadSchema | Any | GetAnalysisServiceAccountsByAnalysisServiceAccountIdResponseDefaultType0 | GetAnalysisServiceAccountsByAnalysisServiceAccountIdResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            analysis_service_account_id=analysis_service_account_id,
            client=client,
        )
    ).parsed
