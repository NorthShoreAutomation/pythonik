from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_views_by_view_id_response_default_type_0 import (
    GetViewsByViewIdResponseDefaultType0,
)
from ...models.get_views_by_view_id_response_default_type_1 import (
    GetViewsByViewIdResponseDefaultType1,
)
from ...models.metadata_view_schema import MetadataViewSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    view_id: str,
    *,
    merge_fields: bool | Unset = True,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["merge_fields"] = merge_fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/views/{view_id}/".format(
            view_id=quote(str(view_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetViewsByViewIdResponseDefaultType0
    | GetViewsByViewIdResponseDefaultType1
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

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    def _parse_response_default(
        data: object,
    ) -> GetViewsByViewIdResponseDefaultType0 | GetViewsByViewIdResponseDefaultType1:
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = GetViewsByViewIdResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = GetViewsByViewIdResponseDefaultType1.from_dict(data)

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetViewsByViewIdResponseDefaultType0
    | GetViewsByViewIdResponseDefaultType1
    | MetadataViewSchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    view_id: str,
    *,
    client: AuthenticatedClient | Client,
    merge_fields: bool | Unset = True,
) -> Response[
    Any
    | GetViewsByViewIdResponseDefaultType0
    | GetViewsByViewIdResponseDefaultType1
    | MetadataViewSchema
]:
    """Returns a particular view by id


    Required roles:
     - can_read_metadata_views

    Args:
        view_id (str):
        merge_fields (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetViewsByViewIdResponseDefaultType0 | GetViewsByViewIdResponseDefaultType1 | MetadataViewSchema]
    """

    kwargs = _get_kwargs(
        view_id=view_id,
        merge_fields=merge_fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    view_id: str,
    *,
    client: AuthenticatedClient | Client,
    merge_fields: bool | Unset = True,
) -> (
    Any
    | GetViewsByViewIdResponseDefaultType0
    | GetViewsByViewIdResponseDefaultType1
    | MetadataViewSchema
    | None
):
    """Returns a particular view by id


    Required roles:
     - can_read_metadata_views

    Args:
        view_id (str):
        merge_fields (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetViewsByViewIdResponseDefaultType0 | GetViewsByViewIdResponseDefaultType1 | MetadataViewSchema
    """

    return sync_detailed(
        view_id=view_id,
        client=client,
        merge_fields=merge_fields,
    ).parsed


async def asyncio_detailed(
    view_id: str,
    *,
    client: AuthenticatedClient | Client,
    merge_fields: bool | Unset = True,
) -> Response[
    Any
    | GetViewsByViewIdResponseDefaultType0
    | GetViewsByViewIdResponseDefaultType1
    | MetadataViewSchema
]:
    """Returns a particular view by id


    Required roles:
     - can_read_metadata_views

    Args:
        view_id (str):
        merge_fields (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetViewsByViewIdResponseDefaultType0 | GetViewsByViewIdResponseDefaultType1 | MetadataViewSchema]
    """

    kwargs = _get_kwargs(
        view_id=view_id,
        merge_fields=merge_fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    view_id: str,
    *,
    client: AuthenticatedClient | Client,
    merge_fields: bool | Unset = True,
) -> (
    Any
    | GetViewsByViewIdResponseDefaultType0
    | GetViewsByViewIdResponseDefaultType1
    | MetadataViewSchema
    | None
):
    """Returns a particular view by id


    Required roles:
     - can_read_metadata_views

    Args:
        view_id (str):
        merge_fields (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetViewsByViewIdResponseDefaultType0 | GetViewsByViewIdResponseDefaultType1 | MetadataViewSchema
    """

    return (
        await asyncio_detailed(
            view_id=view_id,
            client=client,
            merge_fields=merge_fields,
        )
    ).parsed
