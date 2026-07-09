from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bulk_delete_persons_by_versions_schema import (
    BulkDeletePersonsByVersionsSchema,
)
from ...models.delete_face_recognition_assets_by_asset_id_persons_bulk_response_default import (
    DeleteFaceRecognitionAssetsByAssetIdPersonsBulkResponseDefault,
)
from ...types import Response


def _get_kwargs(
    asset_id: str,
    *,
    body: BulkDeletePersonsByVersionsSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/face_recognition/assets/{asset_id}/persons/bulk/".format(
            asset_id=quote(str(asset_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DeleteFaceRecognitionAssetsByAssetIdPersonsBulkResponseDefault:
    if response.status_code == 201:
        response_201 = cast(Any, None)
        return response_201

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

    response_default = (
        DeleteFaceRecognitionAssetsByAssetIdPersonsBulkResponseDefault.from_dict(
            response.json()
        )
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DeleteFaceRecognitionAssetsByAssetIdPersonsBulkResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BulkDeletePersonsByVersionsSchema,
) -> Response[Any | DeleteFaceRecognitionAssetsByAssetIdPersonsBulkResponseDefault]:
    """Delete all persons by asset and versions


    Required roles:
     - can_delete_person

    Args:
        asset_id (str):
        body (BulkDeletePersonsByVersionsSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteFaceRecognitionAssetsByAssetIdPersonsBulkResponseDefault]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BulkDeletePersonsByVersionsSchema,
) -> Any | DeleteFaceRecognitionAssetsByAssetIdPersonsBulkResponseDefault | None:
    """Delete all persons by asset and versions


    Required roles:
     - can_delete_person

    Args:
        asset_id (str):
        body (BulkDeletePersonsByVersionsSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteFaceRecognitionAssetsByAssetIdPersonsBulkResponseDefault
    """

    return sync_detailed(
        asset_id=asset_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BulkDeletePersonsByVersionsSchema,
) -> Response[Any | DeleteFaceRecognitionAssetsByAssetIdPersonsBulkResponseDefault]:
    """Delete all persons by asset and versions


    Required roles:
     - can_delete_person

    Args:
        asset_id (str):
        body (BulkDeletePersonsByVersionsSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteFaceRecognitionAssetsByAssetIdPersonsBulkResponseDefault]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BulkDeletePersonsByVersionsSchema,
) -> Any | DeleteFaceRecognitionAssetsByAssetIdPersonsBulkResponseDefault | None:
    """Delete all persons by asset and versions


    Required roles:
     - can_delete_person

    Args:
        asset_id (str):
        body (BulkDeletePersonsByVersionsSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteFaceRecognitionAssetsByAssetIdPersonsBulkResponseDefault
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            client=client,
            body=body,
        )
    ).parsed
