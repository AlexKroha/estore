# sendemail/urls.py
from django.contrib import admin
from django.urls import path

from .views import success_view

urlpatterns = [
    path('success/', success_view, name='success'),
]