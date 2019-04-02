from app import app
from flask import url_for
from unittest import TestCase, mock

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

    def test_oi_deve_retornar_o_nome_passado(self):
        user = 'Cleyson'
        esperado = f'Olá {user}'
        response = self.client.get(url_for('oi', user=user))
        self.assertEqual(response.data.decode(), esperado)

    def test_create_book_deve_retornar_201(self):
        entrada = {'nome': 'Aprendendo Python', 'autor': 'Eduardo Mendes'}
        esperado = 201
        response = self.client.post(url_for('create_book'), json=entrada)
        self.assertEqual(response.status_code, esperado)

    @mock.patch('app.db.session.commit')
    def test_create_book_deve_chamar_book_com_json_correto(self, mocked_db):
        entrada = {'nome': 'Aprendendo Python', 'autor': 'Eduardo Mendes'}
        response = self.client.post(url_for('create_book'), json=entrada)

        mocked_db.assert_called()

        response.json.pop('id')

        self.assertEqual(entrada, response.json)

    def test_create_book_deve_retornar_com_dados_incorretos(self):
        entrada = {'nome': 'Aprendendo Python'}
        esperado = {'autor': ['Missing data for required field.']}
        response = self.client.post(url_for('create_book'), json=entrada)
        self.assertEqual(esperado, response.json)
