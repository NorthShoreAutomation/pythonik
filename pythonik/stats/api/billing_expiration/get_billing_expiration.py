from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.billings_schema import BillingsSchema
from ...models.get_billing_expiration_response_default_type_0 import (
    GetBillingExpirationResponseDefaultType0,
)
from ...models.get_billing_expiration_response_default_type_1 import (
    GetBillingExpirationResponseDefaultType1,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    per_page: int | Unset = 100,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["per_page"] = per_page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/billing_expiration/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | BillingsSchema
    | GetBillingExpirationResponseDefaultType0
    | GetBillingExpirationResponseDefaultType1
):
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

    def _parse_response_default(
        data: object,
    ) -> (
        GetBillingExpirationResponseDefaultType0
        | GetBillingExpirationResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetBillingExpirationResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = GetBillingExpirationResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | BillingsSchema
    | GetBillingExpirationResponseDefaultType0
    | GetBillingExpirationResponseDefaultType1
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
    per_page: int | Unset = 100,
) -> Response[
    Any
    | BillingsSchema
    | GetBillingExpirationResponseDefaultType0
    | GetBillingExpirationResponseDefaultType1
]:
    """Returns billing expiration info

    Args:
        per_page (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BillingsSchema | GetBillingExpirationResponseDefaultType0 | GetBillingExpirationResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        per_page=per_page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = 100,
) -> (
    Any
    | BillingsSchema
    | GetBillingExpirationResponseDefaultType0
    | GetBillingExpirationResponseDefaultType1
    | None
):
    """Returns billing expiration info

    Args:
        per_page (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BillingsSchema | GetBillingExpirationResponseDefaultType0 | GetBillingExpirationResponseDefaultType1
    """

    return sync_detailed(
        client=client,
        per_page=per_page,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = 100,
) -> Response[
    Any
    | BillingsSchema
    | GetBillingExpirationResponseDefaultType0
    | GetBillingExpirationResponseDefaultType1
]:
    """Returns billing expiration info

    Args:
        per_page (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BillingsSchema | GetBillingExpirationResponseDefaultType0 | GetBillingExpirationResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        per_page=per_page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = 100,
) -> (
    Any
    | BillingsSchema
    | GetBillingExpirationResponseDefaultType0
    | GetBillingExpirationResponseDefaultType1
    | None
):
    """Returns billing expiration info

    Args:
        per_page (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BillingsSchema | GetBillingExpirationResponseDefaultType0 | GetBillingExpirationResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            client=client,
            per_page=per_page,
        )
    ).parsed
