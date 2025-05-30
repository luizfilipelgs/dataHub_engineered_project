import pytest
from fastapi.testclient import TestClient

from src.app.app import app


@pytest.fixture
def client():
    return TestClient(app)
