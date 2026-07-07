from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RecentAssetElasticSchema")


@_attrs_define
class RecentAssetElasticSchema:
    """
    Attributes:
        date_viewed (datetime.datetime | Unset):
        object_id (UUID | Unset):
        object_type (str | Unset):
        system_domain_id (UUID | Unset):
        user_id (UUID | Unset):
    """

    date_viewed: datetime.datetime | Unset = UNSET
    object_id: UUID | Unset = UNSET
    object_type: str | Unset = UNSET
    system_domain_id: UUID | Unset = UNSET
    user_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date_viewed: str | Unset = UNSET
        if not isinstance(self.date_viewed, Unset):
            date_viewed = self.date_viewed.isoformat()

        object_id: str | Unset = UNSET
        if not isinstance(self.object_id, Unset):
            object_id = str(self.object_id)

        object_type = self.object_type

        system_domain_id: str | Unset = UNSET
        if not isinstance(self.system_domain_id, Unset):
            system_domain_id = str(self.system_domain_id)

        user_id: str | Unset = UNSET
        if not isinstance(self.user_id, Unset):
            user_id = str(self.user_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date_viewed is not UNSET:
            field_dict["date_viewed"] = date_viewed
        if object_id is not UNSET:
            field_dict["object_id"] = object_id
        if object_type is not UNSET:
            field_dict["object_type"] = object_type
        if system_domain_id is not UNSET:
            field_dict["system_domain_id"] = system_domain_id
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _date_viewed = d.pop("date_viewed", UNSET)
        date_viewed: datetime.datetime | Unset
        if isinstance(_date_viewed, Unset):
            date_viewed = UNSET
        else:
            date_viewed = datetime.datetime.fromisoformat(_date_viewed)

        _object_id = d.pop("object_id", UNSET)
        object_id: UUID | Unset
        if isinstance(_object_id, Unset):
            object_id = UNSET
        else:
            object_id = UUID(_object_id)

        object_type = d.pop("object_type", UNSET)

        _system_domain_id = d.pop("system_domain_id", UNSET)
        system_domain_id: UUID | Unset
        if isinstance(_system_domain_id, Unset):
            system_domain_id = UNSET
        else:
            system_domain_id = UUID(_system_domain_id)

        _user_id = d.pop("user_id", UNSET)
        user_id: UUID | Unset
        if isinstance(_user_id, Unset):
            user_id = UNSET
        else:
            user_id = UUID(_user_id)

        recent_asset_elastic_schema = cls(
            date_viewed=date_viewed,
            object_id=object_id,
            object_type=object_type,
            system_domain_id=system_domain_id,
            user_id=user_id,
        )

        recent_asset_elastic_schema.additional_properties = d
        return recent_asset_elastic_schema

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
