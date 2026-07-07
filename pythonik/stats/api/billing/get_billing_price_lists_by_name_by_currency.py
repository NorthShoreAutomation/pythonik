from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_billing_price_lists_by_name_by_currency_response_default_type_0 import (
    GetBillingPriceListsByNameByCurrencyResponseDefaultType0,
)
from ...models.get_billing_price_lists_by_name_by_currency_response_default_type_1 import (
    GetBillingPriceListsByNameByCurrencyResponseDefaultType1,
)
from ...models.price_schema import PriceSchema
from ...types import Response


def _get_kwargs(
    name: str,
    currency: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/billing/price_lists/{name}/{currency}/".format(
            name=quote(str(name), safe=""),
            currency=quote(str(currency), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetBillingPriceListsByNameByCurrencyResponseDefaultType0
    | GetBillingPriceListsByNameByCurrencyResponseDefaultType1
    | PriceSchema
):
    if response.status_code == 200:
        response_200 = PriceSchema.from_dict(response.json())

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
        GetBillingPriceListsByNameByCurrencyResponseDefaultType0
        | GetBillingPriceListsByNameByCurrencyResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetBillingPriceListsByNameByCurrencyResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            GetBillingPriceListsByNameByCurrencyResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetBillingPriceListsByNameByCurrencyResponseDefaultType0
    | GetBillingPriceListsByNameByCurrencyResponseDefaultType1
    | PriceSchema
]:
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
) -> Response[
    Any
    | GetBillingPriceListsByNameByCurrencyResponseDefaultType0
    | GetBillingPriceListsByNameByCurrencyResponseDefaultType1
    | PriceSchema
]:
    """Get a Price List

    Args:
        name (str):
        currency (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetBillingPriceListsByNameByCurrencyResponseDefaultType0 | GetBillingPriceListsByNameByCurrencyResponseDefaultType1 | PriceSchema]
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
) -> (
    Any
    | GetBillingPriceListsByNameByCurrencyResponseDefaultType0
    | GetBillingPriceListsByNameByCurrencyResponseDefaultType1
    | PriceSchema
    | None
):
    """Get a Price List

    Args:
        name (str):
        currency (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetBillingPriceListsByNameByCurrencyResponseDefaultType0 | GetBillingPriceListsByNameByCurrencyResponseDefaultType1 | PriceSchema
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
) -> Response[
    Any
    | GetBillingPriceListsByNameByCurrencyResponseDefaultType0
    | GetBillingPriceListsByNameByCurrencyResponseDefaultType1
    | PriceSchema
]:
    """Get a Price List

    Args:
        name (str):
        currency (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetBillingPriceListsByNameByCurrencyResponseDefaultType0 | GetBillingPriceListsByNameByCurrencyResponseDefaultType1 | PriceSchema]
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
) -> (
    Any
    | GetBillingPriceListsByNameByCurrencyResponseDefaultType0
    | GetBillingPriceListsByNameByCurrencyResponseDefaultType1
    | PriceSchema
    | None
):
    """Get a Price List

    Args:
        name (str):
        currency (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetBillingPriceListsByNameByCurrencyResponseDefaultType0 | GetBillingPriceListsByNameByCurrencyResponseDefaultType1 | PriceSchema
    """

    return (
        await asyncio_detailed(
            name=name,
            currency=currency,
            client=client,
        )
    ).parsed
