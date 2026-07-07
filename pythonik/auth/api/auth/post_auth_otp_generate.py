from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.multi_domain_login_schema import MultiDomainLoginSchema
from ...models.post_auth_otp_generate_response_default_type_0 import (
    PostAuthOtpGenerateResponseDefaultType0,
)
from ...models.post_auth_otp_generate_response_default_type_1 import (
    PostAuthOtpGenerateResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    *,
    body: MultiDomainLoginSchema,
    temp_auth_token: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Temp-Auth-Token"] = temp_auth_token

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/auth/otp/generate/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | PostAuthOtpGenerateResponseDefaultType0
    | PostAuthOtpGenerateResponseDefaultType1
):
    if response.status_code == 201:
        response_201 = cast(Any, None)
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
        PostAuthOtpGenerateResponseDefaultType0
        | PostAuthOtpGenerateResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = PostAuthOtpGenerateResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = PostAuthOtpGenerateResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostAuthOtpGenerateResponseDefaultType0
    | PostAuthOtpGenerateResponseDefaultType1
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
    body: MultiDomainLoginSchema,
    temp_auth_token: str,
) -> Response[
    Any
    | PostAuthOtpGenerateResponseDefaultType0
    | PostAuthOtpGenerateResponseDefaultType1
]:
    """Request OTP code

    Args:
        temp_auth_token (str):
        body (MultiDomainLoginSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostAuthOtpGenerateResponseDefaultType0 | PostAuthOtpGenerateResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        body=body,
        temp_auth_token=temp_auth_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: MultiDomainLoginSchema,
    temp_auth_token: str,
) -> (
    Any
    | PostAuthOtpGenerateResponseDefaultType0
    | PostAuthOtpGenerateResponseDefaultType1
    | None
):
    """Request OTP code

    Args:
        temp_auth_token (str):
        body (MultiDomainLoginSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostAuthOtpGenerateResponseDefaultType0 | PostAuthOtpGenerateResponseDefaultType1
    """

    return sync_detailed(
        client=client,
        body=body,
        temp_auth_token=temp_auth_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: MultiDomainLoginSchema,
    temp_auth_token: str,
) -> Response[
    Any
    | PostAuthOtpGenerateResponseDefaultType0
    | PostAuthOtpGenerateResponseDefaultType1
]:
    """Request OTP code

    Args:
        temp_auth_token (str):
        body (MultiDomainLoginSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostAuthOtpGenerateResponseDefaultType0 | PostAuthOtpGenerateResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        body=body,
        temp_auth_token=temp_auth_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: MultiDomainLoginSchema,
    temp_auth_token: str,
) -> (
    Any
    | PostAuthOtpGenerateResponseDefaultType0
    | PostAuthOtpGenerateResponseDefaultType1
    | None
):
    """Request OTP code

    Args:
        temp_auth_token (str):
        body (MultiDomainLoginSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostAuthOtpGenerateResponseDefaultType0 | PostAuthOtpGenerateResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            temp_auth_token=temp_auth_token,
        )
    ).parsed
