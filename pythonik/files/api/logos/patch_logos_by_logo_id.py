from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.logo_schema import LogoSchema
from ...models.patch_logos_by_logo_id_response_default import (
    PatchLogosByLogoIdResponseDefault,
)
from ...types import Response


def _get_kwargs(
    logo_id: str,
    *,
    body: LogoSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/logos/{logo_id}/".format(
            logo_id=quote(str(logo_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | LogoSchema | PatchLogosByLogoIdResponseDefault:
    if response.status_code == 200:
        response_200 = LogoSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = PatchLogosByLogoIdResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | LogoSchema | PatchLogosByLogoIdResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    logo_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: LogoSchema,
) -> Response[Any | LogoSchema | PatchLogosByLogoIdResponseDefault]:
    """Rename a saved logo

     <br/>Only the name can be changed; the image itself is immutable.<br/>Only the name can be changed;
    the image itself is immutable.
    Required roles:
     - can_write_portals

    Args:
        logo_id (str):
        body (LogoSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | LogoSchema | PatchLogosByLogoIdResponseDefault]
    """

    kwargs = _get_kwargs(
        logo_id=logo_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    logo_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: LogoSchema,
) -> Any | LogoSchema | PatchLogosByLogoIdResponseDefault | None:
    """Rename a saved logo

     <br/>Only the name can be changed; the image itself is immutable.<br/>Only the name can be changed;
    the image itself is immutable.
    Required roles:
     - can_write_portals

    Args:
        logo_id (str):
        body (LogoSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | LogoSchema | PatchLogosByLogoIdResponseDefault
    """

    return sync_detailed(
        logo_id=logo_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    logo_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: LogoSchema,
) -> Response[Any | LogoSchema | PatchLogosByLogoIdResponseDefault]:
    """Rename a saved logo

     <br/>Only the name can be changed; the image itself is immutable.<br/>Only the name can be changed;
    the image itself is immutable.
    Required roles:
     - can_write_portals

    Args:
        logo_id (str):
        body (LogoSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | LogoSchema | PatchLogosByLogoIdResponseDefault]
    """

    kwargs = _get_kwargs(
        logo_id=logo_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    logo_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: LogoSchema,
) -> Any | LogoSchema | PatchLogosByLogoIdResponseDefault | None:
    """Rename a saved logo

     <br/>Only the name can be changed; the image itself is immutable.<br/>Only the name can be changed;
    the image itself is immutable.
    Required roles:
     - can_write_portals

    Args:
        logo_id (str):
        body (LogoSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | LogoSchema | PatchLogosByLogoIdResponseDefault
    """

    return (
        await asyncio_detailed(
            logo_id=logo_id,
            client=client,
            body=body,
        )
    ).parsed
