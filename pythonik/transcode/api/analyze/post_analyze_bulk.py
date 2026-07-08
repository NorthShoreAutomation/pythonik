from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bulk_analyze_schema import BulkAnalyzeSchema
from ...models.post_analyze_bulk_response_default import PostAnalyzeBulkResponseDefault
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: BulkAnalyzeSchema | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/analyze/bulk/",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostAnalyzeBulkResponseDefault:
    if response.status_code == 201:
        response_201 = cast(Any, None)
        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = PostAnalyzeBulkResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PostAnalyzeBulkResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BulkAnalyzeSchema | Unset = UNSET,
) -> Response[Any | PostAnalyzeBulkResponseDefault]:
    """Start a job that sends objects for analysis using a custom analysis profile


    Required roles:
     - can_analyze_content

    Args:
        body (BulkAnalyzeSchema | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostAnalyzeBulkResponseDefault]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: BulkAnalyzeSchema | Unset = UNSET,
) -> Any | PostAnalyzeBulkResponseDefault | None:
    """Start a job that sends objects for analysis using a custom analysis profile


    Required roles:
     - can_analyze_content

    Args:
        body (BulkAnalyzeSchema | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostAnalyzeBulkResponseDefault
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BulkAnalyzeSchema | Unset = UNSET,
) -> Response[Any | PostAnalyzeBulkResponseDefault]:
    """Start a job that sends objects for analysis using a custom analysis profile


    Required roles:
     - can_analyze_content

    Args:
        body (BulkAnalyzeSchema | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostAnalyzeBulkResponseDefault]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: BulkAnalyzeSchema | Unset = UNSET,
) -> Any | PostAnalyzeBulkResponseDefault | None:
    """Start a job that sends objects for analysis using a custom analysis profile


    Required roles:
     - can_analyze_content

    Args:
        body (BulkAnalyzeSchema | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostAnalyzeBulkResponseDefault
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
