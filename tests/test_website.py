from dotenv import load_dotenv
load_dotenv(".env")
import pytest
from fastapi import HTTPException
from google.api_core.datetime_helpers import DatetimeWithNanoseconds

from src.TPL.db.website import Website, WebsiteType
from src.TPL.db.config import db
import uuid


# Sample website data
website_data = {
    "created_at": DatetimeWithNanoseconds.now(),
    "description": "Sample website",
    "env": {},
    "name": "website",
    "owner_id": "owner123",
    "port_number": "8000",
    "repo_name": "website_repo",
    "type": WebsiteType.FRONTEND,
}

# Test create website
def test_create_website():
    new_website = Website.create(website_data)

    assert new_website.description == "Sample website"
    assert new_website.repo_name == "website_repo"
    assert new_website.type == WebsiteType.FRONTEND

    # Cleanup
    new_website.delete()

# Test save website
def test_save_website():
    website_id = str(uuid.uuid4())
    website_data["website_id"] = website_id
    website = Website(**website_data)
    website.save()

    saved_website = Website.get_from_id(website_id)
    assert saved_website.website_id == website_id
    assert saved_website.description == "Sample website"
    assert saved_website.repo_name == "website_repo"
    assert saved_website.type == WebsiteType.FRONTEND

    # Cleanup
    website.delete()

# Test delete website
def test_delete_website():
    website_id = str(uuid.uuid4())
    website_data["website_id"] = website_id
    website = Website.create(website_data)
    website.delete()

    with pytest.raises(HTTPException) as excinfo:
        Website.get_from_id(website_id)

    assert excinfo.value.status_code == 404
    assert excinfo.value.detail == "Website not found"

# Test get website from ID not found
def test_get_from_id_not_found():
    website_id = str(uuid.uuid4())

    with pytest.raises(HTTPException) as excinfo:
        Website.get_from_id(website_id)

    assert excinfo.value.status_code == 404
    assert excinfo.value.detail == "Website not found"