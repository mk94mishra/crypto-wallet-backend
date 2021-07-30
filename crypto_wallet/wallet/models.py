from django.db import models
from user.models import User



class Wallet(models.Model):
    account = models.CharField(max_length=200, blank=False)
    private_key = models.CharField(max_length=200,blank=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
	    db_table = 'tbl_wallet'