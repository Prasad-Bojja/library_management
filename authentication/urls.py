from django.contrib import admin
from django.urls import path
from .views import*




# authentication/urls.py

urlpatterns = [

    path('user_list/',user_list,name='user_list'),
    path('user_create/', user_create, name='user_create'),
    path('user_update/<int:user_id>/', user_update, name='user_update'),
    path('user_delete/<int:user_id>/', user_delete, name='user_delete'),
    path('login/', login_form, name='login_form'),
    path('change-password/<int:user_id>/', change_password, name='change_password'),
    path('profile/<int:user_id>/',profile_page,name='profile'),
    path('profile_update/<int:user_id>/',profile_update,name='profile_update'),
    path('logout/',logout_page,name='logout')
]
