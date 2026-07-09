from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.billing_customer_schema import BillingCustomerSchema
from ...models.post_billing_customer_response_default import (
    PostBillingCustomerResponseDefault,
)
from ...types import Response


def _get_kwargs(
    *,
    body: BillingCustomerSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/billing/customer/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | BillingCustomerSchema | PostBillingCustomerResponseDefault:
    if response.status_code == 201:
        response_201 = BillingCustomerSchema.from_dict(response.json())

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

    response_default = PostBillingCustomerResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | BillingCustomerSchema | PostBillingCustomerResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BillingCustomerSchema,
) -> Response[Any | BillingCustomerSchema | PostBillingCustomerResponseDefault]:
    """Updates billing customer


    Required roles:
     - can_write_billing

    Args:
        body (BillingCustomerSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BillingCustomerSchema | PostBillingCustomerResponseDefault]
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
    body: BillingCustomerSchema,
) -> Any | BillingCustomerSchema | PostBillingCustomerResponseDefault | None:
    """Updates billing customer


    Required roles:
     - can_write_billing

    Args:
        body (BillingCustomerSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BillingCustomerSchema | PostBillingCustomerResponseDefault
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BillingCustomerSchema,
) -> Response[Any | BillingCustomerSchema | PostBillingCustomerResponseDefault]:
    """Updates billing customer


    Required roles:
     - can_write_billing

    Args:
        body (BillingCustomerSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BillingCustomerSchema | PostBillingCustomerResponseDefault]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: BillingCustomerSchema,
) -> Any | BillingCustomerSchema | PostBillingCustomerResponseDefault | None:
    """Updates billing customer


    Required roles:
     - can_write_billing

    Args:
        body (BillingCustomerSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BillingCustomerSchema | PostBillingCustomerResponseDefault
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
