from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StorageScanSchema")


@_attrs_define
class StorageScanSchema:
    """
    Attributes:
        files (list[str] | None | Unset):
        ignore_already_active (bool | None | Unset): Will force scanning even if the scan is already active if any of
            `paths` or `files` are specified.
        paths (list[str] | None | Unset):
    """

    files: list[str] | None | Unset = UNSET
    ignore_already_active: bool | None | Unset = UNSET
    paths: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        files: list[str] | None | Unset
        if isinstance(self.files, Unset):
            files = UNSET
        elif isinstance(self.files, list):
            files = self.files

        else:
            files = self.files

        ignore_already_active: bool | None | Unset
        if isinstance(self.ignore_already_active, Unset):
            ignore_already_active = UNSET
        else:
            ignore_already_active = self.ignore_already_active

        paths: list[str] | None | Unset
        if isinstance(self.paths, Unset):
            paths = UNSET
        elif isinstance(self.paths, list):
            paths = self.paths

        else:
            paths = self.paths

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if files is not UNSET:
            field_dict["files"] = files
        if ignore_already_active is not UNSET:
            field_dict["ignore_already_active"] = ignore_already_active
        if paths is not UNSET:
            field_dict["paths"] = paths

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_files(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                files_type_0 = cast(list[str], data)

                return files_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        files = _parse_files(d.pop("files", UNSET))

        def _parse_ignore_already_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        ignore_already_active = _parse_ignore_already_active(
            d.pop("ignore_already_active", UNSET)
        )

        def _parse_paths(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                paths_type_0 = cast(list[str], data)

                return paths_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        paths = _parse_paths(d.pop("paths", UNSET))

        storage_scan_schema = cls(
            files=files,
            ignore_already_active=ignore_already_active,
            paths=paths,
        )

        storage_scan_schema.additional_properties = d
        return storage_scan_schema

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
