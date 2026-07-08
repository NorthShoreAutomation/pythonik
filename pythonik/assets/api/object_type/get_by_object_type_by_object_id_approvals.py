from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.approvals_by_schema import ApprovalsBySchema
from ...models.get_by_object_type_by_object_id_approvals_response_default import (
    GetByObjectTypeByObjectIdApprovalsResponseDefault,
)
from ...types import Response


def _get_kwargs(
    object_type: str,
    object_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/{object_type}/{object_id}/approvals/".format(
            object_type=quote(str(object_type), safe=""),
            object_id=quote(str(object_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ApprovalsBySchema | GetByObjectTypeByObjectIdApprovalsResponseDefault:
    if response.status_code == 200:
        response_200 = ApprovalsBySchema.from_dict(response.json())

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

    response_default = GetByObjectTypeByObjectIdApprovalsResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | ApprovalsBySchema | GetByObjectTypeByObjectIdApprovalsResponseDefault
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
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any | ApprovalsBySchema | GetByObjectTypeByObjectIdApprovalsResponseDefault
]:
    """Returns an objects approval request


    Required roles:
     - can_read_approval_request

    Args:
        object_type (str):
        object_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApprovalsBySchema | GetByObjectTypeByObjectIdApprovalsResponseDefault]
    """

    kwargs = _get_kwargs(
        object_type=object_type,
        object_id=object_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    object_type: str,
    object_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | ApprovalsBySchema | GetByObjectTypeByObjectIdApprovalsResponseDefault | None:
    """Returns an objects approval request


    Required roles:
     - can_read_approval_request

    Args:
        object_type (str):
        object_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApprovalsBySchema | GetByObjectTypeByObjectIdApprovalsResponseDefault
    """

    return sync_detailed(
        object_type=object_type,
        object_id=object_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    object_type: str,
    object_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any | ApprovalsBySchema | GetByObjectTypeByObjectIdApprovalsResponseDefault
]:
    """Returns an objects approval request


    Required roles:
     - can_read_approval_request

    Args:
        object_type (str):
        object_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApprovalsBySchema | GetByObjectTypeByObjectIdApprovalsResponseDefault]
    """

    kwargs = _get_kwargs(
        object_type=object_type,
        object_id=object_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    object_type: str,
    object_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | ApprovalsBySchema | GetByObjectTypeByObjectIdApprovalsResponseDefault | None:
    """Returns an objects approval request


    Required roles:
     - can_read_approval_request

    Args:
        object_type (str):
        object_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApprovalsBySchema | GetByObjectTypeByObjectIdApprovalsResponseDefault
    """

    return (
        await asyncio_detailed(
            object_type=object_type,
            object_id=object_id,
            client=client,
        )
    ).parsed
