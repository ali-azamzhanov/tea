from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import News, Menu, Home, About, Subject, History, Review, Gallery


class SearchApiTest(APITestCase):
    def setUp(self):
        News.objects.create(title='Посещение школы', body='Новость о школе', published_at='2025-10-01T12:00:00Z')
        News.objects.create(title='Успехи учеников', body='Технологии и результаты', published_at='2025-10-03T12:00:00Z')
        Menu.objects.create(title='Главная', url='/', order=1)
        Home.objects.create(title='Добро пожаловать', subtitle='В нашу школу', is_active=True)
        About.objects.create(title='О школе', description='Наша школа...')
        Subject.objects.create(title='Математика', description='Изучение математики', order=1)
        History.objects.create(year=2020, title='Основание школы', description='Школа была основана', order=1)
        Review.objects.create(name='Иван', text='Отличная школа', rating=5, is_active=True)
        Gallery.objects.create(title='Фото школы', description='Фото', order=1)

    def test_search_all_models(self):
        url = reverse('search') + '?q=школ'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('news', response.data['results'])

    def test_search_specific_model(self):
        url = reverse('search') + '?q=математика&model=subject'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']['subject']), 1)

    def test_search_without_q(self):
        url = reverse('search')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_news_list(self):
        url = reverse('news-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_home_list(self):
        url = reverse('home-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
