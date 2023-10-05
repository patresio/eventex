from django.core import mail
from django.template.loader import render_to_string

from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, resolve_url as r

from eventex.subscriptions.forms import SubscriptionForm

from django.conf import settings

from eventex.subscriptions.models import Subscription


# Create your views here.
def new(request):
    return create(request) if request.method == 'POST' else empty_form(request)


def empty_form(request):
    return render(request, 'subscriptions/subscription_form.html', {'form': SubscriptionForm()})


def create(request):
    form = SubscriptionForm(request.POST)

    if not form.is_valid():
        return render(request, 'subscriptions/subscription_form.html', {'form': form})

    subscription = form.save()

    # Send subscription email
    _send_mail(
        'Confirmação de inscrição',
        settings.DEFAULT_FROM_EMAIL,
        subscription.email,
        'subscriptions/subscription_email.txt',
        {'subscription': subscription})

    return HttpResponseRedirect(r('subscriptions:detail', subscription.pk))


def detail(request, pk):
    try:
        subscription = Subscription.objects.get(pk=pk)
    except Subscription.DoesNotExist as e:
        raise Http404 from e
    return render(request, 'subscriptions/subscription_detail.html', {'subscription': subscription})


def _send_mail(subject, from_, to, template_name, context):
    body = render_to_string(template_name, context)
    mail.send_mail(subject, body, from_, [from_, to])
