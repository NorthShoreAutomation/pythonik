from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.upload_storage_method import UploadStorageMethod
from ..types import UNSET, Unset

T = TypeVar("T", bound="UploadStorage")


@_attrs_define
class UploadStorage:
    """
    Attributes:
        add_uuid_to_filenames (bool):
        id (UUID):
        method (UploadStorageMethod):
        presign_md5_checksum (bool | None | Unset):
    """

    add_uuid_to_filenames: bool
    id: UUID
    method: UploadStorageMethod
    presign_md5_checksum: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        add_uuid_to_filenames = self.add_uuid_to_filenames

        id = str(self.id)

        method = self.method.value

        presign_md5_checksum: bool | None | Unset
        if isinstance(self.presign_md5_checksum, Unset):
            presign_md5_checksum = UNSET
        else:
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

        method = UploadStorageMethod(d.pop("method"))

        def _parse_presign_md5_checksum(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        presign_md5_checksum = _parse_presign_md5_checksum(
            d.pop("presign_md5_checksum", UNSET)
        )

        upload_storage = cls(
            add_uuid_to_filenames=add_uuid_to_filenames,
            id=id,
            method=method,
            presign_md5_checksum=presign_md5_checksum,
        )

        upload_storage.additional_properties = d
        return upload_storage

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
