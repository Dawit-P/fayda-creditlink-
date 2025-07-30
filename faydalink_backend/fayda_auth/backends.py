# Custom authentication backend for Fayda OIDC
import jwt
import requests
from django.conf import settings
from django.contrib.auth import get_user_model

class FaydaOIDCAuthBackend:
    def authenticate(self, request, token=None):
        try:
            jwks_url = f"{settings.OIDC_OP_ISSUER}/.well-known/jwks.json"
            jwks_client = jwt.PyJWKClient(jwks_url)
            signing_key = jwks_client.get_signing_key_from_jwt(token)
            payload = jwt.decode(
                token,
                signing_key.key,
                algorithms=["RS256"],
                audience=settings.OIDC_RP_CLIENT_ID,
                issuer=settings.OIDC_OP_ISSUER
            )
            User = get_user_model()
            user, _ = User.objects.get_or_create(
                national_id=payload['nationalId'],
                defaults={
                    'username': payload['sub'],
                    'first_name': payload.get('given_name', ''),
                    'last_name': payload.get('family_name', '')
                }
            )
            return user
        except Exception as e:
            print(f"Authentication failed: {e}")
            return None
