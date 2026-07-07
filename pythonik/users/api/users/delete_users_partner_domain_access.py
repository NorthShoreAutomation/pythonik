from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_users_partner_domain_access_response_default_type_0 import (
    DeleteUsersPartnerDomainAccessResponseDefaultType0,
)
from ...models.delete_users_partner_domain_access_response_default_type_1 import (
    DeleteUsersPartnerDomainAccessResponseDefaultType1,
)
from ...models.partner_domain_access_schema import PartnerDomainAccessSchema
from ...types import Response


def _get_kwargs(
    *,
    body: PartnerDomainAccessSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/users/partner_domain_access/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | DeleteUsersPartnerDomainAccessResponseDefaultType0
    | DeleteUsersPartnerDomainAccessResponseDefaultType1
):
    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    def _parse_response_default(
        data: object,
    ) -> (
        DeleteUsersPartnerDomainAccessResponseDefaultType0
        | DeleteUsersPartnerDomainAccessResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                DeleteUsersPartnerDomainAccessResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            DeleteUsersPartnerDomainAccessResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | DeleteUsersPartnerDomainAccessResponseDefaultType0
    | DeleteUsersPartnerDomainAccessResponseDefaultType1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PartnerDomainAccessSchema,
) -> Response[
    Any
    | DeleteUsersPartnerDomainAccessResponseDefaultType0
    | DeleteUsersPartnerDomainAccessResponseDefaultType1
]:
    """Remove customer domain access from all users in a partner domain.

         (Super admins only)

    Args:
        body (PartnerDomainAccessSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteUsersPartnerDomainAccessResponseDefaultType0 | DeleteUsersPartnerDomainAccessResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: PartnerDomainAccessSchema,
) -> (
    Any
    | DeleteUsersPartnerDomainAccessResponseDefaultType0
    | DeleteUsersPartnerDomainAccessResponseDefaultType1
    | None
):
    """Remove customer domain access from all users in a partner domain.

         (Super admins only)

    Args:
        body (PartnerDomainAccessSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteUsersPartnerDomainAccessResponseDefaultType0 | DeleteUsersPartnerDomainAccessResponseDefaultType1
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PartnerDomainAccessSchema,
) -> Response[
    Any
    | DeleteUsersPartnerDomainAccessResponseDefaultType0
    | DeleteUsersPartnerDomainAccessResponseDefaultType1
]:
    """Remove customer domain access from all users in a partner domain.

         (Super admins only)

    Args:
        body (PartnerDomainAccessSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteUsersPartnerDomainAccessResponseDefaultType0 | DeleteUsersPartnerDomainAccessResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PartnerDomainAccessSchema,
) -> (
    Any
    | DeleteUsersPartnerDomainAccessResponseDefaultType0
    | DeleteUsersPartnerDomainAccessResponseDefaultType1
    | None
):
    """Remove customer domain access from all users in a partner domain.

         (Super admins only)

    Args:
        body (PartnerDomainAccessSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteUsersPartnerDomainAccessResponseDefaultType0 | DeleteUsersPartnerDomainAccessResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
