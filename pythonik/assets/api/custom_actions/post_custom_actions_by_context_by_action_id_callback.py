from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.custom_action_callback_reply_schema import (
    CustomActionCallbackReplySchema,
)
from ...models.custom_action_callback_schema import CustomActionCallbackSchema
from ...models.post_custom_actions_by_context_by_action_id_callback_response_default_type_0 import (
    PostCustomActionsByContextByActionIdCallbackResponseDefaultType0,
)
from ...models.post_custom_actions_by_context_by_action_id_callback_response_default_type_1 import (
    PostCustomActionsByContextByActionIdCallbackResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    context: str,
    action_id: str,
    *,
    body: CustomActionCallbackSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/custom_actions/{context}/{action_id}/callback/".format(
            context=quote(str(context), safe=""),
            action_id=quote(str(action_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | CustomActionCallbackReplySchema
    | PostCustomActionsByContextByActionIdCallbackResponseDefaultType0
    | PostCustomActionsByContextByActionIdCallbackResponseDefaultType1
):
    if response.status_code == 200:
        response_200 = CustomActionCallbackReplySchema.from_dict(response.json())

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
        PostCustomActionsByContextByActionIdCallbackResponseDefaultType0
        | PostCustomActionsByContextByActionIdCallbackResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = PostCustomActionsByContextByActionIdCallbackResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PostCustomActionsByContextByActionIdCallbackResponseDefaultType1.from_dict(
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
    | CustomActionCallbackReplySchema
    | PostCustomActionsByContextByActionIdCallbackResponseDefaultType0
    | PostCustomActionsByContextByActionIdCallbackResponseDefaultType1
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
    body: CustomActionCallbackSchema,
) -> Response[
    Any
    | CustomActionCallbackReplySchema
    | PostCustomActionsByContextByActionIdCallbackResponseDefaultType0
    | PostCustomActionsByContextByActionIdCallbackResponseDefaultType1
]:
    """Schedules a celery task that will call custom action


    Required roles:
     - can_read_custom_actions

    Args:
        context (str):
        action_id (str):
        body (CustomActionCallbackSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CustomActionCallbackReplySchema | PostCustomActionsByContextByActionIdCallbackResponseDefaultType0 | PostCustomActionsByContextByActionIdCallbackResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        context=context,
        action_id=action_id,
        body=body,
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
    body: CustomActionCallbackSchema,
) -> (
    Any
    | CustomActionCallbackReplySchema
    | PostCustomActionsByContextByActionIdCallbackResponseDefaultType0
    | PostCustomActionsByContextByActionIdCallbackResponseDefaultType1
    | None
):
    """Schedules a celery task that will call custom action


    Required roles:
     - can_read_custom_actions

    Args:
        context (str):
        action_id (str):
        body (CustomActionCallbackSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CustomActionCallbackReplySchema | PostCustomActionsByContextByActionIdCallbackResponseDefaultType0 | PostCustomActionsByContextByActionIdCallbackResponseDefaultType1
    """

    return sync_detailed(
        context=context,
        action_id=action_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    context: str,
    action_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CustomActionCallbackSchema,
) -> Response[
    Any
    | CustomActionCallbackReplySchema
    | PostCustomActionsByContextByActionIdCallbackResponseDefaultType0
    | PostCustomActionsByContextByActionIdCallbackResponseDefaultType1
]:
    """Schedules a celery task that will call custom action


    Required roles:
     - can_read_custom_actions

    Args:
        context (str):
        action_id (str):
        body (CustomActionCallbackSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CustomActionCallbackReplySchema | PostCustomActionsByContextByActionIdCallbackResponseDefaultType0 | PostCustomActionsByContextByActionIdCallbackResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        context=context,
        action_id=action_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    context: str,
    action_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CustomActionCallbackSchema,
) -> (
    Any
    | CustomActionCallbackReplySchema
    | PostCustomActionsByContextByActionIdCallbackResponseDefaultType0
    | PostCustomActionsByContextByActionIdCallbackResponseDefaultType1
    | None
):
    """Schedules a celery task that will call custom action


    Required roles:
     - can_read_custom_actions

    Args:
        context (str):
        action_id (str):
        body (CustomActionCallbackSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CustomActionCallbackReplySchema | PostCustomActionsByContextByActionIdCallbackResponseDefaultType0 | PostCustomActionsByContextByActionIdCallbackResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            context=context,
            action_id=action_id,
            client=client,
            body=body,
        )
    ).parsed
