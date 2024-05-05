"""
URL configuration for qrmenu_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include, re_path
from core import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api/places/', views.PlaceList.as_view()),
    path('api/places/<pk>', views.PlaceDetail.as_view()),
    path('api/categories/', views.CategoryList.as_view()),
    path('api/categories/<pk>', views.CategoryDetail.as_view()),
    path('api/menu_items/', views.MenuItemList.as_view()),
    path('api/menu_items/<pk>', views.MenuItemDetail.as_view()),
    path('api/orders/', views.OrderList.as_view()),
    path('api/orders/<pk>', views.OrderDetail.as_view()),
    path('api/create_payment_intent/', views.create_payment_intent),
    re_path('', views.home),
]
