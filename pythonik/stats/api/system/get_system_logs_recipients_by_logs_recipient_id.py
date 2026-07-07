from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_system_logs_recipients_by_logs_recipient_id_response_default_type_0 import (
    GetSystemLogsRecipientsByLogsRecipientIdResponseDefaultType0,
)
from ...models.get_system_logs_recipients_by_logs_recipient_id_response_default_type_1 import (
    GetSystemLogsRecipientsByLogsRecipientIdResponseDefaultType1,
)
from ...models.logs_recipient_read_schema import LogsRecipientReadSchema
from ...types import Response


def _get_kwargs(
    logs_recipient_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/system/logs/recipients/{logs_recipient_id}/".format(
            logs_recipient_id=quote(str(logs_recipient_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetSystemLogsRecipientsByLogsRecipientIdResponseDefaultType0
    | GetSystemLogsRecipientsByLogsRecipientIdResponseDefaultType1
    | LogsRecipientReadSchema
):
    if response.status_code == 200:
        response_200 = LogsRecipientReadSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    def _parse_response_default(
        data: object,
    ) -> (
        GetSystemLogsRecipientsByLogsRecipientIdResponseDefaultType0
        | GetSystemLogsRecipientsByLogsRecipientIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetSystemLogsRecipientsByLogsRecipientIdResponseDefaultType0.from_dict(
                    data
                )
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            GetSystemLogsRecipientsByLogsRecipientIdResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetSystemLogsRecipientsByLogsRecipientIdResponseDefaultType0
    | GetSystemLogsRecipientsByLogsRecipientIdResponseDefaultType1
    | LogsRecipientReadSchema
]:
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
) -> Response[
    Any
    | GetSystemLogsRecipientsByLogsRecipientIdResponseDefaultType0
    | GetSystemLogsRecipientsByLogsRecipientIdResponseDefaultType1
    | LogsRecipientReadSchema
]:
    """Get settings of a logs recipient


    Required roles:
     - can_read_logs_recipients

    Args:
        logs_recipient_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSystemLogsRecipientsByLogsRecipientIdResponseDefaultType0 | GetSystemLogsRecipientsByLogsRecipientIdResponseDefaultType1 | LogsRecipientReadSchema]
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
) -> (
    Any
    | GetSystemLogsRecipientsByLogsRecipientIdResponseDefaultType0
    | GetSystemLogsRecipientsByLogsRecipientIdResponseDefaultType1
    | LogsRecipientReadSchema
    | None
):
    """Get settings of a logs recipient


    Required roles:
     - can_read_logs_recipients

    Args:
        logs_recipient_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSystemLogsRecipientsByLogsRecipientIdResponseDefaultType0 | GetSystemLogsRecipientsByLogsRecipientIdResponseDefaultType1 | LogsRecipientReadSchema
    """

    return sync_detailed(
        logs_recipient_id=logs_recipient_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    logs_recipient_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetSystemLogsRecipientsByLogsRecipientIdResponseDefaultType0
    | GetSystemLogsRecipientsByLogsRecipientIdResponseDefaultType1
    | LogsRecipientReadSchema
]:
    """Get settings of a logs recipient


    Required roles:
     - can_read_logs_recipients

    Args:
        logs_recipient_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSystemLogsRecipientsByLogsRecipientIdResponseDefaultType0 | GetSystemLogsRecipientsByLogsRecipientIdResponseDefaultType1 | LogsRecipientReadSchema]
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
) -> (
    Any
    | GetSystemLogsRecipientsByLogsRecipientIdResponseDefaultType0
    | GetSystemLogsRecipientsByLogsRecipientIdResponseDefaultType1
    | LogsRecipientReadSchema
    | None
):
    """Get settings of a logs recipient


    Required roles:
     - can_read_logs_recipients

    Args:
        logs_recipient_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSystemLogsRecipientsByLogsRecipientIdResponseDefaultType0 | GetSystemLogsRecipientsByLogsRecipientIdResponseDefaultType1 | LogsRecipientReadSchema
    """

    return (
        await asyncio_detailed(
            logs_recipient_id=logs_recipient_id,
            client=client,
        )
    ).parsed
