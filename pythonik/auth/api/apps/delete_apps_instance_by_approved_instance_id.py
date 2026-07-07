from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_apps_instance_by_approved_instance_id_response_default_type_0 import (
    DeleteAppsInstanceByApprovedInstanceIdResponseDefaultType0,
)
from ...models.delete_apps_instance_by_approved_instance_id_response_default_type_1 import (
    DeleteAppsInstanceByApprovedInstanceIdResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    approved_instance_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/apps/instance/{approved_instance_id}/".format(
            approved_instance_id=quote(str(approved_instance_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | DeleteAppsInstanceByApprovedInstanceIdResponseDefaultType0
    | DeleteAppsInstanceByApprovedInstanceIdResponseDefaultType1
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

    def _parse_response_default(
        data: object,
    ) -> (
        DeleteAppsInstanceByApprovedInstanceIdResponseDefaultType0
        | DeleteAppsInstanceByApprovedInstanceIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                DeleteAppsInstanceByApprovedInstanceIdResponseDefaultType0.from_dict(
                    data
                )
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            DeleteAppsInstanceByApprovedInstanceIdResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | DeleteAppsInstanceByApprovedInstanceIdResponseDefaultType0
    | DeleteAppsInstanceByApprovedInstanceIdResponseDefaultType1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    approved_instance_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | DeleteAppsInstanceByApprovedInstanceIdResponseDefaultType0
    | DeleteAppsInstanceByApprovedInstanceIdResponseDefaultType1
]:
    """Delete an approved instance of an app

    Args:
        approved_instance_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteAppsInstanceByApprovedInstanceIdResponseDefaultType0 | DeleteAppsInstanceByApprovedInstanceIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        approved_instance_id=approved_instance_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    approved_instance_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | DeleteAppsInstanceByApprovedInstanceIdResponseDefaultType0
    | DeleteAppsInstanceByApprovedInstanceIdResponseDefaultType1
    | None
):
    """Delete an approved instance of an app

    Args:
        approved_instance_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteAppsInstanceByApprovedInstanceIdResponseDefaultType0 | DeleteAppsInstanceByApprovedInstanceIdResponseDefaultType1
    """

    return sync_detailed(
        approved_instance_id=approved_instance_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    approved_instance_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | DeleteAppsInstanceByApprovedInstanceIdResponseDefaultType0
    | DeleteAppsInstanceByApprovedInstanceIdResponseDefaultType1
]:
    """Delete an approved instance of an app

    Args:
        approved_instance_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteAppsInstanceByApprovedInstanceIdResponseDefaultType0 | DeleteAppsInstanceByApprovedInstanceIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        approved_instance_id=approved_instance_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    approved_instance_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | DeleteAppsInstanceByApprovedInstanceIdResponseDefaultType0
    | DeleteAppsInstanceByApprovedInstanceIdResponseDefaultType1
    | None
):
    """Delete an approved instance of an app

    Args:
        approved_instance_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteAppsInstanceByApprovedInstanceIdResponseDefaultType0 | DeleteAppsInstanceByApprovedInstanceIdResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            approved_instance_id=approved_instance_id,
            client=client,
        )
    ).parsed
