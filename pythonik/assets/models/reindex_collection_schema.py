from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReindexCollectionSchema")


@_attrs_define
class ReindexCollectionSchema:
    """
    Attributes:
        realms (list[str] | None | Unset):
        sync_to_another_dc (bool | None | Unset):
    """

    realms: list[str] | None | Unset = UNSET
    sync_to_another_dc: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        realms: list[str] | None | Unset
        if isinstance(self.realms, Unset):
            realms = UNSET
        elif isinstance(self.realms, list):
            realms = self.realms

        else:
            realms = self.realms

        sync_to_another_dc: bool | None | Unset
        if isinstance(self.sync_to_another_dc, Unset):
            sync_to_another_dc = UNSET
        else:
            sync_to_another_dc = self.sync_to_another_dc

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if realms is not UNSET:
            field_dict["realms"] = realms
        if sync_to_another_dc is not UNSET:
            field_dict["sync_to_another_dc"] = sync_to_another_dc

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_realms(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                realms_type_0 = cast(list[str], data)

                return realms_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        realms = _parse_realms(d.pop("realms", UNSET))

        def _parse_sync_to_another_dc(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        sync_to_another_dc = _parse_sync_to_another_dc(
            d.pop("sync_to_another_dc", UNSET)
        )

        reindex_collection_schema = cls(
            realms=realms,
            sync_to_another_dc=sync_to_another_dc,
        )

        reindex_collection_schema.additional_properties = d
        return reindex_collection_schema

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
