from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.billing_stats_schema import BillingStatsSchema
from ...models.get_billing_status_response_default_type_0 import (
    GetBillingStatusResponseDefaultType0,
)
from ...models.get_billing_status_response_default_type_1 import (
    GetBillingStatusResponseDefaultType1,
)
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/billing/status/",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | BillingStatsSchema
    | GetBillingStatusResponseDefaultType0
    | GetBillingStatusResponseDefaultType1
):
    if response.status_code == 200:
        response_200 = BillingStatsSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    def _parse_response_default(
        data: object,
    ) -> GetBillingStatusResponseDefaultType0 | GetBillingStatusResponseDefaultType1:
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = GetBillingStatusResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = GetBillingStatusResponseDefaultType1.from_dict(data)

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | BillingStatsSchema
    | GetBillingStatusResponseDefaultType0
    | GetBillingStatusResponseDefaultType1
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
) -> Response[
    Any
    | BillingStatsSchema
    | GetBillingStatusResponseDefaultType0
    | GetBillingStatusResponseDefaultType1
]:
    """Returns billing status


    Required roles:
     - can_read_billing

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BillingStatsSchema | GetBillingStatusResponseDefaultType0 | GetBillingStatusResponseDefaultType1]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | BillingStatsSchema
    | GetBillingStatusResponseDefaultType0
    | GetBillingStatusResponseDefaultType1
    | None
):
    """Returns billing status


    Required roles:
     - can_read_billing

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BillingStatsSchema | GetBillingStatusResponseDefaultType0 | GetBillingStatusResponseDefaultType1
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | BillingStatsSchema
    | GetBillingStatusResponseDefaultType0
    | GetBillingStatusResponseDefaultType1
]:
    """Returns billing status


    Required roles:
     - can_read_billing

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BillingStatsSchema | GetBillingStatusResponseDefaultType0 | GetBillingStatusResponseDefaultType1]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | BillingStatsSchema
    | GetBillingStatusResponseDefaultType0
    | GetBillingStatusResponseDefaultType1
    | None
):
    """Returns billing status


    Required roles:
     - can_read_billing

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BillingStatsSchema | GetBillingStatusResponseDefaultType0 | GetBillingStatusResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
