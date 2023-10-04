from django.urls import path
from . import views


urlpatterns = [
    path('', views.subscribe),
    path('<str:id>/', views.detail),
]