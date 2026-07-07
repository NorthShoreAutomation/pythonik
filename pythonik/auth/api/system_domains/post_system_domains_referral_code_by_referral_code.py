from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_system_domains_referral_code_by_referral_code_response_default_type_0 import (
    PostSystemDomainsReferralCodeByReferralCodeResponseDefaultType0,
)
from ...models.post_system_domains_referral_code_by_referral_code_response_default_type_1 import (
    PostSystemDomainsReferralCodeByReferralCodeResponseDefaultType1,
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
    | PostSystemDomainsReferralCodeByReferralCodeResponseDefaultType0
    | PostSystemDomainsReferralCodeByReferralCodeResponseDefaultType1
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

    def _parse_response_default(
        data: object,
    ) -> (
        PostSystemDomainsReferralCodeByReferralCodeResponseDefaultType0
        | PostSystemDomainsReferralCodeByReferralCodeResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = PostSystemDomainsReferralCodeByReferralCodeResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PostSystemDomainsReferralCodeByReferralCodeResponseDefaultType1.from_dict(
                data
            )
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostSystemDomainsReferralCodeByReferralCodeResponseDefaultType0
    | PostSystemDomainsReferralCodeByReferralCodeResponseDefaultType1
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
    | PostSystemDomainsReferralCodeByReferralCodeResponseDefaultType0
    | PostSystemDomainsReferralCodeByReferralCodeResponseDefaultType1
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
        Response[Any | PostSystemDomainsReferralCodeByReferralCodeResponseDefaultType0 | PostSystemDomainsReferralCodeByReferralCodeResponseDefaultType1 | SystemDomainFromTemplateSchema]
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
    | PostSystemDomainsReferralCodeByReferralCodeResponseDefaultType0
    | PostSystemDomainsReferralCodeByReferralCodeResponseDefaultType1
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
        Any | PostSystemDomainsReferralCodeByReferralCodeResponseDefaultType0 | PostSystemDomainsReferralCodeByReferralCodeResponseDefaultType1 | SystemDomainFromTemplateSchema
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
    | PostSystemDomainsReferralCodeByReferralCodeResponseDefaultType0
    | PostSystemDomainsReferralCodeByReferralCodeResponseDefaultType1
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
        Response[Any | PostSystemDomainsReferralCodeByReferralCodeResponseDefaultType0 | PostSystemDomainsReferralCodeByReferralCodeResponseDefaultType1 | SystemDomainFromTemplateSchema]
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
    | PostSystemDomainsReferralCodeByReferralCodeResponseDefaultType0
    | PostSystemDomainsReferralCodeByReferralCodeResponseDefaultType1
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
        Any | PostSystemDomainsReferralCodeByReferralCodeResponseDefaultType0 | PostSystemDomainsReferralCodeByReferralCodeResponseDefaultType1 | SystemDomainFromTemplateSchema
    """

    return (
        await asyncio_detailed(
            referral_code=referral_code,
            client=client,
            body=body,
        )
    ).parsed
