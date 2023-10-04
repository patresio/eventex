from django.urls import path
from . import views

app_name = 'subscriptions'

urlpatterns = [
    path('', views.new, name='new'),
    path('<int:pk>/', views.detail, name='detail'),
]