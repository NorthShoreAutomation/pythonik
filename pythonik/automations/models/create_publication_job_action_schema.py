from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_publication_job_action_schema_type import (
    CreatePublicationJobActionSchemaType,
)

if TYPE_CHECKING:
    from ..models.create_publication_job_parameters import (
        CreatePublicationJobParameters,
    )


T = TypeVar("T", bound="CreatePublicationJobActionSchema")


@_attrs_define
class CreatePublicationJobActionSchema:
    """
    Attributes:
        parameters (CreatePublicationJobParameters):
        type_ (CreatePublicationJobActionSchemaType):  Default:
            CreatePublicationJobActionSchemaType.CREATE_PUBLICATION_JOB.
    """

    parameters: CreatePublicationJobParameters
    type_: CreatePublicationJobActionSchemaType = (
        CreatePublicationJobActionSchemaType.CREATE_PUBLICATION_JOB
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parameters = self.parameters.to_dict()

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "parameters": parameters,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_publication_job_parameters import (
            CreatePublicationJobParameters,
        )

        d = dict(src_dict)
        parameters = CreatePublicationJobParameters.from_dict(d.pop("parameters"))

        type_ = CreatePublicationJobActionSchemaType(d.pop("type"))

        create_publication_job_action_schema = cls(
            parameters=parameters,
            type_=type_,
        )

        create_publication_job_action_schema.additional_properties = d
        return create_publication_job_action_schema

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
