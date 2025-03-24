from django.test import TestCase

class Test__horoscope(TestCase):
    def test__index(self):
        responce = self.client.get('/horoscope/')
        self.assertEqual(responce.status_code, 200)

    def test__libra(self):
        responce = self.client.get('/horoscope/libra/')
        self.assertEqual(responce.status_code, 200)
        self.assertIn('libra. Ищите гармонию в отношениях.', responce.content.decode())

    def test_redirect__libra(self):
        responce = self.client.get('/horoscope/7/')
        self.assertEqual(responce.status_code, 302)
        self.assertEqual(responce.url, '/horoscope/libra/')