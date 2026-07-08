from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_auth_saml_sso_by_public_id_response_default import (
    GetAuthSamlSsoByPublicIdResponseDefault,
)
from ...types import Response


def _get_kwargs(
    public_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/auth/saml/sso/{public_id}/".format(
            public_id=quote(str(public_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetAuthSamlSsoByPublicIdResponseDefault:
    if response.status_code == 302:
        response_302 = cast(Any, None)
        return response_302

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = GetAuthSamlSsoByPublicIdResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetAuthSamlSsoByPublicIdResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    public_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetAuthSamlSsoByPublicIdResponseDefault]:
    """SAML Single sign-on Service

    Args:
        public_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAuthSamlSsoByPublicIdResponseDefault]
    """

    kwargs = _get_kwargs(
        public_id=public_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    public_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetAuthSamlSsoByPublicIdResponseDefault | None:
    """SAML Single sign-on Service

    Args:
        public_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAuthSamlSsoByPublicIdResponseDefault
    """

    return sync_detailed(
        public_id=public_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    public_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetAuthSamlSsoByPublicIdResponseDefault]:
    """SAML Single sign-on Service

    Args:
        public_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAuthSamlSsoByPublicIdResponseDefault]
    """

    kwargs = _get_kwargs(
        public_id=public_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    public_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetAuthSamlSsoByPublicIdResponseDefault | None:
    """SAML Single sign-on Service

    Args:
        public_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAuthSamlSsoByPublicIdResponseDefault
    """

    return (
        await asyncio_detailed(
            public_id=public_id,
            client=client,
        )
    ).parsed
