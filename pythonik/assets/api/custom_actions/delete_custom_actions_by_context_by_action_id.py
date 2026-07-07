from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.custom_action_schema import CustomActionSchema
from ...models.delete_custom_actions_by_context_by_action_id_response_default_type_0 import (
    DeleteCustomActionsByContextByActionIdResponseDefaultType0,
)
from ...models.delete_custom_actions_by_context_by_action_id_response_default_type_1 import (
    DeleteCustomActionsByContextByActionIdResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    context: str,
    action_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/custom_actions/{context}/{action_id}/".format(
            context=quote(str(context), safe=""),
            action_id=quote(str(action_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | CustomActionSchema
    | DeleteCustomActionsByContextByActionIdResponseDefaultType0
    | DeleteCustomActionsByContextByActionIdResponseDefaultType1
):
    if response.status_code == 204:
        response_204 = CustomActionSchema.from_dict(response.json())

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
        DeleteCustomActionsByContextByActionIdResponseDefaultType0
        | DeleteCustomActionsByContextByActionIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                DeleteCustomActionsByContextByActionIdResponseDefaultType0.from_dict(
                    data
                )
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            DeleteCustomActionsByContextByActionIdResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | CustomActionSchema
    | DeleteCustomActionsByContextByActionIdResponseDefaultType0
    | DeleteCustomActionsByContextByActionIdResponseDefaultType1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    context: str,
    action_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | CustomActionSchema
    | DeleteCustomActionsByContextByActionIdResponseDefaultType0
    | DeleteCustomActionsByContextByActionIdResponseDefaultType1
]:
    """Deletes an custom action

    Args:
        context (str):
        action_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CustomActionSchema | DeleteCustomActionsByContextByActionIdResponseDefaultType0 | DeleteCustomActionsByContextByActionIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        context=context,
        action_id=action_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    context: str,
    action_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | CustomActionSchema
    | DeleteCustomActionsByContextByActionIdResponseDefaultType0
    | DeleteCustomActionsByContextByActionIdResponseDefaultType1
    | None
):
    """Deletes an custom action

    Args:
        context (str):
        action_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CustomActionSchema | DeleteCustomActionsByContextByActionIdResponseDefaultType0 | DeleteCustomActionsByContextByActionIdResponseDefaultType1
    """

    return sync_detailed(
        context=context,
        action_id=action_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    context: str,
    action_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | CustomActionSchema
    | DeleteCustomActionsByContextByActionIdResponseDefaultType0
    | DeleteCustomActionsByContextByActionIdResponseDefaultType1
]:
    """Deletes an custom action

    Args:
        context (str):
        action_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CustomActionSchema | DeleteCustomActionsByContextByActionIdResponseDefaultType0 | DeleteCustomActionsByContextByActionIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        context=context,
        action_id=action_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    context: str,
    action_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | CustomActionSchema
    | DeleteCustomActionsByContextByActionIdResponseDefaultType0
    | DeleteCustomActionsByContextByActionIdResponseDefaultType1
    | None
):
    """Deletes an custom action

    Args:
        context (str):
        action_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CustomActionSchema | DeleteCustomActionsByContextByActionIdResponseDefaultType0 | DeleteCustomActionsByContextByActionIdResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            context=context,
            action_id=action_id,
            client=client,
        )
    ).parsed
