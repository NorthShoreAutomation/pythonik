from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.transcoder_usages_elastic_schema_operation_type import (
    TranscoderUsagesElasticSchemaOperationType,
)
from ..models.transcoder_usages_elastic_schema_transcoder_type import (
    TranscoderUsagesElasticSchemaTranscoderType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="TranscoderUsagesElasticSchema")


@_attrs_define
class TranscoderUsagesElasticSchema:
    """
    Attributes:
        transcoder_type (TranscoderUsagesElasticSchemaTranscoderType):
        count (int | Unset):
        date (str | Unset):
        destination_bytes (int | Unset):
        duration_seconds (int | Unset):
        id (UUID | Unset):
        is_user_transcoder (bool | Unset):
        operation_type (TranscoderUsagesElasticSchemaOperationType | Unset):
        source_bytes (int | Unset):
        system_domain_id (UUID | Unset):
    """

    transcoder_type: TranscoderUsagesElasticSchemaTranscoderType
    count: int | Unset = UNSET
    date: str | Unset = UNSET
    destination_bytes: int | Unset = UNSET
    duration_seconds: int | Unset = UNSET
    id: UUID | Unset = UNSET
    is_user_transcoder: bool | Unset = UNSET
    operation_type: TranscoderUsagesElasticSchemaOperationType | Unset = UNSET
    source_bytes: int | Unset = UNSET
    system_domain_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        transcoder_type = self.transcoder_type.value

        count = self.count

        date = self.date

        destination_bytes = self.destination_bytes

        duration_seconds = self.duration_seconds

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        is_user_transcoder = self.is_user_transcoder

        operation_type: str | Unset = UNSET
        if not isinstance(self.operation_type, Unset):
            operation_type = self.operation_type.value

        source_bytes = self.source_bytes

        system_domain_id: str | Unset = UNSET
        if not isinstance(self.system_domain_id, Unset):
            system_domain_id = str(self.system_domain_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "transcoder_type": transcoder_type,
            }
        )
        if count is not UNSET:
            field_dict["count"] = count
        if date is not UNSET:
            field_dict["date"] = date
        if destination_bytes is not UNSET:
            field_dict["destination_bytes"] = destination_bytes
        if duration_seconds is not UNSET:
            field_dict["duration_seconds"] = duration_seconds
        if id is not UNSET:
            field_dict["id"] = id
        if is_user_transcoder is not UNSET:
            field_dict["is_user_transcoder"] = is_user_transcoder
        if operation_type is not UNSET:
            field_dict["operation_type"] = operation_type
        if source_bytes is not UNSET:
            field_dict["source_bytes"] = source_bytes
        if system_domain_id is not UNSET:
            field_dict["system_domain_id"] = system_domain_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        transcoder_type = TranscoderUsagesElasticSchemaTranscoderType(
            d.pop("transcoder_type")
        )

        count = d.pop("count", UNSET)

        date = d.pop("date", UNSET)

        destination_bytes = d.pop("destination_bytes", UNSET)

        duration_seconds = d.pop("duration_seconds", UNSET)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        is_user_transcoder = d.pop("is_user_transcoder", UNSET)

        _operation_type = d.pop("operation_type", UNSET)
        operation_type: TranscoderUsagesElasticSchemaOperationType | Unset
        if isinstance(_operation_type, Unset):
            operation_type = UNSET
        else:
            operation_type = TranscoderUsagesElasticSchemaOperationType(_operation_type)

        source_bytes = d.pop("source_bytes", UNSET)

        _system_domain_id = d.pop("system_domain_id", UNSET)
        system_domain_id: UUID | Unset
        if isinstance(_system_domain_id, Unset):
            system_domain_id = UNSET
        else:
            system_domain_id = UUID(_system_domain_id)

        transcoder_usages_elastic_schema = cls(
            transcoder_type=transcoder_type,
            count=count,
            date=date,
            destination_bytes=destination_bytes,
            duration_seconds=duration_seconds,
            id=id,
            is_user_transcoder=is_user_transcoder,
            operation_type=operation_type,
            source_bytes=source_bytes,
            system_domain_id=system_domain_id,
        )

        transcoder_usages_elastic_schema.additional_properties = d
        return transcoder_usages_elastic_schema

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
