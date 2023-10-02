from django.core import mail
from django.template.loader import render_to_string

from django.contrib import messages

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import  render

from eventex.subscriptions.forms import SubscriptionForm

# Create your views here.
def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)

        if not form.is_valid():
            return render(request, 'subscriptions/subscription_form.html', {'form': form})

        body = render_to_string('subscriptions/subscription_email.txt', form.cleaned_data)
        mail.send_mail('Confirmação de inscrição', body, 'noobemforma@gmail.com', ['noobemforma@gmail.com', form.cleaned_data['email']])
        messages.success(request, 'Inscrição realizada com sucesso!')
        return HttpResponseRedirect('/inscricao/')
    context = {'form': SubscriptionForm()}
    return render(request, 'subscriptions/subscription_form.html', context)
