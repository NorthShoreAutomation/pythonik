# pythonik/tests/test_acls.py
import uuid

import pytest
import requests_mock

from pythonik.client import PythonikClient
from pythonik.models.acls import (
    ACLTemplateSchema,
    CheckBulkACLsSchema,
)
from pythonik.specs.acls import AclsSpec


def test_apply_template_permissions():
    """Test applying template permissions to an object."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        template_id = str(uuid.uuid4())
        object_type = "assets"
        object_key = str(uuid.uuid4())

        # Mock the API endpoint
        mock_address = AclsSpec.gen_url(
            f"acl/templates/{template_id}/{object_type}/{object_key}/")
        m.post(mock_address, status_code=204)

        # Create client and make request
        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)
        response = client.acls().apply_template_permissions(
            template_id=template_id,
            object_type=object_type,
            object_key=object_key,
            ignore_reindexing=True,
            restrict_acls_collection_id="collection-uuid",
        )

        # Verify the response and request
        assert response.response.status_code == 204
        assert m.called
        assert m.last_request.method == "POST"

        # Verify query parameters - lowercase comparison for boolean values
        assert "ignore_reindexing=" in m.last_request.url
        assert ("restrict_acls_collection_id=collection-uuid"
                in m.last_request.url)


def test_apply_group_permissions():
    """Test applying group permissions to an object."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        group_id = str(uuid.uuid4())
        object_type = "assets"
        object_key = str(uuid.uuid4())
        permissions = ["read", "write"]

        # Expected response data
        response_data = {
            "group_id": group_id,
            "object_key": object_key,
            "object_type": object_type,
            "permissions": permissions,
            "date_created": "2025-05-20T09:50:09Z",
            "date_modified": "2025-05-20T09:50:09Z",
        }

        # Mock the API endpoint
        mock_address = AclsSpec.gen_url(
            f"groups/{group_id}/acl/{object_type}/{object_key}/")
        m.put(mock_address, json=response_data)

        # Create client and make request
        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)
        response = client.acls().apply_group_permissions(
            group_id=group_id,
            object_type=object_type,
            object_key=object_key,
            permissions=permissions,
        )

        # Verify the response and request
        assert response.response.ok
        assert m.called
        assert m.last_request.method == "PUT"

        # Verify request body
        request_json = m.last_request.json()
        assert request_json["permissions"] == permissions


def test_apply_group_permissions_invalid_permission():
    """Test applying group permissions with invalid permission raises ValueError."""
    app_id = str(uuid.uuid4())
    auth_token = str(uuid.uuid4())
    group_id = str(uuid.uuid4())
    object_type = "assets"
    object_key = str(uuid.uuid4())
    permissions = ["invalid_permission"]

    # Create client
    client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)

    # Make request with invalid permissions and verify it raises ValueError
    with pytest.raises(ValueError) as exc_info:
        client.acls().apply_group_permissions(
            group_id=group_id,
            object_type=object_type,
            object_key=object_key,
            permissions=permissions,
        )

    # Check error message contains valid permissions
    assert "Value must be one of" in str(exc_info.value)
    assert "read" in str(exc_info.value)
    assert "write" in str(exc_info.value)
    assert "delete" in str(exc_info.value)
    assert "change-acl" in str(exc_info.value)


def test_fetch_object_permissions():
    """Test fetching permissions for an object."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        object_type = "assets"
        object_key = str(uuid.uuid4())

        # Expected response data
        response_data = {
            "users_acl": [{
                "user_id": str(uuid.uuid4()),
                "permissions": ["read", "write"]
            }],
            "groups_acl": [{
                "group_id": str(uuid.uuid4()),
                "permissions": ["read"]
            }],
            "propagating_users_acl": [],
            "propagating_groups_acl": [],
            "inherited_users_acl": [],
            "inherited_groups_acl": [],
        }

        # Mock the API endpoint
        mock_address = AclsSpec.gen_url(f"acl/{object_type}/{object_key}/")
        m.get(mock_address, json=response_data)

        # Create client and make request
        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)
        response = client.acls().list_object_permissions(
            object_type=object_type,
            object_key=object_key,
        )

        # Verify the response and request
        assert response.response.ok
        assert m.called
        assert m.last_request.method == "GET"

        # Verify response data
        assert len(response.data.users_acl) == 1
        assert len(response.data.groups_acl) == 1
        assert response.data.users_acl[0].permissions == ["read", "write"]
        assert response.data.groups_acl[0].permissions == ["read"]


def test_fetch_acl_templates():
    """Test fetching ACL templates."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        template_id = str(uuid.uuid4())

        # Expected response data
        response_data = {
            "objects": [{
                "id": template_id,
                "name": "Test Template",
                "date_created": "2025-05-20T09:50:09Z",
                "date_modified": "2025-05-20T09:50:09Z",
            }]
        }

        # Mock the API endpoint
        mock_address = AclsSpec.gen_url("acl/templates/")
        m.get(mock_address, json=response_data)

        # Create client and make request
        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)
        response = client.acls().list_acl_templates()

        # Verify the response and request
        assert response.response.ok
        assert m.called
        assert m.last_request.method == "GET"

        # Verify response data
        assert len(response.data.objects) == 1
        assert str(response.data.objects[0].id) == template_id
        assert response.data.objects[0].name == "Test Template"


def test_create_acl_template():
    """Test creating an ACL template."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        template_id = str(uuid.uuid4())
        template_name = "New Template"

        # Expected response data
        response_data = {
            "id": template_id,
            "name": template_name,
            "date_created": "2025-05-20T09:50:09Z",
            "date_modified": "2025-05-20T09:50:09Z",
        }

        # Mock the API endpoint
        mock_address = AclsSpec.gen_url("acl/templates/")
        m.post(mock_address, json=response_data)

        # Create client and make request
        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)
        response = client.acls().create_acl_template(name=template_name)

        # Verify the response and request
        assert response.response.ok
        assert m.called
        assert m.last_request.method == "POST"

        # Verify request body
        request_json = m.last_request.json()
        assert request_json["name"] == template_name

        # Verify response data
        assert str(response.data.id) == template_id
        assert response.data.name == template_name


def test_get_acl_template():
    """Test getting an ACL template."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        template_id = str(uuid.uuid4())
        template_name = "Test Template"

        # Expected response data
        response_data = {
            "id": template_id,
            "name": template_name,
            "date_created": "2025-05-20T09:50:09Z",
            "date_modified": "2025-05-20T09:50:09Z",
        }

        # Mock the API endpoint
        mock_address = AclsSpec.gen_url(f"acl/templates/{template_id}/")
        m.get(mock_address, json=response_data)

        # Create client and make request
        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)
        response = client.acls().get_acl_template(template_id=template_id)

        # Verify the response and request
        assert response.response.ok
        assert m.called
        assert m.last_request.method == "GET"

        # Verify response data
        assert str(response.data.id) == template_id
        assert response.data.name == template_name


def test_update_acl_template():
    """Test updating an ACL template."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        template_id = str(uuid.uuid4())
        template_name = "Updated Template"

        # Create template data
        template_data = ACLTemplateSchema(name=template_name)

        # Expected response data
        response_data = {
            "id": template_id,
            "name": template_name,
            "date_created": "2025-05-20T09:50:09Z",
            "date_modified": "2025-05-20T09:50:09Z",
        }

        # Mock the API endpoint
        mock_address = AclsSpec.gen_url(f"acl/templates/{template_id}/")
        m.put(mock_address, json=response_data)

        # Create client and make request
        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)
        response = client.acls().update_acl_template(
            template_id=template_id,
            template=template_data,
        )

        # Verify the response and request
        assert response.response.ok
        assert m.called
        assert m.last_request.method == "PUT"

        # Verify request body
        request_json = m.last_request.json()
        assert request_json["name"] == template_name

        # Verify response data
        assert str(response.data.id) == template_id
        assert response.data.name == template_name


def test_partial_update_acl_template():
    """Test partially updating an ACL template."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        template_id = str(uuid.uuid4())
        template_name = "Partially Updated Template"

        # Create template data
        template_data = {"name": template_name}  # Using dict instead of model

        # Expected response data
        response_data = {
            "id": template_id,
            "name": template_name,
            "date_created": "2025-05-20T09:50:09Z",
            "date_modified": "2025-05-20T09:50:09Z",
        }

        # Mock the API endpoint
        mock_address = AclsSpec.gen_url(f"acl/templates/{template_id}/")
        m.patch(mock_address, json=response_data)

        # Create client and make request
        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)
        response = client.acls().partial_update_acl_template(
            template_id=template_id,
            template=template_data,
        )

        # Verify the response and request
        assert response.response.ok
        assert m.called
        assert m.last_request.method == "PATCH"

        # Verify request body
        request_json = m.last_request.json()
        assert request_json["name"] == template_name

        # Verify response data
        assert str(response.data.id) == template_id
        assert response.data.name == template_name


def test_delete_acl_template():
    """Test deleting an ACL template."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        template_id = str(uuid.uuid4())

        # Mock the API endpoint
        mock_address = AclsSpec.gen_url(f"acl/templates/{template_id}/")
        m.delete(mock_address, status_code=204)

        # Create client and make request
        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)
        response = client.acls().delete_acl_template(template_id=template_id)

        # Verify the response and request
        assert response.response.status_code == 204
        assert m.called
        assert m.last_request.method == "DELETE"


def test_check_objects_permission():
    """Test checking permissions for multiple objects."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        object_key1 = str(uuid.uuid4())
        object_key2 = str(uuid.uuid4())

        # Create request data
        check_data = CheckBulkACLsSchema(
            objects=[{
                "object_keys": [object_key1, object_key2],
                "object_type": "assets",
                "permissions": ["read", "write"],
            }])

        # Expected response data
        response_data = {
            "access_granted": [object_key1],
            "access_denied": [object_key2],
        }

        # Mock the API endpoint
        mock_address = AclsSpec.gen_url("acl/")
        m.post(mock_address, json=response_data)

        # Create client and make request
        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)
        response = client.acls().check_objects_permission(objects=check_data)

        # Verify the response and request
        assert response.response.ok
        assert m.called
        assert m.last_request.method == "POST"

        # Verify request body
        request_json = m.last_request.json()
        assert "objects" in request_json
        assert len(request_json["objects"]) == 1
        assert object_key1 in request_json["objects"][0]["object_keys"]
        assert object_key2 in request_json["objects"][0]["object_keys"]

        # Verify response data
        assert response.data.access_granted == [object_key1]
        assert response.data.access_denied == [object_key2]


def test_check_object_permission():
    """Test checking permission for a single object."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        object_type = "assets"
        object_key = str(uuid.uuid4())
        permission = "read"

        # Mock the API endpoint
        mock_address = AclsSpec.gen_url(
            f"acl/{object_type}/{object_key}/{permission}/")
        m.get(mock_address, status_code=204)

        # Create client and make request
        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)
        response = client.acls().check_object_permission(
            object_type=object_type,
            object_key=object_key,
            permission=permission,
        )

        # Verify the response and request
        assert response.response.status_code == 204
        assert m.called
        assert m.last_request.method == "GET"


def test_get_combined_permissions():
    """Test getting combined permissions for an object."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        object_type = "assets"
        object_key = str(uuid.uuid4())

        # Expected response data
        response_data = {"permissions": ["read", "write", "delete"]}

        # Mock the API endpoint
        mock_address = AclsSpec.gen_url(
            f"acl/{object_type}/{object_key}/permissions/")
        m.get(mock_address, json=response_data)

        # Create client and make request
        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)
        response = client.acls().get_combined_permissions(
            object_type=object_type,
            object_key=object_key,
        )

        # Verify the response and request
        assert response.response.ok
        assert m.called
        assert m.last_request.method == "GET"

        # Verify response data
        assert response.data.permissions == ["read", "write", "delete"]


def test_check_objects_have_permission():
    """Test checking if objects have a specific permission."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        object_type = "assets"
        permission = "read"
        object_key1 = str(uuid.uuid4())
        object_key2 = str(uuid.uuid4())

        # Create request data
        object_keys = {"object_keys": [object_key1, object_key2]}

        # Expected response data
        response_data = {
            "access_granted": [object_key1],
            "access_denied": [object_key2],
        }

        # Mock the API endpoint
        mock_address = AclsSpec.gen_url(f"acl/{object_type}/{permission}/")
        m.post(mock_address, json=response_data)

        # Create client and make request
        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)
        response = client.acls().check_objects_have_permission(
            object_type=object_type,
            permission=permission,
            object_keys=object_keys,
        )

        # Verify the response and request
        assert response.response.ok
        assert m.called
        assert m.last_request.method == "POST"

        # Verify request body
        request_json = m.last_request.json()
        assert "object_keys" in request_json
        assert object_key1 in request_json["object_keys"]
        assert object_key2 in request_json["object_keys"]

        # Verify response data
        assert response.data.access_granted == [object_key1]
        assert response.data.access_denied == [object_key2]


def test_create_acls():
    """Test creating ACLs for multiple objects."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        object_type = "assets"
        object_key1 = str(uuid.uuid4())
        object_key2 = str(uuid.uuid4())
        user_id = str(uuid.uuid4())
        group_id = str(uuid.uuid4())

        # Create request data with all UUIDs as strings
        acls_data = {
            "object_keys": [str(object_key1),
                            str(object_key2)],
            "object_type": object_type,
            "permissions": ["read", "write"],
            "user_ids": [str(user_id)],
            "group_ids": [str(group_id)],
            "mode": "APPEND",
        }

        # Expected response data
        response_data = {
            "updated_object_keys": [str(object_key1),
                                    str(object_key2)]
        }

        # Mock the API endpoint
        mock_address = AclsSpec.gen_url(f"acl/{object_type}/")
        m.put(mock_address, json=response_data)

        # Create client and make request
        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)
        response = client.acls().create_acls(
            object_type=object_type,
            acls=acls_data,
        )

        # Verify the response and request
        assert response.response.ok
        assert m.called
        assert m.last_request.method == "PUT"

        # Verify request body
        request_json = m.last_request.json()
        assert str(object_key1) in request_json["object_keys"]
        assert str(object_key2) in request_json["object_keys"]
        assert request_json["permissions"] == ["read", "write"]
        assert str(user_id) in request_json["user_ids"]
        assert str(group_id) in request_json["group_ids"]
        assert request_json["mode"] == "APPEND"

        # Verify response data
        assert response.data.updated_object_keys == [
            str(object_key1),
            str(object_key2),
        ]


def test_create_bulk_acls():
    """Test creating ACLs for multiple objects with multiple permissions."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        object_type = "assets"
        object_key1 = str(uuid.uuid4())
        object_key2 = str(uuid.uuid4())
        user_id = str(uuid.uuid4())

        # Create request data
        acls_data = {
            "objects": [
                {
                    "object_keys": [str(object_key1)],
                    "permissions": ["read", "write"],
                    "user_ids": [str(user_id)],
                    "mode": "APPEND",
                },
                {
                    "object_keys": [str(object_key2)],
                    "permissions": ["read"],
                    "user_ids": [str(user_id)],
                    "mode": "OVERWRITE",
                },
            ]
        }

        # Mock the API endpoint
        mock_address = AclsSpec.gen_url(f"acl/{object_type}/bulk/")
        m.put(mock_address, status_code=204)

        # Create client and make request
        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)
        response = client.acls().create_bulk_acls(
            object_type=object_type,
            acls=acls_data,
        )

        # Verify the response and request
        assert response.response.status_code == 204
        assert m.called
        assert m.last_request.method == "PUT"

        # Verify request body
        request_json = m.last_request.json()
        assert "objects" in request_json
        assert len(request_json["objects"]) == 2
        assert str(object_key1) in request_json["objects"][0]["object_keys"]
        assert request_json["objects"][0]["permissions"] == ["read", "write"]
        assert str(object_key2) in request_json["objects"][1]["object_keys"]
        assert request_json["objects"][1]["permissions"] == ["read"]


def test_create_acls_for_content():
    """Test creating ACLs for content of multiple objects."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        object_type = "collections"
        object_id1 = str(uuid.uuid4())
        object_id2 = str(uuid.uuid4())
        user_id = str(uuid.uuid4())
        group_id = str(uuid.uuid4())

        # Create request data
        acls_data = {
            "object_ids": [str(object_id1), str(object_id2)],
            "permissions": ["read", "write"],
            "user_ids": [str(user_id)],
            "group_ids": [str(group_id)],
            "include_assets": True,
            "include_collections": True,
            "mode": "APPEND",
        }

        # Mock the API endpoint
        mock_address = AclsSpec.gen_url(f"acl/{object_type}/content/")
        m.put(mock_address, status_code=204)

        # Create client and make request
        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)
        response = client.acls().create_acls_for_content(
            object_type=object_type,
            acls=acls_data,
        )

        # Verify the response and request
        assert response.response.status_code == 204
        assert m.called
        assert m.last_request.method == "PUT"

        # Verify request body
        request_json = m.last_request.json()
        assert str(object_id1) in request_json["object_ids"]
        assert str(object_id2) in request_json["object_ids"]
        assert request_json["permissions"] == ["read", "write"]
        assert str(user_id) in request_json["user_ids"]
        assert str(group_id) in request_json["group_ids"]
        assert request_json["include_assets"] is True
        assert request_json["include_collections"] is True
        assert request_json["mode"] == "APPEND"


def test_delete_acls():
    """Test deleting ACLs for multiple objects."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        object_type = "assets"
        object_key1 = str(uuid.uuid4())
        object_key2 = str(uuid.uuid4())
        user_id = str(uuid.uuid4())
        group_id = str(uuid.uuid4())

        # Create request data
        acls_data = {
            "object_keys": [str(object_key1),
                            str(object_key2)],
            "object_type": object_type,
            "user_ids": [str(user_id)],
            "group_ids": [str(group_id)],
        }

        # Mock the API endpoint
        mock_address = AclsSpec.gen_url(f"acl/{object_type}/")
        m.delete(mock_address, status_code=204)

        # Create client and make request
        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)
        response = client.acls().delete_acls(
            object_type=object_type,
            acls=acls_data,
        )

        # Verify the response and request
        assert response.response.status_code == 204
        assert m.called
        assert m.last_request.method == "DELETE"

        # Verify request body
        request_json = m.last_request.json()
        assert str(object_key1) in request_json["object_keys"]
        assert str(object_key2) in request_json["object_keys"]
        assert str(user_id) in request_json["user_ids"]
        assert str(group_id) in request_json["group_ids"]


def test_delete_acls_for_content():
    """Test deleting ACLs for content of multiple objects."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        object_type = "collections"
        object_id1 = str(uuid.uuid4())
        object_id2 = str(uuid.uuid4())
        user_id = str(uuid.uuid4())
        group_id = str(uuid.uuid4())

        # Create request data
        acls_data = {
            "object_ids": [str(object_id1), str(object_id2)],
            "user_ids": [str(user_id)],
            "group_ids": [str(group_id)],
            "include_assets": True,
            "include_collections": True,
            "object_type": object_type,
        }

        # Mock the API endpoint
        mock_address = AclsSpec.gen_url(f"acl/{object_type}/content/")
        m.delete(mock_address, status_code=204)

        # Create client and make request
        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)
        response = client.acls().delete_acls_for_content(
            object_type=object_type,
            acls=acls_data,
        )

        # Verify the response and request
        assert response.response.status_code == 204
        assert m.called
        assert m.last_request.method == "DELETE"

        # Verify request body
        request_json = m.last_request.json()
        assert str(object_id1) in request_json["object_ids"]
        assert str(object_id2) in request_json["object_ids"]
        assert str(user_id) in request_json["user_ids"]
        assert str(group_id) in request_json["group_ids"]
        assert request_json["include_assets"] is True
        assert request_json["include_collections"] is True


def test_get_group_acl():
    """Test getting group ACL for an object."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        group_id = str(uuid.uuid4())
        object_type = "assets"
        object_key = str(uuid.uuid4())

        # Expected response data
        response_data = {
            "group_id": group_id,
            "object_key": object_key,
            "object_type": object_type,
            "permissions": ["read", "write"],
            "date_created": "2025-05-20T09:50:09Z",
            "date_modified": "2025-05-20T09:50:09Z",
        }

        # Mock the API endpoint
        mock_address = AclsSpec.gen_url(
            f"groups/{group_id}/acl/{object_type}/{object_key}/")
        m.get(mock_address, json=response_data)

        # Create client and make request
        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)
        response = client.acls().get_group_acl(
            group_id=group_id,
            object_type=object_type,
            object_key=object_key,
        )

        # Verify the response and request
        assert response.response.ok
        assert m.called
        assert m.last_request.method == "GET"

        # Verify response data
        assert str(response.data.group_id) == group_id
        assert response.data.object_key == object_key
        assert response.data.object_type == object_type
        assert response.data.permissions == ["read", "write"]


def test_check_group_permission():
    """Test checking group permission for an object."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        group_id = str(uuid.uuid4())
        object_type = "assets"
        object_key = str(uuid.uuid4())
        permission = "read"

        # Mock the API endpoint
        mock_address = AclsSpec.gen_url(
            f"groups/{group_id}/acl/{object_type}/{object_key}/{permission}/")
        m.get(mock_address, status_code=204)

        # Create client and make request
        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)
        response = client.acls().check_group_permission(
            group_id=group_id,
            object_type=object_type,
            object_key=object_key,
            permission=permission,
        )

        # Verify the response and request
        assert response.response.status_code == 204
        assert m.called
        assert m.last_request.method == "GET"


def test_delete_group_acl():
    """Test deleting group ACL for an object."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        group_id = str(uuid.uuid4())
        object_type = "assets"
        object_key = str(uuid.uuid4())

        # Mock the API endpoint
        mock_address = AclsSpec.gen_url(
            f"groups/{group_id}/acl/{object_type}/{object_key}/")
        m.delete(mock_address, status_code=204)

        # Create client and make request
        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)
        response = client.acls().delete_group_acl(
            group_id=group_id,
            object_type=object_type,
            object_key=object_key,
        )

        # Verify the response and request
        assert response.response.status_code == 204
        assert m.called
        assert m.last_request.method == "DELETE"


def test_get_user_acl():
    """Test getting user ACL for an object."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        user_id = str(uuid.uuid4())
        object_type = "assets"
        object_key = str(uuid.uuid4())

        # Expected response data
        response_data = {
            "user_id": user_id,
            "object_key": object_key,
            "object_type": object_type,
            "permissions": ["read", "write"],
            "date_created": "2025-05-20T09:50:09Z",
            "date_modified": "2025-05-20T09:50:09Z",
        }

        # Mock the API endpoint
        mock_address = AclsSpec.gen_url(
            f"users/{user_id}/acl/{object_type}/{object_key}/")
        m.get(mock_address, json=response_data)

        # Create client and make request
        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)
        response = client.acls().get_user_acl(
            user_id=user_id,
            object_type=object_type,
            object_key=object_key,
        )

        # Verify the response and request
        assert response.response.ok
        assert m.called
        assert m.last_request.method == "GET"

        # Verify response data
        assert str(response.data.user_id) == user_id
        assert response.data.object_key == object_key
        assert response.data.object_type == object_type
        assert response.data.permissions == ["read", "write"]


def test_update_user_acl():
    """Test updating user ACL for an object."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        user_id = str(uuid.uuid4())
        object_type = "assets"
        object_key = str(uuid.uuid4())

        # Create ACL data
        acl_data = {"permissions": ["read", "write"]}

        # Expected response data
        response_data = {
            "user_id": user_id,
            "object_key": object_key,
            "object_type": object_type,
            "permissions": ["read", "write"],
            "date_created": "2025-05-20T09:50:09Z",
            "date_modified": "2025-05-20T09:50:09Z",
        }

        # Mock the API endpoint
        mock_address = AclsSpec.gen_url(
            f"users/{user_id}/acl/{object_type}/{object_key}/")
        m.put(mock_address, json=response_data)

        # Create client and make request
        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)
        response = client.acls().update_user_acl(
            user_id=user_id,
            object_type=object_type,
            object_key=object_key,
            acl=acl_data,
        )

        # Verify the response and request
        assert response.response.ok
        assert m.called
        assert m.last_request.method == "PUT"

        # Verify request body
        request_json = m.last_request.json()
        assert request_json["permissions"] == ["read", "write"]

        # Verify response data
        assert str(response.data.user_id) == user_id
        assert response.data.object_key == object_key
        assert response.data.object_type == object_type
        assert response.data.permissions == ["read", "write"]


def test_delete_user_acl():
    """Test deleting user ACL for an object."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        user_id = str(uuid.uuid4())
        object_type = "assets"
        object_key = str(uuid.uuid4())

        # Mock the API endpoint
        mock_address = AclsSpec.gen_url(
            f"users/{user_id}/acl/{object_type}/{object_key}/")
        m.delete(mock_address, status_code=204)

        # Create client and make request
        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)
        response = client.acls().delete_user_acl(
            user_id=user_id,
            object_type=object_type,
            object_key=object_key,
        )

        # Verify the response and request
        assert response.response.status_code == 204
        assert m.called
        assert m.last_request.method == "DELETE"


def test_check_user_permission():
    """Test checking user permission for an object."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        user_id = str(uuid.uuid4())
        object_type = "assets"
        object_key = str(uuid.uuid4())
        permission = "read"

        # Expected response data
        response_data = {
            "user_id": user_id,
            "object_key": object_key,
            "object_type": object_type,
            "permissions": ["read", "write"],
            "date_created": "2025-05-20T09:50:09Z",
            "date_modified": "2025-05-20T09:50:09Z",
        }

        # Mock the API endpoint
        mock_address = AclsSpec.gen_url(
            f"users/{user_id}/acl/{object_type}/{object_key}/{permission}/")
        m.get(mock_address, json=response_data)

        # Create client and make request
        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)
        response = client.acls().check_user_permission(
            user_id=user_id,
            object_type=object_type,
            object_key=object_key,
            permission=permission,
        )

        # Verify the response and request
        assert response.response.ok
        assert m.called
        assert m.last_request.method == "GET"

        # Verify response data
        assert str(response.data.user_id) == user_id
        assert response.data.permissions == ["read", "write"]


def test_fetch_share_acls():
    """Test fetching share ACLs for an object."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        object_type = "assets"
        object_key = str(uuid.uuid4())
        share_id = str(uuid.uuid4())

        # Expected response data
        response_data = {
            "objects": [{
                "share_id": share_id,
                "object_key": object_key,
                "object_type": object_type,
                "permissions": ["read"],
                "date_created": "2025-05-20T09:50:09Z",
                "date_modified": "2025-05-20T09:50:09Z",
            }],
            "total":
            1,
            "page":
            1,
            "pages":
            1,
            "per_page":
            10,
        }

        # Mock the API endpoint
        mock_address = AclsSpec.gen_url(f"shares/{object_type}/{object_key}/")
        m.get(mock_address, json=response_data)

        # Create client and make request
        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)
        response = client.acls().list_share_acls(
            object_type=object_type,
            object_key=object_key,
        )

        # Verify the response and request
        assert response.response.ok
        assert m.called
        assert m.last_request.method == "GET"

        # Verify response data
        assert len(response.data.objects) == 1
        assert str(response.data.objects[0].share_id) == share_id
        assert response.data.objects[0].object_key == object_key
        assert response.data.objects[0].object_type == object_type
        assert response.data.objects[0].permissions == ["read"]


def test_create_share_acls():
    """Test creating share ACLs for multiple objects."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        share_id = str(uuid.uuid4())
        object_type = "assets"
        object_key1 = str(uuid.uuid4())
        object_key2 = str(uuid.uuid4())

        # Create ACLs data
        acls_data = {
            "object_keys": [str(object_key1),
                            str(object_key2)],
            "object_type": object_type,
            "permissions": ["read"],
            "share_id": str(share_id),
        }

        # Expected response data
        response_data = {
            "updated_object_keys": [str(object_key1),
                                    str(object_key2)]
        }

        # Mock the API endpoint
        mock_address = AclsSpec.gen_url(
            f"shares/{share_id}/acl/{object_type}/")
        m.put(mock_address, json=response_data)

        # Create client and make request
        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)
        response = client.acls().create_share_acls(
            share_id=share_id,
            object_type=object_type,
            acls=acls_data,
        )

        # Verify the response and request
        assert response.response.ok
        assert m.called
        assert m.last_request.method == "PUT"

        # Verify request body
        request_json = m.last_request.json()
        assert str(object_key1) in request_json["object_keys"]
        assert str(object_key2) in request_json["object_keys"]
        assert request_json["permissions"] == ["read"]
        assert request_json["object_type"] == object_type

        # Verify response data
        assert response.data.updated_object_keys == [
            str(object_key1),
            str(object_key2),
        ]


def test_get_share_acl():
    """Test getting share ACL for an object."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        share_id = str(uuid.uuid4())
        object_type = "assets"
        object_key = str(uuid.uuid4())

        # Expected response data
        response_data = {
            "share_id": share_id,
            "object_key": object_key,
            "object_type": object_type,
            "permissions": ["read"],
            "date_created": "2025-05-20T09:50:09Z",
            "date_modified": "2025-05-20T09:50:09Z",
        }

        # Mock the API endpoint
        mock_address = AclsSpec.gen_url(
            f"shares/{share_id}/acl/{object_type}/{object_key}/")
        m.get(mock_address, json=response_data)

        # Create client and make request
        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)
        response = client.acls().get_share_acl(
            share_id=share_id,
            object_type=object_type,
            object_key=object_key,
        )

        # Verify the response and request
        assert response.response.ok
        assert m.called
        assert m.last_request.method == "GET"

        # Verify response data
        assert str(response.data.share_id) == share_id
        assert response.data.object_key == object_key
        assert response.data.object_type == object_type
        assert response.data.permissions == ["read"]


def test_create_share_acl():
    """Test creating share ACL for an object."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        share_id = str(uuid.uuid4())
        object_type = "assets"
        object_key = str(uuid.uuid4())

        # Create ACL data
        acl_data = {"permissions": ["read"]}

        # Expected response data
        response_data = {
            "share_id": share_id,
            "object_key": object_key,
            "object_type": object_type,
            "permissions": ["read"],
            "date_created": "2025-05-20T09:50:09Z",
            "date_modified": "2025-05-20T09:50:09Z",
        }

        # Mock the API endpoint
        mock_address = AclsSpec.gen_url(
            f"shares/{share_id}/acl/{object_type}/{object_key}/")
        m.post(mock_address, json=response_data)

        # Create client and make request
        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)
        response = client.acls().create_share_acl(
            share_id=share_id,
            object_type=object_type,
            object_key=object_key,
            acl=acl_data,
        )

        # Verify the response and request
        assert response.response.ok
        assert m.called
        assert m.last_request.method == "POST"

        # Verify request body
        request_json = m.last_request.json()
        assert request_json["permissions"] == ["read"]

        # Verify response data
        assert str(response.data.share_id) == share_id
        assert response.data.object_key == object_key
        assert response.data.object_type == object_type
        assert response.data.permissions == ["read"]


def test_update_share_acl():
    """Test updating share ACL for an object."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        share_id = str(uuid.uuid4())
        object_type = "assets"
        object_key = str(uuid.uuid4())

        # Create ACL data
        acl_data = {"permissions": ["read", "write"]}

        # Expected response data
        response_data = {
            "share_id": share_id,
            "object_key": object_key,
            "object_type": object_type,
            "permissions": ["read", "write"],
            "date_created": "2025-05-20T09:50:09Z",
            "date_modified": "2025-05-20T09:50:09Z",
        }

        # Mock the API endpoint
        mock_address = AclsSpec.gen_url(
            f"shares/{share_id}/acl/{object_type}/{object_key}/")
        m.put(mock_address, json=response_data)

        # Create client and make request
        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)
        response = client.acls().update_share_acl(
            share_id=share_id,
            object_type=object_type,
            object_key=object_key,
            acl=acl_data,
        )

        # Verify the response and request
        assert response.response.ok
        assert m.called
        assert m.last_request.method == "PUT"

        # Verify request body
        request_json = m.last_request.json()
        assert request_json["permissions"] == ["read", "write"]

        # Verify response data
        assert str(response.data.share_id) == share_id
        assert response.data.object_key == object_key
        assert response.data.object_type == object_type
        assert response.data.permissions == ["read", "write"]


def test_delete_share_acl():
    """Test deleting share ACL for an object."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        share_id = str(uuid.uuid4())
        object_type = "assets"
        object_key = str(uuid.uuid4())

        # Mock the API endpoint
        mock_address = AclsSpec.gen_url(
            f"shares/{share_id}/acl/{object_type}/{object_key}/")
        m.delete(mock_address, status_code=204)

        # Create client and make request
        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)
        response = client.acls().delete_share_acl(
            share_id=share_id,
            object_type=object_type,
            object_key=object_key,
        )

        # Verify the response and request
        assert response.response.status_code == 204
        assert m.called
        assert m.last_request.method == "DELETE"


def test_check_share_permission():
    """Test checking share permission for an object."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        share_id = str(uuid.uuid4())
        object_type = "assets"
        object_key = str(uuid.uuid4())
        permission = "read"

        # Mock the API endpoint
        mock_address = AclsSpec.gen_url(
            f"shares/{share_id}/acl/{object_type}/{object_key}/{permission}/")
        m.get(mock_address, status_code=204)

        # Create client and make request
        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)
        response = client.acls().check_share_permission(
            share_id=share_id,
            object_type=object_type,
            object_key=object_key,
            permission=permission,
        )

        # Verify the response and request
        assert response.response.status_code == 204
        assert m.called
        assert m.last_request.method == "GET"
