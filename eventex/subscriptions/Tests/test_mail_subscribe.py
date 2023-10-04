from django.test import TestCase
from django.shortcuts import resolve_url as r
from django.core import mail


class SubscriptionPostValid(TestCase):
    def setUp(self):
        data = dict(name='Ricardo Pereira', cpf='12345678901', email='ricardo@pereira.net', phone='17-98814-7723')
        self.response = self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'noobemforma@gmail.com'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['noobemforma@gmail.com', 'ricardo@pereira.net']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Ricardo Pereira',
            '12345678901',
            'ricardo@pereira.net',
            '17-98814-7723'
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)