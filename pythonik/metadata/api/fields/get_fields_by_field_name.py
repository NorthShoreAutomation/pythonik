from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_fields_by_field_name_response_default import (
    GetFieldsByFieldNameResponseDefault,
)
from ...models.metadata_field_schema import MetadataFieldSchema
from ...types import Response


def _get_kwargs(
    field_name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/fields/{field_name}/".format(
            field_name=quote(str(field_name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetFieldsByFieldNameResponseDefault | MetadataFieldSchema:
    if response.status_code == 200:
        response_200 = MetadataFieldSchema.from_dict(response.json())

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

    response_default = GetFieldsByFieldNameResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetFieldsByFieldNameResponseDefault | MetadataFieldSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    field_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetFieldsByFieldNameResponseDefault | MetadataFieldSchema]:
    """Returns a particular field by name


    Required roles:
     - can_read_metadata_fields

    Args:
        field_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetFieldsByFieldNameResponseDefault | MetadataFieldSchema]
    """

    kwargs = _get_kwargs(
        field_name=field_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    field_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetFieldsByFieldNameResponseDefault | MetadataFieldSchema | None:
    """Returns a particular field by name


    Required roles:
     - can_read_metadata_fields

    Args:
        field_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetFieldsByFieldNameResponseDefault | MetadataFieldSchema
    """

    return sync_detailed(
        field_name=field_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    field_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetFieldsByFieldNameResponseDefault | MetadataFieldSchema]:
    """Returns a particular field by name


    Required roles:
     - can_read_metadata_fields

    Args:
        field_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetFieldsByFieldNameResponseDefault | MetadataFieldSchema]
    """

    kwargs = _get_kwargs(
        field_name=field_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    field_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetFieldsByFieldNameResponseDefault | MetadataFieldSchema | None:
    """Returns a particular field by name


    Required roles:
     - can_read_metadata_fields

    Args:
        field_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetFieldsByFieldNameResponseDefault | MetadataFieldSchema
    """

    return (
        await asyncio_detailed(
            field_name=field_name,
            client=client,
        )
    ).parsed
