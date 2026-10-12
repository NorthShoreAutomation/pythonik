from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.kind_descriptor_schema_options_schema import (
        KindDescriptorSchemaOptionsSchema,
    )


T = TypeVar("T", bound="KindDescriptorSchema")


@_attrs_define
class KindDescriptorSchema:
    """One installed plugin kind and the JSON schema of its options.

    ``options_schema`` is the pydantic JSON schema of the plugin's options
    model — secret fields carry ``format: password`` / ``writeOnly: true``,
    which is exactly what an onboarding UI needs to render them.

        Attributes:
            kind (str):
            options_schema (KindDescriptorSchemaOptionsSchema):
    """

    kind: str
    options_schema: KindDescriptorSchemaOptionsSchema
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind

        options_schema = self.options_schema.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "options_schema": options_schema,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.kind_descriptor_schema_options_schema import (
            KindDescriptorSchemaOptionsSchema,
        )

        d = dict(src_dict)
        kind = d.pop("kind")

        options_schema = KindDescriptorSchemaOptionsSchema.from_dict(
            d.pop("options_schema")
        )

        kind_descriptor_schema = cls(
            kind=kind,
            options_schema=options_schema,
        )

        kind_descriptor_schema.additional_properties = d
        return kind_descriptor_schema

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
