from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_ordway_billing_invoices_response_default_type_0 import (
    GetOrdwayBillingInvoicesResponseDefaultType0,
)
from ...models.get_ordway_billing_invoices_response_default_type_1 import (
    GetOrdwayBillingInvoicesResponseDefaultType1,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    per_page: int | Unset = UNSET,
    page: int | Unset = 1,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["per_page"] = per_page

    params["page"] = page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/ordway/billing/invoices/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetOrdwayBillingInvoicesResponseDefaultType0
    | GetOrdwayBillingInvoicesResponseDefaultType1
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
        GetOrdwayBillingInvoicesResponseDefaultType0
        | GetOrdwayBillingInvoicesResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetOrdwayBillingInvoicesResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            GetOrdwayBillingInvoicesResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetOrdwayBillingInvoicesResponseDefaultType0
    | GetOrdwayBillingInvoicesResponseDefaultType1
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
    per_page: int | Unset = UNSET,
    page: int | Unset = 1,
) -> Response[
    Any
    | GetOrdwayBillingInvoicesResponseDefaultType0
    | GetOrdwayBillingInvoicesResponseDefaultType1
]:
    """Returns billing invoices


    Required roles:
     - can_read_billing

    Args:
        per_page (int | Unset):
        page (int | Unset):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetOrdwayBillingInvoicesResponseDefaultType0 | GetOrdwayBillingInvoicesResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        per_page=per_page,
        page=page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    page: int | Unset = 1,
) -> (
    Any
    | GetOrdwayBillingInvoicesResponseDefaultType0
    | GetOrdwayBillingInvoicesResponseDefaultType1
    | None
):
    """Returns billing invoices


    Required roles:
     - can_read_billing

    Args:
        per_page (int | Unset):
        page (int | Unset):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetOrdwayBillingInvoicesResponseDefaultType0 | GetOrdwayBillingInvoicesResponseDefaultType1
    """

    return sync_detailed(
        client=client,
        per_page=per_page,
        page=page,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    page: int | Unset = 1,
) -> Response[
    Any
    | GetOrdwayBillingInvoicesResponseDefaultType0
    | GetOrdwayBillingInvoicesResponseDefaultType1
]:
    """Returns billing invoices


    Required roles:
     - can_read_billing

    Args:
        per_page (int | Unset):
        page (int | Unset):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetOrdwayBillingInvoicesResponseDefaultType0 | GetOrdwayBillingInvoicesResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        per_page=per_page,
        page=page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    page: int | Unset = 1,
) -> (
    Any
    | GetOrdwayBillingInvoicesResponseDefaultType0
    | GetOrdwayBillingInvoicesResponseDefaultType1
    | None
):
    """Returns billing invoices


    Required roles:
     - can_read_billing

    Args:
        per_page (int | Unset):
        page (int | Unset):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetOrdwayBillingInvoicesResponseDefaultType0 | GetOrdwayBillingInvoicesResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            client=client,
            per_page=per_page,
            page=page,
        )
    ).parsed
