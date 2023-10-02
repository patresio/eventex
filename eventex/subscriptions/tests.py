from django.core import mail
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm

# Create your tests here.
class SubscribeTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/inscricao/')

    def test_get(self):
        '''Get /inscricao/ must response status code 200'''
        self.assertEquals(self.response.status_code, 200)

    def test_template(self):
        '''Template subscriptions/subscription_form.html '''
        #response = self.client.get('/inscricao/')
        self.assertTemplateUsed(self.response, 'subscriptions/subscription_form.html')


    def test_html(self):
        """Html must contain input tags"""
        self.assertContains(self.response, '<form')
        self.assertContains(self.response, '<input', 6)
        self.assertContains(self.response, 'type="text"', 3)
        self.assertContains(self.response, 'type="email"')
        self.assertContains(self.response, 'type="submit"')

    def test_csrf(self):
        """Html must contain csrf"""
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """Context must have subscription form"""
        form = self.response.context['form']
        self.assertIsInstance(form, SubscriptionForm)
    
    def test_form_has_field(self):
        """Form must have 4 fields"""
        form = self.response.context['form']
        self.assertSequenceEqual(['name', 'cpf', 'email', 'phone'], list(form.fields))
    

class SubscriptionPostTest(TestCase):
    def setUp(self):
        data = dict(name='Ricardo Pereira', cpf='12345678901', email='ricardo@pereira.net', phone='17-98814-7723')
        self.response = self.client.post('/inscricao/', data)
    
    def test_post(self):
        """ Valid POST should redirect to /inscricao/ """
        self.assertEqual(self.response.status_code, 302)

    def test_send_subscribe_email(self):
        """ Valid send email for subscribe """
        self.assertEqual(1, len(mail.outbox))
    
    def test_subscription_email_subject(self):
        email = mail.outbox[0]
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, email.subject)

    def test_subscription_email_from(self):
        email = mail.outbox[0]
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, email.from_email)

    def test_subscription_email_to(self):
        email = mail.outbox[0]
        expect = ['contato@eventex.com.br', 'ricardo@pereira.net']

        self.assertEqual(expect, email.to)

    def test_subscription_email_body(self):
        email = mail.outbox[0]

        self.assertIn('Ricardo Pereira', email.body)
        self.assertIn('12345678901', email.body)
        self.assertIn('ricardo@pereira.net', email.body)
        self.assertIn('17-98814-7723', email.body)
        

class SubscribeInvalidPost(TestCase):
    def setUp(self):
        self.response = self.client.post('/inscricao/', {})
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

class SubscribeSucessMessage(TestCase):
    def test_message(self):
        data = dict(name='Ricardo Pereira', cpf='12345678901', email='ricardo@pereira.net', phone='17-98814-7723')
        response = self.client.post('/inscricao/', data, follow=True)
        self.assertContains(response, 'Inscrição realizada com sucesso!')