from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.complete_invitation_schema import CompleteInvitationSchema
from ...models.invitation_response_schema import InvitationResponseSchema
from ...models.put_invitation_complete_by_reset_hash_response_default_type_0 import (
    PutInvitationCompleteByResetHashResponseDefaultType0,
)
from ...models.put_invitation_complete_by_reset_hash_response_default_type_1 import (
    PutInvitationCompleteByResetHashResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    reset_hash: str,
    *,
    body: CompleteInvitationSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/invitation/complete/{reset_hash}/".format(
            reset_hash=quote(str(reset_hash), safe=""),
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
    | InvitationResponseSchema
    | PutInvitationCompleteByResetHashResponseDefaultType0
    | PutInvitationCompleteByResetHashResponseDefaultType1
):
    if response.status_code == 200:
        response_200 = InvitationResponseSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 419:
        response_419 = cast(Any, None)
        return response_419

    def _parse_response_default(
        data: object,
    ) -> (
        PutInvitationCompleteByResetHashResponseDefaultType0
        | PutInvitationCompleteByResetHashResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                PutInvitationCompleteByResetHashResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PutInvitationCompleteByResetHashResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | InvitationResponseSchema
    | PutInvitationCompleteByResetHashResponseDefaultType0
    | PutInvitationCompleteByResetHashResponseDefaultType1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    reset_hash: str,
    *,
    client: AuthenticatedClient | Client,
    body: CompleteInvitationSchema,
) -> Response[
    Any
    | InvitationResponseSchema
    | PutInvitationCompleteByResetHashResponseDefaultType0
    | PutInvitationCompleteByResetHashResponseDefaultType1
]:
    """Completes invitation by setting password and other user details

    Args:
        reset_hash (str):
        body (CompleteInvitationSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | InvitationResponseSchema | PutInvitationCompleteByResetHashResponseDefaultType0 | PutInvitationCompleteByResetHashResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        reset_hash=reset_hash,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    reset_hash: str,
    *,
    client: AuthenticatedClient | Client,
    body: CompleteInvitationSchema,
) -> (
    Any
    | InvitationResponseSchema
    | PutInvitationCompleteByResetHashResponseDefaultType0
    | PutInvitationCompleteByResetHashResponseDefaultType1
    | None
):
    """Completes invitation by setting password and other user details

    Args:
        reset_hash (str):
        body (CompleteInvitationSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | InvitationResponseSchema | PutInvitationCompleteByResetHashResponseDefaultType0 | PutInvitationCompleteByResetHashResponseDefaultType1
    """

    return sync_detailed(
        reset_hash=reset_hash,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    reset_hash: str,
    *,
    client: AuthenticatedClient | Client,
    body: CompleteInvitationSchema,
) -> Response[
    Any
    | InvitationResponseSchema
    | PutInvitationCompleteByResetHashResponseDefaultType0
    | PutInvitationCompleteByResetHashResponseDefaultType1
]:
    """Completes invitation by setting password and other user details

    Args:
        reset_hash (str):
        body (CompleteInvitationSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | InvitationResponseSchema | PutInvitationCompleteByResetHashResponseDefaultType0 | PutInvitationCompleteByResetHashResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        reset_hash=reset_hash,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    reset_hash: str,
    *,
    client: AuthenticatedClient | Client,
    body: CompleteInvitationSchema,
) -> (
    Any
    | InvitationResponseSchema
    | PutInvitationCompleteByResetHashResponseDefaultType0
    | PutInvitationCompleteByResetHashResponseDefaultType1
    | None
):
    """Completes invitation by setting password and other user details

    Args:
        reset_hash (str):
        body (CompleteInvitationSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | InvitationResponseSchema | PutInvitationCompleteByResetHashResponseDefaultType0 | PutInvitationCompleteByResetHashResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            reset_hash=reset_hash,
            client=client,
            body=body,
        )
    ).parsed
