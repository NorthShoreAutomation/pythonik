from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bulk_face_extract_schema import BulkFaceExtractSchema
from ...models.post_face_recognition_bulk_extract_response_default import (
    PostFaceRecognitionBulkExtractResponseDefault,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: BulkFaceExtractSchema | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/face_recognition/bulk/extract/",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostFaceRecognitionBulkExtractResponseDefault:
    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    response_default = PostFaceRecognitionBulkExtractResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PostFaceRecognitionBulkExtractResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BulkFaceExtractSchema | Unset = UNSET,
) -> Response[Any | PostFaceRecognitionBulkExtractResponseDefault]:
    """Run face recognition in bulk for different object types


    Required roles:
     - can_trigger_face_recognition

    Args:
        body (BulkFaceExtractSchema | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostFaceRecognitionBulkExtractResponseDefault]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: BulkFaceExtractSchema | Unset = UNSET,
) -> Any | PostFaceRecognitionBulkExtractResponseDefault | None:
    """Run face recognition in bulk for different object types


    Required roles:
     - can_trigger_face_recognition

    Args:
        body (BulkFaceExtractSchema | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostFaceRecognitionBulkExtractResponseDefault
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BulkFaceExtractSchema | Unset = UNSET,
) -> Response[Any | PostFaceRecognitionBulkExtractResponseDefault]:
    """Run face recognition in bulk for different object types


    Required roles:
     - can_trigger_face_recognition

    Args:
        body (BulkFaceExtractSchema | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostFaceRecognitionBulkExtractResponseDefault]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: BulkFaceExtractSchema | Unset = UNSET,
) -> Any | PostFaceRecognitionBulkExtractResponseDefault | None:
    """Run face recognition in bulk for different object types


    Required roles:
     - can_trigger_face_recognition

    Args:
        body (BulkFaceExtractSchema | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostFaceRecognitionBulkExtractResponseDefault
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
