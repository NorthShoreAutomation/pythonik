from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.put_users_by_user_id_saml_response_default import (
    PutUsersByUserIdSamlResponseDefault,
)
from ...models.user_saml_idp_update_schema import UserSamlIdpUpdateSchema
from ...models.user_schema import UserSchema
from ...types import Response


def _get_kwargs(
    user_id: str,
    *,
    body: UserSamlIdpUpdateSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/users/{user_id}/saml/".format(
            user_id=quote(str(user_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PutUsersByUserIdSamlResponseDefault | UserSchema:
    if response.status_code == 200:
        response_200 = UserSchema.from_dict(response.json())

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

    response_default = PutUsersByUserIdSamlResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PutUsersByUserIdSamlResponseDefault | UserSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UserSamlIdpUpdateSchema,
) -> Response[Any | PutUsersByUserIdSamlResponseDefault | UserSchema]:
    """Update a user's SAML IdP settings

    Args:
        user_id (str):
        body (UserSamlIdpUpdateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutUsersByUserIdSamlResponseDefault | UserSchema]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UserSamlIdpUpdateSchema,
) -> Any | PutUsersByUserIdSamlResponseDefault | UserSchema | None:
    """Update a user's SAML IdP settings

    Args:
        user_id (str):
        body (UserSamlIdpUpdateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutUsersByUserIdSamlResponseDefault | UserSchema
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UserSamlIdpUpdateSchema,
) -> Response[Any | PutUsersByUserIdSamlResponseDefault | UserSchema]:
    """Update a user's SAML IdP settings

    Args:
        user_id (str):
        body (UserSamlIdpUpdateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutUsersByUserIdSamlResponseDefault | UserSchema]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UserSamlIdpUpdateSchema,
) -> Any | PutUsersByUserIdSamlResponseDefault | UserSchema | None:
    """Update a user's SAML IdP settings

    Args:
        user_id (str):
        body (UserSamlIdpUpdateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutUsersByUserIdSamlResponseDefault | UserSchema
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            body=body,
        )
    ).parsed
