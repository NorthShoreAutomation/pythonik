from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.person_schema import PersonSchema
from ...models.post_face_recognition_persons_by_person_id_update_and_confirm_response_default import (
    PostFaceRecognitionPersonsByPersonIdUpdateAndConfirmResponseDefault,
)
from ...models.update_confirm_person_schema import UpdateConfirmPersonSchema
from ...types import Response


def _get_kwargs(
    person_id: str,
    *,
    body: UpdateConfirmPersonSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/face_recognition/persons/{person_id}/update_and_confirm/".format(
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
    | PostFaceRecognitionPersonsByPersonIdUpdateAndConfirmResponseDefault
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

    response_default = (
        PostFaceRecognitionPersonsByPersonIdUpdateAndConfirmResponseDefault.from_dict(
            response.json()
        )
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PersonSchema
    | PostFaceRecognitionPersonsByPersonIdUpdateAndConfirmResponseDefault
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
    body: UpdateConfirmPersonSchema,
) -> Response[
    Any
    | PersonSchema
    | PostFaceRecognitionPersonsByPersonIdUpdateAndConfirmResponseDefault
]:
    """Updates person with name and confirms instances in bulk


    Required roles:
     - can_delete_person
    - can_edit_person

    Args:
        person_id (str):
        body (UpdateConfirmPersonSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PersonSchema | PostFaceRecognitionPersonsByPersonIdUpdateAndConfirmResponseDefault]
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
    body: UpdateConfirmPersonSchema,
) -> (
    Any
    | PersonSchema
    | PostFaceRecognitionPersonsByPersonIdUpdateAndConfirmResponseDefault
    | None
):
    """Updates person with name and confirms instances in bulk


    Required roles:
     - can_delete_person
    - can_edit_person

    Args:
        person_id (str):
        body (UpdateConfirmPersonSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PersonSchema | PostFaceRecognitionPersonsByPersonIdUpdateAndConfirmResponseDefault
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
    body: UpdateConfirmPersonSchema,
) -> Response[
    Any
    | PersonSchema
    | PostFaceRecognitionPersonsByPersonIdUpdateAndConfirmResponseDefault
]:
    """Updates person with name and confirms instances in bulk


    Required roles:
     - can_delete_person
    - can_edit_person

    Args:
        person_id (str):
        body (UpdateConfirmPersonSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PersonSchema | PostFaceRecognitionPersonsByPersonIdUpdateAndConfirmResponseDefault]
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
    body: UpdateConfirmPersonSchema,
) -> (
    Any
    | PersonSchema
    | PostFaceRecognitionPersonsByPersonIdUpdateAndConfirmResponseDefault
    | None
):
    """Updates person with name and confirms instances in bulk


    Required roles:
     - can_delete_person
    - can_edit_person

    Args:
        person_id (str):
        body (UpdateConfirmPersonSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PersonSchema | PostFaceRecognitionPersonsByPersonIdUpdateAndConfirmResponseDefault
    """

    return (
        await asyncio_detailed(
            person_id=person_id,
            client=client,
            body=body,
        )
    ).parsed
