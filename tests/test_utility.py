from dotenv import load_dotenv
load_dotenv(".env")

from fastapi.security import HTTPAuthorizationCredentials
from fastapi import status
import os

from src.TPL.utility.logging import logger
from src.TPL.utility.security import DecodedToken, verify_user, verify_admin
from src.TPL.test.get_token import get_test_user_id_token


def test_init_logger():
    assert logger != None

def test_verify_user_valid():
    id_token = get_test_user_id_token(os.environ.get("TESTBOT_ID"))
    bearer = HTTPAuthorizationCredentials(scheme="Bearer", credentials=id_token)
    decoded_token: DecodedToken = verify_user(bearer)
    assert decoded_token != None 
    assert decoded_token.user_id == os.environ.get("TESTBOT_ID")
    assert decoded_token.email == os.environ.get("TESTBOT_EMAIL")

def test_verify_user_invalid_token():
    id_token = get_test_user_id_token(os.environ.get("TESTBOT_ID"))
    id_token = id_token[:-1]
    bearer = HTTPAuthorizationCredentials(scheme="Bearer", credentials=id_token)
    try:
        verify_user(bearer)
        assert False
    except Exception as e:
        assert e.status_code == status.HTTP_401_UNAUTHORIZED

def test_verify_admin_valid():
    # is admin and valid token
    id_token = get_test_user_id_token(os.environ.get("TESTADMIN_ID"))
    bearer = HTTPAuthorizationCredentials(scheme="Bearer", credentials=id_token)
    decoded_token: DecodedToken = verify_admin(bearer)
    assert decoded_token != None 
    assert decoded_token.user_id == os.environ.get("TESTADMIN_ID")
    assert decoded_token.email == os.environ.get("TESTADMIN_EMAIL")

def test_verify_admin_invalid_token():
    # invalid token
    id_token = get_test_user_id_token(os.environ.get("TESTADMIN_ID"))
    id_token = id_token[:-1]
    bearer = HTTPAuthorizationCredentials(scheme="Bearer", credentials=id_token)
    try:
        verify_admin(bearer)
        assert False
    except Exception as e:
        assert e.status_code == status.HTTP_401_UNAUTHORIZED

def test_verify_admin_not_admin():       
    id_token = get_test_user_id_token()
    bearer = HTTPAuthorizationCredentials(scheme="Bearer", credentials=id_token)
    try:
        verify_admin(bearer)
        assert False
    except Exception as e:
        assert e.status_code == status.HTTP_401_UNAUTHORIZED