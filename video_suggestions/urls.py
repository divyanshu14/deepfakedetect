from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:id>/', views.VideoSuggestionView.as_view()),
]
