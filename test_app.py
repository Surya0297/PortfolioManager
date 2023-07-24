import json
import pytest
from app import app
import requests

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_create_portfolio_manager(client):
    data = {
        "name": "John Doe",
        "status": True,
        "role": "Administrator",
        "bio": "Experienced manager",
        "start_date": "2023-07-18",
        "username": "john_doe",
        "password": "strong_password"
    }

    response = client.post('/portfolio_managers', json=data)
    assert response.status_code == 201
    response_data = json.loads(response.data)
    assert "manager_id" in response_data
    assert "message" in response_data

def test_get_all_portfolio_managers(client):
    response = client.get('/portfolio_managers')
    assert response.status_code == 200
    managers_data = json.loads(response.data)
    assert isinstance(managers_data, list)

def test_get_portfolio_manager(client):
    # First, create a test portfolio manager for testing the GET by ID endpoint
    data = {
        "name": "Test Manager",
        "status": True,
        "role": "Viewer",
        "bio": "Test bio",
        "start_date": "2023-07-19",
        "username": "test_manager",
        "password": "test_password"
    }

    create_response = client.post('/portfolio_managers', json=data)
    create_data = json.loads(create_response.data)
    created_manager_id = create_data["manager_id"]

    # Now, try to fetch the created portfolio manager by ID
    response = client.get(f'/portfolio_managers/{created_manager_id}')
    assert response.status_code == 200
    manager_data = json.loads(response.data)
    assert isinstance(manager_data, dict)

def test_update_portfolio_manager(client):
    # First, create a test portfolio manager for testing the update endpoint
    data = {
        "name": "Test Manager",
        "status": True,
        "role": "Viewer",
        "bio": "Test bio",
        "start_date": "2023-07-19",
        "username": "test_manager",
        "password": "test_password"
    }

    create_response = client.post('/portfolio_managers', json=data)
    create_data = json.loads(create_response.data)
    created_manager_id = create_data["manager_id"]

    # Update the created manager's data
    updated_data = {
        "name": "Updated Test Manager",
        "bio": "Updated bio"
    }

    update_response = client.put(f'/portfolio_managers/{created_manager_id}', json=updated_data)
    assert update_response.status_code == 200
    update_data = json.loads(update_response.data)
    assert "message" in update_data

def test_delete_portfolio_manager(client):
    # First, create a test portfolio manager for testing the delete endpoint
    data = {
        "name": "Test Manager",
        "status": True,
        "role": "Viewer",
        "bio": "Test bio",
        "start_date": "2023-07-19",
        "username": "test_manager",
        "password": "test_password"
    }

    create_response = client.post('/portfolio_managers', json=data)
    create_data = json.loads(create_response.data)
    created_manager_id = create_data["manager_id"]

    # Now, try to delete the created portfolio manager by ID
    delete_response = client.delete(f'/portfolio_managers/{created_manager_id}')
    assert delete_response.status_code == 200
    delete_data = json.loads(delete_response.data)
    assert "message" in delete_data

# Assuming the base URL for the API server
BASE_URL = 'http://localhost:5000'

def test_create_resource(client):
    data = {
        "name": "Test Resource",
        "status": "available"
        # Add other fields as needed for resource creation
    }

    response = client.post('/resources', json=data)
    assert response.status_code == 201
    response_data = json.loads(response.data)
    assert "resource_id" in response_data
    assert "message" in response_data


def test_get_all_resources(client):
    response = client.get('/resources')
    assert response.status_code == 200
    resources_data = json.loads(response.data)
    assert isinstance(resources_data, list)


def test_get_resource(client):
    # First, create a test resource for testing the GET by ID endpoint
    data = {
        "name": "Test Resource",
        "status": "available"
        # Add other fields as needed for resource creation
    }

    create_response = client.post('/resources', json=data)
    create_data = json.loads(create_response.data)
    created_resource_id = create_data["resource_id"]

    # Now, try to fetch the created resource by ID
    response = client.get(f'/resources/{created_resource_id}')
    assert response.status_code == 200
    resource_data = json.loads(response.data)
    assert isinstance(resource_data, dict)


def test_update_resource(client):
    # First, create a test resource for testing the update endpoint
    data = {
        "name": "Test Resource",
        "status": "available"
        # Add other fields as needed for resource creation
    }

    create_response = client.post('/resources', json=data)
    create_data = json.loads(create_response.data)
    created_resource_id = create_data["resource_id"]

    # Update the created resource's data
    updated_data = {
        "name": "Updated Test Resource",
        "status": "unavailable"
        # Add other fields as needed for resource update
    }

    update_response = client.put(f'/resources/{created_resource_id}', json=updated_data)
    assert update_response.status_code == 200
    update_data = json.loads(update_response.data)
    assert "message" in update_data


def test_delete_resource(client):
    # First, create a test resource for testing the delete endpoint
    data = {
        "name": "Test Resource",
        "status": "available"
        # Add other fields as needed for resource creation
    }

    create_response = client.post('/resources', json=data)
    create_data = json.loads(create_response.data)
    created_resource_id = create_data["resource_id"]

    # Now, try to delete the created resource by ID
    delete_response = client.delete(f'/resources/{created_resource_id}')
    assert delete_response.status_code == 200
    delete_data = json.loads(delete_response.data)
    assert "message" in delete_data

