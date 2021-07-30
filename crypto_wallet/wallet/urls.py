from django.urls import path
from wallet import views 
 
urlpatterns = [ 
    # user create, read
    path('api/wallet', views.wallet_create, name='wallet_create'),
    path('api/wallet/<int:user_id>', views.wallet_single_read, name='wallet_single_read'),
    path('api/wallet/balance/<int:user_id>', views.wallet_balance, name='wallet_balance')
]