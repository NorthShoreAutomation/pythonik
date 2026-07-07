from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_shares_custom_actions_by_context_by_action_id_views_response_default_type_0 import (
    GetSharesCustomActionsByContextByActionIdViewsResponseDefaultType0,
)
from ...models.get_shares_custom_actions_by_context_by_action_id_views_response_default_type_1 import (
    GetSharesCustomActionsByContextByActionIdViewsResponseDefaultType1,
)
from ...models.metadata_view_schema import MetadataViewSchema
from ...types import Response


def _get_kwargs(
    context: str,
    action_id: str,
    *,
    share_id: str,
    share_user_id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Share-ID"] = share_id

    headers["Share-User-ID"] = share_user_id

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/shares/custom_actions/{context}/{action_id}/views/".format(
            context=quote(str(context), safe=""),
            action_id=quote(str(action_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetSharesCustomActionsByContextByActionIdViewsResponseDefaultType0
    | GetSharesCustomActionsByContextByActionIdViewsResponseDefaultType1
    | MetadataViewSchema
):
    if response.status_code == 200:
        response_200 = MetadataViewSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    def _parse_response_default(
        data: object,
    ) -> (
        GetSharesCustomActionsByContextByActionIdViewsResponseDefaultType0
        | GetSharesCustomActionsByContextByActionIdViewsResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = GetSharesCustomActionsByContextByActionIdViewsResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = GetSharesCustomActionsByContextByActionIdViewsResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetSharesCustomActionsByContextByActionIdViewsResponseDefaultType0
    | GetSharesCustomActionsByContextByActionIdViewsResponseDefaultType1
    | MetadataViewSchema
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
    share_id: str,
    share_user_id: str,
) -> Response[
    Any
    | GetSharesCustomActionsByContextByActionIdViewsResponseDefaultType0
    | GetSharesCustomActionsByContextByActionIdViewsResponseDefaultType1
    | MetadataViewSchema
]:
    """Returns a particular view for a shared custom action context

    Args:
        context (str):
        action_id (str):
        share_id (str):
        share_user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSharesCustomActionsByContextByActionIdViewsResponseDefaultType0 | GetSharesCustomActionsByContextByActionIdViewsResponseDefaultType1 | MetadataViewSchema]
    """

    kwargs = _get_kwargs(
        context=context,
        action_id=action_id,
        share_id=share_id,
        share_user_id=share_user_id,
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
    share_id: str,
    share_user_id: str,
) -> (
    Any
    | GetSharesCustomActionsByContextByActionIdViewsResponseDefaultType0
    | GetSharesCustomActionsByContextByActionIdViewsResponseDefaultType1
    | MetadataViewSchema
    | None
):
    """Returns a particular view for a shared custom action context

    Args:
        context (str):
        action_id (str):
        share_id (str):
        share_user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSharesCustomActionsByContextByActionIdViewsResponseDefaultType0 | GetSharesCustomActionsByContextByActionIdViewsResponseDefaultType1 | MetadataViewSchema
    """

    return sync_detailed(
        context=context,
        action_id=action_id,
        client=client,
        share_id=share_id,
        share_user_id=share_user_id,
    ).parsed


async def asyncio_detailed(
    context: str,
    action_id: str,
    *,
    client: AuthenticatedClient | Client,
    share_id: str,
    share_user_id: str,
) -> Response[
    Any
    | GetSharesCustomActionsByContextByActionIdViewsResponseDefaultType0
    | GetSharesCustomActionsByContextByActionIdViewsResponseDefaultType1
    | MetadataViewSchema
]:
    """Returns a particular view for a shared custom action context

    Args:
        context (str):
        action_id (str):
        share_id (str):
        share_user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSharesCustomActionsByContextByActionIdViewsResponseDefaultType0 | GetSharesCustomActionsByContextByActionIdViewsResponseDefaultType1 | MetadataViewSchema]
    """

    kwargs = _get_kwargs(
        context=context,
        action_id=action_id,
        share_id=share_id,
        share_user_id=share_user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    context: str,
    action_id: str,
    *,
    client: AuthenticatedClient | Client,
    share_id: str,
    share_user_id: str,
) -> (
    Any
    | GetSharesCustomActionsByContextByActionIdViewsResponseDefaultType0
    | GetSharesCustomActionsByContextByActionIdViewsResponseDefaultType1
    | MetadataViewSchema
    | None
):
    """Returns a particular view for a shared custom action context

    Args:
        context (str):
        action_id (str):
        share_id (str):
        share_user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSharesCustomActionsByContextByActionIdViewsResponseDefaultType0 | GetSharesCustomActionsByContextByActionIdViewsResponseDefaultType1 | MetadataViewSchema
    """

    return (
        await asyncio_detailed(
            context=context,
            action_id=action_id,
            client=client,
            share_id=share_id,
            share_user_id=share_user_id,
        )
    ).parsed
