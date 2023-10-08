from django.test import TestCase
from django.shortcuts import resolve_url as r

from eventex.core.models import Speaker, Talk


class TalkListGet(TestCase):
    def setUp(self):
        t1 = Talk.objects.create(title='Titulo da Palestra', start='10:00', description='Descrição da palestra.')
        t2 = Talk.objects.create(title='Titulo da Palestra', start='13:00', description='Descrição da palestra.')
        speaker = Speaker.objects.create(
            name='Ricardo Pereira', 
            slug='ricardo-pereira',
            website='http://ricardopereira.net')
        t1.speakers.add(speaker)
        t2.speakers.add(speaker)
        self.response = self.client.get(r('talk_list'))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'core/talk_list.html')
    
    def test_html(self):
        contents = [
            (2, 'Titulo da Palestra'),
            (1, '10:00'),
            (1, '13:00'),
            (2, '/palestrantes/ricardo-pereira'),
            (2, 'Ricardo Pereira'),
            (2, 'Descrição da palestra')
        ]
        for count, expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected, count)

    def test_context(self):
        variables = ['morning_talks', 'afternoon_talks']
        for key in variables:
            with self.subTest():    
                self.assertIn(key, self.response.context)


class TalkListGetEmpty(TestCase):
    def test_get_empty(self):
        response = self.client.get(r('talk_list'))

        self.assertContains(response, 'Ainda não existem palestras de manhã.')
        self.assertContains(response, 'Ainda não existem palestras de tarde.')