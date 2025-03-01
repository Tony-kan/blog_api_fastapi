import jwt
import time
from config import get_settings

settings = get_settings()

def decodeJWT(token:str)->dict:
    try:
        decoded_token = jwt.decode(token,f'{settings.SECRET_KEY}',algorithms=['HS256'])
        return decoded_token if decoded_token['exp'] >= time.time() else None
    except jwt.ExpiredSignatureError:
        return None  # Token has expired
    except jwt.InvalidTokenError:
        return None  # Token is invalid