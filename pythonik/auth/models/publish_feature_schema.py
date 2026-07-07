from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.publish_feature_schema_feature import PublishFeatureSchemaFeature

if TYPE_CHECKING:
    from ..models.publish_feature_parameters import PublishFeatureParameters


T = TypeVar("T", bound="PublishFeatureSchema")


@_attrs_define
class PublishFeatureSchema:
    """
    Attributes:
        feature (PublishFeatureSchemaFeature):  Default: PublishFeatureSchemaFeature.WM_PUBLISH_PANEL.
        parameters (PublishFeatureParameters):
    """

    parameters: PublishFeatureParameters
    feature: PublishFeatureSchemaFeature = PublishFeatureSchemaFeature.WM_PUBLISH_PANEL
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        feature = self.feature.value

        parameters = self.parameters.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "feature": feature,
                "parameters": parameters,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.publish_feature_parameters import PublishFeatureParameters

        d = dict(src_dict)
        feature = PublishFeatureSchemaFeature(d.pop("feature"))

        parameters = PublishFeatureParameters.from_dict(d.pop("parameters"))

        publish_feature_schema = cls(
            feature=feature,
            parameters=parameters,
        )

        publish_feature_schema.additional_properties = d
        return publish_feature_schema

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
