"""Friendly-name client for the iconik API.

`Iconik` wraps every generated endpoint in a method named after its human
command name -- the same names the iconik CLI uses -- so callers never touch
operationIds, tags or per-service clients:

    from pythonik.friendly import Iconik

    ik = Iconik(app_id, auth_token)
    ik.put_asset_metadata(asset_id, view_id, body=values)

Methods take path parameters positionally, then keyword-only `body` (when the
operation has a request body) and the operation's query/header parameters.
Each returns the generated `Response[...]` wrapper unchanged.

GENERATED FILE -- do not edit (see targets/python/friendly.py).
"""

import threading

import httpx

from ._base.client import AuthenticatedClient, Client
from ._base.types import UNSET

BASE_URL = "https://app.iconik.io/API"
DEFAULT_TIMEOUT = httpx.Timeout(60.0)
#: the auth headers of an operation on iconik's global security scheme
AUTH_HEADERS = ("App-ID", "Auth-Token")


class Iconik:
    """Every iconik operation as a friendly-named method.

    One client per (service, auth scheme) is built on first use. Auth is
    iconik's two-header scheme: `Auth-Token` carries the token (no `Bearer`
    prefix), `App-ID` rides along as a default header. Operations iconik's
    specs mark unauthenticated -- the login/SAML flows -- get a client that
    sends neither header, so the wire stays exactly what the spec describes.

    Requests time out after 60s unless you pass `timeout=` (an
    `httpx.Timeout`, or `None` to wait forever).
    """

    def __init__(
        self, app_id, auth_token, *, base_url=BASE_URL, timeout=DEFAULT_TIMEOUT
    ):
        self._app_id = app_id
        self._auth_token = auth_token
        self._base_url = base_url.rstrip("/")
        self._timeout = timeout
        self._clients = {}
        self._closed = False
        self._lock = threading.Lock()

    def _client(self, service, auth=AUTH_HEADERS):
        """The client for one iconik service and auth-header set, built on first use.

        `auth` is what the operation's OpenAPI security resolves to; every
        emitted method passes its own, so it is never guessed here.
        """
        client = self._clients.get((service, auth))
        if client is None:
            # ponytail: one lock for all services; per-service locks only if
            # first-call contention ever shows up in a profile
            with self._lock:
                if self._closed:
                    raise RuntimeError("this Iconik is closed; construct a new one")
                client = self._clients.get((service, auth))
                if client is None:
                    kw = {
                        "base_url": f"{self._base_url}/{service}",
                        "timeout": self._timeout,
                        "headers": {"App-ID": self._app_id} if "App-ID" in auth else {},
                    }
                    client = (
                        AuthenticatedClient(
                            token=self._auth_token,
                            prefix="",
                            auth_header_name="Auth-Token",
                            **kw,
                        )
                        if "Auth-Token" in auth
                        else Client(**kw)
                    )
                    # build the httpx.Client, and its connection pool, under the
                    # lock as well: the generated client does it lazily and
                    # unsynchronised, so publishing the holder first would let a
                    # concurrent first call leak a second pool
                    client.get_httpx_client()
                    self._clients[(service, auth)] = client
        return client

    def close(self):
        """Close every client built so far; using this Iconik afterwards raises."""
        with self._lock:
            self._closed = True
            clients, self._clients = self._clients, {}
        for client in clients.values():
            client.get_httpx_client().close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

    def delete_acl_object(self, object_type: str, *, body):
        "Delete acls for multiple objects (DELETE /v1/acl/{object_type}/)"
        from .acls.api.acl import delete_acl_by_object_type as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("acls"), object_type=object_type, body=body
        )

    def delete_acl_object_content(self, object_type: str, *, body):
        "Delete acls for content of multiple objects (DELETE /v1/acl/{object_type}/content/)"
        from .acls.api.acl import delete_acl_by_object_type_content as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("acls"), object_type=object_type, body=body
        )

    def delete_acl_template(self, template_id: str):
        "Remove an acl template (DELETE /v1/acl/templates/{template_id}/)"
        from .acls.api.acl import delete_acl_templates_by_template_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("acls"), template_id=template_id
        )

    def delete_group_acl_object_by_object_key(
        self, group_id: str, object_type: str, object_key: str
    ):
        "Delete a particular acl by id for an object (DELETE /v1/groups/{group_id}/acl/{object_type}/{object_key}/)"
        from .acls.api.groups import (
            delete_groups_by_group_id_acl_by_object_type_by_object_key as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("acls"),
            group_id=group_id,
            object_type=object_type,
            object_key=object_key,
        )

    def delete_share_acl_object_by_object_key(
        self, share_id: str, object_type: str, object_key: str
    ):
        "Delete a share acl for an object (DELETE /v1/shares/{share_id}/acl/{object_type}/{object_key}/)"
        from .acls.api.shares import (
            delete_shares_by_share_id_acl_by_object_type_by_object_key as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("acls"),
            share_id=share_id,
            object_type=object_type,
            object_key=object_key,
        )

    def delete_user_acl_object_by_object_key(
        self, user_id: str, object_type: str, object_key: str
    ):
        "Delete a user acl for an object (DELETE /v1/users/{user_id}/acl/{object_type}/{object_key}/)"
        from .acls.api.users import (
            delete_users_by_user_id_acl_by_object_type_by_object_key as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("acls"),
            user_id=user_id,
            object_type=object_type,
            object_key=object_key,
        )

    def get_acl_object_by_object_key(
        self, object_type: str, object_key: str, *, exclude_deleted=UNSET
    ):
        "List of object permissions (GET /v1/acl/{object_type}/{object_key}/)"
        from .acls.api.acl import get_acl_by_object_type_by_object_key as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("acls"),
            object_type=object_type,
            object_key=object_key,
            exclude_deleted=exclude_deleted,
        )

    def get_acl_object_by_object_key_by_permission(
        self, object_type: str, object_key: str, permission: str
    ):
        "Check if particular object has required permission (GET /v1/acl/{object_type}/{object_key}/{permission}/)"
        from .acls.api.acl import (
            get_acl_by_object_type_by_object_key_by_permission as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("acls"),
            object_type=object_type,
            object_key=object_key,
            permission=permission,
        )

    def get_acl_object_permissions_by_object_key(
        self, object_type: str, object_key: str
    ):
        "List of permissions for the user (GET /v1/acl/{object_type}/{object_key}/permissions/)"
        from .acls.api.acl import (
            get_acl_by_object_type_by_object_key_permissions as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("acls"), object_type=object_type, object_key=object_key
        )

    def get_acl_templates(self):
        "Retreive all acl templates (GET /v1/acl/templates/)"
        from .acls.api.acl import get_acl_templates as _endpoint

        return _endpoint.sync_detailed(client=self._client("acls"))

    def get_acl_template(self, template_id: str):
        "Retreive an acl template (GET /v1/acl/templates/{template_id}/)"
        from .acls.api.acl import get_acl_templates_by_template_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("acls"), template_id=template_id
        )

    def get_group_acl_object_by_object_key(
        self, group_id: str, object_type: str, object_key: str
    ):
        "List of groups permissions for an object (GET /v1/groups/{group_id}/acl/{object_type}/{object_key}/)"
        from .acls.api.groups import (
            get_groups_by_group_id_acl_by_object_type_by_object_key as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("acls"),
            group_id=group_id,
            object_type=object_type,
            object_key=object_key,
        )

    def get_group_acl_object_by_object_key_by_permission(
        self, group_id: str, object_type: str, object_key: str, permission: str
    ):
        "Check if group has particular permission for an object (GET /v1/groups/{group_id}/acl/{object_type}/{object_key}/{permission}/)"
        from .acls.api.groups import (
            get_groups_by_group_id_acl_by_object_type_by_object_key_by_permission as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("acls"),
            group_id=group_id,
            object_type=object_type,
            object_key=object_key,
            permission=permission,
        )

    def get_shares_object_by_object_key(self, object_type: str, object_key: str):
        "List of share acls (GET /v1/shares/{object_type}/{object_key}/)"
        from .acls.api.shares import (
            get_shares_by_object_type_by_object_key as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("acls"), object_type=object_type, object_key=object_key
        )

    def get_share_acl_object_by_object_key(
        self, share_id: str, object_type: str, object_key: str
    ):
        "List of share permissions for an object (GET /v1/shares/{share_id}/acl/{object_type}/{object_key}/)"
        from .acls.api.shares import (
            get_shares_by_share_id_acl_by_object_type_by_object_key as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("acls"),
            share_id=share_id,
            object_type=object_type,
            object_key=object_key,
        )

    def get_share_acl_object_by_object_key_by_permission(
        self, share_id: str, object_type: str, object_key: str, permission: str
    ):
        "Returns a share acl for an object (GET /v1/shares/{share_id}/acl/{object_type}/{object_key}/{permission}/)"
        from .acls.api.shares import (
            get_shares_by_share_id_acl_by_object_type_by_object_key_by_permission as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("acls"),
            share_id=share_id,
            object_type=object_type,
            object_key=object_key,
            permission=permission,
        )

    def get_user_acl_object_by_object_key(
        self, user_id: str, object_type: str, object_key: str
    ):
        "List of user permissions for an object (GET /v1/users/{user_id}/acl/{object_type}/{object_key}/)"
        from .acls.api.users import (
            get_users_by_user_id_acl_by_object_type_by_object_key as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("acls"),
            user_id=user_id,
            object_type=object_type,
            object_key=object_key,
        )

    def get_user_acl_object_by_object_key_by_permission(
        self, user_id: str, object_type: str, object_key: str, permission: str
    ):
        "Returns a user acl for an object (GET /v1/users/{user_id}/acl/{object_type}/{object_key}/{permission}/)"
        from .acls.api.users import (
            get_users_by_user_id_acl_by_object_type_by_object_key_by_permission as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("acls"),
            user_id=user_id,
            object_type=object_type,
            object_key=object_key,
            permission=permission,
        )

    def patch_acl_template(self, template_id: str, *, body):
        "Update an acl template (PATCH /v1/acl/templates/{template_id}/)"
        from .acls.api.acl import patch_acl_templates_by_template_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("acls"), template_id=template_id, body=body
        )

    def post_acl(self, *, body):
        "Check if objects have required permission (POST /v1/acl/)"
        from .acls.api.acl import post_acl as _endpoint

        return _endpoint.sync_detailed(client=self._client("acls"), body=body)

    def post_acl_object_by_permission(self, object_type: str, permission: str, *, body):
        "Check if objects have required permission (POST /v1/acl/{object_type}/{permission}/)"
        from .acls.api.acl import post_acl_by_object_type_by_permission as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("acls"),
            object_type=object_type,
            permission=permission,
            body=body,
        )

    def post_acl_templates(self, *, body):
        "Create an acl template (POST /v1/acl/templates/)"
        from .acls.api.acl import post_acl_templates as _endpoint

        return _endpoint.sync_detailed(client=self._client("acls"), body=body)

    def post_acl_template_object_by_object_key(
        self,
        template_id: str,
        object_type: str,
        object_key: str,
        *,
        ignore_reindexing=UNSET,
        restrict_acls_collection_id=UNSET,
    ):
        "Apply template permissions to an object (POST /v1/acl/templates/{template_id}/{object_type}/{object_key}/)"
        from .acls.api.acl import (
            post_acl_templates_by_template_id_by_object_type_by_object_key as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("acls"),
            template_id=template_id,
            object_type=object_type,
            object_key=object_key,
            ignore_reindexing=ignore_reindexing,
            restrict_acls_collection_id=restrict_acls_collection_id,
        )

    def post_share_acl_object_by_object_key(
        self, share_id: str, object_type: str, object_key: str, *, body
    ):
        "Create a new share acl for an object (POST /v1/shares/{share_id}/acl/{object_type}/{object_key}/)"
        from .acls.api.shares import (
            post_shares_by_share_id_acl_by_object_type_by_object_key as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("acls"),
            share_id=share_id,
            object_type=object_type,
            object_key=object_key,
            body=body,
        )

    def put_acl_object(self, object_type: str, *, body):
        "Create a new acl for multiple objects (PUT /v1/acl/{object_type}/)"
        from .acls.api.acl import put_acl_by_object_type as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("acls"), object_type=object_type, body=body
        )

    def put_acl_object_bulk(self, object_type: str, *, body):
        "Create a new acl for multiple objects with multiple permissions (PUT /v1/acl/{object_type}/bulk/)"
        from .acls.api.acl import put_acl_by_object_type_bulk as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("acls"), object_type=object_type, body=body
        )

    def put_acl_object_content(self, object_type: str, *, body):
        "Create a new acl for content of multiple objects (PUT /v1/acl/{object_type}/content/)"
        from .acls.api.acl import put_acl_by_object_type_content as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("acls"), object_type=object_type, body=body
        )

    def put_acl_template(self, template_id: str, *, body):
        "Update an acl template (PUT /v1/acl/templates/{template_id}/)"
        from .acls.api.acl import put_acl_templates_by_template_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("acls"), template_id=template_id, body=body
        )

    def put_group_acl_object_by_object_key(
        self, group_id: str, object_type: str, object_key: str, *, body
    ):
        "Update or create group acl for an object (PUT /v1/groups/{group_id}/acl/{object_type}/{object_key}/)"
        from .acls.api.groups import (
            put_groups_by_group_id_acl_by_object_type_by_object_key as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("acls"),
            group_id=group_id,
            object_type=object_type,
            object_key=object_key,
            body=body,
        )

    def put_share_acl_object(self, share_id: str, object_type: str, *, body):
        "Create a new acl for multiple share objects (PUT /v1/shares/{share_id}/acl/{object_type}/)"
        from .acls.api.shares import (
            put_shares_by_share_id_acl_by_object_type as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("acls"),
            share_id=share_id,
            object_type=object_type,
            body=body,
        )

    def put_share_acl_object_by_object_key(
        self, share_id: str, object_type: str, object_key: str, *, body
    ):
        "Update share acl for an object (PUT /v1/shares/{share_id}/acl/{object_type}/{object_key}/)"
        from .acls.api.shares import (
            put_shares_by_share_id_acl_by_object_type_by_object_key as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("acls"),
            share_id=share_id,
            object_type=object_type,
            object_key=object_key,
            body=body,
        )

    def put_user_acl_object_by_object_key(
        self, user_id: str, object_type: str, object_key: str, *, body
    ):
        "Update or create user acl for an object (PUT /v1/users/{user_id}/acl/{object_type}/{object_key}/)"
        from .acls.api.users import (
            put_users_by_user_id_acl_by_object_type_by_object_key as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("acls"),
            user_id=user_id,
            object_type=object_type,
            object_key=object_key,
            body=body,
        )

    def delete_asset(self, asset_id: str):
        "Delete a particular asset by id (DELETE /v1/assets/{asset_id}/)"
        from .assets.api.assets import delete_assets_by_asset_id as _endpoint

        return _endpoint.sync_detailed(client=self._client("assets"), asset_id=asset_id)

    def delete_asset_history_by_history_entity(
        self, asset_id: str, history_entity_id: str
    ):
        "Deletes an asset history entity (DELETE /v1/assets/{asset_id}/history/{history_entity_id}/)"
        from .assets.api.assets import (
            delete_assets_by_asset_id_history_by_history_entity_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            asset_id=asset_id,
            history_entity_id=history_entity_id,
        )

    def delete_asset_purge(self, asset_id: str):
        "Purges a particular asset by id immediately (DELETE /v1/assets/{asset_id}/purge/)"
        from .assets.api.assets import delete_assets_by_asset_id_purge as _endpoint

        return _endpoint.sync_detailed(client=self._client("assets"), asset_id=asset_id)

    def delete_asset_relations_by_relation_type_by_related_to_asset(
        self, asset_id: str, relation_type: str, related_to_asset_id: str
    ):
        "Delete a particular asset by id (DELETE /v1/assets/{asset_id}/relations/{relation_type}/{related_to_asset_id}/)"
        from .assets.api.assets import (
            delete_assets_by_asset_id_relations_by_relation_type_by_related_to_asset_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            asset_id=asset_id,
            relation_type=relation_type,
            related_to_asset_id=related_to_asset_id,
        )

    def delete_asset_segments_bulk(
        self, asset_id: str, *, body, immediately=UNSET, ignore_reindexing=UNSET
    ):
        "Delete segments with either ids or by type (DELETE /v1/assets/{asset_id}/segments/bulk/)"
        from .assets.api.assets import (
            delete_assets_by_asset_id_segments_bulk as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            asset_id=asset_id,
            body=body,
            immediately=immediately,
            ignore_reindexing=ignore_reindexing,
        )

    def delete_asset_segment(
        self, asset_id: str, segment_id: str, *, soft_delete=UNSET
    ):
        "Delete a particular segment from an asset by id (DELETE /v1/assets/{asset_id}/segments/{segment_id}/)"
        from .assets.api.assets import (
            delete_assets_by_asset_id_segments_by_segment_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            asset_id=asset_id,
            segment_id=segment_id,
            soft_delete=soft_delete,
        )

    def delete_asset_uploads(self, asset_id: str):
        "Delete a particular asset by id on failed uplaod (DELETE /v1/assets/{asset_id}/uploads/)"
        from .assets.api.assets import delete_assets_by_asset_id_uploads as _endpoint

        return _endpoint.sync_detailed(client=self._client("assets"), asset_id=asset_id)

    def delete_asset_version(
        self, asset_id: str, version_id: str, *, hard_delete=UNSET
    ):
        "Delete a particular asset version by id (DELETE /v1/assets/{asset_id}/versions/{version_id}/)"
        from .assets.api.assets import (
            delete_assets_by_asset_id_versions_by_version_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            asset_id=asset_id,
            version_id=version_id,
            hard_delete=hard_delete,
        )

    def delete_asset_version_transcription_properties(
        self, asset_id: str, version_id: str, transcription_id: str
    ):
        "Delete transcription properties by ID (DELETE /v1/assets/{asset_id}/versions/{version_id}/transcriptions/{transcription_id}/properties/)"
        from .assets.api.assets import (
            delete_assets_by_asset_id_versions_by_version_id_transcriptions_by_transcription_id_properties as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            asset_id=asset_id,
            version_id=version_id,
            transcription_id=transcription_id,
        )

    def delete_asset_versions_old(self, asset_id: str):
        "Delete all asset versions except the latest one (DELETE /v1/assets/{asset_id}/versions/old/)"
        from .assets.api.assets import (
            delete_assets_by_asset_id_versions_old as _endpoint,
        )

        return _endpoint.sync_detailed(client=self._client("assets"), asset_id=asset_id)

    def delete_assets_relation_types_by_relation_type(self, relation_type: str):
        "Delete an asset relation type (DELETE /v1/assets/relation_types/{relation_type}/)"
        from .assets.api.assets import (
            delete_assets_relation_types_by_relation_type as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"), relation_type=relation_type
        )

    def delete_object_approvals(self, object_type: str, object_id: str):
        "Deletes an objects approval status (DELETE /v1/{object_type}/{object_id}/approvals/)"
        from .assets.api.object_type import (
            delete_by_object_type_by_object_id_approvals as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"), object_type=object_type, object_id=object_id
        )

    def delete_object_approvals_external_by_email(
        self, object_type: str, object_id: str, email: str
    ):
        "Deletes an objects approval status by user_id (DELETE /v1/{object_type}/{object_id}/approvals/external/{email}/)"
        from .assets.api.object_type import (
            delete_by_object_type_by_object_id_approvals_external_by_email as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            object_type=object_type,
            object_id=object_id,
            email=email,
        )

    def delete_object_approvals_request(self, object_type: str, object_id: str):
        "Deletes an objects approval request (DELETE /v1/{object_type}/{object_id}/approvals/request/)"
        from .assets.api.object_type import (
            delete_by_object_type_by_object_id_approvals_request as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"), object_type=object_type, object_id=object_id
        )

    def delete_object_approvals_user(
        self, object_type: str, object_id: str, user_id: str
    ):
        "Deletes an objects approval status by user_id (DELETE /v1/{object_type}/{object_id}/approvals/user/{user_id}/)"
        from .assets.api.object_type import (
            delete_by_object_type_by_object_id_approvals_user_by_user_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            object_type=object_type,
            object_id=object_id,
            user_id=user_id,
        )

    def delete_object_share(self, object_type: str, object_id: str, share_id: str):
        "Delete a particular share by id (DELETE /v1/{object_type}/{object_id}/shares/{share_id}/)"
        from .assets.api.object_type import (
            delete_by_object_type_by_object_id_shares_by_share_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            object_type=object_type,
            object_id=object_id,
            share_id=share_id,
        )

    def delete_object_share_users_by_share_user(
        self, object_type: str, object_id: str, share_id: str, share_user_id: str
    ):
        "Delete a particular share_user user by id (DELETE /v1/{object_type}/{object_id}/shares/{share_id}/users/{share_user_id}/)"
        from .assets.api.object_type import (
            delete_by_object_type_by_object_id_shares_by_share_id_users_by_share_user_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            object_type=object_type,
            object_id=object_id,
            share_id=share_id,
            share_user_id=share_user_id,
        )

    def delete_collection(self, collection_id: str):
        "Delete a particular collection by id (DELETE /v1/collections/{collection_id}/)"
        from .assets.api.collections import (
            delete_collections_by_collection_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"), collection_id=collection_id
        )

    def delete_collection_contents_object(
        self, collection_id: str, object_type: str, object_id: str
    ):
        "Delete a particular content object in a collection by id (DELETE /v1/collections/{collection_id}/contents/{object_type}/{object_id}/)"
        from .assets.api.collections import (
            delete_collections_by_collection_id_contents_by_object_type_by_object_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            collection_id=collection_id,
            object_type=object_type,
            object_id=object_id,
        )

    def delete_collection_contents_ordering_custom(self, collection_id: str):
        "Disable custom ordering for a collection's content (DELETE /v1/collections/{collection_id}/contents/ordering/custom/)"
        from .assets.api.collections import (
            delete_collections_by_collection_id_contents_ordering_custom as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"), collection_id=collection_id
        )

    def delete_collection_purge(self, collection_id: str):
        "Purges deleted collection by id immediately (DELETE /v1/collections/{collection_id}/purge/)"
        from .assets.api.collections import (
            delete_collections_by_collection_id_purge as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"), collection_id=collection_id
        )

    def delete_custom_actions_by_context_by_action(self, context: str, action_id: str):
        "Deletes an custom action (DELETE /v1/custom_actions/{context}/{action_id}/)"
        from .assets.api.custom_actions import (
            delete_custom_actions_by_context_by_action_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"), context=context, action_id=action_id
        )

    def delete_delete_queue_assets(self, *, body):
        "Delete assets from delete queue (Mark assets as active again) (DELETE /v1/delete_queue/assets/)"
        from .assets.api.delete_queue import delete_delete_queue_assets as _endpoint

        return _endpoint.sync_detailed(client=self._client("assets"), body=body)

    def delete_delete_queue_collections(self, *, body):
        "Delete collections from delete queue (Mark collections as active again) (DELETE /v1/delete_queue/collections/)"
        from .assets.api.delete_queue import (
            delete_delete_queue_collections as _endpoint,
        )

        return _endpoint.sync_detailed(client=self._client("assets"), body=body)

    def delete_favorites_assets(self, *, body):
        "Deletes objects items from a list of favorites (DELETE /v1/favorites/)"
        from .assets.api.favorites import delete_favorites as _endpoint

        return _endpoint.sync_detailed(client=self._client("assets"), body=body)

    def delete_favorites_all(self):
        "Removes all assets/collections from the list of favourites (DELETE /v1/favorites/all/)"
        from .assets.api.favorites import delete_favorites_all as _endpoint

        return _endpoint.sync_detailed(client=self._client("assets"))

    def delete_favourites_all(self):
        "Removes all assets/collections from the list of favourites (DELETE /v1/favourites/all/)"
        from .assets.api.favourites import delete_favourites_all as _endpoint

        return _endpoint.sync_detailed(client=self._client("assets"))

    def delete_playlist(self, playlist_id: str):
        "Delete a particular playlist by id (DELETE /v1/playlists/{playlist_id}/)"
        from .assets.api.playlists import delete_playlists_by_playlist_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("assets"), playlist_id=playlist_id
        )

    def delete_playlist_item(self, playlist_id: str, item_id: str):
        "Delete a particular playlist item by id (DELETE /v1/playlists/{playlist_id}/items/{item_id}/)"
        from .assets.api.playlists import (
            delete_playlists_by_playlist_id_items_by_item_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"), playlist_id=playlist_id, item_id=item_id
        )

    def delete_project(self, project_id: str):
        "Delete a particular project by id (DELETE /v1/projects/{project_id}/)"
        from .assets.api.projects import delete_projects_by_project_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("assets"), project_id=project_id
        )

    def delete_project_member(self, project_id: str, member_id: str):
        "Delete a particular project member by id (DELETE /v1/projects/{project_id}/members/{member_id}/)"
        from .assets.api.projects import (
            delete_projects_by_project_id_members_by_member_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"), project_id=project_id, member_id=member_id
        )

    def delete_sequence(self, sequence_id: str):
        "Delete a particular sequence by id (DELETE /v1/sequences/{sequence_id}/)"
        from .assets.api.sequences import delete_sequences_by_sequence_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("assets"), sequence_id=sequence_id
        )

    def delete_sequence_item(self, sequence_id: str, item_id: str):
        "Delete a particular sequence item by id (DELETE /v1/sequences/{sequence_id}/items/{item_id}/)"
        from .assets.api.sequences import (
            delete_sequences_by_sequence_id_items_by_item_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"), sequence_id=sequence_id, item_id=item_id
        )

    def delete_shares_allowlist_entry(self, entry_id: str):
        "Delete an allowlist entry. (DELETE /v1/shares/allowlist/entries/{entry_id}/)"
        from .assets.api.shares import (
            delete_shares_allowlist_entries_by_entry_id as _endpoint,
        )

        return _endpoint.sync_detailed(client=self._client("assets"), entry_id=entry_id)

    def delete_shares_bulk(self, *, body):
        "Delete current user's multiple shares by ids (DELETE /v1/shares/bulk/)"
        from .assets.api.shares import delete_shares_bulk as _endpoint

        return _endpoint.sync_detailed(client=self._client("assets"), body=body)

    def delete_shares_bulk_all(self, *, body):
        "Delete multiple shares by ids (DELETE /v1/shares/bulk/all/)"
        from .assets.api.shares import delete_shares_bulk_all as _endpoint

        return _endpoint.sync_detailed(client=self._client("assets"), body=body)

    def delete_sync_sessions_by_sync_session(self, sync_session_id: str):
        "Delete a particular sync session by id (DELETE /v1/sync/sessions/{sync_session_id}/)"
        from .assets.api.sync import (
            delete_sync_sessions_by_sync_session_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"), sync_session_id=sync_session_id
        )

    def get_assets(
        self,
        *,
        per_page=UNSET,
        page=UNSET,
        scroll=UNSET,
        scroll_id=UNSET,
        sort=UNSET,
        field_name=UNSET,
        favoured_by=UNSET,
        types=UNSET,
    ):
        "Get list of assets (GET /v1/assets/)"
        from .assets.api.assets import get_assets as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            per_page=per_page,
            page=page,
            scroll=scroll,
            scroll_id=scroll_id,
            sort=sort,
            field_name=field_name,
            favoured_by=favoured_by,
            types=types,
        )

    def get_asset(
        self, asset_id: str, *, include_collections=UNSET, include_users=UNSET
    ):
        "Returns a particular asset by id (GET /v1/assets/{asset_id}/)"
        from .assets.api.assets import get_assets_by_asset_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            asset_id=asset_id,
            include_collections=include_collections,
            include_users=include_users,
        )

    def get_asset_history(
        self, asset_id: str, *, per_page=UNSET, page=UNSET, sort=UNSET, filter_=UNSET
    ):
        "Get list of history entities for asset (GET /v1/assets/{asset_id}/history/)"
        from .assets.api.assets import get_assets_by_asset_id_history as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            asset_id=asset_id,
            per_page=per_page,
            page=page,
            sort=sort,
            filter_=filter_,
        )

    def get_asset_history_by_history_entity(
        self, asset_id: str, history_entity_id: str
    ):
        "Get an asset history entity (GET /v1/assets/{asset_id}/history/{history_entity_id}/)"
        from .assets.api.assets import (
            get_assets_by_asset_id_history_by_history_entity_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            asset_id=asset_id,
            history_entity_id=history_entity_id,
        )

    def get_asset_relations(
        self,
        asset_id: str,
        *,
        include_deleted=UNSET,
        per_page=UNSET,
        page=UNSET,
        sort=UNSET,
        search_after=UNSET,
    ):
        "Returns an assets relations (GET /v1/assets/{asset_id}/relations/)"
        from .assets.api.assets import get_assets_by_asset_id_relations as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            asset_id=asset_id,
            include_deleted=include_deleted,
            per_page=per_page,
            page=page,
            sort=sort,
            search_after=search_after,
        )

    def get_asset_relations_by_relation_type(
        self,
        asset_id: str,
        relation_type: str,
        *,
        include_deleted=UNSET,
        per_page=UNSET,
        page=UNSET,
        search_after=UNSET,
    ):
        "Returns assets that has a relation to this asset (GET /v1/assets/{asset_id}/relations/{relation_type}/)"
        from .assets.api.assets import (
            get_assets_by_asset_id_relations_by_relation_type as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            asset_id=asset_id,
            relation_type=relation_type,
            include_deleted=include_deleted,
            per_page=per_page,
            page=page,
            search_after=search_after,
        )

    def get_asset_segments(
        self,
        asset_id: str,
        *,
        sort=UNSET,
        ids=UNSET,
        query=UNSET,
        includes=UNSET,
        per_page=UNSET,
        page=UNSET,
        scroll=UNSET,
        scroll_id=UNSET,
        transcription_id=UNSET,
        version_id=UNSET,
        segment_type=UNSET,
        segment_color=UNSET,
        time_start_milliseconds=UNSET,
        time_end_milliseconds=UNSET,
        time_start_milliseconds_gte=UNSET,
        time_end_milliseconds_lte=UNSET,
        status=UNSET,
        person_id=UNSET,
        share_id=UNSET,
        project_id=UNSET,
        include_users=UNSET,
        include_all_versions=UNSET,
    ):
        "List of segments (GET /v1/assets/{asset_id}/segments/)"
        from .assets.api.assets import get_assets_by_asset_id_segments as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            asset_id=asset_id,
            sort=sort,
            ids=ids,
            query=query,
            includes=includes,
            per_page=per_page,
            page=page,
            scroll=scroll,
            scroll_id=scroll_id,
            transcription_id=transcription_id,
            version_id=version_id,
            segment_type=segment_type,
            segment_color=segment_color,
            time_start_milliseconds=time_start_milliseconds,
            time_end_milliseconds=time_end_milliseconds,
            time_start_milliseconds_gte=time_start_milliseconds_gte,
            time_end_milliseconds_lte=time_end_milliseconds_lte,
            status=status,
            person_id=person_id,
            share_id=share_id,
            project_id=project_id,
            include_users=include_users,
            include_all_versions=include_all_versions,
        )

    def get_asset_segment(
        self, asset_id: str, segment_id: str, *, scroll=UNSET, scroll_id=UNSET
    ):
        "Get a segment by ID (GET /v1/assets/{asset_id}/segments/{segment_id}/)"
        from .assets.api.assets import (
            get_assets_by_asset_id_segments_by_segment_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            asset_id=asset_id,
            segment_id=segment_id,
            scroll=scroll,
            scroll_id=scroll_id,
        )

    def get_asset_segments_csv(
        self,
        asset_id: str,
        *,
        ids=UNSET,
        query=UNSET,
        transcription_id=UNSET,
        version_id=UNSET,
        segment_type=UNSET,
        segment_color=UNSET,
    ):
        "List of segments as CSV file (GET /v1/assets/{asset_id}/segments/csv/)"
        from .assets.api.assets import get_assets_by_asset_id_segments_csv as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            asset_id=asset_id,
            ids=ids,
            query=query,
            transcription_id=transcription_id,
            version_id=version_id,
            segment_type=segment_type,
            segment_color=segment_color,
        )

    def get_asset_segments_srt(
        self,
        asset_id: str,
        *,
        ids=UNSET,
        query=UNSET,
        transcription_id=UNSET,
        version_id=UNSET,
        segment_type=UNSET,
        segment_color=UNSET,
        words_per_line=UNSET,
    ):
        "List of segments as SRT file (GET /v1/assets/{asset_id}/segments/srt/)"
        from .assets.api.assets import get_assets_by_asset_id_segments_srt as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            asset_id=asset_id,
            ids=ids,
            query=query,
            transcription_id=transcription_id,
            version_id=version_id,
            segment_type=segment_type,
            segment_color=segment_color,
            words_per_line=words_per_line,
        )

    def get_asset_segments_text(
        self,
        asset_id: str,
        *,
        ids=UNSET,
        query=UNSET,
        transcription_id=UNSET,
        version_id=UNSET,
        segment_type=UNSET,
        segment_color=UNSET,
    ):
        "List of segments as text file (GET /v1/assets/{asset_id}/segments/text/)"
        from .assets.api.assets import get_assets_by_asset_id_segments_text as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            asset_id=asset_id,
            ids=ids,
            query=query,
            transcription_id=transcription_id,
            version_id=version_id,
            segment_type=segment_type,
            segment_color=segment_color,
        )

    def get_asset_segments_vtt(
        self,
        asset_id: str,
        *,
        ids=UNSET,
        query=UNSET,
        transcription_id=UNSET,
        version_id=UNSET,
        segment_type=UNSET,
        segment_color=UNSET,
        words_per_line=UNSET,
    ):
        "List of segments as WebVTT file (GET /v1/assets/{asset_id}/segments/vtt/)"
        from .assets.api.assets import get_assets_by_asset_id_segments_vtt as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            asset_id=asset_id,
            ids=ids,
            query=query,
            transcription_id=transcription_id,
            version_id=version_id,
            segment_type=segment_type,
            segment_color=segment_color,
            words_per_line=words_per_line,
        )

    def get_asset_shares_all(self, asset_id: str):
        "Get list of asset's shares including all direct and indirect shares that were made by sharing (GET /v1/assets/{asset_id}/shares/all/)"
        from .assets.api.assets import get_assets_by_asset_id_shares_all as _endpoint

        return _endpoint.sync_detailed(client=self._client("assets"), asset_id=asset_id)

    def get_asset_version_transcription_properties(
        self, asset_id: str, version_id: str, transcription_id: str
    ):
        "Get a transcription properties by ID (GET /v1/assets/{asset_id}/versions/{version_id}/transcriptions/{transcription_id}/properties/)"
        from .assets.api.assets import (
            get_assets_by_asset_id_versions_by_version_id_transcriptions_by_transcription_id_properties as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            asset_id=asset_id,
            version_id=version_id,
            transcription_id=transcription_id,
        )

    def get_asset_version_transcriptions_properties(
        self, asset_id: str, version_id: str
    ):
        "Get a list of transcription properties (GET /v1/assets/{asset_id}/versions/{version_id}/transcriptions/properties/)"
        from .assets.api.assets import (
            get_assets_by_asset_id_versions_by_version_id_transcriptions_properties as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"), asset_id=asset_id, version_id=version_id
        )

    def get_assets_recent(self, *, per_page=UNSET, page=UNSET, search_after=UNSET):
        "Get list of recently viewed assets (GET /v1/assets/recent/)"
        from .assets.api.assets import get_assets_recent as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            per_page=per_page,
            page=page,
            search_after=search_after,
        )

    def get_assets_relation_types(self):
        "Create a new asset relation type (GET /v1/assets/relation_types/)"
        from .assets.api.assets import get_assets_relation_types as _endpoint

        return _endpoint.sync_detailed(client=self._client("assets"))

    def get_assets_relation_types_by_relation_type(self, relation_type: str):
        "Get a relation type (GET /v1/assets/relation_types/{relation_type}/)"
        from .assets.api.assets import (
            get_assets_relation_types_by_relation_type as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"), relation_type=relation_type
        )

    def get_object_approvals(self, object_type: str, object_id: str):
        "Returns an objects approval request (GET /v1/{object_type}/{object_id}/approvals/)"
        from .assets.api.object_type import (
            get_by_object_type_by_object_id_approvals as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"), object_type=object_type, object_id=object_id
        )

    def get_object_approvals_request(self, object_type: str, object_id: str):
        "Returns an objects approval request (GET /v1/{object_type}/{object_id}/approvals/request/)"
        from .assets.api.object_type import (
            get_by_object_type_by_object_id_approvals_request as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"), object_type=object_type, object_id=object_id
        )

    def get_object_shares(
        self, object_type: str, object_id: str, *, per_page=UNSET, last_id=UNSET
    ):
        "Get list of object shares (GET /v1/{object_type}/{object_id}/shares/)"
        from .assets.api.object_type import (
            get_by_object_type_by_object_id_shares as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            object_type=object_type,
            object_id=object_id,
            per_page=per_page,
            last_id=last_id,
        )

    def get_object_share(self, object_type: str, object_id: str, share_id: str):
        "Returns a particular share by id (GET /v1/{object_type}/{object_id}/shares/{share_id}/)"
        from .assets.api.object_type import (
            get_by_object_type_by_object_id_shares_by_share_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            object_type=object_type,
            object_id=object_id,
            share_id=share_id,
        )

    def get_object_share_users(
        self,
        object_type: str,
        object_id: str,
        share_id: str,
        *,
        per_page=UNSET,
        last_id=UNSET,
    ):
        "Get list of share users (GET /v1/{object_type}/{object_id}/shares/{share_id}/users/)"
        from .assets.api.object_type import (
            get_by_object_type_by_object_id_shares_by_share_id_users as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            object_type=object_type,
            object_id=object_id,
            share_id=share_id,
            per_page=per_page,
            last_id=last_id,
        )

    def get_object_share_users_by_share_user(
        self, object_type: str, object_id: str, share_id: str, share_user_id: str
    ):
        "Returns a particular share user by id (GET /v1/{object_type}/{object_id}/shares/{share_id}/users/{share_user_id}/)"
        from .assets.api.object_type import (
            get_by_object_type_by_object_id_shares_by_share_id_users_by_share_user_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            object_type=object_type,
            object_id=object_id,
            share_id=share_id,
            share_user_id=share_user_id,
        )

    def get_object_version_approvals(
        self, object_type: str, object_id: str, version_id: str
    ):
        "Returns an objects approval request by version (GET /v1/{object_type}/{object_id}/versions/{version_id}/approvals/)"
        from .assets.api.object_type import (
            get_by_object_type_by_object_id_versions_by_version_id_approvals as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            object_type=object_type,
            object_id=object_id,
            version_id=version_id,
        )

    def get_object_version_approvals_request(
        self, object_type: str, object_id: str, version_id: str
    ):
        "Returns an objects approval request by version (GET /v1/{object_type}/{object_id}/versions/{version_id}/approvals/request/)"
        from .assets.api.object_type import (
            get_by_object_type_by_object_id_versions_by_version_id_approvals_request as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            object_type=object_type,
            object_id=object_id,
            version_id=version_id,
        )

    def get_collections(
        self,
        *,
        per_page=UNSET,
        page=UNSET,
        scroll=UNSET,
        scroll_id=UNSET,
        sort=UNSET,
        is_root=UNSET,
        status=UNSET,
        favoured_by=UNSET,
        include_keyframes=UNSET,
    ):
        "Get list of collections (GET /v1/collections/)"
        from .assets.api.collections import get_collections as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            per_page=per_page,
            page=page,
            scroll=scroll,
            scroll_id=scroll_id,
            sort=sort,
            is_root=is_root,
            status=status,
            favoured_by=favoured_by,
            include_keyframes=include_keyframes,
        )

    def get_collection(self, collection_id: str):
        "Returns a particular collection by id (GET /v1/collections/{collection_id}/)"
        from .assets.api.collections import (
            get_collections_by_collection_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"), collection_id=collection_id
        )

    def get_collection_ancestors(self, collection_id: str):
        "Returns list of ancestors of a collection (GET /v1/collections/{collection_id}/ancestors/)"
        from .assets.api.collections import (
            get_collections_by_collection_id_ancestors as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"), collection_id=collection_id
        )

    def get_collection_content_info(
        self,
        collection_id: str,
        *,
        only_active=UNSET,
        include_subcollections=UNSET,
        format_name=UNSET,
        by_storage_id=UNSET,
        types=UNSET,
    ):
        "Get aggregated information about collection (GET /v1/collections/{collection_id}/content/info/)"
        from .assets.api.collections import (
            get_collections_by_collection_id_content_info as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            collection_id=collection_id,
            only_active=only_active,
            include_subcollections=include_subcollections,
            format_name=format_name,
            by_storage_id=by_storage_id,
            types=types,
        )

    def get_collection_contents(
        self,
        collection_id: str,
        *,
        object_types=UNSET,
        object_ids=UNSET,
        external_id=UNSET,
        per_page=UNSET,
        page=UNSET,
        sort=UNSET,
        filter_=UNSET,
        include_keyframes=UNSET,
    ):
        "Returns contents of a collection by id (GET /v1/collections/{collection_id}/contents/)"
        from .assets.api.collections import (
            get_collections_by_collection_id_contents as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            collection_id=collection_id,
            object_types=object_types,
            object_ids=object_ids,
            external_id=external_id,
            per_page=per_page,
            page=page,
            sort=sort,
            filter_=filter_,
            include_keyframes=include_keyframes,
        )

    def get_collection_full_path(self, collection_id: str, *, get_upload_path=UNSET):
        "Gets the full path of the collection (GET /v1/collections/{collection_id}/full/path/)"
        from .assets.api.collections import (
            get_collections_by_collection_id_full_path as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            collection_id=collection_id,
            get_upload_path=get_upload_path,
        )

    def get_collection_shares_all(self, collection_id: str):
        "Get list of collection's shares including all direct and indirect shares that were made by (GET /v1/collections/{collection_id}/shares/all/)"
        from .assets.api.collections import (
            get_collections_by_collection_id_shares_all as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"), collection_id=collection_id
        )

    def get_collection_size(
        self, collection_id: str, *, format_name=UNSET, include_subcollections=UNSET
    ):
        "Returns the size of all the collection's assets in bytes (GET /v1/collections/{collection_id}/size/)"
        from .assets.api.collections import (
            get_collections_by_collection_id_size as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            collection_id=collection_id,
            format_name=format_name,
            include_subcollections=include_subcollections,
        )

    def get_collections_recent(self, *, per_page=UNSET, page=UNSET, search_after=UNSET):
        "Get list of recently viewed collections (GET /v1/collections/recent/)"
        from .assets.api.collections import get_collections_recent as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            per_page=per_page,
            page=page,
            search_after=search_after,
        )

    def get_custom_actions(self):
        "Get list of custom actions (GET /v1/custom_actions/)"
        from .assets.api.custom_actions import get_custom_actions as _endpoint

        return _endpoint.sync_detailed(client=self._client("assets"))

    def get_custom_actions_by_context(self, context: str):
        "Get list of custom actions by context (GET /v1/custom_actions/{context}/)"
        from .assets.api.custom_actions import (
            get_custom_actions_by_context as _endpoint,
        )

        return _endpoint.sync_detailed(client=self._client("assets"), context=context)

    def get_custom_actions_by_context_by_action(self, context: str, action_id: str):
        "Get an asset custom action (GET /v1/custom_actions/{context}/{action_id}/)"
        from .assets.api.custom_actions import (
            get_custom_actions_by_context_by_action_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"), context=context, action_id=action_id
        )

    def get_delete_queue_assets(
        self, *, per_page=UNSET, page=UNSET, sort=UNSET, filter_=UNSET
    ):
        "Get deleted objects (GET /v1/delete_queue/assets/)"
        from .assets.api.delete_queue import get_delete_queue_assets as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            per_page=per_page,
            page=page,
            sort=sort,
            filter_=filter_,
        )

    def get_delete_queue_collections(
        self, *, per_page=UNSET, page=UNSET, sort=UNSET, filter_=UNSET
    ):
        "Get list of collections (GET /v1/delete_queue/collections/)"
        from .assets.api.delete_queue import get_delete_queue_collections as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            per_page=per_page,
            page=page,
            sort=sort,
            filter_=filter_,
        )

    def get_favorites(self, *, per_page=UNSET, page=UNSET, sort=UNSET):
        "Get list of favorite objects (GET /v1/favorites/)"
        from .assets.api.favorites import get_favorites as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("assets"), per_page=per_page, page=page, sort=sort
        )

    def get_person(self, person_id: str, *, page=UNSET, per_page=UNSET, asset_id=UNSET):
        "Get all assets containing a person_id or specific versions of an asset containing a person_id (GET /v1/persons/{person_id}/)"
        from .assets.api.persons import get_persons_by_person_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            person_id=person_id,
            page=page,
            per_page=per_page,
            asset_id=asset_id,
        )

    def get_playlists(
        self,
        *,
        per_page=UNSET,
        page=UNSET,
        scroll=UNSET,
        scroll_id=UNSET,
        sort=UNSET,
        status=UNSET,
        ids=UNSET,
    ):
        "Get list of playlists (GET /v1/playlists/)"
        from .assets.api.playlists import get_playlists as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            per_page=per_page,
            page=page,
            scroll=scroll,
            scroll_id=scroll_id,
            sort=sort,
            status=status,
            ids=ids,
        )

    def get_playlist(self, playlist_id: str):
        "Returns a particular playlist by id (GET /v1/playlists/{playlist_id}/)"
        from .assets.api.playlists import get_playlists_by_playlist_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("assets"), playlist_id=playlist_id
        )

    def get_playlist_items(
        self, playlist_id: str, *, per_page=UNSET, ids=UNSET, page=UNSET
    ):
        "Get list of playlist's items (GET /v1/playlists/{playlist_id}/items/)"
        from .assets.api.playlists import (
            get_playlists_by_playlist_id_items as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            playlist_id=playlist_id,
            per_page=per_page,
            ids=ids,
            page=page,
        )

    def get_projects(
        self,
        *,
        per_page=UNSET,
        page=UNSET,
        scroll=UNSET,
        scroll_id=UNSET,
        sort=UNSET,
        status=UNSET,
    ):
        "Get list of projects (GET /v1/projects/)"
        from .assets.api.projects import get_projects as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            per_page=per_page,
            page=page,
            scroll=scroll,
            scroll_id=scroll_id,
            sort=sort,
            status=status,
        )

    def get_project(self, project_id: str, *, include_users=UNSET):
        "Returns a particular project by id (GET /v1/projects/{project_id}/)"
        from .assets.api.projects import get_projects_by_project_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            project_id=project_id,
            include_users=include_users,
        )

    def get_project_members(self, project_id: str):
        "Get list of project's members (GET /v1/projects/{project_id}/members/)"
        from .assets.api.projects import get_projects_by_project_id_members as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("assets"), project_id=project_id
        )

    def get_project_member(self, project_id: str, member_id: str):
        "Returns a particular project member by id (GET /v1/projects/{project_id}/members/{member_id}/)"
        from .assets.api.projects import (
            get_projects_by_project_id_members_by_member_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"), project_id=project_id, member_id=member_id
        )

    def get_publications_templates(self):
        "Returns publication templates that can be used for publishing (GET /v1/publications/templates/)"
        from .assets.api.publications import get_publications_templates as _endpoint

        return _endpoint.sync_detailed(client=self._client("assets"))

    def get_publications_token(self):
        "Returns publication token that can be used for loading publication panel (GET /v1/publications/token/)"
        from .assets.api.publications import get_publications_token as _endpoint

        return _endpoint.sync_detailed(client=self._client("assets"))

    def get_sequences(
        self,
        *,
        per_page=UNSET,
        page=UNSET,
        scroll=UNSET,
        scroll_id=UNSET,
        sort=UNSET,
        status=UNSET,
    ):
        "Get list of sequences (GET /v1/sequences/)"
        from .assets.api.sequences import get_sequences as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            per_page=per_page,
            page=page,
            scroll=scroll,
            scroll_id=scroll_id,
            sort=sort,
            status=status,
        )

    def get_sequence(self, sequence_id: str):
        "Returns a particular sequence by id (GET /v1/sequences/{sequence_id}/)"
        from .assets.api.sequences import get_sequences_by_sequence_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("assets"), sequence_id=sequence_id
        )

    def get_sequence_items(self, sequence_id: str, *, per_page=UNSET, page=UNSET):
        "Get list of sequence's items (GET /v1/sequences/{sequence_id}/items/)"
        from .assets.api.sequences import (
            get_sequences_by_sequence_id_items as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            sequence_id=sequence_id,
            per_page=per_page,
            page=page,
        )

    def get_shares(
        self,
        *,
        title=UNSET,
        object_type=UNSET,
        object_id=UNSET,
        ids=UNSET,
        query=UNSET,
        field_exists=UNSET,
        date_created=UNSET,
        date_modified=UNSET,
        expires=UNSET,
        include_created_by_me=UNSET,
        include_member_of=UNSET,
        page=UNSET,
        per_page=UNSET,
        scroll=UNSET,
        scroll_id=UNSET,
        sort=UNSET,
    ):
        "Get a list of user's shares (GET /v1/shares/)"
        from .assets.api.shares import get_shares as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            title=title,
            object_type=object_type,
            object_id=object_id,
            ids=ids,
            query=query,
            field_exists=field_exists,
            date_created=date_created,
            date_modified=date_modified,
            expires=expires,
            include_created_by_me=include_created_by_me,
            include_member_of=include_member_of,
            page=page,
            per_page=per_page,
            scroll=scroll,
            scroll_id=scroll_id,
            sort=sort,
        )

    def get_shares_all(
        self,
        *,
        title=UNSET,
        object_type=UNSET,
        object_id=UNSET,
        owner_id=UNSET,
        member_id=UNSET,
        ids=UNSET,
        query=UNSET,
        field_exists=UNSET,
        date_created=UNSET,
        date_modified=UNSET,
        expires=UNSET,
        page=UNSET,
        per_page=UNSET,
        scroll=UNSET,
        scroll_id=UNSET,
        sort=UNSET,
    ):
        "Get a list of all domain shares (GET /v1/shares/all/)"
        from .assets.api.shares import get_shares_all as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            title=title,
            object_type=object_type,
            object_id=object_id,
            owner_id=owner_id,
            member_id=member_id,
            ids=ids,
            query=query,
            field_exists=field_exists,
            date_created=date_created,
            date_modified=date_modified,
            expires=expires,
            page=page,
            per_page=per_page,
            scroll=scroll,
            scroll_id=scroll_id,
            sort=sort,
        )

    def get_shares_allowlist_entries(self):
        "Get all magic link allowlist entries. (GET /v1/shares/allowlist/entries/)"
        from .assets.api.shares import get_shares_allowlist_entries as _endpoint

        return _endpoint.sync_detailed(client=self._client("assets"))

    def get_shares_allowlist_entry(self, entry_id: str):
        "Get a single allowlist entry by ID. (GET /v1/shares/allowlist/entries/{entry_id}/)"
        from .assets.api.shares import (
            get_shares_allowlist_entries_by_entry_id as _endpoint,
        )

        return _endpoint.sync_detailed(client=self._client("assets"), entry_id=entry_id)

    def get_shares_auth_token(self, *, share_auth_token):
        "Check if a token is valid (GET /v1/shares/auth/token/)"
        from .assets.api.shares import get_shares_auth_token as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("assets"), share_auth_token=share_auth_token
        )

    def get_sync_sessions_by_sync_session(self, sync_session_id: str):
        "Returns a particular sync session by id. If a session with such id doesn't exist, (GET /v1/sync/sessions/{sync_session_id}/)"
        from .assets.api.sync import get_sync_sessions_by_sync_session_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("assets"), sync_session_id=sync_session_id
        )

    def patch_assets(self, *, body):
        "Bulk update assets (PATCH /v1/assets/)"
        from .assets.api.assets import patch_assets as _endpoint

        return _endpoint.sync_detailed(client=self._client("assets"), body=body)

    def patch_asset(self, asset_id: str, *, body, generate_subclip_keyframes=UNSET):
        "Update asset (PATCH /v1/assets/{asset_id}/)"
        from .assets.api.assets import patch_assets_by_asset_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            asset_id=asset_id,
            body=body,
            generate_subclip_keyframes=generate_subclip_keyframes,
        )

    def patch_asset_segment(
        self, asset_id: str, segment_id: str, *, body, generate_subclip_keyframes=UNSET
    ):
        "Update segment (PATCH /v1/assets/{asset_id}/segments/{segment_id}/)"
        from .assets.api.assets import (
            patch_assets_by_asset_id_segments_by_segment_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            asset_id=asset_id,
            segment_id=segment_id,
            body=body,
            generate_subclip_keyframes=generate_subclip_keyframes,
        )

    def patch_asset_version(self, asset_id: str, version_id: str, *, body):
        "Edit asset version (PATCH /v1/assets/{asset_id}/versions/{version_id}/)"
        from .assets.api.assets import (
            patch_assets_by_asset_id_versions_by_version_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            asset_id=asset_id,
            version_id=version_id,
            body=body,
        )

    def patch_asset_version_transcription_properties(
        self, asset_id: str, version_id: str, transcription_id: str, *, body
    ):
        "Update transcription properties by ID (PATCH /v1/assets/{asset_id}/versions/{version_id}/transcriptions/{transcription_id}/properties/)"
        from .assets.api.assets import (
            patch_assets_by_asset_id_versions_by_version_id_transcriptions_by_transcription_id_properties as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            asset_id=asset_id,
            version_id=version_id,
            transcription_id=transcription_id,
            body=body,
        )

    def patch_assets_relation_types_by_relation_type(self, relation_type: str, *, body):
        "Update an asset relation type (PATCH /v1/assets/relation_types/{relation_type}/)"
        from .assets.api.assets import (
            patch_assets_relation_types_by_relation_type as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"), relation_type=relation_type, body=body
        )

    def patch_object_approvals_request(self, object_type: str, object_id: str, *, body):
        "Edits an approval request (PATCH /v1/{object_type}/{object_id}/approvals/request/)"
        from .assets.api.object_type import (
            patch_by_object_type_by_object_id_approvals_request as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            object_type=object_type,
            object_id=object_id,
            body=body,
        )

    def patch_object_share_users_by_share_user(
        self,
        object_type: str,
        object_id: str,
        share_id: str,
        share_user_id: str,
        *,
        body,
    ):
        "Update share user (PATCH /v1/{object_type}/{object_id}/shares/{share_id}/users/{share_user_id}/)"
        from .assets.api.object_type import (
            patch_by_object_type_by_object_id_shares_by_share_id_users_by_share_user_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            object_type=object_type,
            object_id=object_id,
            share_id=share_id,
            share_user_id=share_user_id,
            body=body,
        )

    def patch_collection(self, collection_id: str, *, body, change_parent_mode=UNSET):
        "Update collection (PATCH /v1/collections/{collection_id}/)"
        from .assets.api.collections import (
            patch_collections_by_collection_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            collection_id=collection_id,
            body=body,
            change_parent_mode=change_parent_mode,
        )

    def patch_custom_actions_by_context_by_action(
        self, context: str, action_id: str, *, body
    ):
        "Update an custom action (PATCH /v1/custom_actions/{context}/{action_id}/)"
        from .assets.api.custom_actions import (
            patch_custom_actions_by_context_by_action_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            context=context,
            action_id=action_id,
            body=body,
        )

    def patch_playlist(self, playlist_id: str, *, body):
        "Update a playlist (PATCH /v1/playlists/{playlist_id}/)"
        from .assets.api.playlists import patch_playlists_by_playlist_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("assets"), playlist_id=playlist_id, body=body
        )

    def patch_playlist_item(self, playlist_id: str, item_id: str, *, body):
        "Update a playlist item (PATCH /v1/playlists/{playlist_id}/items/{item_id}/)"
        from .assets.api.playlists import (
            patch_playlists_by_playlist_id_items_by_item_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            playlist_id=playlist_id,
            item_id=item_id,
            body=body,
        )

    def patch_project(self, project_id: str, *, body):
        "Update project (PATCH /v1/projects/{project_id}/)"
        from .assets.api.projects import patch_projects_by_project_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("assets"), project_id=project_id, body=body
        )

    def patch_sequence(self, sequence_id: str, *, body):
        "Update a sequence (PATCH /v1/sequences/{sequence_id}/)"
        from .assets.api.sequences import patch_sequences_by_sequence_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("assets"), sequence_id=sequence_id, body=body
        )

    def patch_sync_sessions_by_sync_session(
        self, sync_session_id: str, *, body, update_if_none=UNSET
    ):
        "Edit a sync session. If the session doesn't exist, a new one is created (PATCH /v1/sync/sessions/{sync_session_id}/)"
        from .assets.api.sync import patch_sync_sessions_by_sync_session_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            sync_session_id=sync_session_id,
            body=body,
            update_if_none=update_if_none,
        )

    def post_approvals_bulk(self, *, body):
        "Create a job for bulk request & set approval (POST /v1/approvals/bulk/)"
        from .assets.api.approvals import post_approvals_bulk as _endpoint

        return _endpoint.sync_detailed(client=self._client("assets"), body=body)

    def post_approvals_bulk_remove(self, *, body):
        "Create a job for bulk approval status removal (POST /v1/approvals/bulk_remove/)"
        from .assets.api.approvals import post_approvals_bulk_remove as _endpoint

        return _endpoint.sync_detailed(client=self._client("assets"), body=body)

    def post_assets(
        self,
        *,
        body,
        apply_default_acls=UNSET,
        apply_collection_acls=UNSET,
        assign_to_collection=UNSET,
        generate_subclip_keyframes=UNSET,
        apply_acl_template_id=UNSET,
    ):
        "Create a new asset (POST /v1/assets/)"
        from .assets.api.assets import post_assets as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            body=body,
            apply_default_acls=apply_default_acls,
            apply_collection_acls=apply_collection_acls,
            assign_to_collection=assign_to_collection,
            generate_subclip_keyframes=generate_subclip_keyframes,
            apply_acl_template_id=apply_acl_template_id,
        )

    def post_asset_history(self, asset_id: str, *, body):
        "Create an asset history entity (POST /v1/assets/{asset_id}/history/)"
        from .assets.api.assets import post_assets_by_asset_id_history as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("assets"), asset_id=asset_id, body=body
        )

    def post_asset_history_reindex_by_history_entity(
        self, asset_id: str, history_entity_id: str, *, body
    ):
        "Reindex asset history entity (POST /v1/assets/{asset_id}/history/{history_entity_id}/reindex/)"
        from .assets.api.assets import (
            post_assets_by_asset_id_history_by_history_entity_id_reindex as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            asset_id=asset_id,
            history_entity_id=history_entity_id,
            body=body,
        )

    def post_asset_reindex(self, asset_id: str, *, body):
        "Reindex asset (POST /v1/assets/{asset_id}/reindex/)"
        from .assets.api.assets import post_assets_by_asset_id_reindex as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("assets"), asset_id=asset_id, body=body
        )

    def post_asset_relations(self, asset_id: str, *, body):
        "Create a new asset relation (POST /v1/assets/{asset_id}/relations/)"
        from .assets.api.assets import post_assets_by_asset_id_relations as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("assets"), asset_id=asset_id, body=body
        )

    def post_asset_relations_by_relation_type_by_related_to_asset(
        self, asset_id: str, relation_type: str, related_to_asset_id: str, *, body
    ):
        "Create a new asset relation (POST /v1/assets/{asset_id}/relations/{relation_type}/{related_to_asset_id}/)"
        from .assets.api.assets import (
            post_assets_by_asset_id_relations_by_relation_type_by_related_to_asset_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            asset_id=asset_id,
            relation_type=relation_type,
            related_to_asset_id=related_to_asset_id,
            body=body,
        )

    def post_asset_relations_reverse_by_relation_type_by_related_to_asset(
        self, asset_id: str, relation_type: str, related_to_asset_id: str
    ):
        "Reverse a particular asset's relation (POST /v1/assets/{asset_id}/relations/{relation_type}/{related_to_asset_id}/reverse/)"
        from .assets.api.assets import (
            post_assets_by_asset_id_relations_by_relation_type_by_related_to_asset_id_reverse as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            asset_id=asset_id,
            relation_type=relation_type,
            related_to_asset_id=related_to_asset_id,
        )

    def post_asset_segments(self, asset_id: str, *, body, share_user_email=UNSET):
        "Create a new segment (POST /v1/assets/{asset_id}/segments/)"
        from .assets.api.assets import post_assets_by_asset_id_segments as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            asset_id=asset_id,
            body=body,
            share_user_email=share_user_email,
        )

    def post_asset_segments_bulk(self, asset_id: str, *, body):
        "Create multiple new segments for a single asset (POST /v1/assets/{asset_id}/segments/bulk/)"
        from .assets.api.assets import (
            post_assets_by_asset_id_segments_bulk as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"), asset_id=asset_id, body=body
        )

    def post_asset_segment_reindex(self, asset_id: str, segment_id: str, *, body):
        "Reindex assets segment (POST /v1/assets/{asset_id}/segments/{segment_id}/reindex/)"
        from .assets.api.assets import (
            post_assets_by_asset_id_segments_by_segment_id_reindex as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            asset_id=asset_id,
            segment_id=segment_id,
            body=body,
        )

    def post_asset_segments_reindex(self, asset_id: str, *, body):
        "Reindex assets segments (POST /v1/assets/{asset_id}/segments/reindex/)"
        from .assets.api.assets import (
            post_assets_by_asset_id_segments_reindex as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"), asset_id=asset_id, body=body
        )

    def post_asset_versions(self, asset_id: str, *, body):
        "Add asset version (POST /v1/assets/{asset_id}/versions/)"
        from .assets.api.assets import post_assets_by_asset_id_versions as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("assets"), asset_id=asset_id, body=body
        )

    def post_asset_version_transcriptions_properties(
        self, asset_id: str, version_id: str, *, body
    ):
        "Add a new transcription properties (POST /v1/assets/{asset_id}/versions/{version_id}/transcriptions/properties/)"
        from .assets.api.assets import (
            post_assets_by_asset_id_versions_by_version_id_transcriptions_properties as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            asset_id=asset_id,
            version_id=version_id,
            body=body,
        )

    def post_asset_version_transcriptions_subtitles(
        self, asset_id: str, version_id: str, *, body
    ):
        "Add a new transcription properties (POST /v1/assets/{asset_id}/versions/{version_id}/transcriptions/subtitles/)"
        from .assets.api.assets import (
            post_assets_by_asset_id_versions_by_version_id_transcriptions_subtitles as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            asset_id=asset_id,
            version_id=version_id,
            body=body,
        )

    def post_asset_versions_from_assets_by_source_asset(
        self, asset_id: str, source_asset_id: str, *, body
    ):
        "Create a new asset's version from another asset (POST /v1/assets/{asset_id}/versions/from/assets/{source_asset_id}/)"
        from .assets.api.assets import (
            post_assets_by_asset_id_versions_from_assets_by_source_asset_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            asset_id=asset_id,
            source_asset_id=source_asset_id,
            body=body,
        )

    def post_asset_versions_from_versions_by_source_version(
        self, asset_id: str, source_version_id: str, *, body
    ):
        "Create a new asset's version from another version (POST /v1/assets/{asset_id}/versions/from/versions/{source_version_id}/)"
        from .assets.api.assets import (
            post_assets_by_asset_id_versions_from_versions_by_source_version_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            asset_id=asset_id,
            source_version_id=source_version_id,
            body=body,
        )

    def post_asset_views(self, asset_id: str):
        "Mark asset as viewed (POST /v1/assets/{asset_id}/views/)"
        from .assets.api.assets import post_assets_by_asset_id_views as _endpoint

        return _endpoint.sync_detailed(client=self._client("assets"), asset_id=asset_id)

    def post_assets_reindex(self, *, body=UNSET):
        "Trigger reindexing of all assets (POST /v1/assets/reindex/)"
        from .assets.api.assets import post_assets_reindex as _endpoint

        return _endpoint.sync_detailed(client=self._client("assets"), body=body)

    def post_assets_relation_types(self, *, body):
        "Create a new asset relation type (POST /v1/assets/relation_types/)"
        from .assets.api.assets import post_assets_relation_types as _endpoint

        return _endpoint.sync_detailed(client=self._client("assets"), body=body)

    def post_assets_segments_reindex(self, *, body):
        "Trigger reindexing of all segments (POST /v1/assets/segments/reindex/)"
        from .assets.api.assets import post_assets_segments_reindex as _endpoint

        return _endpoint.sync_detailed(client=self._client("assets"), body=body)

    def post_object_approvals_request(self, object_type: str, object_id: str, *, body):
        "Creates an objects approval request (POST /v1/{object_type}/{object_id}/approvals/request/)"
        from .assets.api.object_type import (
            post_by_object_type_by_object_id_approvals_request as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            object_type=object_type,
            object_id=object_id,
            body=body,
        )

    def post_object_shares(self, object_type: str, object_id: str, *, body):
        "Create a new share. (POST /v1/{object_type}/{object_id}/shares/)"
        from .assets.api.object_type import (
            post_by_object_type_by_object_id_shares as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            object_type=object_type,
            object_id=object_id,
            body=body,
        )

    def post_object_share_reindex(
        self, object_type: str, object_id: str, share_id: str, *, body
    ):
        "Reindex the share (POST /v1/{object_type}/{object_id}/shares/{share_id}/reindex/)"
        from .assets.api.object_type import (
            post_by_object_type_by_object_id_shares_by_share_id_reindex as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            object_type=object_type,
            object_id=object_id,
            share_id=share_id,
            body=body,
        )

    def post_object_share_users(
        self, object_type: str, object_id: str, share_id: str, *, body
    ):
        "Add a new share_user to a share (POST /v1/{object_type}/{object_id}/shares/{share_id}/users/)"
        from .assets.api.object_type import (
            post_by_object_type_by_object_id_shares_by_share_id_users as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            object_type=object_type,
            object_id=object_id,
            share_id=share_id,
            body=body,
        )

    def post_object_shares_url(self, object_type: str, object_id: str, *, body):
        "Generates a URL for the shared object (POST /v1/{object_type}/{object_id}/shares/url/)"
        from .assets.api.object_type import (
            post_by_object_type_by_object_id_shares_url as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            object_type=object_type,
            object_id=object_id,
            body=body,
        )

    def post_collections(
        self,
        *,
        body,
        apply_default_acls=UNSET,
        apply_collection_acls=UNSET,
        restrict_collection_acls=UNSET,
        apply_acl_template_id=UNSET,
    ):
        "Create a new collection (POST /v1/collections/)"
        from .assets.api.collections import post_collections as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            body=body,
            apply_default_acls=apply_default_acls,
            apply_collection_acls=apply_collection_acls,
            restrict_collection_acls=restrict_collection_acls,
            apply_acl_template_id=apply_acl_template_id,
        )

    def post_collection_contents(self, collection_id: str, *, body):
        "Add an object to a collection (POST /v1/collections/{collection_id}/contents/)"
        from .assets.api.collections import (
            post_collections_by_collection_id_contents as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"), collection_id=collection_id, body=body
        )

    def post_collection_contents_object_reindex(
        self, collection_id: str, object_type: str, object_id: str, *, body
    ):
        "Reindex collection content (POST /v1/collections/{collection_id}/contents/{object_type}/{object_id}/reindex/)"
        from .assets.api.collections import (
            post_collections_by_collection_id_contents_by_object_type_by_object_id_reindex as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            collection_id=collection_id,
            object_type=object_type,
            object_id=object_id,
            body=body,
        )

    def post_collection_contents_ordering_custom(self, collection_id: str, *, body):
        "Enable custom ordering for a collection's content (POST /v1/collections/{collection_id}/contents/ordering/custom/)"
        from .assets.api.collections import (
            post_collections_by_collection_id_contents_ordering_custom as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"), collection_id=collection_id, body=body
        )

    def post_collection_keyframes_assets(self, collection_id: str, *, body):
        "Pick up to three asset_ids for collection keyframes (POST /v1/collections/{collection_id}/keyframes/)"
        from .assets.api.collections import (
            post_collections_by_collection_id_keyframes as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"), collection_id=collection_id, body=body
        )

    def post_collection_reindex(self, collection_id: str, *, body):
        "Reindex collection (POST /v1/collections/{collection_id}/reindex/)"
        from .assets.api.collections import (
            post_collections_by_collection_id_reindex as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"), collection_id=collection_id, body=body
        )

    def post_collection_reindex_contents(self, collection_id: str, *, body):
        "Reindex collection and its content (POST /v1/collections/{collection_id}/reindex/contents/)"
        from .assets.api.collections import (
            post_collections_by_collection_id_reindex_contents as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"), collection_id=collection_id, body=body
        )

    def post_collection_subcollections(
        self, collection_id: str, *, body, copy_acl=UNSET, copy_keyframes=UNSET
    ):
        "Copy a collection (recursively) in to another collection (POST /v1/collections/{collection_id}/subcollections/)"
        from .assets.api.collections import (
            post_collections_by_collection_id_subcollections as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            collection_id=collection_id,
            body=body,
            copy_acl=copy_acl,
            copy_keyframes=copy_keyframes,
        )

    def post_collection_views(self, collection_id: str):
        "Mark collection as viewed (POST /v1/collections/{collection_id}/views/)"
        from .assets.api.collections import (
            post_collections_by_collection_id_views as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"), collection_id=collection_id
        )

    def post_collections_reindex(self, *, body=UNSET):
        "Trigger reindexing of all collections (POST /v1/collections/reindex/)"
        from .assets.api.collections import post_collections_reindex as _endpoint

        return _endpoint.sync_detailed(client=self._client("assets"), body=body)

    def post_custom_actions_by_context(self, context: str, *, body):
        "Create an custom action (POST /v1/custom_actions/{context}/)"
        from .assets.api.custom_actions import (
            post_custom_actions_by_context as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"), context=context, body=body
        )

    def post_custom_actions_callback_by_context_by_action(
        self, context: str, action_id: str, *, body
    ):
        "Schedules a celery task that will call custom action (POST /v1/custom_actions/{context}/{action_id}/callback/)"
        from .assets.api.custom_actions import (
            post_custom_actions_by_context_by_action_id_callback as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            context=context,
            action_id=action_id,
            body=body,
        )

    def post_custom_actions_shared_callback_by_context_by_action(
        self, context: str, action_id: str, *, body
    ):
        "Schedules a celery task that will call custom action on shares (POST /v1/custom_actions/shared/{context}/{action_id}/callback/)"
        from .assets.api.custom_actions import (
            post_custom_actions_shared_by_context_by_action_id_callback as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            context=context,
            action_id=action_id,
            body=body,
        )

    def post_delete_queue_assets(self, *, body):
        "Add assets to a delete queue (Mark assets as deleted) (POST /v1/delete_queue/assets/)"
        from .assets.api.delete_queue import post_delete_queue_assets as _endpoint

        return _endpoint.sync_detailed(client=self._client("assets"), body=body)

    def post_delete_queue_assets_purge(self, *, body):
        "Purge assets from delete queue (Permanently delete) (POST /v1/delete_queue/assets/purge/)"
        from .assets.api.delete_queue import post_delete_queue_assets_purge as _endpoint

        return _endpoint.sync_detailed(client=self._client("assets"), body=body)

    def post_delete_queue_assets_purge_all(self):
        "Purge all assets from delete queue (Permanently delete) (POST /v1/delete_queue/assets/purge/all/)"
        from .assets.api.delete_queue import (
            post_delete_queue_assets_purge_all as _endpoint,
        )

        return _endpoint.sync_detailed(client=self._client("assets"))

    def post_delete_queue_assets_restore_all(self):
        "Restore all assets from delete queue (POST /v1/delete_queue/assets/restore/all/)"
        from .assets.api.delete_queue import (
            post_delete_queue_assets_restore_all as _endpoint,
        )

        return _endpoint.sync_detailed(client=self._client("assets"))

    def post_delete_queue_bulk(self, *, body):
        "Bulk delete objects (POST /v1/delete_queue/bulk/)"
        from .assets.api.delete_queue import post_delete_queue_bulk as _endpoint

        return _endpoint.sync_detailed(client=self._client("assets"), body=body)

    def post_delete_queue_collections(self, *, body):
        "Add collections to a delete queue (Mark collections as deleted) (POST /v1/delete_queue/collections/)"
        from .assets.api.delete_queue import post_delete_queue_collections as _endpoint

        return _endpoint.sync_detailed(client=self._client("assets"), body=body)

    def post_delete_queue_collections_purge(self, *, body):
        "Purge collections from delete queue (Permanently delete) (POST /v1/delete_queue/collections/purge/)"
        from .assets.api.delete_queue import (
            post_delete_queue_collections_purge as _endpoint,
        )

        return _endpoint.sync_detailed(client=self._client("assets"), body=body)

    def post_delete_queue_collections_purge_all(self):
        "Purge all collections from delete queue (Permanently delete) (POST /v1/delete_queue/collections/purge/all/)"
        from .assets.api.delete_queue import (
            post_delete_queue_collections_purge_all as _endpoint,
        )

        return _endpoint.sync_detailed(client=self._client("assets"))

    def post_delete_queue_collections_restore_all(self):
        "Restore all collections from delete queue (POST /v1/delete_queue/collections/restore/all/)"
        from .assets.api.delete_queue import (
            post_delete_queue_collections_restore_all as _endpoint,
        )

        return _endpoint.sync_detailed(client=self._client("assets"))

    def post_delete_queue_purge_all(self):
        "Purge all assets and collections from delete queue (Permanently delete) (POST /v1/delete_queue/purge/all/)"
        from .assets.api.delete_queue import post_delete_queue_purge_all as _endpoint

        return _endpoint.sync_detailed(client=self._client("assets"))

    def post_favorites_assets(self, *, body):
        "Adds multiple objects to a list of favorites (POST /v1/favorites/)"
        from .assets.api.favorites import post_favorites as _endpoint

        return _endpoint.sync_detailed(client=self._client("assets"), body=body)

    def post_playlists(self, *, body):
        "Create a new playlist (POST /v1/playlists/)"
        from .assets.api.playlists import post_playlists as _endpoint

        return _endpoint.sync_detailed(client=self._client("assets"), body=body)

    def post_playlist_items(self, playlist_id: str, *, body):
        "Add an item to a playlist (POST /v1/playlists/{playlist_id}/items/)"
        from .assets.api.playlists import (
            post_playlists_by_playlist_id_items as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"), playlist_id=playlist_id, body=body
        )

    def post_playlist_keyframes_assets(self, playlist_id: str, *, body):
        "Pick up to three asset_ids for playlist keyframes (POST /v1/playlists/{playlist_id}/keyframes/)"
        from .assets.api.playlists import (
            post_playlists_by_playlist_id_keyframes as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"), playlist_id=playlist_id, body=body
        )

    def post_playlist_reindex(self, playlist_id: str, *, body):
        "Reindex the playlist (POST /v1/playlists/{playlist_id}/reindex/)"
        from .assets.api.playlists import (
            post_playlists_by_playlist_id_reindex as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"), playlist_id=playlist_id, body=body
        )

    def post_projects(self, *, body):
        "Create a new project (POST /v1/projects/)"
        from .assets.api.projects import post_projects as _endpoint

        return _endpoint.sync_detailed(client=self._client("assets"), body=body)

    def post_project_members(self, project_id: str, *, body):
        "Add a member to a project (POST /v1/projects/{project_id}/members/)"
        from .assets.api.projects import (
            post_projects_by_project_id_members as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"), project_id=project_id, body=body
        )

    def post_project_reindex(self, project_id: str, *, body):
        "Reindex the project (POST /v1/projects/{project_id}/reindex/)"
        from .assets.api.projects import (
            post_projects_by_project_id_reindex as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"), project_id=project_id, body=body
        )

    def post_publications_jobs(self, *, body):
        "\u26a0\ufe0f Beta: Schedules publishing for an asset to a list of destinations based on template_id (POST /v1/publications/jobs/)"
        from .assets.api.publications import post_publications_jobs as _endpoint

        return _endpoint.sync_detailed(client=self._client("assets"), body=body)

    def post_reindex_bulk(self, *, body):
        "Create a job for bulk reindexing of assets (POST /v1/reindex/bulk/)"
        from .assets.api.reindex import post_reindex_bulk as _endpoint

        return _endpoint.sync_detailed(client=self._client("assets"), body=body)

    def post_segments_reindex(self, *, body):
        "Trigger reindexing of specific segment ids (POST /v1/segments/reindex/)"
        from .assets.api.segments import post_segments_reindex as _endpoint

        return _endpoint.sync_detailed(client=self._client("assets"), body=body)

    def post_sequences(self, *, body):
        "Create a new sequence (POST /v1/sequences/)"
        from .assets.api.sequences import post_sequences as _endpoint

        return _endpoint.sync_detailed(client=self._client("assets"), body=body)

    def post_sequence_items(self, sequence_id: str, *, body):
        "Add an item to a sequence (POST /v1/sequences/{sequence_id}/items/)"
        from .assets.api.sequences import (
            post_sequences_by_sequence_id_items as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"), sequence_id=sequence_id, body=body
        )

    def post_sequence_reindex(self, sequence_id: str, *, body):
        "Reindex the sequence (POST /v1/sequences/{sequence_id}/reindex/)"
        from .assets.api.sequences import (
            post_sequences_by_sequence_id_reindex as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"), sequence_id=sequence_id, body=body
        )

    def post_share_object(self, object_type: str, *, body):
        "Create a new share of multiple objects (currently only assets are supported) (POST /v1/share/{object_type}/)"
        from .assets.api.share import post_share_by_object_type as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("assets"), object_type=object_type, body=body
        )

    def post_shares_allowlist_entries(self, *, body):
        "Create a new magic link allowlist entry. (POST /v1/shares/allowlist/entries/)"
        from .assets.api.shares import post_shares_allowlist_entries as _endpoint

        return _endpoint.sync_detailed(client=self._client("assets"), body=body)

    def post_shares_auth_login(self, *, body):
        "Login for share (POST /v1/shares/auth/login/)"
        from .assets.api.shares import post_shares_auth_login as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("assets", ("App-ID",)), body=body
        )

    def post_share_magic_link_request(self, share_id: str, *, body):
        "Request a magic link for share access. (POST /v1/shares/{share_id}/magic_link/request/)"
        from .assets.api.shares import (
            post_shares_by_share_id_magic_link_request as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets", ()), share_id=share_id, body=body
        )

    def post_share_magic_link_validate(self, share_id: str, *, body):
        "Validates the email and single-use hash, and returns a share authorization token. (POST /v1/shares/{share_id}/magic_link/validate/)"
        from .assets.api.shares import (
            post_shares_by_share_id_magic_link_validate as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets", ()), share_id=share_id, body=body
        )

    def post_shares_magic_link_enabled(self, *, body):
        "Check if magic link authentication is enabled for the share's system domain. (POST /v1/shares/magic_link/enabled/)"
        from .assets.api.shares import post_shares_magic_link_enabled as _endpoint

        return _endpoint.sync_detailed(client=self._client("assets", ()), body=body)

    def post_sync_sessions(self, *, body):
        "Create a new sync session (POST /v1/sync/sessions/)"
        from .assets.api.sync import post_sync_sessions as _endpoint

        return _endpoint.sync_detailed(client=self._client("assets"), body=body)

    def put_assets(self, *, body):
        "Bulk update assets (PUT /v1/assets/)"
        from .assets.api.assets import put_assets as _endpoint

        return _endpoint.sync_detailed(client=self._client("assets"), body=body)

    def put_asset(self, asset_id: str, *, body, generate_subclip_keyframes=UNSET):
        "Update asset (PUT /v1/assets/{asset_id}/)"
        from .assets.api.assets import put_assets_by_asset_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            asset_id=asset_id,
            body=body,
            generate_subclip_keyframes=generate_subclip_keyframes,
        )

    def put_asset_restore(self, asset_id: str):
        "Restore deleted asset by id (PUT /v1/assets/{asset_id}/restore/)"
        from .assets.api.assets import put_assets_by_asset_id_restore as _endpoint

        return _endpoint.sync_detailed(client=self._client("assets"), asset_id=asset_id)

    def put_asset_search_document(self, asset_id: str, *, body):
        "Update metadata for asset (PUT /v1/assets/{asset_id}/search_document/)"
        from .assets.api.assets import (
            put_assets_by_asset_id_search_document as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"), asset_id=asset_id, body=body
        )

    def put_asset_segments_bulk(
        self, asset_id: str, *, body, generate_subclip_keyframes=UNSET
    ):
        "Edit multiple asset segments (PUT /v1/assets/{asset_id}/segments/bulk/)"
        from .assets.api.assets import put_assets_by_asset_id_segments_bulk as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            asset_id=asset_id,
            body=body,
            generate_subclip_keyframes=generate_subclip_keyframes,
        )

    def put_asset_segment(
        self, asset_id: str, segment_id: str, *, body, generate_subclip_keyframes=UNSET
    ):
        "Update segment (PUT /v1/assets/{asset_id}/segments/{segment_id}/)"
        from .assets.api.assets import (
            put_assets_by_asset_id_segments_by_segment_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            asset_id=asset_id,
            segment_id=segment_id,
            body=body,
            generate_subclip_keyframes=generate_subclip_keyframes,
        )

    def put_asset_version(self, asset_id: str, version_id: str, *, body):
        "Edit asset version (PUT /v1/assets/{asset_id}/versions/{version_id}/)"
        from .assets.api.assets import (
            put_assets_by_asset_id_versions_by_version_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            asset_id=asset_id,
            version_id=version_id,
            body=body,
        )

    def put_asset_version_promote(self, asset_id: str, version_id: str):
        "Promote a particular asset version to a latest version (PUT /v1/assets/{asset_id}/versions/{version_id}/promote/)"
        from .assets.api.assets import (
            put_assets_by_asset_id_versions_by_version_id_promote as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"), asset_id=asset_id, version_id=version_id
        )

    def put_asset_version_transcription_properties(
        self, asset_id: str, version_id: str, transcription_id: str, *, body
    ):
        "Update transcription properties by ID (PUT /v1/assets/{asset_id}/versions/{version_id}/transcriptions/{transcription_id}/properties/)"
        from .assets.api.assets import (
            put_assets_by_asset_id_versions_by_version_id_transcriptions_by_transcription_id_properties as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            asset_id=asset_id,
            version_id=version_id,
            transcription_id=transcription_id,
            body=body,
        )

    def put_assets_relation_types_by_relation_type(self, relation_type: str, *, body):
        "Update an asset relation type (PUT /v1/assets/relation_types/{relation_type}/)"
        from .assets.api.assets import (
            put_assets_relation_types_by_relation_type as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"), relation_type=relation_type, body=body
        )

    def put_object_approvals(self, object_type: str, object_id: str, *, body):
        "Adds the approval by user and returns an objects approval status (PUT /v1/{object_type}/{object_id}/approvals/)"
        from .assets.api.object_type import (
            put_by_object_type_by_object_id_approvals as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            object_type=object_type,
            object_id=object_id,
            body=body,
        )

    def put_object_approvals_request(self, object_type: str, object_id: str, *, body):
        "Edits an approval request (PUT /v1/{object_type}/{object_id}/approvals/request/)"
        from .assets.api.object_type import (
            put_by_object_type_by_object_id_approvals_request as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            object_type=object_type,
            object_id=object_id,
            body=body,
        )

    def put_object_share(
        self, object_type: str, object_id: str, share_id: str, *, body
    ):
        "Update share (PUT /v1/{object_type}/{object_id}/shares/{share_id}/)"
        from .assets.api.object_type import (
            put_by_object_type_by_object_id_shares_by_share_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            object_type=object_type,
            object_id=object_id,
            share_id=share_id,
            body=body,
        )

    def put_object_share_users_by_share_user(
        self,
        object_type: str,
        object_id: str,
        share_id: str,
        share_user_id: str,
        *,
        body,
    ):
        "Update share user (PUT /v1/{object_type}/{object_id}/shares/{share_id}/users/{share_user_id}/)"
        from .assets.api.object_type import (
            put_by_object_type_by_object_id_shares_by_share_id_users_by_share_user_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            object_type=object_type,
            object_id=object_id,
            share_id=share_id,
            share_user_id=share_user_id,
            body=body,
        )

    def put_collection(self, collection_id: str, *, body, change_parent_mode=UNSET):
        "Update collection (PUT /v1/collections/{collection_id}/)"
        from .assets.api.collections import (
            put_collections_by_collection_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            collection_id=collection_id,
            body=body,
            change_parent_mode=change_parent_mode,
        )

    def put_collection_contents_object(
        self, collection_id: str, object_type: str, object_id: str, *, body
    ):
        "Update an order of a particular content object in a collection (PUT /v1/collections/{collection_id}/contents/{object_type}/{object_id}/)"
        from .assets.api.collections import (
            put_collections_by_collection_id_contents_by_object_type_by_object_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            collection_id=collection_id,
            object_type=object_type,
            object_id=object_id,
            body=body,
        )

    def put_collection_restore(self, collection_id: str):
        "Restore deleted collection by id (PUT /v1/collections/{collection_id}/restore/)"
        from .assets.api.collections import (
            put_collections_by_collection_id_restore as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"), collection_id=collection_id
        )

    def put_collection_search_document(self, collection_id: str, *, body):
        "Update metadata for collection (PUT /v1/collections/{collection_id}/search_document/)"
        from .assets.api.collections import (
            put_collections_by_collection_id_search_document as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"), collection_id=collection_id, body=body
        )

    def put_custom_actions_by_context_by_action(
        self, context: str, action_id: str, *, body
    ):
        "Update an custom action (PUT /v1/custom_actions/{context}/{action_id}/)"
        from .assets.api.custom_actions import (
            put_custom_actions_by_context_by_action_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            context=context,
            action_id=action_id,
            body=body,
        )

    def put_playlist(self, playlist_id: str, *, body):
        "Update a playlist (PUT /v1/playlists/{playlist_id}/)"
        from .assets.api.playlists import put_playlists_by_playlist_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("assets"), playlist_id=playlist_id, body=body
        )

    def put_playlist_item(self, playlist_id: str, item_id: str, *, body):
        "Update a playlist item (PUT /v1/playlists/{playlist_id}/items/{item_id}/)"
        from .assets.api.playlists import (
            put_playlists_by_playlist_id_items_by_item_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            playlist_id=playlist_id,
            item_id=item_id,
            body=body,
        )

    def put_playlist_item_position(self, playlist_id: str, item_id: str, *, body):
        "Update a playlist item position (PUT /v1/playlists/{playlist_id}/items/{item_id}/position/)"
        from .assets.api.playlists import (
            put_playlists_by_playlist_id_items_by_item_id_position as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            playlist_id=playlist_id,
            item_id=item_id,
            body=body,
        )

    def put_project(self, project_id: str, *, body):
        "Update project (PUT /v1/projects/{project_id}/)"
        from .assets.api.projects import put_projects_by_project_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("assets"), project_id=project_id, body=body
        )

    def put_sequence(self, sequence_id: str, *, body):
        "Update a sequence (PUT /v1/sequences/{sequence_id}/)"
        from .assets.api.sequences import put_sequences_by_sequence_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("assets"), sequence_id=sequence_id, body=body
        )

    def put_sequence_item_position(self, sequence_id: str, item_id: str, *, body):
        "Update a sequence item position (PUT /v1/sequences/{sequence_id}/items/{item_id}/position/)"
        from .assets.api.sequences import (
            put_sequences_by_sequence_id_items_by_item_id_position as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            sequence_id=sequence_id,
            item_id=item_id,
            body=body,
        )

    def put_shares_allowlist_entry(self, entry_id: str, *, body):
        "Update an allowlist entry. (PUT /v1/shares/allowlist/entries/{entry_id}/)"
        from .assets.api.shares import (
            put_shares_allowlist_entries_by_entry_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("assets"), entry_id=entry_id, body=body
        )

    def put_shares_auth_token(self, *, share_auth_token):
        "Refreshes a token for share (PUT /v1/shares/auth/token/)"
        from .assets.api.shares import put_shares_auth_token as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("assets"), share_auth_token=share_auth_token
        )

    def put_sync_sessions_by_sync_session(
        self, sync_session_id: str, *, body, update_if_none=UNSET
    ):
        "Edit a sync session. If the session doesn't exist, a new one is created (PUT /v1/sync/sessions/{sync_session_id}/)"
        from .assets.api.sync import put_sync_sessions_by_sync_session_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("assets"),
            sync_session_id=sync_session_id,
            body=body,
            update_if_none=update_if_none,
        )

    def delete_app(self, app_id: str):
        "Delete a particular app by id (DELETE /v1/apps/{app_id}/)"
        from .auth.api.apps import delete_apps_by_app_id as _endpoint

        return _endpoint.sync_detailed(client=self._client("auth"), app_id=app_id)

    def delete_apps_instance_by_approved_instance(self, approved_instance_id: str):
        "Delete an approved instance of an app (DELETE /v1/apps/instance/{approved_instance_id}/)"
        from .auth.api.apps import (
            delete_apps_instance_by_approved_instance_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("auth"), approved_instance_id=approved_instance_id
        )

    def delete_auth_saml_domains_by_domain(self, domain: str):
        "Unbind domain from identity provider (DELETE /v1/auth/saml/domains/{domain}/)"
        from .auth.api.auth import delete_auth_saml_domains_by_domain as _endpoint

        return _endpoint.sync_detailed(client=self._client("auth"), domain=domain)

    def delete_auth_saml_idp_by_identity_provider(self, identity_provider_id: str):
        "Delete a particular identity provider by id (DELETE /v1/auth/saml/idp/{identity_provider_id}/)"
        from .auth.api.auth import (
            delete_auth_saml_idp_by_identity_provider_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("auth"), identity_provider_id=identity_provider_id
        )

    def delete_current_auth_token(self):
        "Revoke token (DELETE /v1/auth/token/)"
        from .auth.api.auth import delete_auth_token as _endpoint

        return _endpoint.sync_detailed(client=self._client("auth"))

    def delete_auth_token(self, token_id: str):
        "Revoke token by ID (DELETE /v1/auth/token/{token_id}/)"
        from .auth.api.auth import delete_auth_token_by_token_id as _endpoint

        return _endpoint.sync_detailed(client=self._client("auth"), token_id=token_id)

    def delete_referral_codes_by_code(self, code: str):
        "Delete a referral_code (DELETE /v1/referral_codes/{code}/)"
        from .auth.api.referral_codes import delete_referral_codes_by_code as _endpoint

        return _endpoint.sync_detailed(client=self._client("auth"), code=code)

    def delete_system_domain(self, system_domain_id: str):
        "Delete a particular system_domain by id (DELETE /v1/system_domains/{system_domain_id}/)"
        from .auth.api.system_domains import (
            delete_system_domains_by_system_domain_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("auth"), system_domain_id=system_domain_id
        )

    def delete_system_domain_e2e(self, system_domain_id: str):
        "Delete a particular system_domain by id. (DELETE /v1/system_domains/{system_domain_id}/e2e/)"
        from .auth.api.system_domains import (
            delete_system_domains_by_system_domain_id_e2_e as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("auth"), system_domain_id=system_domain_id
        )

    def delete_system_domain_logo(self, system_domain_id: str):
        "Delete system domain logo image. (DELETE /v1/system_domains/{system_domain_id}/logo/)"
        from .auth.api.system_domains import (
            delete_system_domains_by_system_domain_id_logo as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("auth"), system_domain_id=system_domain_id
        )

    def get_apps(self, *, per_page=UNSET, last_id=UNSET):
        "List of apps (GET /v1/apps/)"
        from .auth.api.apps import get_apps as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("auth"), per_page=per_page, last_id=last_id
        )

    def get_app(self, app_id: str):
        "Returns a particular app by id (GET /v1/apps/{app_id}/)"
        from .auth.api.apps import get_apps_by_app_id as _endpoint

        return _endpoint.sync_detailed(client=self._client("auth"), app_id=app_id)

    def get_apps_external_auth_by_secret(self, secret: str):
        "Gets a token requested by an external app (GET /v1/apps/external/auth/{secret}/)"
        from .auth.api.apps import get_apps_external_auth_by_secret as _endpoint

        return _endpoint.sync_detailed(client=self._client("auth", ()), secret=secret)

    def get_apps_instance_by_approved_instance(self, approved_instance_id: str):
        "Gets an approved instance of an app (GET /v1/apps/instance/{approved_instance_id}/)"
        from .auth.api.apps import (
            get_apps_instance_by_approved_instance_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("auth"), approved_instance_id=approved_instance_id
        )

    def get_auth_tokens_by_app(self, app_id: str, *, per_page=UNSET, last_id=UNSET):
        "List application tokens (GET /v1/auth/{app_id}/tokens/)"
        from .auth.api.auth import get_auth_by_app_id_tokens as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("auth"),
            app_id=app_id,
            per_page=per_page,
            last_id=last_id,
        )

    def get_auth_saml_idp(self, *, per_page=UNSET, last_id=UNSET):
        "Get list of identity providers (GET /v1/auth/saml/idp/)"
        from .auth.api.auth import get_auth_saml_idp as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("auth"), per_page=per_page, last_id=last_id
        )

    def get_auth_saml_idp_by_identity_provider(self, identity_provider_id: str):
        "Get a particular identity provider by id (GET /v1/auth/saml/idp/{identity_provider_id}/)"
        from .auth.api.auth import (
            get_auth_saml_idp_by_identity_provider_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("auth"), identity_provider_id=identity_provider_id
        )

    def get_auth_saml_metadata_by_public(self, public_id: str):
        "SAML Single Logout Service (GET /v1/auth/saml/metadata/{public_id}/)"
        from .auth.api.auth import get_auth_saml_metadata_by_public_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("auth", ()), public_id=public_id
        )

    def get_auth_saml_metadata_by_system_domain_by_identity_provider(
        self, system_domain_id: str, identity_provider_id: str
    ):
        "SAML Single Logout Service (GET /v1/auth/saml/metadata/{system_domain_id}/{identity_provider_id}/)"
        from .auth.api.auth import (
            get_auth_saml_metadata_by_system_domain_id_by_identity_provider_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("auth", ()),
            system_domain_id=system_domain_id,
            identity_provider_id=identity_provider_id,
        )

    def get_auth_saml_slo_by_public(self, public_id: str):
        "SAML Single Logout Service (GET /v1/auth/saml/slo/{public_id}/)"
        from .auth.api.auth import get_auth_saml_slo_by_public_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("auth", ()), public_id=public_id
        )

    def get_auth_saml_slo_by_system_domain_by_identity_provider(
        self, system_domain_id: str, identity_provider_id: str
    ):
        "SAML Single Logout Service (GET /v1/auth/saml/slo/{system_domain_id}/{identity_provider_id}/)"
        from .auth.api.auth import (
            get_auth_saml_slo_by_system_domain_id_by_identity_provider_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("auth", ()),
            system_domain_id=system_domain_id,
            identity_provider_id=identity_provider_id,
        )

    def get_auth_saml_sso_by_public(self, public_id: str):
        "SAML Single sign-on Service (GET /v1/auth/saml/sso/{public_id}/)"
        from .auth.api.auth import get_auth_saml_sso_by_public_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("auth", ()), public_id=public_id
        )

    def get_auth_saml_sso_by_system_domain_by_identity_provider(
        self, system_domain_id: str, identity_provider_id: str
    ):
        "SAML Single sign-on Service (GET /v1/auth/saml/sso/{system_domain_id}/{identity_provider_id}/)"
        from .auth.api.auth import (
            get_auth_saml_sso_by_system_domain_id_by_identity_provider_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("auth", ()),
            system_domain_id=system_domain_id,
            identity_provider_id=identity_provider_id,
        )

    def get_current_auth_token(self):
        "Check if auth token valid (GET /v1/auth/token/)"
        from .auth.api.auth import get_auth_token as _endpoint

        return _endpoint.sync_detailed(client=self._client("auth"))

    def get_auth_token(self, token_id: str):
        "Get token by ID (GET /v1/auth/token/{token_id}/)"
        from .auth.api.auth import get_auth_token_by_token_id as _endpoint

        return _endpoint.sync_detailed(client=self._client("auth"), token_id=token_id)

    def get_auth_tokens(self, *, per_page=UNSET, last_id=UNSET):
        "List of tokens (GET /v1/auth/tokens/)"
        from .auth.api.auth import get_auth_tokens as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("auth"), per_page=per_page, last_id=last_id
        )

    def get_oauth_authorize(
        self,
        *,
        client_id,
        redirect_uri,
        scope,
        response_type,
        code_challenge,
        code_challenge_method=UNSET,
    ):
        "Validate the authorization request and return consent metadata (GET /v1/oauth/authorize/)"
        from .auth.api.oauth import get_oauth_authorize as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("auth"),
            client_id=client_id,
            redirect_uri=redirect_uri,
            scope=scope,
            response_type=response_type,
            code_challenge=code_challenge,
            code_challenge_method=code_challenge_method,
        )

    def get_password_checks_by_reset_hash(self, reset_hash: str):
        "Returns a list of password checks required for the password to be safe (GET /v1/password/{reset_hash}/checks/)"
        from .auth.api.password import get_password_by_reset_hash_checks as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("auth", ()), reset_hash=reset_hash
        )

    def get_password_checks(self):
        "Returns a list of password checks required for the password to be safe (GET /v1/password/checks/)"
        from .auth.api.password import get_password_checks as _endpoint

        return _endpoint.sync_detailed(client=self._client("auth"))

    def get_referral_codes(self):
        "Get all referral_codes (GET /v1/referral_codes/)"
        from .auth.api.referral_codes import get_referral_codes as _endpoint

        return _endpoint.sync_detailed(client=self._client("auth"))

    def get_referral_codes_by_code(self, code: str):
        "Get a referral_code (GET /v1/referral_codes/{code}/)"
        from .auth.api.referral_codes import get_referral_codes_by_code as _endpoint

        return _endpoint.sync_detailed(client=self._client("auth"), code=code)

    def get_registrations_content(self, *, page_route):
        "Returns page content from Webflow collection (GET /v1/registrations/content/)"
        from .auth.api.registrations import get_registrations_content as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("auth"), page_route=page_route
        )

    def get_registrations_countries(self):
        "Returns list of countries (GET /v1/registrations/countries/)"
        from .auth.api.registrations import get_registrations_countries as _endpoint

        return _endpoint.sync_detailed(client=self._client("auth"))

    def get_system_domains(self, *, query=UNSET, statuses=UNSET):
        "List of system domains (GET /v1/system_domains/)"
        from .auth.api.system_domains import get_system_domains as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("auth"), query=query, statuses=statuses
        )

    def get_system_domains_basic_by_system_domain(self, system_domain_id: str):
        "Returns a particular system domain without details (GET /v1/system_domains/basic/{system_domain_id}/)"
        from .auth.api.system_domains import (
            get_system_domains_basic_by_system_domain_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("auth"), system_domain_id=system_domain_id
        )

    def get_system_domain(self, system_domain_id: str):
        "Returns a particular system domain by id (GET /v1/system_domains/{system_domain_id}/)"
        from .auth.api.system_domains import (
            get_system_domains_by_system_domain_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("auth"), system_domain_id=system_domain_id
        )

    def get_system_domains_search(
        self,
        *,
        page=UNSET,
        per_page=UNSET,
        sort=UNSET,
        query=UNSET,
        statuses=UNSET,
        types=UNSET,
        field_name=UNSET,
    ):
        "List of system domains from Elasticsearch (GET /v1/system_domains/search/)"
        from .auth.api.system_domains import get_system_domains_search as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("auth"),
            page=page,
            per_page=per_page,
            sort=sort,
            query=query,
            statuses=statuses,
            types=types,
            field_name=field_name,
        )

    def get_system_domains_templates(self):
        "List of system domain templates (GET /v1/system_domains/templates/)"
        from .auth.api.system_domains import get_system_domains_templates as _endpoint

        return _endpoint.sync_detailed(client=self._client("auth"))

    def patch_app(self, app_id: str, *, body):
        "Update app (PATCH /v1/apps/{app_id}/)"
        from .auth.api.apps import patch_apps_by_app_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("auth"), app_id=app_id, body=body
        )

    def patch_auth_saml_idp_by_identity_provider(
        self, identity_provider_id: str, *, body
    ):
        "Update a particular identity provider by id (PATCH /v1/auth/saml/idp/{identity_provider_id}/)"
        from .auth.api.auth import (
            patch_auth_saml_idp_by_identity_provider_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("auth"),
            identity_provider_id=identity_provider_id,
            body=body,
        )

    def patch_system_domain(self, system_domain_id: str, *, body):
        "Update system domain (PATCH /v1/system_domains/{system_domain_id}/)"
        from .auth.api.system_domains import (
            patch_system_domains_by_system_domain_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("auth"), system_domain_id=system_domain_id, body=body
        )

    def patch_system_domain_profile(self, system_domain_id: str, *, body):
        "Update system domain profile (PATCH /v1/system_domains/{system_domain_id}/profile/)"
        from .auth.api.system_domains import (
            patch_system_domains_by_system_domain_id_profile as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("auth"), system_domain_id=system_domain_id, body=body
        )

    def post_apps(self, *, body):
        "Create a new app (POST /v1/apps/)"
        from .auth.api.apps import post_apps as _endpoint

        return _endpoint.sync_detailed(client=self._client("auth"), body=body)

    def post_app_token(self, app_id: str, *, expires_in=UNSET):
        "Creates app token by id and returns it's data (POST /v1/apps/{app_id}/token/)"
        from .auth.api.apps import post_apps_by_app_id_token as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("auth"), app_id=app_id, expires_in=expires_in
        )

    def post_apps_external_auth(self, *, body):
        "Create a new token for the logged in user and store it for an external app (POST /v1/apps/external/auth/)"
        from .auth.api.apps import post_apps_external_auth as _endpoint

        return _endpoint.sync_detailed(client=self._client("auth"), body=body)

    def post_apps_instance(self, *, body):
        "Create a new app instance (POST /v1/apps/instance/)"
        from .auth.api.apps import post_apps_instance as _endpoint

        return _endpoint.sync_detailed(client=self._client("auth"), body=body)

    def post_auth_ad_login(self, *, body):
        "Login by ActiveDirectory (POST /v1/auth/ad/login/)"
        from .auth.api.auth import post_auth_ad_login as _endpoint

        return _endpoint.sync_detailed(client=self._client("auth", ()), body=body)

    def post_auth_current_otp_generate(self):
        "Request OTP code as an authenticated user (POST /v1/auth/current/otp/generate/)"
        from .auth.api.auth import post_auth_current_otp_generate as _endpoint

        return _endpoint.sync_detailed(client=self._client("auth"))

    def post_auth_multidomain_login(self, *, body, temp_auth_token):
        "Login by using temp token (POST /v1/auth/multidomain/login/)"
        from .auth.api.auth import post_auth_multidomain_login as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("auth", ()), body=body, temp_auth_token=temp_auth_token
        )

    def post_auth_otp_generate(self, *, body, temp_auth_token):
        "Request OTP code (POST /v1/auth/otp/generate/)"
        from .auth.api.auth import post_auth_otp_generate as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("auth", ()), body=body, temp_auth_token=temp_auth_token
        )

    def post_auth_saml_acs_by_public(self, public_id: str):
        "SAML Assertion Consumer Service (POST /v1/auth/saml/acs/{public_id}/)"
        from .auth.api.auth import post_auth_saml_acs_by_public_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("auth", ()), public_id=public_id
        )

    def post_auth_saml_acs_by_system_domain_by_identity_provider(
        self, system_domain_id: str, identity_provider_id: str
    ):
        "SAML Assertion Consumer Service (POST /v1/auth/saml/acs/{system_domain_id}/{identity_provider_id}/)"
        from .auth.api.auth import (
            post_auth_saml_acs_by_system_domain_id_by_identity_provider_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("auth", ()),
            system_domain_id=system_domain_id,
            identity_provider_id=identity_provider_id,
        )

    def post_auth_saml_domains(self, *, body):
        "Bind domain to identity provider (POST /v1/auth/saml/domains/)"
        from .auth.api.auth import post_auth_saml_domains as _endpoint

        return _endpoint.sync_detailed(client=self._client("auth"), body=body)

    def post_auth_saml_idp(self, *, body=UNSET):
        "Create a new identity provider. (POST /v1/auth/saml/idp/)"
        from .auth.api.auth import post_auth_saml_idp as _endpoint

        return _endpoint.sync_detailed(client=self._client("auth"), body=body)

    def post_auth_saml_idp_convert(self, *, body):
        "Convert an IdP EntityDescriptor XML into json suitable as a settings configuration. (POST /v1/auth/saml/idp/convert/)"
        from .auth.api.auth import post_auth_saml_idp_convert as _endpoint

        return _endpoint.sync_detailed(client=self._client("auth"), body=body)

    def post_auth_saml_login(self, *, body):
        "SAML Single sign-on url by domain (POST /v1/auth/saml/login/)"
        from .auth.api.auth import post_auth_saml_login as _endpoint

        return _endpoint.sync_detailed(client=self._client("auth", ()), body=body)

    def post_auth_saml_logout_by_public(self, public_id: str):
        "Initiate SAML Single logout (POST /v1/auth/saml/logout/{public_id}/)"
        from .auth.api.auth import post_auth_saml_logout_by_public_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("auth", ()), public_id=public_id
        )

    def post_auth_saml_multidomain_login(self, *, body):
        "SAML Single sign-on url by domain (POST /v1/auth/saml/multidomain/login/)"
        from .auth.api.auth import post_auth_saml_multidomain_login as _endpoint

        return _endpoint.sync_detailed(client=self._client("auth", ()), body=body)

    def post_auth_simple_login(self, *, body):
        "Login by using email and password (POST /v1/auth/simple/login/)"
        from .auth.api.auth import post_auth_simple_login as _endpoint

        return _endpoint.sync_detailed(client=self._client("auth", ()), body=body)

    def post_auth_token(self, *, expires_in=UNSET):
        "Create new token without invalidating the old one (POST /v1/auth/token/)"
        from .auth.api.auth import post_auth_token as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("auth"), expires_in=expires_in
        )

    def post_marketplace_google_link(self, *, body):
        "Google cloud marketplace link to existing system domain (POST /v1/marketplace/google/link/)"
        from .auth.api.marketplace import post_marketplace_google_link as _endpoint

        return _endpoint.sync_detailed(client=self._client("auth", ()), body=body)

    def post_marketplace_google_signup(self, *, body=UNSET):
        "Google cloud marketplace signup (POST /v1/marketplace/google/signup/)"
        from .auth.api.marketplace import post_marketplace_google_signup as _endpoint

        return _endpoint.sync_detailed(client=self._client("auth", ()), body=body)

    def post_oauth_authorize(
        self,
        *,
        client_id,
        redirect_uri,
        scope,
        response_type,
        code_challenge,
        code_challenge_method=UNSET,
    ):
        "Submit the user's consent decision. If ``confirm`` is present in (POST /v1/oauth/authorize/)"
        from .auth.api.oauth import post_oauth_authorize as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("auth"),
            client_id=client_id,
            redirect_uri=redirect_uri,
            scope=scope,
            response_type=response_type,
            code_challenge=code_challenge,
            code_challenge_method=code_challenge_method,
        )

    def post_oauth_token(self, *, body):
        "Issue an OAuth token (POST /v1/oauth/token/)"
        from .auth.api.oauth import post_oauth_token as _endpoint

        return _endpoint.sync_detailed(client=self._client("auth", ()), body=body)

    def post_password_forgot(self, *, body):
        "Receives email address and sends email to this address with a link for resetting password. (POST /v1/password/forgot/)"
        from .auth.api.password import post_password_forgot as _endpoint

        return _endpoint.sync_detailed(client=self._client("auth", ()), body=body)

    def post_referral_codes(self, *, body):
        "Create a new referral_code (POST /v1/referral_codes/)"
        from .auth.api.referral_codes import post_referral_codes as _endpoint

        return _endpoint.sync_detailed(client=self._client("auth"), body=body)

    def post_registrations(self, *, body):
        "Create a new registration (POST /v1/registrations/)"
        from .auth.api.registrations import post_registrations as _endpoint

        return _endpoint.sync_detailed(client=self._client("auth", ()), body=body)

    def post_registrations_verify_by_email_hash(self, email_hash: str):
        "Verify email address, create system domain from template, and authenticate user (POST /v1/registrations/verify/{email_hash}/)"
        from .auth.api.registrations import (
            post_registrations_verify_by_email_hash as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("auth", ()), email_hash=email_hash
        )

    def post_system_domains(self, *, body):
        "Create a new system domain (POST /v1/system_domains/)"
        from .auth.api.system_domains import post_system_domains as _endpoint

        return _endpoint.sync_detailed(client=self._client("auth"), body=body)

    def post_system_domain_features(self, system_domain_id: str, *, body):
        "Enable specified feature on a system domain (POST /v1/system_domains/{system_domain_id}/features/)"
        from .auth.api.system_domains import (
            post_system_domains_by_system_domain_id_features as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("auth"), system_domain_id=system_domain_id, body=body
        )

    def post_system_domain_logo(self, system_domain_id: str, *, body):
        "Upload system domain logo image. (POST /v1/system_domains/{system_domain_id}/logo/)"
        from .auth.api.system_domains import (
            post_system_domains_by_system_domain_id_logo as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("auth"), system_domain_id=system_domain_id, body=body
        )

    def post_system_domain_reindex(self, system_domain_id: str, *, body):
        "Reindex system_domain (POST /v1/system_domains/{system_domain_id}/reindex/)"
        from .auth.api.system_domains import (
            post_system_domains_by_system_domain_id_reindex as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("auth"), system_domain_id=system_domain_id, body=body
        )

    def post_system_domains_referral_code_by_referral_code(
        self, referral_code: str, *, body
    ):
        "Create a new system domain from a referral code (That is associated to your domain) (POST /v1/system_domains/referral_code/{referral_code}/)"
        from .auth.api.system_domains import (
            post_system_domains_referral_code_by_referral_code as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("auth"), referral_code=referral_code, body=body
        )

    def put_app(self, app_id: str, *, body):
        "Update app (PUT /v1/apps/{app_id}/)"
        from .auth.api.apps import put_apps_by_app_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("auth"), app_id=app_id, body=body
        )

    def put_auth_saml_idp_by_identity_provider(
        self, identity_provider_id: str, *, body
    ):
        "Update a particular identity provider by id (PUT /v1/auth/saml/idp/{identity_provider_id}/)"
        from .auth.api.auth import (
            put_auth_saml_idp_by_identity_provider_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("auth"),
            identity_provider_id=identity_provider_id,
            body=body,
        )

    def put_auth_token(self):
        "Refresh token (PUT /v1/auth/token/)"
        from .auth.api.auth import put_auth_token as _endpoint

        return _endpoint.sync_detailed(client=self._client("auth"))

    def put_invitation_complete_by_reset_hash(self, reset_hash: str, *, body):
        "Completes invitation by setting password and other user details (PUT /v1/invitation/complete/{reset_hash}/)"
        from .auth.api.invitation import (
            put_invitation_complete_by_reset_hash as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("auth", ()), reset_hash=reset_hash, body=body
        )

    def put_password_reset_by_reset_hash(self, reset_hash: str, *, body):
        "Changes password to a new one (PUT /v1/password/reset/{reset_hash}/)"
        from .auth.api.password import put_password_reset_by_reset_hash as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("auth", ()), reset_hash=reset_hash, body=body
        )

    def put_system_domain(self, system_domain_id: str, *, body):
        "Update system domain (PUT /v1/system_domains/{system_domain_id}/)"
        from .auth.api.system_domains import (
            put_system_domains_by_system_domain_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("auth"), system_domain_id=system_domain_id, body=body
        )

    def delete_automation(self, automation_id: str):
        "Delete a particular automation by id (DELETE /v1/automations/{automation_id}/)"
        from .automations.api.automations import (
            delete_automations_by_automation_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("automations"), automation_id=automation_id
        )

    def delete_automation_history_object_by_version(
        self, automation_id: str, object_type: str, object_id: str, version_id: str
    ):
        "Delete history event (DELETE /v1/automations/{automation_id}/history/{object_type}/{object_id}/{version_id}/)"
        from .automations.api.automations import (
            delete_automations_by_automation_id_history_by_object_type_by_object_id_by_version_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("automations"),
            automation_id=automation_id,
            object_type=object_type,
            object_id=object_id,
            version_id=version_id,
        )

    def get_automations(self):
        "List of automations (GET /v1/automations/)"
        from .automations.api.automations import get_automations as _endpoint

        return _endpoint.sync_detailed(client=self._client("automations"))

    def get_automation(self, automation_id: str):
        "Returns a particular automation by id (GET /v1/automations/{automation_id}/)"
        from .automations.api.automations import (
            get_automations_by_automation_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("automations"), automation_id=automation_id
        )

    def get_automation_history_object_by_version(
        self, automation_id: str, object_type: str, object_id: str, version_id: str
    ):
        "Returns a particular history entity by id (GET /v1/automations/{automation_id}/history/{object_type}/{object_id}/{version_id}/)"
        from .automations.api.automations import (
            get_automations_by_automation_id_history_by_object_type_by_object_id_by_version_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("automations"),
            automation_id=automation_id,
            object_type=object_type,
            object_id=object_id,
            version_id=version_id,
        )

    def get_automation_runs_estimate(self, automation_id: str):
        "Get estimated number objects that might be affected by an automation run (GET /v1/automations/{automation_id}/runs/estimate/)"
        from .automations.api.automations import (
            get_automations_by_automation_id_runs_estimate as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("automations"), automation_id=automation_id
        )

    def patch_automation(self, automation_id: str, *, body):
        "Update automation (PATCH /v1/automations/{automation_id}/)"
        from .automations.api.automations import (
            patch_automations_by_automation_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("automations"), automation_id=automation_id, body=body
        )

    def post_automations(self, *, body):
        "Create a new automation (POST /v1/automations/)"
        from .automations.api.automations import post_automations as _endpoint

        return _endpoint.sync_detailed(client=self._client("automations"), body=body)

    def post_automation_history(self, automation_id: str, *, body, ttl=UNSET):
        "Create a new history entity (POST /v1/automations/{automation_id}/history/)"
        from .automations.api.automations import (
            post_automations_by_automation_id_history as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("automations"),
            automation_id=automation_id,
            body=body,
            ttl=ttl,
        )

    def post_automation_runs(self, automation_id: str):
        "Run an automation for existing objects (POST /v1/automations/{automation_id}/runs/)"
        from .automations.api.automations import (
            post_automations_by_automation_id_runs as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("automations"), automation_id=automation_id
        )

    def put_automation(self, automation_id: str, *, body):
        "Update automation (PUT /v1/automations/{automation_id}/)"
        from .automations.api.automations import (
            put_automations_by_automation_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("automations"), automation_id=automation_id, body=body
        )

    def delete_analysis_profile(self, profile_id: str):
        "Delete an analysis profile (DELETE /v1/analysis/profiles/{profile_id}/)"
        from .files.api.analysis import (
            delete_analysis_profiles_by_profile_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), profile_id=profile_id
        )

    def delete_analysis_profile_default(self, profile_id: str):
        "Removes the default flag on an analysis profile (DELETE /v1/analysis/profiles/{profile_id}/default/)"
        from .files.api.analysis import (
            delete_analysis_profiles_by_profile_id_default as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), profile_id=profile_id
        )

    def delete_analysis_service_accounts_by_analysis_service_account(
        self, analysis_service_account_id: str
    ):
        "Delete an analysis service account (DELETE /v1/analysis/service_accounts/{analysis_service_account_id}/)"
        from .files.api.analysis import (
            delete_analysis_service_accounts_by_analysis_service_account_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            analysis_service_account_id=analysis_service_account_id,
        )

    def delete_asset_file_set(
        self, asset_id: str, file_set_id: str, *, keep_source=UNSET, immediately=UNSET
    ):
        "Delete asset's file set, file entries, and actual files (DELETE /v1/assets/{asset_id}/file_sets/{file_set_id}/)"
        from .files.api.assets import (
            delete_assets_by_asset_id_file_sets_by_file_set_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            file_set_id=file_set_id,
            keep_source=keep_source,
            immediately=immediately,
        )

    def delete_asset_file_set_purge(self, asset_id: str, file_set_id: str):
        "Purge deleted asset's file set, file entries, and actual files. (DELETE /v1/assets/{asset_id}/file_sets/{file_set_id}/purge/)"
        from .files.api.assets import (
            delete_assets_by_asset_id_file_sets_by_file_set_id_purge as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), asset_id=asset_id, file_set_id=file_set_id
        )

    def delete_asset_file(self, asset_id: str, file_id: str):
        "Delete asset's file entry (Not the actual file, use DELETE file_set for that) (DELETE /v1/assets/{asset_id}/files/{file_id}/)"
        from .files.api.assets import (
            delete_assets_by_asset_id_files_by_file_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), asset_id=asset_id, file_id=file_id
        )

    def delete_asset_format(self, asset_id: str, format_id: str, *, immediately=UNSET):
        "Delete asset's format (DELETE /v1/assets/{asset_id}/formats/{format_id}/)"
        from .files.api.assets import (
            delete_assets_by_asset_id_formats_by_format_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            format_id=format_id,
            immediately=immediately,
        )

    def delete_asset_format_archive(self, asset_id: str, format_id: str, *, body):
        "Delete archived format (DELETE /v1/assets/{asset_id}/formats/{format_id}/archive/)"
        from .files.api.assets import (
            delete_assets_by_asset_id_formats_by_format_id_archive as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            format_id=format_id,
            body=body,
        )

    def delete_asset_format_component(
        self, asset_id: str, format_id: str, component_id: str
    ):
        "Delete a component in a format (DELETE /v1/assets/{asset_id}/formats/{format_id}/components/{component_id}/)"
        from .files.api.assets import (
            delete_assets_by_asset_id_formats_by_format_id_components_by_component_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            format_id=format_id,
            component_id=component_id,
        )

    def delete_asset_format_purge(self, asset_id: str, format_id: str):
        "Purge deleted asset's format (DELETE /v1/assets/{asset_id}/formats/{format_id}/purge/)"
        from .files.api.assets import (
            delete_assets_by_asset_id_formats_by_format_id_purge as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), asset_id=asset_id, format_id=format_id
        )

    def delete_asset_keyframe(
        self, asset_id: str, keyframe_id: str, *, keep_poster=UNSET
    ):
        "Delete asset's keyframe (DELETE /v1/assets/{asset_id}/keyframes/{keyframe_id}/)"
        from .files.api.assets import (
            delete_assets_by_asset_id_keyframes_by_keyframe_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            keyframe_id=keyframe_id,
            keep_poster=keep_poster,
        )

    def delete_asset_keyframe_public(self, asset_id: str, keyframe_id: str):
        "Make the keyframe link private (DELETE /v1/assets/{asset_id}/keyframes/{keyframe_id}/public/)"
        from .files.api.assets import (
            delete_assets_by_asset_id_keyframes_by_keyframe_id_public as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), asset_id=asset_id, keyframe_id=keyframe_id
        )

    def delete_asset_proxy(self, asset_id: str, proxy_id: str):
        "Delete asset's proxy (DELETE /v1/assets/{asset_id}/proxies/{proxy_id}/)"
        from .files.api.assets import (
            delete_assets_by_asset_id_proxies_by_proxy_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), asset_id=asset_id, proxy_id=proxy_id
        )

    def delete_asset_proxy_public(self, asset_id: str, proxy_id: str):
        "Make the proxy link private (DELETE /v1/assets/{asset_id}/proxies/{proxy_id}/public/)"
        from .files.api.assets import (
            delete_assets_by_asset_id_proxies_by_proxy_id_public as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), asset_id=asset_id, proxy_id=proxy_id
        )

    def delete_asset_subtitle(self, asset_id: str, subtitle_id: str):
        "Delete asset's subtitle (DELETE /v1/assets/{asset_id}/subtitles/{subtitle_id}/)"
        from .files.api.assets import (
            delete_assets_by_asset_id_subtitles_by_subtitle_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), asset_id=asset_id, subtitle_id=subtitle_id
        )

    def delete_asset_subtitle_cc(self, asset_id: str, subtitle_id: str):
        "Delete asset's subtitle (DELETE /v1/assets/{asset_id}/subtitles/{subtitle_id}/cc/)"
        from .files.api.assets import (
            delete_assets_by_asset_id_subtitles_by_subtitle_id_cc as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), asset_id=asset_id, subtitle_id=subtitle_id
        )

    def delete_asset_temporary_file_sets_by_file_set(
        self, asset_id: str, file_set_id: str, *, delete_cloud_objects=UNSET
    ):
        "Delete temporary file set with files (DELETE /v1/assets/{asset_id}/temporary_file_sets/{file_set_id}/)"
        from .files.api.assets import (
            delete_assets_by_asset_id_temporary_file_sets_by_file_set_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            file_set_id=file_set_id,
            delete_cloud_objects=delete_cloud_objects,
        )

    def delete_asset_versions_all_file_sets(
        self, asset_id: str, *, per_page=UNSET, last_id=UNSET
    ):
        "Delete asset's file sets (DELETE /v1/assets/{asset_id}/versions/all/file_sets/)"
        from .files.api.assets import (
            delete_assets_by_asset_id_versions_all_file_sets as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            per_page=per_page,
            last_id=last_id,
        )

    def delete_asset_versions_all_files(self, asset_id: str):
        "Delete asset's files entries by version (Not the actual file, use DELETE file_set for that) (DELETE /v1/assets/{asset_id}/versions/all/files/)"
        from .files.api.assets import (
            delete_assets_by_asset_id_versions_all_files as _endpoint,
        )

        return _endpoint.sync_detailed(client=self._client("files"), asset_id=asset_id)

    def delete_asset_versions_all_formats(self, asset_id: str, *, immediately=UNSET):
        "Delete asset's formats all versions (DELETE /v1/assets/{asset_id}/versions/all/formats/)"
        from .files.api.assets import (
            delete_assets_by_asset_id_versions_all_formats as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), asset_id=asset_id, immediately=immediately
        )

    def delete_asset_versions_all_keyframes(self, asset_id: str):
        "Delete asset's keyframes all versions (DELETE /v1/assets/{asset_id}/versions/all/keyframes/)"
        from .files.api.assets import (
            delete_assets_by_asset_id_versions_all_keyframes as _endpoint,
        )

        return _endpoint.sync_detailed(client=self._client("files"), asset_id=asset_id)

    def delete_asset_versions_all_proxies(self, asset_id: str):
        "Delete asset's proxies all versions (DELETE /v1/assets/{asset_id}/versions/all/proxies/)"
        from .files.api.assets import (
            delete_assets_by_asset_id_versions_all_proxies as _endpoint,
        )

        return _endpoint.sync_detailed(client=self._client("files"), asset_id=asset_id)

    def delete_asset_versions_all_subtitles(self, asset_id: str):
        "Delete asset's subtitles all versions (DELETE /v1/assets/{asset_id}/versions/all/subtitles/)"
        from .files.api.assets import (
            delete_assets_by_asset_id_versions_all_subtitles as _endpoint,
        )

        return _endpoint.sync_detailed(client=self._client("files"), asset_id=asset_id)

    def delete_asset_version_file_sets(
        self, asset_id: str, version_id: str, *, per_page=UNSET, last_id=UNSET
    ):
        "Delete asset's file sets by version (DELETE /v1/assets/{asset_id}/versions/{version_id}/file_sets/)"
        from .files.api.assets import (
            delete_assets_by_asset_id_versions_by_version_id_file_sets as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            version_id=version_id,
            per_page=per_page,
            last_id=last_id,
        )

    def delete_asset_version_files(self, asset_id: str, version_id: str):
        "Delete asset's files entries by version (Not the actual file, use DELETE file_set for that) (DELETE /v1/assets/{asset_id}/versions/{version_id}/files/)"
        from .files.api.assets import (
            delete_assets_by_asset_id_versions_by_version_id_files as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), asset_id=asset_id, version_id=version_id
        )

    def delete_asset_version_formats(
        self, asset_id: str, version_id: str, *, immediately=UNSET
    ):
        "Delete asset's formats by version (DELETE /v1/assets/{asset_id}/versions/{version_id}/formats/)"
        from .files.api.assets import (
            delete_assets_by_asset_id_versions_by_version_id_formats as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            version_id=version_id,
            immediately=immediately,
        )

    def delete_asset_version_keyframes(
        self, asset_id: str, version_id: str, *, keep_poster=UNSET
    ):
        "Delete asset's keyframes by version (DELETE /v1/assets/{asset_id}/versions/{version_id}/keyframes/)"
        from .files.api.assets import (
            delete_assets_by_asset_id_versions_by_version_id_keyframes as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            version_id=version_id,
            keep_poster=keep_poster,
        )

    def delete_asset_version_proxies(self, asset_id: str, version_id: str):
        "Delete asset's proxies by version (DELETE /v1/assets/{asset_id}/versions/{version_id}/proxies/)"
        from .files.api.assets import (
            delete_assets_by_asset_id_versions_by_version_id_proxies as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), asset_id=asset_id, version_id=version_id
        )

    def delete_asset_version_subtitles(self, asset_id: str, version_id: str):
        "Delete asset's subtitles by version (DELETE /v1/assets/{asset_id}/versions/{version_id}/subtitles/)"
        from .files.api.assets import (
            delete_assets_by_asset_id_versions_by_version_id_subtitles as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), asset_id=asset_id, version_id=version_id
        )

    def delete_collection_keyframe(
        self, collection_id: str, keyframe_id: str, *, regenerate_keyframes=UNSET
    ):
        "Delete collection's keyframe (DELETE /v1/collections/{collection_id}/keyframes/{keyframe_id}/)"
        from .files.api.collections import (
            delete_collections_by_collection_id_keyframes_by_keyframe_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            collection_id=collection_id,
            keyframe_id=keyframe_id,
            regenerate_keyframes=regenerate_keyframes,
        )

    def delete_delete_queue_file_sets(self, *, body):
        "Restore file sets from delete queue (DELETE /v1/delete_queue/file_sets/)"
        from .files.api.delete_queue import delete_delete_queue_file_sets as _endpoint

        return _endpoint.sync_detailed(client=self._client("files"), body=body)

    def delete_delete_queue_formats(self, *, body):
        "Restore formats from delete queue (DELETE /v1/delete_queue/formats/)"
        from .files.api.delete_queue import delete_delete_queue_formats as _endpoint

        return _endpoint.sync_detailed(client=self._client("files"), body=body)

    def delete_export_location(self, export_location_id: str):
        "Delete a particular export_location by id (DELETE /v1/export_locations/{export_location_id}/)"
        from .files.api.export_locations import (
            delete_export_locations_by_export_location_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), export_location_id=export_location_id
        )

    def delete_file_set_transfers_from_by_storage(
        self, file_set_id: str, storage_id: str, *, failed=UNSET
    ):
        "Delete file set transfer after handling it (DELETE /v1/file_sets/{file_set_id}/transfers_from/{storage_id}/)"
        from .files.api.file_sets import (
            delete_file_sets_by_file_set_id_transfers_from_by_storage_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            file_set_id=file_set_id,
            storage_id=storage_id,
            failed=failed,
        )

    def delete_file_set_transfers_to_by_storage(
        self, file_set_id: str, storage_id: str, *, failed=UNSET
    ):
        "Delete file set transfer after handling it (DELETE /v1/file_sets/{file_set_id}/transfers_to/{storage_id}/)"
        from .files.api.file_sets import (
            delete_file_sets_by_file_set_id_transfers_to_by_storage_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            file_set_id=file_set_id,
            storage_id=storage_id,
            failed=failed,
        )

    def delete_file_deletions_from_by_storage(self, file_id: str, storage_id: str):
        "Delete file deletion job after handling it (DELETE /v1/files/{file_id}/deletions_from/{storage_id}/)"
        from .files.api.files import (
            delete_files_by_file_id_deletions_from_by_storage_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), file_id=file_id, storage_id=storage_id
        )

    def delete_files_missing_storage(self, storage_id: str, *, remove_assets=UNSET):
        "Delete all missing files from storage (DELETE /v1/files/missing/storages/{storage_id}/)"
        from .files.api.files import (
            delete_files_missing_storages_by_storage_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            storage_id=storage_id,
            remove_assets=remove_assets,
        )

    def delete_playlist_keyframe(
        self, playlist_id: str, keyframe_id: str, *, regenerate_keyframes=UNSET
    ):
        "Delete playlist's keyframe (DELETE /v1/playlists/{playlist_id}/keyframes/{keyframe_id}/)"
        from .files.api.playlists import (
            delete_playlists_by_playlist_id_keyframes_by_keyframe_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            playlist_id=playlist_id,
            keyframe_id=keyframe_id,
            regenerate_keyframes=regenerate_keyframes,
        )

    def delete_storage_gateway_clusters_by_cluster(self, cluster_id: str):
        "Delete a storage gateway cluster (DELETE /v1/storage_gateway_clusters/{cluster_id}/)"
        from .files.api.storage_gateway_clusters import (
            delete_storage_gateway_clusters_by_cluster_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), cluster_id=cluster_id
        )

    def delete_storage_gateway(self, storage_gateway_id: str):
        "Delete a storage gateway (DELETE /v1/storage_gateways/{storage_gateway_id}/)"
        from .files.api.storage_gateways import (
            delete_storage_gateways_by_storage_gateway_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), storage_gateway_id=storage_gateway_id
        )

    def delete_storage(self, storage_id: str):
        "Delete a particular storage by id (DELETE /v1/storages/{storage_id}/)"
        from .files.api.storages import delete_storages_by_storage_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("files"), storage_id=storage_id
        )

    def delete_storage_auto_scan(self, storage_id: str):
        "Disable cloud storage auto scan (DELETE /v1/storages/{storage_id}/auto_scan/)"
        from .files.api.storages import (
            delete_storages_by_storage_id_auto_scan as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), storage_id=storage_id
        )

    def delete_storage_object_files(self, storage_id: str, object_type: str, *, body):
        "Delete files from a particular storage from multiple objects (DELETE /v1/storages/{storage_id}/{object_type}/files/)"
        from .files.api.storages import (
            delete_storages_by_storage_id_by_object_type_files as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            storage_id=storage_id,
            object_type=object_type,
            body=body,
        )

    def delete_storage_default(self, storage_id: str):
        "Removes the default flag on a storage (DELETE /v1/storages/{storage_id}/default/)"
        from .files.api.storages import (
            delete_storages_by_storage_id_default as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), storage_id=storage_id
        )

    def delete_storage_deletion(self, storage_id: str, deletion_id: str):
        "Delete file deletion job after handling it (DELETE /v1/storages/{storage_id}/deletions/{deletion_id}/)"
        from .files.api.storages import (
            delete_storages_by_storage_id_deletions_by_deletion_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), storage_id=storage_id, deletion_id=deletion_id
        )

    def delete_storage_files(
        self,
        storage_id: str,
        *,
        path=UNSET,
        path_separator=UNSET,
        directory_path=UNSET,
        checksum=UNSET,
        id=UNSET,
        name=UNSET,
        type_=UNSET,
        status=UNSET,
        date_created=UNSET,
        date_modified=UNSET,
    ):
        "DELETE files (with copies in different storages) from a storage folder, or a storage (DELETE /v1/storages/{storage_id}/files/)"
        from .files.api.storages import delete_storages_by_storage_id_files as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("files"),
            storage_id=storage_id,
            path=path,
            path_separator=path_separator,
            directory_path=directory_path,
            checksum=checksum,
            id=id,
            name=name,
            type_=type_,
            status=status,
            date_created=date_created,
            date_modified=date_modified,
        )

    def delete_storage_gateway_event(self, storage_id: str, event_id: str):
        "Delete storage gateway event (DELETE /v1/storages/{storage_id}/gateway/events/{event_id}/)"
        from .files.api.storages import (
            delete_storages_by_storage_id_gateway_events_by_event_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), storage_id=storage_id, event_id=event_id
        )

    def delete_storage_transcoder(self, storage_id: str, transcoder_id: str):
        "Delete a transcoder from storage (DELETE /v1/storages/{storage_id}/transcoders/{transcoder_id}/)"
        from .files.api.storages import (
            delete_storages_by_storage_id_transcoders_by_transcoder_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            storage_id=storage_id,
            transcoder_id=transcoder_id,
        )

    def delete_storage_transfers_from_by_transfer(
        self, storage_id: str, transfer_id: str, *, failed=UNSET, completed=UNSET
    ):
        "Delete file set transfer after handling it (DELETE /v1/storages/{storage_id}/transfers_from/{transfer_id}/)"
        from .files.api.storages import (
            delete_storages_by_storage_id_transfers_from_by_transfer_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            storage_id=storage_id,
            transfer_id=transfer_id,
            failed=failed,
            completed=completed,
        )

    def delete_storage_transfers_to_by_transfer(
        self, storage_id: str, transfer_id: str, *, failed=UNSET, completed=UNSET
    ):
        "Delete file set transfer after handling it (DELETE /v1/storages/{storage_id}/transfers_to/{transfer_id}/)"
        from .files.api.storages import (
            delete_storages_by_storage_id_transfers_to_by_transfer_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            storage_id=storage_id,
            transfer_id=transfer_id,
            failed=failed,
            completed=completed,
        )

    def delete_transcoder(self, transcoder_id: str):
        "Delete a particular transcoder by id (DELETE /v1/transcoders/{transcoder_id}/)"
        from .files.api.transcoders import (
            delete_transcoders_by_transcoder_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), transcoder_id=transcoder_id
        )

    def get_analysis_profiles(self, *, per_page=UNSET, last_id=UNSET):
        "Get analysis profiles (GET /v1/analysis/profiles/)"
        from .files.api.analysis import get_analysis_profiles as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("files"), per_page=per_page, last_id=last_id
        )

    def get_analysis_profiles_default_by_media_type(self, media_type: str):
        "Get a default analysis profile (GET /v1/analysis/profiles/{media_type}/default/)"
        from .files.api.analysis import (
            get_analysis_profiles_by_media_type_default as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), media_type=media_type
        )

    def get_analysis_profile(self, profile_id: str):
        "Get an analysis profile (GET /v1/analysis/profiles/{profile_id}/)"
        from .files.api.analysis import get_analysis_profiles_by_profile_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("files"), profile_id=profile_id
        )

    def get_analysis_service_accounts(self, *, per_page=UNSET, last_id=UNSET):
        "Get analysis service accounts (GET /v1/analysis/service_accounts/)"
        from .files.api.analysis import get_analysis_service_accounts as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("files"), per_page=per_page, last_id=last_id
        )

    def get_analysis_service_accounts_by_analysis_service_account(
        self, analysis_service_account_id: str
    ):
        "Get an analysis service account (GET /v1/analysis/service_accounts/{analysis_service_account_id}/)"
        from .files.api.analysis import (
            get_analysis_service_accounts_by_analysis_service_account_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            analysis_service_account_id=analysis_service_account_id,
        )

    def get_analysis_settings_transcription_default(self):
        "Get default analysis settings for transcription (GET /v1/analysis/settings/transcription/default/)"
        from .files.api.analysis import (
            get_analysis_settings_transcription_default as _endpoint,
        )

        return _endpoint.sync_detailed(client=self._client("files"))

    def get_asset_file_sets(
        self, asset_id: str, *, per_page=UNSET, last_id=UNSET, file_count=UNSET
    ):
        "Get all asset's file sets (GET /v1/assets/{asset_id}/file_sets/)"
        from .files.api.assets import get_assets_by_asset_id_file_sets as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            per_page=per_page,
            last_id=last_id,
            file_count=file_count,
        )

    def get_asset_file_set(self, asset_id: str, file_set_id: str):
        "Get asset's file set (GET /v1/assets/{asset_id}/file_sets/{file_set_id}/)"
        from .files.api.assets import (
            get_assets_by_asset_id_file_sets_by_file_set_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), asset_id=asset_id, file_set_id=file_set_id
        )

    def get_asset_file_set_files(
        self,
        asset_id: str,
        file_set_id: str,
        *,
        per_page=UNSET,
        last_id=UNSET,
        generate_signed_url=UNSET,
        file_count=UNSET,
    ):
        "Get files from a file set (GET /v1/assets/{asset_id}/file_sets/{file_set_id}/files/)"
        from .files.api.assets import (
            get_assets_by_asset_id_file_sets_by_file_set_id_files as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            file_set_id=file_set_id,
            per_page=per_page,
            last_id=last_id,
            generate_signed_url=generate_signed_url,
            file_count=file_count,
        )

    def get_asset_files(
        self,
        asset_id: str,
        *,
        per_page=UNSET,
        generate_signed_url=UNSET,
        content_disposition=UNSET,
        last_id=UNSET,
    ):
        "Get all asset's files (GET /v1/assets/{asset_id}/files/)"
        from .files.api.assets import get_assets_by_asset_id_files as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            per_page=per_page,
            generate_signed_url=generate_signed_url,
            content_disposition=content_disposition,
            last_id=last_id,
        )

    def get_asset_file(
        self,
        asset_id: str,
        file_id: str,
        *,
        generate_signed_post_url=UNSET,
        content_disposition=UNSET,
        content_type=UNSET,
        bypass_url_cache=UNSET,
    ):
        "Get asset's file (GET /v1/assets/{asset_id}/files/{file_id}/)"
        from .files.api.assets import (
            get_assets_by_asset_id_files_by_file_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            file_id=file_id,
            generate_signed_post_url=generate_signed_post_url,
            content_disposition=content_disposition,
            content_type=content_type,
            bypass_url_cache=bypass_url_cache,
        )

    def get_asset_file_download_url(self, asset_id: str, file_id: str):
        "Get asset's file download URL (GET /v1/assets/{asset_id}/files/{file_id}/download_url/)"
        from .files.api.assets import (
            get_assets_by_asset_id_files_by_file_id_download_url as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), asset_id=asset_id, file_id=file_id
        )

    def get_asset_file_isg_handler_url(self, asset_id: str, file_id: str):
        "Get asset's file handler URL for ISG (GET /v1/assets/{asset_id}/files/{file_id}/isg_handler_url/)"
        from .files.api.assets import (
            get_assets_by_asset_id_files_by_file_id_isg_handler_url as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), asset_id=asset_id, file_id=file_id
        )

    def get_asset_file_multipart_url(
        self,
        asset_id: str,
        file_id: str,
        *,
        upload_id,
        type_=UNSET,
        max_part_number=UNSET,
        temporary=UNSET,
    ):
        "Get presigned urls for multipart upload (S3). (GET /v1/assets/{asset_id}/files/{file_id}/multipart_url/)"
        from .files.api.assets import (
            get_assets_by_asset_id_files_by_file_id_multipart_url as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            file_id=file_id,
            upload_id=upload_id,
            type_=type_,
            max_part_number=max_part_number,
            temporary=temporary,
        )

    def get_asset_file_multipart_url_part(
        self,
        asset_id: str,
        file_id: str,
        *,
        upload_id=UNSET,
        parts_num,
        per_page=UNSET,
        page=UNSET,
        temporary=UNSET,
    ):
        "Get presigned urls for multipart part upload (S3 & GCS). (GET /v1/assets/{asset_id}/files/{file_id}/multipart_url/part/)"
        from .files.api.assets import (
            get_assets_by_asset_id_files_by_file_id_multipart_url_part as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            file_id=file_id,
            upload_id=upload_id,
            parts_num=parts_num,
            per_page=per_page,
            page=page,
            temporary=temporary,
        )

    def get_asset_formats(
        self,
        asset_id: str,
        *,
        per_page=UNSET,
        last_id=UNSET,
        include_all_versions=UNSET,
    ):
        "Get all asset's formats (GET /v1/assets/{asset_id}/formats/)"
        from .files.api.assets import get_assets_by_asset_id_formats as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            per_page=per_page,
            last_id=last_id,
            include_all_versions=include_all_versions,
        )

    def get_asset_format(self, asset_id: str, format_id: str):
        "Get asset's format (GET /v1/assets/{asset_id}/formats/{format_id}/)"
        from .files.api.assets import (
            get_assets_by_asset_id_formats_by_format_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), asset_id=asset_id, format_id=format_id
        )

    def get_asset_format_components(self, asset_id: str, format_id: str):
        "Get all components for a format in an asset (GET /v1/assets/{asset_id}/formats/{format_id}/components/)"
        from .files.api.assets import (
            get_assets_by_asset_id_formats_by_format_id_components as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), asset_id=asset_id, format_id=format_id
        )

    def get_asset_format_component(
        self, asset_id: str, format_id: str, component_id: str
    ):
        "Get a component for a format in an asset (GET /v1/assets/{asset_id}/formats/{format_id}/components/{component_id}/)"
        from .files.api.assets import (
            get_assets_by_asset_id_formats_by_format_id_components_by_component_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            format_id=format_id,
            component_id=component_id,
        )

    def get_asset_format_file_sets(
        self, asset_id: str, format_id: str, *, per_page=UNSET, last_id=UNSET
    ):
        "Get all asset's file sets in a specific format (GET /v1/assets/{asset_id}/formats/{format_id}/file_sets/)"
        from .files.api.assets import (
            get_assets_by_asset_id_formats_by_format_id_file_sets as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            format_id=format_id,
            per_page=per_page,
            last_id=last_id,
        )

    def get_asset_format_file_sets_sources(self, asset_id: str, format_id: str):
        "Get all file sets with matching format and storage method (GET /v1/assets/{asset_id}/formats/{format_id}/file_sets/sources/)"
        from .files.api.assets import (
            get_assets_by_asset_id_formats_by_format_id_file_sets_sources as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), asset_id=asset_id, format_id=format_id
        )

    def get_asset_format_file_sets_sources_by_storage_method(
        self, asset_id: str, format_id: str, storage_method: str
    ):
        "Get all file sets with matching format and storage method (GET /v1/assets/{asset_id}/formats/{format_id}/file_sets/sources/{storage_method}/)"
        from .files.api.assets import (
            get_assets_by_asset_id_formats_by_format_id_file_sets_sources_by_storage_method as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            format_id=format_id,
            storage_method=storage_method,
        )

    def get_asset_format_storage_file_sets(
        self,
        asset_id: str,
        format_id: str,
        storage_id: str,
        *,
        per_page=UNSET,
        last_id=UNSET,
    ):
        "Get all asset's file sets in a specific format on a specific storage (GET /v1/assets/{asset_id}/formats/{format_id}/storages/{storage_id}/file_sets/)"
        from .files.api.assets import (
            get_assets_by_asset_id_formats_by_format_id_storages_by_storage_id_file_sets as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            format_id=format_id,
            storage_id=storage_id,
            per_page=per_page,
            last_id=last_id,
        )

    def get_asset_keyframes(
        self,
        asset_id: str,
        *,
        per_page=UNSET,
        generate_signed_url=UNSET,
        content_disposition=UNSET,
        last_id=UNSET,
        include_all_versions=UNSET,
    ):
        "Get all asset's keyframes (GET /v1/assets/{asset_id}/keyframes/)"
        from .files.api.assets import get_assets_by_asset_id_keyframes as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            per_page=per_page,
            generate_signed_url=generate_signed_url,
            content_disposition=content_disposition,
            last_id=last_id,
            include_all_versions=include_all_versions,
        )

    def get_asset_keyframe(
        self,
        asset_id: str,
        keyframe_id: str,
        *,
        content_disposition=UNSET,
        content_type=UNSET,
    ):
        "Get asset's proxy (GET /v1/assets/{asset_id}/keyframes/{keyframe_id}/)"
        from .files.api.assets import (
            get_assets_by_asset_id_keyframes_by_keyframe_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            keyframe_id=keyframe_id,
            content_disposition=content_disposition,
            content_type=content_type,
        )

    def get_asset_proxies(
        self,
        asset_id: str,
        *,
        per_page=UNSET,
        generate_signed_url=UNSET,
        content_disposition=UNSET,
        last_id=UNSET,
        bypass_url_cache=UNSET,
        include_all_versions=UNSET,
    ):
        "Get all asset's proxies (GET /v1/assets/{asset_id}/proxies/)"
        from .files.api.assets import get_assets_by_asset_id_proxies as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            per_page=per_page,
            generate_signed_url=generate_signed_url,
            content_disposition=content_disposition,
            last_id=last_id,
            bypass_url_cache=bypass_url_cache,
            include_all_versions=include_all_versions,
        )

    def get_asset_proxy(
        self,
        asset_id: str,
        proxy_id: str,
        *,
        content_disposition=UNSET,
        content_type=UNSET,
    ):
        "Get asset's proxy (GET /v1/assets/{asset_id}/proxies/{proxy_id}/)"
        from .files.api.assets import (
            get_assets_by_asset_id_proxies_by_proxy_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            proxy_id=proxy_id,
            content_disposition=content_disposition,
            content_type=content_type,
        )

    def get_asset_proxy_download_url(self, asset_id: str, proxy_id: str):
        "Get asset's proxy download url (GET /v1/assets/{asset_id}/proxies/{proxy_id}/download_url/)"
        from .files.api.assets import (
            get_assets_by_asset_id_proxies_by_proxy_id_download_url as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), asset_id=asset_id, proxy_id=proxy_id
        )

    def get_asset_proxy_multipart_url(
        self,
        asset_id: str,
        proxy_id: str,
        *,
        upload_id,
        type_=UNSET,
        max_part_number=UNSET,
    ):
        "Get presigned urls for S3 multipart upload. (GET /v1/assets/{asset_id}/proxies/{proxy_id}/multipart_url/)"
        from .files.api.assets import (
            get_assets_by_asset_id_proxies_by_proxy_id_multipart_url as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            proxy_id=proxy_id,
            upload_id=upload_id,
            type_=type_,
            max_part_number=max_part_number,
        )

    def get_asset_proxy_multipart_url_part(
        self,
        asset_id: str,
        proxy_id: str,
        *,
        upload_id=UNSET,
        parts_num,
        per_page=UNSET,
        page=UNSET,
    ):
        "Get presigned urls for S3 multipart part upload. (GET /v1/assets/{asset_id}/proxies/{proxy_id}/multipart_url/part/)"
        from .files.api.assets import (
            get_assets_by_asset_id_proxies_by_proxy_id_multipart_url_part as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            proxy_id=proxy_id,
            upload_id=upload_id,
            parts_num=parts_num,
            per_page=per_page,
            page=page,
        )

    def get_asset_subtitles(self, asset_id: str, *, per_page=UNSET, last_id=UNSET):
        "Get all asset's subtitles (GET /v1/assets/{asset_id}/subtitles/)"
        from .files.api.assets import get_assets_by_asset_id_subtitles as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            per_page=per_page,
            last_id=last_id,
        )

    def get_asset_subtitles_cc_by_language(self, asset_id: str, language: str):
        "Get asset's closed captions subtitle for a particular language (GET /v1/assets/{asset_id}/subtitles/{language}/cc/)"
        from .files.api.assets import (
            get_assets_by_asset_id_subtitles_by_language_cc as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), asset_id=asset_id, language=language
        )

    def get_asset_subtitles_cc_webvtt_by_language(self, asset_id: str, language: str):
        "Get asset's closed captions subtitle file for a particular language (GET /v1/assets/{asset_id}/subtitles/{language}/cc/webvtt/)"
        from .files.api.assets import (
            get_assets_by_asset_id_subtitles_by_language_cc_webvtt as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), asset_id=asset_id, language=language
        )

    def get_asset_subtitles_webvtt_by_language(self, asset_id: str, language: str):
        "Get asset's subtitle file for a particular language (GET /v1/assets/{asset_id}/subtitles/{language}/webvtt/)"
        from .files.api.assets import (
            get_assets_by_asset_id_subtitles_by_language_webvtt as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), asset_id=asset_id, language=language
        )

    def get_asset_subtitle(self, asset_id: str, subtitle_id: str):
        "Get asset's subtitle for a language (GET /v1/assets/{asset_id}/subtitles/{subtitle_id}/)"
        from .files.api.assets import (
            get_assets_by_asset_id_subtitles_by_subtitle_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), asset_id=asset_id, subtitle_id=subtitle_id
        )

    def get_asset_temporary_file_sets_files_by_file_set(
        self, asset_id: str, file_set_id: str, *, generate_signed_url=UNSET
    ):
        "Get files from a temporary file set (GET /v1/assets/{asset_id}/temporary_file_sets/{file_set_id}/files/)"
        from .files.api.assets import (
            get_assets_by_asset_id_temporary_file_sets_by_file_set_id_files as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            file_set_id=file_set_id,
            generate_signed_url=generate_signed_url,
        )

    def get_asset_version_file_sets(
        self,
        asset_id: str,
        version_id: str,
        *,
        per_page=UNSET,
        last_id=UNSET,
        file_count=UNSET,
    ):
        "Get all asset's file sets by version (GET /v1/assets/{asset_id}/versions/{version_id}/file_sets/)"
        from .files.api.assets import (
            get_assets_by_asset_id_versions_by_version_id_file_sets as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            version_id=version_id,
            per_page=per_page,
            last_id=last_id,
            file_count=file_count,
        )

    def get_asset_version_files(
        self,
        asset_id: str,
        version_id: str,
        *,
        per_page=UNSET,
        generate_signed_url=UNSET,
        content_disposition=UNSET,
        last_id=UNSET,
    ):
        "Get all asset's files by version (GET /v1/assets/{asset_id}/versions/{version_id}/files/)"
        from .files.api.assets import (
            get_assets_by_asset_id_versions_by_version_id_files as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            version_id=version_id,
            per_page=per_page,
            generate_signed_url=generate_signed_url,
            content_disposition=content_disposition,
            last_id=last_id,
        )

    def get_asset_version_formats(
        self, asset_id: str, version_id: str, *, per_page=UNSET, last_id=UNSET
    ):
        "Get all asset's formats by version (GET /v1/assets/{asset_id}/versions/{version_id}/formats/)"
        from .files.api.assets import (
            get_assets_by_asset_id_versions_by_version_id_formats as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            version_id=version_id,
            per_page=per_page,
            last_id=last_id,
        )

    def get_asset_version_keyframes(
        self,
        asset_id: str,
        version_id: str,
        *,
        per_page=UNSET,
        generate_signed_url=UNSET,
        content_disposition=UNSET,
        last_id=UNSET,
    ):
        "Get all asset's keyframes by version (GET /v1/assets/{asset_id}/versions/{version_id}/keyframes/)"
        from .files.api.assets import (
            get_assets_by_asset_id_versions_by_version_id_keyframes as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            version_id=version_id,
            per_page=per_page,
            generate_signed_url=generate_signed_url,
            content_disposition=content_disposition,
            last_id=last_id,
        )

    def get_asset_version_proxies(
        self,
        asset_id: str,
        version_id: str,
        *,
        per_page=UNSET,
        generate_signed_url=UNSET,
        content_disposition=UNSET,
        last_id=UNSET,
    ):
        "Get all asset's proxies by version (GET /v1/assets/{asset_id}/versions/{version_id}/proxies/)"
        from .files.api.assets import (
            get_assets_by_asset_id_versions_by_version_id_proxies as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            version_id=version_id,
            per_page=per_page,
            generate_signed_url=generate_signed_url,
            content_disposition=content_disposition,
            last_id=last_id,
        )

    def get_asset_version_proxy_by_manifest_type(
        self,
        asset_id: str,
        version_id: str,
        proxy_id: str,
        manifest_type: str,
        *,
        path=UNSET,
        relative=UNSET,
        presigned=UNSET,
        recreate=UNSET,
        drm=UNSET,
        watermark=UNSET,
    ):
        "Retrieve manifest/playlist for asset proxy (GET /v1/assets/{asset_id}/versions/{version_id}/proxies/{proxy_id}/{manifest_type}/)"
        from .files.api.assets import (
            get_assets_by_asset_id_versions_by_version_id_proxies_by_proxy_id_by_manifest_type as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            version_id=version_id,
            proxy_id=proxy_id,
            manifest_type=manifest_type,
            path=path,
            relative=relative,
            presigned=presigned,
            recreate=recreate,
            drm=drm,
            watermark=watermark,
        )

    def get_asset_version_subtitles(
        self, asset_id: str, version_id: str, *, per_page=UNSET, last_id=UNSET
    ):
        "Get all asset's subtitles by version (GET /v1/assets/{asset_id}/versions/{version_id}/subtitles/)"
        from .files.api.assets import (
            get_assets_by_asset_id_versions_by_version_id_subtitles as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            version_id=version_id,
            per_page=per_page,
            last_id=last_id,
        )

    def get_asset_version_subtitles_cc_webvtt_by_language(
        self, asset_id: str, version_id: str, language: str
    ):
        "Get asset's closed captions subtitle file for a particular language by version (GET /v1/assets/{asset_id}/versions/{version_id}/subtitles/{language}/cc/webvtt/)"
        from .files.api.assets import (
            get_assets_by_asset_id_versions_by_version_id_subtitles_by_language_cc_webvtt as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            version_id=version_id,
            language=language,
        )

    def get_asset_version_subtitles_webvtt_by_language(
        self, asset_id: str, version_id: str, language: str
    ):
        "Get asset's subtitle file for a particular language by version (GET /v1/assets/{asset_id}/versions/{version_id}/subtitles/{language}/webvtt/)"
        from .files.api.assets import (
            get_assets_by_asset_id_versions_by_version_id_subtitles_by_language_webvtt as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            version_id=version_id,
            language=language,
        )

    def get_asset_watermark_matches(
        self, asset_id: str, *, proxy_id=UNSET, version_id=UNSET
    ):
        "Get all ProxyContainerByUser records for an asset's proxies, (GET /v1/assets/{asset_id}/watermark-matches/)"
        from .files.api.assets import (
            get_assets_by_asset_id_watermark_matches as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            proxy_id=proxy_id,
            version_id=version_id,
        )

    def get_collection_keyframes(
        self,
        collection_id: str,
        *,
        per_page=UNSET,
        generate_signed_url=UNSET,
        last_id=UNSET,
    ):
        "Get all collection's keyframes (GET /v1/collections/{collection_id}/keyframes/)"
        from .files.api.collections import (
            get_collections_by_collection_id_keyframes as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            collection_id=collection_id,
            per_page=per_page,
            generate_signed_url=generate_signed_url,
            last_id=last_id,
        )

    def get_collection_keyframe(self, collection_id: str, keyframe_id: str):
        "Get collection's proxy (GET /v1/collections/{collection_id}/keyframes/{keyframe_id}/)"
        from .files.api.collections import (
            get_collections_by_collection_id_keyframes_by_keyframe_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            collection_id=collection_id,
            keyframe_id=keyframe_id,
        )

    def get_delete_queue_file_sets(
        self, *, per_page=UNSET, page=UNSET, sort=UNSET, query=UNSET, field_name=UNSET
    ):
        "Get deleted file sets (GET /v1/delete_queue/file_sets/)"
        from .files.api.delete_queue import get_delete_queue_file_sets as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("files"),
            per_page=per_page,
            page=page,
            sort=sort,
            query=query,
            field_name=field_name,
        )

    def get_delete_queue_formats(
        self, *, per_page=UNSET, page=UNSET, sort=UNSET, query=UNSET, field_name=UNSET
    ):
        "Get deleted formats (GET /v1/delete_queue/formats/)"
        from .files.api.delete_queue import get_delete_queue_formats as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("files"),
            per_page=per_page,
            page=page,
            sort=sort,
            query=query,
            field_name=field_name,
        )

    def get_export_locations(
        self, *, query=UNSET, ids=UNSET, per_page=UNSET, last_id=UNSET, sort=UNSET
    ):
        "Get all export_locations (GET /v1/export_locations/)"
        from .files.api.export_locations import get_export_locations as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("files"),
            query=query,
            ids=ids,
            per_page=per_page,
            last_id=last_id,
            sort=sort,
        )

    def get_export_location(self, export_location_id: str):
        "Returns a particular export_location by id (GET /v1/export_locations/{export_location_id}/)"
        from .files.api.export_locations import (
            get_export_locations_by_export_location_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), export_location_id=export_location_id
        )

    def get_file_set_files(self, file_set_id: str, *, generate_signed_url=UNSET):
        "Get files from a file set (GET /v1/file_sets/{file_set_id}/files/)"
        from .files.api.file_sets import get_file_sets_by_file_set_id_files as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("files"),
            file_set_id=file_set_id,
            generate_signed_url=generate_signed_url,
        )

    def get_files_checksum_by_checksum(
        self, checksum: str, *, per_page=UNSET, last_id=UNSET
    ):
        "Get files by checksum (GET /v1/files/checksum/{checksum}/)"
        from .files.api.files import get_files_checksum_by_checksum as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("files"),
            checksum=checksum,
            per_page=per_page,
            last_id=last_id,
        )

    def get_playlist_keyframes(
        self,
        playlist_id: str,
        *,
        per_page=UNSET,
        generate_signed_url=UNSET,
        last_id=UNSET,
    ):
        "Get all playlist's keyframes (GET /v1/playlists/{playlist_id}/keyframes/)"
        from .files.api.playlists import (
            get_playlists_by_playlist_id_keyframes as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            playlist_id=playlist_id,
            per_page=per_page,
            generate_signed_url=generate_signed_url,
            last_id=last_id,
        )

    def get_playlist_keyframe(self, playlist_id: str, keyframe_id: str):
        "Get playlist's keyframe (GET /v1/playlists/{playlist_id}/keyframes/{keyframe_id}/)"
        from .files.api.playlists import (
            get_playlists_by_playlist_id_keyframes_by_keyframe_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            playlist_id=playlist_id,
            keyframe_id=keyframe_id,
        )

    def get_shares_storage_files(self, storage_id: str, *, directory_path, name):
        "Check if a specific file is already on the storage for shares (GET /v1/shares/storages/{storage_id}/files/)"
        from .files.api.shares import (
            get_shares_storages_by_storage_id_files as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            storage_id=storage_id,
            directory_path=directory_path,
            name=name,
        )

    def get_storage_gateway_clusters(
        self,
        *,
        page=UNSET,
        per_page=UNSET,
        sort=UNSET,
        query=UNSET,
        view_nodes=UNSET,
        view_stats=UNSET,
    ):
        "Get all storage gateway clusters (GET /v1/storage_gateway_clusters/)"
        from .files.api.storage_gateway_clusters import (
            get_storage_gateway_clusters as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            page=page,
            per_page=per_page,
            sort=sort,
            query=query,
            view_nodes=view_nodes,
            view_stats=view_stats,
        )

    def get_storage_gateway_clusters_by_cluster(
        self, cluster_id: str, *, view_nodes=UNSET, view_stats=UNSET
    ):
        "Get a specific storage gateway cluster (GET /v1/storage_gateway_clusters/{cluster_id}/)"
        from .files.api.storage_gateway_clusters import (
            get_storage_gateway_clusters_by_cluster_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            cluster_id=cluster_id,
            view_nodes=view_nodes,
            view_stats=view_stats,
        )

    def get_storage_gateways(
        self, *, cluster_id=UNSET, page=UNSET, per_page=UNSET, query=UNSET, sort=UNSET
    ):
        "Get all storage gateways (GET /v1/storage_gateways/)"
        from .files.api.storage_gateways import get_storage_gateways as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("files"),
            cluster_id=cluster_id,
            page=page,
            per_page=per_page,
            query=query,
            sort=sort,
        )

    def get_storage_gateway(self, storage_gateway_id: str):
        "Get a specific storage gateway (GET /v1/storage_gateways/{storage_gateway_id}/)"
        from .files.api.storage_gateways import (
            get_storage_gateways_by_storage_gateway_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), storage_gateway_id=storage_gateway_id
        )

    def get_storage_gateway_telemetry(self, storage_gateway_id: str):
        "Get all telemetry for a specific storage gateway (GET /v1/storage_gateways/{storage_gateway_id}/telemetry/)"
        from .files.api.storage_gateways import (
            get_storage_gateways_by_storage_gateway_id_telemetry as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), storage_gateway_id=storage_gateway_id
        )

    def get_storage_gateways_telemetry(self, *, per_page=UNSET, last_id=UNSET):
        "Get all telemetry records with optional filtering (GET /v1/storage_gateways/telemetry/)"
        from .files.api.storage_gateways import (
            get_storage_gateways_telemetry as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), per_page=per_page, last_id=last_id
        )

    def get_storage_gateways_telemetry_by_worker(self, worker_id: str):
        "Get telemetry for a specific worker (GET /v1/storage_gateways/telemetry/{worker_id}/)"
        from .files.api.storage_gateways import (
            get_storage_gateways_telemetry_by_worker_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), worker_id=worker_id
        )

    def get_storages(
        self,
        *,
        page=UNSET,
        per_page=UNSET,
        sort=UNSET,
        id=UNSET,
        name=UNSET,
        method=UNSET,
        status=UNSET,
        purpose=UNSET,
        last_scanned=UNSET,
        scanner_status=UNSET,
        query=UNSET,
        ids=UNSET,
    ):
        "Get all storages (GET /v1/storages/)"
        from .files.api.storages import get_storages as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("files"),
            page=page,
            per_page=per_page,
            sort=sort,
            id=id,
            name=name,
            method=method,
            status=status,
            purpose=purpose,
            last_scanned=last_scanned,
            scanner_status=scanner_status,
            query=query,
            ids=ids,
        )

    def get_storages_default_by_purpose(self, purpose: str):
        "Get a purpose default storage (GET /v1/storages/{purpose}/default/)"
        from .files.api.storages import get_storages_by_purpose_default as _endpoint

        return _endpoint.sync_detailed(client=self._client("files"), purpose=purpose)

    def get_storage(self, storage_id: str):
        "Returns a particular storage by id (GET /v1/storages/{storage_id}/)"
        from .files.api.storages import get_storages_by_storage_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("files"), storage_id=storage_id
        )

    def get_storage_auto_scan(self, storage_id: str):
        "Get cloud storage auto scan settings (GET /v1/storages/{storage_id}/auto_scan/)"
        from .files.api.storages import (
            get_storages_by_storage_id_auto_scan as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), storage_id=storage_id
        )

    def get_storage_deletions(self, storage_id: str, *, per_page=UNSET, last_id=UNSET):
        "Get pending deletions of files from a local storage (GET /v1/storages/{storage_id}/deletions/)"
        from .files.api.storages import (
            get_storages_by_storage_id_deletions as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            storage_id=storage_id,
            per_page=per_page,
            last_id=last_id,
        )

    def get_storage_deletions_from(
        self, storage_id: str, *, per_page=UNSET, last_id=UNSET
    ):
        "Get pending deletions of files from a local storage (GET /v1/storages/{storage_id}/deletions_from/)"
        from .files.api.storages import (
            get_storages_by_storage_id_deletions_from as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            storage_id=storage_id,
            per_page=per_page,
            last_id=last_id,
        )

    def get_storage_files(
        self,
        storage_id: str,
        *,
        path=UNSET,
        path_separator=UNSET,
        directory_path=UNSET,
        checksum=UNSET,
        per_page=UNSET,
        page=UNSET,
        scroll=UNSET,
        scroll_id=UNSET,
        sort=UNSET,
        id=UNSET,
        name=UNSET,
        type_=UNSET,
        status=UNSET,
        date_created=UNSET,
        date_modified=UNSET,
    ):
        "Get files in a storage folder, or all files on a storage (GET /v1/storages/{storage_id}/files/)"
        from .files.api.storages import get_storages_by_storage_id_files as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("files"),
            storage_id=storage_id,
            path=path,
            path_separator=path_separator,
            directory_path=directory_path,
            checksum=checksum,
            per_page=per_page,
            page=page,
            scroll=scroll,
            scroll_id=scroll_id,
            sort=sort,
            id=id,
            name=name,
            type_=type_,
            status=status,
            date_created=date_created,
            date_modified=date_modified,
        )

    def get_storage_gateway_events(self, storage_id: str, *, last_id=UNSET):
        "Get pending storage gateway events (GET /v1/storages/{storage_id}/gateway/events/)"
        from .files.api.storages import (
            get_storages_by_storage_id_gateway_events as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), storage_id=storage_id, last_id=last_id
        )

    def get_storage_gateway_report(self, storage_id: str):
        "Get storage gateway report (GET /v1/storages/{storage_id}/gateway/report/)"
        from .files.api.storages import (
            get_storages_by_storage_id_gateway_report as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), storage_id=storage_id
        )

    def get_storage_temporary_files(
        self, storage_id: str, *, per_page=UNSET, last_id=UNSET
    ):
        "Get storage's exported files (GET /v1/storages/{storage_id}/temporary_files/)"
        from .files.api.storages import (
            get_storages_by_storage_id_temporary_files as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            storage_id=storage_id,
            per_page=per_page,
            last_id=last_id,
        )

    def get_storage_transcoders(
        self, storage_id: str, *, per_page=UNSET, last_id=UNSET
    ):
        "Get all transcoders for a particular storage (GET /v1/storages/{storage_id}/transcoders/)"
        from .files.api.storages import (
            get_storages_by_storage_id_transcoders as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            storage_id=storage_id,
            per_page=per_page,
            last_id=last_id,
        )

    def get_storage_transfers_from(
        self, storage_id: str, *, per_page=UNSET, last_id=UNSET
    ):
        "Get pending transfers of file sets from a local storage (GET /v1/storages/{storage_id}/transfers_from/)"
        from .files.api.storages import (
            get_storages_by_storage_id_transfers_from as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            storage_id=storage_id,
            per_page=per_page,
            last_id=last_id,
        )

    def get_storage_transfers_from_by_transfer(self, storage_id: str, transfer_id: str):
        "Get file set transfer record (GET /v1/storages/{storage_id}/transfers_from/{transfer_id}/)"
        from .files.api.storages import (
            get_storages_by_storage_id_transfers_from_by_transfer_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), storage_id=storage_id, transfer_id=transfer_id
        )

    def get_storage_transfers_to(
        self, storage_id: str, *, per_page=UNSET, last_id=UNSET
    ):
        "Get pending transfers of file sets to a local storage (GET /v1/storages/{storage_id}/transfers_to/)"
        from .files.api.storages import (
            get_storages_by_storage_id_transfers_to as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            storage_id=storage_id,
            per_page=per_page,
            last_id=last_id,
        )

    def get_storage_transfers_to_by_transfer(self, storage_id: str, transfer_id: str):
        "Get file set transfer record (GET /v1/storages/{storage_id}/transfers_to/{transfer_id}/)"
        from .files.api.storages import (
            get_storages_by_storage_id_transfers_to_by_transfer_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), storage_id=storage_id, transfer_id=transfer_id
        )

    def get_storage_verifications_access(self, storage_id: str):
        "Verify storage access (GET /v1/storages/{storage_id}/verifications/access/)"
        from .files.api.storages import (
            get_storages_by_storage_id_verifications_access as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), storage_id=storage_id
        )

    def get_storage_verifications_permissions(self, storage_id: str):
        "Verify storage permissions (GET /v1/storages/{storage_id}/verifications/permissions/)"
        from .files.api.storages import (
            get_storages_by_storage_id_verifications_permissions as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), storage_id=storage_id
        )

    def get_storages_isg_latest_version(self):
        "Get latest ISG version (GET /v1/storages/isg/latest_version/)"
        from .files.api.storages import get_storages_isg_latest_version as _endpoint

        return _endpoint.sync_detailed(client=self._client("files"))

    def get_storages_matching_by_purpose(self, purpose: str, *, storage_id=UNSET):
        "Returns a remote storage matching type (GET /v1/storages/matching/{purpose}/)"
        from .files.api.storages import get_storages_matching_by_purpose as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("files"), purpose=purpose, storage_id=storage_id
        )

    def get_storages_matching_method_by_purpose_by_method(
        self, purpose: str, method: str
    ):
        "Returns a remote storage matching type and method (GET /v1/storages/matching/{purpose}/method/{method}/)"
        from .files.api.storages import (
            get_storages_matching_by_purpose_method_by_method as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), purpose=purpose, method=method
        )

    def get_transcoders(
        self,
        *,
        per_page=UNSET,
        page=UNSET,
        query=UNSET,
        ids=UNSET,
        sort=UNSET,
        include_storages=UNSET,
    ):
        "Get all transcoders (GET /v1/transcoders/)"
        from .files.api.transcoders import get_transcoders as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("files"),
            per_page=per_page,
            page=page,
            query=query,
            ids=ids,
            sort=sort,
            include_storages=include_storages,
        )

    def get_transcoder(self, transcoder_id: str):
        "Returns a particular transcoder by id (GET /v1/transcoders/{transcoder_id}/)"
        from .files.api.transcoders import get_transcoders_by_transcoder_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("files"), transcoder_id=transcoder_id
        )

    def get_transcoder_options_by_option_name(
        self, transcoder_id: str, option_name: str
    ):
        "Get options for a transcoder configuration. (GET /v1/transcoders/{transcoder_id}/options/{option_name}/)"
        from .files.api.transcoders import (
            get_transcoders_by_transcoder_id_options_by_option_name as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            transcoder_id=transcoder_id,
            option_name=option_name,
        )

    def get_transcoder_storages(
        self, transcoder_id: str, *, per_page=UNSET, last_id=UNSET
    ):
        "Get storages linked to a transcoder (GET /v1/transcoders/{transcoder_id}/storages/)"
        from .files.api.transcoders import (
            get_transcoders_by_transcoder_id_storages as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            transcoder_id=transcoder_id,
            per_page=per_page,
            last_id=last_id,
        )

    def get_transfer_urls_verify(self, transfer_id: str, *, user_id, signature):
        "Verifies the signature of a url (GET /v1/transfers/{transfer_id}/urls/verify/)"
        from .files.api.transfers import (
            get_transfers_by_transfer_id_urls_verify as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            transfer_id=transfer_id,
            user_id=user_id,
            signature=signature,
        )

    def patch_analysis_profile(self, profile_id: str, *, body):
        "Update an analysis profile information (PATCH /v1/analysis/profiles/{profile_id}/)"
        from .files.api.analysis import (
            patch_analysis_profiles_by_profile_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), profile_id=profile_id, body=body
        )

    def patch_analysis_service_accounts_by_analysis_service_account(
        self, analysis_service_account_id: str, *, body
    ):
        "Update an analysis service account information (PATCH /v1/analysis/service_accounts/{analysis_service_account_id}/)"
        from .files.api.analysis import (
            patch_analysis_service_accounts_by_analysis_service_account_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            analysis_service_account_id=analysis_service_account_id,
            body=body,
        )

    def patch_asset_file_set(self, asset_id: str, file_set_id: str, *, body):
        "Update file set information (PATCH /v1/assets/{asset_id}/file_sets/{file_set_id}/)"
        from .files.api.assets import (
            patch_assets_by_asset_id_file_sets_by_file_set_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            file_set_id=file_set_id,
            body=body,
        )

    def patch_asset_file(self, asset_id: str, file_id: str, *, body):
        "Update file information (PATCH /v1/assets/{asset_id}/files/{file_id}/)"
        from .files.api.assets import (
            patch_assets_by_asset_id_files_by_file_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), asset_id=asset_id, file_id=file_id, body=body
        )

    def patch_asset_format(
        self, asset_id: str, format_id: str, *, body, sync_components=UNSET
    ):
        "Update format information (PATCH /v1/assets/{asset_id}/formats/{format_id}/)"
        from .files.api.assets import (
            patch_assets_by_asset_id_formats_by_format_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            format_id=format_id,
            body=body,
            sync_components=sync_components,
        )

    def patch_asset_keyframe(self, asset_id: str, keyframe_id: str, *, body):
        "Update keyframe information (PATCH /v1/assets/{asset_id}/keyframes/{keyframe_id}/)"
        from .files.api.assets import (
            patch_assets_by_asset_id_keyframes_by_keyframe_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            keyframe_id=keyframe_id,
            body=body,
        )

    def patch_asset_proxy(self, asset_id: str, proxy_id: str, *, body):
        "Update proxy information (PATCH /v1/assets/{asset_id}/proxies/{proxy_id}/)"
        from .files.api.assets import (
            patch_assets_by_asset_id_proxies_by_proxy_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            proxy_id=proxy_id,
            body=body,
        )

    def patch_asset_proxy_container_file(
        self, asset_id: str, proxy_id: str, container_id: str, file_id: str, *, body
    ):
        "Update proxy file status (PATCH /v1/assets/{asset_id}/proxies/{proxy_id}/containers/{container_id}/files/{file_id}/)"
        from .files.api.assets import (
            patch_assets_by_asset_id_proxies_by_proxy_id_containers_by_container_id_files_by_file_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            proxy_id=proxy_id,
            container_id=container_id,
            file_id=file_id,
            body=body,
        )

    def patch_asset_subtitle(self, asset_id: str, subtitle_id: str, *, body):
        "Update subtitle information (PATCH /v1/assets/{asset_id}/subtitles/{subtitle_id}/)"
        from .files.api.assets import (
            patch_assets_by_asset_id_subtitles_by_subtitle_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            subtitle_id=subtitle_id,
            body=body,
        )

    def patch_asset_temporary_files_by_file(self, asset_id: str, file_id: str, *, body):
        "Update temporary file's info (PATCH /v1/assets/{asset_id}/temporary_files/{file_id}/)"
        from .files.api.assets import (
            patch_assets_by_asset_id_temporary_files_by_file_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), asset_id=asset_id, file_id=file_id, body=body
        )

    def patch_collection_keyframe(self, collection_id: str, keyframe_id: str, *, body):
        "Update keyframe information (PATCH /v1/collections/{collection_id}/keyframes/{keyframe_id}/)"
        from .files.api.collections import (
            patch_collections_by_collection_id_keyframes_by_keyframe_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            collection_id=collection_id,
            keyframe_id=keyframe_id,
            body=body,
        )

    def patch_export_location(self, export_location_id: str, *, body):
        "Update export_location (PATCH /v1/export_locations/{export_location_id}/)"
        from .files.api.export_locations import (
            patch_export_locations_by_export_location_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            export_location_id=export_location_id,
            body=body,
        )

    def patch_playlist_keyframe(self, playlist_id: str, keyframe_id: str, *, body):
        "Update keyframe information (PATCH /v1/playlists/{playlist_id}/keyframes/{keyframe_id}/)"
        from .files.api.playlists import (
            patch_playlists_by_playlist_id_keyframes_by_keyframe_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            playlist_id=playlist_id,
            keyframe_id=keyframe_id,
            body=body,
        )

    def patch_storage_gateway_clusters_by_cluster(self, cluster_id: str, *, body):
        "Update a storage gateway cluster (PATCH /v1/storage_gateway_clusters/{cluster_id}/)"
        from .files.api.storage_gateway_clusters import (
            patch_storage_gateway_clusters_by_cluster_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), cluster_id=cluster_id, body=body
        )

    def patch_storage_gateway(self, storage_gateway_id: str, *, body):
        "Update a storage gateway (PATCH /v1/storage_gateways/{storage_gateway_id}/)"
        from .files.api.storage_gateways import (
            patch_storage_gateways_by_storage_gateway_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            storage_gateway_id=storage_gateway_id,
            body=body,
        )

    def patch_storage(self, storage_id: str, *, body):
        "Update storage (PATCH /v1/storages/{storage_id}/)"
        from .files.api.storages import patch_storages_by_storage_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("files"), storage_id=storage_id, body=body
        )

    def patch_storage_files(self, storage_id: str, *, body):
        "Update file by storage ID and path (PATCH /v1/storages/{storage_id}/files/)"
        from .files.api.storages import patch_storages_by_storage_id_files as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("files"), storage_id=storage_id, body=body
        )

    def patch_transcoder(self, transcoder_id: str, *, body):
        "Update transcoder (PATCH /v1/transcoders/{transcoder_id}/)"
        from .files.api.transcoders import (
            patch_transcoders_by_transcoder_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), transcoder_id=transcoder_id, body=body
        )

    def post_analysis_profiles(self, *, body):
        "Create a new analysis profile (POST /v1/analysis/profiles/)"
        from .files.api.analysis import post_analysis_profiles as _endpoint

        return _endpoint.sync_detailed(client=self._client("files"), body=body)

    def post_analysis_profile_default(self, profile_id: str):
        "Set an analysis profile to the default of its media type (POST /v1/analysis/profiles/{profile_id}/default/)"
        from .files.api.analysis import (
            post_analysis_profiles_by_profile_id_default as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), profile_id=profile_id
        )

    def post_analysis_service_accounts(self, *, body):
        "Create a new analysis service account (POST /v1/analysis/service_accounts/)"
        from .files.api.analysis import post_analysis_service_accounts as _endpoint

        return _endpoint.sync_detailed(client=self._client("files"), body=body)

    def post_assets_bulk_archive_v2(self, *, body, allow_host_transfer=UNSET):
        "Archive multiple assets to a storage. (POST /v2/assets/bulk/archive/)"
        from .files.api.assets import post_assets_bulk_archive as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("files"),
            body=body,
            allow_host_transfer=allow_host_transfer,
        )

    def post_assets_bulk_keyframes(self, *, body):
        "Create a transcode job for proxy and keyframes generation of multiple assets (POST /v1/assets/bulk/keyframes/)"
        from .files.api.assets import post_assets_bulk_keyframes as _endpoint

        return _endpoint.sync_detailed(client=self._client("files"), body=body)

    def post_assets_bulk_restore_v2(self, *, body, allow_host_transfer=UNSET):
        "Restore multiple objects. (POST /v2/assets/bulk/restore/)"
        from .files.api.assets import post_assets_bulk_restore as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("files"),
            body=body,
            allow_host_transfer=allow_host_transfer,
        )

    def post_asset_custom_keyframe(self, asset_id: str, *, content_type=UNSET):
        "Create keyframe of type poster for asset (POST /v1/assets/{asset_id}/custom_keyframe/)"
        from .files.api.assets import (
            post_assets_by_asset_id_custom_keyframe as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), asset_id=asset_id, content_type=content_type
        )

    def post_asset_custom_keyframe_by_poster(
        self, asset_id: str, poster_id: str, *, overwrite=UNSET
    ):
        "Set keyframe of type poster as asset keyframe (POST /v1/assets/{asset_id}/custom_keyframe/{poster_id}/)"
        from .files.api.assets import (
            post_assets_by_asset_id_custom_keyframe_by_poster_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            poster_id=poster_id,
            overwrite=overwrite,
        )

    def post_asset_export_location(
        self, asset_id: str, export_location_id: str, *, body, allow_host_transfer=UNSET
    ):
        "Export asset to export location (POST /v1/assets/{asset_id}/export_locations/{export_location_id}/)"
        from .files.api.assets import (
            post_assets_by_asset_id_export_locations_by_export_location_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            export_location_id=export_location_id,
            body=body,
            allow_host_transfer=allow_host_transfer,
        )

    def post_asset_file_sets(self, asset_id: str, *, body):
        "Create file set and associate to asset (POST /v1/assets/{asset_id}/file_sets/)"
        from .files.api.assets import post_assets_by_asset_id_file_sets as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("files"), asset_id=asset_id, body=body
        )

    def post_asset_file_sets_bulk(
        self,
        asset_id: str,
        *,
        body,
        keep_source=UNSET,
        immediately=UNSET,
        do_not_delete_last_copy=UNSET,
    ):
        "Delete asset's file set, file entries, and actual files in bulk (POST /v1/assets/{asset_id}/file_sets/bulk/)"
        from .files.api.assets import (
            post_assets_by_asset_id_file_sets_bulk as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            body=body,
            keep_source=keep_source,
            immediately=immediately,
            do_not_delete_last_copy=do_not_delete_last_copy,
        )

    def post_asset_files(self, asset_id: str, *, body):
        "Create file and associate to asset (POST /v1/assets/{asset_id}/files/)"
        from .files.api.assets import post_assets_by_asset_id_files as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("files"), asset_id=asset_id, body=body
        )

    def post_asset_file_capture_by_milliseconds(
        self, asset_id: str, file_id: str, milliseconds: int, *, body
    ):
        "Create a transcode job for creating still keyframe (POST /v1/assets/{asset_id}/files/{file_id}/capture/{milliseconds}/)"
        from .files.api.assets import (
            post_assets_by_asset_id_files_by_file_id_capture_by_milliseconds as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            file_id=file_id,
            milliseconds=milliseconds,
            body=body,
        )

    def post_asset_file_edit_proxies(self, asset_id: str, file_id: str, *, body):
        "Create format, file_set, and file for edit proxy if storage has edit proxy transcoder configured (POST /v1/assets/{asset_id}/files/{file_id}/edit_proxies/)"
        from .files.api.assets import (
            post_assets_by_asset_id_files_by_file_id_edit_proxies as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), asset_id=asset_id, file_id=file_id, body=body
        )

    def post_asset_file_keyframes(self, asset_id: str, file_id: str, *, body):
        "Create a transcode job for proxy and keyframes (POST /v1/assets/{asset_id}/files/{file_id}/keyframes/)"
        from .files.api.assets import (
            post_assets_by_asset_id_files_by_file_id_keyframes as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), asset_id=asset_id, file_id=file_id, body=body
        )

    def post_asset_file_mediainfo(self, asset_id: str, file_id: str, *, body):
        "Create a job for extracting mediainfo (POST /v1/assets/{asset_id}/files/{file_id}/mediainfo/)"
        from .files.api.assets import (
            post_assets_by_asset_id_files_by_file_id_mediainfo as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), asset_id=asset_id, file_id=file_id, body=body
        )

    def post_asset_file_multipart(
        self, asset_id: str, file_id: str, *, body, temporary=UNSET
    ):
        "Complete multipart upload (GCS). (POST /v1/assets/{asset_id}/files/{file_id}/multipart/)"
        from .files.api.assets import (
            post_assets_by_asset_id_files_by_file_id_multipart as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            file_id=file_id,
            body=body,
            temporary=temporary,
        )

    def post_asset_file_multipart_b2_cancel(
        self, asset_id: str, file_id: str, *, body, temporary=UNSET
    ):
        "Cancel Backblaze B2 multipart upload. (POST /v1/assets/{asset_id}/files/{file_id}/multipart/b2/cancel/)"
        from .files.api.assets import (
            post_assets_by_asset_id_files_by_file_id_multipart_b2_cancel as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            file_id=file_id,
            body=body,
            temporary=temporary,
        )

    def post_asset_file_multipart_b2_finish(
        self, asset_id: str, file_id: str, *, body, temporary=UNSET
    ):
        "Complete Backblaze B2 multipart upload. (POST /v1/assets/{asset_id}/files/{file_id}/multipart/b2/finish/)"
        from .files.api.assets import (
            post_assets_by_asset_id_files_by_file_id_multipart_b2_finish as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            file_id=file_id,
            body=body,
            temporary=temporary,
        )

    def post_asset_file_multipart_b2_start(
        self, asset_id: str, file_id: str, *, body=UNSET, temporary=UNSET
    ):
        "Start Backblaze B2 multipart upload. (POST /v1/assets/{asset_id}/files/{file_id}/multipart/b2/start/)"
        from .files.api.assets import (
            post_assets_by_asset_id_files_by_file_id_multipart_b2_start as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            file_id=file_id,
            body=body,
            temporary=temporary,
        )

    def post_asset_file_multipart_cleanup(self, asset_id: str, file_id: str, *, body):
        "Cleanup multipart upload (GCS, S3). (POST /v1/assets/{asset_id}/files/{file_id}/multipart/cleanup/)"
        from .files.api.assets import (
            post_assets_by_asset_id_files_by_file_id_multipart_cleanup as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), asset_id=asset_id, file_id=file_id, body=body
        )

    def post_asset_file_multipart_gcs_compose_url(
        self, asset_id: str, file_id: str, *, body, temporary=UNSET
    ):
        "Get object compose url for GCS parallel upload. (POST /v1/assets/{asset_id}/files/{file_id}/multipart/gcs/compose_url/)"
        from .files.api.assets import (
            post_assets_by_asset_id_files_by_file_id_multipart_gcs_compose_url as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            file_id=file_id,
            body=body,
            temporary=temporary,
        )

    def post_asset_file_multipart_url_s3_part(
        self, asset_id: str, file_id: str, *, body, temporary=UNSET
    ):
        "Create presigned urls for multipart part S3 upload. (POST /v1/assets/{asset_id}/files/{file_id}/multipart_url/s3/part/)"
        from .files.api.assets import (
            post_assets_by_asset_id_files_by_file_id_multipart_url_s3_part as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            file_id=file_id,
            body=body,
            temporary=temporary,
        )

    def post_asset_file_reindex(self, asset_id: str, file_id: str, *, body):
        "Trigger reindexing of a file (POST /v1/assets/{asset_id}/files/{file_id}/reindex/)"
        from .files.api.assets import (
            post_assets_by_asset_id_files_by_file_id_reindex as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), asset_id=asset_id, file_id=file_id, body=body
        )

    def post_asset_file_subtitles(self, asset_id: str, file_id: str, *, body=UNSET):
        "Create a transcode job for subtitle files (POST /v1/assets/{asset_id}/files/{file_id}/subtitles/)"
        from .files.api.assets import (
            post_assets_by_asset_id_files_by_file_id_subtitles as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), asset_id=asset_id, file_id=file_id, body=body
        )

    def post_asset_formats(self, asset_id: str, *, body):
        "Create format and associate to asset (POST /v1/assets/{asset_id}/formats/)"
        from .files.api.assets import post_assets_by_asset_id_formats as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("files"), asset_id=asset_id, body=body
        )

    def post_asset_format_archive(
        self, asset_id: str, format_id: str, *, body, allow_host_transfer=UNSET
    ):
        "Archive format (POST /v1/assets/{asset_id}/formats/{format_id}/archive/)"
        from .files.api.assets import (
            post_assets_by_asset_id_formats_by_format_id_archive as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            format_id=format_id,
            body=body,
            allow_host_transfer=allow_host_transfer,
        )

    def post_asset_format_archive_v2(
        self, asset_id: str, format_id: str, *, body, allow_host_transfer=UNSET
    ):
        "Archive format (POST /v2/assets/{asset_id}/formats/{format_id}/archive/)"
        from .files.api.assets import (
            post_assets_by_asset_id_formats_by_format_id_archive_1 as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            format_id=format_id,
            body=body,
            allow_host_transfer=allow_host_transfer,
        )

    def post_asset_format_components(self, asset_id: str, format_id: str, *, body):
        "Add a new format component (POST /v1/assets/{asset_id}/formats/{format_id}/components/)"
        from .files.api.assets import (
            post_assets_by_asset_id_formats_by_format_id_components as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            format_id=format_id,
            body=body,
        )

    def post_asset_format_restore(
        self, asset_id: str, format_id: str, *, body, allow_host_transfer=UNSET
    ):
        "Restore archived format (POST /v1/assets/{asset_id}/formats/{format_id}/restore/)"
        from .files.api.assets import (
            post_assets_by_asset_id_formats_by_format_id_restore as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            format_id=format_id,
            body=body,
            allow_host_transfer=allow_host_transfer,
        )

    def post_asset_format_storage_v2(
        self,
        asset_id: str,
        format_id: str,
        storage_id: str,
        *,
        body,
        allow_host_transfer=UNSET,
    ):
        "Transfer formats file sets to another storage. (POST /v2/assets/{asset_id}/formats/{format_id}/storages/{storage_id}/)"
        from .files.api.assets import (
            post_assets_by_asset_id_formats_by_format_id_storages_by_storage_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            format_id=format_id,
            storage_id=storage_id,
            body=body,
            allow_host_transfer=allow_host_transfer,
        )

    def post_asset_keyframes(
        self, asset_id: str, *, body, use_google_resumable_upload=UNSET
    ):
        "Create keyframe and associate to asset (POST /v1/assets/{asset_id}/keyframes/)"
        from .files.api.assets import post_assets_by_asset_id_keyframes as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            body=body,
            use_google_resumable_upload=use_google_resumable_upload,
        )

    def post_asset_keyframe_public(self, asset_id: str, keyframe_id: str):
        "Make the keyframe link public (POST /v1/assets/{asset_id}/keyframes/{keyframe_id}/public/)"
        from .files.api.assets import (
            post_assets_by_asset_id_keyframes_by_keyframe_id_public as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), asset_id=asset_id, keyframe_id=keyframe_id
        )

    def post_asset_method_keyframes_by_storage_method(
        self,
        asset_id: str,
        storage_method: str,
        *,
        body,
        use_google_resumable_upload=UNSET,
    ):
        "Create keyframe and associate to asset (POST /v1/assets/{asset_id}/method/{storage_method}/keyframes/)"
        from .files.api.assets import (
            post_assets_by_asset_id_method_by_storage_method_keyframes as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            storage_method=storage_method,
            body=body,
            use_google_resumable_upload=use_google_resumable_upload,
        )

    def post_asset_method_proxies_by_storage_method(
        self, asset_id: str, storage_method: str, *, body
    ):
        "Create proxy and associate to asset (POST /v1/assets/{asset_id}/method/{storage_method}/proxies/)"
        from .files.api.assets import (
            post_assets_by_asset_id_method_by_storage_method_proxies as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            storage_method=storage_method,
            body=body,
        )

    def post_asset_proxies(self, asset_id: str, *, body):
        "Create proxy and associate to asset (POST /v1/assets/{asset_id}/proxies/)"
        from .files.api.assets import post_assets_by_asset_id_proxies as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("files"), asset_id=asset_id, body=body
        )

    def post_asset_proxy_container_files(
        self,
        asset_id: str,
        proxy_id: str,
        container_id: str,
        *,
        body,
        drm=UNSET,
        watermark=UNSET,
    ):
        "Create Proxy file (POST /v1/assets/{asset_id}/proxies/{proxy_id}/containers/{container_id}/files/)"
        from .files.api.assets import (
            post_assets_by_asset_id_proxies_by_proxy_id_containers_by_container_id_files as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            proxy_id=proxy_id,
            container_id=container_id,
            body=body,
            drm=drm,
            watermark=watermark,
        )

    def post_asset_proxy_keyframes(self, asset_id: str, proxy_id: str, *, body):
        "Create a transcode job for keyframes from a proxy (POST /v1/assets/{asset_id}/proxies/{proxy_id}/keyframes/)"
        from .files.api.assets import (
            post_assets_by_asset_id_proxies_by_proxy_id_keyframes as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            proxy_id=proxy_id,
            body=body,
        )

    def post_asset_proxy_multipart_cleanup(self, asset_id: str, proxy_id: str, *, body):
        "Cleanup S3 multipart upload (POST /v1/assets/{asset_id}/proxies/{proxy_id}/multipart/cleanup/)"
        from .files.api.assets import (
            post_assets_by_asset_id_proxies_by_proxy_id_multipart_cleanup as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            proxy_id=proxy_id,
            body=body,
        )

    def post_asset_proxy_public(self, asset_id: str, proxy_id: str):
        "Make the proxy link public (POST /v1/assets/{asset_id}/proxies/{proxy_id}/public/)"
        from .files.api.assets import (
            post_assets_by_asset_id_proxies_by_proxy_id_public as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), asset_id=asset_id, proxy_id=proxy_id
        )

    def post_asset_subtitles(self, asset_id: str, *, body):
        "Create subtitle proxy and associate to asset (POST /v1/assets/{asset_id}/subtitles/)"
        from .files.api.assets import post_assets_by_asset_id_subtitles as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("files"), asset_id=asset_id, body=body
        )

    def post_asset_temporary_file_sets(self, asset_id: str, *, body):
        "Create temporary file set and associate to asset (POST /v1/assets/{asset_id}/temporary_file_sets/)"
        from .files.api.assets import (
            post_assets_by_asset_id_temporary_file_sets as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), asset_id=asset_id, body=body
        )

    def post_asset_temporary_files(self, asset_id: str, *, body, store=UNSET):
        "Create temporary transfer file for FILE storage transfers (POST /v1/assets/{asset_id}/temporary_files/)"
        from .files.api.assets import (
            post_assets_by_asset_id_temporary_files as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), asset_id=asset_id, body=body, store=store
        )

    def post_asset_version_transcode(self, asset_id: str, version_id: str, *, body):
        "Create a transcode job for a specific asset version (POST /v1/assets/{asset_id}/versions/{version_id}/transcode/)"
        from .files.api.assets import (
            post_assets_by_asset_id_versions_by_version_id_transcode as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            version_id=version_id,
            body=body,
        )

    def post_assets_export_location(
        self, export_location_id: str, *, body, allow_host_transfer=UNSET
    ):
        "Export multiple assets to export location (POST /v1/assets/export_locations/{export_location_id}/)"
        from .files.api.assets import (
            post_assets_export_locations_by_export_location_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            export_location_id=export_location_id,
            body=body,
            allow_host_transfer=allow_host_transfer,
        )

    def post_assets_export_location_bulk_export_v2(
        self, export_location_id: str, *, body, allow_host_transfer=UNSET
    ):
        "Export multiple assets. (POST /v2/assets/export_locations/{export_location_id}/bulk/export/)"
        from .files.api.assets import (
            post_assets_export_locations_by_export_location_id_bulk_export as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            export_location_id=export_location_id,
            body=body,
            allow_host_transfer=allow_host_transfer,
        )

    def post_assets_storage_bulk_transfer_v2(
        self, storage_id: str, *, body, allow_host_transfer=UNSET
    ):
        "Transfer multiple objects. (POST /v2/assets/storages/{storage_id}/bulk/transfer/)"
        from .files.api.assets import (
            post_assets_storages_by_storage_id_bulk_transfer as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            storage_id=storage_id,
            body=body,
            allow_host_transfer=allow_host_transfer,
        )

    def post_collections_bulk_archive_v2(self, *, body, allow_host_transfer=UNSET):
        "Archive multiple assets to a storage. (POST /v2/collections/bulk/archive/)"
        from .files.api.collections import post_collections_bulk_archive as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("files"),
            body=body,
            allow_host_transfer=allow_host_transfer,
        )

    def post_collections_bulk_restore_v2(self, *, body, allow_host_transfer=UNSET):
        "Restore multiple collections to a storage. (POST /v2/collections/bulk/restore/)"
        from .files.api.collections import post_collections_bulk_restore as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("files"),
            body=body,
            allow_host_transfer=allow_host_transfer,
        )

    def post_collection_custom_keyframe_by_poster(
        self, collection_id: str, poster_id: str, *, overwrite=UNSET
    ):
        "Set keyframe of type poster as collection keyframe (POST /v1/collections/{collection_id}/custom_keyframe/{poster_id}/)"
        from .files.api.collections import (
            post_collections_by_collection_id_custom_keyframe_by_poster_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            collection_id=collection_id,
            poster_id=poster_id,
            overwrite=overwrite,
        )

    def post_collection_export_location(
        self,
        collection_id: str,
        export_location_id: str,
        *,
        body,
        allow_host_transfer=UNSET,
    ):
        "Export collection assets to export location (POST /v1/collections/{collection_id}/export_locations/{export_location_id}/)"
        from .files.api.collections import (
            post_collections_by_collection_id_export_locations_by_export_location_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            collection_id=collection_id,
            export_location_id=export_location_id,
            body=body,
            allow_host_transfer=allow_host_transfer,
        )

    def post_collection_keyframes_files(self, collection_id: str, *, body):
        "Create keyframe and associate to collection (POST /v1/collections/{collection_id}/keyframes/)"
        from .files.api.collections import (
            post_collections_by_collection_id_keyframes as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), collection_id=collection_id, body=body
        )

    def post_collection_keyframes_copy(self, collection_id: str, *, body):
        "Copy collection keyframe to another collection (POST /v1/collections/{collection_id}/keyframes/copy/)"
        from .files.api.collections import (
            post_collections_by_collection_id_keyframes_copy as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), collection_id=collection_id, body=body
        )

    def post_collections_export_location_bulk_export_v2(
        self, export_location_id: str, *, body, allow_host_transfer=UNSET
    ):
        "Export multiple collections. (POST /v2/collections/export_locations/{export_location_id}/bulk/export/)"
        from .files.api.collections import (
            post_collections_export_locations_by_export_location_id_bulk_export as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            export_location_id=export_location_id,
            body=body,
            allow_host_transfer=allow_host_transfer,
        )

    def post_collections_storage_bulk_transfer_v2(
        self, storage_id: str, *, body, allow_host_transfer=UNSET
    ):
        "Transfer multiple objects. (POST /v2/collections/storages/{storage_id}/bulk/transfer/)"
        from .files.api.collections import (
            post_collections_storages_by_storage_id_bulk_transfer as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            storage_id=storage_id,
            body=body,
            allow_host_transfer=allow_host_transfer,
        )

    def post_delete_queue_file_sets_purge(self, *, body):
        "Purge file sets from delete queue (Permanently delete) (POST /v1/delete_queue/file_sets/purge/)"
        from .files.api.delete_queue import (
            post_delete_queue_file_sets_purge as _endpoint,
        )

        return _endpoint.sync_detailed(client=self._client("files"), body=body)

    def post_delete_queue_file_sets_purge_all(self):
        "Purge all file sets from delete queue (Permanently delete) (POST /v1/delete_queue/file_sets/purge/all/)"
        from .files.api.delete_queue import (
            post_delete_queue_file_sets_purge_all as _endpoint,
        )

        return _endpoint.sync_detailed(client=self._client("files"))

    def post_delete_queue_formats_purge(self, *, body):
        "Purge formats from delete queue (Permanently delete) (POST /v1/delete_queue/formats/purge/)"
        from .files.api.delete_queue import post_delete_queue_formats_purge as _endpoint

        return _endpoint.sync_detailed(client=self._client("files"), body=body)

    def post_delete_queue_formats_purge_all(self):
        "Purge all formats from delete queue (Permanently delete) (POST /v1/delete_queue/formats/purge/all/)"
        from .files.api.delete_queue import (
            post_delete_queue_formats_purge_all as _endpoint,
        )

        return _endpoint.sync_detailed(client=self._client("files"))

    def post_drm_asset_version_proxy_auth(
        self,
        asset_id: str,
        version_id: str,
        proxy_id: str,
        *,
        drm=UNSET,
        watermark=UNSET,
    ):
        "Get authentication token for a given asset proxy. (POST /v1/drm/assets/{asset_id}/versions/{version_id}/proxies/{proxy_id}/auth/)"
        from .files.api.drm import (
            post_drm_assets_by_asset_id_versions_by_version_id_proxies_by_proxy_id_auth as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            version_id=version_id,
            proxy_id=proxy_id,
            drm=drm,
            watermark=watermark,
        )

    def post_export_locations(self, *, body):
        "Create a new export_location (POST /v1/export_locations/)"
        from .files.api.export_locations import post_export_locations as _endpoint

        return _endpoint.sync_detailed(client=self._client("files"), body=body)

    def post_export_location_bulk_export(
        self, export_location_id: str, *, body, allow_host_transfer=UNSET
    ):
        "Export multiple objects to export location (POST /v1/export_locations/{export_location_id}/bulk_export/)"
        from .files.api.export_locations import (
            post_export_locations_by_export_location_id_bulk_export as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            export_location_id=export_location_id,
            body=body,
            allow_host_transfer=allow_host_transfer,
        )

    def post_export_location_reindex(self, export_location_id: str, *, body):
        "Trigger reindexing of a export location (POST /v1/export_locations/{export_location_id}/reindex/)"
        from .files.api.export_locations import (
            post_export_locations_by_export_location_id_reindex as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            export_location_id=export_location_id,
            body=body,
        )

    def post_exports_temporary_file_sets_storage_by_file_set(
        self, file_set_id: str, storage_id: str, *, body
    ):
        "Queue export job completion between local storages (POST /v1/exports/temporary_file_sets/{file_set_id}/storages/{storage_id}/)"
        from .files.api.exports import (
            post_exports_temporary_file_sets_by_file_set_id_storages_by_storage_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            file_set_id=file_set_id,
            storage_id=storage_id,
            body=body,
        )

    def post_file_set_storage(
        self, file_set_id: str, storage_id: str, *, body, allow_host_transfer=UNSET
    ):
        "Queue copying of a file set with files from one storage to another (POST /v1/file_sets/{file_set_id}/storages/{storage_id}/)"
        from .files.api.file_sets import (
            post_file_sets_by_file_set_id_storages_by_storage_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            file_set_id=file_set_id,
            storage_id=storage_id,
            body=body,
            allow_host_transfer=allow_host_transfer,
        )

    def post_files_storage(self, storage_id: str, *, body, get_file_size=UNSET):
        "Check file is on storage (POST /v1/files/storages/{storage_id}/)"
        from .files.api.files import post_files_storages_by_storage_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("files"),
            storage_id=storage_id,
            body=body,
            get_file_size=get_file_size,
        )

    def post_files_upload(self, *, body):
        "Upload small files (POST /v1/files/upload/)"
        from .files.api.files import post_files_upload as _endpoint

        return _endpoint.sync_detailed(client=self._client("files"), body=body)

    def post_format_storage(self, format_id: str, storage_id: str, *, body):
        "Queue copying of a formats file sets with files from one storage to another (POST /v1/formats/{format_id}/storages/{storage_id}/)"
        from .files.api.formats import (
            post_formats_by_format_id_storages_by_storage_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            format_id=format_id,
            storage_id=storage_id,
            body=body,
        )

    def post_formats_archive_bulk_by_format_name(
        self, format_name: str, *, body, allow_host_transfer=UNSET
    ):
        "Queue bulk archiving of assets, collections and saved_searches (POST /v1/formats/{format_name}/archive/bulk/)"
        from .files.api.formats import (
            post_formats_by_format_name_archive_bulk as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            format_name=format_name,
            body=body,
            allow_host_transfer=allow_host_transfer,
        )

    def post_formats_restore_bulk_by_format_name(
        self, format_name: str, *, body, allow_host_transfer=UNSET
    ):
        "Queue bulk restore of previously archived assets, collections or saved_searches (POST /v1/formats/{format_name}/restore/bulk/)"
        from .files.api.formats import (
            post_formats_by_format_name_restore_bulk as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            format_name=format_name,
            body=body,
            allow_host_transfer=allow_host_transfer,
        )

    def post_playlist_keyframes_files(self, playlist_id: str, *, body):
        "Create keyframe and associate to playlist (POST /v1/playlists/{playlist_id}/keyframes/)"
        from .files.api.playlists import (
            post_playlists_by_playlist_id_keyframes as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), playlist_id=playlist_id, body=body
        )

    def post_saved_searches_bulk_archive_v2(self, *, body, allow_host_transfer=UNSET):
        "Transfer multiple objects. (POST /v2/saved_searches/bulk/archive/)"
        from .files.api.saved_searches import (
            post_saved_searches_bulk_archive as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            body=body,
            allow_host_transfer=allow_host_transfer,
        )

    def post_saved_searches_bulk_restore_v2(self, *, body, allow_host_transfer=UNSET):
        "Restore multiple saved searches. (POST /v2/saved_searches/bulk/restore/)"
        from .files.api.saved_searches import (
            post_saved_searches_bulk_restore as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            body=body,
            allow_host_transfer=allow_host_transfer,
        )

    def post_saved_searches_export_location_bulk_export_v2(
        self, export_location_id: str, *, body, allow_host_transfer=UNSET
    ):
        "Export multiple saved searches. (POST /v2/saved_searches/export_locations/{export_location_id}/bulk/export/)"
        from .files.api.saved_searches import (
            post_saved_searches_export_locations_by_export_location_id_bulk_export as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            export_location_id=export_location_id,
            body=body,
            allow_host_transfer=allow_host_transfer,
        )

    def post_saved_searches_storage_bulk_transfer_v2(
        self, storage_id: str, *, body, allow_host_transfer=UNSET
    ):
        "Transfer multiple objects. (POST /v2/saved_searches/storages/{storage_id}/bulk/transfer/)"
        from .files.api.saved_searches import (
            post_saved_searches_storages_by_storage_id_bulk_transfer as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            storage_id=storage_id,
            body=body,
            allow_host_transfer=allow_host_transfer,
        )

    def post_storage_gateway_clusters(self, *, body):
        "Create a new storage gateway cluster (POST /v1/storage_gateway_clusters/)"
        from .files.api.storage_gateway_clusters import (
            post_storage_gateway_clusters as _endpoint,
        )

        return _endpoint.sync_detailed(client=self._client("files"), body=body)

    def post_storage_gateways(self, *, body):
        "Create a new storage gateway (POST /v1/storage_gateways/)"
        from .files.api.storage_gateways import post_storage_gateways as _endpoint

        return _endpoint.sync_detailed(client=self._client("files"), body=body)

    def post_storage_gateway_logs(self, storage_gateway_id: str, *, body):
        "Upload storage logs (POST /v1/storage_gateways/{storage_gateway_id}/logs/)"
        from .files.api.storage_gateways import (
            post_storage_gateways_by_storage_gateway_id_logs as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            storage_gateway_id=storage_gateway_id,
            body=body,
        )

    def post_storage_gateway_telemetry(self, storage_gateway_id: str, *, body):
        "Create telemetry (POST /v1/storage_gateways/{storage_gateway_id}/telemetry/)"
        from .files.api.storage_gateways import (
            post_storage_gateways_by_storage_gateway_id_telemetry as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            storage_gateway_id=storage_gateway_id,
            body=body,
        )

    def post_storages(self, *, body):
        "Create a new storage (POST /v1/storages/)"
        from .files.api.storages import post_storages as _endpoint

        return _endpoint.sync_detailed(client=self._client("files"), body=body)

    def post_storage_auto_scan(self, storage_id: str, *, body):
        "Enable cloud storage auto scan (POST /v1/storages/{storage_id}/auto_scan/)"
        from .files.api.storages import (
            post_storages_by_storage_id_auto_scan as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), storage_id=storage_id, body=body
        )

    def post_storage_bulk(self, storage_id: str, *, body, allow_host_transfer=UNSET):
        "Queue copying of files from current storage to specified one (POST /v1/storages/{storage_id}/bulk/)"
        from .files.api.storages import post_storages_by_storage_id_bulk as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("files"),
            storage_id=storage_id,
            body=body,
            allow_host_transfer=allow_host_transfer,
        )

    def post_storage_default(self, storage_id: str):
        "Set a storage to the default of its purpose (POST /v1/storages/{storage_id}/default/)"
        from .files.api.storages import post_storages_by_storage_id_default as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("files"), storage_id=storage_id
        )

    def post_storage_files(self, storage_id: str, *, body):
        "Create file without associating it to an asset (POST /v1/storages/{storage_id}/files/)"
        from .files.api.storages import post_storages_by_storage_id_files as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("files"), storage_id=storage_id, body=body
        )

    def post_storage_file_reindex(self, storage_id: str, file_id: str, *, body):
        "Trigger reindexing for a file on a storage (POST /v1/storages/{storage_id}/files/{file_id}/reindex/)"
        from .files.api.storages import (
            post_storages_by_storage_id_files_by_file_id_reindex as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            storage_id=storage_id,
            file_id=file_id,
            body=body,
        )

    def post_storage_files_reindex(self, storage_id: str, *, body):
        "Trigger reindexing of all files (POST /v1/storages/{storage_id}/files/reindex/)"
        from .files.api.storages import (
            post_storages_by_storage_id_files_reindex as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), storage_id=storage_id, body=body
        )

    def post_storage_gateway_events(self, storage_id: str, *, body):
        "Create new storage gateway event (POST /v1/storages/{storage_id}/gateway/events/)"
        from .files.api.storages import (
            post_storages_by_storage_id_gateway_events as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), storage_id=storage_id, body=body
        )

    def post_storage_gateway_events_purge(self, storage_id: str, *, body):
        "Delete storage gateway events in bulk (POST /v1/storages/{storage_id}/gateway/events/purge/)"
        from .files.api.storages import (
            post_storages_by_storage_id_gateway_events_purge as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), storage_id=storage_id, body=body
        )

    def post_storage_logs(self, storage_id: str, *, body):
        "Upload storage logs (POST /v1/storages/{storage_id}/logs/)"
        from .files.api.storages import post_storages_by_storage_id_logs as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("files"), storage_id=storage_id, body=body
        )

    def post_storage_reindex(self, storage_id: str, *, body):
        "Trigger reindexing of a storage (POST /v1/storages/{storage_id}/reindex/)"
        from .files.api.storages import post_storages_by_storage_id_reindex as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("files"), storage_id=storage_id, body=body
        )

    def post_storage_scan(self, storage_id: str, *, body):
        "Requests to scan a storage (POST /v1/storages/{storage_id}/scan/)"
        from .files.api.storages import post_storages_by_storage_id_scan as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("files"), storage_id=storage_id, body=body
        )

    def post_storages_files_reindex(self, *, body):
        "Trigger reindexing of all files (POST /v1/storages/files/reindex/)"
        from .files.api.storages import post_storages_files_reindex as _endpoint

        return _endpoint.sync_detailed(client=self._client("files"), body=body)

    def post_storages_reindex(self, *, body):
        "Trigger reindexing of all storages (POST /v1/storages/reindex/)"
        from .files.api.storages import post_storages_reindex as _endpoint

        return _endpoint.sync_detailed(client=self._client("files"), body=body)

    def post_storages_swap(self, *, body):
        "Requires SuperAdmin access (POST /v1/storages/swap/)"
        from .files.api.storages import post_storages_swap as _endpoint

        return _endpoint.sync_detailed(client=self._client("files"), body=body)

    def post_storages_verifications_access(self, *, body):
        "Verify access prior to creating a storage (POST /v1/storages/verifications/access/)"
        from .files.api.storages import post_storages_verifications_access as _endpoint

        return _endpoint.sync_detailed(client=self._client("files"), body=body)

    def post_storages_verifications_permissions(self, *, body):
        "Verify permissions prior to creating a storage (POST /v1/storages/verifications/permissions/)"
        from .files.api.storages import (
            post_storages_verifications_permissions as _endpoint,
        )

        return _endpoint.sync_detailed(client=self._client("files"), body=body)

    def post_transcoders(self, *, body):
        "Create a new transcoder (POST /v1/transcoders/)"
        from .files.api.transcoders import post_transcoders as _endpoint

        return _endpoint.sync_detailed(client=self._client("files"), body=body)

    def post_transcoder_logs(self, transcoder_id: str, *, filename):
        "Upload transcoder logs (POST /v1/transcoders/{transcoder_id}/logs/)"
        from .files.api.transcoders import (
            post_transcoders_by_transcoder_id_logs as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), transcoder_id=transcoder_id, filename=filename
        )

    def post_transcoder_reindex(self, transcoder_id: str, *, body):
        "Trigger reindexing of a transcoder (POST /v1/transcoders/{transcoder_id}/reindex/)"
        from .files.api.transcoders import (
            post_transcoders_by_transcoder_id_reindex as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), transcoder_id=transcoder_id, body=body
        )

    def post_transfer_urls(self, transfer_id: str):
        "Generates a url for direct file downloads (for IGSs) (POST /v1/transfers/{transfer_id}/urls/)"
        from .files.api.transfers import post_transfers_by_transfer_id_urls as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("files"), transfer_id=transfer_id
        )

    def put_analysis_profile(self, profile_id: str, *, body):
        "Update an analysis profile information (PUT /v1/analysis/profiles/{profile_id}/)"
        from .files.api.analysis import put_analysis_profiles_by_profile_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("files"), profile_id=profile_id, body=body
        )

    def put_analysis_service_accounts_by_analysis_service_account(
        self, analysis_service_account_id: str, *, body
    ):
        "Update an analysis service account information (PUT /v1/analysis/service_accounts/{analysis_service_account_id}/)"
        from .files.api.analysis import (
            put_analysis_service_accounts_by_analysis_service_account_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            analysis_service_account_id=analysis_service_account_id,
            body=body,
        )

    def put_asset_file_set(self, asset_id: str, file_set_id: str, *, body):
        "Update file set information (PUT /v1/assets/{asset_id}/file_sets/{file_set_id}/)"
        from .files.api.assets import (
            put_assets_by_asset_id_file_sets_by_file_set_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            file_set_id=file_set_id,
            body=body,
        )

    def put_asset_file_set_restore(self, asset_id: str, file_set_id: str):
        "Restore delete asset's file set (PUT /v1/assets/{asset_id}/file_sets/{file_set_id}/restore/)"
        from .files.api.assets import (
            put_assets_by_asset_id_file_sets_by_file_set_id_restore as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), asset_id=asset_id, file_set_id=file_set_id
        )

    def put_asset_file(self, asset_id: str, file_id: str, *, body):
        "Update file information (PUT /v1/assets/{asset_id}/files/{file_id}/)"
        from .files.api.assets import (
            put_assets_by_asset_id_files_by_file_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), asset_id=asset_id, file_id=file_id, body=body
        )

    def put_asset_format(
        self, asset_id: str, format_id: str, *, body, sync_components=UNSET
    ):
        "Update format information (PUT /v1/assets/{asset_id}/formats/{format_id}/)"
        from .files.api.assets import (
            put_assets_by_asset_id_formats_by_format_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            format_id=format_id,
            body=body,
            sync_components=sync_components,
        )

    def put_asset_format_component(
        self, asset_id: str, format_id: str, component_id: str
    ):
        "Update a component in a format (PUT /v1/assets/{asset_id}/formats/{format_id}/components/{component_id}/)"
        from .files.api.assets import (
            put_assets_by_asset_id_formats_by_format_id_components_by_component_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            format_id=format_id,
            component_id=component_id,
        )

    def put_asset_format_restore(self, asset_id: str, format_id: str):
        "Restore deleted asset's format (PUT /v1/assets/{asset_id}/formats/{format_id}/restore/)"
        from .files.api.assets import (
            put_assets_by_asset_id_formats_by_format_id_restore as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), asset_id=asset_id, format_id=format_id
        )

    def put_asset_keyframe(self, asset_id: str, keyframe_id: str, *, body):
        "Update keyframe information (PUT /v1/assets/{asset_id}/keyframes/{keyframe_id}/)"
        from .files.api.assets import (
            put_assets_by_asset_id_keyframes_by_keyframe_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            keyframe_id=keyframe_id,
            body=body,
        )

    def put_asset_proxy(self, asset_id: str, proxy_id: str, *, body):
        "Update proxy information (PUT /v1/assets/{asset_id}/proxies/{proxy_id}/)"
        from .files.api.assets import (
            put_assets_by_asset_id_proxies_by_proxy_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            proxy_id=proxy_id,
            body=body,
        )

    def put_asset_proxy_containers(
        self, asset_id: str, proxy_id: str, *, body, drm=UNSET, watermark=UNSET
    ):
        "Create Proxy container. (PUT /v1/assets/{asset_id}/proxies/{proxy_id}/containers/)"
        from .files.api.assets import (
            put_assets_by_asset_id_proxies_by_proxy_id_containers as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            proxy_id=proxy_id,
            body=body,
            drm=drm,
            watermark=watermark,
        )

    def put_asset_proxy_container_file(
        self, asset_id: str, proxy_id: str, container_id: str, file_id: str, *, body
    ):
        "Update proxy file status (PUT /v1/assets/{asset_id}/proxies/{proxy_id}/containers/{container_id}/files/{file_id}/)"
        from .files.api.assets import (
            put_assets_by_asset_id_proxies_by_proxy_id_containers_by_container_id_files_by_file_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            proxy_id=proxy_id,
            container_id=container_id,
            file_id=file_id,
            body=body,
        )

    def put_asset_subtitle(self, asset_id: str, subtitle_id: str, *, body):
        "Update subtitle information (PUT /v1/assets/{asset_id}/subtitles/{subtitle_id}/)"
        from .files.api.assets import (
            put_assets_by_asset_id_subtitles_by_subtitle_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            asset_id=asset_id,
            subtitle_id=subtitle_id,
            body=body,
        )

    def put_asset_temporary_files_by_file(self, asset_id: str, file_id: str, *, body):
        "Update temporary file's info (PUT /v1/assets/{asset_id}/temporary_files/{file_id}/)"
        from .files.api.assets import (
            put_assets_by_asset_id_temporary_files_by_file_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), asset_id=asset_id, file_id=file_id, body=body
        )

    def put_collection_keyframe(self, collection_id: str, keyframe_id: str, *, body):
        "Update keyframe information (PUT /v1/collections/{collection_id}/keyframes/{keyframe_id}/)"
        from .files.api.collections import (
            put_collections_by_collection_id_keyframes_by_keyframe_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            collection_id=collection_id,
            keyframe_id=keyframe_id,
            body=body,
        )

    def put_export_location(self, export_location_id: str, *, body):
        "Update export_location (PUT /v1/export_locations/{export_location_id}/)"
        from .files.api.export_locations import (
            put_export_locations_by_export_location_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            export_location_id=export_location_id,
            body=body,
        )

    def put_playlist_keyframe(self, playlist_id: str, keyframe_id: str, *, body):
        "Update keyframe information (PUT /v1/playlists/{playlist_id}/keyframes/{keyframe_id}/)"
        from .files.api.playlists import (
            put_playlists_by_playlist_id_keyframes_by_keyframe_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            playlist_id=playlist_id,
            keyframe_id=keyframe_id,
            body=body,
        )

    def put_storage_gateway_clusters_by_cluster(self, cluster_id: str, *, body):
        "Update a storage gateway cluster (PUT /v1/storage_gateway_clusters/{cluster_id}/)"
        from .files.api.storage_gateway_clusters import (
            put_storage_gateway_clusters_by_cluster_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), cluster_id=cluster_id, body=body
        )

    def put_storage_gateway(self, storage_gateway_id: str, *, body):
        "Update a storage gateway (PUT /v1/storage_gateways/{storage_gateway_id}/)"
        from .files.api.storage_gateways import (
            put_storage_gateways_by_storage_gateway_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            storage_gateway_id=storage_gateway_id,
            body=body,
        )

    def put_storage(self, storage_id: str, *, body):
        "Update storage (PUT /v1/storages/{storage_id}/)"
        from .files.api.storages import put_storages_by_storage_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("files"), storage_id=storage_id, body=body
        )

    def put_storage_files(self, storage_id: str, *, body):
        "Update file by storage ID and path (PUT /v1/storages/{storage_id}/files/)"
        from .files.api.storages import put_storages_by_storage_id_files as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("files"), storage_id=storage_id, body=body
        )

    def put_storage_gateway_report(self, storage_id: str, *, body):
        "Create storage gateway report (PUT /v1/storages/{storage_id}/gateway/report/)"
        from .files.api.storages import (
            put_storages_by_storage_id_gateway_report as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), storage_id=storage_id, body=body
        )

    def put_storage_gateway_status(self, storage_id: str, *, body):
        "Update storage gateway status (PUT /v1/storages/{storage_id}/gateway/status/)"
        from .files.api.storages import (
            put_storages_by_storage_id_gateway_status as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), storage_id=storage_id, body=body
        )

    def put_storage_search_document(self, storage_id: str, *, body):
        "Update search document for storage (PUT /v1/storages/{storage_id}/search_document/)"
        from .files.api.storages import (
            put_storages_by_storage_id_search_document as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"), storage_id=storage_id, body=body
        )

    def put_storage_transcoder(self, storage_id: str, transcoder_id: str):
        "Create a new transcoder for storage (PUT /v1/storages/{storage_id}/transcoders/{transcoder_id}/)"
        from .files.api.storages import (
            put_storages_by_storage_id_transcoders_by_transcoder_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("files"),
            storage_id=storage_id,
            transcoder_id=transcoder_id,
        )

    def put_transcoder(self, transcoder_id: str, *, body):
        "Update transcoder (PUT /v1/transcoders/{transcoder_id}/)"
        from .files.api.transcoders import put_transcoders_by_transcoder_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("files"), transcoder_id=transcoder_id, body=body
        )

    def delete_jobs(
        self,
        *,
        body=UNSET,
        parent_id=UNSET,
        object_id=UNSET,
        created_by=UNSET,
        status=UNSET,
        type_=UNSET,
        date_created=UNSET,
        date_modified=UNSET,
        query=UNSET,
        ids=UNSET,
        metadata_automation_id=UNSET,
        field_missing=UNSET,
        field_exists=UNSET,
    ):
        "Delete multiple jobs (DELETE /v1/jobs/)"
        from .jobs.api.jobs import delete_jobs as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("jobs"),
            body=body,
            parent_id=parent_id,
            object_id=object_id,
            created_by=created_by,
            status=status,
            type_=type_,
            date_created=date_created,
            date_modified=date_modified,
            query=query,
            ids=ids,
            metadata_automation_id=metadata_automation_id,
            field_missing=field_missing,
            field_exists=field_exists,
        )

    def delete_job(self, job_id: str, *, recursive=UNSET):
        "Delete a particular job by id (DELETE /v1/jobs/{job_id}/)"
        from .jobs.api.jobs import delete_jobs_by_job_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("jobs"), job_id=job_id, recursive=recursive
        )

    def get_jobs(
        self,
        *,
        facets=UNSET,
        aggregations=UNSET,
        page=UNSET,
        per_page=UNSET,
        scroll=UNSET,
        scroll_id=UNSET,
        sort=UNSET,
        type_=UNSET,
        object_type=UNSET,
        parent_id=UNSET,
        object_id=UNSET,
        status=UNSET,
        created_by=UNSET,
        date_created=UNSET,
        date_modified=UNSET,
        query=UNSET,
        ids=UNSET,
        metadata_automation_id=UNSET,
        metadata_field=UNSET,
        field_missing=UNSET,
        field_exists=UNSET,
    ):
        "Get list of jobs (GET /v1/jobs/)"
        from .jobs.api.jobs import get_jobs as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("jobs"),
            facets=facets,
            aggregations=aggregations,
            page=page,
            per_page=per_page,
            scroll=scroll,
            scroll_id=scroll_id,
            sort=sort,
            type_=type_,
            object_type=object_type,
            parent_id=parent_id,
            object_id=object_id,
            status=status,
            created_by=created_by,
            date_created=date_created,
            date_modified=date_modified,
            query=query,
            ids=ids,
            metadata_automation_id=metadata_automation_id,
            metadata_field=metadata_field,
            field_missing=field_missing,
            field_exists=field_exists,
        )

    def get_job(self, job_id: str):
        "Returns a particular job by id (GET /v1/jobs/{job_id}/)"
        from .jobs.api.jobs import get_jobs_by_job_id as _endpoint

        return _endpoint.sync_detailed(client=self._client("jobs"), job_id=job_id)

    def patch_jobs(
        self,
        *,
        body,
        parent_id=UNSET,
        object_id=UNSET,
        created_by=UNSET,
        status=UNSET,
        type_=UNSET,
        date_created=UNSET,
        date_modified=UNSET,
        query=UNSET,
        ids=UNSET,
        merge_metadata=UNSET,
        metadata_automation_id=UNSET,
        field_missing=UNSET,
        field_exists=UNSET,
    ):
        "Edit jobs (PATCH /v1/jobs/)"
        from .jobs.api.jobs import patch_jobs as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("jobs"),
            body=body,
            parent_id=parent_id,
            object_id=object_id,
            created_by=created_by,
            status=status,
            type_=type_,
            date_created=date_created,
            date_modified=date_modified,
            query=query,
            ids=ids,
            merge_metadata=merge_metadata,
            metadata_automation_id=metadata_automation_id,
            field_missing=field_missing,
            field_exists=field_exists,
        )

    def patch_job(self, job_id: str, *, body, merge_metadata=UNSET):
        "Update job (PATCH /v1/jobs/{job_id}/)"
        from .jobs.api.jobs import patch_jobs_by_job_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("jobs"),
            job_id=job_id,
            body=body,
            merge_metadata=merge_metadata,
        )

    def patch_job_steps(self, job_id: str, *, body):
        "Update multiple job steps (PATCH /v1/jobs/{job_id}/steps/)"
        from .jobs.api.jobs import patch_jobs_by_job_id_steps as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("jobs"), job_id=job_id, body=body
        )

    def patch_job_steps_by_job_step(self, job_id: str, job_step_id: str, *, body):
        "Update job step (PATCH /v1/jobs/{job_id}/steps/{job_step_id}/)"
        from .jobs.api.jobs import (
            patch_jobs_by_job_id_steps_by_job_step_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("jobs"),
            job_id=job_id,
            job_step_id=job_step_id,
            body=body,
        )

    def post_jobs(self, *, body):
        "Create a new job (POST /v1/jobs/)"
        from .jobs.api.jobs import post_jobs as _endpoint

        return _endpoint.sync_detailed(client=self._client("jobs"), body=body)

    def post_job_reindex(self, job_id: str, *, body):
        "Reindex job (POST /v1/jobs/{job_id}/reindex/)"
        from .jobs.api.jobs import post_jobs_by_job_id_reindex as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("jobs"), job_id=job_id, body=body
        )

    def put_job(self, job_id: str, *, body, merge_metadata=UNSET):
        "Update job (PUT /v1/jobs/{job_id}/)"
        from .jobs.api.jobs import put_jobs_by_job_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("jobs"),
            job_id=job_id,
            body=body,
            merge_metadata=merge_metadata,
        )

    def put_job_steps(self, job_id: str, *, body):
        "Update multiple job steps (PUT /v1/jobs/{job_id}/steps/)"
        from .jobs.api.jobs import put_jobs_by_job_id_steps as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("jobs"), job_id=job_id, body=body
        )

    def put_job_steps_by_job_step(self, job_id: str, job_step_id: str, *, body):
        "Update job step (PUT /v1/jobs/{job_id}/steps/{job_step_id}/)"
        from .jobs.api.jobs import put_jobs_by_job_id_steps_by_job_step_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("jobs"),
            job_id=job_id,
            job_step_id=job_step_id,
            body=body,
        )

    def put_jobs_priority(self, *, body):
        "Change jobs priority (PUT /v1/jobs/priority/)"
        from .jobs.api.jobs import put_jobs_priority as _endpoint

        return _endpoint.sync_detailed(client=self._client("jobs"), body=body)

    def put_jobs_state(self, *, body):
        "Change jobs state (PUT /v1/jobs/state/)"
        from .jobs.api.jobs import put_jobs_state as _endpoint

        return _endpoint.sync_detailed(client=self._client("jobs"), body=body)

    def delete_object_categories_metadata_by_name(self, object_type: str, name: str):
        "Delete metadata category by object type and category name (DELETE /v1/{object_type}/categories/{name}/)"
        from .metadata.api.object_type import (
            delete_by_object_type_categories_by_name as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("metadata"), object_type=object_type, name=name
        )

    def delete_fields_metadata_by_field_name(self, field_name: str):
        "Delete a particular field by name (DELETE /v1/fields/{field_name}/)"
        from .metadata.api.fields import delete_fields_by_field_name as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("metadata"), field_name=field_name
        )

    def delete_view_metadata(self, view_id: str):
        "Delete a particular view by id (DELETE /v1/views/{view_id}/)"
        from .metadata.api.views import delete_views_by_view_id as _endpoint

        return _endpoint.sync_detailed(client=self._client("metadata"), view_id=view_id)

    def get_asset_object_version_view_metadata(
        self,
        asset_id: str,
        object_type: str,
        object_id: str,
        version_id: str,
        view_id: str,
    ):
        "Get asset metadata by object type, object ID, version ID and view ID (GET /v1/assets/{asset_id}/{object_type}/{object_id}/versions/{version_id}/views/{view_id}/)"
        from .metadata.api.assets import (
            get_assets_by_asset_id_by_object_type_by_object_id_versions_by_version_id_views_by_view_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("metadata"),
            asset_id=asset_id,
            object_type=object_type,
            object_id=object_id,
            version_id=version_id,
            view_id=view_id,
        )

    def get_asset_object_view_metadata(
        self,
        asset_id: str,
        object_type: str,
        object_id: str,
        view_id: str,
        *,
        reencode_values_to_string=UNSET,
    ):
        "Get asset metadata by object type, object ID and view ID (GET /v1/assets/{asset_id}/{object_type}/{object_id}/views/{view_id}/)"
        from .metadata.api.assets import (
            get_assets_by_asset_id_by_object_type_by_object_id_views_by_view_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("metadata"),
            asset_id=asset_id,
            object_type=object_type,
            object_id=object_id,
            view_id=view_id,
            reencode_values_to_string=reencode_values_to_string,
        )

    def get_asset_version_view_metadata(
        self,
        asset_id: str,
        version_id: str,
        view_id: str,
        *,
        reencode_values_to_string=UNSET,
    ):
        "Get object metadata by object type, object ID, version ID and view ID (GET /v1/assets/{asset_id}/versions/{version_id}/views/{view_id}/)"
        from .metadata.api.assets import (
            get_assets_by_asset_id_versions_by_version_id_views_by_view_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("metadata"),
            asset_id=asset_id,
            version_id=version_id,
            view_id=view_id,
            reencode_values_to_string=reencode_values_to_string,
        )

    def get_object_metadata_direct(
        self,
        object_type: str,
        object_id: str,
        *,
        check_if_subclip=UNSET,
        include_values_for_deleted_fields=UNSET,
    ):
        "Get object metadata by object type and object ID (GET /v1/{object_type}/{object_id}/)"
        from .metadata.api.object_type import (
            get_by_object_type_by_object_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("metadata"),
            object_type=object_type,
            object_id=object_id,
            check_if_subclip=check_if_subclip,
            include_values_for_deleted_fields=include_values_for_deleted_fields,
        )

    def get_object_metadata(
        self,
        object_type: str,
        object_id: str,
        view_id: str,
        *,
        check_if_subclip=UNSET,
        reencode_values_to_string=UNSET,
    ):
        "Get object metadata by object type, object ID and view ID (GET /v1/{object_type}/{object_id}/views/{view_id}/)"
        from .metadata.api.object_type import (
            get_by_object_type_by_object_id_views_by_view_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("metadata"),
            object_type=object_type,
            object_id=object_id,
            view_id=view_id,
            check_if_subclip=check_if_subclip,
            reencode_values_to_string=reencode_values_to_string,
        )

    def get_asset_metadata(
        self,
        asset_id: str,
        view_id: str,
        *,
        check_if_subclip=UNSET,
        reencode_values_to_string=UNSET,
    ):
        "Get object metadata by object type, object ID and view ID (GET /v1/assets/{object_id}/views/{view_id}/)"
        from .metadata.api.object_type import (
            get_by_object_type_by_object_id_views_by_view_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("metadata"),
            object_type="assets",
            object_id=asset_id,
            view_id=view_id,
            check_if_subclip=check_if_subclip,
            reencode_values_to_string=reencode_values_to_string,
        )

    def get_collection_metadata(
        self,
        collection_id: str,
        view_id: str,
        *,
        check_if_subclip=UNSET,
        reencode_values_to_string=UNSET,
    ):
        "Get object metadata by object type, object ID and view ID (GET /v1/collections/{object_id}/views/{view_id}/)"
        from .metadata.api.object_type import (
            get_by_object_type_by_object_id_views_by_view_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("metadata"),
            object_type="collections",
            object_id=collection_id,
            view_id=view_id,
            check_if_subclip=check_if_subclip,
            reencode_values_to_string=reencode_values_to_string,
        )

    def get_segment_metadata(
        self,
        segment_id: str,
        view_id: str,
        *,
        check_if_subclip=UNSET,
        reencode_values_to_string=UNSET,
    ):
        "Get object metadata by object type, object ID and view ID (GET /v1/segments/{object_id}/views/{view_id}/)"
        from .metadata.api.object_type import (
            get_by_object_type_by_object_id_views_by_view_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("metadata"),
            object_type="segments",
            object_id=segment_id,
            view_id=view_id,
            check_if_subclip=check_if_subclip,
            reencode_values_to_string=reencode_values_to_string,
        )

    def get_object_categories_metadata(self, object_type: str):
        "Get metadata categories (GET /v1/{object_type}/categories/)"
        from .metadata.api.object_type import get_by_object_type_categories as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("metadata"), object_type=object_type
        )

    def get_object_categories_metadata_by_name(self, object_type: str, name: str):
        "Get metadata category by object type and category name (GET /v1/{object_type}/categories/{name}/)"
        from .metadata.api.object_type import (
            get_by_object_type_categories_by_name as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("metadata"), object_type=object_type, name=name
        )

    def get_object_categories_views_metadata_by_name(
        self, object_type: str, name: str, *, ext_options=UNSET, writable_only=UNSET
    ):
        "Get metadata views with field for object type and category (GET /v1/{object_type}/categories/{name}/views/)"
        from .metadata.api.object_type import (
            get_by_object_type_categories_by_name_views as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("metadata"),
            object_type=object_type,
            name=name,
            ext_options=ext_options,
            writable_only=writable_only,
        )

    def get_fields_metadata(
        self, *, per_page=UNSET, last_field_name=UNSET, filter_=UNSET
    ):
        "List the fields defined in the system (GET /v1/fields/)"
        from .metadata.api.fields import get_fields as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("metadata"),
            per_page=per_page,
            last_field_name=last_field_name,
            filter_=filter_,
        )

    def get_fields_metadata_by_field_name(self, field_name: str):
        "Returns a particular field by name (GET /v1/fields/{field_name}/)"
        from .metadata.api.fields import get_fields_by_field_name as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("metadata"), field_name=field_name
        )

    def get_mapping_fields_metadata_by_field_name(self, field_name: str):
        "Get the metadata field mapping (GET /v1/mapping/fields/{field_name}/)"
        from .metadata.api.mapping import get_mapping_fields_by_field_name as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("metadata"), field_name=field_name
        )

    def get_mapping_options_metadata(self):
        "List the metadata field mapping options (GET /v1/mapping/options/)"
        from .metadata.api.mapping import get_mapping_options as _endpoint

        return _endpoint.sync_detailed(client=self._client("metadata"))

    def get_shares_custom_actions_views_metadata_by_context_by_action(
        self, context: str, action_id: str, *, share_id, share_user_id
    ):
        "Returns a particular view for a shared custom action context (GET /v1/shares/custom_actions/{context}/{action_id}/views/)"
        from .metadata.api.shares import (
            get_shares_custom_actions_by_context_by_action_id_views as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("metadata"),
            context=context,
            action_id=action_id,
            share_id=share_id,
            share_user_id=share_user_id,
        )

    def get_user_fields_metadata(self):
        "List the fields that can be accessed by a user (GET /v1/user/fields/)"
        from .metadata.api.user import get_user_fields as _endpoint

        return _endpoint.sync_detailed(client=self._client("metadata"))

    def get_views_metadata(self, *, include_fields=UNSET, exclude_fields=UNSET):
        "List the views defined in the system (GET /v1/views/)"
        from .metadata.api.views import get_views as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("metadata"),
            include_fields=include_fields,
            exclude_fields=exclude_fields,
        )

    def get_view_metadata(self, view_id: str, *, merge_fields=UNSET):
        "Returns a particular view by id (GET /v1/views/{view_id}/)"
        from .metadata.api.views import get_views_by_view_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("metadata"), view_id=view_id, merge_fields=merge_fields
        )

    def patch_fields_metadata_by_field_name(self, field_name: str, *, body):
        "Update field by name (PATCH /v1/fields/{field_name}/)"
        from .metadata.api.fields import patch_fields_by_field_name as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("metadata"), field_name=field_name, body=body
        )

    def patch_view_metadata(self, view_id: str, *, body):
        "Update view (PATCH /v1/views/{view_id}/)"
        from .metadata.api.views import patch_views_by_view_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("metadata"), view_id=view_id, body=body
        )

    def post_object_categories_metadata(self, object_type: str, *, body):
        "Add a metadata category for an object type (POST /v1/{object_type}/categories/)"
        from .metadata.api.object_type import (
            post_by_object_type_categories as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("metadata"), object_type=object_type, body=body
        )

    def post_object_view_metadata(self, object_type: str, view_id: str, *, body):
        "Add view metadata values for multiple objects (Assets, Collections or Segments) (POST /v1/{object_type}/views/{view_id}/)"
        from .metadata.api.object_type import (
            post_by_object_type_views_by_view_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("metadata"),
            object_type=object_type,
            view_id=view_id,
            body=body,
        )

    def post_fields_metadata(self, *, body):
        "Create a new field (POST /v1/fields/)"
        from .metadata.api.fields import post_fields as _endpoint

        return _endpoint.sync_detailed(client=self._client("metadata"), body=body)

    def post_mapping_fields_metadata(self, *, body):
        "Create a new metadata field mapping (POST /v1/mapping/fields/)"
        from .metadata.api.mapping import post_mapping_fields as _endpoint

        return _endpoint.sync_detailed(client=self._client("metadata"), body=body)

    def post_views_metadata(self, *, body):
        "Create a new view (POST /v1/views/)"
        from .metadata.api.views import post_views as _endpoint

        return _endpoint.sync_detailed(client=self._client("metadata"), body=body)

    def post_view_reindex_metadata(self, view_id: str, *, body):
        "Reindex metadata views (POST /v1/views/{view_id}/reindex/)"
        from .metadata.api.views import post_views_by_view_id_reindex as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("metadata"), view_id=view_id, body=body
        )

    def post_views_reindex_metadata(self, *, body):
        "Reindex all metadata views for the current domain (POST /v1/views/reindex/)"
        from .metadata.api.views import post_views_reindex as _endpoint

        return _endpoint.sync_detailed(client=self._client("metadata"), body=body)

    def put_asset_object_view_metadata(
        self,
        asset_id: str,
        object_type: str,
        object_id: str,
        view_id: str,
        *,
        body,
        ignore_unchanged=UNSET,
    ):
        "Edit view metadata values for sub-objects of an asset (Such as segments) (PUT /v1/assets/{asset_id}/{object_type}/{object_id}/views/{view_id}/)"
        from .metadata.api.assets import (
            put_assets_by_asset_id_by_object_type_by_object_id_views_by_view_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("metadata"),
            asset_id=asset_id,
            object_type=object_type,
            object_id=object_id,
            view_id=view_id,
            body=body,
            ignore_unchanged=ignore_unchanged,
        )

    def put_object_metadata_direct(
        self,
        object_type: str,
        object_id: str,
        *,
        body,
        check_if_subclip=UNSET,
        ignore_unchanged=UNSET,
    ):
        "Edit metadata values directly without a view. Admin access required. (PUT /v1/{object_type}/{object_id}/)"
        from .metadata.api.object_type import (
            put_by_object_type_by_object_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("metadata"),
            object_type=object_type,
            object_id=object_id,
            body=body,
            check_if_subclip=check_if_subclip,
            ignore_unchanged=ignore_unchanged,
        )

    def put_object_metadata(
        self,
        object_type: str,
        object_id: str,
        view_id: str,
        *,
        body,
        check_if_subclip=UNSET,
        ignore_unchanged=UNSET,
    ):
        "Edit view metadata values for a single object (PUT /v1/{object_type}/{object_id}/views/{view_id}/)"
        from .metadata.api.object_type import (
            put_by_object_type_by_object_id_views_by_view_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("metadata"),
            object_type=object_type,
            object_id=object_id,
            view_id=view_id,
            body=body,
            check_if_subclip=check_if_subclip,
            ignore_unchanged=ignore_unchanged,
        )

    def put_asset_metadata(
        self,
        asset_id: str,
        view_id: str,
        *,
        body,
        check_if_subclip=UNSET,
        ignore_unchanged=UNSET,
    ):
        "Edit view metadata values for a single object (PUT /v1/assets/{object_id}/views/{view_id}/)"
        from .metadata.api.object_type import (
            put_by_object_type_by_object_id_views_by_view_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("metadata"),
            object_type="assets",
            object_id=asset_id,
            view_id=view_id,
            body=body,
            check_if_subclip=check_if_subclip,
            ignore_unchanged=ignore_unchanged,
        )

    def put_collection_metadata(
        self,
        collection_id: str,
        view_id: str,
        *,
        body,
        check_if_subclip=UNSET,
        ignore_unchanged=UNSET,
    ):
        "Edit view metadata values for a single object (PUT /v1/collections/{object_id}/views/{view_id}/)"
        from .metadata.api.object_type import (
            put_by_object_type_by_object_id_views_by_view_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("metadata"),
            object_type="collections",
            object_id=collection_id,
            view_id=view_id,
            body=body,
            check_if_subclip=check_if_subclip,
            ignore_unchanged=ignore_unchanged,
        )

    def put_segment_metadata(
        self,
        segment_id: str,
        view_id: str,
        *,
        body,
        check_if_subclip=UNSET,
        ignore_unchanged=UNSET,
    ):
        "Edit view metadata values for a single object (PUT /v1/segments/{object_id}/views/{view_id}/)"
        from .metadata.api.object_type import (
            put_by_object_type_by_object_id_views_by_view_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("metadata"),
            object_type="segments",
            object_id=segment_id,
            view_id=view_id,
            body=body,
            check_if_subclip=check_if_subclip,
            ignore_unchanged=ignore_unchanged,
        )

    def put_object_categories_metadata_by_name(
        self, object_type: str, name: str, *, body
    ):
        "Edit metadata category for an object type (PUT /v1/{object_type}/categories/{name}/)"
        from .metadata.api.object_type import (
            put_by_object_type_categories_by_name as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("metadata"),
            object_type=object_type,
            name=name,
            body=body,
        )

    def put_object_content_view_metadata(self, object_type: str, view_id: str, *, body):
        "Edit view metadata values for collection or saved search content. (PUT /v1/{object_type}/content/views/{view_id}/)"
        from .metadata.api.object_type import (
            put_by_object_type_content_views_by_view_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("metadata"),
            object_type=object_type,
            view_id=view_id,
            body=body,
        )

    def put_object_metadata_bulk(self, object_type: str, view_id: str, *, body):
        "Edit view metadata values for multiple objects (Assets, Collections or Segments) (PUT /v1/{object_type}/views/{view_id}/)"
        from .metadata.api.object_type import (
            put_by_object_type_views_by_view_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("metadata"),
            object_type=object_type,
            view_id=view_id,
            body=body,
        )

    def put_asset_metadata_bulk(self, view_id: str, *, body):
        "Edit view metadata values for multiple objects (Assets, Collections or Segments) (PUT /v1/assets/views/{view_id}/)"
        from .metadata.api.object_type import (
            put_by_object_type_views_by_view_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("metadata"),
            object_type="assets",
            view_id=view_id,
            body=body,
        )

    def put_collection_metadata_bulk(self, view_id: str, *, body):
        "Edit view metadata values for multiple objects (Assets, Collections or Segments) (PUT /v1/collections/views/{view_id}/)"
        from .metadata.api.object_type import (
            put_by_object_type_views_by_view_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("metadata"),
            object_type="collections",
            view_id=view_id,
            body=body,
        )

    def put_segment_metadata_bulk(self, view_id: str, *, body):
        "Edit view metadata values for multiple objects (Assets, Collections or Segments) (PUT /v1/segments/views/{view_id}/)"
        from .metadata.api.object_type import (
            put_by_object_type_views_by_view_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("metadata"),
            object_type="segments",
            view_id=view_id,
            body=body,
        )

    def put_fields_metadata_by_field_name(self, field_name: str, *, body):
        "Update field by name (PUT /v1/fields/{field_name}/)"
        from .metadata.api.fields import put_fields_by_field_name as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("metadata"), field_name=field_name, body=body
        )

    def put_view_metadata(self, view_id: str, *, body):
        "Update view (PUT /v1/views/{view_id}/)"
        from .metadata.api.views import put_views_by_view_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("metadata"), view_id=view_id, body=body
        )

    def delete_face_recognition_asset_persons_bulk(self, asset_id: str, *, body):
        "Delete all persons by asset and versions (DELETE /v1/face_recognition/assets/{asset_id}/persons/bulk/)"
        from .ml.api.face_recognition import (
            delete_face_recognition_assets_by_asset_id_persons_bulk as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("ml"), asset_id=asset_id, body=body
        )

    def delete_face_recognition_persons_bulk_delete(self, *, body):
        "Bulk delete multiple persons by ID (DELETE /v1/face_recognition/persons/bulk_delete/)"
        from .ml.api.face_recognition import (
            delete_face_recognition_persons_bulk_delete as _endpoint,
        )

        return _endpoint.sync_detailed(client=self._client("ml"), body=body)

    def delete_face_recognition_person(self, person_id: str):
        "Delete a person (DELETE /v1/face_recognition/persons/{person_id}/)"
        from .ml.api.face_recognition import (
            delete_face_recognition_persons_by_person_id as _endpoint,
        )

        return _endpoint.sync_detailed(client=self._client("ml"), person_id=person_id)

    def delete_face_recognition_person_asset_version(
        self, person_id: str, asset_id: str, version_id: str
    ):
        "Delete a person from an asset version (DELETE /v1/face_recognition/persons/{person_id}/assets/{asset_id}/versions/{version_id}/)"
        from .ml.api.face_recognition import (
            delete_face_recognition_persons_by_person_id_assets_by_asset_id_versions_by_version_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("ml"),
            person_id=person_id,
            asset_id=asset_id,
            version_id=version_id,
        )

    def delete_face_recognition_person_bulk(self, person_id: str, *, body):
        "Delete a persons's instances in bulk (DELETE /v1/face_recognition/persons/{person_id}/bulk/)"
        from .ml.api.face_recognition import (
            delete_face_recognition_persons_by_person_id_bulk as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("ml"), person_id=person_id, body=body
        )

    def get_face_recognition_asset_version_persons(
        self, asset_id: str, version_id: str, *, fetch_image_url=UNSET
    ):
        "List all persons associated with a specific asset version (GET /v1/face_recognition/assets/{asset_id}/versions/{version_id}/persons/)"
        from .ml.api.face_recognition import (
            get_face_recognition_assets_by_asset_id_versions_by_version_id_persons as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("ml"),
            asset_id=asset_id,
            version_id=version_id,
            fetch_image_url=fetch_image_url,
        )

    def get_face_recognition_persons(
        self,
        *,
        per_page=UNSET,
        page=UNSET,
        scroll=UNSET,
        scroll_id=UNSET,
        sort=UNSET,
        status=UNSET,
        name=UNSET,
        status_in=UNSET,
        has_name=UNSET,
    ):
        "Get all persons (GET /v1/face_recognition/persons/)"
        from .ml.api.face_recognition import get_face_recognition_persons as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("ml"),
            per_page=per_page,
            page=page,
            scroll=scroll,
            scroll_id=scroll_id,
            sort=sort,
            status=status,
            name=name,
            status_in=status_in,
            has_name=has_name,
        )

    def get_face_recognition_person(self, person_id: str):
        "Get a single person by ID (GET /v1/face_recognition/persons/{person_id}/)"
        from .ml.api.face_recognition import (
            get_face_recognition_persons_by_person_id as _endpoint,
        )

        return _endpoint.sync_detailed(client=self._client("ml"), person_id=person_id)

    def get_face_recognition_person_face_image_url(
        self, person_id: str, face_id: str, *, storage_id=UNSET
    ):
        "Get a presigned URL for a face image (GET /v1/face_recognition/persons/{person_id}/faces/{face_id}/image_url/)"
        from .ml.api.face_recognition import (
            get_face_recognition_persons_by_person_id_faces_by_face_id_image_url as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("ml"),
            person_id=person_id,
            face_id=face_id,
            storage_id=storage_id,
        )

    def get_face_recognition_person_versions(
        self,
        person_id: str,
        *,
        per_page=UNSET,
        page=UNSET,
        include_admin_details=UNSET,
        use_instance_as_main_face=UNSET,
    ):
        "List all person_id instances across assets versions (GET /v1/face_recognition/persons/{person_id}/versions/)"
        from .ml.api.face_recognition import (
            get_face_recognition_persons_by_person_id_versions as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("ml"),
            person_id=person_id,
            per_page=per_page,
            page=page,
            include_admin_details=include_admin_details,
            use_instance_as_main_face=use_instance_as_main_face,
        )

    def patch_face_recognition_person(self, person_id: str, *, body):
        "Update an existing person (PATCH /v1/face_recognition/persons/{person_id}/)"
        from .ml.api.face_recognition import (
            patch_face_recognition_persons_by_person_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("ml"), person_id=person_id, body=body
        )

    def post_face_recognition_bulk_extract(self, *, body=UNSET):
        "Run face recognition in bulk for different object types (POST /v1/face_recognition/bulk/extract/)"
        from .ml.api.face_recognition import (
            post_face_recognition_bulk_extract as _endpoint,
        )

        return _endpoint.sync_detailed(client=self._client("ml"), body=body)

    def post_face_recognition_embedding_reindex(self, embedding_id: str, *, body):
        "Reindex embedding (POST /v1/face_recognition/embeddings/{embedding_id}/reindex/)"
        from .ml.api.face_recognition import (
            post_face_recognition_embeddings_by_embedding_id_reindex as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("ml"), embedding_id=embedding_id, body=body
        )

    def post_face_recognition_embeddings_reindex(self, *, body=UNSET):
        "Trigger reindexing of all embeddings (POST /v1/face_recognition/embeddings/reindex/)"
        from .ml.api.face_recognition import (
            post_face_recognition_embeddings_reindex as _endpoint,
        )

        return _endpoint.sync_detailed(client=self._client("ml"), body=body)

    def post_face_recognition_extract_asset_version(
        self,
        asset_id: str,
        version_id: str,
        *,
        face_image_analysis_profile_id=UNSET,
        face_video_analysis_profile_id=UNSET,
        force=UNSET,
    ):
        "Extract face images and face data for an asset (POST /v1/face_recognition/extract/assets/{asset_id}/versions/{version_id}/)"
        from .ml.api.face_recognition import (
            post_face_recognition_extract_assets_by_asset_id_versions_by_version_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("ml"),
            asset_id=asset_id,
            version_id=version_id,
            face_image_analysis_profile_id=face_image_analysis_profile_id,
            face_video_analysis_profile_id=face_video_analysis_profile_id,
            force=force,
        )

    def post_face_recognition_person_asset_version_change_person(
        self, person_id: str, asset_id: str, version_id: str, *, body
    ):
        "Change a person asset version instance to another person (POST /v1/face_recognition/persons/{person_id}/assets/{asset_id}/versions/{version_id}/change_person/)"
        from .ml.api.face_recognition import (
            post_face_recognition_persons_by_person_id_assets_by_asset_id_versions_by_version_id_change_person as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("ml"),
            person_id=person_id,
            asset_id=asset_id,
            version_id=version_id,
            body=body,
        )

    def post_face_recognition_person_asset_version_confirm_person(
        self,
        person_id: str,
        asset_id: str,
        version_id: str,
        *,
        use_instance_as_main_face=UNSET,
    ):
        "Confirm a system unconfirmed person instance (POST /v1/face_recognition/persons/{person_id}/assets/{asset_id}/versions/{version_id}/confirm_person/)"
        from .ml.api.face_recognition import (
            post_face_recognition_persons_by_person_id_assets_by_asset_id_versions_by_version_id_confirm_person as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("ml"),
            person_id=person_id,
            asset_id=asset_id,
            version_id=version_id,
            use_instance_as_main_face=use_instance_as_main_face,
        )

    def post_face_recognition_person_confirm_person(self, person_id: str, *, body):
        "Confirms multiple person instances in bulk (POST /v1/face_recognition/persons/{person_id}/confirm_person/)"
        from .ml.api.face_recognition import (
            post_face_recognition_persons_by_person_id_confirm_person as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("ml"), person_id=person_id, body=body
        )

    def post_face_recognition_person_merge_by_new_person(
        self, person_id: str, new_person_id: str
    ):
        "Change an existing person to another person (POST /v1/face_recognition/persons/{person_id}/merge/{new_person_id}/)"
        from .ml.api.face_recognition import (
            post_face_recognition_persons_by_person_id_merge_by_new_person_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("ml"), person_id=person_id, new_person_id=new_person_id
        )

    def post_face_recognition_person_reindex(
        self,
        person_id: str,
        *,
        body=UNSET,
        sync_assets=UNSET,
        low_priority_indexing=UNSET,
    ):
        "Reindex person (POST /v1/face_recognition/persons/{person_id}/reindex/)"
        from .ml.api.face_recognition import (
            post_face_recognition_persons_by_person_id_reindex as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("ml"),
            person_id=person_id,
            body=body,
            sync_assets=sync_assets,
            low_priority_indexing=low_priority_indexing,
        )

    def post_face_recognition_person_update_and_confirm(self, person_id: str, *, body):
        "Updates person with name and confirms instances in bulk (POST /v1/face_recognition/persons/{person_id}/update_and_confirm/)"
        from .ml.api.face_recognition import (
            post_face_recognition_persons_by_person_id_update_and_confirm as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("ml"), person_id=person_id, body=body
        )

    def post_face_recognition_persons_reindex(
        self, *, body, sync_assets=UNSET, low_priority_indexing=UNSET
    ):
        "Trigger reindexing of persons by IDs (POST /v1/face_recognition/persons/reindex/)"
        from .ml.api.face_recognition import (
            post_face_recognition_persons_reindex as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("ml"),
            body=body,
            sync_assets=sync_assets,
            low_priority_indexing=low_priority_indexing,
        )

    def put_face_recognition_change_person_jobs_state(self, *, body):
        "Abort Change Person job (PUT /v1/face_recognition/change_person/jobs/state/)"
        from .ml.api.face_recognition import (
            put_face_recognition_change_person_jobs_state as _endpoint,
        )

        return _endpoint.sync_detailed(client=self._client("ml"), body=body)

    def put_face_recognition_jobs_priority(self, *, body):
        "Bulk-change priority of FR jobs (PUT /v1/face_recognition/jobs/priority/)"
        from .ml.api.face_recognition import (
            put_face_recognition_jobs_priority as _endpoint,
        )

        return _endpoint.sync_detailed(client=self._client("ml"), body=body)

    def put_face_recognition_jobs_state(self, *, body):
        "Bulk-abort / restart FR extraction jobs (PUT /v1/face_recognition/jobs/state/)"
        from .ml.api.face_recognition import (
            put_face_recognition_jobs_state as _endpoint,
        )

        return _endpoint.sync_detailed(client=self._client("ml"), body=body)

    def put_face_recognition_person(self, person_id: str, *, body):
        "Update an existing person (PUT /v1/face_recognition/persons/{person_id}/)"
        from .ml.api.face_recognition import (
            put_face_recognition_persons_by_person_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("ml"), person_id=person_id, body=body
        )

    def delete_webhook(self, webhook_id: str):
        "Delete a webhook (DELETE /v1/webhooks/{webhook_id}/)"
        from .notifications.api.webhooks import (
            delete_webhooks_by_webhook_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("notifications"), webhook_id=webhook_id
        )

    def get_webhooks(self):
        "Get all webhooks (GET /v1/webhooks/)"
        from .notifications.api.webhooks import get_webhooks as _endpoint

        return _endpoint.sync_detailed(client=self._client("notifications"))

    def get_webhook(self, webhook_id: str):
        "Get a webhook definition (GET /v1/webhooks/{webhook_id}/)"
        from .notifications.api.webhooks import get_webhooks_by_webhook_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("notifications"), webhook_id=webhook_id
        )

    def post_webhooks(self, *, body):
        "Create a new webhook (POST /v1/webhooks/)"
        from .notifications.api.webhooks import post_webhooks as _endpoint

        return _endpoint.sync_detailed(client=self._client("notifications"), body=body)

    def put_webhook(self, webhook_id: str, *, body):
        "Update a webhook (PUT /v1/webhooks/{webhook_id}/)"
        from .notifications.api.webhooks import put_webhooks_by_webhook_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("notifications"), webhook_id=webhook_id, body=body
        )

    def delete_discovery_default_entity(self, entity_id: str):
        "Delete a discovery entity by id (DELETE /v1/discovery/default/entities/{entity_id}/)"
        from .search.api.discovery import (
            delete_discovery_default_entities_by_entity_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("search"), entity_id=entity_id
        )

    def delete_favorites_search(self, *, body):
        "Deletes multiple saved searches from a list of favorites (DELETE /v1/favorites/)"
        from .search.api.favorites import delete_favorites as _endpoint

        return _endpoint.sync_detailed(client=self._client("search"), body=body)

    def delete_search_history_by_search_history(self, search_history_id: str):
        "Delete a search from history by its id (DELETE /v1/search/history/{search_history_id}/)"
        from .search.api.search import (
            delete_search_history_by_search_history_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("search"), search_history_id=search_history_id
        )

    def delete_search_saved_by_search(self, search_id: str):
        "Delete a saved search by its id (DELETE /v1/search/saved/{search_id}/)"
        from .search.api.search import delete_search_saved_by_search_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("search"), search_id=search_id
        )

    def delete_search_saved_group(self, group_id: str):
        "Delete a saved search group by it's id (DELETE /v1/search/saved/group/{group_id}/)"
        from .search.api.search import (
            delete_search_saved_group_by_group_id as _endpoint,
        )

        return _endpoint.sync_detailed(client=self._client("search"), group_id=group_id)

    def delete_search_saved_group_search(self, group_id: str, search_id: str):
        "Delete saved search from search group (DELETE /v1/search/saved/group/{group_id}/search/{search_id}/)"
        from .search.api.search import (
            delete_search_saved_group_by_group_id_search_by_search_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("search"), group_id=group_id, search_id=search_id
        )

    def delete_views(self, *, body=UNSET):
        "Delete Views for the system domain. (DELETE /v1/views/)"
        from .search.api.views import delete_views as _endpoint

        return _endpoint.sync_detailed(client=self._client("search"), body=body)

    def delete_view(self, view_id: str):
        "Delete a View for the system domain. (DELETE /v1/views/{view_id}/)"
        from .search.api.views import delete_views_by_view_id as _endpoint

        return _endpoint.sync_detailed(client=self._client("search"), view_id=view_id)

    def get_discovery_default_entities(self):
        "Returns the discovery entities that are used to build the discovery view. (GET /v1/discovery/default/entities/)"
        from .search.api.discovery import get_discovery_default_entities as _endpoint

        return _endpoint.sync_detailed(client=self._client("search"))

    def get_discovery_default_entities_admin(self):
        "Returns the discovery entities that are used to build the discovery view. (GET /v1/discovery/default/entities/admin/)"
        from .search.api.discovery import (
            get_discovery_default_entities_admin as _endpoint,
        )

        return _endpoint.sync_detailed(client=self._client("search"))

    def get_discovery_default_entity(self, entity_id: str):
        "Returns discovery entity (GET /v1/discovery/default/entities/{entity_id}/)"
        from .search.api.discovery import (
            get_discovery_default_entities_by_entity_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("search"), entity_id=entity_id
        )

    def get_ping_v2(self):
        "Routing health check (GET /v2/ping/)"
        from .search.api.ping import get_ping as _endpoint

        return _endpoint.sync_detailed(client=self._client("search"))

    def get_search_history(self):
        "Returns the current search history (GET /v1/search/history/)"
        from .search.api.search import get_search_history as _endpoint

        return _endpoint.sync_detailed(client=self._client("search"))

    def get_search_history_by_search_history(
        self,
        search_history_id: str,
        *,
        generate_signed_download_url=UNSET,
        generate_signed_proxy_url=UNSET,
    ):
        "Returns results of search history (GET /v1/search/history/{search_history_id}/)"
        from .search.api.search import (
            get_search_history_by_search_history_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("search"),
            search_history_id=search_history_id,
            generate_signed_download_url=generate_signed_download_url,
            generate_signed_proxy_url=generate_signed_proxy_url,
        )

    def get_search_saved(
        self,
        *,
        per_page=UNSET,
        page=UNSET,
        scroll=UNSET,
        scroll_id=UNSET,
        sort=UNSET,
        group_id=UNSET,
        ids=UNSET,
        query=UNSET,
        favorites=UNSET,
    ):
        "Returns list of saved searches (GET /v1/search/saved/)"
        from .search.api.search import get_search_saved as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("search"),
            per_page=per_page,
            page=page,
            scroll=scroll,
            scroll_id=scroll_id,
            sort=sort,
            group_id=group_id,
            ids=ids,
            query=query,
            favorites=favorites,
        )

    def get_search_saved_by_search(
        self,
        search_id: str,
        *,
        per_page=UNSET,
        page=UNSET,
        include_results=UNSET,
        generate_signed_download_url=UNSET,
        generate_signed_proxy_url=UNSET,
        scroll=UNSET,
        scroll_id=UNSET,
        search_after=UNSET,
    ):
        "Returns results of saved search (GET /v1/search/saved/{search_id}/)"
        from .search.api.search import get_search_saved_by_search_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("search"),
            search_id=search_id,
            per_page=per_page,
            page=page,
            include_results=include_results,
            generate_signed_download_url=generate_signed_download_url,
            generate_signed_proxy_url=generate_signed_proxy_url,
            scroll=scroll,
            scroll_id=scroll_id,
            search_after=search_after,
        )

    def get_search_saved_content_info_by_search(
        self, search_id: str, *, format_name=UNSET, by_storage_id=UNSET
    ):
        "Get aggregated information about saved search results (GET /v1/search/saved/{search_id}/content/info/)"
        from .search.api.search import (
            get_search_saved_by_search_id_content_info as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("search"),
            search_id=search_id,
            format_name=format_name,
            by_storage_id=by_storage_id,
        )

    def get_search_saved_group(self, group_id: str):
        "Returns saved search group data (GET /v1/search/saved/group/{group_id}/)"
        from .search.api.search import get_search_saved_group_by_group_id as _endpoint

        return _endpoint.sync_detailed(client=self._client("search"), group_id=group_id)

    def get_search_saved_groups(
        self, *, per_page=UNSET, page=UNSET, ids=UNSET, sort=UNSET
    ):
        "Returns paginated list of search groups (GET /v1/search/saved/groups/)"
        from .search.api.search import get_search_saved_groups as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("search"),
            per_page=per_page,
            page=page,
            ids=ids,
            sort=sort,
        )

    def get_views(self):
        "Get all Views for the system domain. (GET /v1/views/)"
        from .search.api.views import get_views as _endpoint

        return _endpoint.sync_detailed(client=self._client("search"))

    def get_view(self, view_id: str):
        "Get a View for the system domain. (GET /v1/views/{view_id}/)"
        from .search.api.views import get_views_by_view_id as _endpoint

        return _endpoint.sync_detailed(client=self._client("search"), view_id=view_id)

    def patch_discovery_default_entity(self, entity_id: str, *, body):
        "Update a discovery entity by id (PATCH /v1/discovery/default/entities/{entity_id}/)"
        from .search.api.discovery import (
            patch_discovery_default_entities_by_entity_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("search"), entity_id=entity_id, body=body
        )

    def patch_discovery_entities_object(
        self, object_type: str, object_id: str, *, body
    ):
        "Update a discovery entity by object's type and id (PATCH /v1/discovery/entities/{object_type}/{object_id}/)"
        from .search.api.discovery import (
            patch_discovery_entities_by_object_type_by_object_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("search"),
            object_type=object_type,
            object_id=object_id,
            body=body,
        )

    def patch_search_saved_by_search(self, search_id: str, *, body):
        "Search and save this search (PATCH /v1/search/saved/{search_id}/)"
        from .search.api.search import patch_search_saved_by_search_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("search"), search_id=search_id, body=body
        )

    def patch_search_saved_group(self, group_id: str, *, body):
        "Update and return saved search group data (PATCH /v1/search/saved/group/{group_id}/)"
        from .search.api.search import patch_search_saved_group_by_group_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("search"), group_id=group_id, body=body
        )

    def post_discovery_default_entities(self, *, body):
        "Adds a new discovery entity. (POST /v1/discovery/default/entities/)"
        from .search.api.discovery import post_discovery_default_entities as _endpoint

        return _endpoint.sync_detailed(client=self._client("search"), body=body)

    def post_favorites_search(self, *, body):
        "Adds multiple saved searches to a list of favorites (POST /v1/favorites/)"
        from .search.api.favorites import post_favorites as _endpoint

        return _endpoint.sync_detailed(client=self._client("search"), body=body)

    def post_nltf_parse(self, *, body):
        "Parse a natural language query into structured search filters (POST /v1/nltf_parse/)"
        from .search.api.nltf_parse import post_nltf_parse as _endpoint

        return _endpoint.sync_detailed(client=self._client("search"), body=body)

    def post_nltf_parse_v2(self, *, body):
        "NLTF Parse (POST /v2/nltf_parse/)"
        from .search.api.nltf_parse import post_nltf_parse_1 as _endpoint

        return _endpoint.sync_detailed(client=self._client("search"), body=body)

    def post_search(
        self,
        *,
        body,
        per_page=UNSET,
        page=UNSET,
        scroll=UNSET,
        scroll_id=UNSET,
        generate_signed_url=UNSET,
        generate_signed_download_url=UNSET,
        generate_signed_proxy_url=UNSET,
        save_search_history=UNSET,
        types=UNSET,
    ):
        "Search (POST /v1/search/)"
        from .search.api.search import post_search as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("search"),
            body=body,
            per_page=per_page,
            page=page,
            scroll=scroll,
            scroll_id=scroll_id,
            generate_signed_url=generate_signed_url,
            generate_signed_download_url=generate_signed_download_url,
            generate_signed_proxy_url=generate_signed_proxy_url,
            save_search_history=save_search_history,
            types=types,
        )

    def post_search_v2(
        self,
        *,
        body,
        per_page=UNSET,
        page=UNSET,
        scroll=UNSET,
        scroll_id=UNSET,
        generate_signed_url=UNSET,
        generate_signed_download_url=UNSET,
        generate_signed_proxy_url=UNSET,
        save_search_history=UNSET,
        types=UNSET,
        include_users=UNSET,
    ):
        "Search (POST /v2/search/)"
        from .search.api.search import post_search_1 as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("search"),
            body=body,
            per_page=per_page,
            page=page,
            scroll=scroll,
            scroll_id=scroll_id,
            generate_signed_url=generate_signed_url,
            generate_signed_download_url=generate_signed_download_url,
            generate_signed_proxy_url=generate_signed_proxy_url,
            save_search_history=save_search_history,
            types=types,
            include_users=include_users,
        )

    def post_search_saved(self, *, body):
        "Search, save and return result of this search (POST /v1/search/saved/)"
        from .search.api.search import post_search_saved as _endpoint

        return _endpoint.sync_detailed(client=self._client("search"), body=body)

    def post_search_saved_convert_to_collection_by_search(
        self, search_id: str, *, body
    ):
        "Converts the saved search to a collection (POST /v1/search/saved/{search_id}/convert_to_collection/)"
        from .search.api.search import (
            post_search_saved_by_search_id_convert_to_collection as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("search"), search_id=search_id, body=body
        )

    def post_search_saved_reindex_by_search(self, search_id: str, *, body):
        "Reindex a particular saved search by id (POST /v1/search/saved/{search_id}/reindex/)"
        from .search.api.search import (
            post_search_saved_by_search_id_reindex as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("search"), search_id=search_id, body=body
        )

    def post_search_saved_group(self, *, body):
        "Create and return saved search group data (POST /v1/search/saved/group/)"
        from .search.api.search import post_search_saved_group as _endpoint

        return _endpoint.sync_detailed(client=self._client("search"), body=body)

    def post_search_saved_group_search(self, group_id: str, search_id: str):
        "Adds saved search to group (POST /v1/search/saved/group/{group_id}/search/{search_id}/)"
        from .search.api.search import (
            post_search_saved_group_by_group_id_search_by_search_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("search"), group_id=group_id, search_id=search_id
        )

    def post_search_saved_group_reindex(self, group_id: str, *, body):
        "Reindex a particular saved search group by id (POST /v1/search/saved/groups/{group_id}/reindex/)"
        from .search.api.search import (
            post_search_saved_groups_by_group_id_reindex as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("search"), group_id=group_id, body=body
        )

    def post_search_suggest(self, *, body):
        "Returns search suggestions for a particular query. (POST /v1/search/suggest/)"
        from .search.api.search import post_search_suggest as _endpoint

        return _endpoint.sync_detailed(client=self._client("search"), body=body)

    def post_search_suggest_v2(self, *, body):
        "Search suggestions (POST /v2/search/suggest/)"
        from .search.api.search import post_search_suggest_1 as _endpoint

        return _endpoint.sync_detailed(client=self._client("search"), body=body)

    def post_views(self, *, body):
        "Insert a View for the system domain. (POST /v1/views/)"
        from .search.api.views import post_views as _endpoint

        return _endpoint.sync_detailed(client=self._client("search"), body=body)

    def put_discovery_default(self, *, body):
        "Update default discovery view (PUT /v1/discovery/default/)"
        from .search.api.discovery import put_discovery_default as _endpoint

        return _endpoint.sync_detailed(client=self._client("search"), body=body)

    def put_discovery_default_entity(self, entity_id: str, *, body):
        "Update a discovery entity by id (PUT /v1/discovery/default/entities/{entity_id}/)"
        from .search.api.discovery import (
            put_discovery_default_entities_by_entity_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("search"), entity_id=entity_id, body=body
        )

    def put_discovery_entities_object(self, object_type: str, object_id: str, *, body):
        "Update a discovery entity by object's type and id (PUT /v1/discovery/entities/{object_type}/{object_id}/)"
        from .search.api.discovery import (
            put_discovery_entities_by_object_type_by_object_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("search"),
            object_type=object_type,
            object_id=object_id,
            body=body,
        )

    def put_search_saved_by_search(self, search_id: str, *, body):
        "Search and save this search (PUT /v1/search/saved/{search_id}/)"
        from .search.api.search import put_search_saved_by_search_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("search"), search_id=search_id, body=body
        )

    def put_search_saved_group(self, group_id: str, *, body):
        "Update and return saved search group data (PUT /v1/search/saved/group/{group_id}/)"
        from .search.api.search import put_search_saved_group_by_group_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("search"), group_id=group_id, body=body
        )

    def put_view(self, view_id: str, *, body):
        "Replace a View for the system domain. (PUT /v1/views/{view_id}/)"
        from .search.api.views import put_views_by_view_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("search"), view_id=view_id, body=body
        )

    def delete_cors_host(self, cors_host_id: str):
        "Delete a particular CORS host by id (DELETE /v1/cors_hosts/{cors_host_id}/)"
        from .settings.api.cors_hosts import (
            delete_cors_hosts_by_cors_host_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("settings"), cors_host_id=cors_host_id
        )

    def delete_group_settings(self, group_id: str):
        "Delete group settings (DELETE /v1/group/{group_id}/)"
        from .settings.api.group import delete_group_by_group_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("settings"), group_id=group_id
        )

    def delete_search_view_group_ids_by_view(self, view_id: str, *, body):
        "Remove the Search View ID from any Group ID in the list. (DELETE /v1/search_view/{view_id}/group_ids/)"
        from .settings.api.search_view import (
            delete_search_view_by_view_id_group_ids as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("settings"), view_id=view_id, body=body
        )

    def delete_team_settings(self, team_id: str):
        "Delete team settings (DELETE /v1/team/{team_id}/)"
        from .settings.api.team import delete_team_by_team_id as _endpoint

        return _endpoint.sync_detailed(client=self._client("settings"), team_id=team_id)

    def delete_user_attributes(self, *, body):
        "Remove attributes from user settings (DELETE /v1/user/attributes/)"
        from .settings.api.user import delete_user_attributes as _endpoint

        return _endpoint.sync_detailed(client=self._client("settings"), body=body)

    def delete_user_settings(self, user_id: str):
        "Delete user settings (DELETE /v1/user/{user_id}/)"
        from .settings.api.user import delete_user_by_user_id as _endpoint

        return _endpoint.sync_detailed(client=self._client("settings"), user_id=user_id)

    def get_cors_hosts(self):
        "List of CORS hosts (GET /v1/cors_hosts/)"
        from .settings.api.cors_hosts import get_cors_hosts as _endpoint

        return _endpoint.sync_detailed(client=self._client("settings"))

    def get_cors_host(self, cors_host_id: str):
        "Returns a particular CORS host by id (GET /v1/cors_hosts/{cors_host_id}/)"
        from .settings.api.cors_hosts import get_cors_hosts_by_cors_host_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("settings"), cors_host_id=cors_host_id
        )

    def get_group_settings(self, group_id: str):
        "Group settings (GET /v1/group/{group_id}/)"
        from .settings.api.group import get_group_by_group_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("settings"), group_id=group_id
        )

    def get_merged_by_user(self, user_id: str, *, ignore_logo_url=UNSET):
        "Get merged settings for a specific user (GET /v1/merged/{user_id}/)"
        from .settings.api.merged import get_merged_by_user_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("settings"),
            user_id=user_id,
            ignore_logo_url=ignore_logo_url,
        )

    def get_merged_current(self, *, ignore_logo_url=UNSET):
        "Get merged settings for current user (GET /v1/merged/current/)"
        from .settings.api.merged import get_merged_current as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("settings"), ignore_logo_url=ignore_logo_url
        )

    def get_search_view_group_ids_by_view(self, view_id: str):
        "Get a list of Group IDs that use the given Search View ID (GET /v1/search_view/{view_id}/group_ids/)"
        from .settings.api.search_view import (
            get_search_view_by_view_id_group_ids as _endpoint,
        )

        return _endpoint.sync_detailed(client=self._client("settings"), view_id=view_id)

    def get_system_by_system_domain(
        self, system_domain_id: str, *, ignore_logo_url=UNSET
    ):
        "System settings (GET /v1/system/{system_domain_id}/)"
        from .settings.api.system import get_system_by_system_domain_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("settings"),
            system_domain_id=system_domain_id,
            ignore_logo_url=ignore_logo_url,
        )

    def get_system_current(self, *, ignore_logo_url=UNSET):
        "System settings (GET /v1/system/current/)"
        from .settings.api.system import get_system_current as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("settings"), ignore_logo_url=ignore_logo_url
        )

    def get_team_settings(self, team_id: str):
        "Team settings (GET /v1/team/{team_id}/)"
        from .settings.api.team import get_team_by_team_id as _endpoint

        return _endpoint.sync_detailed(client=self._client("settings"), team_id=team_id)

    def get_user_settings(self, user_id: str):
        "User settings (GET /v1/user/{user_id}/)"
        from .settings.api.user import get_user_by_user_id as _endpoint

        return _endpoint.sync_detailed(client=self._client("settings"), user_id=user_id)

    def patch_group_settings(self, group_id: str, *, body):
        "Change group settings (PATCH /v1/group/{group_id}/)"
        from .settings.api.group import patch_group_by_group_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("settings"), group_id=group_id, body=body
        )

    def patch_search_view_group_ids_by_view(self, view_id: str, *, body):
        "Update the Search View ID for each Group Settings object that (PATCH /v1/search_view/{view_id}/group_ids/)"
        from .settings.api.search_view import (
            patch_search_view_by_view_id_group_ids as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("settings"), view_id=view_id, body=body
        )

    def patch_system_by_system_domain(self, system_domain_id: str, *, body):
        "Change system settings (PATCH /v1/system/{system_domain_id}/)"
        from .settings.api.system import patch_system_by_system_domain_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("settings"),
            system_domain_id=system_domain_id,
            body=body,
        )

    def patch_system_current(self, *, body):
        "Change system settings (PATCH /v1/system/current/)"
        from .settings.api.system import patch_system_current as _endpoint

        return _endpoint.sync_detailed(client=self._client("settings"), body=body)

    def patch_team_settings(self, team_id: str, *, body):
        "Change team settings (PATCH /v1/team/{team_id}/)"
        from .settings.api.team import patch_team_by_team_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("settings"), team_id=team_id, body=body
        )

    def patch_user_settings(self, user_id: str, *, body):
        "Change user settings (PATCH /v1/user/{user_id}/)"
        from .settings.api.user import patch_user_by_user_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("settings"), user_id=user_id, body=body
        )

    def post_cors_hosts(self, *, body):
        "Create a new CORS host (POST /v1/cors_hosts/)"
        from .settings.api.cors_hosts import post_cors_hosts as _endpoint

        return _endpoint.sync_detailed(client=self._client("settings"), body=body)

    def put_group_settings(self, group_id: str, *, body):
        "Change group settings (PUT /v1/group/{group_id}/)"
        from .settings.api.group import put_group_by_group_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("settings"), group_id=group_id, body=body
        )

    def put_search_view_group_ids_by_view(self, view_id: str, *, body):
        "Set the Search View ID for each Group Settings object that (PUT /v1/search_view/{view_id}/group_ids/)"
        from .settings.api.search_view import (
            put_search_view_by_view_id_group_ids as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("settings"), view_id=view_id, body=body
        )

    def put_system_by_system_domain(self, system_domain_id: str, *, body):
        "Change system settings (PUT /v1/system/{system_domain_id}/)"
        from .settings.api.system import put_system_by_system_domain_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("settings"),
            system_domain_id=system_domain_id,
            body=body,
        )

    def put_system_current(self, *, body):
        "Change system settings (PUT /v1/system/current/)"
        from .settings.api.system import put_system_current as _endpoint

        return _endpoint.sync_detailed(client=self._client("settings"), body=body)

    def put_team_settings(self, team_id: str, *, body):
        "Change team settings (PUT /v1/team/{team_id}/)"
        from .settings.api.team import put_team_by_team_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("settings"), team_id=team_id, body=body
        )

    def put_user_settings(self, user_id: str, *, body):
        "Change user settings (PUT /v1/user/{user_id}/)"
        from .settings.api.user import put_user_by_user_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("settings"), user_id=user_id, body=body
        )

    def delete_billing_by_system_domain_by_billing(
        self, system_domain_id: str, billing_id: str
    ):
        "Delete billing record (Requires super admin access). (DELETE /v1/billing/{system_domain_id}/{billing_id}/)"
        from .stats.api.billing import (
            delete_billing_by_system_domain_id_by_billing_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("stats"),
            system_domain_id=system_domain_id,
            billing_id=billing_id,
        )

    def delete_billing_customer_card(self):
        "Creates billing customer card (DELETE /v1/billing/customer/card/)"
        from .stats.api.billing import delete_billing_customer_card as _endpoint

        return _endpoint.sync_detailed(client=self._client("stats"))

    def delete_billing_expiration_by_system_domain_by_billing(
        self, system_domain_id: str, billing_id: str
    ):
        "Delete billing expiration record (Requires super admin access). (DELETE /v1/billing_expiration/{system_domain_id}/{billing_id}/)"
        from .stats.api.billing_expiration import (
            delete_billing_expiration_by_system_domain_id_by_billing_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("stats"),
            system_domain_id=system_domain_id,
            billing_id=billing_id,
        )

    def delete_billing_price_lists_by_name_by_currency(self, name: str, currency: str):
        "Delete a Price list (DELETE /v1/billing/price_lists/{name}/{currency}/)"
        from .stats.api.billing import (
            delete_billing_price_lists_by_name_by_currency as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("stats"), name=name, currency=currency
        )

    def delete_system_logs_recipients_by_logs_recipient(self, logs_recipient_id: str):
        "Delete logs recipient settings (DELETE /v1/system/logs/recipients/{logs_recipient_id}/)"
        from .stats.api.system import (
            delete_system_logs_recipients_by_logs_recipient_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("stats"), logs_recipient_id=logs_recipient_id
        )

    def get_assets_by_by_period(self, period: str, *, from_date=UNSET, to_date=UNSET):
        "Returns all asset usage (GET /v1/assets/by/{period}/)"
        from .stats.api.assets import get_assets_by_by_period as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("stats"),
            period=period,
            from_date=from_date,
            to_date=to_date,
        )

    def get_automations_usage_by_day(self, *, from_date=UNSET, to_date=UNSET):
        "Returns automation runs by day. (GET /v1/automations/usage/by/day/)"
        from .stats.api.automations import get_automations_usage_by_day as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("stats"), from_date=from_date, to_date=to_date
        )

    def get_billing(
        self, *, from_date=UNSET, to_date=UNSET, per_page=UNSET, last_id=UNSET
    ):
        "Returns billing info (GET /v1/billing/)"
        from .stats.api.billing import get_billing as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("stats"),
            from_date=from_date,
            to_date=to_date,
            per_page=per_page,
            last_id=last_id,
        )

    def get_billing_charge_receipt_url(self, charge_id: str):
        "Returns billing receipt (GET /v1/billing/charges/{charge_id}/receipt_url/)"
        from .stats.api.billing import (
            get_billing_charges_by_charge_id_receipt_url as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("stats"), charge_id=charge_id
        )

    def get_billing_credits_price(self, *, credits_):
        "Checks the total price that needs to be paid including VAT if it's needed (GET /v1/billing/credits/price/)"
        from .stats.api.billing import get_billing_credits_price as _endpoint

        return _endpoint.sync_detailed(client=self._client("stats"), credits_=credits_)

    def get_billing_customer(self):
        "Returns billing customer (GET /v1/billing/customer/)"
        from .stats.api.billing import get_billing_customer as _endpoint

        return _endpoint.sync_detailed(client=self._client("stats"))

    def get_billing_expiration(self, *, per_page=UNSET):
        "Returns billing expiration info (GET /v1/billing_expiration/)"
        from .stats.api.billing_expiration import get_billing_expiration as _endpoint

        return _endpoint.sync_detailed(client=self._client("stats"), per_page=per_page)

    def get_billing_invoices(self, *, starting_after=UNSET, limit=UNSET):
        "Returns billing invoices (GET /v1/billing/invoices/)"
        from .stats.api.billing import get_billing_invoices as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("stats"), starting_after=starting_after, limit=limit
        )

    def get_billing_price_lists(self):
        "Get All Price Lists (GET /v1/billing/price_lists/)"
        from .stats.api.billing import get_billing_price_lists as _endpoint

        return _endpoint.sync_detailed(client=self._client("stats"))

    def get_billing_price_lists_by_name_by_currency(self, name: str, currency: str):
        "Get a Price List (GET /v1/billing/price_lists/{name}/{currency}/)"
        from .stats.api.billing import (
            get_billing_price_lists_by_name_by_currency as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("stats"), name=name, currency=currency
        )

    def get_billing_recipients(self):
        "Updates Billing Recipients (GET /v1/billing/recipients/)"
        from .stats.api.billing import get_billing_recipients as _endpoint

        return _endpoint.sync_detailed(client=self._client("stats"))

    def get_billing_settings(self):
        "Updates Billing Settings (GET /v1/billing/settings/)"
        from .stats.api.billing import get_billing_settings as _endpoint

        return _endpoint.sync_detailed(client=self._client("stats"))

    def get_billing_status(self):
        "Returns billing status (GET /v1/billing/status/)"
        from .stats.api.billing import get_billing_status as _endpoint

        return _endpoint.sync_detailed(client=self._client("stats"))

    def get_collections_by_by_period(
        self, period: str, *, from_date=UNSET, to_date=UNSET
    ):
        "Returns all collection usage (GET /v1/collections/by/{period}/)"
        from .stats.api.collections import get_collections_by_by_period as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("stats"),
            period=period,
            from_date=from_date,
            to_date=to_date,
        )

    def get_current_usage(self, *, per_page=UNSET):
        "Returns current usage for system domains (GET /v1/current_usage/)"
        from .stats.api.current_usage import get_current_usage as _endpoint

        return _endpoint.sync_detailed(client=self._client("stats"), per_page=per_page)

    def get_id_info(self, object_id: str):
        "Internal endpoint to convert ID to system domain (GET /v1/id/{object_id}/info/)"
        from .stats.api.id import get_id_by_object_id_info as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("stats"), object_id=object_id
        )

    def get_ordway_billing(
        self, *, from_date=UNSET, to_date=UNSET, per_page=UNSET, page=UNSET
    ):
        "Returns billing info (GET /v1/ordway/billing/)"
        from .stats.api.ordway import get_ordway_billing as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("stats"),
            from_date=from_date,
            to_date=to_date,
            per_page=per_page,
            page=page,
        )

    def get_ordway_billing_customer(self):
        "Returns billing customer (GET /v1/ordway/billing/customer/)"
        from .stats.api.ordway import get_ordway_billing_customer as _endpoint

        return _endpoint.sync_detailed(client=self._client("stats"))

    def get_ordway_billing_invoices(self, *, per_page=UNSET, page=UNSET):
        "Returns billing invoices (GET /v1/ordway/billing/invoices/)"
        from .stats.api.ordway import get_ordway_billing_invoices as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("stats"), per_page=per_page, page=page
        )

    def get_paygo_costs(self):
        "Returns monthly costs from billing (GET /v1/paygo_costs/)"
        from .stats.api.paygo_costs import get_paygo_costs as _endpoint

        return _endpoint.sync_detailed(client=self._client("stats"))

    def get_storage_access_by_by_period(
        self, period: str, *, from_date=UNSET, to_date=UNSET
    ):
        "Returns storage_access for all storages (GET /v1/storage/access/by/{period}/)"
        from .stats.api.storage import get_storage_access_by_by_period as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("stats"),
            period=period,
            from_date=from_date,
            to_date=to_date,
        )

    def get_storage_usage_by_by_period(
        self, period: str, *, from_date=UNSET, to_date=UNSET
    ):
        "Returns storage_usage for all storages (GET /v1/storage/usage/by/{period}/)"
        from .stats.api.storage import get_storage_usage_by_by_period as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("stats"),
            period=period,
            from_date=from_date,
            to_date=to_date,
        )

    def get_system_logs_recipients(self, *, per_page=UNSET, last_id=UNSET):
        "Get logs recipients settings (GET /v1/system/logs/recipients/)"
        from .stats.api.system import get_system_logs_recipients as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("stats"), per_page=per_page, last_id=last_id
        )

    def get_system_logs_recipients_by_logs_recipient(self, logs_recipient_id: str):
        "Get settings of a logs recipient (GET /v1/system/logs/recipients/{logs_recipient_id}/)"
        from .stats.api.system import (
            get_system_logs_recipients_by_logs_recipient_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("stats"), logs_recipient_id=logs_recipient_id
        )

    def get_transcoder_usage_by_by_period(
        self, period: str, *, from_date=UNSET, to_date=UNSET
    ):
        "Returns transcoder_usage for all transcoders (GET /v1/transcoder/usage/by/{period}/)"
        from .stats.api.transcoder import get_transcoder_usage_by_by_period as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("stats"),
            period=period,
            from_date=from_date,
            to_date=to_date,
        )

    def get_user_audit_by_by_period(
        self, period: str, *, from_date=UNSET, to_date=UNSET, system_domain_id=UNSET
    ):
        "Returns all audit (GET /v1/user/audit/by/{period}/)"
        from .stats.api.user import get_user_audit_by_by_period as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("stats"),
            period=period,
            from_date=from_date,
            to_date=to_date,
            system_domain_id=system_domain_id,
        )

    def get_user_licensed_by(
        self, *, from_date=UNSET, to_date=UNSET, system_domain_id=UNSET
    ):
        "Returns licensed user usage (GET /v1/user/licensed/by/)"
        from .stats.api.user import get_user_licensed_by as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("stats"),
            from_date=from_date,
            to_date=to_date,
            system_domain_id=system_domain_id,
        )

    def patch_system_logs_recipients_by_logs_recipient(
        self, logs_recipient_id: str, *, body
    ):
        "Change logs recipient settings (PATCH /v1/system/logs/recipients/{logs_recipient_id}/)"
        from .stats.api.system import (
            patch_system_logs_recipients_by_logs_recipient_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("stats"), logs_recipient_id=logs_recipient_id, body=body
        )

    def post_assets_stats(self, *, body):
        "Sets asset usage. (POST /v1/assets/)"
        from .stats.api.assets import post_assets as _endpoint

        return _endpoint.sync_detailed(client=self._client("stats"), body=body)

    def post_billing(self, *, body):
        "Updates Billing (Requires super admin access). (POST /v1/billing/)"
        from .stats.api.billing import post_billing as _endpoint

        return _endpoint.sync_detailed(client=self._client("stats"), body=body)

    def post_billing_credits(self, *, body):
        "Add credits to an account (POST /v1/billing/credits/)"
        from .stats.api.billing import post_billing_credits as _endpoint

        return _endpoint.sync_detailed(client=self._client("stats"), body=body)

    def post_billing_credits_verify(self, *, body):
        "Verify status of add credits to an account (POST /v1/billing/credits/verify/)"
        from .stats.api.billing import post_billing_credits_verify as _endpoint

        return _endpoint.sync_detailed(client=self._client("stats"), body=body)

    def post_billing_customer(self, *, body):
        "Updates billing customer (POST /v1/billing/customer/)"
        from .stats.api.billing import post_billing_customer as _endpoint

        return _endpoint.sync_detailed(client=self._client("stats"), body=body)

    def post_billing_customer_card(self, *, body):
        "Creates billing customer card (POST /v1/billing/customer/card/)"
        from .stats.api.billing import post_billing_customer_card as _endpoint

        return _endpoint.sync_detailed(client=self._client("stats"), body=body)

    def post_system_logs_recipients(self, *, body):
        "Create logs recipient settings (POST /v1/system/logs/recipients/)"
        from .stats.api.system import post_system_logs_recipients as _endpoint

        return _endpoint.sync_detailed(client=self._client("stats"), body=body)

    def post_system_logs_recipients_by_logs_recipient(self, logs_recipient_id: str):
        "Test logs recipient connection (POST /v1/system/logs/recipients/{logs_recipient_id}/)"
        from .stats.api.system import (
            post_system_logs_recipients_by_logs_recipient_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("stats"), logs_recipient_id=logs_recipient_id
        )

    def put_billing_expiration_by_system_domain_by_billing(
        self, system_domain_id: str, billing_id: str, *, body
    ):
        "Update billing expiration record (Requires super admin access). (PUT /v1/billing_expiration/{system_domain_id}/{billing_id}/)"
        from .stats.api.billing_expiration import (
            put_billing_expiration_by_system_domain_id_by_billing_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("stats"),
            system_domain_id=system_domain_id,
            billing_id=billing_id,
            body=body,
        )

    def put_billing_price_lists(self, *, body):
        "Creates or updates a Price List (PUT /v1/billing/price_lists/)"
        from .stats.api.billing import put_billing_price_lists as _endpoint

        return _endpoint.sync_detailed(client=self._client("stats"), body=body)

    def put_billing_recipients(self, *, body):
        "Updates Billing Recipients (PUT /v1/billing/recipients/)"
        from .stats.api.billing import put_billing_recipients as _endpoint

        return _endpoint.sync_detailed(client=self._client("stats"), body=body)

    def put_billing_settings(self, *, body):
        "Updates Billing Settings (PUT /v1/billing/settings/)"
        from .stats.api.billing import put_billing_settings as _endpoint

        return _endpoint.sync_detailed(client=self._client("stats"), body=body)

    def put_system_logs_recipients_by_logs_recipient(
        self, logs_recipient_id: str, *, body
    ):
        "Change logs recipient settings (PUT /v1/system/logs/recipients/{logs_recipient_id}/)"
        from .stats.api.system import (
            put_system_logs_recipients_by_logs_recipient_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("stats"), logs_recipient_id=logs_recipient_id, body=body
        )

    def delete_edge_transcode_worker(self, worker_id: str):
        "Delete a edge transcode worker (DELETE /v1/edge_transcode/workers/{worker_id}/)"
        from .transcode.api.edge_transcode import (
            delete_edge_transcode_workers_by_worker_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("transcode"), worker_id=worker_id
        )

    def delete_storage_transcode(self, storage_id: str, *, body=UNSET):
        "Cancel all transcode jobs linked to the storage (DELETE /v1/storages/{storage_id}/)"
        from .transcode.api.storages import delete_storages_by_storage_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("transcode"), storage_id=storage_id, body=body
        )

    def delete_storage_file_transcode(self, storage_id: str, file_id: str):
        "Delete local storage transcode job. (DELETE /v1/storages/{storage_id}/files/{file_id}/transcode/)"
        from .transcode.api.storages import (
            delete_storages_by_storage_id_files_by_file_id_transcode as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("transcode"), storage_id=storage_id, file_id=file_id
        )

    def delete_storage_transcode_by_record(self, storage_id: str, record_id: str):
        "Delete local storage transcode job. (DELETE /v1/storages/{storage_id}/transcode/{record_id}/)"
        from .transcode.api.storages import (
            delete_storages_by_storage_id_transcode_by_record_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("transcode"), storage_id=storage_id, record_id=record_id
        )

    def delete_transcode_by_transcode_job(self, transcode_job_id: str):
        "Cancel a particular transcode job by id (DELETE /v1/transcode/{transcode_job_id}/)"
        from .transcode.api.transcode import (
            delete_transcode_by_transcode_job_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("transcode"), transcode_job_id=transcode_job_id
        )

    def get_edge_transcode_workers(self):
        "Get edge transcode workers (GET /v1/edge_transcode/workers/)"
        from .transcode.api.edge_transcode import (
            get_edge_transcode_workers as _endpoint,
        )

        return _endpoint.sync_detailed(client=self._client("transcode"))

    def get_edge_transcode_worker(self, worker_id: str):
        "Get a edge transcode worker (GET /v1/edge_transcode/workers/{worker_id}/)"
        from .transcode.api.edge_transcode import (
            get_edge_transcode_workers_by_worker_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("transcode"), worker_id=worker_id
        )

    def get_metadata_filling_proposals_asset_version(
        self, asset_id: str, version_id: str, *, user_id
    ):
        "Fetch the caller's PENDING_USER LLM proposal for an asset version (GET /v1/metadata_filling/proposals/assets/{asset_id}/versions/{version_id}/)"
        from .transcode.api.metadata_filling import (
            get_metadata_filling_proposals_assets_by_asset_id_versions_by_version_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("transcode"),
            asset_id=asset_id,
            version_id=version_id,
            user_id=user_id,
        )

    def get_metadata_filling_proposals_by_job(self, job_id: str):
        "Fetch the LLM-generated metadata proposal for a completed sub-job (GET /v1/metadata_filling/proposals/{job_id}/)"
        from .transcode.api.metadata_filling import (
            get_metadata_filling_proposals_by_job_id as _endpoint,
        )

        return _endpoint.sync_detailed(client=self._client("transcode"), job_id=job_id)

    def get_storage_edge_transcode_jobs(self, storage_id: str, *, limit=UNSET):
        "Get a edge transcode jobs from the job queue (GET /v1/storages/{storage_id}/edge_transcode/jobs/)"
        from .transcode.api.storages import (
            get_storages_by_storage_id_edge_transcode_jobs as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("transcode"), storage_id=storage_id, limit=limit
        )

    def get_storage_transcode(self, storage_id: str, *, per_page=UNSET, last_id=UNSET):
        "Get pending local storage transcode jobs. (GET /v1/storages/{storage_id}/transcode/)"
        from .transcode.api.storages import (
            get_storages_by_storage_id_transcode as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("transcode"),
            storage_id=storage_id,
            per_page=per_page,
            last_id=last_id,
        )

    def get_storage_transcode_by_record(self, storage_id: str, record_id: str):
        "Get local storage transcode job. (GET /v1/storages/{storage_id}/transcode/{record_id}/)"
        from .transcode.api.storages import (
            get_storages_by_storage_id_transcode_by_record_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("transcode"), storage_id=storage_id, record_id=record_id
        )

    def get_transcode_object(self, object_type: str, object_id: str):
        "Returns list of transcode queue records by object_id (GET /v1/transcode/{object_type}/{object_id}/)"
        from .transcode.api.transcode import (
            get_transcode_by_object_type_by_object_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("transcode"),
            object_type=object_type,
            object_id=object_id,
        )

    def get_transcode_object_version(
        self, object_type: str, object_id: str, version_id: str
    ):
        "Returns list of transcode queue records by version_id (GET /v1/transcode/{object_type}/{object_id}/versions/{version_id}/)"
        from .transcode.api.transcode import (
            get_transcode_by_object_type_by_object_id_versions_by_version_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("transcode"),
            object_type=object_type,
            object_id=object_id,
            version_id=version_id,
        )

    def get_transcode_by_transcode_job(self, transcode_job_id: str):
        "Get transcode job (GET /v1/transcode/{transcode_job_id}/)"
        from .transcode.api.transcode import (
            get_transcode_by_transcode_job_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("transcode"), transcode_job_id=transcode_job_id
        )

    def get_transcode_queue(self, *, per_page=UNSET, page=UNSET, sort=UNSET):
        "Get all the statuses of the queued transcode jobs (GET /v1/transcode/queue/)"
        from .transcode.api.transcode import get_transcode_queue as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("transcode"), per_page=per_page, page=page, sort=sort
        )

    def get_transcode_queue_system(
        self, *, per_domain_id=UNSET, per_page=UNSET, page=UNSET, sort=UNSET
    ):
        "Get the status of the transcode job queues (GET /v1/transcode/queue/system/)"
        from .transcode.api.transcode import get_transcode_queue_system as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("transcode"),
            per_domain_id=per_domain_id,
            per_page=per_page,
            page=page,
            sort=sort,
        )

    def patch_edge_transcode_worker(self, worker_id: str, *, body):
        "Update a edge transcode worker (PATCH /v1/edge_transcode/workers/{worker_id}/)"
        from .transcode.api.edge_transcode import (
            patch_edge_transcode_workers_by_worker_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("transcode"), worker_id=worker_id, body=body
        )

    def post_analyze_asset(self, asset_id: str, *, body=UNSET):
        "Start a job that sends an asset for analysis (POST /v1/analyze/assets/{asset_id}/)"
        from .transcode.api.analyze import post_analyze_assets_by_asset_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("transcode"), asset_id=asset_id, body=body
        )

    def post_analyze_asset_profile(self, asset_id: str, profile_id: str, *, body=UNSET):
        "Start a job that sends an asset for analysis with a custom analysis profile (POST /v1/analyze/assets/{asset_id}/profiles/{profile_id}/)"
        from .transcode.api.analyze import (
            post_analyze_assets_by_asset_id_profiles_by_profile_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("transcode"),
            asset_id=asset_id,
            profile_id=profile_id,
            body=body,
        )

    def post_analyze_asset_profiles_default(self, asset_id: str, *, body=UNSET):
        "Start a job that sends an asset for analysis with a default analysis profile (POST /v1/analyze/assets/{asset_id}/profiles/default/)"
        from .transcode.api.analyze import (
            post_analyze_assets_by_asset_id_profiles_default as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("transcode"), asset_id=asset_id, body=body
        )

    def post_analyze_asset_profiles_default_by_media_type(
        self, asset_id: str, media_type: str, *, body=UNSET
    ):
        "Start a job that sends an asset for analysis (POST /v1/analyze/assets/{asset_id}/profiles/default/{media_type}/)"
        from .transcode.api.analyze import (
            post_analyze_assets_by_asset_id_profiles_default_by_media_type as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("transcode"),
            asset_id=asset_id,
            media_type=media_type,
            body=body,
        )

    def post_analyze_bulk(self, *, body=UNSET):
        "Start a job that sends objects for analysis using a custom analysis profile (POST /v1/analyze/bulk/)"
        from .transcode.api.analyze import post_analyze_bulk as _endpoint

        return _endpoint.sync_detailed(client=self._client("transcode"), body=body)

    def post_edge_transcode_job_acknowledge(self, job_id: str):
        "Acknowledge an edge transcode job (POST /v1/edge_transcode/jobs/{job_id}/acknowledge/)"
        from .transcode.api.edge_transcode import (
            post_edge_transcode_jobs_by_job_id_acknowledge as _endpoint,
        )

        return _endpoint.sync_detailed(client=self._client("transcode"), job_id=job_id)

    def post_edge_transcode_workers(self, *, body):
        "Create a new edge transcode worker (POST /v1/edge_transcode/workers/)"
        from .transcode.api.edge_transcode import (
            post_edge_transcode_workers as _endpoint,
        )

        return _endpoint.sync_detailed(client=self._client("transcode"), body=body)

    def post_keyframes_collection(self, collection_id: str, *, body=UNSET):
        "Start a job that creates a collection keyframe (POST /v1/keyframes/collections/{collection_id}/)"
        from .transcode.api.keyframes import (
            post_keyframes_collections_by_collection_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("transcode"), collection_id=collection_id, body=body
        )

    def post_keyframes_playlist(self, playlist_id: str, *, body=UNSET):
        "Start a job that creates a playlist keyframe (POST /v1/keyframes/playlists/{playlist_id}/)"
        from .transcode.api.keyframes import (
            post_keyframes_playlists_by_playlist_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("transcode"), playlist_id=playlist_id, body=body
        )

    def post_metadata_filling_asset_version(
        self, asset_id: str, version_id: str, *, body
    ):
        "Enqueue enriched metadata filling for a single asset version (POST /v1/metadata_filling/assets/{asset_id}/versions/{version_id}/)"
        from .transcode.api.metadata_filling import (
            post_metadata_filling_assets_by_asset_id_versions_by_version_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("transcode"),
            asset_id=asset_id,
            version_id=version_id,
            body=body,
        )

    def post_metadata_filling_bulk(self, *, body):
        "Run bulk AI metadata filling (POST /v1/metadata_filling/bulk/)"
        from .transcode.api.metadata_filling import (
            post_metadata_filling_bulk as _endpoint,
        )

        return _endpoint.sync_detailed(client=self._client("transcode"), body=body)

    def post_metadata_filling_proposals_accept_by_job(self, job_id: str, *, user_id):
        "Accept an AI metadata-filling proposal (POST /v1/metadata_filling/proposals/{job_id}/accept/)"
        from .transcode.api.metadata_filling import (
            post_metadata_filling_proposals_by_job_id_accept as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("transcode"), job_id=job_id, user_id=user_id
        )

    def post_metadata_filling_proposals_discard_by_job(self, job_id: str, *, user_id):
        "Discard an AI metadata-filling proposal (POST /v1/metadata_filling/proposals/{job_id}/discard/)"
        from .transcode.api.metadata_filling import (
            post_metadata_filling_proposals_by_job_id_discard as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("transcode"), job_id=job_id, user_id=user_id
        )

    def post_metadata_filling_proposals_regenerate_by_job(
        self, job_id: str, *, user_id
    ):
        "Regenerate an AI metadata-filling proposal (POST /v1/metadata_filling/proposals/{job_id}/regenerate/)"
        from .transcode.api.metadata_filling import (
            post_metadata_filling_proposals_by_job_id_regenerate as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("transcode"), job_id=job_id, user_id=user_id
        )

    def post_transcode(self, *, body):
        "Starts a new transcode. (POST /v1/transcode/)"
        from .transcode.api.transcode import post_transcode as _endpoint

        return _endpoint.sync_detailed(client=self._client("transcode"), body=body)

    def post_transcode_position_by_transcode_job_by_position(
        self, transcode_job_id: str, position: str
    ):
        "Move transcode job to top or bottom of the queue (POST /v1/transcode/{transcode_job_id}/position/{position}/)"
        from .transcode.api.transcode import (
            post_transcode_by_transcode_job_id_position_by_position as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("transcode"),
            transcode_job_id=transcode_job_id,
            position=position,
        )

    def post_transcribe_asset_profiles_default(self, asset_id: str, *, body=UNSET):
        "Start a job that sends an asset to default transcription service (POST /v1/transcribe/assets/{asset_id}/profiles/default/)"
        from .transcode.api.transcribe import (
            post_transcribe_assets_by_asset_id_profiles_default as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("transcode"), asset_id=asset_id, body=body
        )

    def post_transcribe_bulk(self, *, body):
        "Start a job that sends multiple objects to transcription service (POST /v1/transcribe/bulk/)"
        from .transcode.api.transcribe import post_transcribe_bulk as _endpoint

        return _endpoint.sync_detailed(client=self._client("transcode"), body=body)

    def put_edge_transcode_worker(self, worker_id: str, *, body):
        "Update a edge transcode worker (PUT /v1/edge_transcode/workers/{worker_id}/)"
        from .transcode.api.edge_transcode import (
            put_edge_transcode_workers_by_worker_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("transcode"), worker_id=worker_id, body=body
        )

    def put_transcode_priority_by_transcode_job_by_priority(
        self, transcode_job_id: str, priority: int
    ):
        "Change transcode job priority (PUT /v1/transcode/{transcode_job_id}/priority/{priority}/)"
        from .transcode.api.transcode import (
            put_transcode_by_transcode_job_id_priority_by_priority as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("transcode"),
            transcode_job_id=transcode_job_id,
            priority=priority,
        )

    def delete_group_users(self, group_id: str):
        "Delete a particular group by id (DELETE /v1/groups/{group_id}/)"
        from .users.api.groups import delete_groups_by_group_id as _endpoint

        return _endpoint.sync_detailed(client=self._client("users"), group_id=group_id)

    def delete_group_logo(self, group_id: str):
        "Delete group logo image (DELETE /v1/groups/{group_id}/logo/)"
        from .users.api.groups import delete_groups_by_group_id_logo as _endpoint

        return _endpoint.sync_detailed(client=self._client("users"), group_id=group_id)

    def delete_group_user(self, group_id: str, user_id: str):
        "Delete a user from group (DELETE /v1/groups/{group_id}/users/{user_id}/)"
        from .users.api.groups import (
            delete_groups_by_group_id_users_by_user_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("users"), group_id=group_id, user_id=user_id
        )

    def delete_groups_mappings_by_name(self, name: str):
        "Delete group mapping by name (DELETE /v1/groups/mappings/{name}/)"
        from .users.api.groups import delete_groups_mappings_by_name as _endpoint

        return _endpoint.sync_detailed(client=self._client("users"), name=name)

    def delete_role_groups_by_group(self, group_id: str):
        "Delete a particular role group by id (DELETE /v1/role_groups/{group_id}/)"
        from .users.api.role_groups import delete_role_groups_by_group_id as _endpoint

        return _endpoint.sync_detailed(client=self._client("users"), group_id=group_id)

    def delete_role_groups_user_by_group(self, group_id: str, user_id: str):
        "Delete a user from role group (DELETE /v1/role_groups/{group_id}/users/{user_id}/)"
        from .users.api.role_groups import (
            delete_role_groups_by_group_id_users_by_user_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("users"), group_id=group_id, user_id=user_id
        )

    def delete_team_users(self, team_id: str):
        "Delete a particular team by id (DELETE /v1/teams/{team_id}/)"
        from .users.api.teams import delete_teams_by_team_id as _endpoint

        return _endpoint.sync_detailed(client=self._client("users"), team_id=team_id)

    def delete_team_logo(self, team_id: str):
        "Delete team logo image (DELETE /v1/teams/{team_id}/logo/)"
        from .users.api.teams import delete_teams_by_team_id_logo as _endpoint

        return _endpoint.sync_detailed(client=self._client("users"), team_id=team_id)

    def delete_team_user(self, team_id: str, user_id: str):
        "Delete a user from team (DELETE /v1/teams/{team_id}/users/{user_id}/)"
        from .users.api.teams import (
            delete_teams_by_team_id_users_by_user_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("users"), team_id=team_id, user_id=user_id
        )

    def delete_user(self, user_id: str):
        "Delete a particular user by id (DELETE /v1/users/{user_id}/)"
        from .users.api.users import delete_users_by_user_id as _endpoint

        return _endpoint.sync_detailed(client=self._client("users"), user_id=user_id)

    def delete_user_photo(self, user_id: str):
        "Delete a photo image of a specified user. (DELETE /v1/users/{user_id}/photo/)"
        from .users.api.users import delete_users_by_user_id_photo as _endpoint

        return _endpoint.sync_detailed(client=self._client("users"), user_id=user_id)

    def delete_user_saml(self, user_id: str):
        "Remove a user's SAML IdP setting (DELETE /v1/users/{user_id}/saml/)"
        from .users.api.users import delete_users_by_user_id_saml as _endpoint

        return _endpoint.sync_detailed(client=self._client("users"), user_id=user_id)

    def delete_users_current_photo(self):
        "Delete current user photo image. (DELETE /v1/users/current/photo/)"
        from .users.api.users import delete_users_current_photo as _endpoint

        return _endpoint.sync_detailed(client=self._client("users"))

    def delete_users_current_totp_configure(self, *, body):
        "Delete totp confguration (DELETE /v1/users/current/totp/configure/)"
        from .users.api.users import delete_users_current_totp_configure as _endpoint

        return _endpoint.sync_detailed(client=self._client("users"), body=body)

    def delete_users_invite_purge(self):
        "Delete all invite links that were generated. (DELETE /v1/users/invite/purge/)"
        from .users.api.users import delete_users_invite_purge as _endpoint

        return _endpoint.sync_detailed(client=self._client("users"))

    def delete_users_partner_domain_access(self, *, body):
        "Remove customer domain access from all users in a partner domain. (DELETE /v1/users/partner_domain_access/)"
        from .users.api.users import delete_users_partner_domain_access as _endpoint

        return _endpoint.sync_detailed(client=self._client("users"), body=body)

    def get_groups(
        self,
        *,
        page=UNSET,
        per_page=UNSET,
        sort=UNSET,
        alias=UNSET,
        description=UNSET,
        name=UNSET,
        roles=UNSET,
        date_created=UNSET,
        date_modified=UNSET,
        query=UNSET,
        ids=UNSET,
    ):
        "List groups with details (GET /v1/groups/)"
        from .users.api.groups import get_groups as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("users"),
            page=page,
            per_page=per_page,
            sort=sort,
            alias=alias,
            description=description,
            name=name,
            roles=roles,
            date_created=date_created,
            date_modified=date_modified,
            query=query,
            ids=ids,
        )

    def get_groups_all_basic(self, *, page=UNSET, per_page=UNSET, ids=UNSET):
        "List all groups without details (GET /v1/groups/all/basic/)"
        from .users.api.groups import get_groups_all_basic as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("users"), page=page, per_page=per_page, ids=ids
        )

    def get_groups_basic(
        self,
        *,
        page=UNSET,
        per_page=UNSET,
        sort=UNSET,
        alias=UNSET,
        description=UNSET,
        name=UNSET,
        roles=UNSET,
        date_created=UNSET,
        date_modified=UNSET,
        query=UNSET,
        ids=UNSET,
    ):
        "List untyped groups without details (GET /v1/groups/basic/)"
        from .users.api.groups import get_groups_basic as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("users"),
            page=page,
            per_page=per_page,
            sort=sort,
            alias=alias,
            description=description,
            name=name,
            roles=roles,
            date_created=date_created,
            date_modified=date_modified,
            query=query,
            ids=ids,
        )

    def get_group_users(self, group_id: str):
        "Returns a particular group by id (GET /v1/groups/{group_id}/)"
        from .users.api.groups import get_groups_by_group_id as _endpoint

        return _endpoint.sync_detailed(client=self._client("users"), group_id=group_id)

    def get_groups_mappings(self, *, per_page=UNSET, last_id=UNSET):
        "Get all group mappings (GET /v1/groups/mappings/)"
        from .users.api.groups import get_groups_mappings as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("users"), per_page=per_page, last_id=last_id
        )

    def get_groups_mappings_by_name(self, name: str):
        "Get a group mapping (GET /v1/groups/mappings/{name}/)"
        from .users.api.groups import get_groups_mappings_by_name as _endpoint

        return _endpoint.sync_detailed(client=self._client("users"), name=name)

    def get_role_groups(
        self,
        *,
        page=UNSET,
        per_page=UNSET,
        sort=UNSET,
        alias=UNSET,
        description=UNSET,
        name=UNSET,
        roles=UNSET,
        date_created=UNSET,
        date_modified=UNSET,
        query=UNSET,
        ids=UNSET,
    ):
        "List role groups with details (GET /v1/role_groups/)"
        from .users.api.role_groups import get_role_groups as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("users"),
            page=page,
            per_page=per_page,
            sort=sort,
            alias=alias,
            description=description,
            name=name,
            roles=roles,
            date_created=date_created,
            date_modified=date_modified,
            query=query,
            ids=ids,
        )

    def get_role_groups_basic(
        self,
        *,
        page=UNSET,
        per_page=UNSET,
        sort=UNSET,
        alias=UNSET,
        description=UNSET,
        name=UNSET,
        roles=UNSET,
        date_created=UNSET,
        date_modified=UNSET,
        query=UNSET,
        ids=UNSET,
    ):
        "List role groups without details (GET /v1/role_groups/basic/)"
        from .users.api.role_groups import get_role_groups_basic as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("users"),
            page=page,
            per_page=per_page,
            sort=sort,
            alias=alias,
            description=description,
            name=name,
            roles=roles,
            date_created=date_created,
            date_modified=date_modified,
            query=query,
            ids=ids,
        )

    def get_role_groups_by_group(self, group_id: str):
        "Returns a particular role group by id (GET /v1/role_groups/{group_id}/)"
        from .users.api.role_groups import get_role_groups_by_group_id as _endpoint

        return _endpoint.sync_detailed(client=self._client("users"), group_id=group_id)

    def get_teams(
        self,
        *,
        page=UNSET,
        per_page=UNSET,
        sort=UNSET,
        alias=UNSET,
        description=UNSET,
        name=UNSET,
        date_created=UNSET,
        date_modified=UNSET,
        query=UNSET,
        ids=UNSET,
    ):
        "List teams with details (GET /v1/teams/)"
        from .users.api.teams import get_teams as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("users"),
            page=page,
            per_page=per_page,
            sort=sort,
            alias=alias,
            description=description,
            name=name,
            date_created=date_created,
            date_modified=date_modified,
            query=query,
            ids=ids,
        )

    def get_teams_basic(
        self,
        *,
        page=UNSET,
        per_page=UNSET,
        sort=UNSET,
        alias=UNSET,
        description=UNSET,
        name=UNSET,
        date_created=UNSET,
        date_modified=UNSET,
        query=UNSET,
        ids=UNSET,
    ):
        "List teams info without details (GET /v1/teams/basic/)"
        from .users.api.teams import get_teams_basic as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("users"),
            page=page,
            per_page=per_page,
            sort=sort,
            alias=alias,
            description=description,
            name=name,
            date_created=date_created,
            date_modified=date_modified,
            query=query,
            ids=ids,
        )

    def get_team_users(self, team_id: str):
        "Returns a particular team by id (GET /v1/teams/{team_id}/)"
        from .users.api.teams import get_teams_by_team_id as _endpoint

        return _endpoint.sync_detailed(client=self._client("users"), team_id=team_id)

    def get_users(
        self,
        *,
        page=UNSET,
        per_page=UNSET,
        sort=UNSET,
        date_created=UNSET,
        date_modified=UNSET,
        email=UNSET,
        first_name=UNSET,
        last_name=UNSET,
        groups=UNSET,
        hide_email=UNSET,
        hide_phone=UNSET,
        is_admin=UNSET,
        password_changed=UNSET,
        phone=UNSET,
        photo=UNSET,
        status=UNSET,
        query=UNSET,
        ids=UNSET,
    ):
        "List of users with details (GET /v1/users/)"
        from .users.api.users import get_users as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("users"),
            page=page,
            per_page=per_page,
            sort=sort,
            date_created=date_created,
            date_modified=date_modified,
            email=email,
            first_name=first_name,
            last_name=last_name,
            groups=groups,
            hide_email=hide_email,
            hide_phone=hide_phone,
            is_admin=is_admin,
            password_changed=password_changed,
            phone=phone,
            photo=photo,
            status=status,
            query=query,
            ids=ids,
        )

    def get_users_basic(
        self,
        *,
        page=UNSET,
        per_page=UNSET,
        sort=UNSET,
        email=UNSET,
        first_name=UNSET,
        last_name=UNSET,
        query=UNSET,
        ids=UNSET,
        emails=UNSET,
    ):
        "List of users without details (GET /v1/users/basic/)"
        from .users.api.users import get_users_basic as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("users"),
            page=page,
            per_page=per_page,
            sort=sort,
            email=email,
            first_name=first_name,
            last_name=last_name,
            query=query,
            ids=ids,
            emails=emails,
        )

    def get_user(self, user_id: str):
        "Returns a particular user by id (GET /v1/users/{user_id}/)"
        from .users.api.users import get_users_by_user_id as _endpoint

        return _endpoint.sync_detailed(client=self._client("users"), user_id=user_id)

    def get_user_roles(self, user_id: str):
        "Returns user roles by user_id (GET /v1/users/{user_id}/roles/)"
        from .users.api.users import get_users_by_user_id_roles as _endpoint

        return _endpoint.sync_detailed(client=self._client("users"), user_id=user_id)

    def get_user_roles_by_role(self, user_id: str, role: str):
        "Returns user roles by user_id (GET /v1/users/{user_id}/roles/{role}/)"
        from .users.api.users import get_users_by_user_id_roles_by_role as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("users"), user_id=user_id, role=role
        )

    def get_users_current(self):
        "Returns current user (GET /v1/users/current/)"
        from .users.api.users import get_users_current as _endpoint

        return _endpoint.sync_detailed(client=self._client("users"))

    def get_users_current_otp_configure(self):
        "Get current otp settings. (GET /v1/users/current/otp/configure/)"
        from .users.api.users import get_users_current_otp_configure as _endpoint

        return _endpoint.sync_detailed(client=self._client("users"))

    def get_users_current_roles(self):
        "Returns current user roles (GET /v1/users/current/roles/)"
        from .users.api.users import get_users_current_roles as _endpoint

        return _endpoint.sync_detailed(client=self._client("users"))

    def patch_group_users(self, group_id: str, *, body):
        "Update group (PATCH /v1/groups/{group_id}/)"
        from .users.api.groups import patch_groups_by_group_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("users"), group_id=group_id, body=body
        )

    def patch_role_groups_by_group(self, group_id: str, *, body):
        "Update role group (PATCH /v1/role_groups/{group_id}/)"
        from .users.api.role_groups import patch_role_groups_by_group_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("users"), group_id=group_id, body=body
        )

    def patch_team_users(self, team_id: str, *, body):
        "Update team (PATCH /v1/teams/{team_id}/)"
        from .users.api.teams import patch_teams_by_team_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("users"), team_id=team_id, body=body
        )

    def patch_user(self, user_id: str, *, body):
        "Update user (PATCH /v1/users/{user_id}/)"
        from .users.api.users import patch_users_by_user_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("users"), user_id=user_id, body=body
        )

    def patch_users_current(self, *, body):
        "Update user (PATCH /v1/users/current/)"
        from .users.api.users import patch_users_current as _endpoint

        return _endpoint.sync_detailed(client=self._client("users"), body=body)

    def post_groups(self, *, body):
        "Create a new group (POST /v1/groups/)"
        from .users.api.groups import post_groups as _endpoint

        return _endpoint.sync_detailed(client=self._client("users"), body=body)

    def post_group_logo(self, group_id: str, *, body):
        "Upload group logo image (POST /v1/groups/{group_id}/logo/)"
        from .users.api.groups import post_groups_by_group_id_logo as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("users"), group_id=group_id, body=body
        )

    def post_group_reindex(self, group_id: str, *, body):
        "Reindex a particular group by id (POST /v1/groups/{group_id}/reindex/)"
        from .users.api.groups import post_groups_by_group_id_reindex as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("users"), group_id=group_id, body=body
        )

    def post_group_user(self, group_id: str, user_id: str):
        "Add user into a group (POST /v1/groups/{group_id}/users/{user_id}/)"
        from .users.api.groups import (
            post_groups_by_group_id_users_by_user_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("users"), group_id=group_id, user_id=user_id
        )

    def post_groups_mappings(self, *, body):
        "Create a new group mapping (POST /v1/groups/mappings/)"
        from .users.api.groups import post_groups_mappings as _endpoint

        return _endpoint.sync_detailed(client=self._client("users"), body=body)

    def post_role_groups(self, *, body):
        "Create a new role group (POST /v1/role_groups/)"
        from .users.api.role_groups import post_role_groups as _endpoint

        return _endpoint.sync_detailed(client=self._client("users"), body=body)

    def post_role_groups_user_by_group(self, group_id: str, user_id: str):
        "Add user into a role group (POST /v1/role_groups/{group_id}/users/{user_id}/)"
        from .users.api.role_groups import (
            post_role_groups_by_group_id_users_by_user_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("users"), group_id=group_id, user_id=user_id
        )

    def post_teams(self, *, body):
        "Create a new team (POST /v1/teams/)"
        from .users.api.teams import post_teams as _endpoint

        return _endpoint.sync_detailed(client=self._client("users"), body=body)

    def post_team_logo(self, team_id: str, *, body):
        "Upload team logo image (POST /v1/teams/{team_id}/logo/)"
        from .users.api.teams import post_teams_by_team_id_logo as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("users"), team_id=team_id, body=body
        )

    def post_team_user(self, team_id: str, user_id: str):
        "Add user into a team (POST /v1/teams/{team_id}/users/{user_id}/)"
        from .users.api.teams import post_teams_by_team_id_users_by_user_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("users"), team_id=team_id, user_id=user_id
        )

    def post_users(self, *, body):
        "Create a new user (POST /v1/users/)"
        from .users.api.users import post_users as _endpoint

        return _endpoint.sync_detailed(client=self._client("users"), body=body)

    def post_user_photo(self, user_id: str, *, body):
        "Upload user photo image. (POST /v1/users/{user_id}/photo/)"
        from .users.api.users import post_users_by_user_id_photo as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("users"), user_id=user_id, body=body
        )

    def post_user_reindex(self, user_id: str, *, body):
        "Reindex a particular user by id (POST /v1/users/{user_id}/reindex/)"
        from .users.api.users import post_users_by_user_id_reindex as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("users"), user_id=user_id, body=body
        )

    def post_users_current_otp_configure(self, *, body):
        "Configure OTP settings. (POST /v1/users/current/otp/configure/)"
        from .users.api.users import post_users_current_otp_configure as _endpoint

        return _endpoint.sync_detailed(client=self._client("users"), body=body)

    def post_users_current_photo(self, *, body):
        "Upload current user photo image. (POST /v1/users/current/photo/)"
        from .users.api.users import post_users_current_photo as _endpoint

        return _endpoint.sync_detailed(client=self._client("users"), body=body)

    def post_users_current_totp_configure(self, *, body=UNSET):
        "Setup totp (POST /v1/users/current/totp/configure/)"
        from .users.api.users import post_users_current_totp_configure as _endpoint

        return _endpoint.sync_detailed(client=self._client("users"), body=body)

    def post_users_current_totp_validate_configuration(self, *, body):
        "Validate totp configuration (POST /v1/users/current/totp/validate_configuration/)"
        from .users.api.users import (
            post_users_current_totp_validate_configuration as _endpoint,
        )

        return _endpoint.sync_detailed(client=self._client("users"), body=body)

    def post_users_invite_register(self, *, body):
        "Register a new user using an invite link token (POST /v1/users/invite/register/)"
        from .users.api.users import post_users_invite_register as _endpoint

        return _endpoint.sync_detailed(client=self._client("users", ()), body=body)

    def post_users_invite_token_request(self, *, body):
        "Request an invite link for user invitation. (POST /v1/users/invite/token/request/)"
        from .users.api.users import post_users_invite_token_request as _endpoint

        return _endpoint.sync_detailed(client=self._client("users"), body=body)

    def post_users_invite_validate(self, *, hash_):
        "Validate an invite link for user invitation. (POST /v1/users/invite/validate/)"
        from .users.api.users import post_users_invite_validate as _endpoint

        return _endpoint.sync_detailed(client=self._client("users", ()), hash_=hash_)

    def post_users_partner_domain_access(self, *, body):
        "Grant all owner users in a partner domain access to a customer domain. (POST /v1/users/partner_domain_access/)"
        from .users.api.users import post_users_partner_domain_access as _endpoint

        return _endpoint.sync_detailed(client=self._client("users"), body=body)

    def put_group_users(self, group_id: str, *, body):
        "Update group (PUT /v1/groups/{group_id}/)"
        from .users.api.groups import put_groups_by_group_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("users"), group_id=group_id, body=body
        )

    def put_role_groups_by_group(self, group_id: str, *, body):
        "Update role group (PUT /v1/role_groups/{group_id}/)"
        from .users.api.role_groups import put_role_groups_by_group_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("users"), group_id=group_id, body=body
        )

    def put_team_users(self, team_id: str, *, body):
        "Update team (PUT /v1/teams/{team_id}/)"
        from .users.api.teams import put_teams_by_team_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("users"), team_id=team_id, body=body
        )

    def put_user(self, user_id: str, *, body):
        "Update user (PUT /v1/users/{user_id}/)"
        from .users.api.users import put_users_by_user_id as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("users"), user_id=user_id, body=body
        )

    def put_user_saml(self, user_id: str, *, body):
        "Update a user's SAML IdP settings (PUT /v1/users/{user_id}/saml/)"
        from .users.api.users import put_users_by_user_id_saml as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("users"), user_id=user_id, body=body
        )

    def put_users_current(self, *, body):
        "Update user (PUT /v1/users/current/)"
        from .users.api.users import put_users_current as _endpoint

        return _endpoint.sync_detailed(client=self._client("users"), body=body)

    def put_users_current_otp_configure(self, *, body):
        "Configure OTP settings. (PUT /v1/users/current/otp/configure/)"
        from .users.api.users import put_users_current_otp_configure as _endpoint

        return _endpoint.sync_detailed(client=self._client("users"), body=body)

    def delete_object_subscriptions_all(self, object_type: str, object_id: str):
        "Delete all user subscriptions for a specific object_type and object_id (DELETE /v1/{object_type}/{object_id}/subscriptions/all/)"
        from .usersnotifications.api.object_type import (
            delete_by_object_type_by_object_id_subscriptions_all as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("users-notifications"),
            object_type=object_type,
            object_id=object_id,
        )

    def delete_notification(self, notification_id: str):
        "Delete a particular notification by id (DELETE /v1/notifications/{notification_id}/)"
        from .usersnotifications.api.notifications import (
            delete_notifications_by_notification_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("users-notifications"), notification_id=notification_id
        )

    def delete_subscription(self, subscription_id: str):
        "Delete a particular subscription by id (DELETE /v1/subscriptions/{subscription_id}/)"
        from .usersnotifications.api.subscriptions import (
            delete_subscriptions_by_subscription_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("users-notifications"), subscription_id=subscription_id
        )

    def delete_user_device_tokens(self, user_id: str):
        "Unregister all device tokens for a user (e.g., on account deletion) (DELETE /v1/users/{user_id}/device_tokens/)"
        from .usersnotifications.api.users import (
            delete_users_by_user_id_device_tokens as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("users-notifications"), user_id=user_id
        )

    def delete_user_device_tokens_by_device_token(
        self, user_id: str, device_token: str
    ):
        "Unregister a device token (DELETE /v1/users/{user_id}/device_tokens/{device_token}/)"
        from .usersnotifications.api.users import (
            delete_users_by_user_id_device_tokens_by_device_token as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("users-notifications"),
            user_id=user_id,
            device_token=device_token,
        )

    def get_object_subscriptions(self, object_type: str, object_id: str):
        "Returns user subscriptions for a specific object_type and object_id (GET /v1/{object_type}/{object_id}/subscriptions/)"
        from .usersnotifications.api.object_type import (
            get_by_object_type_by_object_id_subscriptions as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("users-notifications"),
            object_type=object_type,
            object_id=object_id,
        )

    def get_notification_settings(self, *, per_page=UNSET, last_id=UNSET):
        "Returns a particular notification_setting by id (GET /v1/notification_settings/)"
        from .usersnotifications.api.notification_settings import (
            get_notification_settings as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("users-notifications"),
            per_page=per_page,
            last_id=last_id,
        )

    def get_notification_settings_object_by_sub_object_type_by_event_type_by_protocol(
        self, object_type: str, sub_object_type: str, event_type: str, protocol: str
    ):
        "Returns a particular notification_setting by id (GET /v1/notification_settings/{object_type}/{sub_object_type}/{event_type}/{protocol}/)"
        from .usersnotifications.api.notification_settings import (
            get_notification_settings_by_object_type_by_sub_object_type_by_event_type_by_protocol as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("users-notifications"),
            object_type=object_type,
            sub_object_type=sub_object_type,
            event_type=event_type,
            protocol=protocol,
        )

    def get_notifications(self, *, per_page=UNSET, last_id=UNSET):
        "Returns a list of notifications (GET /v1/notifications/)"
        from .usersnotifications.api.notifications import get_notifications as _endpoint

        return _endpoint.sync_detailed(
            client=self._client("users-notifications"),
            per_page=per_page,
            last_id=last_id,
        )

    def get_notification(self, notification_id: str):
        "Returns a particular notification by id (GET /v1/notifications/{notification_id}/)"
        from .usersnotifications.api.notifications import (
            get_notifications_by_notification_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("users-notifications"), notification_id=notification_id
        )

    def get_subscriptions(self):
        "Returns all user subscriptions (GET /v1/subscriptions/)"
        from .usersnotifications.api.subscriptions import get_subscriptions as _endpoint

        return _endpoint.sync_detailed(client=self._client("users-notifications"))

    def get_subscription(self, subscription_id: str):
        "Returns a particular subscription by id (GET /v1/subscriptions/{subscription_id}/)"
        from .usersnotifications.api.subscriptions import (
            get_subscriptions_by_subscription_id as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("users-notifications"), subscription_id=subscription_id
        )

    def get_user_device_tokens(self, user_id: str, *, per_page=UNSET):
        "Returns a list of device tokens for a user (GET /v1/users/{user_id}/device_tokens/)"
        from .usersnotifications.api.users import (
            get_users_by_user_id_device_tokens as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("users-notifications"),
            user_id=user_id,
            per_page=per_page,
        )

    def get_user_device_tokens_by_device_token(self, user_id: str, device_token: str):
        "Returns a particular device token (GET /v1/users/{user_id}/device_tokens/{device_token}/)"
        from .usersnotifications.api.users import (
            get_users_by_user_id_device_tokens_by_device_token as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("users-notifications"),
            user_id=user_id,
            device_token=device_token,
        )

    def patch_user_device_tokens_by_device_token(
        self, user_id: str, device_token: str, *, body
    ):
        "Update device token metadata (PATCH /v1/users/{user_id}/device_tokens/{device_token}/)"
        from .usersnotifications.api.users import (
            patch_users_by_user_id_device_tokens_by_device_token as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("users-notifications"),
            user_id=user_id,
            device_token=device_token,
            body=body,
        )

    def post_device_tokens(self, *, body):
        "Register a new device token for push notifications (POST /v1/device_tokens/)"
        from .usersnotifications.api.device_tokens import (
            post_device_tokens as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("users-notifications"), body=body
        )

    def post_notifications(self, *, body):
        "Create a new notification (POST /v1/notifications/)"
        from .usersnotifications.api.notifications import (
            post_notifications as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("users-notifications"), body=body
        )

    def post_notifications_system(self, *, body):
        "Create a new system notification (POST /v1/notifications/system/)"
        from .usersnotifications.api.notifications import (
            post_notifications_system as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("users-notifications"), body=body
        )

    def post_subscriptions(self, *, body):
        "Create a new subscription (POST /v1/subscriptions/)"
        from .usersnotifications.api.subscriptions import (
            post_subscriptions as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("users-notifications"), body=body
        )

    def post_user_device_tokens(self, user_id: str, *, body):
        "Register a new device token for push notifications (POST /v1/users/{user_id}/device_tokens/)"
        from .usersnotifications.api.users import (
            post_users_by_user_id_device_tokens as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("users-notifications"), user_id=user_id, body=body
        )

    def put_notification_settings_object_by_sub_object_type_by_event_type_by_protocol(
        self,
        object_type: str,
        sub_object_type: str,
        event_type: str,
        protocol: str,
        *,
        body,
    ):
        "Create a new notification_setting (PUT /v1/notification_settings/{object_type}/{sub_object_type}/{event_type}/{protocol}/)"
        from .usersnotifications.api.notification_settings import (
            put_notification_settings_by_object_type_by_sub_object_type_by_event_type_by_protocol as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("users-notifications"),
            object_type=object_type,
            sub_object_type=sub_object_type,
            event_type=event_type,
            protocol=protocol,
            body=body,
        )

    def put_notifications_all_read(self):
        "Update notification (PUT /v1/notifications/all/read/)"
        from .usersnotifications.api.notifications import (
            put_notifications_all_read as _endpoint,
        )

        return _endpoint.sync_detailed(client=self._client("users-notifications"))

    def put_notification_read(self, notification_id: str):
        "Mark a particular notification as read (PUT /v1/notifications/{notification_id}/read/)"
        from .usersnotifications.api.notifications import (
            put_notifications_by_notification_id_read as _endpoint,
        )

        return _endpoint.sync_detailed(
            client=self._client("users-notifications"), notification_id=notification_id
        )
