"""Contains all the data models used in inputs/outputs"""

from .ac_ls_schema import ACLsSchema
from .acl_schema import ACLSchema
from .acl_template_schema import ACLTemplateSchema
from .acl_templates_schema import ACLTemplatesSchema
from .bulk_ac_ls_object_schema import BulkACLsObjectSchema
from .bulk_ac_ls_object_schema_permissions_item import (
    BulkACLsObjectSchemaPermissionsItem,
)
from .bulk_acl_schema import BulkACLSchema
from .bulk_create_share_ac_ls import BulkCreateShareACLs
from .bulk_delete_share_ac_ls import BulkDeleteShareACLs
from .check_bulk_ac_ls_schema import CheckBulkACLsSchema
from .combined_permissions_schema import CombinedPermissionsSchema
from .copy_inherited_acl_schema import CopyInheritedACLSchema
from .create_ac_ls_result_schema import CreateACLsResultSchema
from .create_ac_ls_schema import CreateACLsSchema
from .create_ac_ls_schema_mode import CreateACLsSchemaMode
from .create_ac_ls_schema_multiple import CreateACLsSchemaMultiple
from .create_ac_ls_schema_multiple_mode import CreateACLsSchemaMultipleMode
from .create_bulk_ac_ls_schema import CreateBulkACLsSchema
from .create_bulk_ac_ls_schema_mode import CreateBulkACLsSchemaMode
from .create_multiple_ac_ls_schema import CreateMultipleACLsSchema
from .create_share_ac_ls_schema import CreateShareACLsSchema
from .delete_ac_ls_schema import DeleteACLsSchema
from .delete_acl_by_object_type_content_response_default_type_0 import (
    DeleteAclByObjectTypeContentResponseDefaultType0,
)
from .delete_acl_by_object_type_content_response_default_type_1 import (
    DeleteAclByObjectTypeContentResponseDefaultType1,
)
from .delete_acl_by_object_type_content_response_default_type_1_errors import (
    DeleteAclByObjectTypeContentResponseDefaultType1Errors,
)
from .delete_acl_by_object_type_response_default_type_0 import (
    DeleteAclByObjectTypeResponseDefaultType0,
)
from .delete_acl_by_object_type_response_default_type_1 import (
    DeleteAclByObjectTypeResponseDefaultType1,
)
from .delete_acl_by_object_type_response_default_type_1_errors import (
    DeleteAclByObjectTypeResponseDefaultType1Errors,
)
from .delete_acl_templates_by_template_id_response_default_type_0 import (
    DeleteAclTemplatesByTemplateIdResponseDefaultType0,
)
from .delete_acl_templates_by_template_id_response_default_type_1 import (
    DeleteAclTemplatesByTemplateIdResponseDefaultType1,
)
from .delete_acl_templates_by_template_id_response_default_type_1_errors import (
    DeleteAclTemplatesByTemplateIdResponseDefaultType1Errors,
)
from .delete_bulk_ac_ls_schema import DeleteBulkACLsSchema
from .delete_groups_by_group_id_acl_by_object_type_by_object_key_response_default_type_0 import (
    DeleteGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType0,
)
from .delete_groups_by_group_id_acl_by_object_type_by_object_key_response_default_type_1 import (
    DeleteGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType1,
)
from .delete_groups_by_group_id_acl_by_object_type_by_object_key_response_default_type_1_errors import (
    DeleteGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType1Errors,
)
from .delete_shares_by_share_id_acl_by_object_type_by_object_key_response_default_type_0 import (
    DeleteSharesByShareIdAclByObjectTypeByObjectKeyResponseDefaultType0,
)
from .delete_shares_by_share_id_acl_by_object_type_by_object_key_response_default_type_1 import (
    DeleteSharesByShareIdAclByObjectTypeByObjectKeyResponseDefaultType1,
)
from .delete_shares_by_share_id_acl_by_object_type_by_object_key_response_default_type_1_errors import (
    DeleteSharesByShareIdAclByObjectTypeByObjectKeyResponseDefaultType1Errors,
)
from .delete_users_by_user_id_acl_by_object_type_by_object_key_response_default_type_0 import (
    DeleteUsersByUserIdAclByObjectTypeByObjectKeyResponseDefaultType0,
)
from .delete_users_by_user_id_acl_by_object_type_by_object_key_response_default_type_1 import (
    DeleteUsersByUserIdAclByObjectTypeByObjectKeyResponseDefaultType1,
)
from .delete_users_by_user_id_acl_by_object_type_by_object_key_response_default_type_1_errors import (
    DeleteUsersByUserIdAclByObjectTypeByObjectKeyResponseDefaultType1Errors,
)
from .get_acl_by_object_type_by_object_key_by_permission_response_default_type_0 import (
    GetAclByObjectTypeByObjectKeyByPermissionResponseDefaultType0,
)
from .get_acl_by_object_type_by_object_key_by_permission_response_default_type_1 import (
    GetAclByObjectTypeByObjectKeyByPermissionResponseDefaultType1,
)
from .get_acl_by_object_type_by_object_key_by_permission_response_default_type_1_errors import (
    GetAclByObjectTypeByObjectKeyByPermissionResponseDefaultType1Errors,
)
from .get_acl_by_object_type_by_object_key_permissions_response_default_type_0 import (
    GetAclByObjectTypeByObjectKeyPermissionsResponseDefaultType0,
)
from .get_acl_by_object_type_by_object_key_permissions_response_default_type_1 import (
    GetAclByObjectTypeByObjectKeyPermissionsResponseDefaultType1,
)
from .get_acl_by_object_type_by_object_key_permissions_response_default_type_1_errors import (
    GetAclByObjectTypeByObjectKeyPermissionsResponseDefaultType1Errors,
)
from .get_acl_by_object_type_by_object_key_response_default_type_0 import (
    GetAclByObjectTypeByObjectKeyResponseDefaultType0,
)
from .get_acl_by_object_type_by_object_key_response_default_type_1 import (
    GetAclByObjectTypeByObjectKeyResponseDefaultType1,
)
from .get_acl_by_object_type_by_object_key_response_default_type_1_errors import (
    GetAclByObjectTypeByObjectKeyResponseDefaultType1Errors,
)
from .get_acl_templates_by_template_id_response_default_type_0 import (
    GetAclTemplatesByTemplateIdResponseDefaultType0,
)
from .get_acl_templates_by_template_id_response_default_type_1 import (
    GetAclTemplatesByTemplateIdResponseDefaultType1,
)
from .get_acl_templates_by_template_id_response_default_type_1_errors import (
    GetAclTemplatesByTemplateIdResponseDefaultType1Errors,
)
from .get_acl_templates_response_default_type_0 import (
    GetAclTemplatesResponseDefaultType0,
)
from .get_acl_templates_response_default_type_1 import (
    GetAclTemplatesResponseDefaultType1,
)
from .get_acl_templates_response_default_type_1_errors import (
    GetAclTemplatesResponseDefaultType1Errors,
)
from .get_groups_by_group_id_acl_by_object_type_by_object_key_by_permission_response_default_type_0 import (
    GetGroupsByGroupIdAclByObjectTypeByObjectKeyByPermissionResponseDefaultType0,
)
from .get_groups_by_group_id_acl_by_object_type_by_object_key_by_permission_response_default_type_1 import (
    GetGroupsByGroupIdAclByObjectTypeByObjectKeyByPermissionResponseDefaultType1,
)
from .get_groups_by_group_id_acl_by_object_type_by_object_key_by_permission_response_default_type_1_errors import (
    GetGroupsByGroupIdAclByObjectTypeByObjectKeyByPermissionResponseDefaultType1Errors,
)
from .get_groups_by_group_id_acl_by_object_type_by_object_key_response_default_type_0 import (
    GetGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType0,
)
from .get_groups_by_group_id_acl_by_object_type_by_object_key_response_default_type_1 import (
    GetGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType1,
)
from .get_groups_by_group_id_acl_by_object_type_by_object_key_response_default_type_1_errors import (
    GetGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType1Errors,
)
from .get_shares_by_object_type_by_object_key_response_default_type_0 import (
    GetSharesByObjectTypeByObjectKeyResponseDefaultType0,
)
from .get_shares_by_object_type_by_object_key_response_default_type_1 import (
    GetSharesByObjectTypeByObjectKeyResponseDefaultType1,
)
from .get_shares_by_object_type_by_object_key_response_default_type_1_errors import (
    GetSharesByObjectTypeByObjectKeyResponseDefaultType1Errors,
)
from .get_shares_by_share_id_acl_by_object_type_by_object_key_by_permission_response_default_type_0 import (
    GetSharesByShareIdAclByObjectTypeByObjectKeyByPermissionResponseDefaultType0,
)
from .get_shares_by_share_id_acl_by_object_type_by_object_key_by_permission_response_default_type_1 import (
    GetSharesByShareIdAclByObjectTypeByObjectKeyByPermissionResponseDefaultType1,
)
from .get_shares_by_share_id_acl_by_object_type_by_object_key_by_permission_response_default_type_1_errors import (
    GetSharesByShareIdAclByObjectTypeByObjectKeyByPermissionResponseDefaultType1Errors,
)
from .get_shares_by_share_id_acl_by_object_type_by_object_key_response_default_type_0 import (
    GetSharesByShareIdAclByObjectTypeByObjectKeyResponseDefaultType0,
)
from .get_shares_by_share_id_acl_by_object_type_by_object_key_response_default_type_1 import (
    GetSharesByShareIdAclByObjectTypeByObjectKeyResponseDefaultType1,
)
from .get_shares_by_share_id_acl_by_object_type_by_object_key_response_default_type_1_errors import (
    GetSharesByShareIdAclByObjectTypeByObjectKeyResponseDefaultType1Errors,
)
from .get_users_by_user_id_acl_by_object_type_by_object_key_by_permission_response_default_type_0 import (
    GetUsersByUserIdAclByObjectTypeByObjectKeyByPermissionResponseDefaultType0,
)
from .get_users_by_user_id_acl_by_object_type_by_object_key_by_permission_response_default_type_1 import (
    GetUsersByUserIdAclByObjectTypeByObjectKeyByPermissionResponseDefaultType1,
)
from .get_users_by_user_id_acl_by_object_type_by_object_key_by_permission_response_default_type_1_errors import (
    GetUsersByUserIdAclByObjectTypeByObjectKeyByPermissionResponseDefaultType1Errors,
)
from .get_users_by_user_id_acl_by_object_type_by_object_key_response_default_type_0 import (
    GetUsersByUserIdAclByObjectTypeByObjectKeyResponseDefaultType0,
)
from .get_users_by_user_id_acl_by_object_type_by_object_key_response_default_type_1 import (
    GetUsersByUserIdAclByObjectTypeByObjectKeyResponseDefaultType1,
)
from .get_users_by_user_id_acl_by_object_type_by_object_key_response_default_type_1_errors import (
    GetUsersByUserIdAclByObjectTypeByObjectKeyResponseDefaultType1Errors,
)
from .group_acl_base import GroupACLBase
from .group_acl_base_schema import GroupACLBaseSchema
from .group_acl_schema import GroupACLSchema
from .group_i_ds_schema import GroupIDsSchema
from .inherited_acl_schema import InheritedACLSchema
from .list_objects_schema import ListObjectsSchema
from .patch_acl_templates_by_template_id_response_default_type_0 import (
    PatchAclTemplatesByTemplateIdResponseDefaultType0,
)
from .patch_acl_templates_by_template_id_response_default_type_1 import (
    PatchAclTemplatesByTemplateIdResponseDefaultType1,
)
from .patch_acl_templates_by_template_id_response_default_type_1_errors import (
    PatchAclTemplatesByTemplateIdResponseDefaultType1Errors,
)
from .post_acl_by_object_type_by_permission_response_default_type_0 import (
    PostAclByObjectTypeByPermissionResponseDefaultType0,
)
from .post_acl_by_object_type_by_permission_response_default_type_1 import (
    PostAclByObjectTypeByPermissionResponseDefaultType1,
)
from .post_acl_by_object_type_by_permission_response_default_type_1_errors import (
    PostAclByObjectTypeByPermissionResponseDefaultType1Errors,
)
from .post_acl_response_default_type_0 import PostAclResponseDefaultType0
from .post_acl_response_default_type_1 import PostAclResponseDefaultType1
from .post_acl_response_default_type_1_errors import PostAclResponseDefaultType1Errors
from .post_acl_templates_by_template_id_by_object_type_by_object_key_response_default_type_0 import (
    PostAclTemplatesByTemplateIdByObjectTypeByObjectKeyResponseDefaultType0,
)
from .post_acl_templates_by_template_id_by_object_type_by_object_key_response_default_type_1 import (
    PostAclTemplatesByTemplateIdByObjectTypeByObjectKeyResponseDefaultType1,
)
from .post_acl_templates_by_template_id_by_object_type_by_object_key_response_default_type_1_errors import (
    PostAclTemplatesByTemplateIdByObjectTypeByObjectKeyResponseDefaultType1Errors,
)
from .post_acl_templates_response_default_type_0 import (
    PostAclTemplatesResponseDefaultType0,
)
from .post_acl_templates_response_default_type_1 import (
    PostAclTemplatesResponseDefaultType1,
)
from .post_acl_templates_response_default_type_1_errors import (
    PostAclTemplatesResponseDefaultType1Errors,
)
from .post_shares_by_share_id_acl_by_object_type_by_object_key_response_default_type_0 import (
    PostSharesByShareIdAclByObjectTypeByObjectKeyResponseDefaultType0,
)
from .post_shares_by_share_id_acl_by_object_type_by_object_key_response_default_type_1 import (
    PostSharesByShareIdAclByObjectTypeByObjectKeyResponseDefaultType1,
)
from .post_shares_by_share_id_acl_by_object_type_by_object_key_response_default_type_1_errors import (
    PostSharesByShareIdAclByObjectTypeByObjectKeyResponseDefaultType1Errors,
)
from .propagating_acl import PropagatingACL
from .propagating_acl_schema import PropagatingACLSchema
from .propagating_group_acl import PropagatingGroupACL
from .propagating_group_acl_schema import PropagatingGroupACLSchema
from .put_acl_by_object_type_bulk_response_default_type_0 import (
    PutAclByObjectTypeBulkResponseDefaultType0,
)
from .put_acl_by_object_type_bulk_response_default_type_1 import (
    PutAclByObjectTypeBulkResponseDefaultType1,
)
from .put_acl_by_object_type_bulk_response_default_type_1_errors import (
    PutAclByObjectTypeBulkResponseDefaultType1Errors,
)
from .put_acl_by_object_type_content_response_default_type_0 import (
    PutAclByObjectTypeContentResponseDefaultType0,
)
from .put_acl_by_object_type_content_response_default_type_1 import (
    PutAclByObjectTypeContentResponseDefaultType1,
)
from .put_acl_by_object_type_content_response_default_type_1_errors import (
    PutAclByObjectTypeContentResponseDefaultType1Errors,
)
from .put_acl_by_object_type_response_default_type_0 import (
    PutAclByObjectTypeResponseDefaultType0,
)
from .put_acl_by_object_type_response_default_type_1 import (
    PutAclByObjectTypeResponseDefaultType1,
)
from .put_acl_by_object_type_response_default_type_1_errors import (
    PutAclByObjectTypeResponseDefaultType1Errors,
)
from .put_acl_templates_by_template_id_response_default_type_0 import (
    PutAclTemplatesByTemplateIdResponseDefaultType0,
)
from .put_acl_templates_by_template_id_response_default_type_1 import (
    PutAclTemplatesByTemplateIdResponseDefaultType1,
)
from .put_acl_templates_by_template_id_response_default_type_1_errors import (
    PutAclTemplatesByTemplateIdResponseDefaultType1Errors,
)
from .put_groups_by_group_id_acl_by_object_type_by_object_key_response_default_type_0 import (
    PutGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType0,
)
from .put_groups_by_group_id_acl_by_object_type_by_object_key_response_default_type_1 import (
    PutGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType1,
)
from .put_groups_by_group_id_acl_by_object_type_by_object_key_response_default_type_1_errors import (
    PutGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType1Errors,
)
from .put_shares_by_share_id_acl_by_object_type_by_object_key_response_default_type_0 import (
    PutSharesByShareIdAclByObjectTypeByObjectKeyResponseDefaultType0,
)
from .put_shares_by_share_id_acl_by_object_type_by_object_key_response_default_type_1 import (
    PutSharesByShareIdAclByObjectTypeByObjectKeyResponseDefaultType1,
)
from .put_shares_by_share_id_acl_by_object_type_by_object_key_response_default_type_1_errors import (
    PutSharesByShareIdAclByObjectTypeByObjectKeyResponseDefaultType1Errors,
)
from .put_shares_by_share_id_acl_by_object_type_response_default_type_0 import (
    PutSharesByShareIdAclByObjectTypeResponseDefaultType0,
)
from .put_shares_by_share_id_acl_by_object_type_response_default_type_1 import (
    PutSharesByShareIdAclByObjectTypeResponseDefaultType1,
)
from .put_shares_by_share_id_acl_by_object_type_response_default_type_1_errors import (
    PutSharesByShareIdAclByObjectTypeResponseDefaultType1Errors,
)
from .put_users_by_user_id_acl_by_object_type_by_object_key_response_default_type_0 import (
    PutUsersByUserIdAclByObjectTypeByObjectKeyResponseDefaultType0,
)
from .put_users_by_user_id_acl_by_object_type_by_object_key_response_default_type_1 import (
    PutUsersByUserIdAclByObjectTypeByObjectKeyResponseDefaultType1,
)
from .put_users_by_user_id_acl_by_object_type_by_object_key_response_default_type_1_errors import (
    PutUsersByUserIdAclByObjectTypeByObjectKeyResponseDefaultType1Errors,
)
from .reindex_propagating_acl_schema import ReindexPropagatingACLSchema
from .share_acl_schema import ShareACLSchema
from .shares_acl_schema import SharesACLSchema
from .user_acl_base import UserACLBase
from .user_acl_base_schema import UserACLBaseSchema
from .user_acl_schema import UserACLSchema
from .user_i_ds_schema import UserIDsSchema
from .users_check_acl_schema import UsersCheckAclSchema
from .users_schema import UsersSchema

__all__ = (
    "ACLSchema",
    "ACLsSchema",
    "ACLTemplateSchema",
    "ACLTemplatesSchema",
    "BulkACLSchema",
    "BulkACLsObjectSchema",
    "BulkACLsObjectSchemaPermissionsItem",
    "BulkCreateShareACLs",
    "BulkDeleteShareACLs",
    "CheckBulkACLsSchema",
    "CombinedPermissionsSchema",
    "CopyInheritedACLSchema",
    "CreateACLsResultSchema",
    "CreateACLsSchema",
    "CreateACLsSchemaMode",
    "CreateACLsSchemaMultiple",
    "CreateACLsSchemaMultipleMode",
    "CreateBulkACLsSchema",
    "CreateBulkACLsSchemaMode",
    "CreateMultipleACLsSchema",
    "CreateShareACLsSchema",
    "DeleteAclByObjectTypeContentResponseDefaultType0",
    "DeleteAclByObjectTypeContentResponseDefaultType1",
    "DeleteAclByObjectTypeContentResponseDefaultType1Errors",
    "DeleteAclByObjectTypeResponseDefaultType0",
    "DeleteAclByObjectTypeResponseDefaultType1",
    "DeleteAclByObjectTypeResponseDefaultType1Errors",
    "DeleteACLsSchema",
    "DeleteAclTemplatesByTemplateIdResponseDefaultType0",
    "DeleteAclTemplatesByTemplateIdResponseDefaultType1",
    "DeleteAclTemplatesByTemplateIdResponseDefaultType1Errors",
    "DeleteBulkACLsSchema",
    "DeleteGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType0",
    "DeleteGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType1",
    "DeleteGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType1Errors",
    "DeleteSharesByShareIdAclByObjectTypeByObjectKeyResponseDefaultType0",
    "DeleteSharesByShareIdAclByObjectTypeByObjectKeyResponseDefaultType1",
    "DeleteSharesByShareIdAclByObjectTypeByObjectKeyResponseDefaultType1Errors",
    "DeleteUsersByUserIdAclByObjectTypeByObjectKeyResponseDefaultType0",
    "DeleteUsersByUserIdAclByObjectTypeByObjectKeyResponseDefaultType1",
    "DeleteUsersByUserIdAclByObjectTypeByObjectKeyResponseDefaultType1Errors",
    "GetAclByObjectTypeByObjectKeyByPermissionResponseDefaultType0",
    "GetAclByObjectTypeByObjectKeyByPermissionResponseDefaultType1",
    "GetAclByObjectTypeByObjectKeyByPermissionResponseDefaultType1Errors",
    "GetAclByObjectTypeByObjectKeyPermissionsResponseDefaultType0",
    "GetAclByObjectTypeByObjectKeyPermissionsResponseDefaultType1",
    "GetAclByObjectTypeByObjectKeyPermissionsResponseDefaultType1Errors",
    "GetAclByObjectTypeByObjectKeyResponseDefaultType0",
    "GetAclByObjectTypeByObjectKeyResponseDefaultType1",
    "GetAclByObjectTypeByObjectKeyResponseDefaultType1Errors",
    "GetAclTemplatesByTemplateIdResponseDefaultType0",
    "GetAclTemplatesByTemplateIdResponseDefaultType1",
    "GetAclTemplatesByTemplateIdResponseDefaultType1Errors",
    "GetAclTemplatesResponseDefaultType0",
    "GetAclTemplatesResponseDefaultType1",
    "GetAclTemplatesResponseDefaultType1Errors",
    "GetGroupsByGroupIdAclByObjectTypeByObjectKeyByPermissionResponseDefaultType0",
    "GetGroupsByGroupIdAclByObjectTypeByObjectKeyByPermissionResponseDefaultType1",
    "GetGroupsByGroupIdAclByObjectTypeByObjectKeyByPermissionResponseDefaultType1Errors",
    "GetGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType0",
    "GetGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType1",
    "GetGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType1Errors",
    "GetSharesByObjectTypeByObjectKeyResponseDefaultType0",
    "GetSharesByObjectTypeByObjectKeyResponseDefaultType1",
    "GetSharesByObjectTypeByObjectKeyResponseDefaultType1Errors",
    "GetSharesByShareIdAclByObjectTypeByObjectKeyByPermissionResponseDefaultType0",
    "GetSharesByShareIdAclByObjectTypeByObjectKeyByPermissionResponseDefaultType1",
    "GetSharesByShareIdAclByObjectTypeByObjectKeyByPermissionResponseDefaultType1Errors",
    "GetSharesByShareIdAclByObjectTypeByObjectKeyResponseDefaultType0",
    "GetSharesByShareIdAclByObjectTypeByObjectKeyResponseDefaultType1",
    "GetSharesByShareIdAclByObjectTypeByObjectKeyResponseDefaultType1Errors",
    "GetUsersByUserIdAclByObjectTypeByObjectKeyByPermissionResponseDefaultType0",
    "GetUsersByUserIdAclByObjectTypeByObjectKeyByPermissionResponseDefaultType1",
    "GetUsersByUserIdAclByObjectTypeByObjectKeyByPermissionResponseDefaultType1Errors",
    "GetUsersByUserIdAclByObjectTypeByObjectKeyResponseDefaultType0",
    "GetUsersByUserIdAclByObjectTypeByObjectKeyResponseDefaultType1",
    "GetUsersByUserIdAclByObjectTypeByObjectKeyResponseDefaultType1Errors",
    "GroupACLBase",
    "GroupACLBaseSchema",
    "GroupACLSchema",
    "GroupIDsSchema",
    "InheritedACLSchema",
    "ListObjectsSchema",
    "PatchAclTemplatesByTemplateIdResponseDefaultType0",
    "PatchAclTemplatesByTemplateIdResponseDefaultType1",
    "PatchAclTemplatesByTemplateIdResponseDefaultType1Errors",
    "PostAclByObjectTypeByPermissionResponseDefaultType0",
    "PostAclByObjectTypeByPermissionResponseDefaultType1",
    "PostAclByObjectTypeByPermissionResponseDefaultType1Errors",
    "PostAclResponseDefaultType0",
    "PostAclResponseDefaultType1",
    "PostAclResponseDefaultType1Errors",
    "PostAclTemplatesByTemplateIdByObjectTypeByObjectKeyResponseDefaultType0",
    "PostAclTemplatesByTemplateIdByObjectTypeByObjectKeyResponseDefaultType1",
    "PostAclTemplatesByTemplateIdByObjectTypeByObjectKeyResponseDefaultType1Errors",
    "PostAclTemplatesResponseDefaultType0",
    "PostAclTemplatesResponseDefaultType1",
    "PostAclTemplatesResponseDefaultType1Errors",
    "PostSharesByShareIdAclByObjectTypeByObjectKeyResponseDefaultType0",
    "PostSharesByShareIdAclByObjectTypeByObjectKeyResponseDefaultType1",
    "PostSharesByShareIdAclByObjectTypeByObjectKeyResponseDefaultType1Errors",
    "PropagatingACL",
    "PropagatingACLSchema",
    "PropagatingGroupACL",
    "PropagatingGroupACLSchema",
    "PutAclByObjectTypeBulkResponseDefaultType0",
    "PutAclByObjectTypeBulkResponseDefaultType1",
    "PutAclByObjectTypeBulkResponseDefaultType1Errors",
    "PutAclByObjectTypeContentResponseDefaultType0",
    "PutAclByObjectTypeContentResponseDefaultType1",
    "PutAclByObjectTypeContentResponseDefaultType1Errors",
    "PutAclByObjectTypeResponseDefaultType0",
    "PutAclByObjectTypeResponseDefaultType1",
    "PutAclByObjectTypeResponseDefaultType1Errors",
    "PutAclTemplatesByTemplateIdResponseDefaultType0",
    "PutAclTemplatesByTemplateIdResponseDefaultType1",
    "PutAclTemplatesByTemplateIdResponseDefaultType1Errors",
    "PutGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType0",
    "PutGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType1",
    "PutGroupsByGroupIdAclByObjectTypeByObjectKeyResponseDefaultType1Errors",
    "PutSharesByShareIdAclByObjectTypeByObjectKeyResponseDefaultType0",
    "PutSharesByShareIdAclByObjectTypeByObjectKeyResponseDefaultType1",
    "PutSharesByShareIdAclByObjectTypeByObjectKeyResponseDefaultType1Errors",
    "PutSharesByShareIdAclByObjectTypeResponseDefaultType0",
    "PutSharesByShareIdAclByObjectTypeResponseDefaultType1",
    "PutSharesByShareIdAclByObjectTypeResponseDefaultType1Errors",
    "PutUsersByUserIdAclByObjectTypeByObjectKeyResponseDefaultType0",
    "PutUsersByUserIdAclByObjectTypeByObjectKeyResponseDefaultType1",
    "PutUsersByUserIdAclByObjectTypeByObjectKeyResponseDefaultType1Errors",
    "ReindexPropagatingACLSchema",
    "ShareACLSchema",
    "SharesACLSchema",
    "UserACLBase",
    "UserACLBaseSchema",
    "UserACLSchema",
    "UserIDsSchema",
    "UsersCheckAclSchema",
    "UsersSchema",
)
