from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserCreate.as_view(), name='account-create'),
    path('login/', views.UserLogin.as_view(), name='account-login'),
]

