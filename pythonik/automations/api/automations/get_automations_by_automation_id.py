from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.automation_schema import AutomationSchema
from ...models.get_automations_by_automation_id_response_default_type_0 import (
    GetAutomationsByAutomationIdResponseDefaultType0,
)
from ...models.get_automations_by_automation_id_response_default_type_1 import (
    GetAutomationsByAutomationIdResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    automation_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/automations/{automation_id}/".format(
            automation_id=quote(str(automation_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | AutomationSchema
    | GetAutomationsByAutomationIdResponseDefaultType0
    | GetAutomationsByAutomationIdResponseDefaultType1
):
    if response.status_code == 200:
        response_200 = AutomationSchema.from_dict(response.json())

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
        GetAutomationsByAutomationIdResponseDefaultType0
        | GetAutomationsByAutomationIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetAutomationsByAutomationIdResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            GetAutomationsByAutomationIdResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | AutomationSchema
    | GetAutomationsByAutomationIdResponseDefaultType0
    | GetAutomationsByAutomationIdResponseDefaultType1
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
    | AutomationSchema
    | GetAutomationsByAutomationIdResponseDefaultType0
    | GetAutomationsByAutomationIdResponseDefaultType1
]:
    """Returns a particular automation by id


    Required roles:
     - can_read_automations

    Args:
        automation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AutomationSchema | GetAutomationsByAutomationIdResponseDefaultType0 | GetAutomationsByAutomationIdResponseDefaultType1]
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
    | AutomationSchema
    | GetAutomationsByAutomationIdResponseDefaultType0
    | GetAutomationsByAutomationIdResponseDefaultType1
    | None
):
    """Returns a particular automation by id


    Required roles:
     - can_read_automations

    Args:
        automation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AutomationSchema | GetAutomationsByAutomationIdResponseDefaultType0 | GetAutomationsByAutomationIdResponseDefaultType1
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
    | AutomationSchema
    | GetAutomationsByAutomationIdResponseDefaultType0
    | GetAutomationsByAutomationIdResponseDefaultType1
]:
    """Returns a particular automation by id


    Required roles:
     - can_read_automations

    Args:
        automation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AutomationSchema | GetAutomationsByAutomationIdResponseDefaultType0 | GetAutomationsByAutomationIdResponseDefaultType1]
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
    | AutomationSchema
    | GetAutomationsByAutomationIdResponseDefaultType0
    | GetAutomationsByAutomationIdResponseDefaultType1
    | None
):
    """Returns a particular automation by id


    Required roles:
     - can_read_automations

    Args:
        automation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AutomationSchema | GetAutomationsByAutomationIdResponseDefaultType0 | GetAutomationsByAutomationIdResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            automation_id=automation_id,
            client=client,
        )
    ).parsed
