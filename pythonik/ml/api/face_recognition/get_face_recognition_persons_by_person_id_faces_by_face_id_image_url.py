from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_face_recognition_persons_by_person_id_faces_by_face_id_image_url_response_default_type_0 import (
    GetFaceRecognitionPersonsByPersonIdFacesByFaceIdImageUrlResponseDefaultType0,
)
from ...models.get_face_recognition_persons_by_person_id_faces_by_face_id_image_url_response_default_type_1 import (
    GetFaceRecognitionPersonsByPersonIdFacesByFaceIdImageUrlResponseDefaultType1,
)
from ...models.url_schema import URLSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    person_id: str,
    face_id: str,
    *,
    storage_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["storage_id"] = storage_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/face_recognition/persons/{person_id}/faces/{face_id}/image_url/".format(
            person_id=quote(str(person_id), safe=""),
            face_id=quote(str(face_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetFaceRecognitionPersonsByPersonIdFacesByFaceIdImageUrlResponseDefaultType0
    | GetFaceRecognitionPersonsByPersonIdFacesByFaceIdImageUrlResponseDefaultType1
    | URLSchema
):
    if response.status_code == 200:
        response_200 = URLSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    def _parse_response_default(
        data: object,
    ) -> (
        GetFaceRecognitionPersonsByPersonIdFacesByFaceIdImageUrlResponseDefaultType0
        | GetFaceRecognitionPersonsByPersonIdFacesByFaceIdImageUrlResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = GetFaceRecognitionPersonsByPersonIdFacesByFaceIdImageUrlResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = GetFaceRecognitionPersonsByPersonIdFacesByFaceIdImageUrlResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetFaceRecognitionPersonsByPersonIdFacesByFaceIdImageUrlResponseDefaultType0
    | GetFaceRecognitionPersonsByPersonIdFacesByFaceIdImageUrlResponseDefaultType1
    | URLSchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    person_id: str,
    face_id: str,
    *,
    client: AuthenticatedClient | Client,
    storage_id: str | Unset = UNSET,
) -> Response[
    Any
    | GetFaceRecognitionPersonsByPersonIdFacesByFaceIdImageUrlResponseDefaultType0
    | GetFaceRecognitionPersonsByPersonIdFacesByFaceIdImageUrlResponseDefaultType1
    | URLSchema
]:
    """Get a presigned URL for a face image

    Args:
        person_id (str):
        face_id (str):
        storage_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetFaceRecognitionPersonsByPersonIdFacesByFaceIdImageUrlResponseDefaultType0 | GetFaceRecognitionPersonsByPersonIdFacesByFaceIdImageUrlResponseDefaultType1 | URLSchema]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        face_id=face_id,
        storage_id=storage_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    person_id: str,
    face_id: str,
    *,
    client: AuthenticatedClient | Client,
    storage_id: str | Unset = UNSET,
) -> (
    Any
    | GetFaceRecognitionPersonsByPersonIdFacesByFaceIdImageUrlResponseDefaultType0
    | GetFaceRecognitionPersonsByPersonIdFacesByFaceIdImageUrlResponseDefaultType1
    | URLSchema
    | None
):
    """Get a presigned URL for a face image

    Args:
        person_id (str):
        face_id (str):
        storage_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetFaceRecognitionPersonsByPersonIdFacesByFaceIdImageUrlResponseDefaultType0 | GetFaceRecognitionPersonsByPersonIdFacesByFaceIdImageUrlResponseDefaultType1 | URLSchema
    """

    return sync_detailed(
        person_id=person_id,
        face_id=face_id,
        client=client,
        storage_id=storage_id,
    ).parsed


async def asyncio_detailed(
    person_id: str,
    face_id: str,
    *,
    client: AuthenticatedClient | Client,
    storage_id: str | Unset = UNSET,
) -> Response[
    Any
    | GetFaceRecognitionPersonsByPersonIdFacesByFaceIdImageUrlResponseDefaultType0
    | GetFaceRecognitionPersonsByPersonIdFacesByFaceIdImageUrlResponseDefaultType1
    | URLSchema
]:
    """Get a presigned URL for a face image

    Args:
        person_id (str):
        face_id (str):
        storage_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetFaceRecognitionPersonsByPersonIdFacesByFaceIdImageUrlResponseDefaultType0 | GetFaceRecognitionPersonsByPersonIdFacesByFaceIdImageUrlResponseDefaultType1 | URLSchema]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        face_id=face_id,
        storage_id=storage_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    person_id: str,
    face_id: str,
    *,
    client: AuthenticatedClient | Client,
    storage_id: str | Unset = UNSET,
) -> (
    Any
    | GetFaceRecognitionPersonsByPersonIdFacesByFaceIdImageUrlResponseDefaultType0
    | GetFaceRecognitionPersonsByPersonIdFacesByFaceIdImageUrlResponseDefaultType1
    | URLSchema
    | None
):
    """Get a presigned URL for a face image

    Args:
        person_id (str):
        face_id (str):
        storage_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetFaceRecognitionPersonsByPersonIdFacesByFaceIdImageUrlResponseDefaultType0 | GetFaceRecognitionPersonsByPersonIdFacesByFaceIdImageUrlResponseDefaultType1 | URLSchema
    """

    return (
        await asyncio_detailed(
            person_id=person_id,
            face_id=face_id,
            client=client,
            storage_id=storage_id,
        )
    ).parsed
