from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_automations_by_automation_id_history_by_object_type_by_object_id_by_version_id_response_default import (
    DeleteAutomationsByAutomationIdHistoryByObjectTypeByObjectIdByVersionIdResponseDefault,
)
from ...types import Response


def _get_kwargs(
    automation_id: str,
    object_type: str,
    object_id: str,
    version_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/automations/{automation_id}/history/{object_type}/{object_id}/{version_id}/".format(
            automation_id=quote(str(automation_id), safe=""),
            object_type=quote(str(object_type), safe=""),
            object_id=quote(str(object_id), safe=""),
            version_id=quote(str(version_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | DeleteAutomationsByAutomationIdHistoryByObjectTypeByObjectIdByVersionIdResponseDefault
):
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

    response_default = DeleteAutomationsByAutomationIdHistoryByObjectTypeByObjectIdByVersionIdResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | DeleteAutomationsByAutomationIdHistoryByObjectTypeByObjectIdByVersionIdResponseDefault
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    automation_id: str,
    object_type: str,
    object_id: str,
    version_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | DeleteAutomationsByAutomationIdHistoryByObjectTypeByObjectIdByVersionIdResponseDefault
]:
    """Delete history event


    Required roles:
     - can_read_automations

    Args:
        automation_id (str):
        object_type (str):
        object_id (str):
        version_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteAutomationsByAutomationIdHistoryByObjectTypeByObjectIdByVersionIdResponseDefault]
    """

    kwargs = _get_kwargs(
        automation_id=automation_id,
        object_type=object_type,
        object_id=object_id,
        version_id=version_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    automation_id: str,
    object_type: str,
    object_id: str,
    version_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | DeleteAutomationsByAutomationIdHistoryByObjectTypeByObjectIdByVersionIdResponseDefault
    | None
):
    """Delete history event


    Required roles:
     - can_read_automations

    Args:
        automation_id (str):
        object_type (str):
        object_id (str):
        version_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteAutomationsByAutomationIdHistoryByObjectTypeByObjectIdByVersionIdResponseDefault
    """

    return sync_detailed(
        automation_id=automation_id,
        object_type=object_type,
        object_id=object_id,
        version_id=version_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    automation_id: str,
    object_type: str,
    object_id: str,
    version_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | DeleteAutomationsByAutomationIdHistoryByObjectTypeByObjectIdByVersionIdResponseDefault
]:
    """Delete history event


    Required roles:
     - can_read_automations

    Args:
        automation_id (str):
        object_type (str):
        object_id (str):
        version_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteAutomationsByAutomationIdHistoryByObjectTypeByObjectIdByVersionIdResponseDefault]
    """

    kwargs = _get_kwargs(
        automation_id=automation_id,
        object_type=object_type,
        object_id=object_id,
        version_id=version_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    automation_id: str,
    object_type: str,
    object_id: str,
    version_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | DeleteAutomationsByAutomationIdHistoryByObjectTypeByObjectIdByVersionIdResponseDefault
    | None
):
    """Delete history event


    Required roles:
     - can_read_automations

    Args:
        automation_id (str):
        object_type (str):
        object_id (str):
        version_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteAutomationsByAutomationIdHistoryByObjectTypeByObjectIdByVersionIdResponseDefault
    """

    return (
        await asyncio_detailed(
            automation_id=automation_id,
            object_type=object_type,
            object_id=object_id,
            version_id=version_id,
            client=client,
        )
    ).parsed
