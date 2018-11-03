from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.SearchView.as_view(), name="search"),
    path('api/', views.search_api, name="search_api"),

]
