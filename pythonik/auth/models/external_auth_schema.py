from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.redirect_info_type import RedirectInfoType


T = TypeVar("T", bound="ExternalAuthSchema")


@_attrs_define
class ExternalAuthSchema:
    """
    Attributes:
        app_id (str | Unset):
        date_created (datetime.datetime | Unset):
        redirect_info (RedirectInfoType | Unset):
        token (str | Unset):
    """

    app_id: str | Unset = UNSET
    date_created: datetime.datetime | Unset = UNSET
    redirect_info: RedirectInfoType | Unset = UNSET
    token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_id = self.app_id

        date_created: str | Unset = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        redirect_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.redirect_info, Unset):
            redirect_info = self.redirect_info.to_dict()

        token = self.token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_id is not UNSET:
            field_dict["app_id"] = app_id
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if redirect_info is not UNSET:
            field_dict["redirect_info"] = redirect_info
        if token is not UNSET:
            field_dict["token"] = token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.redirect_info_type import RedirectInfoType

        d = dict(src_dict)
        app_id = d.pop("app_id", UNSET)

        _date_created = d.pop("date_created", UNSET)
        date_created: datetime.datetime | Unset
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = datetime.datetime.fromisoformat(_date_created)

        _redirect_info = d.pop("redirect_info", UNSET)
        redirect_info: RedirectInfoType | Unset
        if isinstance(_redirect_info, Unset):
            redirect_info = UNSET
        else:
            redirect_info = RedirectInfoType.from_dict(_redirect_info)

        token = d.pop("token", UNSET)

        external_auth_schema = cls(
            app_id=app_id,
            date_created=date_created,
            redirect_info=redirect_info,
            token=token,
        )

        external_auth_schema.additional_properties = d
        return external_auth_schema

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
