from datetime import datetime

from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Ricardo Pereira',
            cpf='12345678901',
            email='ricardo@pereira.net',
            phone='17-988147723'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription must have an auto created_at att."""
        self.assertIsInstance(self.obj.created_at, datetime)
