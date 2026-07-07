from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_face_recognition_persons_response_default_type_0 import (
    GetFaceRecognitionPersonsResponseDefaultType0,
)
from ...models.get_face_recognition_persons_response_default_type_1 import (
    GetFaceRecognitionPersonsResponseDefaultType1,
)
from ...models.person_list_schema import PersonListSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    per_page: int | Unset = UNSET,
    page: int | Unset = 1,
    scroll: bool | Unset = UNSET,
    scroll_id: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    status: str | Unset = UNSET,
    name: str | Unset = UNSET,
    status_in: str | Unset = UNSET,
    has_name: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["per_page"] = per_page

    params["page"] = page

    params["scroll"] = scroll

    params["scroll_id"] = scroll_id

    params["sort"] = sort

    params["status"] = status

    params["name"] = name

    params["status_in"] = status_in

    params["has_name"] = has_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/face_recognition/persons/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetFaceRecognitionPersonsResponseDefaultType0
    | GetFaceRecognitionPersonsResponseDefaultType1
    | PersonListSchema
):
    if response.status_code == 200:
        response_200 = PersonListSchema.from_dict(response.json())

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
        GetFaceRecognitionPersonsResponseDefaultType0
        | GetFaceRecognitionPersonsResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetFaceRecognitionPersonsResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            GetFaceRecognitionPersonsResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetFaceRecognitionPersonsResponseDefaultType0
    | GetFaceRecognitionPersonsResponseDefaultType1
    | PersonListSchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    page: int | Unset = 1,
    scroll: bool | Unset = UNSET,
    scroll_id: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    status: str | Unset = UNSET,
    name: str | Unset = UNSET,
    status_in: str | Unset = UNSET,
    has_name: bool | Unset = UNSET,
) -> Response[
    Any
    | GetFaceRecognitionPersonsResponseDefaultType0
    | GetFaceRecognitionPersonsResponseDefaultType1
    | PersonListSchema
]:
    """Get all persons


    Required roles:
     - can_read_person

    Args:
        per_page (int | Unset):
        page (int | Unset):  Default: 1.
        scroll (bool | Unset):
        scroll_id (str | Unset):
        sort (str | Unset):
        status (str | Unset):
        name (str | Unset):
        status_in (str | Unset):
        has_name (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetFaceRecognitionPersonsResponseDefaultType0 | GetFaceRecognitionPersonsResponseDefaultType1 | PersonListSchema]
    """

    kwargs = _get_kwargs(
        per_page=per_page,
        page=page,
        scroll=scroll,
        scroll_id=scroll_id,
        sort=sort,
        status=status,
        name=name,
        status_in=status_in,
        has_name=has_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    page: int | Unset = 1,
    scroll: bool | Unset = UNSET,
    scroll_id: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    status: str | Unset = UNSET,
    name: str | Unset = UNSET,
    status_in: str | Unset = UNSET,
    has_name: bool | Unset = UNSET,
) -> (
    Any
    | GetFaceRecognitionPersonsResponseDefaultType0
    | GetFaceRecognitionPersonsResponseDefaultType1
    | PersonListSchema
    | None
):
    """Get all persons


    Required roles:
     - can_read_person

    Args:
        per_page (int | Unset):
        page (int | Unset):  Default: 1.
        scroll (bool | Unset):
        scroll_id (str | Unset):
        sort (str | Unset):
        status (str | Unset):
        name (str | Unset):
        status_in (str | Unset):
        has_name (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetFaceRecognitionPersonsResponseDefaultType0 | GetFaceRecognitionPersonsResponseDefaultType1 | PersonListSchema
    """

    return sync_detailed(
        client=client,
        per_page=per_page,
        page=page,
        scroll=scroll,
        scroll_id=scroll_id,
        sort=sort,
        status=status,
        name=name,
        status_in=status_in,
        has_name=has_name,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    page: int | Unset = 1,
    scroll: bool | Unset = UNSET,
    scroll_id: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    status: str | Unset = UNSET,
    name: str | Unset = UNSET,
    status_in: str | Unset = UNSET,
    has_name: bool | Unset = UNSET,
) -> Response[
    Any
    | GetFaceRecognitionPersonsResponseDefaultType0
    | GetFaceRecognitionPersonsResponseDefaultType1
    | PersonListSchema
]:
    """Get all persons


    Required roles:
     - can_read_person

    Args:
        per_page (int | Unset):
        page (int | Unset):  Default: 1.
        scroll (bool | Unset):
        scroll_id (str | Unset):
        sort (str | Unset):
        status (str | Unset):
        name (str | Unset):
        status_in (str | Unset):
        has_name (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetFaceRecognitionPersonsResponseDefaultType0 | GetFaceRecognitionPersonsResponseDefaultType1 | PersonListSchema]
    """

    kwargs = _get_kwargs(
        per_page=per_page,
        page=page,
        scroll=scroll,
        scroll_id=scroll_id,
        sort=sort,
        status=status,
        name=name,
        status_in=status_in,
        has_name=has_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    page: int | Unset = 1,
    scroll: bool | Unset = UNSET,
    scroll_id: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    status: str | Unset = UNSET,
    name: str | Unset = UNSET,
    status_in: str | Unset = UNSET,
    has_name: bool | Unset = UNSET,
) -> (
    Any
    | GetFaceRecognitionPersonsResponseDefaultType0
    | GetFaceRecognitionPersonsResponseDefaultType1
    | PersonListSchema
    | None
):
    """Get all persons


    Required roles:
     - can_read_person

    Args:
        per_page (int | Unset):
        page (int | Unset):  Default: 1.
        scroll (bool | Unset):
        scroll_id (str | Unset):
        sort (str | Unset):
        status (str | Unset):
        name (str | Unset):
        status_in (str | Unset):
        has_name (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetFaceRecognitionPersonsResponseDefaultType0 | GetFaceRecognitionPersonsResponseDefaultType1 | PersonListSchema
    """

    return (
        await asyncio_detailed(
            client=client,
            per_page=per_page,
            page=page,
            scroll=scroll,
            scroll_id=scroll_id,
            sort=sort,
            status=status,
            name=name,
            status_in=status_in,
            has_name=has_name,
        )
    ).parsed
