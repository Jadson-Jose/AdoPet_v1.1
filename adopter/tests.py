from django.test import TestCase
from django.urls import reverse

from adopter.models import Adopter


class TestAdopterViewTest(TestCase):
    def test_create_new_adopter(self):
        data = {
            'name': 'Carlos',
            'email': 'carlos@example.com',
            'phone': '+5511999999999',
            'address': 'Rua 123',
            'number': '10',
            'neighborhood': 'Centro',
            'city': 'São Paulo',
            'state': 'SP',
            'cep': '12345678',
            'date_of_birth': '1980-01-01'
        }
        print(f"Dados enviados: {data}")
        response = self.client.post(reverse('create_adopter'), data)
        self.assertEqual(response.status_code, 302)
        print(f"Status da resposta: {response.status_code}")
        self.assertTrue(Adopter.objects.filter(name='Carlos').exists())


class AdopterListView(TestCase):

    def setUp(self):

        # Criando alguns adotantes no banco de dados de teste
        Adopter.objects.create(
            name='Carlos',
            email='carlos@example.com',
            phone='+5511999999999',
            address='Rua 123',
            number='10',
            complement='abc',
            neighborhood='Centro',
            city='São Paulo',
            state='SP',
            cep='12345678',
            date_of_birth='1980-01-01'
        )

    def test_adopter_lis_view(self):

        # Fazendo uma requisição GET para a URL da view 'adopter_list'
        response = self.client.get(reverse('adopter_list'))

        # Verificando quantos adostantes exisem no banco de dados no momento do teste
        print("Número de adotantes no banco durante o teste", Adopter.objects.count())

        # Verificando se o status da resposta é 200 (ok)
        self.assertEqual(response.status_code, 200)

        # Verificando se o template correto foi usado
        self.assertTemplateUsed(response, 'adopter_list.html')

        # Exibindo o contexto para depuração
        print("Contexto da resposta", response.context['adopters'])

        # Verificando se o contexto contém a lista de adotantes
        self.assertTrue('adopters' in response.context)

        # Verificando se os adotantes criados aparecem na lista
        self.assertEqual(len(response.context['adopters']), 1)
        self.assertContains(response, 'Jadson')
