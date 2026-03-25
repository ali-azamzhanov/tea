import re

from django.db import connection
from django.db.models import Q
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import News, Program, UsefulLink
from .serializers import NewsSerializer, ProgramSerializer, UsefulLinkSerializer


class NewsListCreateView(generics.ListCreateAPIView):
    queryset = News.objects.order_by('-published_at')
    serializer_class = NewsSerializer
    permission_classes = [AllowAny]


class ProgramListCreateView(generics.ListCreateAPIView):
    queryset = Program.objects.order_by('-created_at')
    serializer_class = ProgramSerializer
    permission_classes = [AllowAny]


class UsefulLinkListCreateView(generics.ListCreateAPIView):
    queryset = UsefulLink.objects.order_by('-created_at')
    serializer_class = UsefulLinkSerializer
    permission_classes = [AllowAny]


class ModelSearchView(APIView):
    permission_classes = [AllowAny]

    _models = {
        'news': (News, NewsSerializer, ['title', 'body']),
        'program': (Program, ProgramSerializer, ['name', 'description']),
        'usefullink': (UsefulLink, UsefulLinkSerializer, ['title', 'description']),
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
