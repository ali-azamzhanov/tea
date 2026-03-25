import re

from django.db import connection
from django.db.models import Q
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import (
    News, Menu, Settings, Home, About, AboutExtra,
    Subject, SubjectSection, History, Review, Gallery, HeaderFooterSettings
)
from .serializers import (
    NewsSerializer, MenuSerializer, SettingsSerializer, HomeSerializer,
    AboutSerializer, AboutExtraSerializer, SubjectSerializer, SubjectSectionSerializer,
    HistorySerializer, ReviewSerializer, GallerySerializer, HeaderFooterSettingsSerializer
)


class NewsListCreateView(generics.ListCreateAPIView):
    queryset = News.objects.order_by('-published_at')
    serializer_class = NewsSerializer
    permission_classes = [AllowAny]


class NewsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [AllowAny]


class MenuListCreateView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [AllowAny]


class MenuDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [AllowAny]


class SettingsDetailView(generics.RetrieveUpdateAPIView):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer
    permission_classes = [AllowAny]


class HomeListCreateView(generics.ListCreateAPIView):
    queryset = Home.objects.filter(is_active=True)
    serializer_class = HomeSerializer
    permission_classes = [AllowAny]


class HomeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer
    permission_classes = [AllowAny]


class AboutListCreateView(generics.ListCreateAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    permission_classes = [AllowAny]


class AboutDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    permission_classes = [AllowAny]


class AboutExtraListCreateView(generics.ListCreateAPIView):
    queryset = AboutExtra.objects.all()
    serializer_class = AboutExtraSerializer
    permission_classes = [AllowAny]


class AboutExtraDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AboutExtra.objects.all()
    serializer_class = AboutExtraSerializer
    permission_classes = [AllowAny]


class SubjectListCreateView(generics.ListCreateAPIView):
    queryset = Subject.objects.order_by('order')
    serializer_class = SubjectSerializer
    permission_classes = [AllowAny]


class SubjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [AllowAny]


class SubjectSectionListCreateView(generics.ListCreateAPIView):
    queryset = SubjectSection.objects.all()
    serializer_class = SubjectSectionSerializer
    permission_classes = [AllowAny]


class SubjectSectionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubjectSection.objects.all()
    serializer_class = SubjectSectionSerializer
    permission_classes = [AllowAny]


class HistoryListCreateView(generics.ListCreateAPIView):
    queryset = History.objects.order_by('order')
    serializer_class = HistorySerializer
    permission_classes = [AllowAny]


class HistoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
    permission_classes = [AllowAny]


class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.filter(is_active=True).order_by('-created_at')
    serializer_class = ReviewSerializer
    permission_classes = [AllowAny]


class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [AllowAny]


class GalleryListCreateView(generics.ListCreateAPIView):
    queryset = Gallery.objects.order_by('order')
    serializer_class = GallerySerializer
    permission_classes = [AllowAny]


class GalleryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    permission_classes = [AllowAny]


class HeaderFooterSettingsListCreateView(generics.ListCreateAPIView):
    queryset = HeaderFooterSettings.objects.all()
    serializer_class = HeaderFooterSettingsSerializer
    permission_classes = [AllowAny]


class HeaderFooterSettingsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HeaderFooterSettings.objects.all()
    serializer_class = HeaderFooterSettingsSerializer
    permission_classes = [AllowAny]


class ModelSearchView(APIView):
    permission_classes = [AllowAny]

    _models = {
        'news': (News, NewsSerializer, ['title', 'body']),
        'menu': (Menu, MenuSerializer, ['title']),
        'home': (Home, HomeSerializer, ['title', 'subtitle']),
        'about': (About, AboutSerializer, ['title', 'description']),
        'aboutextra': (AboutExtra, AboutExtraSerializer, ['title', 'description']),
        'subject': (Subject, SubjectSerializer, ['title', 'description']),
        'subjectsection': (SubjectSection, SubjectSectionSerializer, ['title']),
        'history': (History, HistorySerializer, ['title', 'description']),
        'review': (Review, ReviewSerializer, ['name', 'text']),
        'gallery': (Gallery, GallerySerializer, ['title', 'description']),
    }

    @staticmethod
    def _build_query(fields, q):
        q_obj = Q()
        q_obj |= Q(pk__isnull=True) 

        for field in fields:
            q_obj |= Q(**{f"{field}__icontains": q})

        return q_obj

    @staticmethod
    def _normalize_text(text: str) -> str:
        text = str(text).casefold()
        return re.sub(r'[^0-9a-zа-яё]+', '', text)

    @staticmethod
    def _fallback_filter(model_cls, fields, q):
        q_norm = ModelSearchView._normalize_text(q)
        results = []
        for obj in model_cls.objects.all():
            for field in fields:
                value = getattr(obj, field, '') or ''
                value_norm = ModelSearchView._normalize_text(value)
                if q_norm in value_norm:
                    results.append(obj)
                    break
        return results

    def get(self, request):
        q = request.query_params.get('q', '').strip()
        model_name = request.query_params.get('model', '').strip().lower()

        if not q:
            return Response(
                {'detail': 'Query parameter "q" is required for search.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if model_name and model_name not in self._models:
            return Response(
                {
                    'detail': f'Model not supported for search: {model_name}. '
                    f'Choose one of {list(self._models)}.'
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        targets = [(model_name, self._models[model_name])] if model_name else self._models.items()

        results = {}
        for name, (model_cls, serializer_cls, fields) in targets:
            if connection.vendor == 'sqlite':
                queryset = self._fallback_filter(model_cls, fields, q)
            else:
                queryset = model_cls.objects.filter(self._build_query(fields, q))

            if isinstance(queryset, list):
                serializer = serializer_cls(queryset, many=True)
                results[name] = serializer.data
            else:
                results[name] = serializer_cls(queryset, many=True).data

        return Response({'query': q, 'model': model_name or 'all', 'results': results})
