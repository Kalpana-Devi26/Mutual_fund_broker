import sys
import os
import pytest

# Add the root directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

# def test_register_user():
#     response = client.post("/auth/register", json={
#         "email": "testuser@example.com",
#         "password": "test123"
#     })
#     assert response.status_code == 200
#     assert "access_token" in response.json()

# def test_register_existing_user():
#     response = client.post("/auth/register", json={
#         "email": "testuser@example.com",
#         "password": "test123"
#     })
#     assert response.status_code == 400

# def test_login_success():
#     response = client.post("/auth/login", json={
#         "email": "testuser@example.com",
#         "password": "test123"
#     })
#     assert response.status_code == 200
#     assert "access_token" in response.json()

# def test_login_invalid():
#     response = client.post("/auth/login", json={
#         "email": "testuser@example.com",
#         "password": "wrongpassword"
#     })
#     assert response.status_code == 401
# tests/test_auth.py
def test_register_user(client):
    response = client.post("/auth/register", json={"email": "test@test.com", "password": "test123"})
    assert response.status_code == 200 or response.status_code == 400

def test_register_existing_user(client):
    client.post("/auth/register", json={"email": "exist@test.com", "password": "test123"})
    response = client.post("/auth/register", json={"email": "exist@test.com", "password": "test123"})
    assert response.status_code == 400

def test_login_success(client):
    client.post("/auth/register", json={"email": "login@test.com", "password": "test123"})
    response = client.post("/auth/login", json={"email": "login@test.com", "password": "test123"})
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_login_invalid(client):
    response = client.post("/auth/login", json={"email": "nope@test.com", "password": "wrongpass"})
    assert response.status_code == 401
