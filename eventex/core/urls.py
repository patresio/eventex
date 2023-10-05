from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.home, name='home'),
    path('palestrantes/<slug:slug>/', v.speaker_detail, name='speaker_detail'),
]