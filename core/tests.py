from django.test import TestCase, SimpleTestCase

class CoreViewTeste(SimpleTestCase):
    def test_index_200(self):
        resposta= self.client.get("/")
        self.assertEqual(resposta.status_code, 200)

    def test_index_titulo(self):
        resposta = self.client.get("/")
        self.assertEqual(resposta.context["titulo"], "Outro Título")

    def test_contato_200(self):
        resposta= self.client.get("/contato/")
        self.assertEqual(resposta.status_code, 200)

    def test_contato_titulo(self):
        resposta = self.client.get("/contato/")
        self.assertEqual(resposta.context["titulo"], "Contato")


'''
    def test_index_template(self):
        resposta = self.client.get("/")
        self.assertTemplateUsed(self, resposta, 'index.html')
        '''