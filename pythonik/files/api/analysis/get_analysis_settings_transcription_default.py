from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.analysis_transcription_settings_schema import (
    AnalysisTranscriptionSettingsSchema,
)
from ...models.get_analysis_settings_transcription_default_response_default_type_0 import (
    GetAnalysisSettingsTranscriptionDefaultResponseDefaultType0,
)
from ...models.get_analysis_settings_transcription_default_response_default_type_1 import (
    GetAnalysisSettingsTranscriptionDefaultResponseDefaultType1,
)
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/analysis/settings/transcription/default/",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AnalysisTranscriptionSettingsSchema
    | Any
    | GetAnalysisSettingsTranscriptionDefaultResponseDefaultType0
    | GetAnalysisSettingsTranscriptionDefaultResponseDefaultType1
):
    if response.status_code == 200:
        response_200 = AnalysisTranscriptionSettingsSchema.from_dict(response.json())

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

    def _parse_response_default(
        data: object,
    ) -> (
        GetAnalysisSettingsTranscriptionDefaultResponseDefaultType0
        | GetAnalysisSettingsTranscriptionDefaultResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetAnalysisSettingsTranscriptionDefaultResponseDefaultType0.from_dict(
                    data
                )
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            GetAnalysisSettingsTranscriptionDefaultResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AnalysisTranscriptionSettingsSchema
    | Any
    | GetAnalysisSettingsTranscriptionDefaultResponseDefaultType0
    | GetAnalysisSettingsTranscriptionDefaultResponseDefaultType1
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
) -> Response[
    AnalysisTranscriptionSettingsSchema
    | Any
    | GetAnalysisSettingsTranscriptionDefaultResponseDefaultType0
    | GetAnalysisSettingsTranscriptionDefaultResponseDefaultType1
]:
    """Get default analysis settings for transcription


    Required roles:
     - can_transcribe_content

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalysisTranscriptionSettingsSchema | Any | GetAnalysisSettingsTranscriptionDefaultResponseDefaultType0 | GetAnalysisSettingsTranscriptionDefaultResponseDefaultType1]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> (
    AnalysisTranscriptionSettingsSchema
    | Any
    | GetAnalysisSettingsTranscriptionDefaultResponseDefaultType0
    | GetAnalysisSettingsTranscriptionDefaultResponseDefaultType1
    | None
):
    """Get default analysis settings for transcription


    Required roles:
     - can_transcribe_content

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalysisTranscriptionSettingsSchema | Any | GetAnalysisSettingsTranscriptionDefaultResponseDefaultType0 | GetAnalysisSettingsTranscriptionDefaultResponseDefaultType1
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    AnalysisTranscriptionSettingsSchema
    | Any
    | GetAnalysisSettingsTranscriptionDefaultResponseDefaultType0
    | GetAnalysisSettingsTranscriptionDefaultResponseDefaultType1
]:
    """Get default analysis settings for transcription


    Required roles:
     - can_transcribe_content

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalysisTranscriptionSettingsSchema | Any | GetAnalysisSettingsTranscriptionDefaultResponseDefaultType0 | GetAnalysisSettingsTranscriptionDefaultResponseDefaultType1]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> (
    AnalysisTranscriptionSettingsSchema
    | Any
    | GetAnalysisSettingsTranscriptionDefaultResponseDefaultType0
    | GetAnalysisSettingsTranscriptionDefaultResponseDefaultType1
    | None
):
    """Get default analysis settings for transcription


    Required roles:
     - can_transcribe_content

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalysisTranscriptionSettingsSchema | Any | GetAnalysisSettingsTranscriptionDefaultResponseDefaultType0 | GetAnalysisSettingsTranscriptionDefaultResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
