from django.contrib import admin
from django.utils.timezone import now

from eventex.subscriptions.models import Subscription


# Register your models here.

class SubscriptionModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'cpf', 'created_at', 'subscribe_today', 'paid')
    date_hierarchy = 'created_at'
    search_fields = ('name', 'email', 'phone', 'cpf', 'created_at')
    list_filter = ('paid', 'created_at')

    actions = ['mark_as_paid']

    def subscribe_today(self, obj):
        return obj.created_at == now().date()

    subscribe_today.short_description = 'Inscrito hoje?'
    subscribe_today.boolean = True

    def mark_as_paid(self, request, queryset):
        count = queryset.update(paid=True)
        if count == 1:
            msg = f'{count} inscrição foi marcada como paga.'
        else:
            msg = f'{count} inscrições foram marcadas como paga.'

        self.message_user(request, msg)

    mark_as_paid.short_description = 'Marcar como pago!'

admin.site.register(Subscription, SubscriptionModelAdmin)
