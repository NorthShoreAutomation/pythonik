from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.edge_transcode_worker_schema_status import EdgeTranscodeWorkerSchemaStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="EdgeTranscodeWorkerSchema")


@_attrs_define
class EdgeTranscodeWorkerSchema:
    """
    Attributes:
        status (EdgeTranscodeWorkerSchemaStatus):
        storage_id (UUID):
        id (UUID | Unset):
        last_update_date (datetime.datetime | Unset):
    """

    status: EdgeTranscodeWorkerSchemaStatus
    storage_id: UUID
    id: UUID | Unset = UNSET
    last_update_date: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        storage_id = str(self.storage_id)

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        last_update_date: str | Unset = UNSET
        if not isinstance(self.last_update_date, Unset):
            last_update_date = self.last_update_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "storage_id": storage_id,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if last_update_date is not UNSET:
            field_dict["last_update_date"] = last_update_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = EdgeTranscodeWorkerSchemaStatus(d.pop("status"))

        storage_id = UUID(d.pop("storage_id"))

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        _last_update_date = d.pop("last_update_date", UNSET)
        last_update_date: datetime.datetime | Unset
        if isinstance(_last_update_date, Unset):
            last_update_date = UNSET
        else:
            last_update_date = datetime.datetime.fromisoformat(_last_update_date)

        edge_transcode_worker_schema = cls(
            status=status,
            storage_id=storage_id,
            id=id,
            last_update_date=last_update_date,
        )

        edge_transcode_worker_schema.additional_properties = d
        return edge_transcode_worker_schema

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
