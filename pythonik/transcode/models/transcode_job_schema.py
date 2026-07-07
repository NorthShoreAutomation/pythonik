from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.output_endpoint_schema import OutputEndpointSchema


T = TypeVar("T", bound="TranscodeJobSchema")


@_attrs_define
class TranscodeJobSchema:
    """
    Attributes:
        output_endpoint (OutputEndpointSchema):
        height (int | Unset):
        id (str | Unset):
        width (int | Unset):
    """

    output_endpoint: OutputEndpointSchema
    height: int | Unset = UNSET
    id: str | Unset = UNSET
    width: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        output_endpoint = self.output_endpoint.to_dict()

        height = self.height

        id = self.id

        width = self.width

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "output_endpoint": output_endpoint,
            }
        )
        if height is not UNSET:
            field_dict["height"] = height
        if id is not UNSET:
            field_dict["id"] = id
        if width is not UNSET:
            field_dict["width"] = width

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_endpoint_schema import OutputEndpointSchema

        d = dict(src_dict)
        output_endpoint = OutputEndpointSchema.from_dict(d.pop("output_endpoint"))

        height = d.pop("height", UNSET)

        id = d.pop("id", UNSET)

        width = d.pop("width", UNSET)

        transcode_job_schema = cls(
            output_endpoint=output_endpoint,
            height=height,
            id=id,
            width=width,
        )

        transcode_job_schema.additional_properties = d
        return transcode_job_schema

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
