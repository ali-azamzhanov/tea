from django.urls import path

from .views import ModelSearchView, NewsListCreateView, ProgramListCreateView, UsefulLinkListCreateView

urlpatterns = [
    path('search/', ModelSearchView.as_view(), name='home-street-search'),
    path('news/', NewsListCreateView.as_view(), name='news-list-create'),
    path('programs/', ProgramListCreateView.as_view(), name='program-list-create'),
    path('useful-links/', UsefulLinkListCreateView.as_view(), name='useful-links-list-create'),
]
