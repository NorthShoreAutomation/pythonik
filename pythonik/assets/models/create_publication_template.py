from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_publication_template_apply_type_1 import (
        CreatePublicationTemplateApplyType1,
    )
    from ..models.create_publication_template_data import CreatePublicationTemplateData


T = TypeVar("T", bound="CreatePublicationTemplate")


@_attrs_define
class CreatePublicationTemplate:
    """
    Attributes:
        id (str):
        apply (bool | CreatePublicationTemplateApplyType1 | Unset):  Default: True.
        data (CreatePublicationTemplateData | Unset):
    """

    id: str
    apply: bool | CreatePublicationTemplateApplyType1 | Unset = True
    data: CreatePublicationTemplateData | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_publication_template_apply_type_1 import (
            CreatePublicationTemplateApplyType1,
        )

        id = self.id

        apply: bool | dict[str, Any] | Unset
        if isinstance(self.apply, Unset):
            apply = UNSET
        elif isinstance(self.apply, CreatePublicationTemplateApplyType1):
            apply = self.apply.to_dict()
        else:
            apply = self.apply

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

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
        from ..models.create_publication_template_apply_type_1 import (
            CreatePublicationTemplateApplyType1,
        )
        from ..models.create_publication_template_data import (
            CreatePublicationTemplateData,
        )

        d = dict(src_dict)
        id = d.pop("id")

        def _parse_apply(
            data: object,
        ) -> bool | CreatePublicationTemplateApplyType1 | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                apply_type_1 = CreatePublicationTemplateApplyType1.from_dict(data)

                return apply_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(bool | CreatePublicationTemplateApplyType1 | Unset, data)

        apply = _parse_apply(d.pop("apply", UNSET))

        _data = d.pop("data", UNSET)
        data: CreatePublicationTemplateData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = CreatePublicationTemplateData.from_dict(_data)

        create_publication_template = cls(
            id=id,
            apply=apply,
            data=data,
        )

        create_publication_template.additional_properties = d
        return create_publication_template

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
