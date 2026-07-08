from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.acl_templates_schema import ACLTemplatesSchema
from ...models.get_acl_templates_response_default import GetAclTemplatesResponseDefault
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/acl/templates/",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ACLTemplatesSchema | Any | GetAclTemplatesResponseDefault:
    if response.status_code == 200:
        response_200 = ACLTemplatesSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = GetAclTemplatesResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ACLTemplatesSchema | Any | GetAclTemplatesResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[ACLTemplatesSchema | Any | GetAclTemplatesResponseDefault]:
    """Retreive all acl templates


    Required roles:
     - can_read_acl_templates

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ACLTemplatesSchema | Any | GetAclTemplatesResponseDefault]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> ACLTemplatesSchema | Any | GetAclTemplatesResponseDefault | None:
    """Retreive all acl templates


    Required roles:
     - can_read_acl_templates

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ACLTemplatesSchema | Any | GetAclTemplatesResponseDefault
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[ACLTemplatesSchema | Any | GetAclTemplatesResponseDefault]:
    """Retreive all acl templates


    Required roles:
     - can_read_acl_templates

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ACLTemplatesSchema | Any | GetAclTemplatesResponseDefault]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> ACLTemplatesSchema | Any | GetAclTemplatesResponseDefault | None:
    """Retreive all acl templates


    Required roles:
     - can_read_acl_templates

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ACLTemplatesSchema | Any | GetAclTemplatesResponseDefault
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
