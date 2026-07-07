from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_users_by_user_id_saml_response_default_type_0 import (
    DeleteUsersByUserIdSamlResponseDefaultType0,
)
from ...models.delete_users_by_user_id_saml_response_default_type_1 import (
    DeleteUsersByUserIdSamlResponseDefaultType1,
)
from ...models.user_schema import UserSchema
from ...types import Response


def _get_kwargs(
    user_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/users/{user_id}/saml/".format(
            user_id=quote(str(user_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | DeleteUsersByUserIdSamlResponseDefaultType0
    | DeleteUsersByUserIdSamlResponseDefaultType1
    | UserSchema
):
    if response.status_code == 200:
        response_200 = UserSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    def _parse_response_default(
        data: object,
    ) -> (
        DeleteUsersByUserIdSamlResponseDefaultType0
        | DeleteUsersByUserIdSamlResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                DeleteUsersByUserIdSamlResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = DeleteUsersByUserIdSamlResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | DeleteUsersByUserIdSamlResponseDefaultType0
    | DeleteUsersByUserIdSamlResponseDefaultType1
    | UserSchema
]:
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
) -> Response[
    Any
    | DeleteUsersByUserIdSamlResponseDefaultType0
    | DeleteUsersByUserIdSamlResponseDefaultType1
    | UserSchema
]:
    """Remove a user's SAML IdP setting

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteUsersByUserIdSamlResponseDefaultType0 | DeleteUsersByUserIdSamlResponseDefaultType1 | UserSchema]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | DeleteUsersByUserIdSamlResponseDefaultType0
    | DeleteUsersByUserIdSamlResponseDefaultType1
    | UserSchema
    | None
):
    """Remove a user's SAML IdP setting

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteUsersByUserIdSamlResponseDefaultType0 | DeleteUsersByUserIdSamlResponseDefaultType1 | UserSchema
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | DeleteUsersByUserIdSamlResponseDefaultType0
    | DeleteUsersByUserIdSamlResponseDefaultType1
    | UserSchema
]:
    """Remove a user's SAML IdP setting

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteUsersByUserIdSamlResponseDefaultType0 | DeleteUsersByUserIdSamlResponseDefaultType1 | UserSchema]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | DeleteUsersByUserIdSamlResponseDefaultType0
    | DeleteUsersByUserIdSamlResponseDefaultType1
    | UserSchema
    | None
):
    """Remove a user's SAML IdP setting

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteUsersByUserIdSamlResponseDefaultType0 | DeleteUsersByUserIdSamlResponseDefaultType1 | UserSchema
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
        )
    ).parsed
