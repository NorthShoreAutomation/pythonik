from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_acl_action_type import UpdateACLActionType

if TYPE_CHECKING:
    from ..models.update_acl_action_parameters import UpdateACLActionParameters


T = TypeVar("T", bound="UpdateACLAction")


@_attrs_define
class UpdateACLAction:
    """
    Attributes:
        parameters (UpdateACLActionParameters):
        type_ (UpdateACLActionType):  Default: UpdateACLActionType.UPDATE_ACL.
    """

    parameters: UpdateACLActionParameters
    type_: UpdateACLActionType = UpdateACLActionType.UPDATE_ACL
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
        from ..models.update_acl_action_parameters import UpdateACLActionParameters

        d = dict(src_dict)
        parameters = UpdateACLActionParameters.from_dict(d.pop("parameters"))

        type_ = UpdateACLActionType(d.pop("type"))

        update_acl_action = cls(
            parameters=parameters,
            type_=type_,
        )

        update_acl_action.additional_properties = d
        return update_acl_action

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
