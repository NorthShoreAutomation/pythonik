from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.transcoder_token_request_schema_payload import (
        TranscoderTokenRequestSchemaPayload,
    )


T = TypeVar("T", bound="TranscoderTokenRequestSchema")


@_attrs_define
class TranscoderTokenRequestSchema:
    """
    Attributes:
        expires_in (float | Unset):
        payload (TranscoderTokenRequestSchemaPayload | Unset):
    """

    expires_in: float | Unset = UNSET
    payload: TranscoderTokenRequestSchemaPayload | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expires_in = self.expires_in

        payload: dict[str, Any] | Unset = UNSET
        if not isinstance(self.payload, Unset):
            payload = self.payload.to_dict()

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
        from ..models.transcoder_token_request_schema_payload import (
            TranscoderTokenRequestSchemaPayload,
        )

        d = dict(src_dict)
        expires_in = d.pop("expires_in", UNSET)

        _payload = d.pop("payload", UNSET)
        payload: TranscoderTokenRequestSchemaPayload | Unset
        if isinstance(_payload, Unset):
            payload = UNSET
        else:
            payload = TranscoderTokenRequestSchemaPayload.from_dict(_payload)

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
