from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.custom_action_create_schema import CustomActionCreateSchema
from ...models.custom_action_schema import CustomActionSchema
from ...models.post_custom_actions_by_context_response_default_type_0 import (
    PostCustomActionsByContextResponseDefaultType0,
)
from ...models.post_custom_actions_by_context_response_default_type_1 import (
    PostCustomActionsByContextResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    context: str,
    *,
    body: CustomActionCreateSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/custom_actions/{context}/".format(
            context=quote(str(context), safe=""),
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
    | CustomActionSchema
    | PostCustomActionsByContextResponseDefaultType0
    | PostCustomActionsByContextResponseDefaultType1
):
    if response.status_code == 201:
        response_201 = CustomActionSchema.from_dict(response.json())

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
        PostCustomActionsByContextResponseDefaultType0
        | PostCustomActionsByContextResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                PostCustomActionsByContextResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PostCustomActionsByContextResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | CustomActionSchema
    | PostCustomActionsByContextResponseDefaultType0
    | PostCustomActionsByContextResponseDefaultType1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    context: str,
    *,
    client: AuthenticatedClient | Client,
    body: CustomActionCreateSchema,
) -> Response[
    Any
    | CustomActionSchema
    | PostCustomActionsByContextResponseDefaultType0
    | PostCustomActionsByContextResponseDefaultType1
]:
    """Create an custom action

    Args:
        context (str):
        body (CustomActionCreateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CustomActionSchema | PostCustomActionsByContextResponseDefaultType0 | PostCustomActionsByContextResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        context=context,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    context: str,
    *,
    client: AuthenticatedClient | Client,
    body: CustomActionCreateSchema,
) -> (
    Any
    | CustomActionSchema
    | PostCustomActionsByContextResponseDefaultType0
    | PostCustomActionsByContextResponseDefaultType1
    | None
):
    """Create an custom action

    Args:
        context (str):
        body (CustomActionCreateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CustomActionSchema | PostCustomActionsByContextResponseDefaultType0 | PostCustomActionsByContextResponseDefaultType1
    """

    return sync_detailed(
        context=context,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    context: str,
    *,
    client: AuthenticatedClient | Client,
    body: CustomActionCreateSchema,
) -> Response[
    Any
    | CustomActionSchema
    | PostCustomActionsByContextResponseDefaultType0
    | PostCustomActionsByContextResponseDefaultType1
]:
    """Create an custom action

    Args:
        context (str):
        body (CustomActionCreateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CustomActionSchema | PostCustomActionsByContextResponseDefaultType0 | PostCustomActionsByContextResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        context=context,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    context: str,
    *,
    client: AuthenticatedClient | Client,
    body: CustomActionCreateSchema,
) -> (
    Any
    | CustomActionSchema
    | PostCustomActionsByContextResponseDefaultType0
    | PostCustomActionsByContextResponseDefaultType1
    | None
):
    """Create an custom action

    Args:
        context (str):
        body (CustomActionCreateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CustomActionSchema | PostCustomActionsByContextResponseDefaultType0 | PostCustomActionsByContextResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            context=context,
            client=client,
            body=body,
        )
    ).parsed
