from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.analysis_service_account_schema import AnalysisServiceAccountSchema
from ...models.put_analysis_service_accounts_by_analysis_service_account_id_response_default_type_0 import (
    PutAnalysisServiceAccountsByAnalysisServiceAccountIdResponseDefaultType0,
)
from ...models.put_analysis_service_accounts_by_analysis_service_account_id_response_default_type_1 import (
    PutAnalysisServiceAccountsByAnalysisServiceAccountIdResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    analysis_service_account_id: str,
    *,
    body: AnalysisServiceAccountSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/analysis/service_accounts/{analysis_service_account_id}/".format(
            analysis_service_account_id=quote(
                str(analysis_service_account_id), safe=""
            ),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AnalysisServiceAccountSchema
    | Any
    | PutAnalysisServiceAccountsByAnalysisServiceAccountIdResponseDefaultType0
    | PutAnalysisServiceAccountsByAnalysisServiceAccountIdResponseDefaultType1
):
    if response.status_code == 200:
        response_200 = AnalysisServiceAccountSchema.from_dict(response.json())

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
        PutAnalysisServiceAccountsByAnalysisServiceAccountIdResponseDefaultType0
        | PutAnalysisServiceAccountsByAnalysisServiceAccountIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = PutAnalysisServiceAccountsByAnalysisServiceAccountIdResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = PutAnalysisServiceAccountsByAnalysisServiceAccountIdResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AnalysisServiceAccountSchema
    | Any
    | PutAnalysisServiceAccountsByAnalysisServiceAccountIdResponseDefaultType0
    | PutAnalysisServiceAccountsByAnalysisServiceAccountIdResponseDefaultType1
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
    body: AnalysisServiceAccountSchema,
) -> Response[
    AnalysisServiceAccountSchema
    | Any
    | PutAnalysisServiceAccountsByAnalysisServiceAccountIdResponseDefaultType0
    | PutAnalysisServiceAccountsByAnalysisServiceAccountIdResponseDefaultType1
]:
    """Update an analysis service account information


    Required roles:
     - can_write_analysis_service_accounts

    Args:
        analysis_service_account_id (str):
        body (AnalysisServiceAccountSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalysisServiceAccountSchema | Any | PutAnalysisServiceAccountsByAnalysisServiceAccountIdResponseDefaultType0 | PutAnalysisServiceAccountsByAnalysisServiceAccountIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        analysis_service_account_id=analysis_service_account_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    analysis_service_account_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AnalysisServiceAccountSchema,
) -> (
    AnalysisServiceAccountSchema
    | Any
    | PutAnalysisServiceAccountsByAnalysisServiceAccountIdResponseDefaultType0
    | PutAnalysisServiceAccountsByAnalysisServiceAccountIdResponseDefaultType1
    | None
):
    """Update an analysis service account information


    Required roles:
     - can_write_analysis_service_accounts

    Args:
        analysis_service_account_id (str):
        body (AnalysisServiceAccountSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalysisServiceAccountSchema | Any | PutAnalysisServiceAccountsByAnalysisServiceAccountIdResponseDefaultType0 | PutAnalysisServiceAccountsByAnalysisServiceAccountIdResponseDefaultType1
    """

    return sync_detailed(
        analysis_service_account_id=analysis_service_account_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    analysis_service_account_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AnalysisServiceAccountSchema,
) -> Response[
    AnalysisServiceAccountSchema
    | Any
    | PutAnalysisServiceAccountsByAnalysisServiceAccountIdResponseDefaultType0
    | PutAnalysisServiceAccountsByAnalysisServiceAccountIdResponseDefaultType1
]:
    """Update an analysis service account information


    Required roles:
     - can_write_analysis_service_accounts

    Args:
        analysis_service_account_id (str):
        body (AnalysisServiceAccountSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalysisServiceAccountSchema | Any | PutAnalysisServiceAccountsByAnalysisServiceAccountIdResponseDefaultType0 | PutAnalysisServiceAccountsByAnalysisServiceAccountIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        analysis_service_account_id=analysis_service_account_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    analysis_service_account_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AnalysisServiceAccountSchema,
) -> (
    AnalysisServiceAccountSchema
    | Any
    | PutAnalysisServiceAccountsByAnalysisServiceAccountIdResponseDefaultType0
    | PutAnalysisServiceAccountsByAnalysisServiceAccountIdResponseDefaultType1
    | None
):
    """Update an analysis service account information


    Required roles:
     - can_write_analysis_service_accounts

    Args:
        analysis_service_account_id (str):
        body (AnalysisServiceAccountSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalysisServiceAccountSchema | Any | PutAnalysisServiceAccountsByAnalysisServiceAccountIdResponseDefaultType0 | PutAnalysisServiceAccountsByAnalysisServiceAccountIdResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            analysis_service_account_id=analysis_service_account_id,
            client=client,
            body=body,
        )
    ).parsed
