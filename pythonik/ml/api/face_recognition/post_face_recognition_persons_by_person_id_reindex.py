from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_face_recognition_persons_by_person_id_reindex_response_default_type_0 import (
    PostFaceRecognitionPersonsByPersonIdReindexResponseDefaultType0,
)
from ...models.post_face_recognition_persons_by_person_id_reindex_response_default_type_1 import (
    PostFaceRecognitionPersonsByPersonIdReindexResponseDefaultType1,
)
from ...models.reindex_person_schema import ReindexPersonSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    person_id: str,
    *,
    body: ReindexPersonSchema | Unset = UNSET,
    sync_assets: bool | Unset = UNSET,
    low_priority_indexing: bool | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["sync_assets"] = sync_assets

    params["low_priority_indexing"] = low_priority_indexing

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/face_recognition/persons/{person_id}/reindex/".format(
            person_id=quote(str(person_id), safe=""),
        ),
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | PostFaceRecognitionPersonsByPersonIdReindexResponseDefaultType0
    | PostFaceRecognitionPersonsByPersonIdReindexResponseDefaultType1
):
    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    def _parse_response_default(
        data: object,
    ) -> (
        PostFaceRecognitionPersonsByPersonIdReindexResponseDefaultType0
        | PostFaceRecognitionPersonsByPersonIdReindexResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = PostFaceRecognitionPersonsByPersonIdReindexResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PostFaceRecognitionPersonsByPersonIdReindexResponseDefaultType1.from_dict(
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
    | PostFaceRecognitionPersonsByPersonIdReindexResponseDefaultType0
    | PostFaceRecognitionPersonsByPersonIdReindexResponseDefaultType1
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
    body: ReindexPersonSchema | Unset = UNSET,
    sync_assets: bool | Unset = UNSET,
    low_priority_indexing: bool | Unset = UNSET,
) -> Response[
    Any
    | PostFaceRecognitionPersonsByPersonIdReindexResponseDefaultType0
    | PostFaceRecognitionPersonsByPersonIdReindexResponseDefaultType1
]:
    """Reindex person


    Required roles:
     - can_reindex_person

    Args:
        person_id (str):
        sync_assets (bool | Unset):
        low_priority_indexing (bool | Unset):
        body (ReindexPersonSchema | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostFaceRecognitionPersonsByPersonIdReindexResponseDefaultType0 | PostFaceRecognitionPersonsByPersonIdReindexResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        body=body,
        sync_assets=sync_assets,
        low_priority_indexing=low_priority_indexing,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    person_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ReindexPersonSchema | Unset = UNSET,
    sync_assets: bool | Unset = UNSET,
    low_priority_indexing: bool | Unset = UNSET,
) -> (
    Any
    | PostFaceRecognitionPersonsByPersonIdReindexResponseDefaultType0
    | PostFaceRecognitionPersonsByPersonIdReindexResponseDefaultType1
    | None
):
    """Reindex person


    Required roles:
     - can_reindex_person

    Args:
        person_id (str):
        sync_assets (bool | Unset):
        low_priority_indexing (bool | Unset):
        body (ReindexPersonSchema | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostFaceRecognitionPersonsByPersonIdReindexResponseDefaultType0 | PostFaceRecognitionPersonsByPersonIdReindexResponseDefaultType1
    """

    return sync_detailed(
        person_id=person_id,
        client=client,
        body=body,
        sync_assets=sync_assets,
        low_priority_indexing=low_priority_indexing,
    ).parsed


async def asyncio_detailed(
    person_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ReindexPersonSchema | Unset = UNSET,
    sync_assets: bool | Unset = UNSET,
    low_priority_indexing: bool | Unset = UNSET,
) -> Response[
    Any
    | PostFaceRecognitionPersonsByPersonIdReindexResponseDefaultType0
    | PostFaceRecognitionPersonsByPersonIdReindexResponseDefaultType1
]:
    """Reindex person


    Required roles:
     - can_reindex_person

    Args:
        person_id (str):
        sync_assets (bool | Unset):
        low_priority_indexing (bool | Unset):
        body (ReindexPersonSchema | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostFaceRecognitionPersonsByPersonIdReindexResponseDefaultType0 | PostFaceRecognitionPersonsByPersonIdReindexResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        body=body,
        sync_assets=sync_assets,
        low_priority_indexing=low_priority_indexing,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    person_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ReindexPersonSchema | Unset = UNSET,
    sync_assets: bool | Unset = UNSET,
    low_priority_indexing: bool | Unset = UNSET,
) -> (
    Any
    | PostFaceRecognitionPersonsByPersonIdReindexResponseDefaultType0
    | PostFaceRecognitionPersonsByPersonIdReindexResponseDefaultType1
    | None
):
    """Reindex person


    Required roles:
     - can_reindex_person

    Args:
        person_id (str):
        sync_assets (bool | Unset):
        low_priority_indexing (bool | Unset):
        body (ReindexPersonSchema | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostFaceRecognitionPersonsByPersonIdReindexResponseDefaultType0 | PostFaceRecognitionPersonsByPersonIdReindexResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            person_id=person_id,
            client=client,
            body=body,
            sync_assets=sync_assets,
            low_priority_indexing=low_priority_indexing,
        )
    ).parsed
