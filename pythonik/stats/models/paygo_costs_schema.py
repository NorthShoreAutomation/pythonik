from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.paygo_costs_schema_storage_costs_type_0 import (
        PaygoCostsSchemaStorageCostsType0,
    )
    from ..models.paygo_costs_schema_user_costs_type_0 import (
        PaygoCostsSchemaUserCostsType0,
    )


T = TypeVar("T", bound="PaygoCostsSchema")


@_attrs_define
class PaygoCostsSchema:
    """
    Attributes:
        analysis_cost (float | None | Unset):
        automation_cost (float | None | Unset):
        edge_transcoder_cost (float | None | Unset):
        external_storage_cost (float | None | Unset):
        face_recognition_cost (float | None | Unset):
        shield_cost (float | None | Unset):
        storage_costs (None | PaygoCostsSchemaStorageCostsType0 | Unset):
        total_spend (float | None | Unset):
        transcription_cost (float | None | Unset):
        user_costs (None | PaygoCostsSchemaUserCostsType0 | Unset):
    """

    analysis_cost: float | None | Unset = UNSET
    automation_cost: float | None | Unset = UNSET
    edge_transcoder_cost: float | None | Unset = UNSET
    external_storage_cost: float | None | Unset = UNSET
    face_recognition_cost: float | None | Unset = UNSET
    shield_cost: float | None | Unset = UNSET
    storage_costs: None | PaygoCostsSchemaStorageCostsType0 | Unset = UNSET
    total_spend: float | None | Unset = UNSET
    transcription_cost: float | None | Unset = UNSET
    user_costs: None | PaygoCostsSchemaUserCostsType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.paygo_costs_schema_storage_costs_type_0 import (
            PaygoCostsSchemaStorageCostsType0,
        )
        from ..models.paygo_costs_schema_user_costs_type_0 import (
            PaygoCostsSchemaUserCostsType0,
        )

        analysis_cost: float | None | Unset
        if isinstance(self.analysis_cost, Unset):
            analysis_cost = UNSET
        else:
            analysis_cost = self.analysis_cost

        automation_cost: float | None | Unset
        if isinstance(self.automation_cost, Unset):
            automation_cost = UNSET
        else:
            automation_cost = self.automation_cost

        edge_transcoder_cost: float | None | Unset
        if isinstance(self.edge_transcoder_cost, Unset):
            edge_transcoder_cost = UNSET
        else:
            edge_transcoder_cost = self.edge_transcoder_cost

        external_storage_cost: float | None | Unset
        if isinstance(self.external_storage_cost, Unset):
            external_storage_cost = UNSET
        else:
            external_storage_cost = self.external_storage_cost

        face_recognition_cost: float | None | Unset
        if isinstance(self.face_recognition_cost, Unset):
            face_recognition_cost = UNSET
        else:
            face_recognition_cost = self.face_recognition_cost

        shield_cost: float | None | Unset
        if isinstance(self.shield_cost, Unset):
            shield_cost = UNSET
        else:
            shield_cost = self.shield_cost

        storage_costs: dict[str, Any] | None | Unset
        if isinstance(self.storage_costs, Unset):
            storage_costs = UNSET
        elif isinstance(self.storage_costs, PaygoCostsSchemaStorageCostsType0):
            storage_costs = self.storage_costs.to_dict()
        else:
            storage_costs = self.storage_costs

        total_spend: float | None | Unset
        if isinstance(self.total_spend, Unset):
            total_spend = UNSET
        else:
            total_spend = self.total_spend

        transcription_cost: float | None | Unset
        if isinstance(self.transcription_cost, Unset):
            transcription_cost = UNSET
        else:
            transcription_cost = self.transcription_cost

        user_costs: dict[str, Any] | None | Unset
        if isinstance(self.user_costs, Unset):
            user_costs = UNSET
        elif isinstance(self.user_costs, PaygoCostsSchemaUserCostsType0):
            user_costs = self.user_costs.to_dict()
        else:
            user_costs = self.user_costs

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
        from ..models.paygo_costs_schema_storage_costs_type_0 import (
            PaygoCostsSchemaStorageCostsType0,
        )
        from ..models.paygo_costs_schema_user_costs_type_0 import (
            PaygoCostsSchemaUserCostsType0,
        )

        d = dict(src_dict)

        def _parse_analysis_cost(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        analysis_cost = _parse_analysis_cost(d.pop("analysis_cost", UNSET))

        def _parse_automation_cost(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        automation_cost = _parse_automation_cost(d.pop("automation_cost", UNSET))

        def _parse_edge_transcoder_cost(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        edge_transcoder_cost = _parse_edge_transcoder_cost(
            d.pop("edge_transcoder_cost", UNSET)
        )

        def _parse_external_storage_cost(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        external_storage_cost = _parse_external_storage_cost(
            d.pop("external_storage_cost", UNSET)
        )

        def _parse_face_recognition_cost(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        face_recognition_cost = _parse_face_recognition_cost(
            d.pop("face_recognition_cost", UNSET)
        )

        def _parse_shield_cost(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shield_cost = _parse_shield_cost(d.pop("shield_cost", UNSET))

        def _parse_storage_costs(
            data: object,
        ) -> None | PaygoCostsSchemaStorageCostsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                storage_costs_type_0 = PaygoCostsSchemaStorageCostsType0.from_dict(data)

                return storage_costs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PaygoCostsSchemaStorageCostsType0 | Unset, data)

        storage_costs = _parse_storage_costs(d.pop("storage_costs", UNSET))

        def _parse_total_spend(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        total_spend = _parse_total_spend(d.pop("total_spend", UNSET))

        def _parse_transcription_cost(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        transcription_cost = _parse_transcription_cost(
            d.pop("transcription_cost", UNSET)
        )

        def _parse_user_costs(
            data: object,
        ) -> None | PaygoCostsSchemaUserCostsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                user_costs_type_0 = PaygoCostsSchemaUserCostsType0.from_dict(data)

                return user_costs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PaygoCostsSchemaUserCostsType0 | Unset, data)

        user_costs = _parse_user_costs(d.pop("user_costs", UNSET))

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
