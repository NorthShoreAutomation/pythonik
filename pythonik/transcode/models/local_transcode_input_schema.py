from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.endpoint_schema import EndpointSchema


T = TypeVar("T", bound="LocalTranscodeInputSchema")


@_attrs_define
class LocalTranscodeInputSchema:
    """
    Attributes:
        asset_id (str):
        directory_path (str):
        endpoint (EndpointSchema):
        file_id (str):
        file_set_id (str):
        filename (str):
        format_id (str):
        size (int):
        storage_id (str):
        version_id (str):
        checksum (None | str | Unset):
        closed_captions (bool | None | Unset):
        collection_id (None | str | Unset):
        component_ids (list[str] | None | Unset):
        engine (None | str | Unset):
        language (None | str | Unset):
        original_asset_id (None | str | Unset):
        original_name (None | str | Unset):
        proxy_id (None | str | Unset):
        update_proxy_mediainfo (bool | None | Unset):
    """

    asset_id: str
    directory_path: str
    endpoint: EndpointSchema
    file_id: str
    file_set_id: str
    filename: str
    format_id: str
    size: int
    storage_id: str
    version_id: str
    checksum: None | str | Unset = UNSET
    closed_captions: bool | None | Unset = UNSET
    collection_id: None | str | Unset = UNSET
    component_ids: list[str] | None | Unset = UNSET
    engine: None | str | Unset = UNSET
    language: None | str | Unset = UNSET
    original_asset_id: None | str | Unset = UNSET
    original_name: None | str | Unset = UNSET
    proxy_id: None | str | Unset = UNSET
    update_proxy_mediainfo: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_id = self.asset_id

        directory_path = self.directory_path

        endpoint = self.endpoint.to_dict()

        file_id = self.file_id

        file_set_id = self.file_set_id

        filename = self.filename

        format_id = self.format_id

        size = self.size

        storage_id = self.storage_id

        version_id = self.version_id

        checksum: None | str | Unset
        if isinstance(self.checksum, Unset):
            checksum = UNSET
        else:
            checksum = self.checksum

        closed_captions: bool | None | Unset
        if isinstance(self.closed_captions, Unset):
            closed_captions = UNSET
        else:
            closed_captions = self.closed_captions

        collection_id: None | str | Unset
        if isinstance(self.collection_id, Unset):
            collection_id = UNSET
        else:
            collection_id = self.collection_id

        component_ids: list[str] | None | Unset
        if isinstance(self.component_ids, Unset):
            component_ids = UNSET
        elif isinstance(self.component_ids, list):
            component_ids = self.component_ids

        else:
            component_ids = self.component_ids

        engine: None | str | Unset
        if isinstance(self.engine, Unset):
            engine = UNSET
        else:
            engine = self.engine

        language: None | str | Unset
        if isinstance(self.language, Unset):
            language = UNSET
        else:
            language = self.language

        original_asset_id: None | str | Unset
        if isinstance(self.original_asset_id, Unset):
            original_asset_id = UNSET
        else:
            original_asset_id = self.original_asset_id

        original_name: None | str | Unset
        if isinstance(self.original_name, Unset):
            original_name = UNSET
        else:
            original_name = self.original_name

        proxy_id: None | str | Unset
        if isinstance(self.proxy_id, Unset):
            proxy_id = UNSET
        else:
            proxy_id = self.proxy_id

        update_proxy_mediainfo: bool | None | Unset
        if isinstance(self.update_proxy_mediainfo, Unset):
            update_proxy_mediainfo = UNSET
        else:
            update_proxy_mediainfo = self.update_proxy_mediainfo

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "asset_id": asset_id,
                "directory_path": directory_path,
                "endpoint": endpoint,
                "file_id": file_id,
                "file_set_id": file_set_id,
                "filename": filename,
                "format_id": format_id,
                "size": size,
                "storage_id": storage_id,
                "version_id": version_id,
            }
        )
        if checksum is not UNSET:
            field_dict["checksum"] = checksum
        if closed_captions is not UNSET:
            field_dict["closed_captions"] = closed_captions
        if collection_id is not UNSET:
            field_dict["collection_id"] = collection_id
        if component_ids is not UNSET:
            field_dict["component_ids"] = component_ids
        if engine is not UNSET:
            field_dict["engine"] = engine
        if language is not UNSET:
            field_dict["language"] = language
        if original_asset_id is not UNSET:
            field_dict["original_asset_id"] = original_asset_id
        if original_name is not UNSET:
            field_dict["original_name"] = original_name
        if proxy_id is not UNSET:
            field_dict["proxy_id"] = proxy_id
        if update_proxy_mediainfo is not UNSET:
            field_dict["update_proxy_mediainfo"] = update_proxy_mediainfo

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.endpoint_schema import EndpointSchema

        d = dict(src_dict)
        asset_id = d.pop("asset_id")

        directory_path = d.pop("directory_path")

        endpoint = EndpointSchema.from_dict(d.pop("endpoint"))

        file_id = d.pop("file_id")

        file_set_id = d.pop("file_set_id")

        filename = d.pop("filename")

        format_id = d.pop("format_id")

        size = d.pop("size")

        storage_id = d.pop("storage_id")

        version_id = d.pop("version_id")

        def _parse_checksum(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        checksum = _parse_checksum(d.pop("checksum", UNSET))

        def _parse_closed_captions(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        closed_captions = _parse_closed_captions(d.pop("closed_captions", UNSET))

        def _parse_collection_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        collection_id = _parse_collection_id(d.pop("collection_id", UNSET))

        def _parse_component_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                component_ids_type_0 = cast(list[str], data)

                return component_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        component_ids = _parse_component_ids(d.pop("component_ids", UNSET))

        def _parse_engine(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        engine = _parse_engine(d.pop("engine", UNSET))

        def _parse_language(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        language = _parse_language(d.pop("language", UNSET))

        def _parse_original_asset_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        original_asset_id = _parse_original_asset_id(d.pop("original_asset_id", UNSET))

        def _parse_original_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        original_name = _parse_original_name(d.pop("original_name", UNSET))

        def _parse_proxy_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        proxy_id = _parse_proxy_id(d.pop("proxy_id", UNSET))

        def _parse_update_proxy_mediainfo(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        update_proxy_mediainfo = _parse_update_proxy_mediainfo(
            d.pop("update_proxy_mediainfo", UNSET)
        )

        local_transcode_input_schema = cls(
            asset_id=asset_id,
            directory_path=directory_path,
            endpoint=endpoint,
            file_id=file_id,
            file_set_id=file_set_id,
            filename=filename,
            format_id=format_id,
            size=size,
            storage_id=storage_id,
            version_id=version_id,
            checksum=checksum,
            closed_captions=closed_captions,
            collection_id=collection_id,
            component_ids=component_ids,
            engine=engine,
            language=language,
            original_asset_id=original_asset_id,
            original_name=original_name,
            proxy_id=proxy_id,
            update_proxy_mediainfo=update_proxy_mediainfo,
        )

        local_transcode_input_schema.additional_properties = d
        return local_transcode_input_schema

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
