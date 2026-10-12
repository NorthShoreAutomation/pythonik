from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.scoring_stage import ScoringStage
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.scoring_method_params_type_0 import ScoringMethodParamsType0


T = TypeVar("T", bound="ScoringMethod")


@_attrs_define
class ScoringMethod:
    """One scoring/ranking method applied at one stage of the pipeline.

    Strengthens what used to be a pair of free-text fields into an ordered,
    typed record so the response can attest *exactly* how it ranked: the stage,
    the method (an enum value), the concrete model when the method is
    model-backed, and any tuning knobs (e.g. the RRF ``k``). Several may apply
    (e.g. an RRF fusion followed by a cross-encoder rerank), hence a list on
    :class:`ScoringDiagnostics`.

        Attributes:
            method (str):
            stage (ScoringStage): Which stage of the ranking pipeline a :class:`ScoringMethod` describes.
            model (None | str | Unset):
            params (None | ScoringMethodParamsType0 | Unset):
    """

    method: str
    stage: ScoringStage
    model: None | str | Unset = UNSET
    params: None | ScoringMethodParamsType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.scoring_method_params_type_0 import ScoringMethodParamsType0

        method = self.method

        stage = self.stage.value

        model: None | str | Unset
        if isinstance(self.model, Unset):
            model = UNSET
        else:
            model = self.model

        params: dict[str, Any] | None | Unset
        if isinstance(self.params, Unset):
            params = UNSET
        elif isinstance(self.params, ScoringMethodParamsType0):
            params = self.params.to_dict()
        else:
            params = self.params

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "method": method,
                "stage": stage,
            }
        )
        if model is not UNSET:
            field_dict["model"] = model
        if params is not UNSET:
            field_dict["params"] = params

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.scoring_method_params_type_0 import ScoringMethodParamsType0

        d = dict(src_dict)
        method = d.pop("method")

        stage = ScoringStage(d.pop("stage"))

        def _parse_model(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model = _parse_model(d.pop("model", UNSET))

        def _parse_params(data: object) -> None | ScoringMethodParamsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                params_type_0 = ScoringMethodParamsType0.from_dict(data)

                return params_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ScoringMethodParamsType0 | Unset, data)

        params = _parse_params(d.pop("params", UNSET))

        scoring_method = cls(
            method=method,
            stage=stage,
            model=model,
            params=params,
        )

        scoring_method.additional_properties = d
        return scoring_method

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
