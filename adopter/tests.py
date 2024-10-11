from django.test import TestCase
from django.urls import reverse

from adopter.models import Adopter

class TestAdopterCreateNewAdopter(TestCase):
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
