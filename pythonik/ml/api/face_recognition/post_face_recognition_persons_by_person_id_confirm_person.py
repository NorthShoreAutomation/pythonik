from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bulk_confirm_person_schema import BulkConfirmPersonSchema
from ...models.post_face_recognition_persons_by_person_id_confirm_person_response_default import (
    PostFaceRecognitionPersonsByPersonIdConfirmPersonResponseDefault,
)
from ...types import Response


def _get_kwargs(
    person_id: str,
    *,
    body: BulkConfirmPersonSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/face_recognition/persons/{person_id}/confirm_person/".format(
            person_id=quote(str(person_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostFaceRecognitionPersonsByPersonIdConfirmPersonResponseDefault:
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
        PostFaceRecognitionPersonsByPersonIdConfirmPersonResponseDefault.from_dict(
            response.json()
        )
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PostFaceRecognitionPersonsByPersonIdConfirmPersonResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    person_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BulkConfirmPersonSchema,
) -> Response[Any | PostFaceRecognitionPersonsByPersonIdConfirmPersonResponseDefault]:
    """Confirms multiple person instances in bulk


    Required roles:
     - can_delete_person
    - can_edit_person

    Args:
        person_id (str):
        body (BulkConfirmPersonSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostFaceRecognitionPersonsByPersonIdConfirmPersonResponseDefault]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    person_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BulkConfirmPersonSchema,
) -> Any | PostFaceRecognitionPersonsByPersonIdConfirmPersonResponseDefault | None:
    """Confirms multiple person instances in bulk


    Required roles:
     - can_delete_person
    - can_edit_person

    Args:
        person_id (str):
        body (BulkConfirmPersonSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostFaceRecognitionPersonsByPersonIdConfirmPersonResponseDefault
    """

    return sync_detailed(
        person_id=person_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    person_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BulkConfirmPersonSchema,
) -> Response[Any | PostFaceRecognitionPersonsByPersonIdConfirmPersonResponseDefault]:
    """Confirms multiple person instances in bulk


    Required roles:
     - can_delete_person
    - can_edit_person

    Args:
        person_id (str):
        body (BulkConfirmPersonSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostFaceRecognitionPersonsByPersonIdConfirmPersonResponseDefault]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    person_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BulkConfirmPersonSchema,
) -> Any | PostFaceRecognitionPersonsByPersonIdConfirmPersonResponseDefault | None:
    """Confirms multiple person instances in bulk


    Required roles:
     - can_delete_person
    - can_edit_person

    Args:
        person_id (str):
        body (BulkConfirmPersonSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostFaceRecognitionPersonsByPersonIdConfirmPersonResponseDefault
    """

    return (
        await asyncio_detailed(
            person_id=person_id,
            client=client,
            body=body,
        )
    ).parsed
