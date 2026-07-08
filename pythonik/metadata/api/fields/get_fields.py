from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_fields_response_default import GetFieldsResponseDefault
from ...models.metadata_fields_schema import MetadataFieldsSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    per_page: int | Unset = UNSET,
    last_field_name: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["per_page"] = per_page

    params["last_field_name"] = last_field_name

    params["filter"] = filter_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/fields/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetFieldsResponseDefault | MetadataFieldsSchema:
    if response.status_code == 200:
        response_200 = MetadataFieldsSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = GetFieldsResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetFieldsResponseDefault | MetadataFieldsSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    last_field_name: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
) -> Response[Any | GetFieldsResponseDefault | MetadataFieldsSchema]:
    """List the fields defined in the system


    Required roles:
     - can_read_metadata_fields

    Args:
        per_page (int | Unset):
        last_field_name (str | Unset):
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetFieldsResponseDefault | MetadataFieldsSchema]
    """

    kwargs = _get_kwargs(
        per_page=per_page,
        last_field_name=last_field_name,
        filter_=filter_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    last_field_name: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
) -> Any | GetFieldsResponseDefault | MetadataFieldsSchema | None:
    """List the fields defined in the system


    Required roles:
     - can_read_metadata_fields

    Args:
        per_page (int | Unset):
        last_field_name (str | Unset):
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetFieldsResponseDefault | MetadataFieldsSchema
    """

    return sync_detailed(
        client=client,
        per_page=per_page,
        last_field_name=last_field_name,
        filter_=filter_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    last_field_name: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
) -> Response[Any | GetFieldsResponseDefault | MetadataFieldsSchema]:
    """List the fields defined in the system


    Required roles:
     - can_read_metadata_fields

    Args:
        per_page (int | Unset):
        last_field_name (str | Unset):
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetFieldsResponseDefault | MetadataFieldsSchema]
    """

    kwargs = _get_kwargs(
        per_page=per_page,
        last_field_name=last_field_name,
        filter_=filter_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    last_field_name: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
) -> Any | GetFieldsResponseDefault | MetadataFieldsSchema | None:
    """List the fields defined in the system


    Required roles:
     - can_read_metadata_fields

    Args:
        per_page (int | Unset):
        last_field_name (str | Unset):
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetFieldsResponseDefault | MetadataFieldsSchema
    """

    return (
        await asyncio_detailed(
            client=client,
            per_page=per_page,
            last_field_name=last_field_name,
            filter_=filter_,
        )
    ).parsed
