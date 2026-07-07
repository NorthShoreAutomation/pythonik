from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.paygo_costs_schema_storage_costs import PaygoCostsSchemaStorageCosts
    from ..models.paygo_costs_schema_user_costs import PaygoCostsSchemaUserCosts


T = TypeVar("T", bound="PaygoCostsSchema")


@_attrs_define
class PaygoCostsSchema:
    """
    Attributes:
        analysis_cost (float | Unset):
        automation_cost (float | Unset):
        edge_transcoder_cost (float | Unset):
        external_storage_cost (float | Unset):
        face_recognition_cost (float | Unset):
        shield_cost (float | Unset):
        storage_costs (PaygoCostsSchemaStorageCosts | Unset):
        total_spend (float | Unset):
        transcription_cost (float | Unset):
        user_costs (PaygoCostsSchemaUserCosts | Unset):
    """

    analysis_cost: float | Unset = UNSET
    automation_cost: float | Unset = UNSET
    edge_transcoder_cost: float | Unset = UNSET
    external_storage_cost: float | Unset = UNSET
    face_recognition_cost: float | Unset = UNSET
    shield_cost: float | Unset = UNSET
    storage_costs: PaygoCostsSchemaStorageCosts | Unset = UNSET
    total_spend: float | Unset = UNSET
    transcription_cost: float | Unset = UNSET
    user_costs: PaygoCostsSchemaUserCosts | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        analysis_cost = self.analysis_cost

        automation_cost = self.automation_cost

        edge_transcoder_cost = self.edge_transcoder_cost

        external_storage_cost = self.external_storage_cost

        face_recognition_cost = self.face_recognition_cost

        shield_cost = self.shield_cost

        storage_costs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.storage_costs, Unset):
            storage_costs = self.storage_costs.to_dict()

        total_spend = self.total_spend

        transcription_cost = self.transcription_cost

        user_costs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user_costs, Unset):
            user_costs = self.user_costs.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if analysis_cost is not UNSET:
            field_dict["analysis_cost"] = analysis_cost
        if automation_cost is not UNSET:
            field_dict["automation_cost"] = automation_cost
        if edge_transcoder_cost is not UNSET:
            field_dict["edge_transcoder_cost"] = edge_transcoder_cost
        if external_storage_cost is not UNSET:
            field_dict["external_storage_cost"] = external_storage_cost
        if face_recognition_cost is not UNSET:
            field_dict["face_recognition_cost"] = face_recognition_cost
        if shield_cost is not UNSET:
            field_dict["shield_cost"] = shield_cost
        if storage_costs is not UNSET:
            field_dict["storage_costs"] = storage_costs
        if total_spend is not UNSET:
            field_dict["total_spend"] = total_spend
        if transcription_cost is not UNSET:
            field_dict["transcription_cost"] = transcription_cost
        if user_costs is not UNSET:
            field_dict["user_costs"] = user_costs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.paygo_costs_schema_storage_costs import (
            PaygoCostsSchemaStorageCosts,
        )
        from ..models.paygo_costs_schema_user_costs import PaygoCostsSchemaUserCosts

        d = dict(src_dict)
        analysis_cost = d.pop("analysis_cost", UNSET)

        automation_cost = d.pop("automation_cost", UNSET)

        edge_transcoder_cost = d.pop("edge_transcoder_cost", UNSET)

        external_storage_cost = d.pop("external_storage_cost", UNSET)

        face_recognition_cost = d.pop("face_recognition_cost", UNSET)

        shield_cost = d.pop("shield_cost", UNSET)

        _storage_costs = d.pop("storage_costs", UNSET)
        storage_costs: PaygoCostsSchemaStorageCosts | Unset
        if isinstance(_storage_costs, Unset):
            storage_costs = UNSET
        else:
            storage_costs = PaygoCostsSchemaStorageCosts.from_dict(_storage_costs)

        total_spend = d.pop("total_spend", UNSET)

        transcription_cost = d.pop("transcription_cost", UNSET)

        _user_costs = d.pop("user_costs", UNSET)
        user_costs: PaygoCostsSchemaUserCosts | Unset
        if isinstance(_user_costs, Unset):
            user_costs = UNSET
        else:
            user_costs = PaygoCostsSchemaUserCosts.from_dict(_user_costs)

        paygo_costs_schema = cls(
            analysis_cost=analysis_cost,
            automation_cost=automation_cost,
            edge_transcoder_cost=edge_transcoder_cost,
            external_storage_cost=external_storage_cost,
            face_recognition_cost=face_recognition_cost,
            shield_cost=shield_cost,
            storage_costs=storage_costs,
            total_spend=total_spend,
            transcription_cost=transcription_cost,
            user_costs=user_costs,
        )

        paygo_costs_schema.additional_properties = d
        return paygo_costs_schema

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
