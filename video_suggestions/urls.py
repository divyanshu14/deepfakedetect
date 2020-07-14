from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('<int:id>/', views.VideoSuggestionView.as_view(), name='video_suggestion'),
]
