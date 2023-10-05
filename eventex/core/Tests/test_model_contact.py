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