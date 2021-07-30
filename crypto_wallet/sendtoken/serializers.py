from rest_framework import serializers 
from sendtoken.models import SendToken
 
 
class SendTokenSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = SendToken
        fields = ('id',
                  'sender_account',
                  'reciever_account',
                  'token',
                  'transaction_hash',
                  'user_id'
                  )
