from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AIMetadataFillingActionParameters")


@_attrs_define
class AIMetadataFillingActionParameters:
    """
    Attributes:
        metadata_view_id (UUID):
        overwrite (bool):
        field_names (list[str] | None | Unset):
    """

    metadata_view_id: UUID
    overwrite: bool
    field_names: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metadata_view_id = str(self.metadata_view_id)

        overwrite = self.overwrite

        field_names: list[str] | None | Unset
        if isinstance(self.field_names, Unset):
            field_names = UNSET
        elif isinstance(self.field_names, list):
            field_names = self.field_names

        else:
            field_names = self.field_names

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "metadata_view_id": metadata_view_id,
                "overwrite": overwrite,
            }
        )
        if field_names is not UNSET:
            field_dict["field_names"] = field_names

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        metadata_view_id = UUID(d.pop("metadata_view_id"))

        overwrite = d.pop("overwrite")

        def _parse_field_names(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                field_names_type_0 = cast(list[str], data)

                return field_names_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        field_names = _parse_field_names(d.pop("field_names", UNSET))

        ai_metadata_filling_action_parameters = cls(
            metadata_view_id=metadata_view_id,
            overwrite=overwrite,
            field_names=field_names,
        )

        ai_metadata_filling_action_parameters.additional_properties = d
        return ai_metadata_filling_action_parameters

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
