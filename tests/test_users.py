from fastapi.testclient import TestClient
from app.main import app
from app import schemas

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to my API"}

def test_create_user():
    response = client.post("/users/", json={
        "email": "vitalicstinca123@gmail.com",
        "password": "password123"
    })
    user = schemas.UserResponse(**response.json())
    assert response.status_code == 201
    assert user.email == "vitalicstinca123@gmail.com"