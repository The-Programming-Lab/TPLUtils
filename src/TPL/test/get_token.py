import pyrebase
from firebase_admin import credentials, auth
import firebase_admin
import os


firebase_config = {
    "apiKey": os.environ.get("TEST_FIREBASE_API_KEY"),
    "authDomain": os.environ.get("TEST_FIREBASE_AUTH_DOMAIN"),
    "databaseURL": os.environ.get("TEST_FIREBASE_DATABASE_URL"),
    "storageBucket": os.environ.get("TEST_FIREBASE_STORAGE_BUCKET"),
}

firebase = pyrebase.initialize_app(firebase_config)

# Initialize the Firebase Admin SDK
if not firebase_admin._apps:
    cred = credentials.Certificate(os.environ.get("TPL_FIREBASE_AUTH"))
    firebase_admin.initialize_app(cred)

def get_test_user_id_token(user_id: str = os.environ.get("TESTBOT_ID")):
    # Generate a custom token for the test user
    custom_token = auth.create_custom_token(user_id).decode('utf-8')

    # Exchange the custom token for an ID token
    user = firebase.auth().sign_in_with_custom_token(custom_token)
    id_token = user['idToken']
    return id_token