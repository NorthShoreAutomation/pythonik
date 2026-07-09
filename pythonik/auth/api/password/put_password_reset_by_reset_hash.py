from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.put_password_reset_by_reset_hash_response_default import (
    PutPasswordResetByResetHashResponseDefault,
)
from ...models.reset_password_schema import ResetPasswordSchema
from ...types import Response


def _get_kwargs(
    reset_hash: str,
    *,
    body: ResetPasswordSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/password/reset/{reset_hash}/".format(
            reset_hash=quote(str(reset_hash), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PutPasswordResetByResetHashResponseDefault:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 419:
        response_419 = cast(Any, None)
        return response_419

    response_default = PutPasswordResetByResetHashResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PutPasswordResetByResetHashResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    reset_hash: str,
    *,
    client: AuthenticatedClient | Client,
    body: ResetPasswordSchema,
) -> Response[Any | PutPasswordResetByResetHashResponseDefault]:
    """Changes password to a new one

    Args:
        reset_hash (str):
        body (ResetPasswordSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutPasswordResetByResetHashResponseDefault]
    """

    kwargs = _get_kwargs(
        reset_hash=reset_hash,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    reset_hash: str,
    *,
    client: AuthenticatedClient | Client,
    body: ResetPasswordSchema,
) -> Any | PutPasswordResetByResetHashResponseDefault | None:
    """Changes password to a new one

    Args:
        reset_hash (str):
        body (ResetPasswordSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutPasswordResetByResetHashResponseDefault
    """

    return sync_detailed(
        reset_hash=reset_hash,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    reset_hash: str,
    *,
    client: AuthenticatedClient | Client,
    body: ResetPasswordSchema,
) -> Response[Any | PutPasswordResetByResetHashResponseDefault]:
    """Changes password to a new one

    Args:
        reset_hash (str):
        body (ResetPasswordSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutPasswordResetByResetHashResponseDefault]
    """

    kwargs = _get_kwargs(
        reset_hash=reset_hash,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    reset_hash: str,
    *,
    client: AuthenticatedClient | Client,
    body: ResetPasswordSchema,
) -> Any | PutPasswordResetByResetHashResponseDefault | None:
    """Changes password to a new one

    Args:
        reset_hash (str):
        body (ResetPasswordSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutPasswordResetByResetHashResponseDefault
    """

    return (
        await asyncio_detailed(
            reset_hash=reset_hash,
            client=client,
            body=body,
        )
    ).parsed
