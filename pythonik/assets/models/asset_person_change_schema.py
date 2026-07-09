from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AssetPersonChangeSchema")


@_attrs_define
class AssetPersonChangeSchema:
    """
    Attributes:
        asset_id (UUID):
        destination_person_id (UUID):
        has_unconfirmed_persons (bool):
        person_ids_after (list[UUID]):
        source_person_id (UUID):
        version_id (UUID):
        delete_source_person_from_version (bool | None | Unset):
        update_segments (bool | None | Unset):
    """

    asset_id: UUID
    destination_person_id: UUID
    has_unconfirmed_persons: bool
    person_ids_after: list[UUID]
    source_person_id: UUID
    version_id: UUID
    delete_source_person_from_version: bool | None | Unset = UNSET
    update_segments: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_id = str(self.asset_id)

        destination_person_id = str(self.destination_person_id)

        has_unconfirmed_persons = self.has_unconfirmed_persons

        person_ids_after = []
        for person_ids_after_item_data in self.person_ids_after:
            person_ids_after_item = str(person_ids_after_item_data)
            person_ids_after.append(person_ids_after_item)

        source_person_id = str(self.source_person_id)

        version_id = str(self.version_id)

        delete_source_person_from_version: bool | None | Unset
        if isinstance(self.delete_source_person_from_version, Unset):
            delete_source_person_from_version = UNSET
        else:
            delete_source_person_from_version = self.delete_source_person_from_version

        update_segments: bool | None | Unset
        if isinstance(self.update_segments, Unset):
            update_segments = UNSET
        else:
            update_segments = self.update_segments

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "asset_id": asset_id,
                "destination_person_id": destination_person_id,
                "has_unconfirmed_persons": has_unconfirmed_persons,
                "person_ids_after": person_ids_after,
                "source_person_id": source_person_id,
                "version_id": version_id,
            }
        )
        if delete_source_person_from_version is not UNSET:
            field_dict["delete_source_person_from_version"] = (
                delete_source_person_from_version
            )
        if update_segments is not UNSET:
            field_dict["update_segments"] = update_segments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        asset_id = UUID(d.pop("asset_id"))

        destination_person_id = UUID(d.pop("destination_person_id"))

        has_unconfirmed_persons = d.pop("has_unconfirmed_persons")

        person_ids_after = []
        _person_ids_after = d.pop("person_ids_after")
        for person_ids_after_item_data in _person_ids_after:
            person_ids_after_item = UUID(person_ids_after_item_data)

            person_ids_after.append(person_ids_after_item)

        source_person_id = UUID(d.pop("source_person_id"))

        version_id = UUID(d.pop("version_id"))

        def _parse_delete_source_person_from_version(
            data: object,
        ) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        delete_source_person_from_version = _parse_delete_source_person_from_version(
            d.pop("delete_source_person_from_version", UNSET)
        )

        def _parse_update_segments(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        update_segments = _parse_update_segments(d.pop("update_segments", UNSET))

        asset_person_change_schema = cls(
            asset_id=asset_id,
            destination_person_id=destination_person_id,
            has_unconfirmed_persons=has_unconfirmed_persons,
            person_ids_after=person_ids_after,
            source_person_id=source_person_id,
            version_id=version_id,
            delete_source_person_from_version=delete_source_person_from_version,
            update_segments=update_segments,
        )

        asset_person_change_schema.additional_properties = d
        return asset_person_change_schema

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
