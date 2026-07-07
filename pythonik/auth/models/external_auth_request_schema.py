from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.redirect_info_type import RedirectInfoType


T = TypeVar("T", bound="ExternalAuthRequestSchema")


@_attrs_define
class ExternalAuthRequestSchema:
    """
    Attributes:
        secret (str):
        app_id (UUID | Unset):
        app_name (str | Unset):
        redirect_info (None | RedirectInfoType | Unset):
    """

    secret: str
    app_id: UUID | Unset = UNSET
    app_name: str | Unset = UNSET
    redirect_info: None | RedirectInfoType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.redirect_info_type import RedirectInfoType

        secret = self.secret

        app_id: str | Unset = UNSET
        if not isinstance(self.app_id, Unset):
            app_id = str(self.app_id)

        app_name = self.app_name

        redirect_info: dict[str, Any] | None | Unset
        if isinstance(self.redirect_info, Unset):
            redirect_info = UNSET
        elif isinstance(self.redirect_info, RedirectInfoType):
            redirect_info = self.redirect_info.to_dict()
        else:
            redirect_info = self.redirect_info

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "secret": secret,
            }
        )
        if app_id is not UNSET:
            field_dict["app_id"] = app_id
        if app_name is not UNSET:
            field_dict["app_name"] = app_name
        if redirect_info is not UNSET:
            field_dict["redirect_info"] = redirect_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.redirect_info_type import RedirectInfoType

        d = dict(src_dict)
        secret = d.pop("secret")

        _app_id = d.pop("app_id", UNSET)
        app_id: UUID | Unset
        if isinstance(_app_id, Unset):
            app_id = UNSET
        else:
            app_id = UUID(_app_id)

        app_name = d.pop("app_name", UNSET)

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

        external_auth_request_schema = cls(
            secret=secret,
            app_id=app_id,
            app_name=app_name,
            redirect_info=redirect_info,
        )

        external_auth_request_schema.additional_properties = d
        return external_auth_request_schema

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
