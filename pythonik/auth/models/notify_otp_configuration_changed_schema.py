from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.notify_otp_configuration_changed_schema_message_type import (
    NotifyOTPConfigurationChangedSchemaMessageType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notify_otp_configuration_changed_schema_metadata_type_0 import (
        NotifyOTPConfigurationChangedSchemaMetadataType0,
    )


T = TypeVar("T", bound="NotifyOTPConfigurationChangedSchema")


@_attrs_define
class NotifyOTPConfigurationChangedSchema:
    """
    Attributes:
        email (str):
        message_type (NotifyOTPConfigurationChangedSchemaMessageType):
        metadata (None | NotifyOTPConfigurationChangedSchemaMetadataType0 | Unset):
    """

    email: str
    message_type: NotifyOTPConfigurationChangedSchemaMessageType
    metadata: None | NotifyOTPConfigurationChangedSchemaMetadataType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.notify_otp_configuration_changed_schema_metadata_type_0 import (
            NotifyOTPConfigurationChangedSchemaMetadataType0,
        )

        email = self.email

        message_type = self.message_type.value

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(
            self.metadata, NotifyOTPConfigurationChangedSchemaMetadataType0
        ):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "message_type": message_type,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.notify_otp_configuration_changed_schema_metadata_type_0 import (
            NotifyOTPConfigurationChangedSchemaMetadataType0,
        )

        d = dict(src_dict)
        email = d.pop("email")

        message_type = NotifyOTPConfigurationChangedSchemaMessageType(
            d.pop("message_type")
        )

        def _parse_metadata(
            data: object,
        ) -> None | NotifyOTPConfigurationChangedSchemaMetadataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = (
                    NotifyOTPConfigurationChangedSchemaMetadataType0.from_dict(data)
                )

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | NotifyOTPConfigurationChangedSchemaMetadataType0 | Unset, data
            )

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        notify_otp_configuration_changed_schema = cls(
            email=email,
            message_type=message_type,
            metadata=metadata,
        )

        notify_otp_configuration_changed_schema.additional_properties = d
        return notify_otp_configuration_changed_schema

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
