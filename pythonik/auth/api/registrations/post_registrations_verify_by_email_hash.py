from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_registrations_verify_by_email_hash_response_default import (
    PostRegistrationsVerifyByEmailHashResponseDefault,
)
from ...models.verification_response_schema import VerificationResponseSchema
from ...types import Response


def _get_kwargs(
    email_hash: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/registrations/verify/{email_hash}/".format(
            email_hash=quote(str(email_hash), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any | PostRegistrationsVerifyByEmailHashResponseDefault | VerificationResponseSchema
):
    if response.status_code == 201:
        response_201 = VerificationResponseSchema.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = PostRegistrationsVerifyByEmailHashResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | PostRegistrationsVerifyByEmailHashResponseDefault | VerificationResponseSchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    email_hash: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any | PostRegistrationsVerifyByEmailHashResponseDefault | VerificationResponseSchema
]:
    """Verify email address, create system domain from template, and authenticate user

    Args:
        email_hash (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostRegistrationsVerifyByEmailHashResponseDefault | VerificationResponseSchema]
    """

    kwargs = _get_kwargs(
        email_hash=email_hash,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    email_hash: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | PostRegistrationsVerifyByEmailHashResponseDefault
    | VerificationResponseSchema
    | None
):
    """Verify email address, create system domain from template, and authenticate user

    Args:
        email_hash (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostRegistrationsVerifyByEmailHashResponseDefault | VerificationResponseSchema
    """

    return sync_detailed(
        email_hash=email_hash,
        client=client,
    ).parsed


async def asyncio_detailed(
    email_hash: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any | PostRegistrationsVerifyByEmailHashResponseDefault | VerificationResponseSchema
]:
    """Verify email address, create system domain from template, and authenticate user

    Args:
        email_hash (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostRegistrationsVerifyByEmailHashResponseDefault | VerificationResponseSchema]
    """

    kwargs = _get_kwargs(
        email_hash=email_hash,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    email_hash: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | PostRegistrationsVerifyByEmailHashResponseDefault
    | VerificationResponseSchema
    | None
):
    """Verify email address, create system domain from template, and authenticate user

    Args:
        email_hash (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostRegistrationsVerifyByEmailHashResponseDefault | VerificationResponseSchema
    """

    return (
        await asyncio_detailed(
            email_hash=email_hash,
            client=client,
        )
    ).parsed
