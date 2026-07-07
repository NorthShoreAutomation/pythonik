from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_face_recognition_persons_by_person_id_response_default_type_0 import (
    GetFaceRecognitionPersonsByPersonIdResponseDefaultType0,
)
from ...models.get_face_recognition_persons_by_person_id_response_default_type_1 import (
    GetFaceRecognitionPersonsByPersonIdResponseDefaultType1,
)
from ...models.person_schema import PersonSchema
from ...types import Response


def _get_kwargs(
    person_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/face_recognition/persons/{person_id}/".format(
            person_id=quote(str(person_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetFaceRecognitionPersonsByPersonIdResponseDefaultType0
    | GetFaceRecognitionPersonsByPersonIdResponseDefaultType1
    | PersonSchema
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
        GetFaceRecognitionPersonsByPersonIdResponseDefaultType0
        | GetFaceRecognitionPersonsByPersonIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetFaceRecognitionPersonsByPersonIdResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            GetFaceRecognitionPersonsByPersonIdResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetFaceRecognitionPersonsByPersonIdResponseDefaultType0
    | GetFaceRecognitionPersonsByPersonIdResponseDefaultType1
    | PersonSchema
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
) -> Response[
    Any
    | GetFaceRecognitionPersonsByPersonIdResponseDefaultType0
    | GetFaceRecognitionPersonsByPersonIdResponseDefaultType1
    | PersonSchema
]:
    """Get a single person by ID


    Required roles:
     - can_read_person

    Args:
        person_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetFaceRecognitionPersonsByPersonIdResponseDefaultType0 | GetFaceRecognitionPersonsByPersonIdResponseDefaultType1 | PersonSchema]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    person_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetFaceRecognitionPersonsByPersonIdResponseDefaultType0
    | GetFaceRecognitionPersonsByPersonIdResponseDefaultType1
    | PersonSchema
    | None
):
    """Get a single person by ID


    Required roles:
     - can_read_person

    Args:
        person_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetFaceRecognitionPersonsByPersonIdResponseDefaultType0 | GetFaceRecognitionPersonsByPersonIdResponseDefaultType1 | PersonSchema
    """

    return sync_detailed(
        person_id=person_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    person_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetFaceRecognitionPersonsByPersonIdResponseDefaultType0
    | GetFaceRecognitionPersonsByPersonIdResponseDefaultType1
    | PersonSchema
]:
    """Get a single person by ID


    Required roles:
     - can_read_person

    Args:
        person_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetFaceRecognitionPersonsByPersonIdResponseDefaultType0 | GetFaceRecognitionPersonsByPersonIdResponseDefaultType1 | PersonSchema]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    person_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetFaceRecognitionPersonsByPersonIdResponseDefaultType0
    | GetFaceRecognitionPersonsByPersonIdResponseDefaultType1
    | PersonSchema
    | None
):
    """Get a single person by ID


    Required roles:
     - can_read_person

    Args:
        person_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetFaceRecognitionPersonsByPersonIdResponseDefaultType0 | GetFaceRecognitionPersonsByPersonIdResponseDefaultType1 | PersonSchema
    """

    return (
        await asyncio_detailed(
            person_id=person_id,
            client=client,
        )
    ).parsed
