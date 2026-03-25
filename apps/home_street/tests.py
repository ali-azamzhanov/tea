from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import News, Program, UsefulLink


class SearchApiTest(APITestCase):
    def setUp(self):
        News.objects.create(title='Посещение школы', body='Новость о школе', published_at='2025-10-01T12:00:00Z')
        News.objects.create(title='Успехи учеников', body='Технологии и результаты', published_at='2025-10-03T12:00:00Z')
        Program.objects.create(name='Математика', description='Программа углублённого обучения')
        Program.objects.create(name='Английский язык', description='Новая интенсивная программа')
        UsefulLink.objects.create(title='E-Bilim', url='https://ebilim.kg', description='Ссылка на электронную библиотеку')

    def test_search_all_models(self):
        url = reverse('home-street-search') + '?q=школ'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('news', response.data['results'])

    def test_search_specific_model(self):
        url = reverse('home-street-search') + '?q=математика&model=program'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']['program']), 1)

    def test_search_without_q(self):
        url = reverse('home-street-search')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_search_specific_usefullink(self):
        url = reverse('home-street-search') + '?q=ebilim&model=usefullink'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']['usefullink']), 1)

    def test_usefullink_list(self):
        url = reverse('useful-links-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
