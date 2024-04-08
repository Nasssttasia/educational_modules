from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from main.models import Module
from users.models import User


class ModuleTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            email='test@mail.ru',
            name='Nastya',
            is_active=True,
            is_staff=True,
            is_superuser=True,
        )

        self.main = Module.objects.create(
            num=1,
            title='text',
            description='text',
        )
        self.main.save()
        self.client.force_authenticate(user=self.user)

    def test_create_module(self):
        """Тест создания модуля"""

        module = {
            'id': 2,
            'num': 2,
            'title': 'text2',
            'description': 'text2',
        }

        response = self.client.post(
            reverse('main:module-create'),
            data=module
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(
            response.json(),
            {'id': 2, 'num': 2, 'title': 'text2', 'description': 'text2'}
        )
        self.assertTrue(
            Module.objects.all().exists()
        )

        response = self.client.get(
            '/module/',
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_list_module(self):
        """Тест вывода списка модулей"""
        response = self.client.get(
            reverse('main:module-list'),
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(),
            {'count': 1, 'next': None, 'previous': None, 'results': [{'description': 'text', 'id': 4, 'num': 1, 'title': 'text'}]}

        )

    def test_update_module(self):
        """Тест изменения модуля"""

        module = {
            'id': 1,
            'num': 1,
            'title': 'text3',
            'description': 'text3',
        }

        response = self.client.put(
            reverse('main:module-update', args=[self.main.pk]),
            data=module,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'id': 6, 'num': 1, 'title': 'text3', 'description': 'text3'}
        )

    def test_retrieve_module(self):
        """Тест просмотра модуля"""
        response = self.client.get(
            reverse('main:module-retrieve', args=[self.main.pk]),
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_module(self):
        """Тест удаления модуля"""
        response = self.client.delete(
            reverse('main:module-delete', args=[self.main.pk]),
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

