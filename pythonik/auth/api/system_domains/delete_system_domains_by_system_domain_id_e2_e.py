from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_system_domains_by_system_domain_id_e2e_response_default_type_0 import (
    DeleteSystemDomainsBySystemDomainIdE2EResponseDefaultType0,
)
from ...models.delete_system_domains_by_system_domain_id_e2e_response_default_type_1 import (
    DeleteSystemDomainsBySystemDomainIdE2EResponseDefaultType1,
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
) -> (
    Any
    | DeleteSystemDomainsBySystemDomainIdE2EResponseDefaultType0
    | DeleteSystemDomainsBySystemDomainIdE2EResponseDefaultType1
):
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    def _parse_response_default(
        data: object,
    ) -> (
        DeleteSystemDomainsBySystemDomainIdE2EResponseDefaultType0
        | DeleteSystemDomainsBySystemDomainIdE2EResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                DeleteSystemDomainsBySystemDomainIdE2EResponseDefaultType0.from_dict(
                    data
                )
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            DeleteSystemDomainsBySystemDomainIdE2EResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | DeleteSystemDomainsBySystemDomainIdE2EResponseDefaultType0
    | DeleteSystemDomainsBySystemDomainIdE2EResponseDefaultType1
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
    Any
    | DeleteSystemDomainsBySystemDomainIdE2EResponseDefaultType0
    | DeleteSystemDomainsBySystemDomainIdE2EResponseDefaultType1
]:
    """Delete a particular system_domain by id.

     (For internal use. Should not be displayed in Swagger docs)

    Args:
        system_domain_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteSystemDomainsBySystemDomainIdE2EResponseDefaultType0 | DeleteSystemDomainsBySystemDomainIdE2EResponseDefaultType1]
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
) -> (
    Any
    | DeleteSystemDomainsBySystemDomainIdE2EResponseDefaultType0
    | DeleteSystemDomainsBySystemDomainIdE2EResponseDefaultType1
    | None
):
    """Delete a particular system_domain by id.

     (For internal use. Should not be displayed in Swagger docs)

    Args:
        system_domain_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteSystemDomainsBySystemDomainIdE2EResponseDefaultType0 | DeleteSystemDomainsBySystemDomainIdE2EResponseDefaultType1
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
    Any
    | DeleteSystemDomainsBySystemDomainIdE2EResponseDefaultType0
    | DeleteSystemDomainsBySystemDomainIdE2EResponseDefaultType1
]:
    """Delete a particular system_domain by id.

     (For internal use. Should not be displayed in Swagger docs)

    Args:
        system_domain_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteSystemDomainsBySystemDomainIdE2EResponseDefaultType0 | DeleteSystemDomainsBySystemDomainIdE2EResponseDefaultType1]
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
) -> (
    Any
    | DeleteSystemDomainsBySystemDomainIdE2EResponseDefaultType0
    | DeleteSystemDomainsBySystemDomainIdE2EResponseDefaultType1
    | None
):
    """Delete a particular system_domain by id.

     (For internal use. Should not be displayed in Swagger docs)

    Args:
        system_domain_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteSystemDomainsBySystemDomainIdE2EResponseDefaultType0 | DeleteSystemDomainsBySystemDomainIdE2EResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            system_domain_id=system_domain_id,
            client=client,
        )
    ).parsed
