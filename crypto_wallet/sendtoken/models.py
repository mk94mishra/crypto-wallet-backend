from django.db import models
from user.models import User



class SendToken(models.Model):
    sender_account = models.CharField(max_length=200, blank=False)
    reciever_account = models.CharField(max_length=200, blank=False)
    token = models.FloatField(blank=False)
    transaction_hash = models.CharField(max_length=200, blank=False)

    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
	    db_table = 'tbl_send_token'