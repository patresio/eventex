from django.forms import ValidationError
from django.test import TestCase
from eventex.core.models import Speaker, Contact


class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Ricardo Pereira',
            slug='ricardo-pereira',
            photo='https://encurtador.com.br/abwFZ'
        )

    def test_email(self):
        contact = Contact.objects.create(
            speaker=self.speaker,
            kind=Contact.EMAIL,
            value='ricardo@pereira.net'
        )

        self.assertTrue(Contact.objects.exists())
    
    def test_phone(self):
        contact = Contact.objects.create(
            speaker=self.speaker,
            kind=Contact.PHONE,
            value='17988147723'
        )

        self.assertTrue(Contact.objects.exists())

    def test_choices(self):
        """ Contact king should be limited to E or P """
        contact = Contact(speaker=self.speaker, kind='A', value='B')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        contact = Contact(
            speaker=self.speaker,
            kind=Contact.EMAIL,
            value='ricardo@pereira.net'
        )
        self.assertEqual('ricardo@pereira.net', str(contact))


class ContactManagerTest(TestCase):
    def setUp(self):
        s = Speaker.objects.create(
            name='Ricardo Pereira',
            slug='ricardo-pereira',
            photo='http://rlbp.link',
        )

        s.contact_set.create(kind=Contact.EMAIL, value='ricardo@pereira.net')
        s.contact_set.create(kind=Contact.PHONE, value='17988147723')
    
    def test_emails(self):
        qs = Contact.objects.emails()
        expected = ['ricardo@pereira.net']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)

    def test_phone(self):
        qs = Contact.objects.phones()
        expected = ['17988147723']
        self.assertQuerySetEqual(qs, expected, lambda o: o.value)