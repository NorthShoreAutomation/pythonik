from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MultipartUploadCleanupSchema")


@_attrs_define
class MultipartUploadCleanupSchema:
    """
    Attributes:
        abort_upload (bool | None | Unset):
        parts_group_number (int | None | Unset):
        parts_number (int | None | Unset):
        temporary (bool | None | Unset):  Default: False.
        upload_id (None | str | Unset):
    """

    abort_upload: bool | None | Unset = UNSET
    parts_group_number: int | None | Unset = UNSET
    parts_number: int | None | Unset = UNSET
    temporary: bool | None | Unset = False
    upload_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        abort_upload: bool | None | Unset
        if isinstance(self.abort_upload, Unset):
            abort_upload = UNSET
        else:
            abort_upload = self.abort_upload

        parts_group_number: int | None | Unset
        if isinstance(self.parts_group_number, Unset):
            parts_group_number = UNSET
        else:
            parts_group_number = self.parts_group_number

        parts_number: int | None | Unset
        if isinstance(self.parts_number, Unset):
            parts_number = UNSET
        else:
            parts_number = self.parts_number

        temporary: bool | None | Unset
        if isinstance(self.temporary, Unset):
            temporary = UNSET
        else:
            temporary = self.temporary

        upload_id: None | str | Unset
        if isinstance(self.upload_id, Unset):
            upload_id = UNSET
        else:
            upload_id = self.upload_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if abort_upload is not UNSET:
            field_dict["abort_upload"] = abort_upload
        if parts_group_number is not UNSET:
            field_dict["parts_group_number"] = parts_group_number
        if parts_number is not UNSET:
            field_dict["parts_number"] = parts_number
        if temporary is not UNSET:
            field_dict["temporary"] = temporary
        if upload_id is not UNSET:
            field_dict["upload_id"] = upload_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_abort_upload(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        abort_upload = _parse_abort_upload(d.pop("abort_upload", UNSET))

        def _parse_parts_group_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        parts_group_number = _parse_parts_group_number(
            d.pop("parts_group_number", UNSET)
        )

        def _parse_parts_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        parts_number = _parse_parts_number(d.pop("parts_number", UNSET))

        def _parse_temporary(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        temporary = _parse_temporary(d.pop("temporary", UNSET))

        def _parse_upload_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        upload_id = _parse_upload_id(d.pop("upload_id", UNSET))

        multipart_upload_cleanup_schema = cls(
            abort_upload=abort_upload,
            parts_group_number=parts_group_number,
            parts_number=parts_number,
            temporary=temporary,
            upload_id=upload_id,
        )

        multipart_upload_cleanup_schema.additional_properties = d
        return multipart_upload_cleanup_schema

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
