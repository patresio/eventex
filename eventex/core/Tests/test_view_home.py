from django.test import TestCase
from django.shortcuts import resolve_url as r


class HomeTest(TestCase):
    fixtures=['keynotes.json']
    def setUp(self):
        self.response = self.client.get(r('home'))

    def test_get(self):
        '''GET / must return status code 200'''
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        '''Must use index.html'''
        self.assertTemplateUsed(self.response, 'index.html')

    def test_subscription_link(self):
        expected = f"""href="{r('subscriptions:new')}\""""
        self.assertContains(self.response, expected)

    def test_speakers(self):
        """Must show keynote speakers"""
        contents = [
            'href="{}"'.format(r('speaker_detail', slug='grace-hopper')),
            'Grace Hopper',
            'https://encurtador.com.br/bsUVZ',
            'href="{}"'.format(r('speaker_detail', slug='alan-turing')),
            'Alan Turing',
            'https://encurtador.com.br/cvI39'
        ]

        for expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected)

    def test_speakers_link(self):  # sourcery skip: use-fstring-for-formatting
        expected = 'href="{}#speakers"'.format(r('home'))
        self.assertContains(self.response, expected)

    def test_talks_link(self):  # sourcery skip: use-fstring-for-formatting
        expected = 'href="{}'.format(r('talk_list'))
        self.assertContains(self.response, expected)