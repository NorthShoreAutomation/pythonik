from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ai_consent_schema import AIConsentSchema
    from ..models.ai_state_schema_features_type_0 import AIStateSchemaFeaturesType0


T = TypeVar("T", bound="AIStateSchema")


@_attrs_define
class AIStateSchema:
    """
    Attributes:
        consents (list[AIConsentSchema] | None | Unset): Every position this customer has taken, accepted and refused
            alike. A refusal does not switch anything off by itself: it stops the terms taking effect by non-objection.
        disabled_by_domain (bool | None | Unset): The platform forbids AI on this system domain. Every feature reads as
            UNAVAILABLE and nothing can be enabled. Not something the customer can change; the interface should explain
            rather than offer a switch.
        enabled (bool | None | Unset): Master switch.
        features (AIStateSchemaFeaturesType0 | None | Unset):
    """

    consents: list[AIConsentSchema] | None | Unset = UNSET
    disabled_by_domain: bool | None | Unset = UNSET
    enabled: bool | None | Unset = UNSET
    features: AIStateSchemaFeaturesType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.ai_state_schema_features_type_0 import AIStateSchemaFeaturesType0

        consents: list[dict[str, Any]] | None | Unset
        if isinstance(self.consents, Unset):
            consents = UNSET
        elif isinstance(self.consents, list):
            consents = []
            for consents_type_0_item_data in self.consents:
                consents_type_0_item = consents_type_0_item_data.to_dict()
                consents.append(consents_type_0_item)

        else:
            consents = self.consents

        disabled_by_domain: bool | None | Unset
        if isinstance(self.disabled_by_domain, Unset):
            disabled_by_domain = UNSET
        else:
            disabled_by_domain = self.disabled_by_domain

        enabled: bool | None | Unset
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        features: dict[str, Any] | None | Unset
        if isinstance(self.features, Unset):
            features = UNSET
        elif isinstance(self.features, AIStateSchemaFeaturesType0):
            features = self.features.to_dict()
        else:
            features = self.features

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if consents is not UNSET:
            field_dict["consents"] = consents
        if disabled_by_domain is not UNSET:
            field_dict["disabled_by_domain"] = disabled_by_domain
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if features is not UNSET:
            field_dict["features"] = features

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ai_consent_schema import AIConsentSchema
        from ..models.ai_state_schema_features_type_0 import AIStateSchemaFeaturesType0

        d = dict(src_dict)

        def _parse_consents(data: object) -> list[AIConsentSchema] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                consents_type_0 = []
                _consents_type_0 = data
                for consents_type_0_item_data in _consents_type_0:
                    consents_type_0_item = AIConsentSchema.from_dict(
                        consents_type_0_item_data
                    )

                    consents_type_0.append(consents_type_0_item)

                return consents_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AIConsentSchema] | None | Unset, data)

        consents = _parse_consents(d.pop("consents", UNSET))

        def _parse_disabled_by_domain(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        disabled_by_domain = _parse_disabled_by_domain(
            d.pop("disabled_by_domain", UNSET)
        )

        def _parse_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))

        def _parse_features(data: object) -> AIStateSchemaFeaturesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                features_type_0 = AIStateSchemaFeaturesType0.from_dict(data)

                return features_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AIStateSchemaFeaturesType0 | None | Unset, data)

        features = _parse_features(d.pop("features", UNSET))

        ai_state_schema = cls(
            consents=consents,
            disabled_by_domain=disabled_by_domain,
            enabled=enabled,
            features=features,
        )

        ai_state_schema.additional_properties = d
        return ai_state_schema

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
