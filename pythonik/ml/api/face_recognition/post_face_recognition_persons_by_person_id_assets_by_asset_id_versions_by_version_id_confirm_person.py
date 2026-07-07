from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.person_by_asset_and_version_schema import PersonByAssetAndVersionSchema
from ...models.post_face_recognition_persons_by_person_id_assets_by_asset_id_versions_by_version_id_confirm_person_response_default_type_0 import (
    PostFaceRecognitionPersonsByPersonIdAssetsByAssetIdVersionsByVersionIdConfirmPersonResponseDefaultType0,
)
from ...models.post_face_recognition_persons_by_person_id_assets_by_asset_id_versions_by_version_id_confirm_person_response_default_type_1 import (
    PostFaceRecognitionPersonsByPersonIdAssetsByAssetIdVersionsByVersionIdConfirmPersonResponseDefaultType1,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    person_id: str,
    asset_id: str,
    version_id: str,
    *,
    use_instance_as_main_face: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["use_instance_as_main_face"] = use_instance_as_main_face

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/face_recognition/persons/{person_id}/assets/{asset_id}/versions/{version_id}/confirm_person/".format(
            person_id=quote(str(person_id), safe=""),
            asset_id=quote(str(asset_id), safe=""),
            version_id=quote(str(version_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | PersonByAssetAndVersionSchema
    | PostFaceRecognitionPersonsByPersonIdAssetsByAssetIdVersionsByVersionIdConfirmPersonResponseDefaultType0
    | PostFaceRecognitionPersonsByPersonIdAssetsByAssetIdVersionsByVersionIdConfirmPersonResponseDefaultType1
):
    if response.status_code == 200:
        response_200 = PersonByAssetAndVersionSchema.from_dict(response.json())

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
        PostFaceRecognitionPersonsByPersonIdAssetsByAssetIdVersionsByVersionIdConfirmPersonResponseDefaultType0
        | PostFaceRecognitionPersonsByPersonIdAssetsByAssetIdVersionsByVersionIdConfirmPersonResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = PostFaceRecognitionPersonsByPersonIdAssetsByAssetIdVersionsByVersionIdConfirmPersonResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = PostFaceRecognitionPersonsByPersonIdAssetsByAssetIdVersionsByVersionIdConfirmPersonResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PersonByAssetAndVersionSchema
    | PostFaceRecognitionPersonsByPersonIdAssetsByAssetIdVersionsByVersionIdConfirmPersonResponseDefaultType0
    | PostFaceRecognitionPersonsByPersonIdAssetsByAssetIdVersionsByVersionIdConfirmPersonResponseDefaultType1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    person_id: str,
    asset_id: str,
    version_id: str,
    *,
    client: AuthenticatedClient | Client,
    use_instance_as_main_face: bool | Unset = False,
) -> Response[
    Any
    | PersonByAssetAndVersionSchema
    | PostFaceRecognitionPersonsByPersonIdAssetsByAssetIdVersionsByVersionIdConfirmPersonResponseDefaultType0
    | PostFaceRecognitionPersonsByPersonIdAssetsByAssetIdVersionsByVersionIdConfirmPersonResponseDefaultType1
]:
    """Confirm a system unconfirmed person instance


    Required roles:
     - can_delete_person
    - can_edit_person

    Args:
        person_id (str):
        asset_id (str):
        version_id (str):
        use_instance_as_main_face (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PersonByAssetAndVersionSchema | PostFaceRecognitionPersonsByPersonIdAssetsByAssetIdVersionsByVersionIdConfirmPersonResponseDefaultType0 | PostFaceRecognitionPersonsByPersonIdAssetsByAssetIdVersionsByVersionIdConfirmPersonResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        asset_id=asset_id,
        version_id=version_id,
        use_instance_as_main_face=use_instance_as_main_face,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    person_id: str,
    asset_id: str,
    version_id: str,
    *,
    client: AuthenticatedClient | Client,
    use_instance_as_main_face: bool | Unset = False,
) -> (
    Any
    | PersonByAssetAndVersionSchema
    | PostFaceRecognitionPersonsByPersonIdAssetsByAssetIdVersionsByVersionIdConfirmPersonResponseDefaultType0
    | PostFaceRecognitionPersonsByPersonIdAssetsByAssetIdVersionsByVersionIdConfirmPersonResponseDefaultType1
    | None
):
    """Confirm a system unconfirmed person instance


    Required roles:
     - can_delete_person
    - can_edit_person

    Args:
        person_id (str):
        asset_id (str):
        version_id (str):
        use_instance_as_main_face (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PersonByAssetAndVersionSchema | PostFaceRecognitionPersonsByPersonIdAssetsByAssetIdVersionsByVersionIdConfirmPersonResponseDefaultType0 | PostFaceRecognitionPersonsByPersonIdAssetsByAssetIdVersionsByVersionIdConfirmPersonResponseDefaultType1
    """

    return sync_detailed(
        person_id=person_id,
        asset_id=asset_id,
        version_id=version_id,
        client=client,
        use_instance_as_main_face=use_instance_as_main_face,
    ).parsed


async def asyncio_detailed(
    person_id: str,
    asset_id: str,
    version_id: str,
    *,
    client: AuthenticatedClient | Client,
    use_instance_as_main_face: bool | Unset = False,
) -> Response[
    Any
    | PersonByAssetAndVersionSchema
    | PostFaceRecognitionPersonsByPersonIdAssetsByAssetIdVersionsByVersionIdConfirmPersonResponseDefaultType0
    | PostFaceRecognitionPersonsByPersonIdAssetsByAssetIdVersionsByVersionIdConfirmPersonResponseDefaultType1
]:
    """Confirm a system unconfirmed person instance


    Required roles:
     - can_delete_person
    - can_edit_person

    Args:
        person_id (str):
        asset_id (str):
        version_id (str):
        use_instance_as_main_face (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PersonByAssetAndVersionSchema | PostFaceRecognitionPersonsByPersonIdAssetsByAssetIdVersionsByVersionIdConfirmPersonResponseDefaultType0 | PostFaceRecognitionPersonsByPersonIdAssetsByAssetIdVersionsByVersionIdConfirmPersonResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        asset_id=asset_id,
        version_id=version_id,
        use_instance_as_main_face=use_instance_as_main_face,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    person_id: str,
    asset_id: str,
    version_id: str,
    *,
    client: AuthenticatedClient | Client,
    use_instance_as_main_face: bool | Unset = False,
) -> (
    Any
    | PersonByAssetAndVersionSchema
    | PostFaceRecognitionPersonsByPersonIdAssetsByAssetIdVersionsByVersionIdConfirmPersonResponseDefaultType0
    | PostFaceRecognitionPersonsByPersonIdAssetsByAssetIdVersionsByVersionIdConfirmPersonResponseDefaultType1
    | None
):
    """Confirm a system unconfirmed person instance


    Required roles:
     - can_delete_person
    - can_edit_person

    Args:
        person_id (str):
        asset_id (str):
        version_id (str):
        use_instance_as_main_face (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PersonByAssetAndVersionSchema | PostFaceRecognitionPersonsByPersonIdAssetsByAssetIdVersionsByVersionIdConfirmPersonResponseDefaultType0 | PostFaceRecognitionPersonsByPersonIdAssetsByAssetIdVersionsByVersionIdConfirmPersonResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            person_id=person_id,
            asset_id=asset_id,
            version_id=version_id,
            client=client,
            use_instance_as_main_face=use_instance_as_main_face,
        )
    ).parsed
