from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_system_domains_by_system_domain_id_response_default import (
    GetSystemDomainsBySystemDomainIdResponseDefault,
)
from ...models.system_domain_schema import SystemDomainSchema
from ...types import Response


def _get_kwargs(
    system_domain_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/system_domains/{system_domain_id}/".format(
            system_domain_id=quote(str(system_domain_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetSystemDomainsBySystemDomainIdResponseDefault | SystemDomainSchema:
    if response.status_code == 200:
        response_200 = SystemDomainSchema.from_dict(response.json())

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

    response_default = GetSystemDomainsBySystemDomainIdResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | GetSystemDomainsBySystemDomainIdResponseDefault | SystemDomainSchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    system_domain_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any | GetSystemDomainsBySystemDomainIdResponseDefault | SystemDomainSchema
]:
    """Returns a particular system domain by id


    Required roles:
     - can_read_system_domains

    Args:
        system_domain_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSystemDomainsBySystemDomainIdResponseDefault | SystemDomainSchema]
    """

    kwargs = _get_kwargs(
        system_domain_id=system_domain_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    system_domain_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetSystemDomainsBySystemDomainIdResponseDefault | SystemDomainSchema | None:
    """Returns a particular system domain by id


    Required roles:
     - can_read_system_domains

    Args:
        system_domain_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSystemDomainsBySystemDomainIdResponseDefault | SystemDomainSchema
    """

    return sync_detailed(
        system_domain_id=system_domain_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    system_domain_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any | GetSystemDomainsBySystemDomainIdResponseDefault | SystemDomainSchema
]:
    """Returns a particular system domain by id


    Required roles:
     - can_read_system_domains

    Args:
        system_domain_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSystemDomainsBySystemDomainIdResponseDefault | SystemDomainSchema]
    """

    kwargs = _get_kwargs(
        system_domain_id=system_domain_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    system_domain_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetSystemDomainsBySystemDomainIdResponseDefault | SystemDomainSchema | None:
    """Returns a particular system domain by id


    Required roles:
     - can_read_system_domains

    Args:
        system_domain_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSystemDomainsBySystemDomainIdResponseDefault | SystemDomainSchema
    """

    return (
        await asyncio_detailed(
            system_domain_id=system_domain_id,
            client=client,
        )
    ).parsed
