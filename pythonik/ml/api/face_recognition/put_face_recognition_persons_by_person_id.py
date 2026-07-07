from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.person_schema import PersonSchema
from ...models.put_face_recognition_persons_by_person_id_response_default_type_0 import (
    PutFaceRecognitionPersonsByPersonIdResponseDefaultType0,
)
from ...models.put_face_recognition_persons_by_person_id_response_default_type_1 import (
    PutFaceRecognitionPersonsByPersonIdResponseDefaultType1,
)
from ...models.update_person_schema import UpdatePersonSchema
from ...types import Response


def _get_kwargs(
    person_id: str,
    *,
    body: UpdatePersonSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/face_recognition/persons/{person_id}/".format(
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
    | PersonSchema
    | PutFaceRecognitionPersonsByPersonIdResponseDefaultType0
    | PutFaceRecognitionPersonsByPersonIdResponseDefaultType1
):
    if response.status_code == 200:
        response_200 = PersonSchema.from_dict(response.json())

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

    def _parse_response_default(
        data: object,
    ) -> (
        PutFaceRecognitionPersonsByPersonIdResponseDefaultType0
        | PutFaceRecognitionPersonsByPersonIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                PutFaceRecognitionPersonsByPersonIdResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PutFaceRecognitionPersonsByPersonIdResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PersonSchema
    | PutFaceRecognitionPersonsByPersonIdResponseDefaultType0
    | PutFaceRecognitionPersonsByPersonIdResponseDefaultType1
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
    body: UpdatePersonSchema,
) -> Response[
    Any
    | PersonSchema
    | PutFaceRecognitionPersonsByPersonIdResponseDefaultType0
    | PutFaceRecognitionPersonsByPersonIdResponseDefaultType1
]:
    """Update an existing person


    Required roles:
     - can_edit_person

    Args:
        person_id (str):
        body (UpdatePersonSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PersonSchema | PutFaceRecognitionPersonsByPersonIdResponseDefaultType0 | PutFaceRecognitionPersonsByPersonIdResponseDefaultType1]
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
    body: UpdatePersonSchema,
) -> (
    Any
    | PersonSchema
    | PutFaceRecognitionPersonsByPersonIdResponseDefaultType0
    | PutFaceRecognitionPersonsByPersonIdResponseDefaultType1
    | None
):
    """Update an existing person


    Required roles:
     - can_edit_person

    Args:
        person_id (str):
        body (UpdatePersonSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PersonSchema | PutFaceRecognitionPersonsByPersonIdResponseDefaultType0 | PutFaceRecognitionPersonsByPersonIdResponseDefaultType1
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
    body: UpdatePersonSchema,
) -> Response[
    Any
    | PersonSchema
    | PutFaceRecognitionPersonsByPersonIdResponseDefaultType0
    | PutFaceRecognitionPersonsByPersonIdResponseDefaultType1
]:
    """Update an existing person


    Required roles:
     - can_edit_person

    Args:
        person_id (str):
        body (UpdatePersonSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PersonSchema | PutFaceRecognitionPersonsByPersonIdResponseDefaultType0 | PutFaceRecognitionPersonsByPersonIdResponseDefaultType1]
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
    body: UpdatePersonSchema,
) -> (
    Any
    | PersonSchema
    | PutFaceRecognitionPersonsByPersonIdResponseDefaultType0
    | PutFaceRecognitionPersonsByPersonIdResponseDefaultType1
    | None
):
    """Update an existing person


    Required roles:
     - can_edit_person

    Args:
        person_id (str):
        body (UpdatePersonSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PersonSchema | PutFaceRecognitionPersonsByPersonIdResponseDefaultType0 | PutFaceRecognitionPersonsByPersonIdResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            person_id=person_id,
            client=client,
            body=body,
        )
    ).parsed
