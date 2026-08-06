from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_portfolios_by_portfolio_id_response_default import (
    GetPortfoliosByPortfolioIdResponseDefault,
)
from ...models.portfolio_schema import PortfolioSchema
from ...types import Response


def _get_kwargs(
    portfolio_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/portfolios/{portfolio_id}/".format(
            portfolio_id=quote(str(portfolio_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetPortfoliosByPortfolioIdResponseDefault | PortfolioSchema:
    if response.status_code == 200:
        response_200 = PortfolioSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = GetPortfoliosByPortfolioIdResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetPortfoliosByPortfolioIdResponseDefault | PortfolioSchema]:
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
) -> Response[Any | GetPortfoliosByPortfolioIdResponseDefault | PortfolioSchema]:
    """Returns a particular portfolio by id


    Required roles:
     - can_read_portfolios

    Args:
        portfolio_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetPortfoliosByPortfolioIdResponseDefault | PortfolioSchema]
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
) -> Any | GetPortfoliosByPortfolioIdResponseDefault | PortfolioSchema | None:
    """Returns a particular portfolio by id


    Required roles:
     - can_read_portfolios

    Args:
        portfolio_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetPortfoliosByPortfolioIdResponseDefault | PortfolioSchema
    """

    return sync_detailed(
        portfolio_id=portfolio_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    portfolio_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetPortfoliosByPortfolioIdResponseDefault | PortfolioSchema]:
    """Returns a particular portfolio by id


    Required roles:
     - can_read_portfolios

    Args:
        portfolio_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetPortfoliosByPortfolioIdResponseDefault | PortfolioSchema]
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
) -> Any | GetPortfoliosByPortfolioIdResponseDefault | PortfolioSchema | None:
    """Returns a particular portfolio by id


    Required roles:
     - can_read_portfolios

    Args:
        portfolio_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetPortfoliosByPortfolioIdResponseDefault | PortfolioSchema
    """

    return (
        await asyncio_detailed(
            portfolio_id=portfolio_id,
            client=client,
        )
    ).parsed
