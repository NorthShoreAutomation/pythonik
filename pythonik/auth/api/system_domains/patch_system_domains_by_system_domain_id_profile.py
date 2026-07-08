from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.patch_system_domains_by_system_domain_id_profile_response_default import (
    PatchSystemDomainsBySystemDomainIdProfileResponseDefault,
)
from ...models.system_domain_profile_schema import SystemDomainProfileSchema
from ...types import Response


def _get_kwargs(
    system_domain_id: str,
    *,
    body: SystemDomainProfileSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/system_domains/{system_domain_id}/profile/".format(
            system_domain_id=quote(str(system_domain_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | PatchSystemDomainsBySystemDomainIdProfileResponseDefault
    | SystemDomainProfileSchema
):
    if response.status_code == 200:
        response_200 = SystemDomainProfileSchema.from_dict(response.json())

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

    response_default = (
        PatchSystemDomainsBySystemDomainIdProfileResponseDefault.from_dict(
            response.json()
        )
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PatchSystemDomainsBySystemDomainIdProfileResponseDefault
    | SystemDomainProfileSchema
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
    body: SystemDomainProfileSchema,
) -> Response[
    Any
    | PatchSystemDomainsBySystemDomainIdProfileResponseDefault
    | SystemDomainProfileSchema
]:
    """Update system domain profile

    Args:
        system_domain_id (str):
        body (SystemDomainProfileSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PatchSystemDomainsBySystemDomainIdProfileResponseDefault | SystemDomainProfileSchema]
    """

    kwargs = _get_kwargs(
        system_domain_id=system_domain_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    system_domain_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SystemDomainProfileSchema,
) -> (
    Any
    | PatchSystemDomainsBySystemDomainIdProfileResponseDefault
    | SystemDomainProfileSchema
    | None
):
    """Update system domain profile

    Args:
        system_domain_id (str):
        body (SystemDomainProfileSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PatchSystemDomainsBySystemDomainIdProfileResponseDefault | SystemDomainProfileSchema
    """

    return sync_detailed(
        system_domain_id=system_domain_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    system_domain_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SystemDomainProfileSchema,
) -> Response[
    Any
    | PatchSystemDomainsBySystemDomainIdProfileResponseDefault
    | SystemDomainProfileSchema
]:
    """Update system domain profile

    Args:
        system_domain_id (str):
        body (SystemDomainProfileSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PatchSystemDomainsBySystemDomainIdProfileResponseDefault | SystemDomainProfileSchema]
    """

    kwargs = _get_kwargs(
        system_domain_id=system_domain_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    system_domain_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SystemDomainProfileSchema,
) -> (
    Any
    | PatchSystemDomainsBySystemDomainIdProfileResponseDefault
    | SystemDomainProfileSchema
    | None
):
    """Update system domain profile

    Args:
        system_domain_id (str):
        body (SystemDomainProfileSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PatchSystemDomainsBySystemDomainIdProfileResponseDefault | SystemDomainProfileSchema
    """

    return (
        await asyncio_detailed(
            system_domain_id=system_domain_id,
            client=client,
            body=body,
        )
    ).parsed
