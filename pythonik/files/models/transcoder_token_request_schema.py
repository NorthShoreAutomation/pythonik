from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.transcoder_token_request_schema_payload_type_0 import (
        TranscoderTokenRequestSchemaPayloadType0,
    )


T = TypeVar("T", bound="TranscoderTokenRequestSchema")


@_attrs_define
class TranscoderTokenRequestSchema:
    """
    Attributes:
        expires_in (float | None | Unset):
        payload (None | TranscoderTokenRequestSchemaPayloadType0 | Unset):
    """

    expires_in: float | None | Unset = UNSET
    payload: None | TranscoderTokenRequestSchemaPayloadType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.transcoder_token_request_schema_payload_type_0 import (
            TranscoderTokenRequestSchemaPayloadType0,
        )

        expires_in: float | None | Unset
        if isinstance(self.expires_in, Unset):
            expires_in = UNSET
        else:
            expires_in = self.expires_in

        payload: dict[str, Any] | None | Unset
        if isinstance(self.payload, Unset):
            payload = UNSET
        elif isinstance(self.payload, TranscoderTokenRequestSchemaPayloadType0):
            payload = self.payload.to_dict()
        else:
            payload = self.payload

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if expires_in is not UNSET:
            field_dict["expires_in"] = expires_in
        if payload is not UNSET:
            field_dict["payload"] = payload

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.transcoder_token_request_schema_payload_type_0 import (
            TranscoderTokenRequestSchemaPayloadType0,
        )

        d = dict(src_dict)

        def _parse_expires_in(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        expires_in = _parse_expires_in(d.pop("expires_in", UNSET))

        def _parse_payload(
            data: object,
        ) -> None | TranscoderTokenRequestSchemaPayloadType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                payload_type_0 = TranscoderTokenRequestSchemaPayloadType0.from_dict(
                    data
                )

                return payload_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TranscoderTokenRequestSchemaPayloadType0 | Unset, data)

        payload = _parse_payload(d.pop("payload", UNSET))

        transcoder_token_request_schema = cls(
            expires_in=expires_in,
            payload=payload,
        )

        transcoder_token_request_schema.additional_properties = d
        return transcoder_token_request_schema

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
