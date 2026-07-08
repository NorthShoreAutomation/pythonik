from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_system_domains_referral_code_by_referral_code_response_default import (
    PostSystemDomainsReferralCodeByReferralCodeResponseDefault,
)
from ...models.system_domain_from_referral_code_schema import (
    SystemDomainFromReferralCodeSchema,
)
from ...models.system_domain_from_template_schema import SystemDomainFromTemplateSchema
from ...types import Response


def _get_kwargs(
    referral_code: str,
    *,
    body: SystemDomainFromReferralCodeSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/system_domains/referral_code/{referral_code}/".format(
            referral_code=quote(str(referral_code), safe=""),
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
    | PostSystemDomainsReferralCodeByReferralCodeResponseDefault
    | SystemDomainFromTemplateSchema
):
    if response.status_code == 201:
        response_201 = SystemDomainFromTemplateSchema.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = (
        PostSystemDomainsReferralCodeByReferralCodeResponseDefault.from_dict(
            response.json()
        )
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostSystemDomainsReferralCodeByReferralCodeResponseDefault
    | SystemDomainFromTemplateSchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    referral_code: str,
    *,
    client: AuthenticatedClient | Client,
    body: SystemDomainFromReferralCodeSchema,
) -> Response[
    Any
    | PostSystemDomainsReferralCodeByReferralCodeResponseDefault
    | SystemDomainFromTemplateSchema
]:
    """Create a new system domain from a referral code (That is associated to your domain)

    Args:
        referral_code (str):
        body (SystemDomainFromReferralCodeSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostSystemDomainsReferralCodeByReferralCodeResponseDefault | SystemDomainFromTemplateSchema]
    """

    kwargs = _get_kwargs(
        referral_code=referral_code,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    referral_code: str,
    *,
    client: AuthenticatedClient | Client,
    body: SystemDomainFromReferralCodeSchema,
) -> (
    Any
    | PostSystemDomainsReferralCodeByReferralCodeResponseDefault
    | SystemDomainFromTemplateSchema
    | None
):
    """Create a new system domain from a referral code (That is associated to your domain)

    Args:
        referral_code (str):
        body (SystemDomainFromReferralCodeSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostSystemDomainsReferralCodeByReferralCodeResponseDefault | SystemDomainFromTemplateSchema
    """

    return sync_detailed(
        referral_code=referral_code,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    referral_code: str,
    *,
    client: AuthenticatedClient | Client,
    body: SystemDomainFromReferralCodeSchema,
) -> Response[
    Any
    | PostSystemDomainsReferralCodeByReferralCodeResponseDefault
    | SystemDomainFromTemplateSchema
]:
    """Create a new system domain from a referral code (That is associated to your domain)

    Args:
        referral_code (str):
        body (SystemDomainFromReferralCodeSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostSystemDomainsReferralCodeByReferralCodeResponseDefault | SystemDomainFromTemplateSchema]
    """

    kwargs = _get_kwargs(
        referral_code=referral_code,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    referral_code: str,
    *,
    client: AuthenticatedClient | Client,
    body: SystemDomainFromReferralCodeSchema,
) -> (
    Any
    | PostSystemDomainsReferralCodeByReferralCodeResponseDefault
    | SystemDomainFromTemplateSchema
    | None
):
    """Create a new system domain from a referral code (That is associated to your domain)

    Args:
        referral_code (str):
        body (SystemDomainFromReferralCodeSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostSystemDomainsReferralCodeByReferralCodeResponseDefault | SystemDomainFromTemplateSchema
    """

    return (
        await asyncio_detailed(
            referral_code=referral_code,
            client=client,
            body=body,
        )
    ).parsed
