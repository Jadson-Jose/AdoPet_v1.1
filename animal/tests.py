from django.test import TestCase
from django.urls import reverse
from .models import Animal


class AnimalListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        # Cria alguns animais no banco de dados de teste
        Animal.objects.create(name='Cachorro', age=3, raca='Labrador')
        Animal.objects.create(name="Gato", age=2, raca="Siames")

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('animal_list/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('list'))

    def test_view_lists_all_animals(self):
        response = self.client.get(reverse('list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Cachorro")
        self.assertContains(response, "Gato")
