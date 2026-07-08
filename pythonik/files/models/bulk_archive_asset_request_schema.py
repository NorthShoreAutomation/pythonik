from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.archive_asset_request import ArchiveAssetRequest


T = TypeVar("T", bound="BulkArchiveAssetRequestSchema")


@_attrs_define
class BulkArchiveAssetRequestSchema:
    """
    Attributes:
        destination_storage_id (None | Unset | UUID): ID of the storage to archive the assets to.
        objects (list[ArchiveAssetRequest] | None | Unset): List of assets to archive. Each asset should contain the
            asset ID.
        parent_job_id (None | Unset | UUID): Parent job ID
    """

    destination_storage_id: None | Unset | UUID = UNSET
    objects: list[ArchiveAssetRequest] | None | Unset = UNSET
    parent_job_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        destination_storage_id: None | str | Unset
        if isinstance(self.destination_storage_id, Unset):
            destination_storage_id = UNSET
        elif isinstance(self.destination_storage_id, UUID):
            destination_storage_id = str(self.destination_storage_id)
        else:
            destination_storage_id = self.destination_storage_id

        objects: list[dict[str, Any]] | None | Unset
        if isinstance(self.objects, Unset):
            objects = UNSET
        elif isinstance(self.objects, list):
            objects = []
            for objects_type_0_item_data in self.objects:
                objects_type_0_item = objects_type_0_item_data.to_dict()
                objects.append(objects_type_0_item)

        else:
            objects = self.objects

        parent_job_id: None | str | Unset
        if isinstance(self.parent_job_id, Unset):
            parent_job_id = UNSET
        elif isinstance(self.parent_job_id, UUID):
            parent_job_id = str(self.parent_job_id)
        else:
            parent_job_id = self.parent_job_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if destination_storage_id is not UNSET:
            field_dict["destination_storage_id"] = destination_storage_id
        if objects is not UNSET:
            field_dict["objects"] = objects
        if parent_job_id is not UNSET:
            field_dict["parent_job_id"] = parent_job_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.archive_asset_request import ArchiveAssetRequest

        d = dict(src_dict)

        def _parse_destination_storage_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                destination_storage_id_type_0 = UUID(data)

                return destination_storage_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        destination_storage_id = _parse_destination_storage_id(
            d.pop("destination_storage_id", UNSET)
        )

        def _parse_objects(data: object) -> list[ArchiveAssetRequest] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                objects_type_0 = []
                _objects_type_0 = data
                for objects_type_0_item_data in _objects_type_0:
                    objects_type_0_item = ArchiveAssetRequest.from_dict(
                        objects_type_0_item_data
                    )

                    objects_type_0.append(objects_type_0_item)

                return objects_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ArchiveAssetRequest] | None | Unset, data)

        objects = _parse_objects(d.pop("objects", UNSET))

        def _parse_parent_job_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parent_job_id_type_0 = UUID(data)

                return parent_job_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        parent_job_id = _parse_parent_job_id(d.pop("parent_job_id", UNSET))

        bulk_archive_asset_request_schema = cls(
            destination_storage_id=destination_storage_id,
            objects=objects,
            parent_job_id=parent_job_id,
        )

        bulk_archive_asset_request_schema.additional_properties = d
        return bulk_archive_asset_request_schema

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
