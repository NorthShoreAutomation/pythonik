from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.patch_system_domains_by_system_domain_id_response_default_type_0 import (
    PatchSystemDomainsBySystemDomainIdResponseDefaultType0,
)
from ...models.patch_system_domains_by_system_domain_id_response_default_type_1 import (
    PatchSystemDomainsBySystemDomainIdResponseDefaultType1,
)
from ...models.system_domain_super_admin_schema import SystemDomainSuperAdminSchema
from ...types import Response


def _get_kwargs(
    system_domain_id: str,
    *,
    body: SystemDomainSuperAdminSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/system_domains/{system_domain_id}/".format(
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
    | PatchSystemDomainsBySystemDomainIdResponseDefaultType0
    | PatchSystemDomainsBySystemDomainIdResponseDefaultType1
    | SystemDomainSuperAdminSchema
):
    if response.status_code == 200:
        response_200 = SystemDomainSuperAdminSchema.from_dict(response.json())

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
        PatchSystemDomainsBySystemDomainIdResponseDefaultType0
        | PatchSystemDomainsBySystemDomainIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                PatchSystemDomainsBySystemDomainIdResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PatchSystemDomainsBySystemDomainIdResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PatchSystemDomainsBySystemDomainIdResponseDefaultType0
    | PatchSystemDomainsBySystemDomainIdResponseDefaultType1
    | SystemDomainSuperAdminSchema
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
    body: SystemDomainSuperAdminSchema,
) -> Response[
    Any
    | PatchSystemDomainsBySystemDomainIdResponseDefaultType0
    | PatchSystemDomainsBySystemDomainIdResponseDefaultType1
    | SystemDomainSuperAdminSchema
]:
    """Update system domain

    Args:
        system_domain_id (str):
        body (SystemDomainSuperAdminSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PatchSystemDomainsBySystemDomainIdResponseDefaultType0 | PatchSystemDomainsBySystemDomainIdResponseDefaultType1 | SystemDomainSuperAdminSchema]
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
    body: SystemDomainSuperAdminSchema,
) -> (
    Any
    | PatchSystemDomainsBySystemDomainIdResponseDefaultType0
    | PatchSystemDomainsBySystemDomainIdResponseDefaultType1
    | SystemDomainSuperAdminSchema
    | None
):
    """Update system domain

    Args:
        system_domain_id (str):
        body (SystemDomainSuperAdminSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PatchSystemDomainsBySystemDomainIdResponseDefaultType0 | PatchSystemDomainsBySystemDomainIdResponseDefaultType1 | SystemDomainSuperAdminSchema
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
    body: SystemDomainSuperAdminSchema,
) -> Response[
    Any
    | PatchSystemDomainsBySystemDomainIdResponseDefaultType0
    | PatchSystemDomainsBySystemDomainIdResponseDefaultType1
    | SystemDomainSuperAdminSchema
]:
    """Update system domain

    Args:
        system_domain_id (str):
        body (SystemDomainSuperAdminSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PatchSystemDomainsBySystemDomainIdResponseDefaultType0 | PatchSystemDomainsBySystemDomainIdResponseDefaultType1 | SystemDomainSuperAdminSchema]
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
    body: SystemDomainSuperAdminSchema,
) -> (
    Any
    | PatchSystemDomainsBySystemDomainIdResponseDefaultType0
    | PatchSystemDomainsBySystemDomainIdResponseDefaultType1
    | SystemDomainSuperAdminSchema
    | None
):
    """Update system domain

    Args:
        system_domain_id (str):
        body (SystemDomainSuperAdminSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PatchSystemDomainsBySystemDomainIdResponseDefaultType0 | PatchSystemDomainsBySystemDomainIdResponseDefaultType1 | SystemDomainSuperAdminSchema
    """

    return (
        await asyncio_detailed(
            system_domain_id=system_domain_id,
            client=client,
            body=body,
        )
    ).parsed
