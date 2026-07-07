from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_system_logs_recipients_by_logs_recipient_id_response_200 import (
    PostSystemLogsRecipientsByLogsRecipientIdResponse200,
)
from ...models.post_system_logs_recipients_by_logs_recipient_id_response_default_type_0 import (
    PostSystemLogsRecipientsByLogsRecipientIdResponseDefaultType0,
)
from ...models.post_system_logs_recipients_by_logs_recipient_id_response_default_type_1 import (
    PostSystemLogsRecipientsByLogsRecipientIdResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    logs_recipient_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/system/logs/recipients/{logs_recipient_id}/".format(
            logs_recipient_id=quote(str(logs_recipient_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | PostSystemLogsRecipientsByLogsRecipientIdResponse200
    | PostSystemLogsRecipientsByLogsRecipientIdResponseDefaultType0
    | PostSystemLogsRecipientsByLogsRecipientIdResponseDefaultType1
):
    if response.status_code == 200:
        response_200 = PostSystemLogsRecipientsByLogsRecipientIdResponse200.from_dict(
            response.json()
        )

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
        PostSystemLogsRecipientsByLogsRecipientIdResponseDefaultType0
        | PostSystemLogsRecipientsByLogsRecipientIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                PostSystemLogsRecipientsByLogsRecipientIdResponseDefaultType0.from_dict(
                    data
                )
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PostSystemLogsRecipientsByLogsRecipientIdResponseDefaultType1.from_dict(
                data
            )
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostSystemLogsRecipientsByLogsRecipientIdResponse200
    | PostSystemLogsRecipientsByLogsRecipientIdResponseDefaultType0
    | PostSystemLogsRecipientsByLogsRecipientIdResponseDefaultType1
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
    | PostSystemLogsRecipientsByLogsRecipientIdResponse200
    | PostSystemLogsRecipientsByLogsRecipientIdResponseDefaultType0
    | PostSystemLogsRecipientsByLogsRecipientIdResponseDefaultType1
]:
    """Test logs recipient connection


    Required roles:
     - can_write_logs_recipients

    Args:
        logs_recipient_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostSystemLogsRecipientsByLogsRecipientIdResponse200 | PostSystemLogsRecipientsByLogsRecipientIdResponseDefaultType0 | PostSystemLogsRecipientsByLogsRecipientIdResponseDefaultType1]
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
    | PostSystemLogsRecipientsByLogsRecipientIdResponse200
    | PostSystemLogsRecipientsByLogsRecipientIdResponseDefaultType0
    | PostSystemLogsRecipientsByLogsRecipientIdResponseDefaultType1
    | None
):
    """Test logs recipient connection


    Required roles:
     - can_write_logs_recipients

    Args:
        logs_recipient_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostSystemLogsRecipientsByLogsRecipientIdResponse200 | PostSystemLogsRecipientsByLogsRecipientIdResponseDefaultType0 | PostSystemLogsRecipientsByLogsRecipientIdResponseDefaultType1
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
    | PostSystemLogsRecipientsByLogsRecipientIdResponse200
    | PostSystemLogsRecipientsByLogsRecipientIdResponseDefaultType0
    | PostSystemLogsRecipientsByLogsRecipientIdResponseDefaultType1
]:
    """Test logs recipient connection


    Required roles:
     - can_write_logs_recipients

    Args:
        logs_recipient_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostSystemLogsRecipientsByLogsRecipientIdResponse200 | PostSystemLogsRecipientsByLogsRecipientIdResponseDefaultType0 | PostSystemLogsRecipientsByLogsRecipientIdResponseDefaultType1]
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
    | PostSystemLogsRecipientsByLogsRecipientIdResponse200
    | PostSystemLogsRecipientsByLogsRecipientIdResponseDefaultType0
    | PostSystemLogsRecipientsByLogsRecipientIdResponseDefaultType1
    | None
):
    """Test logs recipient connection


    Required roles:
     - can_write_logs_recipients

    Args:
        logs_recipient_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostSystemLogsRecipientsByLogsRecipientIdResponse200 | PostSystemLogsRecipientsByLogsRecipientIdResponseDefaultType0 | PostSystemLogsRecipientsByLogsRecipientIdResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            logs_recipient_id=logs_recipient_id,
            client=client,
        )
    ).parsed
