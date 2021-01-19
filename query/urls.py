from django.contrib import admin
from django.urls import path, include
from . import views
from .views import SearchResults

urlpatterns = [
    path('', views.home, name='query-home'),
    path('search/', views.SearchResults, name='searchResults'),
    path('about/', views.About, name='about'),
    path('<str:nickname>/', views.details, name='details'),
]
