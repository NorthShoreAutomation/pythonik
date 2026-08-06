from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DeletePersonByVersionSchema")


@_attrs_define
class DeletePersonByVersionSchema:
    """
    Attributes:
        person_id (UUID):
        version_id (UUID):
    """

    person_id: UUID
    version_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        person_id = str(self.person_id)

        version_id = str(self.version_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "person_id": person_id,
                "version_id": version_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        person_id = UUID(d.pop("person_id"))

        version_id = UUID(d.pop("version_id"))

        delete_person_by_version_schema = cls(
            person_id=person_id,
            version_id=version_id,
        )

        delete_person_by_version_schema.additional_properties = d
        return delete_person_by_version_schema

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
