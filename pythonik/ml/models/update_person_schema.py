from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdatePersonSchema")


@_attrs_define
class UpdatePersonSchema:
    """
    Attributes:
        main_face_id (UUID | Unset):
        name (None | str | Unset):
    """

    main_face_id: UUID | Unset = UNSET
    name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        main_face_id: str | Unset = UNSET
        if not isinstance(self.main_face_id, Unset):
            main_face_id = str(self.main_face_id)

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if main_face_id is not UNSET:
            field_dict["main_face_id"] = main_face_id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _main_face_id = d.pop("main_face_id", UNSET)
        main_face_id: UUID | Unset
        if isinstance(_main_face_id, Unset):
            main_face_id = UNSET
        else:
            main_face_id = UUID(_main_face_id)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        update_person_schema = cls(
            main_face_id=main_face_id,
            name=name,
        )

        update_person_schema.additional_properties = d
        return update_person_schema

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
