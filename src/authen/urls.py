from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import AuthView, logoutView

urlpatterns = [
    path('', AuthView.as_view(), name='auth'),
    path('logout/', logoutView, name='logout'),

]