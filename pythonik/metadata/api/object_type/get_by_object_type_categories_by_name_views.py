from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_by_object_type_categories_by_name_views_response_default import (
    GetByObjectTypeCategoriesByNameViewsResponseDefault,
)
from ...models.metadata_category_schema import MetadataCategorySchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    object_type: str,
    name: str,
    *,
    ext_options: bool | Unset = UNSET,
    writable_only: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["ext_options"] = ext_options

    params["writable_only"] = writable_only

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/{object_type}/categories/{name}/views/".format(
            object_type=quote(str(object_type), safe=""),
            name=quote(str(name), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetByObjectTypeCategoriesByNameViewsResponseDefault | MetadataCategorySchema:
    if response.status_code == 200:
        response_200 = MetadataCategorySchema.from_dict(response.json())

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

    response_default = GetByObjectTypeCategoriesByNameViewsResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | GetByObjectTypeCategoriesByNameViewsResponseDefault | MetadataCategorySchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    object_type: str,
    name: str,
    *,
    client: AuthenticatedClient | Client,
    ext_options: bool | Unset = UNSET,
    writable_only: bool | Unset = UNSET,
) -> Response[
    Any | GetByObjectTypeCategoriesByNameViewsResponseDefault | MetadataCategorySchema
]:
    """Get metadata views with field for object type and category


    Required roles:
     - can_read_metadata_categories

    Args:
        object_type (str):
        name (str):
        ext_options (bool | Unset):
        writable_only (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetByObjectTypeCategoriesByNameViewsResponseDefault | MetadataCategorySchema]
    """

    kwargs = _get_kwargs(
        object_type=object_type,
        name=name,
        ext_options=ext_options,
        writable_only=writable_only,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    object_type: str,
    name: str,
    *,
    client: AuthenticatedClient | Client,
    ext_options: bool | Unset = UNSET,
    writable_only: bool | Unset = UNSET,
) -> (
    Any
    | GetByObjectTypeCategoriesByNameViewsResponseDefault
    | MetadataCategorySchema
    | None
):
    """Get metadata views with field for object type and category


    Required roles:
     - can_read_metadata_categories

    Args:
        object_type (str):
        name (str):
        ext_options (bool | Unset):
        writable_only (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetByObjectTypeCategoriesByNameViewsResponseDefault | MetadataCategorySchema
    """

    return sync_detailed(
        object_type=object_type,
        name=name,
        client=client,
        ext_options=ext_options,
        writable_only=writable_only,
    ).parsed


async def asyncio_detailed(
    object_type: str,
    name: str,
    *,
    client: AuthenticatedClient | Client,
    ext_options: bool | Unset = UNSET,
    writable_only: bool | Unset = UNSET,
) -> Response[
    Any | GetByObjectTypeCategoriesByNameViewsResponseDefault | MetadataCategorySchema
]:
    """Get metadata views with field for object type and category


    Required roles:
     - can_read_metadata_categories

    Args:
        object_type (str):
        name (str):
        ext_options (bool | Unset):
        writable_only (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetByObjectTypeCategoriesByNameViewsResponseDefault | MetadataCategorySchema]
    """

    kwargs = _get_kwargs(
        object_type=object_type,
        name=name,
        ext_options=ext_options,
        writable_only=writable_only,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    object_type: str,
    name: str,
    *,
    client: AuthenticatedClient | Client,
    ext_options: bool | Unset = UNSET,
    writable_only: bool | Unset = UNSET,
) -> (
    Any
    | GetByObjectTypeCategoriesByNameViewsResponseDefault
    | MetadataCategorySchema
    | None
):
    """Get metadata views with field for object type and category


    Required roles:
     - can_read_metadata_categories

    Args:
        object_type (str):
        name (str):
        ext_options (bool | Unset):
        writable_only (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetByObjectTypeCategoriesByNameViewsResponseDefault | MetadataCategorySchema
    """

    return (
        await asyncio_detailed(
            object_type=object_type,
            name=name,
            client=client,
            ext_options=ext_options,
            writable_only=writable_only,
        )
    ).parsed
