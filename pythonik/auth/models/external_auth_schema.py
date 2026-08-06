from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

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
        app_id (None | str | Unset):
        date_created (datetime.datetime | None | Unset):
        redirect_info (None | RedirectInfoType | Unset):
        token (None | str | Unset):
    """

    app_id: None | str | Unset = UNSET
    date_created: datetime.datetime | None | Unset = UNSET
    redirect_info: None | RedirectInfoType | Unset = UNSET
    token: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.redirect_info_type import RedirectInfoType

        app_id: None | str | Unset
        if isinstance(self.app_id, Unset):
            app_id = UNSET
        else:
            app_id = self.app_id

        date_created: None | str | Unset
        if isinstance(self.date_created, Unset):
            date_created = UNSET
        elif isinstance(self.date_created, datetime.datetime):
            date_created = self.date_created.isoformat()
        else:
            date_created = self.date_created

        redirect_info: dict[str, Any] | None | Unset
        if isinstance(self.redirect_info, Unset):
            redirect_info = UNSET
        elif isinstance(self.redirect_info, RedirectInfoType):
            redirect_info = self.redirect_info.to_dict()
        else:
            redirect_info = self.redirect_info

        token: None | str | Unset
        if isinstance(self.token, Unset):
            token = UNSET
        else:
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

        def _parse_app_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        app_id = _parse_app_id(d.pop("app_id", UNSET))

        def _parse_date_created(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_created_type_0 = datetime.datetime.fromisoformat(data)

                return date_created_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_created = _parse_date_created(d.pop("date_created", UNSET))

        def _parse_redirect_info(data: object) -> None | RedirectInfoType | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                redirect_info_type_1 = RedirectInfoType.from_dict(data)

                return redirect_info_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RedirectInfoType | Unset, data)

        redirect_info = _parse_redirect_info(d.pop("redirect_info", UNSET))

        def _parse_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        token = _parse_token(d.pop("token", UNSET))

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
