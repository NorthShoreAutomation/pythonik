from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_apps_by_app_id_response_default_type_0 import (
    DeleteAppsByAppIdResponseDefaultType0,
)
from ...models.delete_apps_by_app_id_response_default_type_1 import (
    DeleteAppsByAppIdResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    app_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/apps/{app_id}/".format(
            app_id=quote(str(app_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any | DeleteAppsByAppIdResponseDefaultType0 | DeleteAppsByAppIdResponseDefaultType1
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
    ) -> DeleteAppsByAppIdResponseDefaultType0 | DeleteAppsByAppIdResponseDefaultType1:
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = DeleteAppsByAppIdResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = DeleteAppsByAppIdResponseDefaultType1.from_dict(data)

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | DeleteAppsByAppIdResponseDefaultType0 | DeleteAppsByAppIdResponseDefaultType1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    app_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any | DeleteAppsByAppIdResponseDefaultType0 | DeleteAppsByAppIdResponseDefaultType1
]:
    """Delete a particular app by id


    Required roles:
     - can_delete_apps

    Args:
        app_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteAppsByAppIdResponseDefaultType0 | DeleteAppsByAppIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    app_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | DeleteAppsByAppIdResponseDefaultType0
    | DeleteAppsByAppIdResponseDefaultType1
    | None
):
    """Delete a particular app by id


    Required roles:
     - can_delete_apps

    Args:
        app_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteAppsByAppIdResponseDefaultType0 | DeleteAppsByAppIdResponseDefaultType1
    """

    return sync_detailed(
        app_id=app_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    app_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any | DeleteAppsByAppIdResponseDefaultType0 | DeleteAppsByAppIdResponseDefaultType1
]:
    """Delete a particular app by id


    Required roles:
     - can_delete_apps

    Args:
        app_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteAppsByAppIdResponseDefaultType0 | DeleteAppsByAppIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | DeleteAppsByAppIdResponseDefaultType0
    | DeleteAppsByAppIdResponseDefaultType1
    | None
):
    """Delete a particular app by id


    Required roles:
     - can_delete_apps

    Args:
        app_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteAppsByAppIdResponseDefaultType0 | DeleteAppsByAppIdResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            app_id=app_id,
            client=client,
        )
    ).parsed
