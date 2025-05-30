from urllib.parse import urlparse
from xml.dom.minidom import parseString
from functools import wraps
import warnings
from typing import Union, Dict, Any, Optional, Literal

import requests

from pythonik.constants import (
    GCS_KEYFRAME_LOCATION_KEY,
    GCS_UPLOADID_KEY,
    S3_UPLOADID_KEY,
)
from pythonik.exceptions import UnexpectedStorageMethodForProxy
from pythonik.models.base import Response, StorageMethod, PaginatedResponse
from pythonik.models.files.file import (
    File,
    FileSetsFilesResponse,
    Files,
    FileSet,
    FileSets,
    FileCreate,
    FileSetCreate,
    S3MultipartUploadResponse,
)
from pythonik.models.files.keyframe import (
    Keyframe,
    Keyframes,
    GCSKeyframeUploadResponse,
)
from pythonik.models.files.proxy import Proxies, Proxy
from pythonik.specs.base import Spec, PythonikResponse
from pythonik.models.files.storage import Storage, Storages
from pythonik.models.files.format import Component, Formats, Format, FormatCreate

GET_ASSET_PROXY_PATH = "assets/{}/proxies/{}/"
GET_ASSET_PROXIES_PATH = "assets/{}/proxies/"
GET_ASSET_PROXIES_MULTIPART_URL_PATH = GET_ASSET_PROXY_PATH + "multipart_url/part/"
GET_ASSET_PROXIES_MULTIPART_COMPLETE_URL_PATH = GET_ASSET_PROXY_PATH + "multipart_url/"
GET_ASSETS_FORMATS_PATH = "assets/{}/formats/"
GET_ASSETS_FORMAT_PATH = "assets/{}/formats/{}/"
GET_ASSETS_FORMAT_COMPONENTS_PATH = "assets/{}/formats/{}/components"
GET_ASSETS_FILES_PATH = "assets/{}/files/"
GET_ASSETS_FILE_SETS_PATH = "assets/{}/file_sets/"
GET_ASSETS_FILE_SET_FILES_PATH = "assets/{}/file_sets/{}/files/"
GET_STORAGE_PATH = "storages/{}/"
GET_STORAGES_PATH = "storages/"
GET_ASSET_KEYFRAME = "assets/{}/keyframes/{}/"
GET_ASSET_KEYFRAMES = "assets/{}/keyframes/"
GET_ASSETS_FILE_PATH = "assets/{}/files/{}/"
DELETE_ASSETS_FILE_SET_PATH = "assets/{}/file_sets/{}/"
DELETE_ASSETS_FILE_PATH = "assets/{}/files/{}/"
GET_ASSETS_VERSION_FILE_SETS_PATH = "assets/{}/versions/{}/file_sets/"
GET_ASSETS_VERSION_FILES_PATH = "assets/{}/versions/{}/files/"
GET_ASSETS_VERSION_FORMATS_PATH = "assets/{}/versions/{}/formats/"


class FilesSpec(Spec):
    server = "API/files/"

    def create_asset_format_component(
        self,
        asset_id: str,
        format_id: str,
        body: Union[Component, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Create a new format component

        Args:
            asset_id: ID of the asset
            format_id: ID for the format
            body: Component creation parameters, either as Component model or dict
            exclude_defaults: Whether to exclude default values when dumping Pydantic models
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=Formats)

        Required roles:
            - can_write_formats

        Raises:
            400 Bad request
            401 Token is invalid
            404 Formats for this asset don't exist
        """
        json_data = self._prepare_model_data(body, exclude_defaults=exclude_defaults)
        response = self._post(
            GET_ASSETS_FORMAT_COMPONENTS_PATH.format(asset_id, format_id),
            json=json_data,
            **kwargs,
        )
        return self.parse_response(response, Formats)

    def delete_asset_file(self, asset_id: str, file_id: str, **kwargs) -> Response:
        """Delete a specific file from an asset
        
        Args:
            asset_id: The ID of the asset
            file_id: The ID of the file to delete
            **kwargs: Additional kwargs to pass to the request
            
        Returns:
            Response with no data model
        """
        response = self._delete(DELETE_ASSETS_FILE_PATH.format(asset_id, file_id), **kwargs)
        return self.parse_response(response, model=None)

    def delete_asset_file_set(
        self, asset_id: str, file_set_id: str, keep_source: bool = False, **kwargs
    ) -> Response:
        """Delete asset's file set, file entries, and actual files
        
        Args:
            asset_id: The ID of the asset
            file_set_id: The ID of the file set to delete
            keep_source: If true, keep source objects
            
        Returns:
            Response with FileSet model if status code is 200 (file set marked as deleted)
            Response with no data model if status code is 204 (immediate deletion)
        """
        params = {"keep_source": keep_source} if keep_source else None
        response = self._delete(
            DELETE_ASSETS_FILE_SET_PATH.format(asset_id, file_set_id),
            params=params,
            **kwargs
        )
        
        # If status is 204, return response with no model
        if response.status_code == 204:
            return self.parse_response(response, model=None)
            
        # If status is possibly 200, return response with FileSet model
        return self.parse_response(response, FileSet)

    def delete_asset_keyframe(self, asset_id: str, keyframe_id: str, **kwargs):
        response = self._delete(GET_ASSET_KEYFRAME.format(asset_id, keyframe_id), **kwargs)
        return self.parse_response(response, model=None)


    def get_asset_file(self, asset_id: str, file_id: str, **kwargs) -> Response:
        """Get metadata for a specific file associated with an asset
        
        Args:
            asset_id: The ID of the asset
            file_id: The ID of the file to retrieve
            **kwargs: Additional arguments to pass to the request
            
        Returns:
            Response with File model
        """
        resp = self._get(GET_ASSETS_FILE_PATH.format(asset_id, file_id), **kwargs)
        return self.parse_response(resp, File)

    def get_asset_file_set_files(self, asset_id: str, file_sets_id: str, **kwargs) -> Response:
        """
        Retrieve files for a specific file set
        """
        response = self._get(GET_ASSETS_FILE_SET_FILES_PATH.format(asset_id, file_sets_id), **kwargs)
        return self.parse_response(response, FileSetsFilesResponse)

    def get_asset_keyframe(self, asset_id: str, keyframe_id: str, **kwargs) -> Response:
        """Get a specific keyframe for an asset
        
        Args:
            asset_id: The ID of the asset
            keyframe_id: The ID of the keyframe to retrieve
            
        Returns:
            Response with Keyframe model
        """
        response = self._get(GET_ASSET_KEYFRAME.format(asset_id, keyframe_id), **kwargs)
        return self.parse_response(response, Keyframe)

    def get_asset_keyframes(self, asset_id: str, **kwargs) -> Keyframes:
        """Get all keyframes for an asset
        
        Args:
            asset_id: The ID of the asset
            
        Returns:
            Response containing list of Keyframes
        """
        response = self._get(GET_ASSET_KEYFRAMES.format(asset_id), **kwargs)
        return self.parse_response(response, Keyframes)

    def create_asset_keyframe(
        self, asset_id: str, body: Union[Keyframe, Dict[str, Any]], exclude_defaults: bool = True, **kwargs
    ) -> Response:
        """Create a new keyframe for an asset
        
        Args:
            asset_id: The ID of the asset
            body: Keyframe object containing the keyframe data, either as Keyframe model or dict
            exclude_defaults: Whether to exclude default values when dumping Pydantic models
            **kwargs: Additional arguments to pass to the request
            
        Returns:
            Response with created Keyframe model
        """
        json_data = self._prepare_model_data(body, exclude_defaults=exclude_defaults)
        response = self._post(
            GET_ASSET_KEYFRAMES.format(asset_id),
            json=json_data,
            **kwargs,
        )
        return self.parse_response(response, Keyframe)

    def get_asset_proxy(self, asset_id: str, proxy_id: str, **kwargs) -> Response:
        """Get asset's proxy
        Returns: Response(model=Proxy)
        """

        resp = self._get(GET_ASSET_PROXY_PATH.format(asset_id, proxy_id), **kwargs)

        return self.parse_response(resp, Proxy)

    def update_asset_proxy(
        self, asset_id: str, proxy_id: str, body: Union[Proxy, Dict[str, Any]], exclude_defaults: bool = True, **kwargs
    ) -> Response:
        """
        Update asset's proxy
        """
        json_data = self._prepare_model_data(body, exclude_defaults=exclude_defaults)
        response = self._patch(
            GET_ASSET_PROXY_PATH.format(asset_id, proxy_id),
            json=json_data,
            **kwargs,
        )
        return self.parse_response(response, Proxy)

    def create_asset_proxy(
        self, asset_id: str, body: Union[Proxy, Dict[str, Any]], exclude_defaults: bool = True, **kwargs
    ) -> Response:
        """
        Create proxy and associate to asset
        Returns: Response(model=Proxy)
        """
        json_data = self._prepare_model_data(body, exclude_defaults=exclude_defaults)
        response = self._post(
            GET_ASSET_PROXIES_PATH.format(asset_id),
            json=json_data,
            **kwargs,
        )
        return self.parse_response(response, Proxy)

    def partial_update_keyframe(
        self,
        asset_id: str,
        keyframe_id: str,
        body: Union[Keyframe, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """Partially update an asset keyframe using PATCH"""
        json_data = self._prepare_model_data(body, exclude_defaults=exclude_defaults)
        response = self._patch(
            GET_ASSET_KEYFRAME.format(asset_id, keyframe_id),
            json=json_data,
            **kwargs,
        )
        return self.parse_response(response, Keyframe)

    def update_keyframe(
        self,
        asset_id: str,
        keyframe_id: str,
        body: Union[Keyframe, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """Update an asset keyframe using POST"""
        json_data = self._prepare_model_data(body, exclude_defaults=exclude_defaults)
        response = self._post(
            GET_ASSET_KEYFRAME.format(asset_id, keyframe_id),
            json=json_data,
            **kwargs,
        )
        return self.parse_response(response, Keyframe)

    def get_upload_id_for_keyframe(self, keyframe: Keyframe) -> PythonikResponse:
        """
        Get upload ID for keyframe. This ID is required to upload keyframe files.

        :return: PythonikResponse
        :raises UnexpectedStorageMethodForProxy: When keyframe exists on an unsupported storage method (i.e. Pythonik cannot
        automatically determine the upload ID)
        """
        headers = {"Origin": self.base_url, "Referer": self.base_url}
        if keyframe.storage_method == StorageMethod.S3:
            upload_url = keyframe.multipart_upload_url
            headers = {"Host": urlparse(upload_url).netloc, **headers}
        elif keyframe.storage_method == StorageMethod.GCS:
            upload_url = keyframe.upload_url
            headers = {"X-Goog-Resumable": "start", **headers}
        else:
            # escape hatch
            supported_methods = [StorageMethod.S3, StorageMethod.GCS]
            raise UnexpectedStorageMethodForProxy(
                f"Unexpected storage method: {keyframe.storage_method}."
                f" Pythonik supports {supported_methods}."
            )

        upload_url_response = requests.post(upload_url, headers=headers)
        if not upload_url_response.ok:
            return PythonikResponse(response=upload_url_response, data=None)

        if keyframe.storage_method == StorageMethod.S3:
            raise NotImplementedError(
                "Pythonik does not currently support creating keyframes on S3"
            )
            xml = parseString(upload_url_response.text)
            key = xml.getElementsByTagName("Key")[0].firstChild.nodeValue
            bucket = xml.getElementsByTagName("Bucket")[0].firstChild.nodeValue
            upload_id = xml.getElementsByTagName(S3_UPLOADID_KEY)[
                0
            ].firstChild.nodeValue
            data = upload_id
        elif keyframe.storage_method == StorageMethod.GCS:
            upload_id = upload_url_response.headers[GCS_UPLOADID_KEY]
            location = upload_url_response.headers[GCS_KEYFRAME_LOCATION_KEY]
            data = GCSKeyframeUploadResponse(upload_id=upload_id, location=location)
        else:
            supported_methods = [StorageMethod.S3, StorageMethod.GCS]
            raise UnexpectedStorageMethodForProxy(
                f"Unexpected storage method: {keyframe.storage_method}."
                f" Pythonik supports {supported_methods}."
            )

        return PythonikResponse(response=upload_url_response, data=data)

    def get_upload_id_for_proxy(self, asset_id: str, proxy_id: str) -> PythonikResponse:
        """
        Get upload ID for proxy. This ID is required to upload proxy files.
        :param asset_id: Asset ID
        :param proxy_id: Proxy ID
        :return: PythonikResponse
        :raises UnexpectedStorageMethodForProxy: When prox exists on an unsupported storage method (i.e. Pythonik cannot
        automatically determine the upload ID)
        """
        proxy_response = self.get_asset_proxy(asset_id, proxy_id)
        if not proxy_response.response.ok:
            # bubble up the error for caller to handle
            return proxy_response

        proxy = proxy_response.data
        headers = {"Origin": self.base_url, "Referer": self.base_url}
        if proxy.storage_method == StorageMethod.S3:
            upload_url = proxy.multipart_upload_url
            headers = {"Host": urlparse(upload_url).netloc, **headers}
        elif proxy.storage_method == StorageMethod.GCS:
            upload_url = proxy.upload_url
            headers = {"X-Goog-Resumable": "start", **headers}
        else:
            # escape hatch
            supported_methods = [StorageMethod.S3, StorageMethod.GCS]
            raise UnexpectedStorageMethodForProxy(
                f"Unexpected storage method: {proxy.storage_method}."
                f" pythonik supports {supported_methods}."
            )

        upload_url_response = requests.post(upload_url, headers=headers)
        if not upload_url_response.ok:
            return PythonikResponse(response=upload_url_response, data=None)

        if proxy.storage_method == StorageMethod.S3:
            xml = parseString(upload_url_response.text)
            # key = xml.getElementsByTagName("Key")[0].firstChild.nodeValue
            # bucket = xml.getElementsByTagName("Bucket")[0].firstChild.nodeValue
            upload_id = xml.getElementsByTagName(S3_UPLOADID_KEY)[
                0
            ].firstChild.nodeValue
        elif proxy.storage_method == StorageMethod.GCS:
            upload_id = upload_url_response.headers[GCS_UPLOADID_KEY]
        else:
            supported_methods = [StorageMethod.S3, StorageMethod.GCS]
            raise UnexpectedStorageMethodForProxy(
                f"Unexpected storage method: {proxy.storage_method}."
                f" pythonik supports {supported_methods}."
            )

        return PythonikResponse(response=upload_url_response, data=upload_id)

    def get_s3_presigned_url(
        self, asset_id: str, proxy_id: str, upload_id: str, part_number: int,
        **kwargs
    ) -> PythonikResponse:
        """
        Get a singed part URL to upload a proxy.
        :param asset_id: Asset ID
        :param proxy_id: Proxy ID
        :param upload_id: Upload ID
        :param part_number: Upload part number
        :return: PythonikResponse
        """
        response = self._get(
            path=GET_ASSET_PROXIES_MULTIPART_URL_PATH.format(asset_id, proxy_id),
            params={"upload_id": upload_id, "parts_num": part_number},
            **kwargs
        )

        if not response.ok:
            return PythonikResponse(response=response, data=None)

        return self.parse_response(response, S3MultipartUploadResponse)

    def get_s3_complete_url(
        self, asset_id: str, proxy_id: str, upload_id: str, **kwargs
    ) -> PythonikResponse:
        response = self._get(
            GET_ASSET_PROXIES_MULTIPART_COMPLETE_URL_PATH.format(asset_id, proxy_id),
            params={"upload_id": upload_id, "type": "complete_url"},
            **kwargs
        )
        if not response.ok:
            return PythonikResponse(response=response, data=None)
        return PythonikResponse(response=response, data=response.json()["complete_url"])

    def get_asset_proxies(self, asset_id: str, **kwargs) -> PythonikResponse:
        resp = self._get(GET_ASSET_PROXIES_PATH.format(asset_id), **kwargs)

        return self.parse_response(resp, Proxies)

    def create_asset_format(
        self, asset_id: str, body: Union[FormatCreate, Dict[str, Any]], exclude_defaults: bool = True, **kwargs
    ) -> Response:
        """
        Create format and associate it to asset
        Returns: Response(model=Format)
        """
        json_data = self._prepare_model_data(body, exclude_defaults=exclude_defaults)
        response = self._post(
            GET_ASSETS_FORMATS_PATH.format(asset_id),
            json=json_data,
            **kwargs,
        )
        return self.parse_response(response, Format)

    def create_asset_file(
        self, asset_id: str, body: Union[FileCreate, Dict[str, Any]], exclude_defaults: bool = True, **kwargs
    ) -> Response:
        """
        Create file and associate to asset
        Returns: Response(model=File)
        """
        json_data = self._prepare_model_data(body, exclude_defaults=exclude_defaults)
        response = self._post(
            GET_ASSETS_FILES_PATH.format(asset_id),
            json=json_data,
            **kwargs,
        )
        return self.parse_response(response, File)

    def create_asset_filesets(
        self, asset_id: str, body: Union[FileSetCreate, Dict[str, Any]], exclude_defaults: bool = True, **kwargs
    ) -> Response:
        warnings.warn(
            "'create_asset_filesets' is deprecated. Use 'create_asset_file_sets' instead.",
            DeprecationWarning,
            stacklevel=2
        )
        return self.create_asset_file_sets(asset_id, body, exclude_defaults, **kwargs)

    def create_asset_file_sets(
        self, asset_id: str, body: Union[FileSetCreate, Dict[str, Any]], exclude_defaults: bool = True, **kwargs
    ) -> Response:
        """
        Create file sets and associate it to asset
        Returns: Response(model=FileSet)
        """
        json_data = self._prepare_model_data(body, exclude_defaults=exclude_defaults)
        response = self._post(
            GET_ASSETS_FILE_SETS_PATH.format(asset_id),
            json=json_data,
            **kwargs,
        )
        return self.parse_response(response, FileSet)

    def get_asset_file_sets_by_version(
        self, asset_id: str, version_id: str, per_page: int = None, last_id: str = None, file_count: bool = None, **kwargs
    ) -> Response:
        """
        Get all asset's file sets by version
        
        Args:
            asset_id: ID of the asset
            version_id: ID of the version
            per_page: The number of items for each page
            last_id: ID of a last file set on previous page
            file_count: Set to true if you need a total amount of files in a file set
            **kwargs: Additional kwargs to pass to the request
            
        Returns:
            Response(model=FileSets)
            
        Required roles:
            - can_read_files
            
        Raises:
            401 Token is invalid
            404 FileSets for this asset don't exist
        """
        params = {}
        if per_page is not None:
            params["per_page"] = per_page
        if last_id is not None:
            params["last_id"] = last_id
        if file_count is not None:
            params["file_count"] = file_count

        response = self._get(
            GET_ASSETS_VERSION_FILE_SETS_PATH.format(asset_id, version_id),
            params=params,
            **kwargs,
        )
        return self.parse_response(response, FileSets)

    def get_asset_filesets(self, asset_id: str, **kwargs) -> Response:
        """Get all file sets associated with an asset
        
        Args:
            asset_id: The ID of the asset
            **kwargs: Additional arguments to pass to the request
            
        Returns:
            Response containing list of FileSets
        """
        resp = self._get(GET_ASSETS_FILE_SETS_PATH.format(asset_id), **kwargs)
        return self.parse_response(resp, FileSets)

    def get_asset_formats(self, asset_id: str, **kwargs) -> Response:
        """Get all formats associated with an asset
        
        Args:
            asset_id: The ID of the asset
            **kwargs: Additional arguments to pass to the request
            
        Returns:
            Response containing list of Formats
        """
        resp = self._get(GET_ASSETS_FORMATS_PATH.format(asset_id), **kwargs)
        return self.parse_response(resp, Formats)

    def get_asset_format(self, asset_id: str, format_id: str, **kwargs) -> Response:
        """Get a specific format for an asset
        
        Args:
            asset_id: The ID of the asset
            format_id: The ID of the format to retrieve
            **kwargs: Additional arguments to pass to the request
            
        Returns:
            Response with Format model
        """
        resp = self._get(GET_ASSETS_FORMAT_PATH.format(asset_id, format_id), **kwargs)
        return self.parse_response(resp, Format)

    def get_asset_files(self, asset_id: str, **kwargs) -> Response:
        """Get all files associated with an asset
        
        Args:
            asset_id: The ID of the asset
            **kwargs: Additional arguments to pass to the request
            
        Returns:
            Response containing list of Files
        """
        resp = self._get(GET_ASSETS_FILES_PATH.format(asset_id), **kwargs)
        return self.parse_response(resp, Files)

    def get_storage(self, storage_id: str, **kwargs):
        """Get metadata for a specific storage
        
        Args:
            storage_id: The ID of the storage to retrieve
            **kwargs: Additional arguments to pass to the request
            
        Returns:
            Response with Storage model
        """
        resp = self._get(GET_STORAGE_PATH.format(storage_id), **kwargs)
        return self.parse_response(resp, Storage)

    def get_storages(self, **kwargs):
        """Get metadata for all available storages
        
        Args:
            **kwargs: Additional arguments to pass to the request
            
        Returns:
            Response containing list of Storages
        """
        resp = self._get(GET_STORAGES_PATH, **kwargs)
        return self.parse_response(resp, Storages)

    def update_asset_format(
        self, asset_id: str, format_id: str, body: Union[FormatCreate, Dict[str, Any]], exclude_defaults: bool = True, **kwargs
    ) -> Response:
        """
        Update format information for an asset using PUT
        
        Args:
            asset_id: ID of the asset
            format_id: ID of the format to update
            body: Format update parameters, either as FormatCreate model or dict
            exclude_defaults: Whether to exclude default values when dumping Pydantic models
            **kwargs: Additional kwargs to pass to the request
            
        Returns:
            Response(model=Format)
            
        Required roles:
            - can_write_formats
            
        Raises:
            400 Bad request
            401 Token is invalid
            404 Format for this asset doesn't exist
        """
        json_data = self._prepare_model_data(body, exclude_defaults=exclude_defaults)
        response = self._put(
            GET_ASSETS_FORMAT_PATH.format(asset_id, format_id),
            json=json_data,
            **kwargs,
        )
        return self.parse_response(response, Format)

    def partial_update_asset_format(
        self, asset_id: str, format_id: str, body: Union[FormatCreate, Dict[str, Any]], exclude_defaults: bool = True, **kwargs
    ) -> Response:
        """
        Partially update format information for an asset using PATCH
        
        Args:
            asset_id: ID of the asset
            format_id: ID of the format to update
            body: Format update parameters, either as FormatCreate model or dict
            exclude_defaults: Whether to exclude default values when dumping Pydantic models
            **kwargs: Additional kwargs to pass to the request
            
        Returns:
            Response(model=Format)
            
        Required roles:
            - can_write_formats
            
        Raises:
            400 Bad request
            401 Token is invalid
            404 Format for this asset doesn't exist
        """
        json_data = self._prepare_model_data(body, exclude_defaults=exclude_defaults)
        response = self._patch(
            GET_ASSETS_FORMAT_PATH.format(asset_id, format_id),
            json=json_data,
            **kwargs,
        )
        return self.parse_response(response, Format)

    def update_asset_file_set(
        self, asset_id: str, file_set_id: str, body: Union[FileSetCreate, Dict[str, Any]], exclude_defaults: bool = True, **kwargs
    ) -> Response:
        """
        Update file set information for an asset using PUT
        
        Args:
            asset_id: ID of the asset
            file_set_id: ID of the file set to update
            body: File set update parameters, either as FileSetCreate model or dict
            exclude_defaults: Whether to exclude default values when dumping Pydantic models
            **kwargs: Additional kwargs to pass to the request
            
        Returns:
            Response(model=FileSet)
            
        Required roles:
            - can_write_files
            
        Raises:
            400 Bad request
            401 Token is invalid
            404 File set for this asset doesn't exist
        """
        json_data = self._prepare_model_data(body, exclude_defaults=exclude_defaults)
        response = self._put(
            GET_ASSETS_FILE_SETS_PATH.format(asset_id, file_set_id),
            json=json_data,
            **kwargs,
        )
        return self.parse_response(response, FileSet)

    def partial_update_asset_file_set(
        self, asset_id: str, file_set_id: str, body: Union[FileSetCreate, Dict[str, Any]], exclude_defaults: bool = True, **kwargs
    ) -> Response:
        """
        Partially update file set information for an asset using PATCH
        
        Args:
            asset_id: ID of the asset
            file_set_id: ID of the file set to update
            body: File set update parameters, either as FileSetCreate model or dict
            exclude_defaults: Whether to exclude default values when dumping Pydantic models
            **kwargs: Additional kwargs to pass to the request
            
        Returns:
            Response(model=FileSet)
            
        Required roles:
            - can_write_files
            
        Raises:
            400 Bad request
            401 Token is invalid
            404 File set for this asset doesn't exist
        """
        json_data = self._prepare_model_data(body, exclude_defaults=exclude_defaults)
        response = self._patch(
            GET_ASSETS_FILE_SETS_PATH.format(asset_id, file_set_id),
            json=json_data,
            **kwargs,
        )
        return self.parse_response(response, FileSet)

    def update_asset_file(
        self, asset_id: str, file_id: str, body: Union[FileCreate, Dict[str, Any]], exclude_defaults: bool = True, **kwargs
    ) -> Response:
        """
        Update file information for an asset using PUT
        
        Args:
            asset_id: ID of the asset
            file_id: ID of the file to update
            body: File update parameters, either as FileCreate model or dict
            exclude_defaults: Whether to exclude default values when dumping Pydantic models
            **kwargs: Additional kwargs to pass to the request
            
        Returns:
            Response(model=File)
            
        Required roles:
            - can_write_files
            
        Raises:
            400 Bad request
            401 Token is invalid
            404 File for this asset doesn't exist
        """
        json_data = self._prepare_model_data(body, exclude_defaults=exclude_defaults)
        response = self._put(
            GET_ASSETS_FILE_PATH.format(asset_id, file_id),
            json=json_data,
            **kwargs,
        )
        return self.parse_response(response, File)

    def partial_update_asset_file(
        self, asset_id: str, file_id: str, body: Union[FileCreate, Dict[str, Any]], exclude_defaults: bool = True, **kwargs
    ) -> Response:
        """
        Partially update file information for an asset using PATCH
        
        Args:
            asset_id: ID of the asset
            file_id: ID of the file to update
            body: File update parameters, either as FileCreate model or dict
            exclude_defaults: Whether to exclude default values when dumping Pydantic models
            **kwargs: Additional kwargs to pass to the request
            
        Returns:
            Response(model=File)
            
        Required roles:
            - can_write_files
            
        Raises:
            400 Bad request
            401 Token is invalid
            404 File for this asset doesn't exist
        """
        json_data = self._prepare_model_data(body, exclude_defaults=exclude_defaults)
        response = self._patch(
            GET_ASSETS_FILE_PATH.format(asset_id, file_id),
            json=json_data,
            **kwargs,
        )
        return self.parse_response(response, File)

    def get_asset_formats_by_version(
        self, asset_id: str, version_id: str, per_page: int = None, last_id: str = None, **kwargs
    ) -> Response:
        """
        Get all asset's formats by version
        
        Args:
            asset_id: ID of the asset
            version_id: ID of the version
            per_page: The number of items for each page
            last_id: ID of a last format on previous page
            **kwargs: Additional kwargs to pass to the request
            
        Returns:
            Response(model=Formats)
            
        Required roles:
            - can_read_formats
            
        Raises:
            401 Token is invalid
            404 Formats for this asset don't exist
        """
        params = {}
        if per_page is not None:
            params["per_page"] = per_page
        if last_id is not None:
            params["last_id"] = last_id

        response = self._get(
            GET_ASSETS_VERSION_FORMATS_PATH.format(asset_id, version_id),
            params=params,
            **kwargs,
        )
        return self.parse_response(response, Formats)

    def get_asset_files_by_version(
        self, asset_id: str, version_id: str, per_page: int = None, last_id: str = None, 
        generate_signed_url: bool = None, content_disposition: str = None, **kwargs
    ) -> Response:
        """
        Get all asset's files by version
        
        Args:
            asset_id: ID of the asset
            version_id: ID of the version
            per_page: The number of items for each page
            last_id: ID of a last file on previous page
            generate_signed_url: Set to False if you do not need a URL, will slow things down otherwise
            content_disposition: Set to attachment if you want a download link. Note that this will not create a download in asset history
            **kwargs: Additional kwargs to pass to the request
            
        Returns:
            Response(model=Files)
            
        Required roles:
            - can_read_files
            
        Raises:
            401 Token is invalid
            404 Files for this asset don't exist
        """
        params = {}
        if per_page is not None:
            params["per_page"] = per_page
        if last_id is not None:
            params["last_id"] = last_id
        if generate_signed_url is not None:
            params["generate_signed_url"] = generate_signed_url
        if content_disposition is not None:
            params["content_disposition"] = content_disposition

        response = self._get(
            GET_ASSETS_VERSION_FILES_PATH.format(asset_id, version_id),
            params=params,
            **kwargs,
        )
        return self.parse_response(response, Files)

    def create_storage_file(
            self,
            storage_id: str,
            body: Union[File, Dict[str, Any]],
            exclude_defaults: bool = True,
            **kwargs
    ) -> Response:
        """
        Create file without associating it to an asset.

        Args:
            storage_id: The ID of the storage to retrieve
            body: Storage file creation parameters, either as File model or dict
            exclude_defaults: Whether to exclude default values when dumping
                Pydantic models
            **kwargs: Additional arguments to pass to the request

        Returns:
            Response(model=PaginatedResponse) with created file information
        """
        json_data = self._prepare_model_data(
            body, exclude_defaults=exclude_defaults
        )
        resp = self._post(
            self.gen_url(f"storages/{storage_id}/files/"),
            json=json_data,
            **kwargs
        )
        return self.parse_response(resp, PaginatedResponse)

    def list_asset_format_components(
            self, asset_id: str, format_id: str, **kwargs
    ) -> Response:
        """
        Get all components for a format in an asset.

        Args:
            asset_id: The ID of the asset
            format_id: The ID of the format to retrieve
            **kwargs: Additional arguments to pass to the request

        Returns:
            Response(model=PaginatedResponse) containing format components
        """
        resp = self._get(
            self.gen_url(f"assets/{asset_id}/formats/{format_id}/components/"),
            **kwargs
        )
        return self.parse_response(resp, PaginatedResponse)

    def list_storage_files(self, storage_id: str, **kwargs) -> Response:
        """
        Get all files on a storage, or files in a storage folder.

        Args:
            storage_id: The ID of the storage to retrieve
            **kwargs: Additional arguments to pass to the request

        Returns:
            Response(model=PaginatedResponse) containing storage files
        """
        resp = self._get(
            self.gen_url(f"storages/{storage_id}/files/"), **kwargs
        )
        return self.parse_response(resp, PaginatedResponse)

    def _get_deleted_object_type(
            self, object_type: Literal["file_sets", "formats"], **kwargs
    ) -> Response:
        """
        Get deleted object type.

        Args:
            object_type: The type of object to retrieve
            **kwargs: Additional arguments to pass to the request

        Returns:
            Response(model=None) containing deleted objects

        Raises:
            ValueError: If object_type is not 'file_sets' or 'formats'
        """
        if object_type not in ["file_sets", "formats"]:
            raise ValueError("object_type must be one of file_sets or formats")
        resp = self._get(self.gen_url(f"delete_queue/{object_type}/"), **kwargs)
        return self.parse_response(resp, None)

    def get_deleted_file_sets(self, **kwargs) -> Response:
        """
        Get deleted file sets.

        Args:
            **kwargs: Additional arguments to pass to the request

        Returns:
            Response(model=None) containing deleted file sets
        """
        return self._get_deleted_object_type("file_sets", **kwargs)

    # Create method alias
    get_deleted_filesets = get_deleted_file_sets

    def get_deleted_formats(self, **kwargs) -> Response:
        """
        Get deleted formats.

        Args:
            **kwargs: Additional arguments to pass to the request

        Returns:
            Response(model=None) containing deleted formats
        """
        return self._get_deleted_object_type("formats", **kwargs)

    def create_mediainfo_job(
            self,
            asset_id: str,
            file_id: str,
            priority: Optional[int] = 5,
            **kwargs
    ) -> Response:
        """
        Create a job for extracting mediainfo.

        Args:
            asset_id: ID of the asset
            file_id: ID of the file
            priority: Job priority 1-10. Default is 5
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=None) with job creation status
        """
        body = {"priority": priority}
        resp = self._post(
            self.gen_url(f"assets/{asset_id}/files/{file_id}/mediainfo"),
            json=body,
            **kwargs
        )
        return self.parse_response(resp, None)

    def create_transcode_job(
            self,
            asset_id: str,
            file_id: str,
            priority: Optional[int] = 5,
            **kwargs
    ) -> Response:
        """
        Create a transcode job for proxy and keyframes.

        Args:
            asset_id: ID of the asset
            file_id: ID of the file
            priority: Job priority 1-10. Default is 5
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=None) with job creation status
        """
        body = {"priority": priority}
        resp = self._post(
            self.gen_url(f"assets/{asset_id}/files/{file_id}/keyframes"),
            json=body,
            **kwargs
        )
        return self.parse_response(resp, None)
