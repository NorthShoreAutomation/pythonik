from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asset_version_lookup_schema import AssetVersionLookupSchema


T = TypeVar("T", bound="ScheduleSyncPersonToVersionsSchema")


@_attrs_define
class ScheduleSyncPersonToVersionsSchema:
    """
    Attributes:
        objects (list[AssetVersionLookupSchema]):
        sync_id (UUID):
        finished (bool | None | Unset):  Default: False.
        has_unconfirmed_instances (bool | None | Unset):  Default: False.
        job_id (None | Unset | UUID):
        person_id (None | Unset | UUID):
    """

    objects: list[AssetVersionLookupSchema]
    sync_id: UUID
    finished: bool | None | Unset = False
    has_unconfirmed_instances: bool | None | Unset = False
    job_id: None | Unset | UUID = UNSET
    person_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objects = []
        for objects_item_data in self.objects:
            objects_item = objects_item_data.to_dict()
            objects.append(objects_item)

        sync_id = str(self.sync_id)

        finished: bool | None | Unset
        if isinstance(self.finished, Unset):
            finished = UNSET
        else:
            finished = self.finished

        has_unconfirmed_instances: bool | None | Unset
        if isinstance(self.has_unconfirmed_instances, Unset):
            has_unconfirmed_instances = UNSET
        else:
            has_unconfirmed_instances = self.has_unconfirmed_instances

        job_id: None | str | Unset
        if isinstance(self.job_id, Unset):
            job_id = UNSET
        elif isinstance(self.job_id, UUID):
            job_id = str(self.job_id)
        else:
            job_id = self.job_id

        person_id: None | str | Unset
        if isinstance(self.person_id, Unset):
            person_id = UNSET
        elif isinstance(self.person_id, UUID):
            person_id = str(self.person_id)
        else:
            person_id = self.person_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "objects": objects,
                "sync_id": sync_id,
            }
        )
        if finished is not UNSET:
            field_dict["finished"] = finished
        if has_unconfirmed_instances is not UNSET:
            field_dict["has_unconfirmed_instances"] = has_unconfirmed_instances
        if job_id is not UNSET:
            field_dict["job_id"] = job_id
        if person_id is not UNSET:
            field_dict["person_id"] = person_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.asset_version_lookup_schema import AssetVersionLookupSchema

        d = dict(src_dict)
        objects = []
        _objects = d.pop("objects")
        for objects_item_data in _objects:
            objects_item = AssetVersionLookupSchema.from_dict(objects_item_data)

            objects.append(objects_item)

        sync_id = UUID(d.pop("sync_id"))

        def _parse_finished(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        finished = _parse_finished(d.pop("finished", UNSET))

        def _parse_has_unconfirmed_instances(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        has_unconfirmed_instances = _parse_has_unconfirmed_instances(
            d.pop("has_unconfirmed_instances", UNSET)
        )

        def _parse_job_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                job_id_type_0 = UUID(data)

                return job_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        job_id = _parse_job_id(d.pop("job_id", UNSET))

        def _parse_person_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                person_id_type_0 = UUID(data)

                return person_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        person_id = _parse_person_id(d.pop("person_id", UNSET))

        schedule_sync_person_to_versions_schema = cls(
            objects=objects,
            sync_id=sync_id,
            finished=finished,
            has_unconfirmed_instances=has_unconfirmed_instances,
            job_id=job_id,
            person_id=person_id,
        )

        schedule_sync_person_to_versions_schema.additional_properties = d
        return schedule_sync_person_to_versions_schema

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
