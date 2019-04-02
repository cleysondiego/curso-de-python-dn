from unittest import TestCase

def get_users():
    return [('507', 'Jorge', 'jorgin_gatin@hotmail.com'), ('100', 'Cleyson', 'cleyson7@hotmail.com')]


def filter_users(tupla):
    for item in tupla:
        if int(item[0]) > 100:
            return item


class TestFilterUsers(TestCase):
    def test_filter_users_deve_retornar_apenas_quando_id_maior_que_100(self):
        esperado = ('507', 'Jorge', 'jorgin_gatin@hotmail.com')
        self.assertEqual(filter_users(get_users()), esperado)
