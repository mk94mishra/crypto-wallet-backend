from django.urls import path
from sendtoken import views 
 
urlpatterns = [ 
    # user create, read
    path('api/transaction', views.transaction_create, name='transaction_create'),
    #path('api/transaction/<int:user_id>', views.transaction_single_read, name='transaction_single_read')
]