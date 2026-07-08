from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.billings_schema import BillingsSchema
from ...models.get_ordway_billing_response_default import (
    GetOrdwayBillingResponseDefault,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    from_date: str | Unset = UNSET,
    to_date: str | Unset = UNSET,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["from_date"] = from_date

    params["to_date"] = to_date

    params["per_page"] = per_page

    params["page"] = page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/ordway/billing/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | BillingsSchema | GetOrdwayBillingResponseDefault:
    if response.status_code == 200:
        response_200 = BillingsSchema.from_dict(response.json())

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

    response_default = GetOrdwayBillingResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | BillingsSchema | GetOrdwayBillingResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    from_date: str | Unset = UNSET,
    to_date: str | Unset = UNSET,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
) -> Response[Any | BillingsSchema | GetOrdwayBillingResponseDefault]:
    """Returns billing info


    Required roles:
     - can_read_stats

    Args:
        from_date (str | Unset):
        to_date (str | Unset):
        per_page (int | Unset):
        page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BillingsSchema | GetOrdwayBillingResponseDefault]
    """

    kwargs = _get_kwargs(
        from_date=from_date,
        to_date=to_date,
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
    from_date: str | Unset = UNSET,
    to_date: str | Unset = UNSET,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
) -> Any | BillingsSchema | GetOrdwayBillingResponseDefault | None:
    """Returns billing info


    Required roles:
     - can_read_stats

    Args:
        from_date (str | Unset):
        to_date (str | Unset):
        per_page (int | Unset):
        page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BillingsSchema | GetOrdwayBillingResponseDefault
    """

    return sync_detailed(
        client=client,
        from_date=from_date,
        to_date=to_date,
        per_page=per_page,
        page=page,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    from_date: str | Unset = UNSET,
    to_date: str | Unset = UNSET,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
) -> Response[Any | BillingsSchema | GetOrdwayBillingResponseDefault]:
    """Returns billing info


    Required roles:
     - can_read_stats

    Args:
        from_date (str | Unset):
        to_date (str | Unset):
        per_page (int | Unset):
        page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BillingsSchema | GetOrdwayBillingResponseDefault]
    """

    kwargs = _get_kwargs(
        from_date=from_date,
        to_date=to_date,
        per_page=per_page,
        page=page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    from_date: str | Unset = UNSET,
    to_date: str | Unset = UNSET,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
) -> Any | BillingsSchema | GetOrdwayBillingResponseDefault | None:
    """Returns billing info


    Required roles:
     - can_read_stats

    Args:
        from_date (str | Unset):
        to_date (str | Unset):
        per_page (int | Unset):
        page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BillingsSchema | GetOrdwayBillingResponseDefault
    """

    return (
        await asyncio_detailed(
            client=client,
            from_date=from_date,
            to_date=to_date,
            per_page=per_page,
            page=page,
        )
    ).parsed
