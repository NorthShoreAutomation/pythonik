from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_auth_token_by_token_id_response_default_type_0 import (
    GetAuthTokenByTokenIdResponseDefaultType0,
)
from ...models.get_auth_token_by_token_id_response_default_type_1 import (
    GetAuthTokenByTokenIdResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    token_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/auth/token/{token_id}/".format(
            token_id=quote(str(token_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetAuthTokenByTokenIdResponseDefaultType0
    | GetAuthTokenByTokenIdResponseDefaultType1
):
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    def _parse_response_default(
        data: object,
    ) -> (
        GetAuthTokenByTokenIdResponseDefaultType0
        | GetAuthTokenByTokenIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetAuthTokenByTokenIdResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = GetAuthTokenByTokenIdResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetAuthTokenByTokenIdResponseDefaultType0
    | GetAuthTokenByTokenIdResponseDefaultType1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    token_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetAuthTokenByTokenIdResponseDefaultType0
    | GetAuthTokenByTokenIdResponseDefaultType1
]:
    """Get token by ID

    Args:
        token_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAuthTokenByTokenIdResponseDefaultType0 | GetAuthTokenByTokenIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        token_id=token_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    token_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetAuthTokenByTokenIdResponseDefaultType0
    | GetAuthTokenByTokenIdResponseDefaultType1
    | None
):
    """Get token by ID

    Args:
        token_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAuthTokenByTokenIdResponseDefaultType0 | GetAuthTokenByTokenIdResponseDefaultType1
    """

    return sync_detailed(
        token_id=token_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    token_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetAuthTokenByTokenIdResponseDefaultType0
    | GetAuthTokenByTokenIdResponseDefaultType1
]:
    """Get token by ID

    Args:
        token_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAuthTokenByTokenIdResponseDefaultType0 | GetAuthTokenByTokenIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        token_id=token_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    token_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetAuthTokenByTokenIdResponseDefaultType0
    | GetAuthTokenByTokenIdResponseDefaultType1
    | None
):
    """Get token by ID

    Args:
        token_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAuthTokenByTokenIdResponseDefaultType0 | GetAuthTokenByTokenIdResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            token_id=token_id,
            client=client,
        )
    ).parsed
