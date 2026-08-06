from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.person_by_asset_and_version import PersonByAssetAndVersion


T = TypeVar("T", bound="BulkPersonByAssetAndVersion")


@_attrs_define
class BulkPersonByAssetAndVersion:
    """
    Attributes:
        version_id (UUID):
        persons (list[PersonByAssetAndVersion] | None | Unset):
    """

    version_id: UUID
    persons: list[PersonByAssetAndVersion] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        version_id = str(self.version_id)

        persons: list[dict[str, Any]] | None | Unset
        if isinstance(self.persons, Unset):
            persons = UNSET
        elif isinstance(self.persons, list):
            persons = []
            for persons_type_0_item_data in self.persons:
                persons_type_0_item = persons_type_0_item_data.to_dict()
                persons.append(persons_type_0_item)

        else:
            persons = self.persons

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "version_id": version_id,
            }
        )
        if persons is not UNSET:
            field_dict["persons"] = persons

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.person_by_asset_and_version import PersonByAssetAndVersion

        d = dict(src_dict)
        version_id = UUID(d.pop("version_id"))

        def _parse_persons(
            data: object,
        ) -> list[PersonByAssetAndVersion] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                persons_type_0 = []
                _persons_type_0 = data
                for persons_type_0_item_data in _persons_type_0:
                    persons_type_0_item = PersonByAssetAndVersion.from_dict(
                        persons_type_0_item_data
                    )

                    persons_type_0.append(persons_type_0_item)

                return persons_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PersonByAssetAndVersion] | None | Unset, data)

        persons = _parse_persons(d.pop("persons", UNSET))

        bulk_person_by_asset_and_version = cls(
            version_id=version_id,
            persons=persons,
        )

        bulk_person_by_asset_and_version.additional_properties = d
        return bulk_person_by_asset_and_version

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
