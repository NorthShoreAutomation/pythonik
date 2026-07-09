from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_billing_price_lists_by_name_by_currency_response_default import (
    DeleteBillingPriceListsByNameByCurrencyResponseDefault,
)
from ...types import Response


def _get_kwargs(
    name: str,
    currency: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/billing/price_lists/{name}/{currency}/".format(
            name=quote(str(name), safe=""),
            currency=quote(str(currency), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DeleteBillingPriceListsByNameByCurrencyResponseDefault:
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

    response_default = DeleteBillingPriceListsByNameByCurrencyResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DeleteBillingPriceListsByNameByCurrencyResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    name: str,
    currency: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DeleteBillingPriceListsByNameByCurrencyResponseDefault]:
    """Delete a Price list

    Args:
        name (str):
        currency (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteBillingPriceListsByNameByCurrencyResponseDefault]
    """

    kwargs = _get_kwargs(
        name=name,
        currency=currency,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    name: str,
    currency: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | DeleteBillingPriceListsByNameByCurrencyResponseDefault | None:
    """Delete a Price list

    Args:
        name (str):
        currency (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteBillingPriceListsByNameByCurrencyResponseDefault
    """

    return sync_detailed(
        name=name,
        currency=currency,
        client=client,
    ).parsed


async def asyncio_detailed(
    name: str,
    currency: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DeleteBillingPriceListsByNameByCurrencyResponseDefault]:
    """Delete a Price list

    Args:
        name (str):
        currency (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteBillingPriceListsByNameByCurrencyResponseDefault]
    """

    kwargs = _get_kwargs(
        name=name,
        currency=currency,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    name: str,
    currency: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | DeleteBillingPriceListsByNameByCurrencyResponseDefault | None:
    """Delete a Price list

    Args:
        name (str):
        currency (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteBillingPriceListsByNameByCurrencyResponseDefault
    """

    return (
        await asyncio_detailed(
            name=name,
            currency=currency,
            client=client,
        )
    ).parsed
