from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="S3SettingsSchema")


@_attrs_define
class S3SettingsSchema:
    """
    Attributes:
        bucket (str):
        endpoint (str):
        path (str):
        region (str):
        access_group_id (None | Unset | UUID):
        access_key (str | Unset):
        acl_template_id (None | Unset | UUID):
        add_uuid_to_filenames (bool | Unset):
        aggregate_identical_files (bool | Unset):
        aggregate_ignore (list[str] | Unset):
        aggregate_only_on_same_storage (bool | Unset):
        delete (bool | Unset):
        enable_collection_directory_mapping (bool | Unset):
        filename_is_external_id (bool | Unset):
        folder_name_tags_metadata_field_name (str | Unset):
        folder_name_tags_metadata_view_id (None | Unset | UUID):
        glacier_restore_timeout (int | None | Unset): Keep restored assets online for this many days to allow them to be
            copied before going back to Glacier
        is_system (bool | Unset):
        metadata_conversion_url (str | Unset):
        metadata_conversion_url_headers (None | str | Unset):
        metadata_view_id (None | Unset | UUID):
        notification_sqs_url (str | Unset):
        preload_edge_jobs (int | None | Unset):
        presign_md5_checksum (bool | Unset):
        read (bool | Unset):
        root_collection_id (UUID | Unset):
        scan (bool | Unset):
        scan_directories (list[str] | Unset):
        scan_ignore (list[str] | Unset):
        secret_key (str | Unset):
        session_token (str | Unset):
        sidecar_metadata_required (bool | Unset):
        title_includes_extension (bool | Unset):
        transcode_ignore (list[str] | Unset):
        use_acceleration (bool | Unset):
        write (bool | Unset):
    """

    bucket: str
    endpoint: str
    path: str
    region: str
    access_group_id: None | Unset | UUID = UNSET
    access_key: str | Unset = UNSET
    acl_template_id: None | Unset | UUID = UNSET
    add_uuid_to_filenames: bool | Unset = UNSET
    aggregate_identical_files: bool | Unset = UNSET
    aggregate_ignore: list[str] | Unset = UNSET
    aggregate_only_on_same_storage: bool | Unset = UNSET
    delete: bool | Unset = UNSET
    enable_collection_directory_mapping: bool | Unset = UNSET
    filename_is_external_id: bool | Unset = UNSET
    folder_name_tags_metadata_field_name: str | Unset = UNSET
    folder_name_tags_metadata_view_id: None | Unset | UUID = UNSET
    glacier_restore_timeout: int | None | Unset = UNSET
    is_system: bool | Unset = UNSET
    metadata_conversion_url: str | Unset = UNSET
    metadata_conversion_url_headers: None | str | Unset = UNSET
    metadata_view_id: None | Unset | UUID = UNSET
    notification_sqs_url: str | Unset = UNSET
    preload_edge_jobs: int | None | Unset = UNSET
    presign_md5_checksum: bool | Unset = UNSET
    read: bool | Unset = UNSET
    root_collection_id: UUID | Unset = UNSET
    scan: bool | Unset = UNSET
    scan_directories: list[str] | Unset = UNSET
    scan_ignore: list[str] | Unset = UNSET
    secret_key: str | Unset = UNSET
    session_token: str | Unset = UNSET
    sidecar_metadata_required: bool | Unset = UNSET
    title_includes_extension: bool | Unset = UNSET
    transcode_ignore: list[str] | Unset = UNSET
    use_acceleration: bool | Unset = UNSET
    write: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bucket = self.bucket

        endpoint = self.endpoint

        path = self.path

        region = self.region

        access_group_id: None | str | Unset
        if isinstance(self.access_group_id, Unset):
            access_group_id = UNSET
        elif isinstance(self.access_group_id, UUID):
            access_group_id = str(self.access_group_id)
        else:
            access_group_id = self.access_group_id

        access_key = self.access_key

        acl_template_id: None | str | Unset
        if isinstance(self.acl_template_id, Unset):
            acl_template_id = UNSET
        elif isinstance(self.acl_template_id, UUID):
            acl_template_id = str(self.acl_template_id)
        else:
            acl_template_id = self.acl_template_id

        add_uuid_to_filenames = self.add_uuid_to_filenames

        aggregate_identical_files = self.aggregate_identical_files

        aggregate_ignore: list[str] | Unset = UNSET
        if not isinstance(self.aggregate_ignore, Unset):
            aggregate_ignore = self.aggregate_ignore

        aggregate_only_on_same_storage = self.aggregate_only_on_same_storage

        delete = self.delete

        enable_collection_directory_mapping = self.enable_collection_directory_mapping

        filename_is_external_id = self.filename_is_external_id

        folder_name_tags_metadata_field_name = self.folder_name_tags_metadata_field_name

        folder_name_tags_metadata_view_id: None | str | Unset
        if isinstance(self.folder_name_tags_metadata_view_id, Unset):
            folder_name_tags_metadata_view_id = UNSET
        elif isinstance(self.folder_name_tags_metadata_view_id, UUID):
            folder_name_tags_metadata_view_id = str(
                self.folder_name_tags_metadata_view_id
            )
        else:
            folder_name_tags_metadata_view_id = self.folder_name_tags_metadata_view_id

        glacier_restore_timeout: int | None | Unset
        if isinstance(self.glacier_restore_timeout, Unset):
            glacier_restore_timeout = UNSET
        else:
            glacier_restore_timeout = self.glacier_restore_timeout

        is_system = self.is_system

        metadata_conversion_url = self.metadata_conversion_url

        metadata_conversion_url_headers: None | str | Unset
        if isinstance(self.metadata_conversion_url_headers, Unset):
            metadata_conversion_url_headers = UNSET
        else:
            metadata_conversion_url_headers = self.metadata_conversion_url_headers

        metadata_view_id: None | str | Unset
        if isinstance(self.metadata_view_id, Unset):
            metadata_view_id = UNSET
        elif isinstance(self.metadata_view_id, UUID):
            metadata_view_id = str(self.metadata_view_id)
        else:
            metadata_view_id = self.metadata_view_id

        notification_sqs_url = self.notification_sqs_url

        preload_edge_jobs: int | None | Unset
        if isinstance(self.preload_edge_jobs, Unset):
            preload_edge_jobs = UNSET
        else:
            preload_edge_jobs = self.preload_edge_jobs

        presign_md5_checksum = self.presign_md5_checksum

        read = self.read

        root_collection_id: str | Unset = UNSET
        if not isinstance(self.root_collection_id, Unset):
            root_collection_id = str(self.root_collection_id)

        scan = self.scan

        scan_directories: list[str] | Unset = UNSET
        if not isinstance(self.scan_directories, Unset):
            scan_directories = self.scan_directories

        scan_ignore: list[str] | Unset = UNSET
        if not isinstance(self.scan_ignore, Unset):
            scan_ignore = self.scan_ignore

        secret_key = self.secret_key

        session_token = self.session_token

        sidecar_metadata_required = self.sidecar_metadata_required

        title_includes_extension = self.title_includes_extension

        transcode_ignore: list[str] | Unset = UNSET
        if not isinstance(self.transcode_ignore, Unset):
            transcode_ignore = self.transcode_ignore

        use_acceleration = self.use_acceleration

        write = self.write

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bucket": bucket,
                "endpoint": endpoint,
                "path": path,
                "region": region,
            }
        )
        if access_group_id is not UNSET:
            field_dict["access_group_id"] = access_group_id
        if access_key is not UNSET:
            field_dict["access_key"] = access_key
        if acl_template_id is not UNSET:
            field_dict["acl_template_id"] = acl_template_id
        if add_uuid_to_filenames is not UNSET:
            field_dict["add_uuid_to_filenames"] = add_uuid_to_filenames
        if aggregate_identical_files is not UNSET:
            field_dict["aggregate_identical_files"] = aggregate_identical_files
        if aggregate_ignore is not UNSET:
            field_dict["aggregate_ignore"] = aggregate_ignore
        if aggregate_only_on_same_storage is not UNSET:
            field_dict["aggregate_only_on_same_storage"] = (
                aggregate_only_on_same_storage
            )
        if delete is not UNSET:
            field_dict["delete"] = delete
        if enable_collection_directory_mapping is not UNSET:
            field_dict["enable_collection_directory_mapping"] = (
                enable_collection_directory_mapping
            )
        if filename_is_external_id is not UNSET:
            field_dict["filename_is_external_id"] = filename_is_external_id
        if folder_name_tags_metadata_field_name is not UNSET:
            field_dict["folder_name_tags_metadata_field_name"] = (
                folder_name_tags_metadata_field_name
            )
        if folder_name_tags_metadata_view_id is not UNSET:
            field_dict["folder_name_tags_metadata_view_id"] = (
                folder_name_tags_metadata_view_id
            )
        if glacier_restore_timeout is not UNSET:
            field_dict["glacier_restore_timeout"] = glacier_restore_timeout
        if is_system is not UNSET:
            field_dict["is_system"] = is_system
        if metadata_conversion_url is not UNSET:
            field_dict["metadata_conversion_url"] = metadata_conversion_url
        if metadata_conversion_url_headers is not UNSET:
            field_dict["metadata_conversion_url_headers"] = (
                metadata_conversion_url_headers
            )
        if metadata_view_id is not UNSET:
            field_dict["metadata_view_id"] = metadata_view_id
        if notification_sqs_url is not UNSET:
            field_dict["notification_sqs_url"] = notification_sqs_url
        if preload_edge_jobs is not UNSET:
            field_dict["preload_edge_jobs"] = preload_edge_jobs
        if presign_md5_checksum is not UNSET:
            field_dict["presign_md5_checksum"] = presign_md5_checksum
        if read is not UNSET:
            field_dict["read"] = read
        if root_collection_id is not UNSET:
            field_dict["root_collection_id"] = root_collection_id
        if scan is not UNSET:
            field_dict["scan"] = scan
        if scan_directories is not UNSET:
            field_dict["scan_directories"] = scan_directories
        if scan_ignore is not UNSET:
            field_dict["scan_ignore"] = scan_ignore
        if secret_key is not UNSET:
            field_dict["secret_key"] = secret_key
        if session_token is not UNSET:
            field_dict["session_token"] = session_token
        if sidecar_metadata_required is not UNSET:
            field_dict["sidecar_metadata_required"] = sidecar_metadata_required
        if title_includes_extension is not UNSET:
            field_dict["title_includes_extension"] = title_includes_extension
        if transcode_ignore is not UNSET:
            field_dict["transcode_ignore"] = transcode_ignore
        if use_acceleration is not UNSET:
            field_dict["use_acceleration"] = use_acceleration
        if write is not UNSET:
            field_dict["write"] = write

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bucket = d.pop("bucket")

        endpoint = d.pop("endpoint")

        path = d.pop("path")

        region = d.pop("region")

        def _parse_access_group_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                access_group_id_type_0 = UUID(data)

                return access_group_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        access_group_id = _parse_access_group_id(d.pop("access_group_id", UNSET))

        access_key = d.pop("access_key", UNSET)

        def _parse_acl_template_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                acl_template_id_type_0 = UUID(data)

                return acl_template_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        acl_template_id = _parse_acl_template_id(d.pop("acl_template_id", UNSET))

        add_uuid_to_filenames = d.pop("add_uuid_to_filenames", UNSET)

        aggregate_identical_files = d.pop("aggregate_identical_files", UNSET)

        aggregate_ignore = cast(list[str], d.pop("aggregate_ignore", UNSET))

        aggregate_only_on_same_storage = d.pop("aggregate_only_on_same_storage", UNSET)

        delete = d.pop("delete", UNSET)

        enable_collection_directory_mapping = d.pop(
            "enable_collection_directory_mapping", UNSET
        )

        filename_is_external_id = d.pop("filename_is_external_id", UNSET)

        folder_name_tags_metadata_field_name = d.pop(
            "folder_name_tags_metadata_field_name", UNSET
        )

        def _parse_folder_name_tags_metadata_view_id(
            data: object,
        ) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                folder_name_tags_metadata_view_id_type_0 = UUID(data)

                return folder_name_tags_metadata_view_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        folder_name_tags_metadata_view_id = _parse_folder_name_tags_metadata_view_id(
            d.pop("folder_name_tags_metadata_view_id", UNSET)
        )

        def _parse_glacier_restore_timeout(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        glacier_restore_timeout = _parse_glacier_restore_timeout(
            d.pop("glacier_restore_timeout", UNSET)
        )

        is_system = d.pop("is_system", UNSET)

        metadata_conversion_url = d.pop("metadata_conversion_url", UNSET)

        def _parse_metadata_conversion_url_headers(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        metadata_conversion_url_headers = _parse_metadata_conversion_url_headers(
            d.pop("metadata_conversion_url_headers", UNSET)
        )

        def _parse_metadata_view_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                metadata_view_id_type_0 = UUID(data)

                return metadata_view_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        metadata_view_id = _parse_metadata_view_id(d.pop("metadata_view_id", UNSET))

        notification_sqs_url = d.pop("notification_sqs_url", UNSET)

        def _parse_preload_edge_jobs(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        preload_edge_jobs = _parse_preload_edge_jobs(d.pop("preload_edge_jobs", UNSET))

        presign_md5_checksum = d.pop("presign_md5_checksum", UNSET)

        read = d.pop("read", UNSET)

        _root_collection_id = d.pop("root_collection_id", UNSET)
        root_collection_id: UUID | Unset
        if isinstance(_root_collection_id, Unset):
            root_collection_id = UNSET
        else:
            root_collection_id = UUID(_root_collection_id)

        scan = d.pop("scan", UNSET)

        scan_directories = cast(list[str], d.pop("scan_directories", UNSET))

        scan_ignore = cast(list[str], d.pop("scan_ignore", UNSET))

        secret_key = d.pop("secret_key", UNSET)

        session_token = d.pop("session_token", UNSET)

        sidecar_metadata_required = d.pop("sidecar_metadata_required", UNSET)

        title_includes_extension = d.pop("title_includes_extension", UNSET)

        transcode_ignore = cast(list[str], d.pop("transcode_ignore", UNSET))

        use_acceleration = d.pop("use_acceleration", UNSET)

        write = d.pop("write", UNSET)

        s3_settings_schema = cls(
            bucket=bucket,
            endpoint=endpoint,
            path=path,
            region=region,
            access_group_id=access_group_id,
            access_key=access_key,
            acl_template_id=acl_template_id,
            add_uuid_to_filenames=add_uuid_to_filenames,
            aggregate_identical_files=aggregate_identical_files,
            aggregate_ignore=aggregate_ignore,
            aggregate_only_on_same_storage=aggregate_only_on_same_storage,
            delete=delete,
            enable_collection_directory_mapping=enable_collection_directory_mapping,
            filename_is_external_id=filename_is_external_id,
            folder_name_tags_metadata_field_name=folder_name_tags_metadata_field_name,
            folder_name_tags_metadata_view_id=folder_name_tags_metadata_view_id,
            glacier_restore_timeout=glacier_restore_timeout,
            is_system=is_system,
            metadata_conversion_url=metadata_conversion_url,
            metadata_conversion_url_headers=metadata_conversion_url_headers,
            metadata_view_id=metadata_view_id,
            notification_sqs_url=notification_sqs_url,
            preload_edge_jobs=preload_edge_jobs,
            presign_md5_checksum=presign_md5_checksum,
            read=read,
            root_collection_id=root_collection_id,
            scan=scan,
            scan_directories=scan_directories,
            scan_ignore=scan_ignore,
            secret_key=secret_key,
            session_token=session_token,
            sidecar_metadata_required=sidecar_metadata_required,
            title_includes_extension=title_includes_extension,
            transcode_ignore=transcode_ignore,
            use_acceleration=use_acceleration,
            write=write,
        )

        s3_settings_schema.additional_properties = d
        return s3_settings_schema

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
