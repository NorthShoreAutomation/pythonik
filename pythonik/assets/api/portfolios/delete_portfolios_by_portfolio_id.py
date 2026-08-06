from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_portfolios_by_portfolio_id_response_default import (
    DeletePortfoliosByPortfolioIdResponseDefault,
)
from ...types import Response


def _get_kwargs(
    portfolio_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/portfolios/{portfolio_id}/".format(
            portfolio_id=quote(str(portfolio_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DeletePortfoliosByPortfolioIdResponseDefault:
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

    response_default = DeletePortfoliosByPortfolioIdResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DeletePortfoliosByPortfolioIdResponseDefault]:
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
) -> Response[Any | DeletePortfoliosByPortfolioIdResponseDefault]:
    """Delete a particular portfolio by id


    Required roles:
     - can_delete_portfolios

    Args:
        portfolio_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeletePortfoliosByPortfolioIdResponseDefault]
    """

    kwargs = _get_kwargs(
        portfolio_id=portfolio_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    portfolio_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | DeletePortfoliosByPortfolioIdResponseDefault | None:
    """Delete a particular portfolio by id


    Required roles:
     - can_delete_portfolios

    Args:
        portfolio_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeletePortfoliosByPortfolioIdResponseDefault
    """

    return sync_detailed(
        portfolio_id=portfolio_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    portfolio_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DeletePortfoliosByPortfolioIdResponseDefault]:
    """Delete a particular portfolio by id


    Required roles:
     - can_delete_portfolios

    Args:
        portfolio_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeletePortfoliosByPortfolioIdResponseDefault]
    """

    kwargs = _get_kwargs(
        portfolio_id=portfolio_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    portfolio_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | DeletePortfoliosByPortfolioIdResponseDefault | None:
    """Delete a particular portfolio by id


    Required roles:
     - can_delete_portfolios

    Args:
        portfolio_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeletePortfoliosByPortfolioIdResponseDefault
    """

    return (
        await asyncio_detailed(
            portfolio_id=portfolio_id,
            client=client,
        )
    ).parsed
