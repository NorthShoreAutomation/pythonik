from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.billing_settings_schema import BillingSettingsSchema
from ...models.get_billing_settings_response_default import (
    GetBillingSettingsResponseDefault,
)
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/billing/settings/",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | BillingSettingsSchema | GetBillingSettingsResponseDefault:
    if response.status_code == 200:
        response_200 = BillingSettingsSchema.from_dict(response.json())

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

    response_default = GetBillingSettingsResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | BillingSettingsSchema | GetBillingSettingsResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | BillingSettingsSchema | GetBillingSettingsResponseDefault]:
    """Updates Billing Settings


    Required roles:
     - can_read_billing

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BillingSettingsSchema | GetBillingSettingsResponseDefault]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> Any | BillingSettingsSchema | GetBillingSettingsResponseDefault | None:
    """Updates Billing Settings


    Required roles:
     - can_read_billing

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BillingSettingsSchema | GetBillingSettingsResponseDefault
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | BillingSettingsSchema | GetBillingSettingsResponseDefault]:
    """Updates Billing Settings


    Required roles:
     - can_read_billing

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BillingSettingsSchema | GetBillingSettingsResponseDefault]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> Any | BillingSettingsSchema | GetBillingSettingsResponseDefault | None:
    """Updates Billing Settings


    Required roles:
     - can_read_billing

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BillingSettingsSchema | GetBillingSettingsResponseDefault
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
