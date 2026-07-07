from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_shares_auth_login_response_default_type_0 import (
    PostSharesAuthLoginResponseDefaultType0,
)
from ...models.post_shares_auth_login_response_default_type_1 import (
    PostSharesAuthLoginResponseDefaultType1,
)
from ...models.share_login_schema import ShareLoginSchema
from ...models.share_token_schema import ShareTokenSchema
from ...types import Response


def _get_kwargs(
    *,
    body: ShareLoginSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/shares/auth/login/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | PostSharesAuthLoginResponseDefaultType0
    | PostSharesAuthLoginResponseDefaultType1
    | ShareTokenSchema
):
    if response.status_code == 200:
        response_200 = ShareTokenSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    def _parse_response_default(
        data: object,
    ) -> (
        PostSharesAuthLoginResponseDefaultType0
        | PostSharesAuthLoginResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = PostSharesAuthLoginResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = PostSharesAuthLoginResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostSharesAuthLoginResponseDefaultType0
    | PostSharesAuthLoginResponseDefaultType1
    | ShareTokenSchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ShareLoginSchema,
) -> Response[
    Any
    | PostSharesAuthLoginResponseDefaultType0
    | PostSharesAuthLoginResponseDefaultType1
    | ShareTokenSchema
]:
    """Login for share

    Args:
        body (ShareLoginSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostSharesAuthLoginResponseDefaultType0 | PostSharesAuthLoginResponseDefaultType1 | ShareTokenSchema]
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
    client: AuthenticatedClient,
    body: ShareLoginSchema,
) -> (
    Any
    | PostSharesAuthLoginResponseDefaultType0
    | PostSharesAuthLoginResponseDefaultType1
    | ShareTokenSchema
    | None
):
    """Login for share

    Args:
        body (ShareLoginSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostSharesAuthLoginResponseDefaultType0 | PostSharesAuthLoginResponseDefaultType1 | ShareTokenSchema
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ShareLoginSchema,
) -> Response[
    Any
    | PostSharesAuthLoginResponseDefaultType0
    | PostSharesAuthLoginResponseDefaultType1
    | ShareTokenSchema
]:
    """Login for share

    Args:
        body (ShareLoginSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostSharesAuthLoginResponseDefaultType0 | PostSharesAuthLoginResponseDefaultType1 | ShareTokenSchema]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ShareLoginSchema,
) -> (
    Any
    | PostSharesAuthLoginResponseDefaultType0
    | PostSharesAuthLoginResponseDefaultType1
    | ShareTokenSchema
    | None
):
    """Login for share

    Args:
        body (ShareLoginSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostSharesAuthLoginResponseDefaultType0 | PostSharesAuthLoginResponseDefaultType1 | ShareTokenSchema
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
