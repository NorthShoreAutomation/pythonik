#!/usr/bin/env python3
"""
Simple integration test for the new get_segments endpoint.
Fill in your API credentials and asset ID to test locally.
"""

from pythonik.client import PythonikClient


def test_get_segments():
    # TODO: Fill in your actual credentials
    APP_ID = "8ede105e-79c8-11ef-b0e6-6ece97c32577"
    AUTH_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjIzOWFjODFlLTUyOTktMTFmMC1hZDQ2LTQ2ZmZjMmViZGM5YyIsImV4cCI6MjA2NjQwNzgxMiwic3lzIjoiaWNvbmlrLXVzIn0.3ZqehiN58GfyUKdXSTlVuj1nq10NUz05cCGtEaya1Pw"
    ASSET_ID = "513c2498-b9b0-11ef-a1ef-c2b84ec08062"  # Asset that has segments

    print("Testing get_segments endpoint...")

    # Initialize client
    client = PythonikClient(app_id=APP_ID, auth_token=AUTH_TOKEN, timeout=10)

    try:
        # Test 1: Basic call
        print("\n1. Testing basic get_segments call...")
        response = client.assets().get_segments(asset_id=ASSET_ID)

        print(f"Status Code: {response.response.status_code}")
        print(f"Total segments: {response.data.total}")
        print(f"Segments returned: {len(response.data.objects)}")

        if response.data.objects:
            first_segment = response.data.objects[0]
            print(f"First segment ID: {first_segment.id}")
            print(f"First segment text: {first_segment.segment_text}")
            print(f"First segment type: {first_segment.segment_type}")

        # Test 2: With pagination
        print("\n2. Testing with pagination...")
        response = client.assets().get_segments(asset_id=ASSET_ID, per_page=5, page=1)
        print(f"Per page: {response.data.per_page}")
        print(f"Current page: {response.data.page}")
        print(f"Segments returned: {len(response.data.objects)}")

        # Test 3: With filters (if you have specific segment types)
        print("\n3. Testing with filters...")
        response = client.assets().get_segments(
            asset_id=ASSET_ID,
            segment_type="MARKER",  # Change this to a type you have
            per_page=10,
        )
        print(f"Filtered segments (MARKER): {len(response.data.objects)}")

        # Test 4: With time filters
        print("\n4. Testing with time filters...")
        response = client.assets().get_segments(
            asset_id=ASSET_ID,
            time_start_milliseconds__gte=0,
            time_end_milliseconds__lte=60000,  # First minute
            per_page=10,
        )
        print(f"Segments in first minute: {len(response.data.objects)}")

        print("\n✅ All tests completed successfully!")

    except Exception as e:
        print(f"\n❌ Error occurred: {e}")
        print(f"Error type: {type(e).__name__}")

        # Print response details if available
        if hasattr(e, "response"):
            print(f"Response status: {e.response.status_code}")
            print(f"Response text: {e.response.text}")


if __name__ == "__main__":
    test_get_segments()
