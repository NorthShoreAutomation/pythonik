from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_portfolios_by_portfolio_id_reindex_response_default import (
    PostPortfoliosByPortfolioIdReindexResponseDefault,
)
from ...models.reindex_portfolio_schema import ReindexPortfolioSchema
from ...types import Response


def _get_kwargs(
    portfolio_id: str,
    *,
    body: ReindexPortfolioSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/portfolios/{portfolio_id}/reindex/".format(
            portfolio_id=quote(str(portfolio_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostPortfoliosByPortfolioIdReindexResponseDefault:
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

    response_default = PostPortfoliosByPortfolioIdReindexResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PostPortfoliosByPortfolioIdReindexResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    portfolio_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ReindexPortfolioSchema,
) -> Response[Any | PostPortfoliosByPortfolioIdReindexResponseDefault]:
    """Reindex the portfolio


    Required roles:
     - can_reindex_portfolios

    Args:
        portfolio_id (str):
        body (ReindexPortfolioSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostPortfoliosByPortfolioIdReindexResponseDefault]
    """

    kwargs = _get_kwargs(
        portfolio_id=portfolio_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    portfolio_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ReindexPortfolioSchema,
) -> Any | PostPortfoliosByPortfolioIdReindexResponseDefault | None:
    """Reindex the portfolio


    Required roles:
     - can_reindex_portfolios

    Args:
        portfolio_id (str):
        body (ReindexPortfolioSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostPortfoliosByPortfolioIdReindexResponseDefault
    """

    return sync_detailed(
        portfolio_id=portfolio_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    portfolio_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ReindexPortfolioSchema,
) -> Response[Any | PostPortfoliosByPortfolioIdReindexResponseDefault]:
    """Reindex the portfolio


    Required roles:
     - can_reindex_portfolios

    Args:
        portfolio_id (str):
        body (ReindexPortfolioSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostPortfoliosByPortfolioIdReindexResponseDefault]
    """

    kwargs = _get_kwargs(
        portfolio_id=portfolio_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    portfolio_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ReindexPortfolioSchema,
) -> Any | PostPortfoliosByPortfolioIdReindexResponseDefault | None:
    """Reindex the portfolio


    Required roles:
     - can_reindex_portfolios

    Args:
        portfolio_id (str):
        body (ReindexPortfolioSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostPortfoliosByPortfolioIdReindexResponseDefault
    """

    return (
        await asyncio_detailed(
            portfolio_id=portfolio_id,
            client=client,
            body=body,
        )
    ).parsed
