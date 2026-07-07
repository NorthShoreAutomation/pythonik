from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_auth_ad_login_body import PostAuthAdLoginBody
from ...models.post_auth_ad_login_response_default_type_0 import (
    PostAuthAdLoginResponseDefaultType0,
)
from ...models.post_auth_ad_login_response_default_type_1 import (
    PostAuthAdLoginResponseDefaultType1,
)
from ...models.token_schema import TokenSchema
from ...types import Response


def _get_kwargs(
    *,
    body: PostAuthAdLoginBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/auth/ad/login/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | PostAuthAdLoginResponseDefaultType0
    | PostAuthAdLoginResponseDefaultType1
    | TokenSchema
):
    if response.status_code == 201:
        response_201 = TokenSchema.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    def _parse_response_default(
        data: object,
    ) -> PostAuthAdLoginResponseDefaultType0 | PostAuthAdLoginResponseDefaultType1:
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = PostAuthAdLoginResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = PostAuthAdLoginResponseDefaultType1.from_dict(data)

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostAuthAdLoginResponseDefaultType0
    | PostAuthAdLoginResponseDefaultType1
    | TokenSchema
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
    body: PostAuthAdLoginBody,
) -> Response[
    Any
    | PostAuthAdLoginResponseDefaultType0
    | PostAuthAdLoginResponseDefaultType1
    | TokenSchema
]:
    """Login by ActiveDirectory

     <br/>This function is not yet implemented.

    Args:
        body (PostAuthAdLoginBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostAuthAdLoginResponseDefaultType0 | PostAuthAdLoginResponseDefaultType1 | TokenSchema]
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
    body: PostAuthAdLoginBody,
) -> (
    Any
    | PostAuthAdLoginResponseDefaultType0
    | PostAuthAdLoginResponseDefaultType1
    | TokenSchema
    | None
):
    """Login by ActiveDirectory

     <br/>This function is not yet implemented.

    Args:
        body (PostAuthAdLoginBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostAuthAdLoginResponseDefaultType0 | PostAuthAdLoginResponseDefaultType1 | TokenSchema
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostAuthAdLoginBody,
) -> Response[
    Any
    | PostAuthAdLoginResponseDefaultType0
    | PostAuthAdLoginResponseDefaultType1
    | TokenSchema
]:
    """Login by ActiveDirectory

     <br/>This function is not yet implemented.

    Args:
        body (PostAuthAdLoginBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostAuthAdLoginResponseDefaultType0 | PostAuthAdLoginResponseDefaultType1 | TokenSchema]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostAuthAdLoginBody,
) -> (
    Any
    | PostAuthAdLoginResponseDefaultType0
    | PostAuthAdLoginResponseDefaultType1
    | TokenSchema
    | None
):
    """Login by ActiveDirectory

     <br/>This function is not yet implemented.

    Args:
        body (PostAuthAdLoginBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostAuthAdLoginResponseDefaultType0 | PostAuthAdLoginResponseDefaultType1 | TokenSchema
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
