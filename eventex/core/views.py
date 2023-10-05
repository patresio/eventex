from django.shortcuts import render

# Create your views here.
def home(request):
    speakers = [
        {'name': 'Grace Hopper', 'photo': 'https://encurtador.com.br/bsUVZ'},
        {'name': 'Alan Turing', 'photo': 'https://encurtador.com.br/uRUY5'}
    ]
    return render(request, 'index.html', {'speakers': speakers})
