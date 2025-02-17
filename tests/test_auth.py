import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

test_user = {
    "email": "testuser@example.com",
    "password": "testpassword123"
}

def test_register_user():
    response = client.post("/auth/register/", json=test_user)
    assert response.status_code == 200
    assert response.json()["message"] == "User registered correctly"

def test_register_duplicate_user():
    response1 = client.post("/auth/register/", json=test_user)
    assert response1.status_code == 200
    
    response2 = client.post("/auth/register/", json=test_user)
    assert response2.status_code == 400
    assert "already exists" in response2.json()["detail"]

def test_login_correct():
    response = client.post("auth/login/", json=test_user)
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_login_incorrect():
    wrong_user = {"email": "testuser@example.com", "password": "wrongpassword"}
    response = client.post("auth/login/", json=wrong_user)
    assert response.status_code == 401
    assert "access_token" not in response.json()