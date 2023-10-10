from django.urls import path

from eventex.core.views import talk_list, speaker_detail, home

urlpatterns = [
    path('', home, name='home'),
    path('palestras/', talk_list, name='talk_list'),
    path('palestrantes/<slug:slug>/', speaker_detail, name='speaker_detail'),
]