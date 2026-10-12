from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cutting_room_token_response_schema_token_type import (
    CuttingRoomTokenResponseSchemaTokenType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CuttingRoomTokenResponseSchema")


@_attrs_define
class CuttingRoomTokenResponseSchema:
    """
    Attributes:
        access_token (None | str | Unset):
        expires_in (None | str | Unset):
        refresh_expires_in (None | str | Unset):
        refresh_token (None | str | Unset):
        token_type (CuttingRoomTokenResponseSchemaTokenType | None | Unset):
    """

    access_token: None | str | Unset = UNSET
    expires_in: None | str | Unset = UNSET
    refresh_expires_in: None | str | Unset = UNSET
    refresh_token: None | str | Unset = UNSET
    token_type: CuttingRoomTokenResponseSchemaTokenType | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_token: None | str | Unset
        if isinstance(self.access_token, Unset):
            access_token = UNSET
        else:
            access_token = self.access_token

        expires_in: None | str | Unset
        if isinstance(self.expires_in, Unset):
            expires_in = UNSET
        else:
            expires_in = self.expires_in

        refresh_expires_in: None | str | Unset
        if isinstance(self.refresh_expires_in, Unset):
            refresh_expires_in = UNSET
        else:
            refresh_expires_in = self.refresh_expires_in

        refresh_token: None | str | Unset
        if isinstance(self.refresh_token, Unset):
            refresh_token = UNSET
        else:
            refresh_token = self.refresh_token

        token_type: None | str | Unset
        if isinstance(self.token_type, Unset):
            token_type = UNSET
        elif isinstance(self.token_type, CuttingRoomTokenResponseSchemaTokenType):
            token_type = self.token_type.value
        else:
            token_type = self.token_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_token is not UNSET:
            field_dict["access_token"] = access_token
        if expires_in is not UNSET:
            field_dict["expires_in"] = expires_in
        if refresh_expires_in is not UNSET:
            field_dict["refresh_expires_in"] = refresh_expires_in
        if refresh_token is not UNSET:
            field_dict["refresh_token"] = refresh_token
        if token_type is not UNSET:
            field_dict["token_type"] = token_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_access_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        access_token = _parse_access_token(d.pop("access_token", UNSET))

        def _parse_expires_in(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        expires_in = _parse_expires_in(d.pop("expires_in", UNSET))

        def _parse_refresh_expires_in(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        refresh_expires_in = _parse_refresh_expires_in(
            d.pop("refresh_expires_in", UNSET)
        )

        def _parse_refresh_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        refresh_token = _parse_refresh_token(d.pop("refresh_token", UNSET))

        def _parse_token_type(
            data: object,
        ) -> CuttingRoomTokenResponseSchemaTokenType | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                token_type_type_1 = CuttingRoomTokenResponseSchemaTokenType(data)

                return token_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CuttingRoomTokenResponseSchemaTokenType | None | Unset, data)

        token_type = _parse_token_type(d.pop("token_type", UNSET))

        cutting_room_token_response_schema = cls(
            access_token=access_token,
            expires_in=expires_in,
            refresh_expires_in=refresh_expires_in,
            refresh_token=refresh_token,
            token_type=token_type,
        )

        cutting_room_token_response_schema.additional_properties = d
        return cutting_room_token_response_schema

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
