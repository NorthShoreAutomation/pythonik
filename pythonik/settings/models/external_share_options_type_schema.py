from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.external_share_options_type_schema_show_for_groups import (
    ExternalShareOptionsTypeSchemaShowForGroups,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExternalShareOptionsTypeSchema")


@_attrs_define
class ExternalShareOptionsTypeSchema:
    """
    Attributes:
        groups (list[UUID] | None | Unset):
        show_for_groups (ExternalShareOptionsTypeSchemaShowForGroups | None | Unset):
    """

    groups: list[UUID] | None | Unset = UNSET
    show_for_groups: ExternalShareOptionsTypeSchemaShowForGroups | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        groups: list[str] | None | Unset
        if isinstance(self.groups, Unset):
            groups = UNSET
        elif isinstance(self.groups, list):
            groups = []
            for groups_type_0_item_data in self.groups:
                groups_type_0_item = str(groups_type_0_item_data)
                groups.append(groups_type_0_item)

        else:
            groups = self.groups

        show_for_groups: None | str | Unset
        if isinstance(self.show_for_groups, Unset):
            show_for_groups = UNSET
        elif isinstance(
            self.show_for_groups, ExternalShareOptionsTypeSchemaShowForGroups
        ):
            show_for_groups = self.show_for_groups.value
        else:
            show_for_groups = self.show_for_groups

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if groups is not UNSET:
            field_dict["groups"] = groups
        if show_for_groups is not UNSET:
            field_dict["show_for_groups"] = show_for_groups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_groups(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                groups_type_0 = []
                _groups_type_0 = data
                for groups_type_0_item_data in _groups_type_0:
                    groups_type_0_item = UUID(groups_type_0_item_data)

                    groups_type_0.append(groups_type_0_item)

                return groups_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        groups = _parse_groups(d.pop("groups", UNSET))

        def _parse_show_for_groups(
            data: object,
        ) -> ExternalShareOptionsTypeSchemaShowForGroups | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                show_for_groups_type_1 = ExternalShareOptionsTypeSchemaShowForGroups(
                    data
                )

                return show_for_groups_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                ExternalShareOptionsTypeSchemaShowForGroups | None | Unset, data
            )

        show_for_groups = _parse_show_for_groups(d.pop("show_for_groups", UNSET))

        external_share_options_type_schema = cls(
            groups=groups,
            show_for_groups=show_for_groups,
        )

        external_share_options_type_schema.additional_properties = d
        return external_share_options_type_schema

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
