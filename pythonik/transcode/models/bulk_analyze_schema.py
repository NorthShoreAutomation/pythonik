from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
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
        force (bool | Unset):  Default: False.
        force_type (BulkAnalyzeSchemaForceType | Unset):  Default: BulkAnalyzeSchemaForceType.OVERWRITE.
        profile_id (UUID | Unset):
    """

    object_ids: list[UUID]
    object_type: BulkAnalyzeSchemaObjectType
    force: bool | Unset = False
    force_type: BulkAnalyzeSchemaForceType | Unset = (
        BulkAnalyzeSchemaForceType.OVERWRITE
    )
    profile_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_ids = []
        for object_ids_item_data in self.object_ids:
            object_ids_item = str(object_ids_item_data)
            object_ids.append(object_ids_item)

        object_type = self.object_type.value

        force = self.force

        force_type: str | Unset = UNSET
        if not isinstance(self.force_type, Unset):
            force_type = self.force_type.value

        profile_id: str | Unset = UNSET
        if not isinstance(self.profile_id, Unset):
            profile_id = str(self.profile_id)

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

        force = d.pop("force", UNSET)

        _force_type = d.pop("force_type", UNSET)
        force_type: BulkAnalyzeSchemaForceType | Unset
        if isinstance(_force_type, Unset):
            force_type = UNSET
        else:
            force_type = BulkAnalyzeSchemaForceType(_force_type)

        _profile_id = d.pop("profile_id", UNSET)
        profile_id: UUID | Unset
        if isinstance(_profile_id, Unset):
            profile_id = UNSET
        else:
            profile_id = UUID(_profile_id)

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
