from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AssetSharedTriggerParameters")


@_attrs_define
class AssetSharedTriggerParameters:
    """
    Attributes:
        allow_download (bool | None | Unset):
    """

    allow_download: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allow_download: bool | None | Unset
        if isinstance(self.allow_download, Unset):
            allow_download = UNSET
        else:
            allow_download = self.allow_download

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allow_download is not UNSET:
            field_dict["allow_download"] = allow_download

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_allow_download(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        allow_download = _parse_allow_download(d.pop("allow_download", UNSET))

        asset_shared_trigger_parameters = cls(
            allow_download=allow_download,
        )

        asset_shared_trigger_parameters.additional_properties = d
        return asset_shared_trigger_parameters

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
