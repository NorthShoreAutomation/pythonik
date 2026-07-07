from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_billing_invoices_response_default_type_0 import (
    GetBillingInvoicesResponseDefaultType0,
)
from ...models.get_billing_invoices_response_default_type_1 import (
    GetBillingInvoicesResponseDefaultType1,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    starting_after: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["starting_after"] = starting_after

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/billing/invoices/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetBillingInvoicesResponseDefaultType0
    | GetBillingInvoicesResponseDefaultType1
):
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    def _parse_response_default(
        data: object,
    ) -> (
        GetBillingInvoicesResponseDefaultType0 | GetBillingInvoicesResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = GetBillingInvoicesResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = GetBillingInvoicesResponseDefaultType1.from_dict(data)

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetBillingInvoicesResponseDefaultType0
    | GetBillingInvoicesResponseDefaultType1
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
    starting_after: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[
    Any
    | GetBillingInvoicesResponseDefaultType0
    | GetBillingInvoicesResponseDefaultType1
]:
    """Returns billing invoices


    Required roles:
     - can_read_billing

    Args:
        starting_after (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetBillingInvoicesResponseDefaultType0 | GetBillingInvoicesResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        starting_after=starting_after,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    starting_after: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> (
    Any
    | GetBillingInvoicesResponseDefaultType0
    | GetBillingInvoicesResponseDefaultType1
    | None
):
    """Returns billing invoices


    Required roles:
     - can_read_billing

    Args:
        starting_after (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetBillingInvoicesResponseDefaultType0 | GetBillingInvoicesResponseDefaultType1
    """

    return sync_detailed(
        client=client,
        starting_after=starting_after,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    starting_after: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[
    Any
    | GetBillingInvoicesResponseDefaultType0
    | GetBillingInvoicesResponseDefaultType1
]:
    """Returns billing invoices


    Required roles:
     - can_read_billing

    Args:
        starting_after (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetBillingInvoicesResponseDefaultType0 | GetBillingInvoicesResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        starting_after=starting_after,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    starting_after: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> (
    Any
    | GetBillingInvoicesResponseDefaultType0
    | GetBillingInvoicesResponseDefaultType1
    | None
):
    """Returns billing invoices


    Required roles:
     - can_read_billing

    Args:
        starting_after (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetBillingInvoicesResponseDefaultType0 | GetBillingInvoicesResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            client=client,
            starting_after=starting_after,
            limit=limit,
        )
    ).parsed
