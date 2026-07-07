from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.trigger_schema_event_type import TriggerSchemaEventType
from ..models.trigger_schema_operations_item import TriggerSchemaOperationsItem
from ..models.trigger_schema_realm import TriggerSchemaRealm
from ..models.trigger_schema_type import TriggerSchemaType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.condition_schema import ConditionSchema


T = TypeVar("T", bound="TriggerSchema")


@_attrs_define
class TriggerSchema:
    """
    Attributes:
        event_type (TriggerSchemaEventType):
        type_ (TriggerSchemaType):
        date_created (datetime.datetime | Unset):
        date_modified (datetime.datetime | Unset):
        execute_at (datetime.datetime | Unset):
        filters (list[ConditionSchema] | Unset):
        object_id (None | Unset | UUID):
        operations (list[TriggerSchemaOperationsItem] | Unset):
        realm (TriggerSchemaRealm | Unset):
    """

    event_type: TriggerSchemaEventType
    type_: TriggerSchemaType
    date_created: datetime.datetime | Unset = UNSET
    date_modified: datetime.datetime | Unset = UNSET
    execute_at: datetime.datetime | Unset = UNSET
    filters: list[ConditionSchema] | Unset = UNSET
    object_id: None | Unset | UUID = UNSET
    operations: list[TriggerSchemaOperationsItem] | Unset = UNSET
    realm: TriggerSchemaRealm | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_type = self.event_type.value

        type_ = self.type_.value

        date_created: str | Unset = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        date_modified: str | Unset = UNSET
        if not isinstance(self.date_modified, Unset):
            date_modified = self.date_modified.isoformat()

        execute_at: str | Unset = UNSET
        if not isinstance(self.execute_at, Unset):
            execute_at = self.execute_at.isoformat()

        filters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.filters, Unset):
            filters = []
            for filters_item_data in self.filters:
                filters_item = filters_item_data.to_dict()
                filters.append(filters_item)

        object_id: None | str | Unset
        if isinstance(self.object_id, Unset):
            object_id = UNSET
        elif isinstance(self.object_id, UUID):
            object_id = str(self.object_id)
        else:
            object_id = self.object_id

        operations: list[str] | Unset = UNSET
        if not isinstance(self.operations, Unset):
            operations = []
            for operations_item_data in self.operations:
                operations_item = operations_item_data.value
                operations.append(operations_item)

        realm: str | Unset = UNSET
        if not isinstance(self.realm, Unset):
            realm = self.realm.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event_type": event_type,
                "type": type_,
            }
        )
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if execute_at is not UNSET:
            field_dict["execute_at"] = execute_at
        if filters is not UNSET:
            field_dict["filters"] = filters
        if object_id is not UNSET:
            field_dict["object_id"] = object_id
        if operations is not UNSET:
            field_dict["operations"] = operations
        if realm is not UNSET:
            field_dict["realm"] = realm

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.condition_schema import ConditionSchema

        d = dict(src_dict)
        event_type = TriggerSchemaEventType(d.pop("event_type"))

        type_ = TriggerSchemaType(d.pop("type"))

        _date_created = d.pop("date_created", UNSET)
        date_created: datetime.datetime | Unset
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = datetime.datetime.fromisoformat(_date_created)

        _date_modified = d.pop("date_modified", UNSET)
        date_modified: datetime.datetime | Unset
        if isinstance(_date_modified, Unset):
            date_modified = UNSET
        else:
            date_modified = datetime.datetime.fromisoformat(_date_modified)

        _execute_at = d.pop("execute_at", UNSET)
        execute_at: datetime.datetime | Unset
        if isinstance(_execute_at, Unset):
            execute_at = UNSET
        else:
            execute_at = datetime.datetime.fromisoformat(_execute_at)

        _filters = d.pop("filters", UNSET)
        filters: list[ConditionSchema] | Unset = UNSET
        if _filters is not UNSET:
            filters = []
            for filters_item_data in _filters:
                filters_item = ConditionSchema.from_dict(filters_item_data)

                filters.append(filters_item)

        def _parse_object_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                object_id_type_0 = UUID(data)

                return object_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        object_id = _parse_object_id(d.pop("object_id", UNSET))

        _operations = d.pop("operations", UNSET)
        operations: list[TriggerSchemaOperationsItem] | Unset = UNSET
        if _operations is not UNSET:
            operations = []
            for operations_item_data in _operations:
                operations_item = TriggerSchemaOperationsItem(operations_item_data)

                operations.append(operations_item)

        _realm = d.pop("realm", UNSET)
        realm: TriggerSchemaRealm | Unset
        if isinstance(_realm, Unset):
            realm = UNSET
        else:
            realm = TriggerSchemaRealm(_realm)

        trigger_schema = cls(
            event_type=event_type,
            type_=type_,
            date_created=date_created,
            date_modified=date_modified,
            execute_at=execute_at,
            filters=filters,
            object_id=object_id,
            operations=operations,
            realm=realm,
        )

        trigger_schema.additional_properties = d
        return trigger_schema

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
