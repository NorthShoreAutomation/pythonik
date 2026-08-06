from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.asset_person_change_schema import AssetPersonChangeSchema


T = TypeVar("T", bound="BulkAssetPersonChangeSchema")


@_attrs_define
class BulkAssetPersonChangeSchema:
    """
    Attributes:
        job_id (UUID):
        objects (list[AssetPersonChangeSchema]):
    """

    job_id: UUID
    objects: list[AssetPersonChangeSchema]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job_id = str(self.job_id)

        objects = []
        for objects_item_data in self.objects:
            objects_item = objects_item_data.to_dict()
            objects.append(objects_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "job_id": job_id,
                "objects": objects,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.asset_person_change_schema import AssetPersonChangeSchema

        d = dict(src_dict)
        job_id = UUID(d.pop("job_id"))

        objects = []
        _objects = d.pop("objects")
        for objects_item_data in _objects:
            objects_item = AssetPersonChangeSchema.from_dict(objects_item_data)

            objects.append(objects_item)

        bulk_asset_person_change_schema = cls(
            job_id=job_id,
            objects=objects,
        )

        bulk_asset_person_change_schema.additional_properties = d
        return bulk_asset_person_change_schema

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
