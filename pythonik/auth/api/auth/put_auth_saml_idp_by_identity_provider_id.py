from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.identity_provider_schema import IdentityProviderSchema
from ...models.put_auth_saml_idp_by_identity_provider_id_response_default_type_0 import (
    PutAuthSamlIdpByIdentityProviderIdResponseDefaultType0,
)
from ...models.put_auth_saml_idp_by_identity_provider_id_response_default_type_1 import (
    PutAuthSamlIdpByIdentityProviderIdResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    identity_provider_id: str,
    *,
    body: IdentityProviderSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/auth/saml/idp/{identity_provider_id}/".format(
            identity_provider_id=quote(str(identity_provider_id), safe=""),
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
    | IdentityProviderSchema
    | PutAuthSamlIdpByIdentityProviderIdResponseDefaultType0
    | PutAuthSamlIdpByIdentityProviderIdResponseDefaultType1
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
        PutAuthSamlIdpByIdentityProviderIdResponseDefaultType0
        | PutAuthSamlIdpByIdentityProviderIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                PutAuthSamlIdpByIdentityProviderIdResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PutAuthSamlIdpByIdentityProviderIdResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | IdentityProviderSchema
    | PutAuthSamlIdpByIdentityProviderIdResponseDefaultType0
    | PutAuthSamlIdpByIdentityProviderIdResponseDefaultType1
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
    body: IdentityProviderSchema,
) -> Response[
    Any
    | IdentityProviderSchema
    | PutAuthSamlIdpByIdentityProviderIdResponseDefaultType0
    | PutAuthSamlIdpByIdentityProviderIdResponseDefaultType1
]:
    """Update a particular identity provider by id


    Required roles:
     - can_write_identity_providers

    Args:
        identity_provider_id (str):
        body (IdentityProviderSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | IdentityProviderSchema | PutAuthSamlIdpByIdentityProviderIdResponseDefaultType0 | PutAuthSamlIdpByIdentityProviderIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        identity_provider_id=identity_provider_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    identity_provider_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: IdentityProviderSchema,
) -> (
    Any
    | IdentityProviderSchema
    | PutAuthSamlIdpByIdentityProviderIdResponseDefaultType0
    | PutAuthSamlIdpByIdentityProviderIdResponseDefaultType1
    | None
):
    """Update a particular identity provider by id


    Required roles:
     - can_write_identity_providers

    Args:
        identity_provider_id (str):
        body (IdentityProviderSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | IdentityProviderSchema | PutAuthSamlIdpByIdentityProviderIdResponseDefaultType0 | PutAuthSamlIdpByIdentityProviderIdResponseDefaultType1
    """

    return sync_detailed(
        identity_provider_id=identity_provider_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    identity_provider_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: IdentityProviderSchema,
) -> Response[
    Any
    | IdentityProviderSchema
    | PutAuthSamlIdpByIdentityProviderIdResponseDefaultType0
    | PutAuthSamlIdpByIdentityProviderIdResponseDefaultType1
]:
    """Update a particular identity provider by id


    Required roles:
     - can_write_identity_providers

    Args:
        identity_provider_id (str):
        body (IdentityProviderSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | IdentityProviderSchema | PutAuthSamlIdpByIdentityProviderIdResponseDefaultType0 | PutAuthSamlIdpByIdentityProviderIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        identity_provider_id=identity_provider_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    identity_provider_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: IdentityProviderSchema,
) -> (
    Any
    | IdentityProviderSchema
    | PutAuthSamlIdpByIdentityProviderIdResponseDefaultType0
    | PutAuthSamlIdpByIdentityProviderIdResponseDefaultType1
    | None
):
    """Update a particular identity provider by id


    Required roles:
     - can_write_identity_providers

    Args:
        identity_provider_id (str):
        body (IdentityProviderSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | IdentityProviderSchema | PutAuthSamlIdpByIdentityProviderIdResponseDefaultType0 | PutAuthSamlIdpByIdentityProviderIdResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            identity_provider_id=identity_provider_id,
            client=client,
            body=body,
        )
    ).parsed
