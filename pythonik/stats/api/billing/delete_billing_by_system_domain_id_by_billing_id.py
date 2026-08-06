from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_billing_by_system_domain_id_by_billing_id_response_default import (
    DeleteBillingBySystemDomainIdByBillingIdResponseDefault,
)
from ...types import Response


def _get_kwargs(
    system_domain_id: str,
    billing_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/billing/{system_domain_id}/{billing_id}/".format(
            system_domain_id=quote(str(system_domain_id), safe=""),
            billing_id=quote(str(billing_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DeleteBillingBySystemDomainIdByBillingIdResponseDefault:
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

    response_default = (
        DeleteBillingBySystemDomainIdByBillingIdResponseDefault.from_dict(
            response.json()
        )
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DeleteBillingBySystemDomainIdByBillingIdResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    system_domain_id: str,
    billing_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DeleteBillingBySystemDomainIdByBillingIdResponseDefault]:
    """Delete billing record (Requires super admin access).

    Args:
        system_domain_id (str):
        billing_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteBillingBySystemDomainIdByBillingIdResponseDefault]
    """

    kwargs = _get_kwargs(
        system_domain_id=system_domain_id,
        billing_id=billing_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    system_domain_id: str,
    billing_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | DeleteBillingBySystemDomainIdByBillingIdResponseDefault | None:
    """Delete billing record (Requires super admin access).

    Args:
        system_domain_id (str):
        billing_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteBillingBySystemDomainIdByBillingIdResponseDefault
    """

    return sync_detailed(
        system_domain_id=system_domain_id,
        billing_id=billing_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    system_domain_id: str,
    billing_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DeleteBillingBySystemDomainIdByBillingIdResponseDefault]:
    """Delete billing record (Requires super admin access).

    Args:
        system_domain_id (str):
        billing_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteBillingBySystemDomainIdByBillingIdResponseDefault]
    """

    kwargs = _get_kwargs(
        system_domain_id=system_domain_id,
        billing_id=billing_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    system_domain_id: str,
    billing_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | DeleteBillingBySystemDomainIdByBillingIdResponseDefault | None:
    """Delete billing record (Requires super admin access).

    Args:
        system_domain_id (str):
        billing_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteBillingBySystemDomainIdByBillingIdResponseDefault
    """

    return (
        await asyncio_detailed(
            system_domain_id=system_domain_id,
            billing_id=billing_id,
            client=client,
        )
    ).parsed
