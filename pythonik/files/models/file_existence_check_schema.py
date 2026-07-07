from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.file_existence_check_schema_file_type import (
    FileExistenceCheckSchemaFileType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="FileExistenceCheckSchema")


@_attrs_define
class FileExistenceCheckSchema:
    """
    Attributes:
        directory_path (str):
        file_name (str):
        file_type (FileExistenceCheckSchemaFileType | Unset):
        template (str | Unset):
        template_engine (str | Unset):
    """

    directory_path: str
    file_name: str
    file_type: FileExistenceCheckSchemaFileType | Unset = UNSET
    template: str | Unset = UNSET
    template_engine: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        directory_path = self.directory_path

        file_name = self.file_name

        file_type: str | Unset = UNSET
        if not isinstance(self.file_type, Unset):
            file_type = self.file_type.value

        template = self.template

        template_engine = self.template_engine

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "directory_path": directory_path,
                "file_name": file_name,
            }
        )
        if file_type is not UNSET:
            field_dict["file_type"] = file_type
        if template is not UNSET:
            field_dict["template"] = template
        if template_engine is not UNSET:
            field_dict["template_engine"] = template_engine

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        directory_path = d.pop("directory_path")

        file_name = d.pop("file_name")

        _file_type = d.pop("file_type", UNSET)
        file_type: FileExistenceCheckSchemaFileType | Unset
        if isinstance(_file_type, Unset):
            file_type = UNSET
        else:
            file_type = FileExistenceCheckSchemaFileType(_file_type)

        template = d.pop("template", UNSET)

        template_engine = d.pop("template_engine", UNSET)

        file_existence_check_schema = cls(
            directory_path=directory_path,
            file_name=file_name,
            file_type=file_type,
            template=template,
            template_engine=template_engine,
        )

        file_existence_check_schema.additional_properties = d
        return file_existence_check_schema

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
