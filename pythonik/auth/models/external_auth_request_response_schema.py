from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.redirect_info_type import RedirectInfoType


T = TypeVar("T", bound="ExternalAuthRequestResponseSchema")


@_attrs_define
class ExternalAuthRequestResponseSchema:
    """
    Attributes:
        app_id (UUID | Unset):
        redirect_info (RedirectInfoType | Unset):
    """

    app_id: UUID | Unset = UNSET
    redirect_info: RedirectInfoType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_id: str | Unset = UNSET
        if not isinstance(self.app_id, Unset):
            app_id = str(self.app_id)

        redirect_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.redirect_info, Unset):
            redirect_info = self.redirect_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_id is not UNSET:
            field_dict["app_id"] = app_id
        if redirect_info is not UNSET:
            field_dict["redirect_info"] = redirect_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.redirect_info_type import RedirectInfoType

        d = dict(src_dict)
        _app_id = d.pop("app_id", UNSET)
        app_id: UUID | Unset
        if isinstance(_app_id, Unset):
            app_id = UNSET
        else:
            app_id = UUID(_app_id)

        _redirect_info = d.pop("redirect_info", UNSET)
        redirect_info: RedirectInfoType | Unset
        if isinstance(_redirect_info, Unset):
            redirect_info = UNSET
        else:
            redirect_info = RedirectInfoType.from_dict(_redirect_info)

        external_auth_request_response_schema = cls(
            app_id=app_id,
            redirect_info=redirect_info,
        )

        external_auth_request_response_schema.additional_properties = d
        return external_auth_request_response_schema

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
