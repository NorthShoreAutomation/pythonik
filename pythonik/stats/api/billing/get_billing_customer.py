from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.billing_schema import BillingSchema
from ...models.get_billing_customer_response_default_type_0 import (
    GetBillingCustomerResponseDefaultType0,
)
from ...models.get_billing_customer_response_default_type_1 import (
    GetBillingCustomerResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    *,
    body: BillingSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/billing/customer/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | BillingSchema
    | GetBillingCustomerResponseDefaultType0
    | GetBillingCustomerResponseDefaultType1
):
    if response.status_code == 201:
        response_201 = BillingSchema.from_dict(response.json())

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

    def _parse_response_default(
        data: object,
    ) -> (
        GetBillingCustomerResponseDefaultType0 | GetBillingCustomerResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = GetBillingCustomerResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = GetBillingCustomerResponseDefaultType1.from_dict(data)

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | BillingSchema
    | GetBillingCustomerResponseDefaultType0
    | GetBillingCustomerResponseDefaultType1
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
    body: BillingSchema,
) -> Response[
    Any
    | BillingSchema
    | GetBillingCustomerResponseDefaultType0
    | GetBillingCustomerResponseDefaultType1
]:
    """Returns billing customer


    Required roles:
     - can_read_billing

    Args:
        body (BillingSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BillingSchema | GetBillingCustomerResponseDefaultType0 | GetBillingCustomerResponseDefaultType1]
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
    body: BillingSchema,
) -> (
    Any
    | BillingSchema
    | GetBillingCustomerResponseDefaultType0
    | GetBillingCustomerResponseDefaultType1
    | None
):
    """Returns billing customer


    Required roles:
     - can_read_billing

    Args:
        body (BillingSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BillingSchema | GetBillingCustomerResponseDefaultType0 | GetBillingCustomerResponseDefaultType1
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BillingSchema,
) -> Response[
    Any
    | BillingSchema
    | GetBillingCustomerResponseDefaultType0
    | GetBillingCustomerResponseDefaultType1
]:
    """Returns billing customer


    Required roles:
     - can_read_billing

    Args:
        body (BillingSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BillingSchema | GetBillingCustomerResponseDefaultType0 | GetBillingCustomerResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: BillingSchema,
) -> (
    Any
    | BillingSchema
    | GetBillingCustomerResponseDefaultType0
    | GetBillingCustomerResponseDefaultType1
    | None
):
    """Returns billing customer


    Required roles:
     - can_read_billing

    Args:
        body (BillingSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BillingSchema | GetBillingCustomerResponseDefaultType0 | GetBillingCustomerResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
