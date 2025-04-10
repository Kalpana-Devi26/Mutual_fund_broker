import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# tests/test_portfolio.py
def test_add_investment(client):
    payload = {"fund_name": "Test Fund", "amount_invested": 1000.0}
    response = client.post("/portfolio/add", json=payload)
    assert response.status_code == 200

def test_view_portfolio(client):
    response = client.get("/portfolio/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# def test_add_investment():
#     # First register and login to get token
#     client.post("/auth/register", json={"email": "investor@test.com", "password": "invest123"})
#     login_resp = client.post("/auth/login", json={"email": "investor@test.com", "password": "invest123"})
#     token = login_resp.json()["access_token"]

#     headers = {"Authorization": f"Bearer {token}"}
#     data = {"fund_name": "Test Fund", "amount_invested": 1000.0}
#     response = client.post("/portfolio/add", json=data, headers=headers)

#     assert response.status_code == 200
#     assert response.json()["fund_name"] == "Test Fund"

# def test_view_portfolio():
#     response = client.get("/portfolio/")
#     assert response.status_code == 200
