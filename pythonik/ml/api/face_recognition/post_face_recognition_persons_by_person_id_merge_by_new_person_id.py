from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_face_recognition_persons_by_person_id_merge_by_new_person_id_response_default import (
    PostFaceRecognitionPersonsByPersonIdMergeByNewPersonIdResponseDefault,
)
from ...types import Response


def _get_kwargs(
    person_id: str,
    new_person_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/face_recognition/persons/{person_id}/merge/{new_person_id}/".format(
            person_id=quote(str(person_id), safe=""),
            new_person_id=quote(str(new_person_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostFaceRecognitionPersonsByPersonIdMergeByNewPersonIdResponseDefault:
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

    response_default = (
        PostFaceRecognitionPersonsByPersonIdMergeByNewPersonIdResponseDefault.from_dict(
            response.json()
        )
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | PostFaceRecognitionPersonsByPersonIdMergeByNewPersonIdResponseDefault
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    person_id: str,
    new_person_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any | PostFaceRecognitionPersonsByPersonIdMergeByNewPersonIdResponseDefault
]:
    """Change an existing person to another person


    Required roles:
     - can_delete_person
    - can_edit_person
    - can_add_person

    Args:
        person_id (str):
        new_person_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostFaceRecognitionPersonsByPersonIdMergeByNewPersonIdResponseDefault]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        new_person_id=new_person_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    person_id: str,
    new_person_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | PostFaceRecognitionPersonsByPersonIdMergeByNewPersonIdResponseDefault | None:
    """Change an existing person to another person


    Required roles:
     - can_delete_person
    - can_edit_person
    - can_add_person

    Args:
        person_id (str):
        new_person_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostFaceRecognitionPersonsByPersonIdMergeByNewPersonIdResponseDefault
    """

    return sync_detailed(
        person_id=person_id,
        new_person_id=new_person_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    person_id: str,
    new_person_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any | PostFaceRecognitionPersonsByPersonIdMergeByNewPersonIdResponseDefault
]:
    """Change an existing person to another person


    Required roles:
     - can_delete_person
    - can_edit_person
    - can_add_person

    Args:
        person_id (str):
        new_person_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostFaceRecognitionPersonsByPersonIdMergeByNewPersonIdResponseDefault]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        new_person_id=new_person_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    person_id: str,
    new_person_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | PostFaceRecognitionPersonsByPersonIdMergeByNewPersonIdResponseDefault | None:
    """Change an existing person to another person


    Required roles:
     - can_delete_person
    - can_edit_person
    - can_add_person

    Args:
        person_id (str):
        new_person_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostFaceRecognitionPersonsByPersonIdMergeByNewPersonIdResponseDefault
    """

    return (
        await asyncio_detailed(
            person_id=person_id,
            new_person_id=new_person_id,
            client=client,
        )
    ).parsed
