from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.put_system_current_response_default import (
    PutSystemCurrentResponseDefault,
)
from ...models.system_setting_public_schema import SystemSettingPublicSchema
from ...types import Response


def _get_kwargs(
    *,
    body: SystemSettingPublicSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/system/current/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PutSystemCurrentResponseDefault | SystemSettingPublicSchema:
    if response.status_code == 200:
        response_200 = SystemSettingPublicSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = PutSystemCurrentResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PutSystemCurrentResponseDefault | SystemSettingPublicSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SystemSettingPublicSchema,
) -> Response[Any | PutSystemCurrentResponseDefault | SystemSettingPublicSchema]:
    """Change system settings

    Args:
        body (SystemSettingPublicSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutSystemCurrentResponseDefault | SystemSettingPublicSchema]
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
    body: SystemSettingPublicSchema,
) -> Any | PutSystemCurrentResponseDefault | SystemSettingPublicSchema | None:
    """Change system settings

    Args:
        body (SystemSettingPublicSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutSystemCurrentResponseDefault | SystemSettingPublicSchema
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SystemSettingPublicSchema,
) -> Response[Any | PutSystemCurrentResponseDefault | SystemSettingPublicSchema]:
    """Change system settings

    Args:
        body (SystemSettingPublicSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutSystemCurrentResponseDefault | SystemSettingPublicSchema]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SystemSettingPublicSchema,
) -> Any | PutSystemCurrentResponseDefault | SystemSettingPublicSchema | None:
    """Change system settings

    Args:
        body (SystemSettingPublicSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutSystemCurrentResponseDefault | SystemSettingPublicSchema
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
