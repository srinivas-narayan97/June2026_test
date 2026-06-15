import pytest
from playwright.sync_api import APIRequestContext


@pytest.fixture
def api_context(playwright):
    """Fixture to create and manage Playwright API request context."""
    request_context = playwright.request.new_context(
        base_url="https://simple-grocery-store-api.click"
    )
    yield request_context
    request_context.dispose()


def test_get_status_api(api_context: APIRequestContext):
    """GET /status should return 200 and JSON {"status": "UP"} using playwright fixture."""
    
    response = api_context.get("/status")
    
    # Validate status code is 200
    assert response.status == 200, f"Expected status code 200, got {response.status}"
    
    # Parse and validate JSON response
    json_data = response.json()
    
    # Validate response contains "status" key
    assert "status" in json_data, "Response does not contain 'status' key"
    
    # Validate status value is "UP"
    assert json_data["status"] == "UP", f"Expected status 'UP', got {json_data['status']}"
    
    print(f"✓ Test passed! Response: {json_data}")
