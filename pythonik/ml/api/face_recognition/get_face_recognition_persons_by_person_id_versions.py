from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_face_recognition_persons_by_person_id_versions_response_default_type_0 import (
    GetFaceRecognitionPersonsByPersonIdVersionsResponseDefaultType0,
)
from ...models.get_face_recognition_persons_by_person_id_versions_response_default_type_1 import (
    GetFaceRecognitionPersonsByPersonIdVersionsResponseDefaultType1,
)
from ...models.person_assets_versions_list_schema import PersonAssetsVersionsListSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    person_id: str,
    *,
    per_page: int | Unset = UNSET,
    page: int | Unset = 1,
    include_admin_details: bool | Unset = True,
    use_instance_as_main_face: bool | Unset = True,
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
    | GetFaceRecognitionPersonsByPersonIdVersionsResponseDefaultType0
    | GetFaceRecognitionPersonsByPersonIdVersionsResponseDefaultType1
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

    def _parse_response_default(
        data: object,
    ) -> (
        GetFaceRecognitionPersonsByPersonIdVersionsResponseDefaultType0
        | GetFaceRecognitionPersonsByPersonIdVersionsResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = GetFaceRecognitionPersonsByPersonIdVersionsResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            GetFaceRecognitionPersonsByPersonIdVersionsResponseDefaultType1.from_dict(
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
    | GetFaceRecognitionPersonsByPersonIdVersionsResponseDefaultType0
    | GetFaceRecognitionPersonsByPersonIdVersionsResponseDefaultType1
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
    page: int | Unset = 1,
    include_admin_details: bool | Unset = True,
    use_instance_as_main_face: bool | Unset = True,
) -> Response[
    Any
    | GetFaceRecognitionPersonsByPersonIdVersionsResponseDefaultType0
    | GetFaceRecognitionPersonsByPersonIdVersionsResponseDefaultType1
    | PersonAssetsVersionsListSchema
]:
    """List all person_id instances across assets versions


    Required roles:
     - can_read_person

    Args:
        person_id (str):
        per_page (int | Unset):
        page (int | Unset):  Default: 1.
        include_admin_details (bool | Unset):  Default: True.
        use_instance_as_main_face (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetFaceRecognitionPersonsByPersonIdVersionsResponseDefaultType0 | GetFaceRecognitionPersonsByPersonIdVersionsResponseDefaultType1 | PersonAssetsVersionsListSchema]
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
    page: int | Unset = 1,
    include_admin_details: bool | Unset = True,
    use_instance_as_main_face: bool | Unset = True,
) -> (
    Any
    | GetFaceRecognitionPersonsByPersonIdVersionsResponseDefaultType0
    | GetFaceRecognitionPersonsByPersonIdVersionsResponseDefaultType1
    | PersonAssetsVersionsListSchema
    | None
):
    """List all person_id instances across assets versions


    Required roles:
     - can_read_person

    Args:
        person_id (str):
        per_page (int | Unset):
        page (int | Unset):  Default: 1.
        include_admin_details (bool | Unset):  Default: True.
        use_instance_as_main_face (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetFaceRecognitionPersonsByPersonIdVersionsResponseDefaultType0 | GetFaceRecognitionPersonsByPersonIdVersionsResponseDefaultType1 | PersonAssetsVersionsListSchema
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
    page: int | Unset = 1,
    include_admin_details: bool | Unset = True,
    use_instance_as_main_face: bool | Unset = True,
) -> Response[
    Any
    | GetFaceRecognitionPersonsByPersonIdVersionsResponseDefaultType0
    | GetFaceRecognitionPersonsByPersonIdVersionsResponseDefaultType1
    | PersonAssetsVersionsListSchema
]:
    """List all person_id instances across assets versions


    Required roles:
     - can_read_person

    Args:
        person_id (str):
        per_page (int | Unset):
        page (int | Unset):  Default: 1.
        include_admin_details (bool | Unset):  Default: True.
        use_instance_as_main_face (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetFaceRecognitionPersonsByPersonIdVersionsResponseDefaultType0 | GetFaceRecognitionPersonsByPersonIdVersionsResponseDefaultType1 | PersonAssetsVersionsListSchema]
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
    page: int | Unset = 1,
    include_admin_details: bool | Unset = True,
    use_instance_as_main_face: bool | Unset = True,
) -> (
    Any
    | GetFaceRecognitionPersonsByPersonIdVersionsResponseDefaultType0
    | GetFaceRecognitionPersonsByPersonIdVersionsResponseDefaultType1
    | PersonAssetsVersionsListSchema
    | None
):
    """List all person_id instances across assets versions


    Required roles:
     - can_read_person

    Args:
        person_id (str):
        per_page (int | Unset):
        page (int | Unset):  Default: 1.
        include_admin_details (bool | Unset):  Default: True.
        use_instance_as_main_face (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetFaceRecognitionPersonsByPersonIdVersionsResponseDefaultType0 | GetFaceRecognitionPersonsByPersonIdVersionsResponseDefaultType1 | PersonAssetsVersionsListSchema
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
