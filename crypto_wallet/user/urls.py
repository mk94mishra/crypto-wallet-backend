from django.urls import path
from user import views 
 
urlpatterns = [ 
    # user create, read
    path('api/user/signup', views.user_create, name='user_create'),
    path('api/user/login', views.user_login, name='user_login'),
    path('api/user/<int:user_id>', views.user_single_read, name='user_single_read'),
    path('api/user/list', views.user_list_read, name='user_list_read')
]