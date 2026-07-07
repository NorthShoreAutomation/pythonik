from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_auth_saml_domains_by_domain_response_default_type_0 import (
    DeleteAuthSamlDomainsByDomainResponseDefaultType0,
)
from ...models.delete_auth_saml_domains_by_domain_response_default_type_1 import (
    DeleteAuthSamlDomainsByDomainResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    domain: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/auth/saml/domains/{domain}/".format(
            domain=quote(str(domain), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | DeleteAuthSamlDomainsByDomainResponseDefaultType0
    | DeleteAuthSamlDomainsByDomainResponseDefaultType1
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

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    def _parse_response_default(
        data: object,
    ) -> (
        DeleteAuthSamlDomainsByDomainResponseDefaultType0
        | DeleteAuthSamlDomainsByDomainResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                DeleteAuthSamlDomainsByDomainResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            DeleteAuthSamlDomainsByDomainResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | DeleteAuthSamlDomainsByDomainResponseDefaultType0
    | DeleteAuthSamlDomainsByDomainResponseDefaultType1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    domain: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | DeleteAuthSamlDomainsByDomainResponseDefaultType0
    | DeleteAuthSamlDomainsByDomainResponseDefaultType1
]:
    """Unbind domain from identity provider

    Args:
        domain (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteAuthSamlDomainsByDomainResponseDefaultType0 | DeleteAuthSamlDomainsByDomainResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        domain=domain,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    domain: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | DeleteAuthSamlDomainsByDomainResponseDefaultType0
    | DeleteAuthSamlDomainsByDomainResponseDefaultType1
    | None
):
    """Unbind domain from identity provider

    Args:
        domain (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteAuthSamlDomainsByDomainResponseDefaultType0 | DeleteAuthSamlDomainsByDomainResponseDefaultType1
    """

    return sync_detailed(
        domain=domain,
        client=client,
    ).parsed


async def asyncio_detailed(
    domain: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | DeleteAuthSamlDomainsByDomainResponseDefaultType0
    | DeleteAuthSamlDomainsByDomainResponseDefaultType1
]:
    """Unbind domain from identity provider

    Args:
        domain (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteAuthSamlDomainsByDomainResponseDefaultType0 | DeleteAuthSamlDomainsByDomainResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        domain=domain,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    domain: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | DeleteAuthSamlDomainsByDomainResponseDefaultType0
    | DeleteAuthSamlDomainsByDomainResponseDefaultType1
    | None
):
    """Unbind domain from identity provider

    Args:
        domain (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteAuthSamlDomainsByDomainResponseDefaultType0 | DeleteAuthSamlDomainsByDomainResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            domain=domain,
            client=client,
        )
    ).parsed
