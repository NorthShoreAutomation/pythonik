from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.automation_run_estimate_schema import AutomationRunEstimateSchema
from ...models.get_automations_by_automation_id_runs_estimate_response_default import (
    GetAutomationsByAutomationIdRunsEstimateResponseDefault,
)
from ...types import Response


def _get_kwargs(
    automation_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/automations/{automation_id}/runs/estimate/".format(
            automation_id=quote(str(automation_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | AutomationRunEstimateSchema
    | GetAutomationsByAutomationIdRunsEstimateResponseDefault
):
    if response.status_code == 200:
        response_200 = AutomationRunEstimateSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = (
        GetAutomationsByAutomationIdRunsEstimateResponseDefault.from_dict(
            response.json()
        )
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | AutomationRunEstimateSchema
    | GetAutomationsByAutomationIdRunsEstimateResponseDefault
]:
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
) -> Response[
    Any
    | AutomationRunEstimateSchema
    | GetAutomationsByAutomationIdRunsEstimateResponseDefault
]:
    """Get estimated number objects that might be affected by an automation run


    Required roles:
     - can_run_automations

    Args:
        automation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AutomationRunEstimateSchema | GetAutomationsByAutomationIdRunsEstimateResponseDefault]
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
) -> (
    Any
    | AutomationRunEstimateSchema
    | GetAutomationsByAutomationIdRunsEstimateResponseDefault
    | None
):
    """Get estimated number objects that might be affected by an automation run


    Required roles:
     - can_run_automations

    Args:
        automation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AutomationRunEstimateSchema | GetAutomationsByAutomationIdRunsEstimateResponseDefault
    """

    return sync_detailed(
        automation_id=automation_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    automation_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | AutomationRunEstimateSchema
    | GetAutomationsByAutomationIdRunsEstimateResponseDefault
]:
    """Get estimated number objects that might be affected by an automation run


    Required roles:
     - can_run_automations

    Args:
        automation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AutomationRunEstimateSchema | GetAutomationsByAutomationIdRunsEstimateResponseDefault]
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
) -> (
    Any
    | AutomationRunEstimateSchema
    | GetAutomationsByAutomationIdRunsEstimateResponseDefault
    | None
):
    """Get estimated number objects that might be affected by an automation run


    Required roles:
     - can_run_automations

    Args:
        automation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AutomationRunEstimateSchema | GetAutomationsByAutomationIdRunsEstimateResponseDefault
    """

    return (
        await asyncio_detailed(
            automation_id=automation_id,
            client=client,
        )
    ).parsed
