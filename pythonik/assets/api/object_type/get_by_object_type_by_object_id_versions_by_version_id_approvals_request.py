from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.approval_schema import ApprovalSchema
from ...models.get_by_object_type_by_object_id_versions_by_version_id_approvals_request_response_default_type_0 import (
    GetByObjectTypeByObjectIdVersionsByVersionIdApprovalsRequestResponseDefaultType0,
)
from ...models.get_by_object_type_by_object_id_versions_by_version_id_approvals_request_response_default_type_1 import (
    GetByObjectTypeByObjectIdVersionsByVersionIdApprovalsRequestResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    object_type: str,
    object_id: str,
    version_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/{object_type}/{object_id}/versions/{version_id}/approvals/request/".format(
            object_type=quote(str(object_type), safe=""),
            object_id=quote(str(object_id), safe=""),
            version_id=quote(str(version_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | ApprovalSchema
    | GetByObjectTypeByObjectIdVersionsByVersionIdApprovalsRequestResponseDefaultType0
    | GetByObjectTypeByObjectIdVersionsByVersionIdApprovalsRequestResponseDefaultType1
):
    if response.status_code == 200:
        response_200 = ApprovalSchema.from_dict(response.json())

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
        GetByObjectTypeByObjectIdVersionsByVersionIdApprovalsRequestResponseDefaultType0
        | GetByObjectTypeByObjectIdVersionsByVersionIdApprovalsRequestResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = GetByObjectTypeByObjectIdVersionsByVersionIdApprovalsRequestResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = GetByObjectTypeByObjectIdVersionsByVersionIdApprovalsRequestResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | ApprovalSchema
    | GetByObjectTypeByObjectIdVersionsByVersionIdApprovalsRequestResponseDefaultType0
    | GetByObjectTypeByObjectIdVersionsByVersionIdApprovalsRequestResponseDefaultType1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    object_type: str,
    object_id: str,
    version_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | ApprovalSchema
    | GetByObjectTypeByObjectIdVersionsByVersionIdApprovalsRequestResponseDefaultType0
    | GetByObjectTypeByObjectIdVersionsByVersionIdApprovalsRequestResponseDefaultType1
]:
    """Returns an objects approval request by version


    Required roles:
     - can_read_approval_request

    Args:
        object_type (str):
        object_id (str):
        version_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApprovalSchema | GetByObjectTypeByObjectIdVersionsByVersionIdApprovalsRequestResponseDefaultType0 | GetByObjectTypeByObjectIdVersionsByVersionIdApprovalsRequestResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        object_type=object_type,
        object_id=object_id,
        version_id=version_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    object_type: str,
    object_id: str,
    version_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | ApprovalSchema
    | GetByObjectTypeByObjectIdVersionsByVersionIdApprovalsRequestResponseDefaultType0
    | GetByObjectTypeByObjectIdVersionsByVersionIdApprovalsRequestResponseDefaultType1
    | None
):
    """Returns an objects approval request by version


    Required roles:
     - can_read_approval_request

    Args:
        object_type (str):
        object_id (str):
        version_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApprovalSchema | GetByObjectTypeByObjectIdVersionsByVersionIdApprovalsRequestResponseDefaultType0 | GetByObjectTypeByObjectIdVersionsByVersionIdApprovalsRequestResponseDefaultType1
    """

    return sync_detailed(
        object_type=object_type,
        object_id=object_id,
        version_id=version_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    object_type: str,
    object_id: str,
    version_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | ApprovalSchema
    | GetByObjectTypeByObjectIdVersionsByVersionIdApprovalsRequestResponseDefaultType0
    | GetByObjectTypeByObjectIdVersionsByVersionIdApprovalsRequestResponseDefaultType1
]:
    """Returns an objects approval request by version


    Required roles:
     - can_read_approval_request

    Args:
        object_type (str):
        object_id (str):
        version_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApprovalSchema | GetByObjectTypeByObjectIdVersionsByVersionIdApprovalsRequestResponseDefaultType0 | GetByObjectTypeByObjectIdVersionsByVersionIdApprovalsRequestResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        object_type=object_type,
        object_id=object_id,
        version_id=version_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    object_type: str,
    object_id: str,
    version_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | ApprovalSchema
    | GetByObjectTypeByObjectIdVersionsByVersionIdApprovalsRequestResponseDefaultType0
    | GetByObjectTypeByObjectIdVersionsByVersionIdApprovalsRequestResponseDefaultType1
    | None
):
    """Returns an objects approval request by version


    Required roles:
     - can_read_approval_request

    Args:
        object_type (str):
        object_id (str):
        version_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApprovalSchema | GetByObjectTypeByObjectIdVersionsByVersionIdApprovalsRequestResponseDefaultType0 | GetByObjectTypeByObjectIdVersionsByVersionIdApprovalsRequestResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            object_type=object_type,
            object_id=object_id,
            version_id=version_id,
            client=client,
        )
    ).parsed
