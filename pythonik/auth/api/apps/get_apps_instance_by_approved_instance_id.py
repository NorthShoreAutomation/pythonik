from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.external_auth_schema import ExternalAuthSchema
from ...models.get_apps_instance_by_approved_instance_id_response_default_type_0 import (
    GetAppsInstanceByApprovedInstanceIdResponseDefaultType0,
)
from ...models.get_apps_instance_by_approved_instance_id_response_default_type_1 import (
    GetAppsInstanceByApprovedInstanceIdResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    approved_instance_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/apps/instance/{approved_instance_id}/".format(
            approved_instance_id=quote(str(approved_instance_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | ExternalAuthSchema
    | GetAppsInstanceByApprovedInstanceIdResponseDefaultType0
    | GetAppsInstanceByApprovedInstanceIdResponseDefaultType1
):
    if response.status_code == 200:
        response_200 = ExternalAuthSchema.from_dict(response.json())

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
        GetAppsInstanceByApprovedInstanceIdResponseDefaultType0
        | GetAppsInstanceByApprovedInstanceIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetAppsInstanceByApprovedInstanceIdResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            GetAppsInstanceByApprovedInstanceIdResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | ExternalAuthSchema
    | GetAppsInstanceByApprovedInstanceIdResponseDefaultType0
    | GetAppsInstanceByApprovedInstanceIdResponseDefaultType1
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
    | ExternalAuthSchema
    | GetAppsInstanceByApprovedInstanceIdResponseDefaultType0
    | GetAppsInstanceByApprovedInstanceIdResponseDefaultType1
]:
    """Gets an approved instance of an app

    Args:
        approved_instance_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ExternalAuthSchema | GetAppsInstanceByApprovedInstanceIdResponseDefaultType0 | GetAppsInstanceByApprovedInstanceIdResponseDefaultType1]
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
    | ExternalAuthSchema
    | GetAppsInstanceByApprovedInstanceIdResponseDefaultType0
    | GetAppsInstanceByApprovedInstanceIdResponseDefaultType1
    | None
):
    """Gets an approved instance of an app

    Args:
        approved_instance_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ExternalAuthSchema | GetAppsInstanceByApprovedInstanceIdResponseDefaultType0 | GetAppsInstanceByApprovedInstanceIdResponseDefaultType1
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
    | ExternalAuthSchema
    | GetAppsInstanceByApprovedInstanceIdResponseDefaultType0
    | GetAppsInstanceByApprovedInstanceIdResponseDefaultType1
]:
    """Gets an approved instance of an app

    Args:
        approved_instance_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ExternalAuthSchema | GetAppsInstanceByApprovedInstanceIdResponseDefaultType0 | GetAppsInstanceByApprovedInstanceIdResponseDefaultType1]
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
    | ExternalAuthSchema
    | GetAppsInstanceByApprovedInstanceIdResponseDefaultType0
    | GetAppsInstanceByApprovedInstanceIdResponseDefaultType1
    | None
):
    """Gets an approved instance of an app

    Args:
        approved_instance_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ExternalAuthSchema | GetAppsInstanceByApprovedInstanceIdResponseDefaultType0 | GetAppsInstanceByApprovedInstanceIdResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            approved_instance_id=approved_instance_id,
            client=client,
        )
    ).parsed
