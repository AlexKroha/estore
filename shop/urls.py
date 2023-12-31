"""estore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path

from shop.views import *

urlpatterns = [
    path('', home, name='home'),
    path('category_list/', category_list, name='category_list'),
    re_path(r'(?P<id>\d+)/(?P<slug>[-\w]+)/$', product_detail, name='product_detail'),
    re_path(r'(?P<category_slug>[-\w]+)/$', product_list, name='product_list_by_category'),
]
