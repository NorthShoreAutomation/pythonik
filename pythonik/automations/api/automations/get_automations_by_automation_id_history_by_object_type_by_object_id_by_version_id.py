from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.automation_history_schema import AutomationHistorySchema
from ...models.get_automations_by_automation_id_history_by_object_type_by_object_id_by_version_id_response_default_type_0 import (
    GetAutomationsByAutomationIdHistoryByObjectTypeByObjectIdByVersionIdResponseDefaultType0,
)
from ...models.get_automations_by_automation_id_history_by_object_type_by_object_id_by_version_id_response_default_type_1 import (
    GetAutomationsByAutomationIdHistoryByObjectTypeByObjectIdByVersionIdResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    automation_id: str,
    object_type: str,
    object_id: str,
    version_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
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
    | AutomationHistorySchema
    | GetAutomationsByAutomationIdHistoryByObjectTypeByObjectIdByVersionIdResponseDefaultType0
    | GetAutomationsByAutomationIdHistoryByObjectTypeByObjectIdByVersionIdResponseDefaultType1
):
    if response.status_code == 200:
        response_200 = AutomationHistorySchema.from_dict(response.json())

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
        GetAutomationsByAutomationIdHistoryByObjectTypeByObjectIdByVersionIdResponseDefaultType0
        | GetAutomationsByAutomationIdHistoryByObjectTypeByObjectIdByVersionIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = GetAutomationsByAutomationIdHistoryByObjectTypeByObjectIdByVersionIdResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = GetAutomationsByAutomationIdHistoryByObjectTypeByObjectIdByVersionIdResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | AutomationHistorySchema
    | GetAutomationsByAutomationIdHistoryByObjectTypeByObjectIdByVersionIdResponseDefaultType0
    | GetAutomationsByAutomationIdHistoryByObjectTypeByObjectIdByVersionIdResponseDefaultType1
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
    | AutomationHistorySchema
    | GetAutomationsByAutomationIdHistoryByObjectTypeByObjectIdByVersionIdResponseDefaultType0
    | GetAutomationsByAutomationIdHistoryByObjectTypeByObjectIdByVersionIdResponseDefaultType1
]:
    """Returns a particular history entity by id


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
        Response[Any | AutomationHistorySchema | GetAutomationsByAutomationIdHistoryByObjectTypeByObjectIdByVersionIdResponseDefaultType0 | GetAutomationsByAutomationIdHistoryByObjectTypeByObjectIdByVersionIdResponseDefaultType1]
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
    | AutomationHistorySchema
    | GetAutomationsByAutomationIdHistoryByObjectTypeByObjectIdByVersionIdResponseDefaultType0
    | GetAutomationsByAutomationIdHistoryByObjectTypeByObjectIdByVersionIdResponseDefaultType1
    | None
):
    """Returns a particular history entity by id


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
        Any | AutomationHistorySchema | GetAutomationsByAutomationIdHistoryByObjectTypeByObjectIdByVersionIdResponseDefaultType0 | GetAutomationsByAutomationIdHistoryByObjectTypeByObjectIdByVersionIdResponseDefaultType1
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
    | AutomationHistorySchema
    | GetAutomationsByAutomationIdHistoryByObjectTypeByObjectIdByVersionIdResponseDefaultType0
    | GetAutomationsByAutomationIdHistoryByObjectTypeByObjectIdByVersionIdResponseDefaultType1
]:
    """Returns a particular history entity by id


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
        Response[Any | AutomationHistorySchema | GetAutomationsByAutomationIdHistoryByObjectTypeByObjectIdByVersionIdResponseDefaultType0 | GetAutomationsByAutomationIdHistoryByObjectTypeByObjectIdByVersionIdResponseDefaultType1]
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
    | AutomationHistorySchema
    | GetAutomationsByAutomationIdHistoryByObjectTypeByObjectIdByVersionIdResponseDefaultType0
    | GetAutomationsByAutomationIdHistoryByObjectTypeByObjectIdByVersionIdResponseDefaultType1
    | None
):
    """Returns a particular history entity by id


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
        Any | AutomationHistorySchema | GetAutomationsByAutomationIdHistoryByObjectTypeByObjectIdByVersionIdResponseDefaultType0 | GetAutomationsByAutomationIdHistoryByObjectTypeByObjectIdByVersionIdResponseDefaultType1
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
