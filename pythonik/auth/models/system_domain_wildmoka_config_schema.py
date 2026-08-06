from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SystemDomainWildmokaConfigSchema")


@_attrs_define
class SystemDomainWildmokaConfigSchema:
    """
    Attributes:
        api_base_url (None | str | Unset): Wildmoka API endpoint URL
        issuer (None | str | Unset): JWT issuer to use for authentication
        role_arn (None | str | Unset): AWS IAM role ARN for Wildmoka S3 access
        secret_key (None | str | Unset): JWT secret key to use for authentication
        ui_base_url (None | str | Unset): Wildmoka UI endpoint URL
    """

    api_base_url: None | str | Unset = UNSET
    issuer: None | str | Unset = UNSET
    role_arn: None | str | Unset = UNSET
    secret_key: None | str | Unset = UNSET
    ui_base_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_base_url: None | str | Unset
        if isinstance(self.api_base_url, Unset):
            api_base_url = UNSET
        else:
            api_base_url = self.api_base_url

        issuer: None | str | Unset
        if isinstance(self.issuer, Unset):
            issuer = UNSET
        else:
            issuer = self.issuer

        role_arn: None | str | Unset
        if isinstance(self.role_arn, Unset):
            role_arn = UNSET
        else:
            role_arn = self.role_arn

        secret_key: None | str | Unset
        if isinstance(self.secret_key, Unset):
            secret_key = UNSET
        else:
            secret_key = self.secret_key

        ui_base_url: None | str | Unset
        if isinstance(self.ui_base_url, Unset):
            ui_base_url = UNSET
        else:
            ui_base_url = self.ui_base_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_base_url is not UNSET:
            field_dict["api_base_url"] = api_base_url
        if issuer is not UNSET:
            field_dict["issuer"] = issuer
        if role_arn is not UNSET:
            field_dict["role_arn"] = role_arn
        if secret_key is not UNSET:
            field_dict["secret_key"] = secret_key
        if ui_base_url is not UNSET:
            field_dict["ui_base_url"] = ui_base_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_api_base_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        api_base_url = _parse_api_base_url(d.pop("api_base_url", UNSET))

        def _parse_issuer(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        issuer = _parse_issuer(d.pop("issuer", UNSET))

        def _parse_role_arn(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        role_arn = _parse_role_arn(d.pop("role_arn", UNSET))

        def _parse_secret_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        secret_key = _parse_secret_key(d.pop("secret_key", UNSET))

        def _parse_ui_base_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ui_base_url = _parse_ui_base_url(d.pop("ui_base_url", UNSET))

        system_domain_wildmoka_config_schema = cls(
            api_base_url=api_base_url,
            issuer=issuer,
            role_arn=role_arn,
            secret_key=secret_key,
            ui_base_url=ui_base_url,
        )

        system_domain_wildmoka_config_schema.additional_properties = d
        return system_domain_wildmoka_config_schema

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
