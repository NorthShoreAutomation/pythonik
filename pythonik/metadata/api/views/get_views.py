from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_views_response_default_type_0 import GetViewsResponseDefaultType0
from ...models.get_views_response_default_type_1 import GetViewsResponseDefaultType1
from ...models.metadata_views_schema import MetadataViewsSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    include_fields: str | Unset = UNSET,
    exclude_fields: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["include_fields"] = include_fields

    params["exclude_fields"] = exclude_fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/views/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetViewsResponseDefaultType0
    | GetViewsResponseDefaultType1
    | MetadataViewsSchema
):
    if response.status_code == 200:
        response_200 = MetadataViewsSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    def _parse_response_default(
        data: object,
    ) -> GetViewsResponseDefaultType0 | GetViewsResponseDefaultType1:
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = GetViewsResponseDefaultType0.from_dict(data)

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = GetViewsResponseDefaultType1.from_dict(data)

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetViewsResponseDefaultType0
    | GetViewsResponseDefaultType1
    | MetadataViewsSchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    include_fields: str | Unset = UNSET,
    exclude_fields: str | Unset = UNSET,
) -> Response[
    Any
    | GetViewsResponseDefaultType0
    | GetViewsResponseDefaultType1
    | MetadataViewsSchema
]:
    """List the views defined in the system


    Required roles:
     - can_read_metadata_views

    Args:
        include_fields (str | Unset):
        exclude_fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetViewsResponseDefaultType0 | GetViewsResponseDefaultType1 | MetadataViewsSchema]
    """

    kwargs = _get_kwargs(
        include_fields=include_fields,
        exclude_fields=exclude_fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    include_fields: str | Unset = UNSET,
    exclude_fields: str | Unset = UNSET,
) -> (
    Any
    | GetViewsResponseDefaultType0
    | GetViewsResponseDefaultType1
    | MetadataViewsSchema
    | None
):
    """List the views defined in the system


    Required roles:
     - can_read_metadata_views

    Args:
        include_fields (str | Unset):
        exclude_fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetViewsResponseDefaultType0 | GetViewsResponseDefaultType1 | MetadataViewsSchema
    """

    return sync_detailed(
        client=client,
        include_fields=include_fields,
        exclude_fields=exclude_fields,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    include_fields: str | Unset = UNSET,
    exclude_fields: str | Unset = UNSET,
) -> Response[
    Any
    | GetViewsResponseDefaultType0
    | GetViewsResponseDefaultType1
    | MetadataViewsSchema
]:
    """List the views defined in the system


    Required roles:
     - can_read_metadata_views

    Args:
        include_fields (str | Unset):
        exclude_fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetViewsResponseDefaultType0 | GetViewsResponseDefaultType1 | MetadataViewsSchema]
    """

    kwargs = _get_kwargs(
        include_fields=include_fields,
        exclude_fields=exclude_fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    include_fields: str | Unset = UNSET,
    exclude_fields: str | Unset = UNSET,
) -> (
    Any
    | GetViewsResponseDefaultType0
    | GetViewsResponseDefaultType1
    | MetadataViewsSchema
    | None
):
    """List the views defined in the system


    Required roles:
     - can_read_metadata_views

    Args:
        include_fields (str | Unset):
        exclude_fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetViewsResponseDefaultType0 | GetViewsResponseDefaultType1 | MetadataViewsSchema
    """

    return (
        await asyncio_detailed(
            client=client,
            include_fields=include_fields,
            exclude_fields=exclude_fields,
        )
    ).parsed
