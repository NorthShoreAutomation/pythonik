"""
Iconik Acls Models
This module contains Pydantic models for the Iconik Acls API.
"""

from __future__ import annotations

from datetime import datetime
from typing import (
    List,
    Literal,
    Optional,
)

from pydantic import (
    BaseModel,
    Field,
)


class UsersSchema(BaseModel):
    """Represents a UsersSchema in the Iconik system."""

    users: Optional[List["UsersCheckAclSchema"]] = Field(default_factory=list)


class UsersCheckAclSchema(BaseModel):
    """Represents a UsersCheckAclSchema in the Iconik system."""

    group_ids: Optional[List[str]] = Field(default_factory=list)
    user_id: Optional[str] = None


class UserIDsSchema(BaseModel):
    """Represents a UserIDsSchema in the Iconik system."""

    user_ids: Optional[List[str]] = Field(default_factory=list)


class UserACLSchema(BaseModel):
    """Represents a UserACLSchema in the Iconik system."""

    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    object_key: Optional[str] = None
    object_type: Optional[str] = None
    permissions: List[str]
    user_id: Optional[str] = None


class UserACLBaseSchema(BaseModel):
    """Represents a UserACLBaseSchema in the Iconik system."""

    permissions: List[str]
    user_id: Optional[str] = None


class SharesACLSchema(BaseModel):
    """Represents a SharesACLSchema in the Iconik system."""

    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[List["ShareACLSchema"]] = Field(default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    total: Optional[int] = Field(None,
                                 ge=-9223372036854775808,
                                 le=9223372036854775807)


class ShareACLSchema(BaseModel):
    """Represents a ShareACLSchema in the Iconik system."""

    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    object_key: Optional[str] = None
    object_type: Optional[str] = None
    permissions: List[str]
    share_id: Optional[str] = None


class ReindexPropagatingACLSchema(BaseModel):
    """Represents a ReindexPropagatingACLSchema in the Iconik system."""

    sync_to_another_dc: Optional[bool] = None


class PropagatingGroupACLSchema(BaseModel):
    """Represents a PropagatingGroupACLSchema in the Iconik system."""

    group_id: Optional[str] = None
    object_key: Optional[str] = None
    object_type: Optional[str] = None
    permissions: List[str]


class PropagatingACLSchema(BaseModel):
    """Represents a PropagatingACLSchema in the Iconik system."""

    object_key: Optional[str] = None
    object_type: Optional[str] = None
    permissions: List[str]
    user_id: Optional[str] = None


class ListObjectsSchema(BaseModel):
    """Represents a ListObjectsSchema in the Iconik system."""

    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    total: Optional[int] = Field(None,
                                 ge=-9223372036854775808,
                                 le=9223372036854775807)


class InheritedACLSchema(BaseModel):
    """Represents a InheritedACLSchema in the Iconik system."""

    collection_ids: List[str]
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    object_key: Optional[str] = None
    object_type: Optional[str] = None


class GroupIDsSchema(BaseModel):
    """Represents a GroupIDsSchema in the Iconik system."""

    group_ids: Optional[List[str]] = Field(default_factory=list)


class GroupACLSchema(BaseModel):
    """Represents a GroupACLSchema in the Iconik system."""

    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    group_id: Optional[str] = None
    object_key: Optional[str] = None
    object_type: Optional[str] = None
    permissions: List[str]


class GroupACLBaseSchema(BaseModel):
    """Represents a GroupACLBaseSchema in the Iconik system."""

    group_id: Optional[str] = None
    permissions: List[str]


class DeleteBulkACLsSchema(BaseModel):
    """Represents a DeleteBulkACLsSchema in the Iconik system."""

    group_ids: Optional[List[str]] = Field(default_factory=list)
    include_assets: bool
    include_collections: bool
    object_ids: Optional[List[str]] = Field(default_factory=list)
    object_type: Optional[str] = None
    user_ids: Optional[List[str]] = Field(default_factory=list)


class DeleteACLsSchema(BaseModel):
    """Represents a DeleteACLsSchema in the Iconik system."""

    group_ids: Optional[List[str]] = Field(default_factory=list)
    object_keys: Optional[List[str]] = Field(default_factory=list)
    object_type: Optional[str] = None
    user_ids: Optional[List[str]] = Field(default_factory=list)


class CreateShareACLsSchema(BaseModel):
    """Represents a CreateShareACLsSchema in the Iconik system."""

    object_keys: Optional[List[str]] = Field(default_factory=list)
    object_type: Optional[str] = None
    permissions: List[str]
    share_id: Optional[str] = None


class CreateMultipleACLsSchema(BaseModel):
    """Represents a CreateMultipleACLsSchema in the Iconik system."""

    objects: List["CreateACLsSchemaMultiple"]


class CreateBulkACLsSchema(BaseModel):
    """Represents a CreateBulkACLsSchema in the Iconik system."""

    group_ids: Optional[List[str]] = Field(default_factory=list)
    include_assets: bool
    include_collections: bool
    mode: Optional[Literal["APPEND", "OVERWRITE"]] = None
    object_ids: Optional[List[str]] = Field(default_factory=list)
    object_type: Optional[str] = None
    permissions: List[str]
    user_ids: Optional[List[str]] = Field(default_factory=list)


class CreateACLsSchemaMultiple(BaseModel):
    """Represents a CreateACLsSchemaMultiple in the Iconik system."""

    group_ids: Optional[List[str]] = Field(default_factory=list)
    mode: Optional[Literal["APPEND", "OVERWRITE"]] = None
    object_keys: List[str]
    object_type: Optional[str] = None
    permissions: List[str]
    user_ids: Optional[List[str]] = Field(default_factory=list)


class CreateACLsSchema(BaseModel):
    """Represents a CreateACLsSchema in the Iconik system."""

    group_ids: Optional[List[str]] = Field(default_factory=list)
    mode: Optional[Literal["APPEND", "OVERWRITE"]] = None
    object_keys: List[str]
    object_type: Optional[str] = None
    permissions: List[str]
    user_ids: Optional[List[str]] = Field(default_factory=list)


class CreateACLsResultSchema(BaseModel):
    """Represents a CreateACLsResultSchema in the Iconik system."""

    updated_object_keys: Optional[List[str]] = Field(default_factory=list)


class CopyInheritedACLSchema(BaseModel):
    """Represents a CopyInheritedACLSchema in the Iconik system."""

    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    from_collection_ids: List[str]
    object_key: str
    object_type: str


class CombinedPermissionsSchema(BaseModel):
    """Represents a CombinedPermissionsSchema in the Iconik system."""

    permissions: Optional[List[str]] = Field(default_factory=list)


class CheckBulkACLsSchema(BaseModel):
    """Represents a CheckBulkACLsSchema in the Iconik system."""

    objects: List["BulkACLsObjectSchema"]


class BulkDeleteShareACLs(BaseModel):
    """Represents a BulkDeleteShareACLs in the Iconik system."""

    share_ids: List[str]


class BulkCreateShareACLs(BaseModel):
    """Represents a BulkCreateShareACLs in the Iconik system."""

    permissions: List[str]
    share_ids: List[str]


class BulkACLsObjectSchema(BaseModel):
    """Represents a BulkACLsObjectSchema in the Iconik system."""

    object_keys: List[str]
    object_type: str
    permissions: List[Literal["read", "write", "delete", "change-acl"]]


class BulkACLSchema(BaseModel):
    """Represents a BulkACLSchema in the Iconik system."""

    access_denied: Optional[List[str]] = Field(default_factory=list)
    access_granted: Optional[List[str]] = Field(default_factory=list)


class ACLsSchema(BaseModel):
    """Represents a ACLsSchema in the Iconik system."""

    object_keys: Optional[List[str]] = Field(default_factory=list)


class ACLTemplatesSchema(BaseModel):
    """Represents a ACLTemplatesSchema in the Iconik system."""

    objects: Optional[List["ACLTemplateSchema"]] = Field(default_factory=list)


class ACLTemplateSchema(BaseModel):
    """Represents a ACLTemplateSchema in the Iconik system."""

    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    id: Optional[str] = None
    name: str


class ACLSchema(BaseModel):
    """Represents a ACLSchema in the Iconik system."""

    groups_acl: Optional[List["GroupACLBase"]] = Field(default_factory=list)
    inherited_groups_acl: Optional[List["PropagatingGroupACL"]] = Field(
        default_factory=list)
    inherited_users_acl: Optional[List["PropagatingACL"]] = Field(
        default_factory=list)
    propagating_groups_acl: Optional[List["PropagatingGroupACL"]] = Field(
        default_factory=list)
    propagating_users_acl: Optional[List["PropagatingACL"]] = Field(
        default_factory=list)
    users_acl: Optional[List["UserACLBase"]] = Field(default_factory=list)


class PropagatingGroupACL(BaseModel):
    """Represents a PropagatingGroupACL in the Iconik system."""

    group_id: Optional[str] = None
    object_key: Optional[str] = None
    object_type: Optional[str] = None
    permissions: List[str]


class PropagatingACL(BaseModel):
    """Represents a PropagatingACL in the Iconik system."""

    object_key: Optional[str] = None
    object_type: Optional[str] = None
    permissions: List[str]
    user_id: Optional[str] = None


class UserACLBase(BaseModel):
    """Represents a UserACLBase in the Iconik system."""

    permissions: List[str]
    user_id: Optional[str] = None


class GroupACLBase(BaseModel):
    """Represents a GroupACLBase in the Iconik system."""

    group_id: Optional[str] = None
    permissions: List[str]


# Update forward references
UsersSchema.model_rebuild()
UsersCheckAclSchema.model_rebuild()
UserIDsSchema.model_rebuild()
UserACLSchema.model_rebuild()
UserACLBaseSchema.model_rebuild()
SharesACLSchema.model_rebuild()
ShareACLSchema.model_rebuild()
ReindexPropagatingACLSchema.model_rebuild()
PropagatingGroupACLSchema.model_rebuild()
PropagatingACLSchema.model_rebuild()
ListObjectsSchema.model_rebuild()
InheritedACLSchema.model_rebuild()
GroupIDsSchema.model_rebuild()
GroupACLSchema.model_rebuild()
GroupACLBaseSchema.model_rebuild()
DeleteBulkACLsSchema.model_rebuild()
DeleteACLsSchema.model_rebuild()
CreateShareACLsSchema.model_rebuild()
CreateMultipleACLsSchema.model_rebuild()
CreateBulkACLsSchema.model_rebuild()
CreateACLsSchemaMultiple.model_rebuild()
CreateACLsSchema.model_rebuild()
CreateACLsResultSchema.model_rebuild()
CopyInheritedACLSchema.model_rebuild()
CombinedPermissionsSchema.model_rebuild()
CheckBulkACLsSchema.model_rebuild()
BulkDeleteShareACLs.model_rebuild()
BulkCreateShareACLs.model_rebuild()
BulkACLsObjectSchema.model_rebuild()
BulkACLSchema.model_rebuild()
ACLsSchema.model_rebuild()
ACLTemplatesSchema.model_rebuild()
ACLTemplateSchema.model_rebuild()
ACLSchema.model_rebuild()
PropagatingGroupACL.model_rebuild()
PropagatingACL.model_rebuild()
UserACLBase.model_rebuild()
GroupACLBase.model_rebuild()
