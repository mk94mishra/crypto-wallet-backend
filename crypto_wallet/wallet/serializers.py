from rest_framework import serializers 
from wallet.models import Wallet
 
 
class WalletSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Wallet
        fields = ('id',
                  'account',
                  'private_key',
                  'user_id')
