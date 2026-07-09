from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bulk_analyze_schema_force_type import BulkAnalyzeSchemaForceType
from ..models.bulk_analyze_schema_object_type import BulkAnalyzeSchemaObjectType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BulkAnalyzeSchema")


@_attrs_define
class BulkAnalyzeSchema:
    """
    Attributes:
        object_ids (list[UUID]):
        object_type (BulkAnalyzeSchemaObjectType):
        force (bool | None | Unset):  Default: False.
        force_type (BulkAnalyzeSchemaForceType | None | Unset):
        profile_id (None | Unset | UUID):
    """

    object_ids: list[UUID]
    object_type: BulkAnalyzeSchemaObjectType
    force: bool | None | Unset = False
    force_type: BulkAnalyzeSchemaForceType | None | Unset = UNSET
    profile_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_ids = []
        for object_ids_item_data in self.object_ids:
            object_ids_item = str(object_ids_item_data)
            object_ids.append(object_ids_item)

        object_type = self.object_type.value

        force: bool | None | Unset
        if isinstance(self.force, Unset):
            force = UNSET
        else:
            force = self.force

        force_type: None | str | Unset
        if isinstance(self.force_type, Unset):
            force_type = UNSET
        elif isinstance(self.force_type, BulkAnalyzeSchemaForceType):
            force_type = self.force_type.value
        else:
            force_type = self.force_type

        profile_id: None | str | Unset
        if isinstance(self.profile_id, Unset):
            profile_id = UNSET
        elif isinstance(self.profile_id, UUID):
            profile_id = str(self.profile_id)
        else:
            profile_id = self.profile_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object_ids": object_ids,
                "object_type": object_type,
            }
        )
        if force is not UNSET:
            field_dict["force"] = force
        if force_type is not UNSET:
            field_dict["force_type"] = force_type
        if profile_id is not UNSET:
            field_dict["profile_id"] = profile_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        object_ids = []
        _object_ids = d.pop("object_ids")
        for object_ids_item_data in _object_ids:
            object_ids_item = UUID(object_ids_item_data)

            object_ids.append(object_ids_item)

        object_type = BulkAnalyzeSchemaObjectType(d.pop("object_type"))

        def _parse_force(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        force = _parse_force(d.pop("force", UNSET))

        def _parse_force_type(
            data: object,
        ) -> BulkAnalyzeSchemaForceType | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                force_type_type_1 = BulkAnalyzeSchemaForceType(data)

                return force_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BulkAnalyzeSchemaForceType | None | Unset, data)

        force_type = _parse_force_type(d.pop("force_type", UNSET))

        def _parse_profile_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                profile_id_type_0 = UUID(data)

                return profile_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        profile_id = _parse_profile_id(d.pop("profile_id", UNSET))

        bulk_analyze_schema = cls(
            object_ids=object_ids,
            object_type=object_type,
            force=force,
            force_type=force_type,
            profile_id=profile_id,
        )

        bulk_analyze_schema.additional_properties = d
        return bulk_analyze_schema

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
