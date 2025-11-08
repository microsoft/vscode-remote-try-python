"""Configure pytest for the project."""
import os
import sys

# Add the root directory to Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))