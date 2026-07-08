from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, File, FileTypes, Unset

T = TypeVar("T", bound="PostTeamsByTeamIdLogoBody")


@_attrs_define
class PostTeamsByTeamIdLogoBody:
    """
    Attributes:
        logo (File | None | Unset):
    """

    logo: File | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        logo: FileTypes | None | Unset
        if isinstance(self.logo, Unset):
            logo = UNSET
        elif isinstance(self.logo, File):
            logo = self.logo.to_tuple()

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

        def _parse_logo(data: object) -> File | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, bytes):
                    raise TypeError()
                logo_type_0 = File(payload=BytesIO(data))

                return logo_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(File | None | Unset, data)

        logo = _parse_logo(d.pop("logo", UNSET))

        post_teams_by_team_id_logo_body = cls(
            logo=logo,
        )

        post_teams_by_team_id_logo_body.additional_properties = d
        return post_teams_by_team_id_logo_body

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
