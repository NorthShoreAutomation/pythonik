from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ai_feature_state_schema_status import AIFeatureStateSchemaStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ai_consent_document_schema import AIConsentDocumentSchema


T = TypeVar("T", bound="AIFeatureStateSchema")


@_attrs_define
class AIFeatureStateSchema:
    """
    Attributes:
        billing_tiers (list[str] | None | Unset): Billing tiers that grant this feature, as an alternative to its
            feature flag. Empty when no tier does: the feature is then gated on the flag alone.
        consent_enforced (bool | None | Unset): False while the interface for accepting this feature's terms is still
            being built: `documents_to_accept` is reported as usual, but it neither blocks enabling the feature nor masks it
            off.
        documents_to_accept (list[AIConsentDocumentSchema] | None | Unset): Accept these to satisfy what this feature is
            missing. Empty when nothing is.
        effective (bool | None | Unset): What the feature actually does. False as soon as the master switch is off, the
            consent is missing or stale, or the domain lost the entitlement.
        enabled (bool | None | Unset): What the administrator asked for.
        id (None | str | Unset):
        setting_name (None | str | Unset):
        status (AIFeatureStateSchemaStatus | None | Unset):
    """

    billing_tiers: list[str] | None | Unset = UNSET
    consent_enforced: bool | None | Unset = UNSET
    documents_to_accept: list[AIConsentDocumentSchema] | None | Unset = UNSET
    effective: bool | None | Unset = UNSET
    enabled: bool | None | Unset = UNSET
    id: None | str | Unset = UNSET
    setting_name: None | str | Unset = UNSET
    status: AIFeatureStateSchemaStatus | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        billing_tiers: list[str] | None | Unset
        if isinstance(self.billing_tiers, Unset):
            billing_tiers = UNSET
        elif isinstance(self.billing_tiers, list):
            billing_tiers = self.billing_tiers

        else:
            billing_tiers = self.billing_tiers

        consent_enforced: bool | None | Unset
        if isinstance(self.consent_enforced, Unset):
            consent_enforced = UNSET
        else:
            consent_enforced = self.consent_enforced

        documents_to_accept: list[dict[str, Any]] | None | Unset
        if isinstance(self.documents_to_accept, Unset):
            documents_to_accept = UNSET
        elif isinstance(self.documents_to_accept, list):
            documents_to_accept = []
            for documents_to_accept_type_0_item_data in self.documents_to_accept:
                documents_to_accept_type_0_item = (
                    documents_to_accept_type_0_item_data.to_dict()
                )
                documents_to_accept.append(documents_to_accept_type_0_item)

        else:
            documents_to_accept = self.documents_to_accept

        effective: bool | None | Unset
        if isinstance(self.effective, Unset):
            effective = UNSET
        else:
            effective = self.effective

        enabled: bool | None | Unset
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        setting_name: None | str | Unset
        if isinstance(self.setting_name, Unset):
            setting_name = UNSET
        else:
            setting_name = self.setting_name

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, AIFeatureStateSchemaStatus):
            status = self.status.value
        else:
            status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if billing_tiers is not UNSET:
            field_dict["billing_tiers"] = billing_tiers
        if consent_enforced is not UNSET:
            field_dict["consent_enforced"] = consent_enforced
        if documents_to_accept is not UNSET:
            field_dict["documents_to_accept"] = documents_to_accept
        if effective is not UNSET:
            field_dict["effective"] = effective
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if id is not UNSET:
            field_dict["id"] = id
        if setting_name is not UNSET:
            field_dict["setting_name"] = setting_name
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ai_consent_document_schema import AIConsentDocumentSchema

        d = dict(src_dict)

        def _parse_billing_tiers(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                billing_tiers_type_0 = cast(list[str], data)

                return billing_tiers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        billing_tiers = _parse_billing_tiers(d.pop("billing_tiers", UNSET))

        def _parse_consent_enforced(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        consent_enforced = _parse_consent_enforced(d.pop("consent_enforced", UNSET))

        def _parse_documents_to_accept(
            data: object,
        ) -> list[AIConsentDocumentSchema] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                documents_to_accept_type_0 = []
                _documents_to_accept_type_0 = data
                for documents_to_accept_type_0_item_data in _documents_to_accept_type_0:
                    documents_to_accept_type_0_item = AIConsentDocumentSchema.from_dict(
                        documents_to_accept_type_0_item_data
                    )

                    documents_to_accept_type_0.append(documents_to_accept_type_0_item)

                return documents_to_accept_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AIConsentDocumentSchema] | None | Unset, data)

        documents_to_accept = _parse_documents_to_accept(
            d.pop("documents_to_accept", UNSET)
        )

        def _parse_effective(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        effective = _parse_effective(d.pop("effective", UNSET))

        def _parse_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_setting_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        setting_name = _parse_setting_name(d.pop("setting_name", UNSET))

        def _parse_status(data: object) -> AIFeatureStateSchemaStatus | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_1 = AIFeatureStateSchemaStatus(data)

                return status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AIFeatureStateSchemaStatus | None | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        ai_feature_state_schema = cls(
            billing_tiers=billing_tiers,
            consent_enforced=consent_enforced,
            documents_to_accept=documents_to_accept,
            effective=effective,
            enabled=enabled,
            id=id,
            setting_name=setting_name,
            status=status,
        )

        ai_feature_state_schema.additional_properties = d
        return ai_feature_state_schema

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
