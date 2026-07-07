from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_password_by_reset_hash_checks_response_default_type_0 import (
    GetPasswordByResetHashChecksResponseDefaultType0,
)
from ...models.get_password_by_reset_hash_checks_response_default_type_1 import (
    GetPasswordByResetHashChecksResponseDefaultType1,
)
from ...models.password_checks_schema import PasswordChecksSchema
from ...types import Response


def _get_kwargs(
    reset_hash: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/password/{reset_hash}/checks/".format(
            reset_hash=quote(str(reset_hash), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetPasswordByResetHashChecksResponseDefaultType0
    | GetPasswordByResetHashChecksResponseDefaultType1
    | PasswordChecksSchema
):
    if response.status_code == 200:
        response_200 = PasswordChecksSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 419:
        response_419 = cast(Any, None)
        return response_419

    def _parse_response_default(
        data: object,
    ) -> (
        GetPasswordByResetHashChecksResponseDefaultType0
        | GetPasswordByResetHashChecksResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetPasswordByResetHashChecksResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            GetPasswordByResetHashChecksResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetPasswordByResetHashChecksResponseDefaultType0
    | GetPasswordByResetHashChecksResponseDefaultType1
    | PasswordChecksSchema
]:
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
) -> Response[
    Any
    | GetPasswordByResetHashChecksResponseDefaultType0
    | GetPasswordByResetHashChecksResponseDefaultType1
    | PasswordChecksSchema
]:
    """Returns a list of password checks required for the password to be safe

    Args:
        reset_hash (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetPasswordByResetHashChecksResponseDefaultType0 | GetPasswordByResetHashChecksResponseDefaultType1 | PasswordChecksSchema]
    """

    kwargs = _get_kwargs(
        reset_hash=reset_hash,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    reset_hash: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetPasswordByResetHashChecksResponseDefaultType0
    | GetPasswordByResetHashChecksResponseDefaultType1
    | PasswordChecksSchema
    | None
):
    """Returns a list of password checks required for the password to be safe

    Args:
        reset_hash (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetPasswordByResetHashChecksResponseDefaultType0 | GetPasswordByResetHashChecksResponseDefaultType1 | PasswordChecksSchema
    """

    return sync_detailed(
        reset_hash=reset_hash,
        client=client,
    ).parsed


async def asyncio_detailed(
    reset_hash: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetPasswordByResetHashChecksResponseDefaultType0
    | GetPasswordByResetHashChecksResponseDefaultType1
    | PasswordChecksSchema
]:
    """Returns a list of password checks required for the password to be safe

    Args:
        reset_hash (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetPasswordByResetHashChecksResponseDefaultType0 | GetPasswordByResetHashChecksResponseDefaultType1 | PasswordChecksSchema]
    """

    kwargs = _get_kwargs(
        reset_hash=reset_hash,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    reset_hash: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetPasswordByResetHashChecksResponseDefaultType0
    | GetPasswordByResetHashChecksResponseDefaultType1
    | PasswordChecksSchema
    | None
):
    """Returns a list of password checks required for the password to be safe

    Args:
        reset_hash (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetPasswordByResetHashChecksResponseDefaultType0 | GetPasswordByResetHashChecksResponseDefaultType1 | PasswordChecksSchema
    """

    return (
        await asyncio_detailed(
            reset_hash=reset_hash,
            client=client,
        )
    ).parsed
