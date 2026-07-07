from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_auth_by_app_id_tokens_response_default_type_0 import (
    GetAuthByAppIdTokensResponseDefaultType0,
)
from ...models.get_auth_by_app_id_tokens_response_default_type_1 import (
    GetAuthByAppIdTokensResponseDefaultType1,
)
from ...models.tokens_schema import TokensSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    app_id: str,
    *,
    per_page: int | Unset = 10,
    last_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["per_page"] = per_page

    params["last_id"] = last_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/auth/{app_id}/tokens/".format(
            app_id=quote(str(app_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetAuthByAppIdTokensResponseDefaultType0
    | GetAuthByAppIdTokensResponseDefaultType1
    | TokensSchema
):
    if response.status_code == 200:
        response_200 = TokensSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    def _parse_response_default(
        data: object,
    ) -> (
        GetAuthByAppIdTokensResponseDefaultType0
        | GetAuthByAppIdTokensResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetAuthByAppIdTokensResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = GetAuthByAppIdTokensResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetAuthByAppIdTokensResponseDefaultType0
    | GetAuthByAppIdTokensResponseDefaultType1
    | TokensSchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    app_id: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = 10,
    last_id: str | Unset = UNSET,
) -> Response[
    Any
    | GetAuthByAppIdTokensResponseDefaultType0
    | GetAuthByAppIdTokensResponseDefaultType1
    | TokensSchema
]:
    """List application tokens

    Args:
        app_id (str):
        per_page (int | Unset):  Default: 10.
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAuthByAppIdTokensResponseDefaultType0 | GetAuthByAppIdTokensResponseDefaultType1 | TokensSchema]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        per_page=per_page,
        last_id=last_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    app_id: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = 10,
    last_id: str | Unset = UNSET,
) -> (
    Any
    | GetAuthByAppIdTokensResponseDefaultType0
    | GetAuthByAppIdTokensResponseDefaultType1
    | TokensSchema
    | None
):
    """List application tokens

    Args:
        app_id (str):
        per_page (int | Unset):  Default: 10.
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAuthByAppIdTokensResponseDefaultType0 | GetAuthByAppIdTokensResponseDefaultType1 | TokensSchema
    """

    return sync_detailed(
        app_id=app_id,
        client=client,
        per_page=per_page,
        last_id=last_id,
    ).parsed


async def asyncio_detailed(
    app_id: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = 10,
    last_id: str | Unset = UNSET,
) -> Response[
    Any
    | GetAuthByAppIdTokensResponseDefaultType0
    | GetAuthByAppIdTokensResponseDefaultType1
    | TokensSchema
]:
    """List application tokens

    Args:
        app_id (str):
        per_page (int | Unset):  Default: 10.
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAuthByAppIdTokensResponseDefaultType0 | GetAuthByAppIdTokensResponseDefaultType1 | TokensSchema]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        per_page=per_page,
        last_id=last_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_id: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = 10,
    last_id: str | Unset = UNSET,
) -> (
    Any
    | GetAuthByAppIdTokensResponseDefaultType0
    | GetAuthByAppIdTokensResponseDefaultType1
    | TokensSchema
    | None
):
    """List application tokens

    Args:
        app_id (str):
        per_page (int | Unset):  Default: 10.
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAuthByAppIdTokensResponseDefaultType0 | GetAuthByAppIdTokensResponseDefaultType1 | TokensSchema
    """

    return (
        await asyncio_detailed(
            app_id=app_id,
            client=client,
            per_page=per_page,
            last_id=last_id,
        )
    ).parsed
