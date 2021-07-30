import json
from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view


from wallet.models import Wallet
from sendtoken.models import SendToken
from sendtoken.serializers import SendTokenSerializer
from common.transaction import transaction_init
from common.token import token_verify, token_decode



# transaction Create
@api_view(['POST'])
@token_verify
def transaction_create(request):
    request_data = JSONParser().parse(request)
    # get user id by decode token
    payload = token_decode(request)
    user_id = payload['sub']
    sender_data = Wallet.objects.filter(user_id=int(user_id)).order_by('-user_id')
    
    try:
        sender_data = Wallet.objects.get(user_id=user_id) 
        
        transaction_hash = transaction_init(sender_data.account, sender_data.private_key, request_data['reciever_account'], request_data['token'])

        transaction_data = {
            'sender_account':sender_data.account,
            'reciever_account':request_data['reciever_account'],
            'token': request_data['token'],
            'transaction_hash': transaction_hash,
            'user_id': user_id
        }
        transaction_serializer = SendTokenSerializer(data=transaction_data)
        if transaction_serializer.is_valid():
            transaction_serializer.save()

            transaction_created = {
                "account": transaction_data['sender_account'],
                "transaction_hash":transaction_hash,
                }
            return JsonResponse({"status":"succes","data": transaction_created},safe=False, status=status.HTTP_201_CREATED) 
        return JsonResponse({"status":"error","error": transaction_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except:
        return JsonResponse({"status":"error","error": "does not exist!"}, status=status.HTTP_400_BAD_REQUEST)
