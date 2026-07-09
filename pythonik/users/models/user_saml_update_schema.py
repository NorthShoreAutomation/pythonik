from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserSamlUpdateSchema")


@_attrs_define
class UserSamlUpdateSchema:
    """
    Attributes:
        email (str):
        first_name (None | str | Unset):
        group_names (list[str] | None | Unset):
        identity_provider_id (None | Unset | UUID):
        last_name (None | str | Unset):
    """

    email: str
    first_name: None | str | Unset = UNSET
    group_names: list[str] | None | Unset = UNSET
    identity_provider_id: None | Unset | UUID = UNSET
    last_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        first_name: None | str | Unset
        if isinstance(self.first_name, Unset):
            first_name = UNSET
        else:
            first_name = self.first_name

        group_names: list[str] | None | Unset
        if isinstance(self.group_names, Unset):
            group_names = UNSET
        elif isinstance(self.group_names, list):
            group_names = self.group_names

        else:
            group_names = self.group_names

        identity_provider_id: None | str | Unset
        if isinstance(self.identity_provider_id, Unset):
            identity_provider_id = UNSET
        elif isinstance(self.identity_provider_id, UUID):
            identity_provider_id = str(self.identity_provider_id)
        else:
            identity_provider_id = self.identity_provider_id

        last_name: None | str | Unset
        if isinstance(self.last_name, Unset):
            last_name = UNSET
        else:
            last_name = self.last_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
            }
        )
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if group_names is not UNSET:
            field_dict["group_names"] = group_names
        if identity_provider_id is not UNSET:
            field_dict["identity_provider_id"] = identity_provider_id
        if last_name is not UNSET:
            field_dict["last_name"] = last_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        def _parse_first_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        first_name = _parse_first_name(d.pop("first_name", UNSET))

        def _parse_group_names(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                group_names_type_0 = cast(list[str], data)

                return group_names_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        group_names = _parse_group_names(d.pop("group_names", UNSET))

        def _parse_identity_provider_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                identity_provider_id_type_0 = UUID(data)

                return identity_provider_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        identity_provider_id = _parse_identity_provider_id(
            d.pop("identity_provider_id", UNSET)
        )

        def _parse_last_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_name = _parse_last_name(d.pop("last_name", UNSET))

        user_saml_update_schema = cls(
            email=email,
            first_name=first_name,
            group_names=group_names,
            identity_provider_id=identity_provider_id,
            last_name=last_name,
        )

        user_saml_update_schema.additional_properties = d
        return user_saml_update_schema

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
