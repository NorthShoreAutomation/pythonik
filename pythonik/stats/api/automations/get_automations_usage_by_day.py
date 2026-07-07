from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.automation_runs_schema import AutomationRunsSchema
from ...models.get_automations_usage_by_day_response_default_type_0 import (
    GetAutomationsUsageByDayResponseDefaultType0,
)
from ...models.get_automations_usage_by_day_response_default_type_1 import (
    GetAutomationsUsageByDayResponseDefaultType1,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    from_date: str | Unset = UNSET,
    to_date: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["from_date"] = from_date

    params["to_date"] = to_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/automations/usage/by/day/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | AutomationRunsSchema
    | GetAutomationsUsageByDayResponseDefaultType0
    | GetAutomationsUsageByDayResponseDefaultType1
):
    if response.status_code == 200:
        response_200 = AutomationRunsSchema.from_dict(response.json())

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

    def _parse_response_default(
        data: object,
    ) -> (
        GetAutomationsUsageByDayResponseDefaultType0
        | GetAutomationsUsageByDayResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetAutomationsUsageByDayResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            GetAutomationsUsageByDayResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | AutomationRunsSchema
    | GetAutomationsUsageByDayResponseDefaultType0
    | GetAutomationsUsageByDayResponseDefaultType1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    from_date: str | Unset = UNSET,
    to_date: str | Unset = UNSET,
) -> Response[
    Any
    | AutomationRunsSchema
    | GetAutomationsUsageByDayResponseDefaultType0
    | GetAutomationsUsageByDayResponseDefaultType1
]:
    """Returns automation runs by day.


    Required roles:
     - can_read_stats

    Args:
        from_date (str | Unset):
        to_date (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AutomationRunsSchema | GetAutomationsUsageByDayResponseDefaultType0 | GetAutomationsUsageByDayResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        from_date=from_date,
        to_date=to_date,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    from_date: str | Unset = UNSET,
    to_date: str | Unset = UNSET,
) -> (
    Any
    | AutomationRunsSchema
    | GetAutomationsUsageByDayResponseDefaultType0
    | GetAutomationsUsageByDayResponseDefaultType1
    | None
):
    """Returns automation runs by day.


    Required roles:
     - can_read_stats

    Args:
        from_date (str | Unset):
        to_date (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AutomationRunsSchema | GetAutomationsUsageByDayResponseDefaultType0 | GetAutomationsUsageByDayResponseDefaultType1
    """

    return sync_detailed(
        client=client,
        from_date=from_date,
        to_date=to_date,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    from_date: str | Unset = UNSET,
    to_date: str | Unset = UNSET,
) -> Response[
    Any
    | AutomationRunsSchema
    | GetAutomationsUsageByDayResponseDefaultType0
    | GetAutomationsUsageByDayResponseDefaultType1
]:
    """Returns automation runs by day.


    Required roles:
     - can_read_stats

    Args:
        from_date (str | Unset):
        to_date (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AutomationRunsSchema | GetAutomationsUsageByDayResponseDefaultType0 | GetAutomationsUsageByDayResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        from_date=from_date,
        to_date=to_date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    from_date: str | Unset = UNSET,
    to_date: str | Unset = UNSET,
) -> (
    Any
    | AutomationRunsSchema
    | GetAutomationsUsageByDayResponseDefaultType0
    | GetAutomationsUsageByDayResponseDefaultType1
    | None
):
    """Returns automation runs by day.


    Required roles:
     - can_read_stats

    Args:
        from_date (str | Unset):
        to_date (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AutomationRunsSchema | GetAutomationsUsageByDayResponseDefaultType0 | GetAutomationsUsageByDayResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            client=client,
            from_date=from_date,
            to_date=to_date,
        )
    ).parsed
