"""Tests for Docker environment configuration and container functionality."""
import os
import sys
import pytest
import socket
from app import app


@pytest.fixture
def docker_environment():
    """Setup Docker environment configuration"""
    return {
        'PYTHON_VERSION': '3.11',
        'PORT': 9000,
        'APP_DIR': '/app'
    }


def test_python_version(docker_environment):
    """Test Python version matches Docker configuration"""
    current_version = f"{sys.version_info.major}.{sys.version_info.minor}"
    assert current_version == docker_environment['PYTHON_VERSION'], \
        f"Python version {current_version} does not match expected {docker_environment['PYTHON_VERSION']}"


def test_docker_environment_variables():
    """Test Docker environment variables are set correctly"""
    # Check if running in Docker (presence of /.dockerenv file)
    in_docker = os.path.exists('/.dockerenv')
    if in_docker:
        # Verify working directory
        assert os.getcwd() == '/app', "Working directory should be /app in Docker"
        
        # Check PATH includes Python binaries
        assert '/usr/local/bin' in os.environ.get('PATH', ''), \
            "Python binary path not found in PATH"


def test_static_directory_mount():
    """Test static directory is properly mounted and accessible"""
    assert os.path.exists('static'), "Static directory not found"
    assert os.path.exists('static/index.html'), "index.html not found in static directory"
    
    # Test file permissions
    assert os.access('static/index.html', os.R_OK), "static/index.html is not readable"


def test_port_availability(docker_environment):
    """Test if the default port is available"""
    port = docker_environment['PORT']
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind(('', port))
        port_available = True
    except socket.error:
        port_available = False
    finally:
        s.close()
    
    assert port_available, f"Port {port} is not available"


def test_docker_flask_config():
    """Test Flask application configuration in Docker"""
    # Test debug mode (should be off in Docker)
    assert not app.debug, "Debug mode should be disabled in Docker environment"
    
    # Test static folder configuration
    assert app.static_folder.endswith('static'), "Static folder not properly configured"
    assert os.path.isabs(app.static_folder), \
        "Static folder path should be absolute in Docker"


def test_requirements_installed():
    """Test that all required packages are installed"""
    import pkg_resources
    
    with open('requirements.txt') as f:
        requirements = [
            line.strip().split('==')[0].lower()
            for line in f
            if line.strip() and not line.startswith('#')
        ]
    
    installed = {pkg.key for pkg in pkg_resources.working_set}
    missing = [req for req in requirements if req not in installed]
    
    assert not missing, f"Missing required packages: {', '.join(missing)}"


@pytest.mark.skipif(not os.path.exists('Dockerfile.test'),
                   reason="Dockerfile.test not found")
def test_dockerfile_configuration():
    """Test Dockerfile.test contains required configuration"""
    with open('Dockerfile.test') as f:
        content = f.read().lower()
        
        # Check for essential Docker commands
        assert 'from python' in content, "Base Python image not specified"
        assert 'copy requirements.txt' in content, "Requirements.txt not copied"
        assert 'pip install' in content, "Dependencies not installed"
        assert 'cmd ["pytest"' in content, "Test command not properly configured"


def test_flask_test_client(docker_environment):
    """Test Flask test client works in Docker environment"""
    app.config['TESTING'] = True
    client = app.test_client()
    
    response = client.get('/')
    assert response.status_code == 200, "Flask test client failed to get index route"
    assert response.content_type == 'text/html; charset=utf-8', \
        "Incorrect content type from test client"