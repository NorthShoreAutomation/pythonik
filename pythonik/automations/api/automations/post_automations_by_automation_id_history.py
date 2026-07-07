from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.automation_history_schema import AutomationHistorySchema
from ...models.post_automations_by_automation_id_history_response_default_type_0 import (
    PostAutomationsByAutomationIdHistoryResponseDefaultType0,
)
from ...models.post_automations_by_automation_id_history_response_default_type_1 import (
    PostAutomationsByAutomationIdHistoryResponseDefaultType1,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    automation_id: str,
    *,
    body: AutomationHistorySchema,
    ttl: int | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["ttl"] = ttl

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/automations/{automation_id}/history/".format(
            automation_id=quote(str(automation_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | AutomationHistorySchema
    | PostAutomationsByAutomationIdHistoryResponseDefaultType0
    | PostAutomationsByAutomationIdHistoryResponseDefaultType1
):
    if response.status_code == 201:
        response_201 = AutomationHistorySchema.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    def _parse_response_default(
        data: object,
    ) -> (
        PostAutomationsByAutomationIdHistoryResponseDefaultType0
        | PostAutomationsByAutomationIdHistoryResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                PostAutomationsByAutomationIdHistoryResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PostAutomationsByAutomationIdHistoryResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | AutomationHistorySchema
    | PostAutomationsByAutomationIdHistoryResponseDefaultType0
    | PostAutomationsByAutomationIdHistoryResponseDefaultType1
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
    body: AutomationHistorySchema,
    ttl: int | Unset = UNSET,
) -> Response[
    Any
    | AutomationHistorySchema
    | PostAutomationsByAutomationIdHistoryResponseDefaultType0
    | PostAutomationsByAutomationIdHistoryResponseDefaultType1
]:
    """Create a new history entity


    Required roles:
     - can_write_automations

    Args:
        automation_id (str):
        ttl (int | Unset):
        body (AutomationHistorySchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AutomationHistorySchema | PostAutomationsByAutomationIdHistoryResponseDefaultType0 | PostAutomationsByAutomationIdHistoryResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        automation_id=automation_id,
        body=body,
        ttl=ttl,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    automation_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AutomationHistorySchema,
    ttl: int | Unset = UNSET,
) -> (
    Any
    | AutomationHistorySchema
    | PostAutomationsByAutomationIdHistoryResponseDefaultType0
    | PostAutomationsByAutomationIdHistoryResponseDefaultType1
    | None
):
    """Create a new history entity


    Required roles:
     - can_write_automations

    Args:
        automation_id (str):
        ttl (int | Unset):
        body (AutomationHistorySchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AutomationHistorySchema | PostAutomationsByAutomationIdHistoryResponseDefaultType0 | PostAutomationsByAutomationIdHistoryResponseDefaultType1
    """

    return sync_detailed(
        automation_id=automation_id,
        client=client,
        body=body,
        ttl=ttl,
    ).parsed


async def asyncio_detailed(
    automation_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AutomationHistorySchema,
    ttl: int | Unset = UNSET,
) -> Response[
    Any
    | AutomationHistorySchema
    | PostAutomationsByAutomationIdHistoryResponseDefaultType0
    | PostAutomationsByAutomationIdHistoryResponseDefaultType1
]:
    """Create a new history entity


    Required roles:
     - can_write_automations

    Args:
        automation_id (str):
        ttl (int | Unset):
        body (AutomationHistorySchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AutomationHistorySchema | PostAutomationsByAutomationIdHistoryResponseDefaultType0 | PostAutomationsByAutomationIdHistoryResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        automation_id=automation_id,
        body=body,
        ttl=ttl,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    automation_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AutomationHistorySchema,
    ttl: int | Unset = UNSET,
) -> (
    Any
    | AutomationHistorySchema
    | PostAutomationsByAutomationIdHistoryResponseDefaultType0
    | PostAutomationsByAutomationIdHistoryResponseDefaultType1
    | None
):
    """Create a new history entity


    Required roles:
     - can_write_automations

    Args:
        automation_id (str):
        ttl (int | Unset):
        body (AutomationHistorySchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AutomationHistorySchema | PostAutomationsByAutomationIdHistoryResponseDefaultType0 | PostAutomationsByAutomationIdHistoryResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            automation_id=automation_id,
            client=client,
            body=body,
            ttl=ttl,
        )
    ).parsed
