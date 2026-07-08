from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.transcoder_usages_elastic_schema_transcoder_type import (
    TranscoderUsagesElasticSchemaTranscoderType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.transcoder_usages_elastic_schema_operation_type_type_1 import (
        TranscoderUsagesElasticSchemaOperationTypeType1,
    )


T = TypeVar("T", bound="TranscoderUsagesElasticSchema")


@_attrs_define
class TranscoderUsagesElasticSchema:
    """
    Attributes:
        transcoder_type (TranscoderUsagesElasticSchemaTranscoderType):
        count (int | None | Unset):
        date (None | str | Unset):
        destination_bytes (int | None | Unset):
        duration_seconds (int | None | Unset):
        id (None | Unset | UUID):
        is_user_transcoder (bool | None | Unset):
        operation_type (None | TranscoderUsagesElasticSchemaOperationTypeType1 | Unset):
        source_bytes (int | None | Unset):
        system_domain_id (None | Unset | UUID):
    """

    transcoder_type: TranscoderUsagesElasticSchemaTranscoderType
    count: int | None | Unset = UNSET
    date: None | str | Unset = UNSET
    destination_bytes: int | None | Unset = UNSET
    duration_seconds: int | None | Unset = UNSET
    id: None | Unset | UUID = UNSET
    is_user_transcoder: bool | None | Unset = UNSET
    operation_type: None | TranscoderUsagesElasticSchemaOperationTypeType1 | Unset = (
        UNSET
    )
    source_bytes: int | None | Unset = UNSET
    system_domain_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.transcoder_usages_elastic_schema_operation_type_type_1 import (
            TranscoderUsagesElasticSchemaOperationTypeType1,
        )

        transcoder_type = self.transcoder_type.value

        count: int | None | Unset
        if isinstance(self.count, Unset):
            count = UNSET
        else:
            count = self.count

        date: None | str | Unset
        if isinstance(self.date, Unset):
            date = UNSET
        else:
            date = self.date

        destination_bytes: int | None | Unset
        if isinstance(self.destination_bytes, Unset):
            destination_bytes = UNSET
        else:
            destination_bytes = self.destination_bytes

        duration_seconds: int | None | Unset
        if isinstance(self.duration_seconds, Unset):
            duration_seconds = UNSET
        else:
            duration_seconds = self.duration_seconds

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        is_user_transcoder: bool | None | Unset
        if isinstance(self.is_user_transcoder, Unset):
            is_user_transcoder = UNSET
        else:
            is_user_transcoder = self.is_user_transcoder

        operation_type: dict[str, Any] | None | Unset
        if isinstance(self.operation_type, Unset):
            operation_type = UNSET
        elif isinstance(
            self.operation_type, TranscoderUsagesElasticSchemaOperationTypeType1
        ):
            operation_type = self.operation_type.to_dict()
        else:
            operation_type = self.operation_type

        source_bytes: int | None | Unset
        if isinstance(self.source_bytes, Unset):
            source_bytes = UNSET
        else:
            source_bytes = self.source_bytes

        system_domain_id: None | str | Unset
        if isinstance(self.system_domain_id, Unset):
            system_domain_id = UNSET
        elif isinstance(self.system_domain_id, UUID):
            system_domain_id = str(self.system_domain_id)
        else:
            system_domain_id = self.system_domain_id

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
        from ..models.transcoder_usages_elastic_schema_operation_type_type_1 import (
            TranscoderUsagesElasticSchemaOperationTypeType1,
        )

        d = dict(src_dict)
        transcoder_type = TranscoderUsagesElasticSchemaTranscoderType(
            d.pop("transcoder_type")
        )

        def _parse_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        count = _parse_count(d.pop("count", UNSET))

        def _parse_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date = _parse_date(d.pop("date", UNSET))

        def _parse_destination_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        destination_bytes = _parse_destination_bytes(d.pop("destination_bytes", UNSET))

        def _parse_duration_seconds(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        duration_seconds = _parse_duration_seconds(d.pop("duration_seconds", UNSET))

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

        def _parse_is_user_transcoder(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_user_transcoder = _parse_is_user_transcoder(
            d.pop("is_user_transcoder", UNSET)
        )

        def _parse_operation_type(
            data: object,
        ) -> None | TranscoderUsagesElasticSchemaOperationTypeType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                operation_type_type_1 = (
                    TranscoderUsagesElasticSchemaOperationTypeType1.from_dict(data)
                )

                return operation_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | TranscoderUsagesElasticSchemaOperationTypeType1 | Unset, data
            )

        operation_type = _parse_operation_type(d.pop("operation_type", UNSET))

        def _parse_source_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        source_bytes = _parse_source_bytes(d.pop("source_bytes", UNSET))

        def _parse_system_domain_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                system_domain_id_type_0 = UUID(data)

                return system_domain_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        system_domain_id = _parse_system_domain_id(d.pop("system_domain_id", UNSET))

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
