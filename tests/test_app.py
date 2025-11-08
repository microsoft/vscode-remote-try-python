"""Tests for vscode-remote-try-python Flask application."""
import os
import pytest
from app import app


@pytest.fixture
def test_client():
    """Create a test client fixture"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


@pytest.fixture
def app_config():
    """Fixture for app configuration"""
    return {
        'STATIC_FOLDER': 'static',
        'TESTING': True,
        'DEBUG': False
    }


def test_index_route(test_client):
    """Test that the index route returns the correct static file"""
    response = test_client.get('/')

    # Test status code
    assert response.status_code == 200

    # Test content type
    assert response.content_type == 'text/html; charset=utf-8'

    # Test actual content from static/index.html
    assert b'VS Code Rocks!' in response.data
    assert b'VS Code can do that?' in response.data


def test_static_file_serving(test_client):
    """Test that static files are served correctly"""
    response = test_client.get('/')
    assert response.status_code == 200
    assert 'text/html' in response.content_type


def test_docker_container_environment(test_client):
    """Test application works correctly in Docker environment"""
    response = test_client.get('/')
    assert response.status_code == 200

    # Verify static file configuration
    # Check if path ends with /static
    assert app.static_folder.endswith('/static')
    assert app.static_url_path == '/static'
