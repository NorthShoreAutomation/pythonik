from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_system_logs_recipients_by_logs_recipient_id_response_default import (
    DeleteSystemLogsRecipientsByLogsRecipientIdResponseDefault,
)
from ...types import Response


def _get_kwargs(
    logs_recipient_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/system/logs/recipients/{logs_recipient_id}/".format(
            logs_recipient_id=quote(str(logs_recipient_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DeleteSystemLogsRecipientsByLogsRecipientIdResponseDefault:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = (
        DeleteSystemLogsRecipientsByLogsRecipientIdResponseDefault.from_dict(
            response.json()
        )
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DeleteSystemLogsRecipientsByLogsRecipientIdResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    logs_recipient_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DeleteSystemLogsRecipientsByLogsRecipientIdResponseDefault]:
    """Delete logs recipient settings


    Required roles:
     - can_delete_logs_recipients

    Args:
        logs_recipient_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteSystemLogsRecipientsByLogsRecipientIdResponseDefault]
    """

    kwargs = _get_kwargs(
        logs_recipient_id=logs_recipient_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    logs_recipient_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | DeleteSystemLogsRecipientsByLogsRecipientIdResponseDefault | None:
    """Delete logs recipient settings


    Required roles:
     - can_delete_logs_recipients

    Args:
        logs_recipient_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteSystemLogsRecipientsByLogsRecipientIdResponseDefault
    """

    return sync_detailed(
        logs_recipient_id=logs_recipient_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    logs_recipient_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DeleteSystemLogsRecipientsByLogsRecipientIdResponseDefault]:
    """Delete logs recipient settings


    Required roles:
     - can_delete_logs_recipients

    Args:
        logs_recipient_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteSystemLogsRecipientsByLogsRecipientIdResponseDefault]
    """

    kwargs = _get_kwargs(
        logs_recipient_id=logs_recipient_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    logs_recipient_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | DeleteSystemLogsRecipientsByLogsRecipientIdResponseDefault | None:
    """Delete logs recipient settings


    Required roles:
     - can_delete_logs_recipients

    Args:
        logs_recipient_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteSystemLogsRecipientsByLogsRecipientIdResponseDefault
    """

    return (
        await asyncio_detailed(
            logs_recipient_id=logs_recipient_id,
            client=client,
        )
    ).parsed
