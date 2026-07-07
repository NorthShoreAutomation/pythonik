from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_exports_temporary_file_sets_by_file_set_id_storages_by_storage_id_response_default_type_1_errors import (
        PostExportsTemporaryFileSetsByFileSetIdStoragesByStorageIdResponseDefaultType1Errors,
    )


T = TypeVar(
    "T",
    bound="PostExportsTemporaryFileSetsByFileSetIdStoragesByStorageIdResponseDefaultType1",
)


@_attrs_define
class PostExportsTemporaryFileSetsByFileSetIdStoragesByStorageIdResponseDefaultType1:
    """
    Attributes:
        errors (PostExportsTemporaryFileSetsByFileSetIdStoragesByStorageIdResponseDefaultType1Errors | Unset):
    """

    errors: (
        PostExportsTemporaryFileSetsByFileSetIdStoragesByStorageIdResponseDefaultType1Errors
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        errors: dict[str, Any] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_exports_temporary_file_sets_by_file_set_id_storages_by_storage_id_response_default_type_1_errors import (
            PostExportsTemporaryFileSetsByFileSetIdStoragesByStorageIdResponseDefaultType1Errors,
        )

        d = dict(src_dict)
        _errors = d.pop("errors", UNSET)
        errors: (
            PostExportsTemporaryFileSetsByFileSetIdStoragesByStorageIdResponseDefaultType1Errors
            | Unset
        )
        if isinstance(_errors, Unset):
            errors = UNSET
        else:
            errors = PostExportsTemporaryFileSetsByFileSetIdStoragesByStorageIdResponseDefaultType1Errors.from_dict(
                _errors
            )

        post_exports_temporary_file_sets_by_file_set_id_storages_by_storage_id_response_default_type_1 = cls(
            errors=errors,
        )

        post_exports_temporary_file_sets_by_file_set_id_storages_by_storage_id_response_default_type_1.additional_properties = d
        return post_exports_temporary_file_sets_by_file_set_id_storages_by_storage_id_response_default_type_1

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
