from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateConfirmPersonSchema")


@_attrs_define
class UpdateConfirmPersonSchema:
    """
    Attributes:
        name (str):
        all_instances_except_unconfirmed (bool | None | Unset):  Default: False.
        version_ids (list[UUID] | None | Unset):
    """

    name: str
    all_instances_except_unconfirmed: bool | None | Unset = False
    version_ids: list[UUID] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        all_instances_except_unconfirmed: bool | None | Unset
        if isinstance(self.all_instances_except_unconfirmed, Unset):
            all_instances_except_unconfirmed = UNSET
        else:
            all_instances_except_unconfirmed = self.all_instances_except_unconfirmed

        version_ids: list[str] | None | Unset
        if isinstance(self.version_ids, Unset):
            version_ids = UNSET
        elif isinstance(self.version_ids, list):
            version_ids = []
            for version_ids_type_0_item_data in self.version_ids:
                version_ids_type_0_item = str(version_ids_type_0_item_data)
                version_ids.append(version_ids_type_0_item)

        else:
            version_ids = self.version_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if all_instances_except_unconfirmed is not UNSET:
            field_dict["all_instances_except_unconfirmed"] = (
                all_instances_except_unconfirmed
            )
        if version_ids is not UNSET:
            field_dict["version_ids"] = version_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_all_instances_except_unconfirmed(
            data: object,
        ) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        all_instances_except_unconfirmed = _parse_all_instances_except_unconfirmed(
            d.pop("all_instances_except_unconfirmed", UNSET)
        )

        def _parse_version_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                version_ids_type_0 = []
                _version_ids_type_0 = data
                for version_ids_type_0_item_data in _version_ids_type_0:
                    version_ids_type_0_item = UUID(version_ids_type_0_item_data)

                    version_ids_type_0.append(version_ids_type_0_item)

                return version_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        version_ids = _parse_version_ids(d.pop("version_ids", UNSET))

        update_confirm_person_schema = cls(
            name=name,
            all_instances_except_unconfirmed=all_instances_except_unconfirmed,
            version_ids=version_ids,
        )

        update_confirm_person_schema.additional_properties = d
        return update_confirm_person_schema

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
