import os
import time
import requests
import jwt
from dotenv import load_dotenv

load_dotenv()

def get_user_info(fin: str):
    # Load environment variables
    CLIENT_ID = os.getenv('CLIENT_ID')
    TOKEN_ENDPOINT = os.getenv('TOKEN_ENDPOINT')
    USERINFO_ENDPOINT = os.getenv('USERINFO_ENDPOINT')
    PRIVATE_KEY = os.getenv('PRIVATE_KEY')
    ALGORITHM = os.getenv('ALGORITHM', 'RS256')
    EXPIRATION_TIME = int(os.getenv('EXPIRATION_TIME', '15'))
    CLIENT_ASSERTION_TYPE = os.getenv('CLIENT_ASSERTION_TYPE')

    # JWT client assertion payload
    now = int(time.time())
    payload = {
        'iss': CLIENT_ID,
        'sub': CLIENT_ID,
        'aud': TOKEN_ENDPOINT,
        'iat': now,
        'exp': now + EXPIRATION_TIME,
        'jti': str(now) + fin
    }
    client_assertion = jwt.encode(payload, PRIVATE_KEY, algorithm=ALGORITHM)

    # Token request
    data = {
        'grant_type': 'password',
        'client_id': CLIENT_ID,
        'client_assertion': client_assertion,
        'client_assertion_type': CLIENT_ASSERTION_TYPE,
        'username': fin,
        'password': fin,
        'scope': 'openid'
    }
    token_resp = requests.post(TOKEN_ENDPOINT, data=data)
    token_resp.raise_for_status()
    access_token = token_resp.json().get('access_token')
    if not access_token:
        raise Exception('No access_token in response')

    # User info request
    headers = {'Authorization': f'Bearer {access_token}'}
    userinfo_resp = requests.get(USERINFO_ENDPOINT, headers=headers)
    userinfo_resp.raise_for_status()
    return userinfo_resp.json()
