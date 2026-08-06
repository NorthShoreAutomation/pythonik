from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_publication_template_schema_apply_type_1 import (
        CreatePublicationTemplateSchemaApplyType1,
    )
    from ..models.create_publication_template_schema_data_type_0 import (
        CreatePublicationTemplateSchemaDataType0,
    )


T = TypeVar("T", bound="CreatePublicationTemplateSchema")


@_attrs_define
class CreatePublicationTemplateSchema:
    """
    Attributes:
        id (str):
        apply (bool | CreatePublicationTemplateSchemaApplyType1 | None | Unset):  Default: True.
        data (CreatePublicationTemplateSchemaDataType0 | None | Unset):
    """

    id: str
    apply: bool | CreatePublicationTemplateSchemaApplyType1 | None | Unset = True
    data: CreatePublicationTemplateSchemaDataType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_publication_template_schema_apply_type_1 import (
            CreatePublicationTemplateSchemaApplyType1,
        )
        from ..models.create_publication_template_schema_data_type_0 import (
            CreatePublicationTemplateSchemaDataType0,
        )

        id = self.id

        apply: bool | dict[str, Any] | None | Unset
        if isinstance(self.apply, Unset):
            apply = UNSET
        elif isinstance(self.apply, CreatePublicationTemplateSchemaApplyType1):
            apply = self.apply.to_dict()
        else:
            apply = self.apply

        data: dict[str, Any] | None | Unset
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, CreatePublicationTemplateSchemaDataType0):
            data = self.data.to_dict()
        else:
            data = self.data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if apply is not UNSET:
            field_dict["apply"] = apply
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_publication_template_schema_apply_type_1 import (
            CreatePublicationTemplateSchemaApplyType1,
        )
        from ..models.create_publication_template_schema_data_type_0 import (
            CreatePublicationTemplateSchemaDataType0,
        )

        d = dict(src_dict)
        id = d.pop("id")

        def _parse_apply(
            data: object,
        ) -> bool | CreatePublicationTemplateSchemaApplyType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                apply_type_1 = CreatePublicationTemplateSchemaApplyType1.from_dict(data)

                return apply_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                bool | CreatePublicationTemplateSchemaApplyType1 | None | Unset, data
            )

        apply = _parse_apply(d.pop("apply", UNSET))

        def _parse_data(
            data: object,
        ) -> CreatePublicationTemplateSchemaDataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = CreatePublicationTemplateSchemaDataType0.from_dict(data)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreatePublicationTemplateSchemaDataType0 | None | Unset, data)

        data = _parse_data(d.pop("data", UNSET))

        create_publication_template_schema = cls(
            id=id,
            apply=apply,
            data=data,
        )

        create_publication_template_schema.additional_properties = d
        return create_publication_template_schema

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
