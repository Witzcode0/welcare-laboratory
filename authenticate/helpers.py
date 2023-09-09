from django.conf import settings
import jwt
import string
import random

secret_key = settings.SECRET_KEY

def create_jwt_token(payload):
    """
    This function reaturn JWT token
    """
    return jwt.encode(payload, secret_key, algorithm='HS256')


# 
def generate_otp(length=6):
    """
    Generate a random OTP of a specified length (e.g., 6 characters)
    """
    characters = string.digits  # Use digits for OTP
    return ''.join(random.choice(characters) for _ in range(length))