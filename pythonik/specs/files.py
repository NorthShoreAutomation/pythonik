from urllib.parse import urlparse
from xml.dom.minidom import parseString

import requests

from pythonik.constants import (
    GCS_KEYFRAME_LOCATION_KEY,
    GCS_UPLOADID_KEY,
    S3_UPLOADID_KEY,
)
from pythonik.exceptions import UnexpectedStorageMethodForProxy
from pythonik.models.base import Response, StorageMethod
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
GET_ASSETS_FILE_SET_PATH = "assets/{}/file_sets/"
GET_ASSETS_FILE_SET_FILES_PATH = "assets/{}/file_sets/{}/files/"
GET_STORAGE_PATH = "storages/{}/"
GET_STORAGES_PATH = "storages/"
GET_ASSET_KEYFRAME = "assets/{}/keyframes/{}/"
GET_ASSET_KEYFRAMES = "assets/{}/keyframes/"
GET_ASSETS_FILE_PATH = "assets/{}/files/{}/"
DELETE_ASSETS_FILE_SET_PATH = "assets/{}/file_sets/{}/"
DELETE_ASSETS_FILE_PATH = "assets/{}/files/{}/"


class FilesSpec(Spec):
    server = "API/files/"

    def get_asset_file_sets(self, asset_id: str, file_sets_id: str, **kwargs) -> Response:
        """
        Retrieve file sets for a specific asset

        Args:
            asset_id: ID of the asset
            file_sets_id: ID of the file set to retrieve
            kwargs: additional kwargs passed to the request
        
        Returns:
            Response(model=FileSetsFilesResponse)
        
        Required roles:
            - can_read_files
        
        Raises:
            - 401 Token is invalid
            - 404 FileSets for this asset don't exist
        """
        response = self._get(
            GET_ASSETS_FILE_SET_FILES_PATH.format(asset_id, file_sets_id),
            **kwargs
        )
        return self.parse_response(response, FileSetsFilesResponse)

    def create_asset_format_component(
        self,
        asset_id: str,
        format_id: str,
        body: Component,
        exclude_defaults=True,
        **kwargs,
    ) -> Response:
        """
        Create a new format component

        Args:
            asset_id: ID of the asset
            format_id: ID for the format
            body: component creation parameters
            exclude_defaults: If True, exclude default values from request
            kwargs: additional kwargs passed to the request

        Returns:
            Response(model=Formats)

        Required roles:
            - can_write_formats

        Raises:
            400 Bad request
            401 Token is invalid
            404 Formats for this asset don't exist
        """
        response = self._post(
            GET_ASSETS_FORMAT_COMPONENTS_PATH.format(asset_id, format_id),
            json=body.model_dump(exclude_defaults=exclude_defaults),
            **kwargs,
        )
        return self.parse_response(response, Formats)
    

    def delete_asset_file(self, asset_id: str, file_id: str) -> Response:
        """Delete a specific file from an asset
        
        Args:
            asset_id: The ID of the asset
            file_id: The ID of the file to delete
            
        Returns:
            Response with no data model
        """
        response = self._delete(DELETE_ASSETS_FILE_PATH.format(asset_id, file_id))
        return self.parse_response(response, model=None)

    def delete_asset_file_set(
        self, asset_id: str, file_set_id: str, keep_source: bool = False
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
            params=params
        )
        
        # If status is 204, return response with no model
        if response.status_code == 204:
            return self.parse_response(response, model=None)
            
        # If status is possibly 200, return response with FileSet model
        return self.parse_response(response, FileSet)


    def delete_asset_keyframe(self, asset_id: str, keyframe_id: str):
        response = self._delete(GET_ASSET_KEYFRAME.format(asset_id, keyframe_id))
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

    def get_asset_keyframe(self, asset_id: str, keyframe_id: str) -> Response:
        """Get a specific keyframe for an asset
        
        Args:
            asset_id: The ID of the asset
            keyframe_id: The ID of the keyframe to retrieve
            
        Returns:
            Response with Keyframe model
        """
        response = self._get(GET_ASSET_KEYFRAME.format(asset_id, keyframe_id))
        return self.parse_response(response, Keyframe)

    def get_asset_keyframes(self, asset_id: str) -> Keyframes:
        """Get all keyframes for an asset
        
        Args:
            asset_id: The ID of the asset
            
        Returns:
            Response containing list of Keyframes
        """
        response = self._get(GET_ASSET_KEYFRAMES.format(asset_id))
        return self.parse_response(response, Keyframes)

    def create_asset_keyframe(
        self, asset_id: str, body: Keyframe, exclude_defaults=True, **kwargs
    ) -> Response:
        """Create a new keyframe for an asset
        
        Args:
            asset_id: The ID of the asset
            body: Keyframe object containing the keyframe data
            exclude_defaults: If True, exclude default values from the request
            **kwargs: Additional arguments to pass to the request
            
        Returns:
            Response with created Keyframe model
        """
        response = self._post(
            GET_ASSET_KEYFRAMES.format(asset_id),
            json=body.model_dump(exclude_defaults=exclude_defaults),
            **kwargs,
        )
        return self.parse_response(response, Keyframe)

    def get_asset_proxy(self, asset_id: str, proxy_id: str) -> Response:
        """Get asset's proxy
        Returns: Response(model=Proxy)
        """

        resp = self._get(GET_ASSET_PROXY_PATH.format(asset_id, proxy_id))

        return self.parse_response(resp, Proxy)

    def update_asset_proxy(
        self, asset_id: str, proxy_id: str, body: Proxy, exclude_defaults=True, **kwargs
    ) -> Response:
        """
        Update asset's proxy
        """
        response = self._patch(
            GET_ASSET_PROXY_PATH.format(asset_id, proxy_id),
            json=body.model_dump(exclude_defaults=exclude_defaults),
            **kwargs,
        )
        return self.parse_response(response, Proxy)

    def create_asset_proxy(
        self, asset_id: str, body: Proxy, exclude_defaults=True, **kwargs
    ) -> Response:
        """
        Create proxy and associate to asset
        Returns: Response(model=Proxy)
        """
        response = self._post(
            GET_ASSET_PROXIES_PATH.format(asset_id),
            json=body.model_dump(exclude_defaults=exclude_defaults),
            **kwargs,
        )
        return self.parse_response(response, Proxy)

    def partial_update_keyframe(
        self,
        asset_id: str,
        keyframe_id: str,
        body: Keyframe,
        exclude_defaults=True,
        **kwargs,
    ) -> Response:
        "Partially update an asset keyframe using PATCH"
        response = self._patch(
            GET_ASSET_KEYFRAME.format(asset_id, keyframe_id),
            json=body.model_dump(exclude_defaults=exclude_defaults),
            **kwargs,
        )
        return self.parse_response(response, Keyframe)

    def update_keyframe(
        self,
        asset_id: str,
        keyframe_id: str,
        body: Keyframe,
        exclude_defaults=True,
        **kwargs,
    ) -> Response:
        "Update an asset keyframe using POST"
        response = self._post(
            GET_ASSET_KEYFRAME.format(asset_id, keyframe_id),
            json=body.model_dump(exclude_defaults=exclude_defaults),
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
                f" Pythonik supports {supported_methods}."
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
                f" Pythonik supports {supported_methods}."
            )

        return PythonikResponse(response=upload_url_response, data=upload_id)

    def get_s3_presigned_url(
        self, asset_id: str, proxy_id: str, upload_id: str, part_number: int
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
        )

        if not response.ok:
            return PythonikResponse(response=response, data=None)

        return self.parse_response(response, S3MultipartUploadResponse)

    def get_s3_complete_url(
        self, asset_id: str, proxy_id: str, upload_id: str
    ) -> PythonikResponse:
        response = self._get(
            GET_ASSET_PROXIES_MULTIPART_COMPLETE_URL_PATH.format(asset_id, proxy_id),
            params={"upload_id": upload_id, "type": "complete_url"},
        )
        if not response.ok:
            return PythonikResponse(response=response, data=None)
        return PythonikResponse(response=response, data=response.json()["complete_url"])

    def get_asset_proxies(self, asset_id: str):
        resp = self._get(GET_ASSET_PROXIES_PATH.format(asset_id))

        return self.parse_response(resp, Proxies)

    def create_asset_format(
        self, asset_id: str, body: FormatCreate, exclude_defaults=True, **kwargs
    ) -> Response:
        """
        Create format and associate it to asset
        Returns: Response(model=Format)
        """
        response = self._post(
            GET_ASSETS_FORMATS_PATH.format(asset_id),
            json=body.model_dump(exclude_defaults=exclude_defaults),
            **kwargs,
        )
        return self.parse_response(response, Format)

    def create_asset_file(
        self, asset_id: str, body: FileCreate, exclude_defaults=True, **kwargs
    ) -> Response:
        """
        Create file and associate to asset
        Returns: Response(model=File)
        """
        response = self._post(
            GET_ASSETS_FILES_PATH.format(asset_id),
            json=body.model_dump(exclude_defaults=exclude_defaults),
            **kwargs,
        )
        return self.parse_response(response, File)

    def create_asset_filesets(
        self, asset_id: str, body: FileSetCreate, exclude_defaults=True, **kwargs
    ) -> Response:
        """
        Create file sets and associate it to asset
        Returns: Response(model=FileSet)
        """
        response = self._post(
            GET_ASSETS_FILE_SET_PATH.format(asset_id),
            json=body.model_dump(exclude_defaults=exclude_defaults),
            **kwargs,
        )
        return self.parse_response(response, FileSet)

    def get_asset_filesets(self, asset_id: str, **kwargs) -> Response:
        """Get all file sets associated with an asset
        
        Args:
            asset_id: The ID of the asset
            **kwargs: Additional arguments to pass to the request
            
        Returns:
            Response containing list of FileSets
        """
        resp = self._get(GET_ASSETS_FILE_SET_PATH.format(asset_id), **kwargs)
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
