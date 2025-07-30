import os
import requests
import time
from requests.exceptions import RequestException

FAYDA_TOKEN_URL = 'https://fayda-auth.nationalid.gov.et/token'
FAYDA_VERIFY_URL = 'https://fayda-api.nationalid.gov.et/verify'
CLIENT_ID = os.getenv('FAYDA_CLIENT_ID')
CLIENT_SECRET = os.getenv('FAYDA_CLIENT_SECRET')

_token_cache = {
    'access_token': None,
    'expires_at': 0,
}

def get_access_token():
    now = time.time()
    if _token_cache['access_token'] and _token_cache['expires_at'] > now:
        return _token_cache['access_token']
    data = {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    }
    try:
        resp = requests.post(FAYDA_TOKEN_URL, data=data)
        resp.raise_for_status()
        token_data = resp.json()
        _token_cache['access_token'] = token_data['access_token']
        _token_cache['expires_at'] = now + token_data.get('expires_in', 3600) - 60
        return _token_cache['access_token']
    except RequestException as e:
        raise Exception(f'Failed to get access token: {e}')

def get_national_id_data(fin):
    token = get_access_token()
    headers = {'Authorization': f'Bearer {token}'}
    payload = {'fin': fin}
    try:
        resp = requests.post(FAYDA_VERIFY_URL, json=payload, headers=headers)
        if resp.status_code == 429:
            raise Exception('API rate limit exceeded')
        if resp.status_code == 401:
            raise Exception('Authentication failed')
        if resp.status_code == 400:
            raise Exception('Invalid FIN')
        resp.raise_for_status()
        data = resp.json()
        return {
            'full_name': data.get('full_name'),
            'date_of_birth': data.get('date_of_birth'),
            'photo_url': data.get('photo_url'),
        }
    except RequestException as e:
        raise Exception(f'Failed to fetch National ID data: {e}')

def fetch_transaction_history(national_id):
    # Placeholder: Replace with actual DB/API call
    # Returns dict with keys: payment_history, credit_utilization, history_length, new_applications
    return {
        'payment_history': 0.9,  # 90% on-time
        'credit_utilization': 0.4,  # 40% utilization
        'history_length': 5,  # years
        'new_applications': 1,  # last year
    }

def calculate_credit_score(national_id):
    data = fetch_transaction_history(national_id)
    # Normalize factors
    payment_score = data['payment_history'] * 850
    utilization_score = (1 - data['credit_utilization']) * 850
    history_score = min(data['history_length'] / 10, 1) * 850
    new_app_score = max(1 - data['new_applications'] / 5, 0) * 850
    score = (
        payment_score * 0.5 +
        utilization_score * 0.3 +
        history_score * 0.15 +
        new_app_score * 0.05
    )
    return int(max(300, min(score, 850)))

def calculate_credit_limit(score):
    base_limit = 5000
    multiplier = 50
    limit = base_limit + score * multiplier
    return min(limit, 100000)

def update_credit_profile(national_id):
    score = calculate_credit_score(national_id)
    limit = calculate_credit_limit(score)
    # Placeholder: Save to DB (replace with ORM/model logic)
    # Example: Customer.objects.update_or_create(national_id=national_id, defaults={...})
    print(f"Updated profile for {national_id}: score={score}, limit={limit}")
    return {'score': score, 'limit': limit}
