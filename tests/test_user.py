from dotenv import load_dotenv
load_dotenv(".env")
import pytest
from google.api_core.datetime_helpers import DatetimeWithNanoseconds
from fastapi import HTTPException


from src.TPL.db.user import User

@pytest.fixture
def user_data():
    return {
        "user_id": "123",
        "allowed_deployments": 5,
        "email": "test@example.com",
        "fname": "John",
        "github": "https://github.com/johndoe",
        "linkedin": "https://linkedin.com/in/johndoe",
        "lname": "Doe",
        "phone": "+1 555-555-5555",
        "photo_url": "https://example.com/profile.jpg",
        "role": "admin",
        "username": "johndoe",
        "websites": {}
    }

def test_create_user(user_data):
    user = User.create(user_data)
    user_from_db = User.get(user.user_id)

    assert user.user_id == user_from_db.user_id
    assert user.username == user_from_db.username

def test_save_user(user_data):
    user_data["created_at"] = DatetimeWithNanoseconds(2023, 4, 23, 10, 30)
    user = User(**user_data)
    user.save()

    user_from_db = User.get(user.user_id)
    assert user_from_db.user_id == user_data["user_id"]

def test_get_user(user_data):
    user = User.get(user_data["user_id"])
    assert user.user_id == user_data["user_id"]

def test_get_user_not_found():
    with pytest.raises(HTTPException) as excinfo:
        User.get("non_existing_user_id")

    assert excinfo.value.status_code == 404
    assert excinfo.value.detail == "User not found"

def test_get_user_from_username(user_data):
    user = User.get_from_username(user_data["username"])
    assert user.user_id == user_data["user_id"]

def test_get_user_from_username_not_found():
    with pytest.raises(HTTPException) as excinfo:
        User.get_from_username("non_existing_username")

    assert excinfo.value.status_code == 404
    assert excinfo.value.detail == "User not found"
