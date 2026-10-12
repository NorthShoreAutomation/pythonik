from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_response_errors_type_1 import ErrorResponseErrorsType1


T = TypeVar("T", bound="ErrorResponse")


@_attrs_define
class ErrorResponse:
    """Common iconik error envelope.

    ``errors`` is either a flat list of messages or a mapping of field name to
    its list of messages, matching the shapes returned across the v2 endpoints.

        Attributes:
            errors (ErrorResponseErrorsType1 | list[str] | None | Unset):  Example: ['Bad request: Invalid JSON'].
    """

    errors: ErrorResponseErrorsType1 | list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.error_response_errors_type_1 import ErrorResponseErrorsType1

        errors: dict[str, Any] | list[str] | None | Unset
        if isinstance(self.errors, Unset):
            errors = UNSET
        elif isinstance(self.errors, list):
            errors = self.errors

        elif isinstance(self.errors, ErrorResponseErrorsType1):
            errors = self.errors.to_dict()
        else:
            errors = self.errors

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error_response_errors_type_1 import ErrorResponseErrorsType1

        d = dict(src_dict)

        def _parse_errors(
            data: object,
        ) -> ErrorResponseErrorsType1 | list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                errors_type_0 = cast(list[str], data)

                return errors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                errors_type_1 = ErrorResponseErrorsType1.from_dict(data)

                return errors_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ErrorResponseErrorsType1 | list[str] | None | Unset, data)

        errors = _parse_errors(d.pop("errors", UNSET))

        error_response = cls(
            errors=errors,
        )

        error_response.additional_properties = d
        return error_response

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
