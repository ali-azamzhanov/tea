"""
Схемы для стандартизации ответов API
"""
from drf_spectacular.utils import OpenApiExample


class ErrorResponseExamples:
    """Стандартные примеры ошибок"""
    
    UNAUTHORIZED = OpenApiExample(
        'Unauthorized',
        value={
            'code': 'NOT_AUTHENTICATED',
            'message': 'Not authenticated'
        }
    )
    
    FORBIDDEN = OpenApiExample(
        'Forbidden',
        value={
            'code': 'PERMISSION_DENIED',
            'message': 'You do not have permission to perform this action.'
        }
    )
    
    NOT_FOUND = OpenApiExample(
        'Not Found',
        value={
            'code': 'NOT_FOUND',
            'message': 'Not found'
        }
    )
    
    VALIDATION_ERROR = OpenApiExample(
        'Validation Error',
        value={
            'detail': [
                {
                    'loc': ['body', 'email'],
                    'msg': 'Enter a valid email address.',
                    'type': 'value_error'
                },
                {
                    'loc': ['body', 'name'],
                    'msg': 'This field is required.',
                    'type': 'value_error.missing'
                }
            ]
        }
    )
    
    BAD_REQUEST = OpenApiExample(
        'Bad Request',
        value={
            'code': 'BAD_REQUEST',
            'message': 'Invalid request'
        }
    )
    
    INTERNAL_SERVER_ERROR = OpenApiExample(
        'Internal Server Error',
        value={
            'code': 'UNKNOWN_ERROR',
            'message': 'Unknown error'
        }
    )
