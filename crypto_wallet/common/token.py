import jwt
from time import time
import datetime
from django.conf import settings
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status


def token_create(payload):
    exp = (int(time()) + settings.TOKEN_VALIDITY_PERIOD)
    payload["exp"] = exp
    encoded_jwt = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
    return encoded_jwt

def token_decode(request):
    auth_header = request.headers.get('Authorization') 
    token = auth_header.split(" ")[1] # Parses out the "Bearer" portion
    payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
    return payload

def token_verify(func):
    def inner(request, *args, **kwargs):
        # check token from header
        auth_header = request.headers.get('Authorization') 

        if auth_header:
            token = auth_header.split(" ")[1] # Parses out the "Bearer" portion
            print(token)
        else:
            return JsonResponse({'message': 'Login Again!'}, status=status.HTTP_401_UNAUTHORIZED)

       # verify token
        try:
            claims = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            
        except:
            return JsonResponse({'message': 'Login Again!'}, status=status.HTTP_401_UNAUTHORIZED)

        return func(request, *args, **kwargs)
    return inner


def auth_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        print(response)
        return response

    return middleware