from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r

from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


# Create your tests here.
class SubscriptionNewGet(TestCase):
    def setUp(self):
        self.response = self.client.get(r('subscriptions:new'))

    def test_get(self):
        '''Get /inscricao/ must response status code 200'''
        self.assertEquals(self.response.status_code, 200)

    def test_template(self):
        '''Template subscriptions/subscription_form.html '''
        # response = self.client.get('/inscricao/')
        self.assertTemplateUsed(self.response, 'subscriptions/subscription_form.html')

    def test_html(self):
        """Html must contain input tags"""
        tags = (
            ('<form', 1),
            ('<input', 6),
            ('type="text"', 3),
            ('type="email"', 1),
            ('type="submit"', 1)
        )

        # sourcery skip: no-loop-in-tests
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)

    def test_csrf(self):
        """Html must contain csrf"""
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """Context must have subscription form"""
        form = self.response.context['form']
        self.assertIsInstance(form, SubscriptionForm)


class SubscriptionNewPostValid(TestCase):
    def setUp(self):
        self.data = dict(name='Ricardo Pereira', cpf='12345678901', email='ricardo@pereira.net', phone='17-98814-7723')
        self.response = self.client.post(r('subscriptions:new'), self.data)

    def test_post(self):
        """ Valid POST should redirect to /inscricao/1/ """
        self.assertRedirects(self.response, r('subscriptions:detail', 1))

    def test_send_subscribe_email(self):
        """ Valid send email for subscribe """
        self.assertEqual(1, len(mail.outbox))

    def test_save_subscription(self):
        self.assertTrue(Subscription.objects.exists())


class SubscriptionNewPostInvalid(TestCase):
    def setUp(self):
        self.response = self.client.post(r('subscriptions:new'), {})

    def test_post(self):
        """Invalid POST should not redirect"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'subscriptions/subscription_form.html')

    def test_has_form(self):
        form = self.response.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_errors(self):
        form = self.response.context['form']
        self.assertTrue(form.errors)

    def test_dont_save_subscription(self):
        self.assertFalse(Subscription.objects.exists())


class TemplateRegressionTest(TestCase):
    def test_template_has_non_field_errors(self):
        invalid_data = dict(
            name='Ricardo Pereira',
            cpf='12345678901'
        )
        response = self.client.post(r('subscriptions:new'), invalid_data)
        self.assertContains(response, '<ul class="errorlist nonfield">')