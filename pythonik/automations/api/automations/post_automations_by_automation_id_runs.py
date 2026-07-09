from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_automations_by_automation_id_runs_response_default import (
    PostAutomationsByAutomationIdRunsResponseDefault,
)
from ...types import Response


def _get_kwargs(
    automation_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/automations/{automation_id}/runs/".format(
            automation_id=quote(str(automation_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostAutomationsByAutomationIdRunsResponseDefault:
    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = PostAutomationsByAutomationIdRunsResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PostAutomationsByAutomationIdRunsResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    automation_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | PostAutomationsByAutomationIdRunsResponseDefault]:
    """Run an automation for existing objects


    Required roles:
     - can_run_automations

    Args:
        automation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostAutomationsByAutomationIdRunsResponseDefault]
    """

    kwargs = _get_kwargs(
        automation_id=automation_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    automation_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | PostAutomationsByAutomationIdRunsResponseDefault | None:
    """Run an automation for existing objects


    Required roles:
     - can_run_automations

    Args:
        automation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostAutomationsByAutomationIdRunsResponseDefault
    """

    return sync_detailed(
        automation_id=automation_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    automation_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | PostAutomationsByAutomationIdRunsResponseDefault]:
    """Run an automation for existing objects


    Required roles:
     - can_run_automations

    Args:
        automation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostAutomationsByAutomationIdRunsResponseDefault]
    """

    kwargs = _get_kwargs(
        automation_id=automation_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    automation_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | PostAutomationsByAutomationIdRunsResponseDefault | None:
    """Run an automation for existing objects


    Required roles:
     - can_run_automations

    Args:
        automation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostAutomationsByAutomationIdRunsResponseDefault
    """

    return (
        await asyncio_detailed(
            automation_id=automation_id,
            client=client,
        )
    ).parsed
