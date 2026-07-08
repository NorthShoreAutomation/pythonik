from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_share_upload_edit_schema_status_type_1 import (
        FileShareUploadEditSchemaStatusType1,
    )


T = TypeVar("T", bound="FileShareUploadEditSchema")


@_attrs_define
class FileShareUploadEditSchema:
    """
    Attributes:
        size (int | None | Unset):
        status (FileShareUploadEditSchemaStatusType1 | None | Unset):
    """

    size: int | None | Unset = UNSET
    status: FileShareUploadEditSchemaStatusType1 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.file_share_upload_edit_schema_status_type_1 import (
            FileShareUploadEditSchemaStatusType1,
        )

        size: int | None | Unset
        if isinstance(self.size, Unset):
            size = UNSET
        else:
            size = self.size

        status: dict[str, Any] | None | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, FileShareUploadEditSchemaStatusType1):
            status = self.status.to_dict()
        else:
            status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if size is not UNSET:
            field_dict["size"] = size
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_share_upload_edit_schema_status_type_1 import (
            FileShareUploadEditSchemaStatusType1,
        )

        d = dict(src_dict)

        def _parse_size(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        size = _parse_size(d.pop("size", UNSET))

        def _parse_status(
            data: object,
        ) -> FileShareUploadEditSchemaStatusType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                status_type_1 = FileShareUploadEditSchemaStatusType1.from_dict(data)

                return status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FileShareUploadEditSchemaStatusType1 | None | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        file_share_upload_edit_schema = cls(
            size=size,
            status=status,
        )

        file_share_upload_edit_schema.additional_properties = d
        return file_share_upload_edit_schema

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
