from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.edge_transcode_endpoint_schema import EdgeTranscodeEndpointSchema


T = TypeVar("T", bound="EdgeTranscodeInputSchema")


@_attrs_define
class EdgeTranscodeInputSchema:
    """
    Attributes:
        endpoint (EdgeTranscodeEndpointSchema):
        asset_id (str | Unset):
        closed_captions (bool | Unset):
        directory_path (str | Unset):
        file_id (str | Unset):
        file_set_id (None | str | Unset):
        format_id (None | str | Unset):
        language (str | Unset):
        original_asset_id (None | str | Unset):
        original_name (str | Unset):
        proxy_id (None | str | Unset):
        storage_id (str | Unset):
    """

    endpoint: EdgeTranscodeEndpointSchema
    asset_id: str | Unset = UNSET
    closed_captions: bool | Unset = UNSET
    directory_path: str | Unset = UNSET
    file_id: str | Unset = UNSET
    file_set_id: None | str | Unset = UNSET
    format_id: None | str | Unset = UNSET
    language: str | Unset = UNSET
    original_asset_id: None | str | Unset = UNSET
    original_name: str | Unset = UNSET
    proxy_id: None | str | Unset = UNSET
    storage_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        endpoint = self.endpoint.to_dict()

        asset_id = self.asset_id

        closed_captions = self.closed_captions

        directory_path = self.directory_path

        file_id = self.file_id

        file_set_id: None | str | Unset
        if isinstance(self.file_set_id, Unset):
            file_set_id = UNSET
        else:
            file_set_id = self.file_set_id

        format_id: None | str | Unset
        if isinstance(self.format_id, Unset):
            format_id = UNSET
        else:
            format_id = self.format_id

        language = self.language

        original_asset_id: None | str | Unset
        if isinstance(self.original_asset_id, Unset):
            original_asset_id = UNSET
        else:
            original_asset_id = self.original_asset_id

        original_name = self.original_name

        proxy_id: None | str | Unset
        if isinstance(self.proxy_id, Unset):
            proxy_id = UNSET
        else:
            proxy_id = self.proxy_id

        storage_id = self.storage_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "endpoint": endpoint,
            }
        )
        if asset_id is not UNSET:
            field_dict["asset_id"] = asset_id
        if closed_captions is not UNSET:
            field_dict["closed_captions"] = closed_captions
        if directory_path is not UNSET:
            field_dict["directory_path"] = directory_path
        if file_id is not UNSET:
            field_dict["file_id"] = file_id
        if file_set_id is not UNSET:
            field_dict["file_set_id"] = file_set_id
        if format_id is not UNSET:
            field_dict["format_id"] = format_id
        if language is not UNSET:
            field_dict["language"] = language
        if original_asset_id is not UNSET:
            field_dict["original_asset_id"] = original_asset_id
        if original_name is not UNSET:
            field_dict["original_name"] = original_name
        if proxy_id is not UNSET:
            field_dict["proxy_id"] = proxy_id
        if storage_id is not UNSET:
            field_dict["storage_id"] = storage_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.edge_transcode_endpoint_schema import EdgeTranscodeEndpointSchema

        d = dict(src_dict)
        endpoint = EdgeTranscodeEndpointSchema.from_dict(d.pop("endpoint"))

        asset_id = d.pop("asset_id", UNSET)

        closed_captions = d.pop("closed_captions", UNSET)

        directory_path = d.pop("directory_path", UNSET)

        file_id = d.pop("file_id", UNSET)

        def _parse_file_set_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_set_id = _parse_file_set_id(d.pop("file_set_id", UNSET))

        def _parse_format_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        format_id = _parse_format_id(d.pop("format_id", UNSET))

        language = d.pop("language", UNSET)

        def _parse_original_asset_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        original_asset_id = _parse_original_asset_id(d.pop("original_asset_id", UNSET))

        original_name = d.pop("original_name", UNSET)

        def _parse_proxy_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        proxy_id = _parse_proxy_id(d.pop("proxy_id", UNSET))

        storage_id = d.pop("storage_id", UNSET)

        edge_transcode_input_schema = cls(
            endpoint=endpoint,
            asset_id=asset_id,
            closed_captions=closed_captions,
            directory_path=directory_path,
            file_id=file_id,
            file_set_id=file_set_id,
            format_id=format_id,
            language=language,
            original_asset_id=original_asset_id,
            original_name=original_name,
            proxy_id=proxy_id,
            storage_id=storage_id,
        )

        edge_transcode_input_schema.additional_properties = d
        return edge_transcode_input_schema

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
