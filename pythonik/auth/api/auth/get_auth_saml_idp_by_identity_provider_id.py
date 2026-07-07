from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_auth_saml_idp_by_identity_provider_id_response_default_type_0 import (
    GetAuthSamlIdpByIdentityProviderIdResponseDefaultType0,
)
from ...models.get_auth_saml_idp_by_identity_provider_id_response_default_type_1 import (
    GetAuthSamlIdpByIdentityProviderIdResponseDefaultType1,
)
from ...models.identity_provider_schema import IdentityProviderSchema
from ...types import Response


def _get_kwargs(
    identity_provider_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/auth/saml/idp/{identity_provider_id}/".format(
            identity_provider_id=quote(str(identity_provider_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetAuthSamlIdpByIdentityProviderIdResponseDefaultType0
    | GetAuthSamlIdpByIdentityProviderIdResponseDefaultType1
    | IdentityProviderSchema
):
    if response.status_code == 200:
        response_200 = IdentityProviderSchema.from_dict(response.json())

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
        GetAuthSamlIdpByIdentityProviderIdResponseDefaultType0
        | GetAuthSamlIdpByIdentityProviderIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetAuthSamlIdpByIdentityProviderIdResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            GetAuthSamlIdpByIdentityProviderIdResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetAuthSamlIdpByIdentityProviderIdResponseDefaultType0
    | GetAuthSamlIdpByIdentityProviderIdResponseDefaultType1
    | IdentityProviderSchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    identity_provider_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetAuthSamlIdpByIdentityProviderIdResponseDefaultType0
    | GetAuthSamlIdpByIdentityProviderIdResponseDefaultType1
    | IdentityProviderSchema
]:
    """Get a particular identity provider by id


    Required roles:
     - can_read_identity_providers

    Args:
        identity_provider_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAuthSamlIdpByIdentityProviderIdResponseDefaultType0 | GetAuthSamlIdpByIdentityProviderIdResponseDefaultType1 | IdentityProviderSchema]
    """

    kwargs = _get_kwargs(
        identity_provider_id=identity_provider_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    identity_provider_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetAuthSamlIdpByIdentityProviderIdResponseDefaultType0
    | GetAuthSamlIdpByIdentityProviderIdResponseDefaultType1
    | IdentityProviderSchema
    | None
):
    """Get a particular identity provider by id


    Required roles:
     - can_read_identity_providers

    Args:
        identity_provider_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAuthSamlIdpByIdentityProviderIdResponseDefaultType0 | GetAuthSamlIdpByIdentityProviderIdResponseDefaultType1 | IdentityProviderSchema
    """

    return sync_detailed(
        identity_provider_id=identity_provider_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    identity_provider_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetAuthSamlIdpByIdentityProviderIdResponseDefaultType0
    | GetAuthSamlIdpByIdentityProviderIdResponseDefaultType1
    | IdentityProviderSchema
]:
    """Get a particular identity provider by id


    Required roles:
     - can_read_identity_providers

    Args:
        identity_provider_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAuthSamlIdpByIdentityProviderIdResponseDefaultType0 | GetAuthSamlIdpByIdentityProviderIdResponseDefaultType1 | IdentityProviderSchema]
    """

    kwargs = _get_kwargs(
        identity_provider_id=identity_provider_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    identity_provider_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetAuthSamlIdpByIdentityProviderIdResponseDefaultType0
    | GetAuthSamlIdpByIdentityProviderIdResponseDefaultType1
    | IdentityProviderSchema
    | None
):
    """Get a particular identity provider by id


    Required roles:
     - can_read_identity_providers

    Args:
        identity_provider_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAuthSamlIdpByIdentityProviderIdResponseDefaultType0 | GetAuthSamlIdpByIdentityProviderIdResponseDefaultType1 | IdentityProviderSchema
    """

    return (
        await asyncio_detailed(
            identity_provider_id=identity_provider_id,
            client=client,
        )
    ).parsed
