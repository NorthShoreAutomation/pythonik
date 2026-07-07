from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.logs_recipient_read_schema import LogsRecipientReadSchema
from ...models.logs_recipient_schema import LogsRecipientSchema
from ...models.post_system_logs_recipients_response_default_type_0 import (
    PostSystemLogsRecipientsResponseDefaultType0,
)
from ...models.post_system_logs_recipients_response_default_type_1 import (
    PostSystemLogsRecipientsResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    *,
    body: LogsRecipientSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/system/logs/recipients/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | LogsRecipientReadSchema
    | PostSystemLogsRecipientsResponseDefaultType0
    | PostSystemLogsRecipientsResponseDefaultType1
):
    if response.status_code == 201:
        response_201 = LogsRecipientReadSchema.from_dict(response.json())

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
        PostSystemLogsRecipientsResponseDefaultType0
        | PostSystemLogsRecipientsResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                PostSystemLogsRecipientsResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PostSystemLogsRecipientsResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | LogsRecipientReadSchema
    | PostSystemLogsRecipientsResponseDefaultType0
    | PostSystemLogsRecipientsResponseDefaultType1
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
    body: LogsRecipientSchema,
) -> Response[
    Any
    | LogsRecipientReadSchema
    | PostSystemLogsRecipientsResponseDefaultType0
    | PostSystemLogsRecipientsResponseDefaultType1
]:
    """Create logs recipient settings


    Required roles:
     - can_write_logs_recipients

    Args:
        body (LogsRecipientSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | LogsRecipientReadSchema | PostSystemLogsRecipientsResponseDefaultType0 | PostSystemLogsRecipientsResponseDefaultType1]
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
    body: LogsRecipientSchema,
) -> (
    Any
    | LogsRecipientReadSchema
    | PostSystemLogsRecipientsResponseDefaultType0
    | PostSystemLogsRecipientsResponseDefaultType1
    | None
):
    """Create logs recipient settings


    Required roles:
     - can_write_logs_recipients

    Args:
        body (LogsRecipientSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | LogsRecipientReadSchema | PostSystemLogsRecipientsResponseDefaultType0 | PostSystemLogsRecipientsResponseDefaultType1
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: LogsRecipientSchema,
) -> Response[
    Any
    | LogsRecipientReadSchema
    | PostSystemLogsRecipientsResponseDefaultType0
    | PostSystemLogsRecipientsResponseDefaultType1
]:
    """Create logs recipient settings


    Required roles:
     - can_write_logs_recipients

    Args:
        body (LogsRecipientSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | LogsRecipientReadSchema | PostSystemLogsRecipientsResponseDefaultType0 | PostSystemLogsRecipientsResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: LogsRecipientSchema,
) -> (
    Any
    | LogsRecipientReadSchema
    | PostSystemLogsRecipientsResponseDefaultType0
    | PostSystemLogsRecipientsResponseDefaultType1
    | None
):
    """Create logs recipient settings


    Required roles:
     - can_write_logs_recipients

    Args:
        body (LogsRecipientSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | LogsRecipientReadSchema | PostSystemLogsRecipientsResponseDefaultType0 | PostSystemLogsRecipientsResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
