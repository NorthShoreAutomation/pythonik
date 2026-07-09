from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_face_recognition_persons_by_person_id_versions_response_default import (
    GetFaceRecognitionPersonsByPersonIdVersionsResponseDefault,
)
from ...models.person_assets_versions_list_schema import PersonAssetsVersionsListSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    person_id: str,
    *,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
    include_admin_details: bool | Unset = UNSET,
    use_instance_as_main_face: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["per_page"] = per_page

    params["page"] = page

    params["include_admin_details"] = include_admin_details

    params["use_instance_as_main_face"] = use_instance_as_main_face

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/face_recognition/persons/{person_id}/versions/".format(
            person_id=quote(str(person_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetFaceRecognitionPersonsByPersonIdVersionsResponseDefault
    | PersonAssetsVersionsListSchema
):
    if response.status_code == 200:
        response_200 = PersonAssetsVersionsListSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = (
        GetFaceRecognitionPersonsByPersonIdVersionsResponseDefault.from_dict(
            response.json()
        )
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetFaceRecognitionPersonsByPersonIdVersionsResponseDefault
    | PersonAssetsVersionsListSchema
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
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
    include_admin_details: bool | Unset = UNSET,
    use_instance_as_main_face: bool | Unset = UNSET,
) -> Response[
    Any
    | GetFaceRecognitionPersonsByPersonIdVersionsResponseDefault
    | PersonAssetsVersionsListSchema
]:
    """List all person_id instances across assets versions


    Required roles:
     - can_read_person

    Args:
        person_id (str):
        per_page (int | Unset):
        page (int | Unset):
        include_admin_details (bool | Unset):
        use_instance_as_main_face (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetFaceRecognitionPersonsByPersonIdVersionsResponseDefault | PersonAssetsVersionsListSchema]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        per_page=per_page,
        page=page,
        include_admin_details=include_admin_details,
        use_instance_as_main_face=use_instance_as_main_face,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    person_id: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
    include_admin_details: bool | Unset = UNSET,
    use_instance_as_main_face: bool | Unset = UNSET,
) -> (
    Any
    | GetFaceRecognitionPersonsByPersonIdVersionsResponseDefault
    | PersonAssetsVersionsListSchema
    | None
):
    """List all person_id instances across assets versions


    Required roles:
     - can_read_person

    Args:
        person_id (str):
        per_page (int | Unset):
        page (int | Unset):
        include_admin_details (bool | Unset):
        use_instance_as_main_face (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetFaceRecognitionPersonsByPersonIdVersionsResponseDefault | PersonAssetsVersionsListSchema
    """

    return sync_detailed(
        person_id=person_id,
        client=client,
        per_page=per_page,
        page=page,
        include_admin_details=include_admin_details,
        use_instance_as_main_face=use_instance_as_main_face,
    ).parsed


async def asyncio_detailed(
    person_id: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
    include_admin_details: bool | Unset = UNSET,
    use_instance_as_main_face: bool | Unset = UNSET,
) -> Response[
    Any
    | GetFaceRecognitionPersonsByPersonIdVersionsResponseDefault
    | PersonAssetsVersionsListSchema
]:
    """List all person_id instances across assets versions


    Required roles:
     - can_read_person

    Args:
        person_id (str):
        per_page (int | Unset):
        page (int | Unset):
        include_admin_details (bool | Unset):
        use_instance_as_main_face (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetFaceRecognitionPersonsByPersonIdVersionsResponseDefault | PersonAssetsVersionsListSchema]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        per_page=per_page,
        page=page,
        include_admin_details=include_admin_details,
        use_instance_as_main_face=use_instance_as_main_face,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    person_id: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
    include_admin_details: bool | Unset = UNSET,
    use_instance_as_main_face: bool | Unset = UNSET,
) -> (
    Any
    | GetFaceRecognitionPersonsByPersonIdVersionsResponseDefault
    | PersonAssetsVersionsListSchema
    | None
):
    """List all person_id instances across assets versions


    Required roles:
     - can_read_person

    Args:
        person_id (str):
        per_page (int | Unset):
        page (int | Unset):
        include_admin_details (bool | Unset):
        use_instance_as_main_face (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetFaceRecognitionPersonsByPersonIdVersionsResponseDefault | PersonAssetsVersionsListSchema
    """

    return (
        await asyncio_detailed(
            person_id=person_id,
            client=client,
            per_page=per_page,
            page=page,
            include_admin_details=include_admin_details,
            use_instance_as_main_face=use_instance_as_main_face,
        )
    ).parsed
