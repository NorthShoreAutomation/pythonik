from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.edge_transcode_worker_schema import EdgeTranscodeWorkerSchema


T = TypeVar("T", bound="EdgeTranscodeWorkersSchema")


@_attrs_define
class EdgeTranscodeWorkersSchema:
    """
    Attributes:
        objects (list[EdgeTranscodeWorkerSchema] | Unset):
    """

    objects: list[EdgeTranscodeWorkerSchema] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objects: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.objects, Unset):
            objects = []
            for objects_item_data in self.objects:
                objects_item = objects_item_data.to_dict()
                objects.append(objects_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objects is not UNSET:
            field_dict["objects"] = objects

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.edge_transcode_worker_schema import EdgeTranscodeWorkerSchema

        d = dict(src_dict)
        _objects = d.pop("objects", UNSET)
        objects: list[EdgeTranscodeWorkerSchema] | Unset = UNSET
        if _objects is not UNSET:
            objects = []
            for objects_item_data in _objects:
                objects_item = EdgeTranscodeWorkerSchema.from_dict(objects_item_data)

                objects.append(objects_item)

        edge_transcode_workers_schema = cls(
            objects=objects,
        )

        edge_transcode_workers_schema.additional_properties = d
        return edge_transcode_workers_schema

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
