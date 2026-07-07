from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.export_location_schema import ExportLocationSchema
from ...models.get_export_locations_by_export_location_id_response_default_type_0 import (
    GetExportLocationsByExportLocationIdResponseDefaultType0,
)
from ...models.get_export_locations_by_export_location_id_response_default_type_1 import (
    GetExportLocationsByExportLocationIdResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    export_location_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/export_locations/{export_location_id}/".format(
            export_location_id=quote(str(export_location_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | ExportLocationSchema
    | GetExportLocationsByExportLocationIdResponseDefaultType0
    | GetExportLocationsByExportLocationIdResponseDefaultType1
):
    if response.status_code == 200:
        response_200 = ExportLocationSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    def _parse_response_default(
        data: object,
    ) -> (
        GetExportLocationsByExportLocationIdResponseDefaultType0
        | GetExportLocationsByExportLocationIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetExportLocationsByExportLocationIdResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            GetExportLocationsByExportLocationIdResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | ExportLocationSchema
    | GetExportLocationsByExportLocationIdResponseDefaultType0
    | GetExportLocationsByExportLocationIdResponseDefaultType1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    export_location_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | ExportLocationSchema
    | GetExportLocationsByExportLocationIdResponseDefaultType0
    | GetExportLocationsByExportLocationIdResponseDefaultType1
]:
    """Returns a particular export_location by id


    Required roles:
     - can_read_export_locations

    Args:
        export_location_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ExportLocationSchema | GetExportLocationsByExportLocationIdResponseDefaultType0 | GetExportLocationsByExportLocationIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        export_location_id=export_location_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    export_location_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | ExportLocationSchema
    | GetExportLocationsByExportLocationIdResponseDefaultType0
    | GetExportLocationsByExportLocationIdResponseDefaultType1
    | None
):
    """Returns a particular export_location by id


    Required roles:
     - can_read_export_locations

    Args:
        export_location_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ExportLocationSchema | GetExportLocationsByExportLocationIdResponseDefaultType0 | GetExportLocationsByExportLocationIdResponseDefaultType1
    """

    return sync_detailed(
        export_location_id=export_location_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    export_location_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | ExportLocationSchema
    | GetExportLocationsByExportLocationIdResponseDefaultType0
    | GetExportLocationsByExportLocationIdResponseDefaultType1
]:
    """Returns a particular export_location by id


    Required roles:
     - can_read_export_locations

    Args:
        export_location_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ExportLocationSchema | GetExportLocationsByExportLocationIdResponseDefaultType0 | GetExportLocationsByExportLocationIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        export_location_id=export_location_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    export_location_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | ExportLocationSchema
    | GetExportLocationsByExportLocationIdResponseDefaultType0
    | GetExportLocationsByExportLocationIdResponseDefaultType1
    | None
):
    """Returns a particular export_location by id


    Required roles:
     - can_read_export_locations

    Args:
        export_location_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ExportLocationSchema | GetExportLocationsByExportLocationIdResponseDefaultType0 | GetExportLocationsByExportLocationIdResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            export_location_id=export_location_id,
            client=client,
        )
    ).parsed
