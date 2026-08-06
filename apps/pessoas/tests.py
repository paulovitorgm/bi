from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from apps.pessoas.models import UnidadeDeLotacao


class UnidadeDeLotacaoModalTests(TestCase):
    def setUp(self):
        usuario = get_user_model().objects.create_user(
            username='teste',
            password='senha-segura',
        )
        self.client.force_login(usuario)

    def test_cria_unidade_e_retorna_opcao_para_o_formulario(self):
        response = self.client.post(
            reverse('modal_unidade_lotacao_criar'),
            {'sigla': 'FGA', 'nome': 'Faculdade do Gama'},
        )

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            response.content,
            {'id': UnidadeDeLotacao.objects.get().pk, 'text': 'FGA - Faculdade do Gama'},
        )

    def test_formulario_de_pessoa_exibe_atalho_para_nova_unidade(self):
        response = self.client.get(reverse('criar-pessoa'))

        self.assertContains(response, reverse('modal_unidade_lotacao_criar'))
