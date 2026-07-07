from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_by_object_type_by_object_id_approvals_user_by_user_id_response_default_type_0 import (
    DeleteByObjectTypeByObjectIdApprovalsUserByUserIdResponseDefaultType0,
)
from ...models.delete_by_object_type_by_object_id_approvals_user_by_user_id_response_default_type_1 import (
    DeleteByObjectTypeByObjectIdApprovalsUserByUserIdResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    object_type: str,
    object_id: str,
    user_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/{object_type}/{object_id}/approvals/user/{user_id}/".format(
            object_type=quote(str(object_type), safe=""),
            object_id=quote(str(object_id), safe=""),
            user_id=quote(str(user_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | DeleteByObjectTypeByObjectIdApprovalsUserByUserIdResponseDefaultType0
    | DeleteByObjectTypeByObjectIdApprovalsUserByUserIdResponseDefaultType1
):
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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
        DeleteByObjectTypeByObjectIdApprovalsUserByUserIdResponseDefaultType0
        | DeleteByObjectTypeByObjectIdApprovalsUserByUserIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = DeleteByObjectTypeByObjectIdApprovalsUserByUserIdResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = DeleteByObjectTypeByObjectIdApprovalsUserByUserIdResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | DeleteByObjectTypeByObjectIdApprovalsUserByUserIdResponseDefaultType0
    | DeleteByObjectTypeByObjectIdApprovalsUserByUserIdResponseDefaultType1
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
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | DeleteByObjectTypeByObjectIdApprovalsUserByUserIdResponseDefaultType0
    | DeleteByObjectTypeByObjectIdApprovalsUserByUserIdResponseDefaultType1
]:
    """Deletes an objects approval status by user_id


    Required roles:
     - can_delete_approval_status

    Args:
        object_type (str):
        object_id (str):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteByObjectTypeByObjectIdApprovalsUserByUserIdResponseDefaultType0 | DeleteByObjectTypeByObjectIdApprovalsUserByUserIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        object_type=object_type,
        object_id=object_id,
        user_id=user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    object_type: str,
    object_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | DeleteByObjectTypeByObjectIdApprovalsUserByUserIdResponseDefaultType0
    | DeleteByObjectTypeByObjectIdApprovalsUserByUserIdResponseDefaultType1
    | None
):
    """Deletes an objects approval status by user_id


    Required roles:
     - can_delete_approval_status

    Args:
        object_type (str):
        object_id (str):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteByObjectTypeByObjectIdApprovalsUserByUserIdResponseDefaultType0 | DeleteByObjectTypeByObjectIdApprovalsUserByUserIdResponseDefaultType1
    """

    return sync_detailed(
        object_type=object_type,
        object_id=object_id,
        user_id=user_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    object_type: str,
    object_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | DeleteByObjectTypeByObjectIdApprovalsUserByUserIdResponseDefaultType0
    | DeleteByObjectTypeByObjectIdApprovalsUserByUserIdResponseDefaultType1
]:
    """Deletes an objects approval status by user_id


    Required roles:
     - can_delete_approval_status

    Args:
        object_type (str):
        object_id (str):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteByObjectTypeByObjectIdApprovalsUserByUserIdResponseDefaultType0 | DeleteByObjectTypeByObjectIdApprovalsUserByUserIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        object_type=object_type,
        object_id=object_id,
        user_id=user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    object_type: str,
    object_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | DeleteByObjectTypeByObjectIdApprovalsUserByUserIdResponseDefaultType0
    | DeleteByObjectTypeByObjectIdApprovalsUserByUserIdResponseDefaultType1
    | None
):
    """Deletes an objects approval status by user_id


    Required roles:
     - can_delete_approval_status

    Args:
        object_type (str):
        object_id (str):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteByObjectTypeByObjectIdApprovalsUserByUserIdResponseDefaultType0 | DeleteByObjectTypeByObjectIdApprovalsUserByUserIdResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            object_type=object_type,
            object_id=object_id,
            user_id=user_id,
            client=client,
        )
    ).parsed
