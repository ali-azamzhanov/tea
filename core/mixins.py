"""
Миксины для стандартизации ответов API
"""
from rest_framework import status
from drf_spectacular.utils import OpenApiResponse, OpenApiExample
from drf_spectacular.types import OpenApiTypes


class StandardResponseMixin:
    """Миксин для стандартизации ответов API"""
    
    @staticmethod
    def get_error_responses():
        """Стандартные примеры ошибок для Swagger"""
        return {
            status.HTTP_400_BAD_REQUEST: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                description='Bad Request',
                examples=[
                    OpenApiExample(
                        'Validation Error',
                        value={
                            'detail': 'Invalid input data',
                            'errors': {
                                'field_name': ['This field is required.']
                            }
                        }
                    )
                ]
            ),
            status.HTTP_403_FORBIDDEN: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                description='Forbidden',
                examples=[
                    OpenApiExample(
                        'Permission Denied',
                        value={
                            'detail': 'You do not have permission to perform this action.'
                        }
                    )
                ]
            ),
            status.HTTP_404_NOT_FOUND: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                description='Not Found',
                examples=[
                    OpenApiExample(
                        'Not Found',
                        value={
                            'detail': 'Not found.'
                        }
                    )
                ]
            ),
            status.HTTP_500_INTERNAL_SERVER_ERROR: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                description='Internal Server Error',
                examples=[
                    OpenApiExample(
                        'Server Error',
                        value={
                            'detail': 'A server error occurred.'
                        }
                    )
                ]
            ),
        }
    
    @staticmethod
    def get_success_responses(serializer_class, description='Success'):
        """Стандартные примеры успешных ответов"""
        return {
            status.HTTP_200_OK: OpenApiResponse(
                response=serializer_class,
                description=description,
            ),
            status.HTTP_201_CREATED: OpenApiResponse(
                response=serializer_class,
                description='Created successfully',
            ),
        }
