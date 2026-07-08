from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.invitation_response_schema_domain_status import (
    InvitationResponseSchemaDomainStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auto_login_schema import AutoLoginSchema


T = TypeVar("T", bound="InvitationResponseSchema")


@_attrs_define
class InvitationResponseSchema:
    """
    Attributes:
        auto_login (bool | None | Unset):
        domain_status (InvitationResponseSchemaDomainStatus | None | Unset):
        login_data (AutoLoginSchema | None | Unset):
        user_id (None | Unset | UUID):
    """

    auto_login: bool | None | Unset = UNSET
    domain_status: InvitationResponseSchemaDomainStatus | None | Unset = UNSET
    login_data: AutoLoginSchema | None | Unset = UNSET
    user_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.auto_login_schema import AutoLoginSchema

        auto_login: bool | None | Unset
        if isinstance(self.auto_login, Unset):
            auto_login = UNSET
        else:
            auto_login = self.auto_login

        domain_status: None | str | Unset
        if isinstance(self.domain_status, Unset):
            domain_status = UNSET
        elif isinstance(self.domain_status, InvitationResponseSchemaDomainStatus):
            domain_status = self.domain_status.value
        else:
            domain_status = self.domain_status

        login_data: dict[str, Any] | None | Unset
        if isinstance(self.login_data, Unset):
            login_data = UNSET
        elif isinstance(self.login_data, AutoLoginSchema):
            login_data = self.login_data.to_dict()
        else:
            login_data = self.login_data

        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        elif isinstance(self.user_id, UUID):
            user_id = str(self.user_id)
        else:
            user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auto_login is not UNSET:
            field_dict["auto_login"] = auto_login
        if domain_status is not UNSET:
            field_dict["domain_status"] = domain_status
        if login_data is not UNSET:
            field_dict["login_data"] = login_data
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.auto_login_schema import AutoLoginSchema

        d = dict(src_dict)

        def _parse_auto_login(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        auto_login = _parse_auto_login(d.pop("auto_login", UNSET))

        def _parse_domain_status(
            data: object,
        ) -> InvitationResponseSchemaDomainStatus | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                domain_status_type_1 = InvitationResponseSchemaDomainStatus(data)

                return domain_status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InvitationResponseSchemaDomainStatus | None | Unset, data)

        domain_status = _parse_domain_status(d.pop("domain_status", UNSET))

        def _parse_login_data(data: object) -> AutoLoginSchema | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                login_data_type_1 = AutoLoginSchema.from_dict(data)

                return login_data_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AutoLoginSchema | None | Unset, data)

        login_data = _parse_login_data(d.pop("login_data", UNSET))

        def _parse_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                user_id_type_0 = UUID(data)

                return user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))

        invitation_response_schema = cls(
            auto_login=auto_login,
            domain_status=domain_status,
            login_data=login_data,
            user_id=user_id,
        )

        invitation_response_schema.additional_properties = d
        return invitation_response_schema

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
