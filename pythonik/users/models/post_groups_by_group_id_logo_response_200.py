from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostGroupsByGroupIdLogoResponse200")


@_attrs_define
class PostGroupsByGroupIdLogoResponse200:
    """
    Attributes:
        logo (None | str | Unset): Url for the group logo
    """

    logo: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        logo: None | str | Unset
        if isinstance(self.logo, Unset):
            logo = UNSET
        else:
            logo = self.logo

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if logo is not UNSET:
            field_dict["logo"] = logo

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_logo(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        logo = _parse_logo(d.pop("logo", UNSET))

        post_groups_by_group_id_logo_response_200 = cls(
            logo=logo,
        )

        post_groups_by_group_id_logo_response_200.additional_properties = d
        return post_groups_by_group_id_logo_response_200

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
