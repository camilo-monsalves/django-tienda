from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('registro/', views.registro, name='registro-usuario'),
    path('login/', views.custom_login, name='login-usuario'),
    path('logout/', views.custom_logout, name='logout-usuario'),
]