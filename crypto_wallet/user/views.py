from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view

from common.token import token_create, token_verify
 
from user.models import User
from user.serializers import UserSerializer, UserSerializerRead



# User Create
@api_view(['POST'])
def user_create(request):
    user_data = JSONParser().parse(request)
    user_serializer = UserSerializer(data=user_data)
    if user_serializer.is_valid():
        user_serializer.save()
        user_created = {
            "mobile": user_data['mobile']
            }
        return JsonResponse({"status":"succes","data": "user created"}, status=status.HTTP_201_CREATED) 
    return JsonResponse({"status":"error","error": user_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


# User Login
@api_view(['POST'])
def user_login(request):
    user_data = JSONParser().parse(request)
    print(user_data)
    user = User.objects.get(mobile=user_data['mobile'],password=user_data['password'])
    print(user.mobile)
    
    try:
        user = User.objects.get(mobile=user_data['mobile'],password=user_data['password'])
        # create token value
        claims = {
            'sub': user.id
        }
        return JsonResponse({"token": token_create(claims),"user_id": user.id}, status=status.HTTP_201_CREATED, safe=False) 
    except:
        return JsonResponse({"status":"error","error": "please check mobile and password"}, status=status.HTTP_400_BAD_REQUEST)



# User get
@api_view(['GET'])
def user_single_read(request, user_id):
    user = User.objects.filter(id=user_id) 
    user_serializer = UserSerializerRead(user, many=True) 
    return JsonResponse({"status":"succes","data": user_serializer.data}, safe=False) 



# user list
@api_view(['GET'])
@token_verify
def user_list_read(request):
    user_list = User.objects.all()
    user_serializer = UserSerializerRead(user_list, many=True) 
    return JsonResponse({"status":"succes","data": user_serializer.data}, safe=False)

