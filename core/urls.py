from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.LIS,name="lis_view"),
    path('wis/',views.WIS,name="wis_view"),
]