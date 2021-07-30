from common.transaction import get_balance
from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view
 
from wallet.models import Wallet
from wallet.serializers import WalletSerializer

from common.token import token_verify
from common.transaction import get_balance



# wallet Create
@api_view(['POST'])
def wallet_create(request):
    wallet_data = JSONParser().parse(request)
    wallet_serializer = WalletSerializer(data=wallet_data)
    if wallet_serializer.is_valid():
        wallet_serializer.save()
        wallet_created = {
            "account": wallet_data['account'],
            "balance": get_balance(wallet_data['account'])
            }
        return JsonResponse({"status":"succes","data": wallet_created}, status=status.HTTP_201_CREATED) 
    return JsonResponse({"status":"error","error": wallet_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# wallet get
@api_view(['GET'])
def wallet_single_read(request, user_id):
    wallet = Wallet.objects.filter(user_id=user_id) 
    wallet_serializer = WalletSerializer(wallet, many=True) 
    return JsonResponse({"status":"succes","data": wallet_serializer.data}, safe=False) 



# wallet get balance
@api_view(['GET'])
def wallet_balance(request, user_id):
    wallet = Wallet.objects.get(user_id=user_id) 
    balance = {
        "account":wallet.account,
        "balance": get_balance(wallet.account)
    }
    return JsonResponse({"status":"succes","data": balance}, safe=False) 




