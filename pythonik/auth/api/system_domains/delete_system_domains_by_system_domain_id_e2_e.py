from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_system_domains_by_system_domain_id_e2e_response_default import (
    DeleteSystemDomainsBySystemDomainIdE2EResponseDefault,
)
from ...types import Response


def _get_kwargs(
    system_domain_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/system_domains/{system_domain_id}/e2e/".format(
            system_domain_id=quote(str(system_domain_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DeleteSystemDomainsBySystemDomainIdE2EResponseDefault:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = DeleteSystemDomainsBySystemDomainIdE2EResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DeleteSystemDomainsBySystemDomainIdE2EResponseDefault]:
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
) -> Response[Any | DeleteSystemDomainsBySystemDomainIdE2EResponseDefault]:
    """Delete a particular system_domain by id.

     (For internal use. Should not be displayed in Swagger docs)

    Args:
        system_domain_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteSystemDomainsBySystemDomainIdE2EResponseDefault]
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
) -> Any | DeleteSystemDomainsBySystemDomainIdE2EResponseDefault | None:
    """Delete a particular system_domain by id.

     (For internal use. Should not be displayed in Swagger docs)

    Args:
        system_domain_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteSystemDomainsBySystemDomainIdE2EResponseDefault
    """

    return sync_detailed(
        system_domain_id=system_domain_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    system_domain_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DeleteSystemDomainsBySystemDomainIdE2EResponseDefault]:
    """Delete a particular system_domain by id.

     (For internal use. Should not be displayed in Swagger docs)

    Args:
        system_domain_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteSystemDomainsBySystemDomainIdE2EResponseDefault]
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
) -> Any | DeleteSystemDomainsBySystemDomainIdE2EResponseDefault | None:
    """Delete a particular system_domain by id.

     (For internal use. Should not be displayed in Swagger docs)

    Args:
        system_domain_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteSystemDomainsBySystemDomainIdE2EResponseDefault
    """

    return (
        await asyncio_detailed(
            system_domain_id=system_domain_id,
            client=client,
        )
    ).parsed
