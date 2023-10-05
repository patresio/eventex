from django.shortcuts import get_object_or_404, render

from eventex.core.models import Speaker


# Create your views here.
def home(request):
    speakers = [
        {'name': 'Grace Hopper', 'photo': 'https://encurtador.com.br/bsUVZ'},
        {'name': 'Alan Turing', 'photo': 'https://encurtador.com.br/uRUY5'}
    ]
    return render(request, 'index.html', {'speakers': speakers})


def speaker_detail(request, slug):
    speaker = get_object_or_404(Speaker, slug=slug)
    return render(request, 'core/speaker_detail.html', {'speaker': speaker})
