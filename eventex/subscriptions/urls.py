from django.urls import path
from . import views


urlpatterns = [
    path('', views.subscribe),
    path('<int:pk>/', views.detail),
]