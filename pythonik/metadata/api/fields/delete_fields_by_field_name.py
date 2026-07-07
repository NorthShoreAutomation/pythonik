from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_fields_by_field_name_response_default_type_0 import (
    DeleteFieldsByFieldNameResponseDefaultType0,
)
from ...models.delete_fields_by_field_name_response_default_type_1 import (
    DeleteFieldsByFieldNameResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    field_name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/fields/{field_name}/".format(
            field_name=quote(str(field_name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | DeleteFieldsByFieldNameResponseDefaultType0
    | DeleteFieldsByFieldNameResponseDefaultType1
):
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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
        DeleteFieldsByFieldNameResponseDefaultType0
        | DeleteFieldsByFieldNameResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                DeleteFieldsByFieldNameResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = DeleteFieldsByFieldNameResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | DeleteFieldsByFieldNameResponseDefaultType0
    | DeleteFieldsByFieldNameResponseDefaultType1
]:
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
) -> Response[
    Any
    | DeleteFieldsByFieldNameResponseDefaultType0
    | DeleteFieldsByFieldNameResponseDefaultType1
]:
    """Delete a particular field by name


    Required roles:
     - can_delete_metadata_fields

    Args:
        field_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteFieldsByFieldNameResponseDefaultType0 | DeleteFieldsByFieldNameResponseDefaultType1]
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
) -> (
    Any
    | DeleteFieldsByFieldNameResponseDefaultType0
    | DeleteFieldsByFieldNameResponseDefaultType1
    | None
):
    """Delete a particular field by name


    Required roles:
     - can_delete_metadata_fields

    Args:
        field_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteFieldsByFieldNameResponseDefaultType0 | DeleteFieldsByFieldNameResponseDefaultType1
    """

    return sync_detailed(
        field_name=field_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    field_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | DeleteFieldsByFieldNameResponseDefaultType0
    | DeleteFieldsByFieldNameResponseDefaultType1
]:
    """Delete a particular field by name


    Required roles:
     - can_delete_metadata_fields

    Args:
        field_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteFieldsByFieldNameResponseDefaultType0 | DeleteFieldsByFieldNameResponseDefaultType1]
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
) -> (
    Any
    | DeleteFieldsByFieldNameResponseDefaultType0
    | DeleteFieldsByFieldNameResponseDefaultType1
    | None
):
    """Delete a particular field by name


    Required roles:
     - can_delete_metadata_fields

    Args:
        field_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteFieldsByFieldNameResponseDefaultType0 | DeleteFieldsByFieldNameResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            field_name=field_name,
            client=client,
        )
    ).parsed
