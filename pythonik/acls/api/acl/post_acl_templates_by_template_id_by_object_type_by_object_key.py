from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_acl_templates_by_template_id_by_object_type_by_object_key_response_default_type_0 import (
    PostAclTemplatesByTemplateIdByObjectTypeByObjectKeyResponseDefaultType0,
)
from ...models.post_acl_templates_by_template_id_by_object_type_by_object_key_response_default_type_1 import (
    PostAclTemplatesByTemplateIdByObjectTypeByObjectKeyResponseDefaultType1,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    template_id: str,
    object_type: str,
    object_key: str,
    *,
    ignore_reindexing: bool | Unset = UNSET,
    restrict_acls_collection_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["ignore_reindexing"] = ignore_reindexing

    params["restrict_acls_collection_id"] = restrict_acls_collection_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/acl/templates/{template_id}/{object_type}/{object_key}/".format(
            template_id=quote(str(template_id), safe=""),
            object_type=quote(str(object_type), safe=""),
            object_key=quote(str(object_key), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | PostAclTemplatesByTemplateIdByObjectTypeByObjectKeyResponseDefaultType0
    | PostAclTemplatesByTemplateIdByObjectTypeByObjectKeyResponseDefaultType1
):
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    def _parse_response_default(
        data: object,
    ) -> (
        PostAclTemplatesByTemplateIdByObjectTypeByObjectKeyResponseDefaultType0
        | PostAclTemplatesByTemplateIdByObjectTypeByObjectKeyResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = PostAclTemplatesByTemplateIdByObjectTypeByObjectKeyResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = PostAclTemplatesByTemplateIdByObjectTypeByObjectKeyResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostAclTemplatesByTemplateIdByObjectTypeByObjectKeyResponseDefaultType0
    | PostAclTemplatesByTemplateIdByObjectTypeByObjectKeyResponseDefaultType1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    template_id: str,
    object_type: str,
    object_key: str,
    *,
    client: AuthenticatedClient | Client,
    ignore_reindexing: bool | Unset = UNSET,
    restrict_acls_collection_id: str | Unset = UNSET,
) -> Response[
    Any
    | PostAclTemplatesByTemplateIdByObjectTypeByObjectKeyResponseDefaultType0
    | PostAclTemplatesByTemplateIdByObjectTypeByObjectKeyResponseDefaultType1
]:
    """Apply template permissions to an object

    Args:
        template_id (str):
        object_type (str):
        object_key (str):
        ignore_reindexing (bool | Unset):
        restrict_acls_collection_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostAclTemplatesByTemplateIdByObjectTypeByObjectKeyResponseDefaultType0 | PostAclTemplatesByTemplateIdByObjectTypeByObjectKeyResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        template_id=template_id,
        object_type=object_type,
        object_key=object_key,
        ignore_reindexing=ignore_reindexing,
        restrict_acls_collection_id=restrict_acls_collection_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    template_id: str,
    object_type: str,
    object_key: str,
    *,
    client: AuthenticatedClient | Client,
    ignore_reindexing: bool | Unset = UNSET,
    restrict_acls_collection_id: str | Unset = UNSET,
) -> (
    Any
    | PostAclTemplatesByTemplateIdByObjectTypeByObjectKeyResponseDefaultType0
    | PostAclTemplatesByTemplateIdByObjectTypeByObjectKeyResponseDefaultType1
    | None
):
    """Apply template permissions to an object

    Args:
        template_id (str):
        object_type (str):
        object_key (str):
        ignore_reindexing (bool | Unset):
        restrict_acls_collection_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostAclTemplatesByTemplateIdByObjectTypeByObjectKeyResponseDefaultType0 | PostAclTemplatesByTemplateIdByObjectTypeByObjectKeyResponseDefaultType1
    """

    return sync_detailed(
        template_id=template_id,
        object_type=object_type,
        object_key=object_key,
        client=client,
        ignore_reindexing=ignore_reindexing,
        restrict_acls_collection_id=restrict_acls_collection_id,
    ).parsed


async def asyncio_detailed(
    template_id: str,
    object_type: str,
    object_key: str,
    *,
    client: AuthenticatedClient | Client,
    ignore_reindexing: bool | Unset = UNSET,
    restrict_acls_collection_id: str | Unset = UNSET,
) -> Response[
    Any
    | PostAclTemplatesByTemplateIdByObjectTypeByObjectKeyResponseDefaultType0
    | PostAclTemplatesByTemplateIdByObjectTypeByObjectKeyResponseDefaultType1
]:
    """Apply template permissions to an object

    Args:
        template_id (str):
        object_type (str):
        object_key (str):
        ignore_reindexing (bool | Unset):
        restrict_acls_collection_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostAclTemplatesByTemplateIdByObjectTypeByObjectKeyResponseDefaultType0 | PostAclTemplatesByTemplateIdByObjectTypeByObjectKeyResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        template_id=template_id,
        object_type=object_type,
        object_key=object_key,
        ignore_reindexing=ignore_reindexing,
        restrict_acls_collection_id=restrict_acls_collection_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    template_id: str,
    object_type: str,
    object_key: str,
    *,
    client: AuthenticatedClient | Client,
    ignore_reindexing: bool | Unset = UNSET,
    restrict_acls_collection_id: str | Unset = UNSET,
) -> (
    Any
    | PostAclTemplatesByTemplateIdByObjectTypeByObjectKeyResponseDefaultType0
    | PostAclTemplatesByTemplateIdByObjectTypeByObjectKeyResponseDefaultType1
    | None
):
    """Apply template permissions to an object

    Args:
        template_id (str):
        object_type (str):
        object_key (str):
        ignore_reindexing (bool | Unset):
        restrict_acls_collection_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostAclTemplatesByTemplateIdByObjectTypeByObjectKeyResponseDefaultType0 | PostAclTemplatesByTemplateIdByObjectTypeByObjectKeyResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            template_id=template_id,
            object_type=object_type,
            object_key=object_key,
            client=client,
            ignore_reindexing=ignore_reindexing,
            restrict_acls_collection_id=restrict_acls_collection_id,
        )
    ).parsed
