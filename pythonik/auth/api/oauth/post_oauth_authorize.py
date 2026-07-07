from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.o_auth_2_authorize_response_schema import OAuth2AuthorizeResponseSchema
from ...models.post_oauth_authorize_response_default_type_0 import (
    PostOauthAuthorizeResponseDefaultType0,
)
from ...models.post_oauth_authorize_response_default_type_1 import (
    PostOauthAuthorizeResponseDefaultType1,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client_id: str,
    redirect_uri: str,
    scope: str,
    response_type: str,
    code_challenge: str,
    code_challenge_method: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["client_id"] = client_id

    params["redirect_uri"] = redirect_uri

    params["scope"] = scope

    params["response_type"] = response_type

    params["code_challenge"] = code_challenge

    params["code_challenge_method"] = code_challenge_method

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/oauth/authorize/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | OAuth2AuthorizeResponseSchema
    | PostOauthAuthorizeResponseDefaultType0
    | PostOauthAuthorizeResponseDefaultType1
):
    if response.status_code == 200:
        response_200 = OAuth2AuthorizeResponseSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    def _parse_response_default(
        data: object,
    ) -> (
        PostOauthAuthorizeResponseDefaultType0 | PostOauthAuthorizeResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = PostOauthAuthorizeResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = PostOauthAuthorizeResponseDefaultType1.from_dict(data)

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | OAuth2AuthorizeResponseSchema
    | PostOauthAuthorizeResponseDefaultType0
    | PostOauthAuthorizeResponseDefaultType1
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
    client_id: str,
    redirect_uri: str,
    scope: str,
    response_type: str,
    code_challenge: str,
    code_challenge_method: str | Unset = UNSET,
) -> Response[
    Any
    | OAuth2AuthorizeResponseSchema
    | PostOauthAuthorizeResponseDefaultType0
    | PostOauthAuthorizeResponseDefaultType1
]:
    """Submit the user's consent decision. If ``confirm`` is present in

     the form body the authorization code is minted; otherwise the<br/>request is denied
    (``error=access_denied``).

    Args:
        client_id (str):
        redirect_uri (str):
        scope (str):
        response_type (str):
        code_challenge (str):
        code_challenge_method (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | OAuth2AuthorizeResponseSchema | PostOauthAuthorizeResponseDefaultType0 | PostOauthAuthorizeResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        client_id=client_id,
        redirect_uri=redirect_uri,
        scope=scope,
        response_type=response_type,
        code_challenge=code_challenge,
        code_challenge_method=code_challenge_method,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    client_id: str,
    redirect_uri: str,
    scope: str,
    response_type: str,
    code_challenge: str,
    code_challenge_method: str | Unset = UNSET,
) -> (
    Any
    | OAuth2AuthorizeResponseSchema
    | PostOauthAuthorizeResponseDefaultType0
    | PostOauthAuthorizeResponseDefaultType1
    | None
):
    """Submit the user's consent decision. If ``confirm`` is present in

     the form body the authorization code is minted; otherwise the<br/>request is denied
    (``error=access_denied``).

    Args:
        client_id (str):
        redirect_uri (str):
        scope (str):
        response_type (str):
        code_challenge (str):
        code_challenge_method (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | OAuth2AuthorizeResponseSchema | PostOauthAuthorizeResponseDefaultType0 | PostOauthAuthorizeResponseDefaultType1
    """

    return sync_detailed(
        client=client,
        client_id=client_id,
        redirect_uri=redirect_uri,
        scope=scope,
        response_type=response_type,
        code_challenge=code_challenge,
        code_challenge_method=code_challenge_method,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    client_id: str,
    redirect_uri: str,
    scope: str,
    response_type: str,
    code_challenge: str,
    code_challenge_method: str | Unset = UNSET,
) -> Response[
    Any
    | OAuth2AuthorizeResponseSchema
    | PostOauthAuthorizeResponseDefaultType0
    | PostOauthAuthorizeResponseDefaultType1
]:
    """Submit the user's consent decision. If ``confirm`` is present in

     the form body the authorization code is minted; otherwise the<br/>request is denied
    (``error=access_denied``).

    Args:
        client_id (str):
        redirect_uri (str):
        scope (str):
        response_type (str):
        code_challenge (str):
        code_challenge_method (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | OAuth2AuthorizeResponseSchema | PostOauthAuthorizeResponseDefaultType0 | PostOauthAuthorizeResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        client_id=client_id,
        redirect_uri=redirect_uri,
        scope=scope,
        response_type=response_type,
        code_challenge=code_challenge,
        code_challenge_method=code_challenge_method,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    client_id: str,
    redirect_uri: str,
    scope: str,
    response_type: str,
    code_challenge: str,
    code_challenge_method: str | Unset = UNSET,
) -> (
    Any
    | OAuth2AuthorizeResponseSchema
    | PostOauthAuthorizeResponseDefaultType0
    | PostOauthAuthorizeResponseDefaultType1
    | None
):
    """Submit the user's consent decision. If ``confirm`` is present in

     the form body the authorization code is minted; otherwise the<br/>request is denied
    (``error=access_denied``).

    Args:
        client_id (str):
        redirect_uri (str):
        scope (str):
        response_type (str):
        code_challenge (str):
        code_challenge_method (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | OAuth2AuthorizeResponseSchema | PostOauthAuthorizeResponseDefaultType0 | PostOauthAuthorizeResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            client=client,
            client_id=client_id,
            redirect_uri=redirect_uri,
            scope=scope,
            response_type=response_type,
            code_challenge=code_challenge,
            code_challenge_method=code_challenge_method,
        )
    ).parsed
