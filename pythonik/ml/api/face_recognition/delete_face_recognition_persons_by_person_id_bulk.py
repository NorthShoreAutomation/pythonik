from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bulk_delete_persons_schema import BulkDeletePersonsSchema
from ...models.delete_face_recognition_persons_by_person_id_bulk_response_default_type_0 import (
    DeleteFaceRecognitionPersonsByPersonIdBulkResponseDefaultType0,
)
from ...models.delete_face_recognition_persons_by_person_id_bulk_response_default_type_1 import (
    DeleteFaceRecognitionPersonsByPersonIdBulkResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    person_id: str,
    *,
    body: BulkDeletePersonsSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/face_recognition/persons/{person_id}/bulk/".format(
            person_id=quote(str(person_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | DeleteFaceRecognitionPersonsByPersonIdBulkResponseDefaultType0
    | DeleteFaceRecognitionPersonsByPersonIdBulkResponseDefaultType1
):
    if response.status_code == 201:
        response_201 = cast(Any, None)
        return response_201

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
        DeleteFaceRecognitionPersonsByPersonIdBulkResponseDefaultType0
        | DeleteFaceRecognitionPersonsByPersonIdBulkResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = DeleteFaceRecognitionPersonsByPersonIdBulkResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            DeleteFaceRecognitionPersonsByPersonIdBulkResponseDefaultType1.from_dict(
                data
            )
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | DeleteFaceRecognitionPersonsByPersonIdBulkResponseDefaultType0
    | DeleteFaceRecognitionPersonsByPersonIdBulkResponseDefaultType1
]:
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
    body: BulkDeletePersonsSchema,
) -> Response[
    Any
    | DeleteFaceRecognitionPersonsByPersonIdBulkResponseDefaultType0
    | DeleteFaceRecognitionPersonsByPersonIdBulkResponseDefaultType1
]:
    """Delete a persons's instances in bulk


    Required roles:
     - can_delete_person

    Args:
        person_id (str):
        body (BulkDeletePersonsSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteFaceRecognitionPersonsByPersonIdBulkResponseDefaultType0 | DeleteFaceRecognitionPersonsByPersonIdBulkResponseDefaultType1]
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
    body: BulkDeletePersonsSchema,
) -> (
    Any
    | DeleteFaceRecognitionPersonsByPersonIdBulkResponseDefaultType0
    | DeleteFaceRecognitionPersonsByPersonIdBulkResponseDefaultType1
    | None
):
    """Delete a persons's instances in bulk


    Required roles:
     - can_delete_person

    Args:
        person_id (str):
        body (BulkDeletePersonsSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteFaceRecognitionPersonsByPersonIdBulkResponseDefaultType0 | DeleteFaceRecognitionPersonsByPersonIdBulkResponseDefaultType1
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
    body: BulkDeletePersonsSchema,
) -> Response[
    Any
    | DeleteFaceRecognitionPersonsByPersonIdBulkResponseDefaultType0
    | DeleteFaceRecognitionPersonsByPersonIdBulkResponseDefaultType1
]:
    """Delete a persons's instances in bulk


    Required roles:
     - can_delete_person

    Args:
        person_id (str):
        body (BulkDeletePersonsSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteFaceRecognitionPersonsByPersonIdBulkResponseDefaultType0 | DeleteFaceRecognitionPersonsByPersonIdBulkResponseDefaultType1]
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
    body: BulkDeletePersonsSchema,
) -> (
    Any
    | DeleteFaceRecognitionPersonsByPersonIdBulkResponseDefaultType0
    | DeleteFaceRecognitionPersonsByPersonIdBulkResponseDefaultType1
    | None
):
    """Delete a persons's instances in bulk


    Required roles:
     - can_delete_person

    Args:
        person_id (str):
        body (BulkDeletePersonsSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteFaceRecognitionPersonsByPersonIdBulkResponseDefaultType0 | DeleteFaceRecognitionPersonsByPersonIdBulkResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            person_id=person_id,
            client=client,
            body=body,
        )
    ).parsed
