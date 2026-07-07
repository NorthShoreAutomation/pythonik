from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_shares_by_share_id_acl_by_object_type_by_object_key_by_permission_response_default_type_1_errors import (
        GetSharesByShareIdAclByObjectTypeByObjectKeyByPermissionResponseDefaultType1Errors,
    )


T = TypeVar(
    "T",
    bound="GetSharesByShareIdAclByObjectTypeByObjectKeyByPermissionResponseDefaultType1",
)


@_attrs_define
class GetSharesByShareIdAclByObjectTypeByObjectKeyByPermissionResponseDefaultType1:
    """
    Attributes:
        errors (GetSharesByShareIdAclByObjectTypeByObjectKeyByPermissionResponseDefaultType1Errors | Unset):
    """

    errors: (
        GetSharesByShareIdAclByObjectTypeByObjectKeyByPermissionResponseDefaultType1Errors
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
        from ..models.get_shares_by_share_id_acl_by_object_type_by_object_key_by_permission_response_default_type_1_errors import (
            GetSharesByShareIdAclByObjectTypeByObjectKeyByPermissionResponseDefaultType1Errors,
        )

        d = dict(src_dict)
        _errors = d.pop("errors", UNSET)
        errors: (
            GetSharesByShareIdAclByObjectTypeByObjectKeyByPermissionResponseDefaultType1Errors
            | Unset
        )
        if isinstance(_errors, Unset):
            errors = UNSET
        else:
            errors = GetSharesByShareIdAclByObjectTypeByObjectKeyByPermissionResponseDefaultType1Errors.from_dict(
                _errors
            )

        get_shares_by_share_id_acl_by_object_type_by_object_key_by_permission_response_default_type_1 = cls(
            errors=errors,
        )

        get_shares_by_share_id_acl_by_object_type_by_object_key_by_permission_response_default_type_1.additional_properties = d
        return get_shares_by_share_id_acl_by_object_type_by_object_key_by_permission_response_default_type_1

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
