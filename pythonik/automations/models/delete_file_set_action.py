from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.delete_file_set_action_type import DeleteFileSetActionType

if TYPE_CHECKING:
    from ..models.delete_file_set_action_parameters import DeleteFileSetActionParameters


T = TypeVar("T", bound="DeleteFileSetAction")


@_attrs_define
class DeleteFileSetAction:
    """
    Attributes:
        parameters (DeleteFileSetActionParameters):
        type_ (DeleteFileSetActionType):  Default: DeleteFileSetActionType.DELETE_FILE_SET.
    """

    parameters: DeleteFileSetActionParameters
    type_: DeleteFileSetActionType = DeleteFileSetActionType.DELETE_FILE_SET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parameters = self.parameters.to_dict()

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "parameters": parameters,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.delete_file_set_action_parameters import (
            DeleteFileSetActionParameters,
        )

        d = dict(src_dict)
        parameters = DeleteFileSetActionParameters.from_dict(d.pop("parameters"))

        type_ = DeleteFileSetActionType(d.pop("type"))

        delete_file_set_action = cls(
            parameters=parameters,
            type_=type_,
        )

        delete_file_set_action.additional_properties = d
        return delete_file_set_action

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
