from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="VersionOnlineTriggerParameters")


@_attrs_define
class VersionOnlineTriggerParameters:
    """
    Attributes:
        only_first_version (bool):
        wait_for_transcode (bool):
    """

    only_first_version: bool
    wait_for_transcode: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        only_first_version = self.only_first_version

        wait_for_transcode = self.wait_for_transcode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "only_first_version": only_first_version,
                "wait_for_transcode": wait_for_transcode,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        only_first_version = d.pop("only_first_version")

        wait_for_transcode = d.pop("wait_for_transcode")

        version_online_trigger_parameters = cls(
            only_first_version=only_first_version,
            wait_for_transcode=wait_for_transcode,
        )

        version_online_trigger_parameters.additional_properties = d
        return version_online_trigger_parameters

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
