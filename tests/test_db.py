from src.TPL.db.config import db
from src.TPL.utility.logging import logger
from src.TPL.db.user import User
import os



def test_init_db():
    print(os.environ.get("TPL_FIREBASE_AUTH"))
    assert db != None

def test_init_logger():
    assert logger != None

def test_user():
    user = User.get_from_username("Braeden6")
    assert user.fname == "Braeden"
    user = User.get("EkKx1XhMYtUahLhRpOmpdqKO9Oo2")
    assert user.fname == "Braeden"