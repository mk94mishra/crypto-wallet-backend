from django.db import models


class User(models.Model):
    name = models.CharField(max_length=70, blank=False)
    mobile = models.CharField(max_length=20,blank=False, unique=True)
    password = models.CharField(max_length=200,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
	    db_table = 'tbl_user'
