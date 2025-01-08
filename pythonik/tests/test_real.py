"""
testing real api calls
"""

import pytest
from pythonik.client import PythonikClient
from pythonik.models.assets.segments import SegmentBody
from pythonik.models.mutation.metadata.mutate import UpdateMetadata
from pythonik.models.assets.collections import Content, AddContentResponse
from pythonik.models.base import ObjectType
from pythonik.models.search.search_body import SearchBody

@pytest.mark.skip
def test_create_segment_with_view():
    """Test creating a segment and adding view metadata to it"""
    # These would typically come from environment variables or config
    app_id = "caa5a1a8-9bb8-11ef-acdf-f2076c2749c9"
    auth_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjM0ZjVhYjFhLWExZWItMTFlZi1iNzdlLWRhNGViMjdkZjhiYyIsImV4cCI6MjA0Njk4MTcwNCwic3lzIjoiaWNvbmlrLXVzIn0.aLjigwHx_kal6Qqv5v3WNASKt_yJ2vB8yLIVrubi2RU"
    asset_id = "b56d6758-9e24-11ef-8773-8a9b2df86038"
    view_id = "f55d96d8-9b01-11ef-bdeb-fa5f803dfa2b"
    
    # Initialize client
    client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=10)
    

    segment_data = {
        "metadata_view_id": view_id,
        "segment_text": "Test Segment",
        "segment_type": "GENERIC",
        "time_start_milliseconds": 1024,
        "time_end_milliseconds": 1024,
    }
    segment_body = SegmentBody(**segment_data)
    
    # Create the segment
    segment_response = client.assets().create_segment(
        asset_id=asset_id, 
        body=segment_body
    )
    
    assert segment_response.response.ok == True
    assert segment_response.data.segment_text == "Test Segment"

    
    # Get the segment ID from the response
    segment_id = segment_response.data.id
    
    # Create metadata for the segment view
    metadata_values = {
        "metadata_values": {
            "Quarter": {
                "field_values": [
                    {"value": "Q1"}
                ]
            },
            "PeriodType": {
                "field_values": [
                    {"value": "REGULAR"}
                ]
            },
            "tricode": {
                "field_values": [
                    {"value": "GSW"}
                ]
            },
            "Name": {
                "field_values": [
                    {"value": "Stephen Curry 3PT Jump Shot"}
                ]
            },
            "description": {
                "field_values": [
                    {"value": "Stephen Curry makes 26-foot three point jumper (Draymond Green assists)"}
                ]
            }
        }
    }
    metadata_body = UpdateMetadata.model_validate(metadata_values)
    
    # Update the segment's view metadata
    metadata_response = client.metadata().put_segment_view_metadata(
        asset_id=asset_id,
        segment_id=segment_id,
        view_id=view_id,
        metadata=metadata_body
    )
    
    assert metadata_response.response.ok == True
    assert metadata_response.data is not None


@pytest.mark.skip
def test_add_content_to_collection():
    """Test adding an asset to a collection"""
    # These would typically come from environment variables or config
    app_id = "caa5a1a8-9bb8-11ef-acdf-f2076c2749c9"
    auth_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjM0ZjVhYjFhLWExZWItMTFlZi1iNzdlLWRhNGViMjdkZjhiYyIsImV4cCI6MjA0Njk4MTcwNCwic3lzIjoiaWNvbmlrLXVzIn0.aLjigwHx_kal6Qqv5v3WNASKt_yJ2vB8yLIVrubi2RU"
    collection_id = "dc800ca8-b335-11ef-b839-6af17edf168a"
    asset_id = "b56d6758-9e24-11ef-8773-8a9b2df86038"
    
    # Initialize client
    client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=10)
    
    # Create content object
    content = Content(
        object_id=asset_id,
        object_type=ObjectType.ASSETS
    )
    
    # Add content to collection
    response = client.collections().add_content(
        collection_id=collection_id,
        body=content
    )
    

    # Verify the response
    assert response.response.ok == True
    assert isinstance(response.data, AddContentResponse)


@pytest.mark.skip
def test_put_metadata_direct():
    """Test direct metadata update without a view."""
    # These would typically come from environment variables or config
    app_id = "caa5a1a8-9bb8-11ef-acdf-f2076c2749c9"
    auth_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjM0ZjVhYjFhLWExZWItMTFlZi1iNzdlLWRhNGViMjdkZjhiYyIsImV4cCI6MjA0Njk4MTcwNCwic3lzIjoiaWNvbmlrLXVzIn0.aLjigwHx_kal6Qqv5v3WNASKt_yJ2vB8yLIVrubi2RU"
    object_type = ObjectType.ASSETS.value
    object_id = "b56d6758-9e24-11ef-8773-8a9b2df86038"

    # Initialize client with longer timeout for real API calls
    client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=10)

    # Create test metadata
    metadata_values = {
        "metadata_values": {
            "description": {
                "field_values": [
                    {"value": "Test value from direct update"}
                ]
            },
            "Title": {
                "field_values": [
                    {"value": "Test title"}
                ]
            },
            "_gcvi_tags": {
                "field_values": [
                    {"value": "Art"},
                    {"value": "Adventure"}
                ]
            }
        }
    }
    metadata = UpdateMetadata.model_validate(metadata_values)

    # Update metadata directly
    response = client.metadata().put_metadata_direct(
        object_type=object_type,
        object_id=object_id,
        metadata=metadata
    )

    # Verify response
    assert response.response.ok, f"Failed to update metadata: {response.response.status_code}"
    assert response.data.object_id == object_id
    assert response.data.object_type == object_type
    
    # Verify metadata values were updated
    assert "description" in response.data.metadata_values
    assert "Title" in response.data.metadata_values
    assert "_gcvi_tags" in response.data.metadata_values
    
    # Verify specific values
    description = response.data.metadata_values["description"]["field_values"][0]["value"]
    assert description == "Test value from direct update"
    
    title = response.data.metadata_values["Title"]["field_values"][0]["value"]
    assert title == "Test title"
    
    tags = [v["value"] for v in response.data.metadata_values["_gcvi_tags"]["field_values"]]
    assert tags == ["Art", "Adventure"]
    
    print(f"Successfully updated metadata for {object_type}/{object_id}")
    print(f"Updated values: {response.data.metadata_values}")


def test_get_asset_alternative_url():
    """Test getting an asset using alternative base URL"""
    # These would typically come from environment variables or config
    app_id = "590e8726-c3cc-11ef-8ca0-fa3de296928f"
    auth_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjY0MTkxM2MwLWMzY2MtMTFlZi1iOGY2LTcyZDQyOTliNGRjMyIsImV4cCI6MjA1MDcwNjgwOSwic3lzIjoiaWNvbmlrLWF3cy11cyJ9.fwS6xXNK19dvWTTLL5SFgQr8WJTBhE4np8yR2H7olTM"
    asset_id = "b109ad6e-565a-11ef-a79a-f2af7ce6e2fb"
    
    # Initialize client with alternative base URL
    client = PythonikClient(
        app_id=app_id, 
        auth_token=auth_token, 
        timeout=10,
        base_url="https://app.aws.iconik.io/"
    )
    
    # Get the asset
    asset_response = client.assets().get(asset_id=asset_id)
    
    # Verify the response
    assert asset_response.response.ok == True
    assert asset_response.data.id == asset_id


def test_get_asset_default_url():
    """Test getting an asset using default base URL"""
    # These would typically come from environment variables or config
    app_id = "caa5a1a8-9bb8-11ef-acdf-f2076c2749c9"
    auth_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjM0ZjVhYjFhLWExZWItMTFlZi1iNzdlLWRhNGViMjdkZjhiYyIsImV4cCI6MjA0Njk4MTcwNCwic3lzIjoiaWNvbmlrLXVzIn0.aLjigwHx_kal6Qqv5v3WNASKt_yJ2vB8yLIVrubi2RU"
    asset_id = "5379bff4-b9b0-11ef-b483-8ed2245f54dc"
    
    # Initialize client with default base URL
    client = PythonikClient(
        app_id=app_id, 
        auth_token=auth_token, 
        timeout=10
    )
    
    # Get the asset
    asset_response = client.assets().get(asset_id=asset_id)
    
    # Verify the response
    assert asset_response.response.ok == True
    assert asset_response.data.id == asset_id


def test_search_alternative_url():
    """Test searching using alternative base URL"""
    # These would typically come from environment variables or config
    app_id = "590e8726-c3cc-11ef-8ca0-fa3de296928f"
    auth_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjY0MTkxM2MwLWMzY2MtMTFlZi1iOGY2LTcyZDQyOTliNGRjMyIsImV4cCI6MjA1MDcwNjgwOSwic3lzIjoiaWNvbmlrLWF3cy11cyJ9.fwS6xXNK19dvWTTLL5SFgQr8WJTBhE4np8yR2H7olTM"
    
    # Initialize client with alternative base URL
    client = PythonikClient(
        app_id=app_id, 
        auth_token=auth_token, 
        timeout=10,
        base_url="https://app.aws.iconik.io/"
    )
    
    # Create search body
    search_body = SearchBody(
        doc_types=["assets"],
        query="test",  # Search for assets containing "test"
        include_fields=["id", "title", "description"]
    )
    
    # Perform the search
    search_response = client.search().search(search_body=search_body)
    
    # Verify the response
    assert search_response.response.ok == True
    assert hasattr(search_response.data, 'objects')
    assert isinstance(search_response.data.objects, list)
    assert len(search_response.data.objects) > 0
    
    # Verify search found items with "test" in the title
    for obj in search_response.data.objects:
        assert "test" in obj.title.lower()