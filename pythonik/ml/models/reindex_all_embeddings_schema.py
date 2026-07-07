from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReindexAllEmbeddingsSchema")


@_attrs_define
class ReindexAllEmbeddingsSchema:
    """
    Attributes:
        embedding_ids (list[UUID] | None | Unset):
        sync_to_another_dc (bool | Unset):
    """

    embedding_ids: list[UUID] | None | Unset = UNSET
    sync_to_another_dc: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        embedding_ids: list[str] | None | Unset
        if isinstance(self.embedding_ids, Unset):
            embedding_ids = UNSET
        elif isinstance(self.embedding_ids, list):
            embedding_ids = []
            for embedding_ids_type_0_item_data in self.embedding_ids:
                embedding_ids_type_0_item = str(embedding_ids_type_0_item_data)
                embedding_ids.append(embedding_ids_type_0_item)

        else:
            embedding_ids = self.embedding_ids

        sync_to_another_dc = self.sync_to_another_dc

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if embedding_ids is not UNSET:
            field_dict["embedding_ids"] = embedding_ids
        if sync_to_another_dc is not UNSET:
            field_dict["sync_to_another_dc"] = sync_to_another_dc

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_embedding_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                embedding_ids_type_0 = []
                _embedding_ids_type_0 = data
                for embedding_ids_type_0_item_data in _embedding_ids_type_0:
                    embedding_ids_type_0_item = UUID(embedding_ids_type_0_item_data)

                    embedding_ids_type_0.append(embedding_ids_type_0_item)

                return embedding_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        embedding_ids = _parse_embedding_ids(d.pop("embedding_ids", UNSET))

        sync_to_another_dc = d.pop("sync_to_another_dc", UNSET)

        reindex_all_embeddings_schema = cls(
            embedding_ids=embedding_ids,
            sync_to_another_dc=sync_to_another_dc,
        )

        reindex_all_embeddings_schema.additional_properties = d
        return reindex_all_embeddings_schema

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
