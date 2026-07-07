from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.identity_provider_base_schema_saml_settings import (
        IdentityProviderBaseSchemaSamlSettings,
    )


T = TypeVar("T", bound="IdentityProviderBaseSchema")


@_attrs_define
class IdentityProviderBaseSchema:
    """
    Attributes:
        saml_settings (IdentityProviderBaseSchemaSamlSettings | Unset):
    """

    saml_settings: IdentityProviderBaseSchemaSamlSettings | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        saml_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.saml_settings, Unset):
            saml_settings = self.saml_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if saml_settings is not UNSET:
            field_dict["saml_settings"] = saml_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.identity_provider_base_schema_saml_settings import (
            IdentityProviderBaseSchemaSamlSettings,
        )

        d = dict(src_dict)
        _saml_settings = d.pop("saml_settings", UNSET)
        saml_settings: IdentityProviderBaseSchemaSamlSettings | Unset
        if isinstance(_saml_settings, Unset):
            saml_settings = UNSET
        else:
            saml_settings = IdentityProviderBaseSchemaSamlSettings.from_dict(
                _saml_settings
            )

        identity_provider_base_schema = cls(
            saml_settings=saml_settings,
        )

        identity_provider_base_schema.additional_properties = d
        return identity_provider_base_schema

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
