from typing import (
    Any,
    Dict,
    List,
    Optional,
    Union,
)

from pythonik.models.acls import (
    ACLSchema,
    ACLsSchema,
    ACLTemplateSchema,
    ACLTemplatesSchema,
    BulkACLSchema,
    CheckBulkACLsSchema,
    CombinedPermissionsSchema,
    CreateACLsResultSchema,
    CreateACLsSchema,
    CreateBulkACLsSchema,
    CreateMultipleACLsSchema,
    CreateShareACLsSchema,
    DeleteACLsSchema,
    DeleteBulkACLsSchema,
    GroupACLSchema,
    ShareACLSchema,
    SharesACLSchema,
    UserACLSchema,
)
from pythonik.models.base import Response
from pythonik.specs.base import Spec

from ._internal_utils import is_pydantic_model


class AclsSpec(Spec):
    server = "API/acls/"
    VALID_PERMISSIONS = ["change-acl", "delete", "read", "write"]

    # pylint: disable=too-many-positional-arguments
    def apply_template_permissions(
        self,
        template_id: str,
        object_type: str,
        object_key: str,
        ignore_reindexing: Optional[bool] = False,
        restrict_acls_collection_id: Optional[str] = None,
        **kwargs,
    ) -> Response:
        """
        Apply template permissions to an object

        Args:
            template_id: ID of the template to apply permissions for
            object_type: Type of the object (e.g. "user")
            object_key: ID of the object
            ignore_reindexing: Ignore reindexing
            restrict_acls_collection_id: Do not apply any ACLs that are not in
                the collection_id provided (Parent collection normally)
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=None)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
            - 403 User does not have permission
            - 404 ACL template does not exist
        """
        params = {
            "ignore_reindexing": ignore_reindexing,
            "restrict_acls_collection_id": restrict_acls_collection_id,
        }
        url = self.gen_url(
            f"acl/templates/{template_id}/{object_type}/{object_key}/")
        resp = self._post(url, params=params, **kwargs)
        return self.parse_response(resp, None)

    def apply_group_permissions(
        self,
        group_id: str,
        object_type: str,
        object_key: str,
        permissions: List[str],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Update or create group acl for an object

        Args:
            group_id: ID of the group to apply permissions for
            object_type: Type of the object
            object_key: ID of the object
            permissions: List of permissions to apply
            exclude_defaults: Whether to exclude default values when dumping
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=GroupACLSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
            - 404 ACL does not exist
            - ValueError: If invalid permissions provided
        """
        if permissions and not any(_ in permissions
                                   for _ in self.VALID_PERMISSIONS):
            raise ValueError(f"Value must be one of {self.VALID_PERMISSIONS}")
        model = GroupACLSchema(permissions=permissions)
        body = model.model_dump(exclude_defaults=exclude_defaults)
        url = self.gen_url(
            f"groups/{group_id}/acl/{object_type}/{object_key}/")
        resp = self._put(url, json=body, **kwargs)
        return self.parse_response(resp, GroupACLSchema)

    def list_object_permissions(self, object_type: str, object_key: str,
                                **kwargs) -> Response:
        """
        List of object permissions

        Args:
            object_type: Type of the object
            object_key: ID of the object
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=ACLSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        url = self.gen_url(f"acl/{object_type}/{object_key}/")
        resp = self._get(url, **kwargs)
        return self.parse_response(resp, ACLSchema)

    def list_acl_templates(self, **kwargs) -> Response:
        """
        Retrieve all ACL templates

        Args:
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=ACLTemplatesSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        url = self.gen_url("acl/templates/")
        resp = self._get(url, **kwargs)
        return self.parse_response(resp, ACLTemplatesSchema)

    def create_acl_template(
        self,
        name: str,
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Create an ACL template

        Args:
            name: Name of the template
            exclude_defaults: Whether to exclude default values when dumping
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=ACLTemplateSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        model = ACLTemplateSchema(name=name)
        body = model.model_dump(exclude_defaults=exclude_defaults)
        url = self.gen_url("acl/templates/")
        resp = self._post(url, json=body, **kwargs)
        return self.parse_response(resp, ACLTemplateSchema)

    def get_acl_template(self, template_id: str, **kwargs) -> Response:
        """
        Retrieve an ACL template

        Args:
            template_id: ID of the template
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=ACLTemplateSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
            - 404 Template does not exist
        """
        url = self.gen_url(f"acl/templates/{template_id}/")
        resp = self._get(url, **kwargs)
        return self.parse_response(resp, ACLTemplateSchema)

    def update_acl_template(
        self,
        template_id: str,
        template: Union[ACLTemplateSchema, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Update an ACL template

        Args:
            template_id: ID of the template
            template: Template data (either as ACLTemplateSchema or dict)
            exclude_defaults: Whether to exclude default values when dumping
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=ACLTemplateSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
            - 404 ACL template does not exist
        """
        body = (template.model_dump(exclude_defaults=exclude_defaults)
                if is_pydantic_model(template) else template)
        url = self.gen_url(f"acl/templates/{template_id}/")
        resp = self._put(url, json=body, **kwargs)
        return self.parse_response(resp, ACLTemplateSchema)

    def partial_update_acl_template(
        self,
        template_id: str,
        template: Union[ACLTemplateSchema, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Partially update an ACL template

        Args:
            template_id: ID of the template
            template: Template data to update (either as ACLTemplateSchema
                or dict)
            exclude_defaults: Whether to exclude default values when dumping
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=ACLTemplateSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
            - 404 ACL template does not exist
        """
        body = (template.model_dump(exclude_defaults=exclude_defaults,
                                    exclude_unset=True)
                if is_pydantic_model(template) else template)
        url = self.gen_url(f"acl/templates/{template_id}/")
        resp = self._patch(url, json=body, **kwargs)
        return self.parse_response(resp, ACLTemplateSchema)

    def delete_acl_template(self, template_id: str, **kwargs) -> Response:
        """
        Remove an ACL template

        Args:
            template_id: ID of the template to delete
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=None)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
            - 404 ACL template does not exist
        """
        url = self.gen_url(f"acl/templates/{template_id}/")
        resp = self._delete(url, **kwargs)
        return self.parse_response(resp, None)

    def check_objects_permission(
        self,
        objects: Union[CheckBulkACLsSchema, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Check if objects have required permission

        Args:
            objects: Objects to check permissions for (either as
                CheckBulkACLsSchema or dict)
            exclude_defaults: Whether to exclude default values when dumping
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=BulkACLSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
            - 403 User doesn't have permission
        """
        body = (objects.model_dump(exclude_defaults=exclude_defaults)
                if is_pydantic_model(objects) else objects)
        url = self.gen_url("acl/")
        resp = self._post(url, json=body, **kwargs)
        return self.parse_response(resp, BulkACLSchema)

    def check_object_permission(
        self,
        object_type: str,
        object_key: str,
        permission: str,
        **kwargs,
    ) -> Response:
        """
        Check if a particular object has required permission

        Args:
            object_type: Type of the object
            object_key: ID of the object
            permission: Permission to check
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=None)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
            - 403 User doesn't have permission
        """
        url = self.gen_url(f"acl/{object_type}/{object_key}/{permission}/")
        resp = self._get(url, **kwargs)
        return self.parse_response(resp, None)

    def get_combined_permissions(
        self,
        object_type: str,
        object_key: str,
        **kwargs,
    ) -> Response:
        """
        List of permissions for the user

        Args:
            object_type: Type of the object
            object_key: ID of the object
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=CombinedPermissionsSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        url = self.gen_url(f"acl/{object_type}/{object_key}/permissions/")
        resp = self._get(url, **kwargs)
        return self.parse_response(resp, CombinedPermissionsSchema)

    def check_objects_have_permission(
        self,
        object_type: str,
        permission: str,
        object_keys: Union[ACLsSchema, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Check if objects have required permission

        Args:
            object_type: Type of the object
            permission: Permission to check
            object_keys: Object keys to check
            exclude_defaults: Whether to exclude default values when dumping
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=BulkACLSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
            - 403 User doesn't have permission
        """
        body = (object_keys.model_dump(exclude_defaults=exclude_defaults)
                if is_pydantic_model(object_keys) else object_keys)
        url = self.gen_url(f"acl/{object_type}/{permission}/")
        resp = self._post(url, json=body, **kwargs)
        return self.parse_response(resp, BulkACLSchema)

    def create_acls(
        self,
        object_type: str,
        acls: Union[CreateACLsSchema, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Create a new ACL for multiple objects

        Args:
            object_type: Type of the object
            acls: ACLs to create (either as CreateACLsSchema or dict)
            exclude_defaults: Whether to exclude default values when dumping
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=CreateACLsResultSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        body = (acls.model_dump(exclude_defaults=exclude_defaults)
                if is_pydantic_model(acls) else acls)
        url = self.gen_url(f"acl/{object_type}/")
        resp = self._put(url, json=body, **kwargs)
        return self.parse_response(resp, CreateACLsResultSchema)

    def create_bulk_acls(
        self,
        object_type: str,
        acls: Union[CreateMultipleACLsSchema, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Create a new ACL for multiple objects with multiple permissions

        Args:
            object_type: Type of the object
            acls: ACLs to create (either as CreateMultipleACLsSchema or dict)
            exclude_defaults: Whether to exclude default values when dumping
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=None)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        body = (acls.model_dump(exclude_defaults=exclude_defaults)
                if is_pydantic_model(acls) else acls)
        url = self.gen_url(f"acl/{object_type}/bulk/")
        resp = self._put(url, json=body, **kwargs)
        return self.parse_response(resp, None)

    def create_acls_for_content(
        self,
        object_type: str,
        acls: Union[CreateBulkACLsSchema, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Create a new ACL for content of multiple objects

        Args:
            object_type: Type of the object
            acls: ACLs to create (either as CreateBulkACLsSchema or dict)
            exclude_defaults: Whether to exclude default values when dumping
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=None)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
            - 501 Invalid object type
        """
        body = (acls.model_dump(exclude_defaults=exclude_defaults)
                if is_pydantic_model(acls) else acls)
        url = self.gen_url(f"acl/{object_type}/content/")
        resp = self._put(url, json=body, **kwargs)
        return self.parse_response(resp, None)

    def delete_acls(
        self,
        object_type: str,
        acls: Union[DeleteACLsSchema, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Delete ACLs for multiple objects

        Args:
            object_type: Type of the object
            acls: ACLs to delete (either as DeleteACLsSchema or dict)
            exclude_defaults: Whether to exclude default values when dumping
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=None)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        body = (acls.model_dump(exclude_defaults=exclude_defaults)
                if is_pydantic_model(acls) else acls)
        url = self.gen_url(f"acl/{object_type}/")
        resp = self._delete(url, json=body, **kwargs)
        return self.parse_response(resp, None)

    def delete_acls_for_content(
        self,
        object_type: str,
        acls: Union[DeleteBulkACLsSchema, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Delete ACLs for content of multiple objects

        Args:
            object_type: Type of the object
            acls: ACLs to delete (either as DeleteBulkACLsSchema or dict)
            exclude_defaults: Whether to exclude default values when dumping
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=None)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        body = (acls.model_dump(exclude_defaults=exclude_defaults)
                if is_pydantic_model(acls) else acls)
        url = self.gen_url(f"acl/{object_type}/content/")
        resp = self._delete(url, json=body, **kwargs)
        return self.parse_response(resp, None)

    def get_group_acl(
        self,
        group_id: str,
        object_type: str,
        object_key: str,
        **kwargs,
    ) -> Response:
        """
        List of group permissions for an object

        Args:
            group_id: ID of the group
            object_type: Type of the object
            object_key: ID of the object
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=GroupACLSchema)

        Raises:
            - 401 Token is invalid
            - 404 Group doesn't have permissions
        """
        url = self.gen_url(
            f"groups/{group_id}/acl/{object_type}/{object_key}/")
        resp = self._get(url, **kwargs)
        return self.parse_response(resp, GroupACLSchema)

    def check_group_permission(
        self,
        group_id: str,
        object_type: str,
        object_key: str,
        permission: str,
        **kwargs,
    ) -> Response:
        """
        Check if group has particular permission for an object

        Args:
            group_id: ID of the group
            object_type: Type of the object
            object_key: ID of the object
            permission: Permission to check
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=None)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
            - 403 Group doesn't have particular permission
        """
        url = self.gen_url(f"groups/{group_id}/acl/{object_type}/{object_key}/"
                           f"{permission}/")
        resp = self._get(url, **kwargs)
        return self.parse_response(resp, None)

    def delete_group_acl(
        self,
        group_id: str,
        object_type: str,
        object_key: str,
        **kwargs,
    ) -> Response:
        """
        Delete a particular ACL by id for an object

        Args:
            group_id: ID of the group
            object_type: Type of the object
            object_key: ID of the object
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=None)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
            - 404 ACL does not exist
        """
        url = self.gen_url(
            f"groups/{group_id}/acl/{object_type}/{object_key}/")
        resp = self._delete(url, **kwargs)
        return self.parse_response(resp, None)

    def get_user_acl(
        self,
        user_id: str,
        object_type: str,
        object_key: str,
        **kwargs,
    ) -> Response:
        """
        List of user permissions for an object

        Args:
            user_id: ID of the user
            object_type: Type of the object
            object_key: ID of the object
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=UserACLSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        url = self.gen_url(f"users/{user_id}/acl/{object_type}/{object_key}/")
        resp = self._get(url, **kwargs)
        return self.parse_response(resp, UserACLSchema)

    def update_user_acl(
        self,
        user_id: str,
        object_type: str,
        object_key: str,
        acl: Union[UserACLSchema, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Update or create user ACL for an object

        Args:
            user_id: ID of the user
            object_type: Type of the object
            object_key: ID of the object
            acl: User ACL data (either as UserACLSchema or dict)
            exclude_defaults: Whether to exclude default values when dumping
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=UserACLSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
            - 404 ACL does not exist
        """
        body = (acl.model_dump(exclude_defaults=exclude_defaults)
                if is_pydantic_model(acl) else acl)
        url = self.gen_url(f"users/{user_id}/acl/{object_type}/{object_key}/")
        resp = self._put(url, json=body, **kwargs)
        return self.parse_response(resp, UserACLSchema)

    def delete_user_acl(
        self,
        user_id: str,
        object_type: str,
        object_key: str,
        **kwargs,
    ) -> Response:
        """
        Delete a user ACL for an object

        Args:
            user_id: ID of the user
            object_type: Type of the object
            object_key: ID of the object
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=None)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
            - 404 ACL does not exist
        """
        url = self.gen_url(f"users/{user_id}/acl/{object_type}/{object_key}/")
        resp = self._delete(url, **kwargs)
        return self.parse_response(resp, None)

    def check_user_permission(
        self,
        user_id: str,
        object_type: str,
        object_key: str,
        permission: str,
        **kwargs,
    ) -> Response:
        """
        Returns a user ACL for an object

        Args:
            user_id: ID of the user
            object_type: Type of the object
            object_key: ID of the object
            permission: Permission to check
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=UserACLSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
            - 403 User does not have permission
        """
        url = self.gen_url(f"users/{user_id}/acl/{object_type}/{object_key}/"
                           f"{permission}/")
        resp = self._get(url, **kwargs)
        return self.parse_response(resp, UserACLSchema)

    def list_share_acls(
        self,
        object_type: str,
        object_key: str,
        **kwargs,
    ) -> Response:
        """
        List of share ACLs

        Args:
            object_type: Type of the object
            object_key: ID of the object
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=SharesACLSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        url = self.gen_url(f"shares/{object_type}/{object_key}/")
        resp = self._get(url, **kwargs)
        return self.parse_response(resp, SharesACLSchema)

    def create_share_acls(
        self,
        share_id: str,
        object_type: str,
        acls: Union[CreateShareACLsSchema, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Create a new ACL for multiple share objects

        Args:
            share_id: ID of the share
            object_type: Type of the object
            acls: Share ACLs data (either as CreateShareACLsSchema or dict)
            exclude_defaults: Whether to exclude default values when dumping
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=CreateACLsResultSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        body = (acls.model_dump(exclude_defaults=exclude_defaults)
                if is_pydantic_model(acls) else acls)
        url = self.gen_url(f"shares/{share_id}/acl/{object_type}/")
        resp = self._put(url, json=body, **kwargs)
        return self.parse_response(resp, CreateACLsResultSchema)

    def get_share_acl(
        self,
        share_id: str,
        object_type: str,
        object_key: str,
        **kwargs,
    ) -> Response:
        """
        List of share permissions for an object

        Args:
            share_id: ID of the share
            object_type: Type of the object
            object_key: ID of the object
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=ShareACLSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        url = self.gen_url(f"shares/{share_id}/acl/{object_type}/"
                           f"{object_key}/")
        resp = self._get(url, **kwargs)
        return self.parse_response(resp, ShareACLSchema)

    def create_share_acl(
        self,
        share_id: str,
        object_type: str,
        object_key: str,
        acl: Union[ShareACLSchema, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Create a new share ACL for an object

        Args:
            share_id: ID of the share
            object_type: Type of the object
            object_key: ID of the object
            acl: Share ACL data (either as ShareACLSchema or dict)
            exclude_defaults: Whether to exclude default values when dumping
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=ShareACLSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        body = (acl.model_dump(exclude_defaults=exclude_defaults)
                if is_pydantic_model(acl) else acl)
        url = self.gen_url(f"shares/{share_id}/acl/{object_type}/"
                           f"{object_key}/")
        resp = self._post(url, json=body, **kwargs)
        return self.parse_response(resp, ShareACLSchema)

    def update_share_acl(
        self,
        share_id: str,
        object_type: str,
        object_key: str,
        acl: Union[ShareACLSchema, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Update share ACL for an object

        Args:
            share_id: ID of the share
            object_type: Type of the object
            object_key: ID of the object
            acl: Share ACL data (either as ShareACLSchema or dict)
            exclude_defaults: Whether to exclude default values when dumping
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=ShareACLSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
            - 404 ACL does not exist
        """
        body = (acl.model_dump(exclude_defaults=exclude_defaults)
                if is_pydantic_model(acl) else acl)
        url = self.gen_url(f"shares/{share_id}/acl/{object_type}/"
                           f"{object_key}/")
        resp = self._put(url, json=body, **kwargs)
        return self.parse_response(resp, ShareACLSchema)

    def delete_share_acl(
        self,
        share_id: str,
        object_type: str,
        object_key: str,
        **kwargs,
    ) -> Response:
        """
        Delete a share ACL for an object

        Args:
            share_id: ID of the share
            object_type: Type of the object
            object_key: ID of the object
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=None)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
            - 404 ACL does not exist
        """
        url = self.gen_url(f"shares/{share_id}/acl/{object_type}/"
                           f"{object_key}/")
        resp = self._delete(url, **kwargs)
        return self.parse_response(resp, None)

    def check_share_permission(
        self,
        share_id: str,
        object_type: str,
        object_key: str,
        permission: str,
        **kwargs,
    ) -> Response:
        """
        Returns a share ACL for an object

        Args:
            share_id: ID of the share
            object_type: Type of the object
            object_key: ID of the object
            permission: Permission to check
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=None)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
            - 403 User does not have permission
        """
        url = self.gen_url(f"shares/{share_id}/acl/{object_type}/"
                           f"{object_key}/{permission}/")
        resp = self._get(url, **kwargs)
        return self.parse_response(resp, None)
