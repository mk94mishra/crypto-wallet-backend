from django.urls import include, path

urlpatterns = [
    path('', include('user.urls')),
    path('', include('wallet.urls')),
    path('', include('sendtoken.urls'))
]