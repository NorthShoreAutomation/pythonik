from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_system_by_system_domain_id_response_default import (
    GetSystemBySystemDomainIdResponseDefault,
)
from ...models.system_setting_public_schema import SystemSettingPublicSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    system_domain_id: str,
    *,
    ignore_logo_url: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["ignore_logo_url"] = ignore_logo_url

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/system/{system_domain_id}/".format(
            system_domain_id=quote(str(system_domain_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetSystemBySystemDomainIdResponseDefault | SystemSettingPublicSchema:
    if response.status_code == 200:
        response_200 = SystemSettingPublicSchema.from_dict(response.json())

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

    response_default = GetSystemBySystemDomainIdResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | GetSystemBySystemDomainIdResponseDefault | SystemSettingPublicSchema
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
    ignore_logo_url: bool | Unset = UNSET,
) -> Response[
    Any | GetSystemBySystemDomainIdResponseDefault | SystemSettingPublicSchema
]:
    """System settings

    Args:
        system_domain_id (str):
        ignore_logo_url (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSystemBySystemDomainIdResponseDefault | SystemSettingPublicSchema]
    """

    kwargs = _get_kwargs(
        system_domain_id=system_domain_id,
        ignore_logo_url=ignore_logo_url,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    system_domain_id: str,
    *,
    client: AuthenticatedClient | Client,
    ignore_logo_url: bool | Unset = UNSET,
) -> Any | GetSystemBySystemDomainIdResponseDefault | SystemSettingPublicSchema | None:
    """System settings

    Args:
        system_domain_id (str):
        ignore_logo_url (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSystemBySystemDomainIdResponseDefault | SystemSettingPublicSchema
    """

    return sync_detailed(
        system_domain_id=system_domain_id,
        client=client,
        ignore_logo_url=ignore_logo_url,
    ).parsed


async def asyncio_detailed(
    system_domain_id: str,
    *,
    client: AuthenticatedClient | Client,
    ignore_logo_url: bool | Unset = UNSET,
) -> Response[
    Any | GetSystemBySystemDomainIdResponseDefault | SystemSettingPublicSchema
]:
    """System settings

    Args:
        system_domain_id (str):
        ignore_logo_url (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSystemBySystemDomainIdResponseDefault | SystemSettingPublicSchema]
    """

    kwargs = _get_kwargs(
        system_domain_id=system_domain_id,
        ignore_logo_url=ignore_logo_url,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    system_domain_id: str,
    *,
    client: AuthenticatedClient | Client,
    ignore_logo_url: bool | Unset = UNSET,
) -> Any | GetSystemBySystemDomainIdResponseDefault | SystemSettingPublicSchema | None:
    """System settings

    Args:
        system_domain_id (str):
        ignore_logo_url (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSystemBySystemDomainIdResponseDefault | SystemSettingPublicSchema
    """

    return (
        await asyncio_detailed(
            system_domain_id=system_domain_id,
            client=client,
            ignore_logo_url=ignore_logo_url,
        )
    ).parsed
