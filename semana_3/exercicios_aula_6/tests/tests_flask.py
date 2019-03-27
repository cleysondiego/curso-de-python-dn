from app import app
from flask import url_for
from unittest import TestCase

class TestHome(TestCase):
    def setUp(self):
        self.app = app
        self.app.testing = True
        self.app_context = self.app.test_request_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def test_home_deve_retornar_sc_200(self):
        esperado = 200
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, esperado)
    
    def test_home_deve_retornar_ola_jovens(self):
        esperado = 'Olá jovens'
        response = self.client.get(url_for('home'))
        self.assertEqual(response.data.decode(), esperado)