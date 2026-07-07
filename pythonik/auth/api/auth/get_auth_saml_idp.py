from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_auth_saml_idp_response_default_type_0 import (
    GetAuthSamlIdpResponseDefaultType0,
)
from ...models.get_auth_saml_idp_response_default_type_1 import (
    GetAuthSamlIdpResponseDefaultType1,
)
from ...models.identity_providers_schema import IdentityProvidersSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    per_page: int | Unset = UNSET,
    last_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["per_page"] = per_page

    params["last_id"] = last_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/auth/saml/idp/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetAuthSamlIdpResponseDefaultType0
    | GetAuthSamlIdpResponseDefaultType1
    | IdentityProvidersSchema
):
    if response.status_code == 200:
        response_200 = IdentityProvidersSchema.from_dict(response.json())

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
    ) -> GetAuthSamlIdpResponseDefaultType0 | GetAuthSamlIdpResponseDefaultType1:
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = GetAuthSamlIdpResponseDefaultType0.from_dict(data)

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = GetAuthSamlIdpResponseDefaultType1.from_dict(data)

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetAuthSamlIdpResponseDefaultType0
    | GetAuthSamlIdpResponseDefaultType1
    | IdentityProvidersSchema
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
    per_page: int | Unset = UNSET,
    last_id: str | Unset = UNSET,
) -> Response[
    Any
    | GetAuthSamlIdpResponseDefaultType0
    | GetAuthSamlIdpResponseDefaultType1
    | IdentityProvidersSchema
]:
    """Get list of identity providers


    Required roles:
     - can_read_identity_providers

    Args:
        per_page (int | Unset):
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAuthSamlIdpResponseDefaultType0 | GetAuthSamlIdpResponseDefaultType1 | IdentityProvidersSchema]
    """

    kwargs = _get_kwargs(
        per_page=per_page,
        last_id=last_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    last_id: str | Unset = UNSET,
) -> (
    Any
    | GetAuthSamlIdpResponseDefaultType0
    | GetAuthSamlIdpResponseDefaultType1
    | IdentityProvidersSchema
    | None
):
    """Get list of identity providers


    Required roles:
     - can_read_identity_providers

    Args:
        per_page (int | Unset):
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAuthSamlIdpResponseDefaultType0 | GetAuthSamlIdpResponseDefaultType1 | IdentityProvidersSchema
    """

    return sync_detailed(
        client=client,
        per_page=per_page,
        last_id=last_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    last_id: str | Unset = UNSET,
) -> Response[
    Any
    | GetAuthSamlIdpResponseDefaultType0
    | GetAuthSamlIdpResponseDefaultType1
    | IdentityProvidersSchema
]:
    """Get list of identity providers


    Required roles:
     - can_read_identity_providers

    Args:
        per_page (int | Unset):
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAuthSamlIdpResponseDefaultType0 | GetAuthSamlIdpResponseDefaultType1 | IdentityProvidersSchema]
    """

    kwargs = _get_kwargs(
        per_page=per_page,
        last_id=last_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    last_id: str | Unset = UNSET,
) -> (
    Any
    | GetAuthSamlIdpResponseDefaultType0
    | GetAuthSamlIdpResponseDefaultType1
    | IdentityProvidersSchema
    | None
):
    """Get list of identity providers


    Required roles:
     - can_read_identity_providers

    Args:
        per_page (int | Unset):
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAuthSamlIdpResponseDefaultType0 | GetAuthSamlIdpResponseDefaultType1 | IdentityProvidersSchema
    """

    return (
        await asyncio_detailed(
            client=client,
            per_page=per_page,
            last_id=last_id,
        )
    ).parsed
