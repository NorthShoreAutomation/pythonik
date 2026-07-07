from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_user_fields_response_default_type_0 import (
    GetUserFieldsResponseDefaultType0,
)
from ...models.get_user_fields_response_default_type_1 import (
    GetUserFieldsResponseDefaultType1,
)
from ...models.metadata_fields_schema import MetadataFieldsSchema
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/user/fields/",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetUserFieldsResponseDefaultType0
    | GetUserFieldsResponseDefaultType1
    | MetadataFieldsSchema
):
    if response.status_code == 200:
        response_200 = MetadataFieldsSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    def _parse_response_default(
        data: object,
    ) -> GetUserFieldsResponseDefaultType0 | GetUserFieldsResponseDefaultType1:
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = GetUserFieldsResponseDefaultType0.from_dict(data)

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = GetUserFieldsResponseDefaultType1.from_dict(data)

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetUserFieldsResponseDefaultType0
    | GetUserFieldsResponseDefaultType1
    | MetadataFieldsSchema
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
) -> Response[
    Any
    | GetUserFieldsResponseDefaultType0
    | GetUserFieldsResponseDefaultType1
    | MetadataFieldsSchema
]:
    """List the fields that can be accessed by a user


    Required roles:
     - can_read_metadata_fields

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetUserFieldsResponseDefaultType0 | GetUserFieldsResponseDefaultType1 | MetadataFieldsSchema]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetUserFieldsResponseDefaultType0
    | GetUserFieldsResponseDefaultType1
    | MetadataFieldsSchema
    | None
):
    """List the fields that can be accessed by a user


    Required roles:
     - can_read_metadata_fields

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetUserFieldsResponseDefaultType0 | GetUserFieldsResponseDefaultType1 | MetadataFieldsSchema
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetUserFieldsResponseDefaultType0
    | GetUserFieldsResponseDefaultType1
    | MetadataFieldsSchema
]:
    """List the fields that can be accessed by a user


    Required roles:
     - can_read_metadata_fields

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetUserFieldsResponseDefaultType0 | GetUserFieldsResponseDefaultType1 | MetadataFieldsSchema]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetUserFieldsResponseDefaultType0
    | GetUserFieldsResponseDefaultType1
    | MetadataFieldsSchema
    | None
):
    """List the fields that can be accessed by a user


    Required roles:
     - can_read_metadata_fields

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetUserFieldsResponseDefaultType0 | GetUserFieldsResponseDefaultType1 | MetadataFieldsSchema
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
