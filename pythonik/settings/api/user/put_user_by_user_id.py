from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.put_user_by_user_id_response_default_type_0 import (
    PutUserByUserIdResponseDefaultType0,
)
from ...models.put_user_by_user_id_response_default_type_1 import (
    PutUserByUserIdResponseDefaultType1,
)
from ...models.user_setting_schema import UserSettingSchema
from ...types import Response


def _get_kwargs(
    user_id: str,
    *,
    body: UserSettingSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/user/{user_id}/".format(
            user_id=quote(str(user_id), safe=""),
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
    | PutUserByUserIdResponseDefaultType0
    | PutUserByUserIdResponseDefaultType1
    | UserSettingSchema
):
    if response.status_code == 200:
        response_200 = UserSettingSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    def _parse_response_default(
        data: object,
    ) -> PutUserByUserIdResponseDefaultType0 | PutUserByUserIdResponseDefaultType1:
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = PutUserByUserIdResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = PutUserByUserIdResponseDefaultType1.from_dict(data)

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PutUserByUserIdResponseDefaultType0
    | PutUserByUserIdResponseDefaultType1
    | UserSettingSchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UserSettingSchema,
) -> Response[
    Any
    | PutUserByUserIdResponseDefaultType0
    | PutUserByUserIdResponseDefaultType1
    | UserSettingSchema
]:
    """Change user settings

    Args:
        user_id (str):
        body (UserSettingSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutUserByUserIdResponseDefaultType0 | PutUserByUserIdResponseDefaultType1 | UserSettingSchema]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UserSettingSchema,
) -> (
    Any
    | PutUserByUserIdResponseDefaultType0
    | PutUserByUserIdResponseDefaultType1
    | UserSettingSchema
    | None
):
    """Change user settings

    Args:
        user_id (str):
        body (UserSettingSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutUserByUserIdResponseDefaultType0 | PutUserByUserIdResponseDefaultType1 | UserSettingSchema
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UserSettingSchema,
) -> Response[
    Any
    | PutUserByUserIdResponseDefaultType0
    | PutUserByUserIdResponseDefaultType1
    | UserSettingSchema
]:
    """Change user settings

    Args:
        user_id (str):
        body (UserSettingSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutUserByUserIdResponseDefaultType0 | PutUserByUserIdResponseDefaultType1 | UserSettingSchema]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UserSettingSchema,
) -> (
    Any
    | PutUserByUserIdResponseDefaultType0
    | PutUserByUserIdResponseDefaultType1
    | UserSettingSchema
    | None
):
    """Change user settings

    Args:
        user_id (str):
        body (UserSettingSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutUserByUserIdResponseDefaultType0 | PutUserByUserIdResponseDefaultType1 | UserSettingSchema
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            body=body,
        )
    ).parsed
