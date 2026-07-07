from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.upload_storage_schema_method import UploadStorageSchemaMethod
from ..types import UNSET, Unset

T = TypeVar("T", bound="UploadStorageSchema")


@_attrs_define
class UploadStorageSchema:
    """
    Attributes:
        add_uuid_to_filenames (bool):
        id (UUID):
        method (UploadStorageSchemaMethod):
        presign_md5_checksum (bool | Unset):
    """

    add_uuid_to_filenames: bool
    id: UUID
    method: UploadStorageSchemaMethod
    presign_md5_checksum: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        add_uuid_to_filenames = self.add_uuid_to_filenames

        id = str(self.id)

        method = self.method.value

        presign_md5_checksum = self.presign_md5_checksum

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "add_uuid_to_filenames": add_uuid_to_filenames,
                "id": id,
                "method": method,
            }
        )
        if presign_md5_checksum is not UNSET:
            field_dict["presign_md5_checksum"] = presign_md5_checksum

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        add_uuid_to_filenames = d.pop("add_uuid_to_filenames")

        id = UUID(d.pop("id"))

        method = UploadStorageSchemaMethod(d.pop("method"))

        presign_md5_checksum = d.pop("presign_md5_checksum", UNSET)

        upload_storage_schema = cls(
            add_uuid_to_filenames=add_uuid_to_filenames,
            id=id,
            method=method,
            presign_md5_checksum=presign_md5_checksum,
        )

        upload_storage_schema.additional_properties = d
        return upload_storage_schema

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
