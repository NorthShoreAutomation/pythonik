from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_existence_check_schema_file_type_type_1 import (
        FileExistenceCheckSchemaFileTypeType1,
    )


T = TypeVar("T", bound="FileExistenceCheckSchema")


@_attrs_define
class FileExistenceCheckSchema:
    """
    Attributes:
        directory_path (str):
        file_name (str):
        file_type (FileExistenceCheckSchemaFileTypeType1 | None | Unset):
        template (None | str | Unset):
        template_engine (None | str | Unset):
    """

    directory_path: str
    file_name: str
    file_type: FileExistenceCheckSchemaFileTypeType1 | None | Unset = UNSET
    template: None | str | Unset = UNSET
    template_engine: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.file_existence_check_schema_file_type_type_1 import (
            FileExistenceCheckSchemaFileTypeType1,
        )

        directory_path = self.directory_path

        file_name = self.file_name

        file_type: dict[str, Any] | None | Unset
        if isinstance(self.file_type, Unset):
            file_type = UNSET
        elif isinstance(self.file_type, FileExistenceCheckSchemaFileTypeType1):
            file_type = self.file_type.to_dict()
        else:
            file_type = self.file_type

        template: None | str | Unset
        if isinstance(self.template, Unset):
            template = UNSET
        else:
            template = self.template

        template_engine: None | str | Unset
        if isinstance(self.template_engine, Unset):
            template_engine = UNSET
        else:
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
        from ..models.file_existence_check_schema_file_type_type_1 import (
            FileExistenceCheckSchemaFileTypeType1,
        )

        d = dict(src_dict)
        directory_path = d.pop("directory_path")

        file_name = d.pop("file_name")

        def _parse_file_type(
            data: object,
        ) -> FileExistenceCheckSchemaFileTypeType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                file_type_type_1 = FileExistenceCheckSchemaFileTypeType1.from_dict(data)

                return file_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FileExistenceCheckSchemaFileTypeType1 | None | Unset, data)

        file_type = _parse_file_type(d.pop("file_type", UNSET))

        def _parse_template(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        template = _parse_template(d.pop("template", UNSET))

        def _parse_template_engine(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        template_engine = _parse_template_engine(d.pop("template_engine", UNSET))

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
