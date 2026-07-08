from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
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
        id (None | Unset | UUID):
        last_update_date (datetime.datetime | None | Unset):
    """

    status: EdgeTranscodeWorkerSchemaStatus
    storage_id: UUID
    id: None | Unset | UUID = UNSET
    last_update_date: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        storage_id = str(self.storage_id)

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        last_update_date: None | str | Unset
        if isinstance(self.last_update_date, Unset):
            last_update_date = UNSET
        elif isinstance(self.last_update_date, datetime.datetime):
            last_update_date = self.last_update_date.isoformat()
        else:
            last_update_date = self.last_update_date

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

        def _parse_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                id_type_0 = UUID(data)

                return id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_last_update_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_update_date_type_0 = datetime.datetime.fromisoformat(data)

                return last_update_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_update_date = _parse_last_update_date(d.pop("last_update_date", UNSET))

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
