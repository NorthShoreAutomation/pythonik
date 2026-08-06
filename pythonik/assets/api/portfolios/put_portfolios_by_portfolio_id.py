from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.portfolio_schema import PortfolioSchema
from ...models.put_portfolios_by_portfolio_id_response_default import (
    PutPortfoliosByPortfolioIdResponseDefault,
)
from ...types import Response


def _get_kwargs(
    portfolio_id: str,
    *,
    body: PortfolioSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/portfolios/{portfolio_id}/".format(
            portfolio_id=quote(str(portfolio_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PortfolioSchema | PutPortfoliosByPortfolioIdResponseDefault:
    if response.status_code == 200:
        response_200 = PortfolioSchema.from_dict(response.json())

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

    response_default = PutPortfoliosByPortfolioIdResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PortfolioSchema | PutPortfoliosByPortfolioIdResponseDefault]:
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
    body: PortfolioSchema,
) -> Response[Any | PortfolioSchema | PutPortfoliosByPortfolioIdResponseDefault]:
    """Update a portfolio


    Required roles:
     - can_write_portfolios

    Args:
        portfolio_id (str):
        body (PortfolioSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PortfolioSchema | PutPortfoliosByPortfolioIdResponseDefault]
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
    body: PortfolioSchema,
) -> Any | PortfolioSchema | PutPortfoliosByPortfolioIdResponseDefault | None:
    """Update a portfolio


    Required roles:
     - can_write_portfolios

    Args:
        portfolio_id (str):
        body (PortfolioSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PortfolioSchema | PutPortfoliosByPortfolioIdResponseDefault
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
    body: PortfolioSchema,
) -> Response[Any | PortfolioSchema | PutPortfoliosByPortfolioIdResponseDefault]:
    """Update a portfolio


    Required roles:
     - can_write_portfolios

    Args:
        portfolio_id (str):
        body (PortfolioSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PortfolioSchema | PutPortfoliosByPortfolioIdResponseDefault]
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
    body: PortfolioSchema,
) -> Any | PortfolioSchema | PutPortfoliosByPortfolioIdResponseDefault | None:
    """Update a portfolio


    Required roles:
     - can_write_portfolios

    Args:
        portfolio_id (str):
        body (PortfolioSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PortfolioSchema | PutPortfoliosByPortfolioIdResponseDefault
    """

    return (
        await asyncio_detailed(
            portfolio_id=portfolio_id,
            client=client,
            body=body,
        )
    ).parsed
