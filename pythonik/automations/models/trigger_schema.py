from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.trigger_schema_event_type import TriggerSchemaEventType
from ..models.trigger_schema_operations_type_0_item import (
    TriggerSchemaOperationsType0Item,
)
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
        date_created (datetime.datetime | None | Unset):
        date_modified (datetime.datetime | None | Unset):
        execute_at (datetime.datetime | None | Unset):
        filters (list[ConditionSchema] | None | Unset):
        object_id (None | Unset | UUID):
        operations (list[TriggerSchemaOperationsType0Item] | None | Unset):
        realm (None | TriggerSchemaRealm | Unset):
    """

    event_type: TriggerSchemaEventType
    type_: TriggerSchemaType
    date_created: datetime.datetime | None | Unset = UNSET
    date_modified: datetime.datetime | None | Unset = UNSET
    execute_at: datetime.datetime | None | Unset = UNSET
    filters: list[ConditionSchema] | None | Unset = UNSET
    object_id: None | Unset | UUID = UNSET
    operations: list[TriggerSchemaOperationsType0Item] | None | Unset = UNSET
    realm: None | TriggerSchemaRealm | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_type = self.event_type.value

        type_ = self.type_.value

        date_created: None | str | Unset
        if isinstance(self.date_created, Unset):
            date_created = UNSET
        elif isinstance(self.date_created, datetime.datetime):
            date_created = self.date_created.isoformat()
        else:
            date_created = self.date_created

        date_modified: None | str | Unset
        if isinstance(self.date_modified, Unset):
            date_modified = UNSET
        elif isinstance(self.date_modified, datetime.datetime):
            date_modified = self.date_modified.isoformat()
        else:
            date_modified = self.date_modified

        execute_at: None | str | Unset
        if isinstance(self.execute_at, Unset):
            execute_at = UNSET
        elif isinstance(self.execute_at, datetime.datetime):
            execute_at = self.execute_at.isoformat()
        else:
            execute_at = self.execute_at

        filters: list[dict[str, Any]] | None | Unset
        if isinstance(self.filters, Unset):
            filters = UNSET
        elif isinstance(self.filters, list):
            filters = []
            for filters_type_0_item_data in self.filters:
                filters_type_0_item = filters_type_0_item_data.to_dict()
                filters.append(filters_type_0_item)

        else:
            filters = self.filters

        object_id: None | str | Unset
        if isinstance(self.object_id, Unset):
            object_id = UNSET
        elif isinstance(self.object_id, UUID):
            object_id = str(self.object_id)
        else:
            object_id = self.object_id

        operations: list[str] | None | Unset
        if isinstance(self.operations, Unset):
            operations = UNSET
        elif isinstance(self.operations, list):
            operations = []
            for operations_type_0_item_data in self.operations:
                operations_type_0_item = operations_type_0_item_data.value
                operations.append(operations_type_0_item)

        else:
            operations = self.operations

        realm: None | str | Unset
        if isinstance(self.realm, Unset):
            realm = UNSET
        elif isinstance(self.realm, TriggerSchemaRealm):
            realm = self.realm.value
        else:
            realm = self.realm

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

        def _parse_date_created(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_created_type_0 = datetime.datetime.fromisoformat(data)

                return date_created_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_created = _parse_date_created(d.pop("date_created", UNSET))

        def _parse_date_modified(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_modified_type_0 = datetime.datetime.fromisoformat(data)

                return date_modified_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_modified = _parse_date_modified(d.pop("date_modified", UNSET))

        def _parse_execute_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                execute_at_type_0 = datetime.datetime.fromisoformat(data)

                return execute_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        execute_at = _parse_execute_at(d.pop("execute_at", UNSET))

        def _parse_filters(data: object) -> list[ConditionSchema] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                filters_type_0 = []
                _filters_type_0 = data
                for filters_type_0_item_data in _filters_type_0:
                    filters_type_0_item = ConditionSchema.from_dict(
                        filters_type_0_item_data
                    )

                    filters_type_0.append(filters_type_0_item)

                return filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ConditionSchema] | None | Unset, data)

        filters = _parse_filters(d.pop("filters", UNSET))

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

        def _parse_operations(
            data: object,
        ) -> list[TriggerSchemaOperationsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                operations_type_0 = []
                _operations_type_0 = data
                for operations_type_0_item_data in _operations_type_0:
                    operations_type_0_item = TriggerSchemaOperationsType0Item(
                        operations_type_0_item_data
                    )

                    operations_type_0.append(operations_type_0_item)

                return operations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TriggerSchemaOperationsType0Item] | None | Unset, data)

        operations = _parse_operations(d.pop("operations", UNSET))

        def _parse_realm(data: object) -> None | TriggerSchemaRealm | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                realm_type_1 = TriggerSchemaRealm(data)

                return realm_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TriggerSchemaRealm | Unset, data)

        realm = _parse_realm(d.pop("realm", UNSET))

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
